// Sayo's evening note: Web Push from the Worker, no third-party service.
// - The app stores one subscription per device in KV with the learner's chosen time and zone.
// - A cron every 15 minutes sends each due device one encrypted push a day (RFC 8291/8292).
// - The push carries no learning data; the device's service worker decides what Sayo says
//   from its own local progress (public/push-sw.js).
// Requests reach /api/* only through Cloudflare Access, like the rest of the site.

export type KV = {
  get(key: string): Promise<string | null>;
  put(key: string, value: string): Promise<void>;
  delete(key: string): Promise<void>;
  list(options: { prefix: string; cursor?: string }): Promise<{ keys: { name: string }[]; list_complete: boolean; cursor?: string }>;
};
export type PushEnvironment = { PUSH?: KV; VAPID_PUBLIC?: string; VAPID_PRIVATE_JWK?: string };
export type PushSubscriptionJSON = { endpoint: string; keys: { p256dh: string; auth: string } };
type Stored = { subscription: PushSubscriptionJSON; time: string; tz: string; lastSent?: string; createdAt: number };

const enc = new TextEncoder();
export const b64url = {
  encode(bytes: Uint8Array) {
    let s = "";
    for (const b of bytes) s += String.fromCharCode(b);
    return btoa(s).replace(/\+/g, "-").replace(/\//g, "_").replace(/=+$/, "");
  },
  decode(text: string) {
    const s = atob(text.replace(/-/g, "+").replace(/_/g, "/") + "===".slice((text.length + 3) % 4));
    return Uint8Array.from(s, (c) => c.charCodeAt(0));
  },
};
const concat = (...parts: Uint8Array[]) => {
  const out = new Uint8Array(parts.reduce((n, p) => n + p.length, 0));
  let o = 0;
  for (const p of parts) { out.set(p, o); o += p.length; }
  return out;
};
// Copies keep every buffer a plain ArrayBuffer, which WebCrypto's types require.
async function hmac(key: Uint8Array, data: Uint8Array) {
  const k = await crypto.subtle.importKey("raw", new Uint8Array(key), { name: "HMAC", hash: "SHA-256" }, false, ["sign"]);
  return new Uint8Array(await crypto.subtle.sign("HMAC", k, new Uint8Array(data)));
}

/** RFC 8291 aes128gcm encryption of `payload` for one subscription. */
export async function encryptPayload(sub: PushSubscriptionJSON, payload: Uint8Array) {
  const uaPublic = b64url.decode(sub.keys.p256dh);
  const authSecret = b64url.decode(sub.keys.auth);
  const local = (await crypto.subtle.generateKey({ name: "ECDH", namedCurve: "P-256" }, true, ["deriveBits"])) as CryptoKeyPair;
  const asPublic = new Uint8Array(await crypto.subtle.exportKey("raw", local.publicKey));
  const uaKey = await crypto.subtle.importKey("raw", uaPublic, { name: "ECDH", namedCurve: "P-256" }, false, []);
  const ecdh = new Uint8Array(await crypto.subtle.deriveBits({ name: "ECDH", public: uaKey }, local.privateKey, 256));
  const prkKey = await hmac(authSecret, ecdh);
  const ikm = await hmac(prkKey, concat(enc.encode("WebPush: info\0"), uaPublic, asPublic, new Uint8Array([1])));
  const salt = crypto.getRandomValues(new Uint8Array(16));
  const prk = await hmac(salt, ikm);
  const cek = (await hmac(prk, concat(enc.encode("Content-Encoding: aes128gcm\0"), new Uint8Array([1])))).slice(0, 16);
  const nonce = (await hmac(prk, concat(enc.encode("Content-Encoding: nonce\0"), new Uint8Array([1])))).slice(0, 12);
  const key = await crypto.subtle.importKey("raw", cek, "AES-GCM", false, ["encrypt"]);
  const cipher = new Uint8Array(await crypto.subtle.encrypt({ name: "AES-GCM", iv: nonce }, key, concat(payload, new Uint8Array([2]))));
  const header = new Uint8Array(21 + asPublic.length);
  header.set(salt, 0);
  new DataView(header.buffer).setUint32(16, 4096);
  header[20] = asPublic.length;
  header.set(asPublic, 21);
  return concat(header, cipher);
}

/** RFC 8292 VAPID header for one push service origin. */
export async function vapidHeader(endpoint: string, publicKey: string, privateJwk: JsonWebKey, now = Date.now()) {
  const aud = new URL(endpoint).origin;
  const part = (o: object) => b64url.encode(enc.encode(JSON.stringify(o)));
  const unsigned = `${part({ typ: "JWT", alg: "ES256" })}.${part({ aud, exp: Math.floor(now / 1000) + 12 * 3600, sub: "https://kiyo.gbaonvo.com" })}`;
  const key = await crypto.subtle.importKey("jwk", privateJwk, { name: "ECDSA", namedCurve: "P-256" }, false, ["sign"]);
  const sig = new Uint8Array(await crypto.subtle.sign({ name: "ECDSA", hash: "SHA-256" }, key, enc.encode(unsigned)));
  return `vapid t=${unsigned}.${b64url.encode(sig)}, k=${publicKey}`;
}

export async function sendPush(env: PushEnvironment, sub: PushSubscriptionJSON, message: object) {
  if (!env.VAPID_PUBLIC || !env.VAPID_PRIVATE_JWK) throw new Error("Push keys are not configured");
  const body = await encryptPayload(sub, enc.encode(JSON.stringify(message)));
  return fetch(sub.endpoint, {
    method: "POST",
    headers: {
      Authorization: await vapidHeader(sub.endpoint, env.VAPID_PUBLIC, JSON.parse(env.VAPID_PRIVATE_JWK)),
      "Content-Encoding": "aes128gcm",
      "Content-Type": "application/octet-stream",
      TTL: String(6 * 3600),
      Urgency: "normal",
    },
    body,
  });
}

const keyFor = async (endpoint: string) =>
  "sub:" + b64url.encode(new Uint8Array(await crypto.subtle.digest("SHA-256", enc.encode(endpoint)))).slice(0, 32);
const json = (data: unknown, status = 200) =>
  new Response(JSON.stringify(data), { status, headers: { "Content-Type": "application/json", "Cache-Control": "no-store" } });
const validTime = (t: unknown): t is string => typeof t === "string" && /^([01]\d|2[0-3]):[0-5]\d$/.test(t);
const validSub = (s: unknown): s is PushSubscriptionJSON => {
  const v = s as PushSubscriptionJSON | undefined;
  return !!v && typeof v.endpoint === "string" && /^https:\/\//.test(v.endpoint) && typeof v.keys?.p256dh === "string" && typeof v.keys?.auth === "string";
};

/** Local date and HH:MM in an IANA zone. */
export function localNow(tz: string, now = new Date()) {
  const parts = Object.fromEntries(
    new Intl.DateTimeFormat("en-CA", { timeZone: tz, year: "numeric", month: "2-digit", day: "2-digit", hour: "2-digit", minute: "2-digit", hourCycle: "h23" })
      .formatToParts(now).map((p) => [p.type, p.value]),
  );
  return { day: `${parts.year}-${parts.month}-${parts.day}`, time: `${parts.hour}:${parts.minute}` };
}

/** Is a device due: today's note not sent yet and its time reached within the last two hours. */
export function isDue(s: Pick<Stored, "time" | "tz" | "lastSent">, now = new Date()) {
  const { day, time } = localNow(s.tz, now);
  if (s.lastSent === day) return false;
  const minutes = (t: string) => Number(t.slice(0, 2)) * 60 + Number(t.slice(3));
  const late = minutes(time) - minutes(s.time);
  return late >= 0 && late < 120;
}

const ready = (env: PushEnvironment): env is Required<PushEnvironment> => Boolean(env.PUSH && env.VAPID_PUBLIC && env.VAPID_PRIVATE_JWK);

export async function handlePushApi(request: Request, env: PushEnvironment): Promise<Response> {
  const path = new URL(request.url).pathname;
  // No key until the server can really send, so the app offers the calendar instead.
  if (path === "/api/push/key") return json({ key: ready(env) ? env.VAPID_PUBLIC : null });
  if (!env.PUSH) return json({ error: "Reminders are not set up on this server" }, 503);
  if (request.method !== "POST") return json({ error: "POST only" }, 405);
  let body: { subscription?: unknown; time?: unknown; tz?: unknown; endpoint?: unknown };
  try { body = await request.json(); } catch { return json({ error: "Invalid JSON" }, 400); }
  if (path === "/api/push/subscribe") {
    if (!validSub(body.subscription) || !validTime(body.time) || typeof body.tz !== "string") return json({ error: "Invalid subscription" }, 400);
    try { localNow(body.tz); } catch { return json({ error: "Unknown time zone" }, 400); }
    const key = await keyFor(body.subscription.endpoint);
    const old = await env.PUSH.get(key);
    const stored: Stored = { subscription: body.subscription, time: body.time, tz: body.tz, createdAt: Date.now(), lastSent: old ? (JSON.parse(old) as Stored).lastSent : undefined };
    await env.PUSH.put(key, JSON.stringify(stored));
    return json({ ok: true });
  }
  if (path === "/api/push/unsubscribe") {
    if (typeof body.endpoint !== "string") return json({ error: "Missing endpoint" }, 400);
    await env.PUSH.delete(await keyFor(body.endpoint));
    return json({ ok: true });
  }
  if (path === "/api/push/test") {
    if (typeof body.endpoint !== "string") return json({ error: "Missing endpoint" }, 400);
    const raw = await env.PUSH.get(await keyFor(body.endpoint));
    if (!raw) return json({ error: "This device is not subscribed" }, 404);
    const res = await sendPush(env, (JSON.parse(raw) as Stored).subscription, { kind: "test" });
    return json({ ok: res.ok, status: res.status }, res.ok ? 200 : 502);
  }
  return json({ error: "Not found" }, 404);
}

/** Cron: one note per device per day, at or just after its chosen time. */
export async function sendDueNotes(env: PushEnvironment, now = new Date()) {
  if (!ready(env)) return { sent: 0, removed: 0 };
  let sent = 0, removed = 0, cursor: string | undefined;
  do {
    const page = await env.PUSH.list({ prefix: "sub:", cursor });
    for (const { name } of page.keys) {
      const raw = await env.PUSH.get(name);
      if (!raw) continue;
      const s = JSON.parse(raw) as Stored;
      if (!isDue(s, now)) continue;
      // One unreachable push service must not stop the rest of the run.
      const res = await sendPush(env, s.subscription, { kind: "daily" }).catch(() => null);
      if (!res) continue;
      if (res.status === 404 || res.status === 410) { await env.PUSH.delete(name); removed++; continue; }
      if (res.ok) { s.lastSent = localNow(s.tz, now).day; await env.PUSH.put(name, JSON.stringify(s)); sent++; }
    }
    cursor = page.list_complete ? undefined : page.cursor;
  } while (cursor);
  return { sent, removed };
}
