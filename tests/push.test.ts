import { afterEach, expect, it, vi } from "vitest";
import { b64url, encryptPayload, handlePushApi, isDue, localNow, sendDueNotes, vapidHeader, type KV } from "../workers/push";

const enc = new TextEncoder();
// Copies keep every buffer a plain ArrayBuffer, which WebCrypto's types require.
async function hmac(key: Uint8Array, data: Uint8Array) {
  const k = await crypto.subtle.importKey("raw", new Uint8Array(key), { name: "HMAC", hash: "SHA-256" }, false, ["sign"]);
  return new Uint8Array(await crypto.subtle.sign("HMAC", k, new Uint8Array(data)));
}
const cat = (...p: Uint8Array[]) => { const o = new Uint8Array(p.reduce((n, x) => n + x.length, 0)); let i = 0; for (const x of p) { o.set(x, i); i += x.length; } return o; };

/** A browser's side of RFC 8291: decrypt with the subscription's private key. */
async function browserDecrypt(body: Uint8Array, uaKeys: CryptoKeyPair, auth: Uint8Array) {
  const salt = body.slice(0, 16), idlen = body[20], asPublic = body.slice(21, 21 + idlen), cipher = body.slice(21 + idlen);
  const uaPublic = new Uint8Array(await crypto.subtle.exportKey("raw", uaKeys.publicKey));
  const asKey = await crypto.subtle.importKey("raw", asPublic, { name: "ECDH", namedCurve: "P-256" }, false, []);
  const ecdh = new Uint8Array(await crypto.subtle.deriveBits({ name: "ECDH", public: asKey }, uaKeys.privateKey, 256));
  const ikm = await hmac(await hmac(auth, ecdh), cat(enc.encode("WebPush: info\0"), uaPublic, asPublic, new Uint8Array([1])));
  const prk = await hmac(salt, ikm);
  const cek = (await hmac(prk, cat(enc.encode("Content-Encoding: aes128gcm\0"), new Uint8Array([1])))).slice(0, 16);
  const nonce = (await hmac(prk, cat(enc.encode("Content-Encoding: nonce\0"), new Uint8Array([1])))).slice(0, 12);
  const key = await crypto.subtle.importKey("raw", cek, "AES-GCM", false, ["decrypt"]);
  return new Uint8Array(await crypto.subtle.decrypt({ name: "AES-GCM", iv: nonce }, key, cipher));
}
async function device() {
  const ua = (await crypto.subtle.generateKey({ name: "ECDH", namedCurve: "P-256" }, true, ["deriveBits"])) as CryptoKeyPair;
  const auth = crypto.getRandomValues(new Uint8Array(16));
  const p256dh = b64url.encode(new Uint8Array(await crypto.subtle.exportKey("raw", ua.publicKey)));
  return { ua, auth, sub: { endpoint: "https://push.example.com/send/abc", keys: { p256dh, auth: b64url.encode(auth) } } };
}
async function vapidKeys() {
  const k = (await crypto.subtle.generateKey({ name: "ECDSA", namedCurve: "P-256" }, true, ["sign", "verify"])) as CryptoKeyPair;
  return { k, pub: b64url.encode(new Uint8Array(await crypto.subtle.exportKey("raw", k.publicKey))), jwk: await crypto.subtle.exportKey("jwk", k.privateKey) };
}
function memoryKV(): KV & { data: Map<string, string> } {
  const data = new Map<string, string>();
  return {
    data,
    async get(k) { return data.get(k) ?? null; },
    async put(k, v) { data.set(k, v); },
    async delete(k) { data.delete(k); },
    async list({ prefix }) { return { keys: [...data.keys()].filter((k) => k.startsWith(prefix)).map((name) => ({ name })), list_complete: true }; },
  };
}
afterEach(() => vi.unstubAllGlobals());

it("encrypts a push a browser can decrypt (RFC 8291 aes128gcm)", async () => {
  const d = await device();
  const body = await encryptPayload(d.sub, enc.encode(JSON.stringify({ kind: "daily" })));
  expect(new DataView(body.buffer).getUint32(16)).toBe(4096);
  const plain = await browserDecrypt(body, d.ua, d.auth);
  expect(plain.at(-1)).toBe(2); // last-record delimiter
  expect(JSON.parse(new TextDecoder().decode(plain.slice(0, -1)))).toEqual({ kind: "daily" });
});

it("signs a VAPID token the push service can verify (RFC 8292)", async () => {
  const v = await vapidKeys();
  const header = await vapidHeader("https://web.push.apple.com/abc", v.pub, v.jwk, Date.UTC(2026, 9, 30));
  const [, t, k] = header.match(/^vapid t=([^,]+), k=(.+)$/)!;
  expect(k).toBe(v.pub);
  const [h, c, s] = t.split(".");
  expect(JSON.parse(new TextDecoder().decode(b64url.decode(c))).aud).toBe("https://web.push.apple.com");
  expect(await crypto.subtle.verify({ name: "ECDSA", hash: "SHA-256" }, v.k.publicKey, b64url.decode(s), enc.encode(`${h}.${c}`))).toBe(true);
});

it("is due once a day, at or up to two hours after the chosen local time", () => {
  const at = (iso: string) => new Date(iso);
  const s = { time: "20:00", tz: "America/Detroit" };
  expect(localNow("America/Detroit", at("2026-10-31T00:07:00Z")).time).toBe("20:07");
  expect(isDue(s, at("2026-10-31T00:07:00Z"))).toBe(true); // 20:07 in Detroit
  expect(isDue(s, at("2026-10-30T23:59:00Z"))).toBe(false); // 19:59
  expect(isDue(s, at("2026-10-31T02:30:00Z"))).toBe(false); // 22:30: too late, wait for tomorrow
  expect(isDue({ ...s, lastSent: "2026-10-30" }, at("2026-10-31T00:07:00Z"))).toBe(false); // already sent today
});

it("stores, sends to and forgets a subscription; a gone device is removed", async () => {
  const v = await vapidKeys();
  const d = await device();
  const env = { PUSH: memoryKV(), VAPID_PUBLIC: v.pub, VAPID_PRIVATE_JWK: JSON.stringify(v.jwk) };
  const post = (path: string, body: object) => handlePushApi(new Request(`https://kiyo.test${path}`, { method: "POST", body: JSON.stringify(body) }), env);
  expect((await post("/api/push/subscribe", { subscription: d.sub, time: "20:00", tz: "America/Detroit" })).status).toBe(200);
  expect((await post("/api/push/subscribe", { subscription: d.sub, time: "25:00", tz: "America/Detroit" })).status).toBe(400);
  expect(env.PUSH.data.size).toBe(1);
  const fetch = vi.fn(async () => new Response(null, { status: 201 }));
  vi.stubGlobal("fetch", fetch);
  expect(await sendDueNotes(env, new Date("2026-10-31T00:07:00Z"))).toEqual({ sent: 1, removed: 0 });
  expect(await sendDueNotes(env, new Date("2026-10-31T00:22:00Z"))).toEqual({ sent: 0, removed: 0 }); // once a day
  const [, init] = fetch.mock.calls[0] as unknown as [string, RequestInit];
  expect((init.headers as Record<string, string>)["Content-Encoding"]).toBe("aes128gcm");
  fetch.mockImplementation(async () => new Response(null, { status: 410 }));
  expect(await sendDueNotes(env, new Date("2026-11-01T00:07:00Z"))).toEqual({ sent: 0, removed: 1 });
  expect(env.PUSH.data.size).toBe(0);
  expect((await post("/api/push/unsubscribe", { endpoint: d.sub.endpoint })).status).toBe(200);
});
