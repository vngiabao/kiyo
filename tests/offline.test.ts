import { afterEach, beforeAll, expect, it, vi } from "vitest";
import { clipUrls, savedClipCount, saveAllAudio, saveDictionary, savedShardCount } from "../src/offline";
import { loadAudioCatalog } from "../src/audio-catalog";

vi.mock("../src/audio-assets.json", () => ({ default: {
  a: { clear: "/audio/a.mp3", cool: "/audio/a.mp3" },
  b: { clear: "/audio/b.mp3" }, c: { clear: "/audio/c.mp3" },
} }));
afterEach(() => vi.unstubAllGlobals());
// The catalogue loads lazily in the app; load the mocked one before clipUrls() is read.
beforeAll(() => loadAudioCatalog());
const audio = () => new Response(new Uint8Array([73, 68, 51]), { headers: { "content-type": "audio/mpeg" } });
function setup(saved = 2) {
  vi.stubGlobal("location", { origin: "https://kiyo.example" });
  const urls = clipUrls();
  const entries = new Map(urls.slice(0, saved).map((url) => [url, audio()]));
  const cache = {
    match: vi.fn(async (url: string) => entries.get(url)?.clone()),
    put: vi.fn(async (url: string, response: Response) => { entries.set(url, response); }),
    keys: vi.fn(() => { throw new Error("Must not enumerate the full cache"); }),
  };
  vi.stubGlobal("caches", { open: async () => cache });
  const fetch = vi.fn(async () => audio());
  vi.stubGlobal("fetch", fetch);
  return { cache, entries, fetch, urls };
}

it("deduplicates URLs and counts only audio, without enumerating cache keys", async () => {
  const { entries, urls } = setup();
  entries.set(urls[0], new Response("Sign in", { headers: { "content-type": "text/html" } }));
  expect(urls).toHaveLength(3);
  expect(await savedClipCount()).toBe(1);
});
it("rejects login HTML and keeps failed clips out of the saved count", async () => {
  const { fetch, cache } = setup();
  fetch.mockImplementation(async () => new Response("Sign in", { headers: { "content-type": "text/html" } }));
  const progress = vi.fn();
  expect(await saveAllAudio(progress)).toEqual({ total: 3, saved: 2, failed: 1, cancelled: false });
  expect(cache.put).not.toHaveBeenCalled();
  expect(progress).toHaveBeenLastCalledWith(2, 3);
  expect(fetch).toHaveBeenCalledOnce();
});
it("resumes only missing clips and verifies their cache retention", async () => {
  const { fetch, cache } = setup();
  expect((await saveAllAudio(() => undefined)).saved).toBe(3);
  expect(cache.put).toHaveBeenCalledOnce();
  await saveAllAudio(() => undefined);
  expect(fetch).toHaveBeenCalledOnce();
});
it("retries network and transient server failures, but not a missing file", async () => {
  const { fetch } = setup();
  fetch.mockRejectedValueOnce(new TypeError("Disconnected"))
    .mockResolvedValueOnce(new Response("Busy", { status: 503 }));
  expect((await saveAllAudio(() => undefined)).failed).toBe(0);
  expect(fetch).toHaveBeenCalledTimes(3);
  const fresh = setup();
  fresh.fetch.mockResolvedValue(new Response("Missing", { status: 404 }));
  expect((await saveAllAudio(() => undefined)).failed).toBe(1);
  expect(fresh.fetch).toHaveBeenCalledOnce();
});
it("reports cancellation instead of claiming a complete download", async () => {
  const { fetch } = setup();
  const controller = new AbortController();
  fetch.mockImplementation(async () => { controller.abort(); throw new DOMException("Stopped", "AbortError"); });
  expect(await saveAllAudio(() => undefined, controller.signal))
    .toEqual({ total: 3, saved: 2, failed: 0, cancelled: true });
});
it("keeps existing clips and surfaces storage exhaustion after workers settle", async () => {
  const { cache, entries } = setup();
  cache.put.mockRejectedValue(new DOMException("Full", "QuotaExceededError"));
  await expect(saveAllAudio(() => undefined)).rejects.toThrow("no room");
  expect(entries.size).toBe(2);
});
it("does not count a cache write that was immediately evicted", async () => {
  const { cache } = setup();
  cache.put.mockImplementation(async () => undefined);
  expect((await saveAllAudio(() => undefined)).saved).toBe(2);
  expect((await saveAllAudio(() => undefined)).failed).toBe(1);
});
it("keeps HTML and failed dictionary downloads out of saved progress", async () => {
  const { fetch, entries } = setup(0);
  entries.set("https://kiyo.example/dict/000.json", new Response("Login", { headers: { "content-type": "text/html" } }));
  fetch.mockResolvedValue(new Response("Unavailable", { status: 503 }));
  const progress = vi.fn();
  expect(await savedShardCount(2)).toBe(0);
  expect(await saveDictionary(2, progress)).toEqual({ failed: 2, cancelled: false });
  expect(progress).toHaveBeenLastCalledWith(0);
});
it("resumes retained dictionary shards and reports a stopped download", async () => {
  const { entries, fetch } = setup(0);
  entries.set("https://kiyo.example/dict/000.json", new Response("[]", { headers: { "content-type": "application/json" } }));
  const controller = new AbortController();
  fetch.mockImplementation(async () => { controller.abort(); throw new DOMException("Stopped", "AbortError"); });
  expect(await saveDictionary(2, () => undefined, controller.signal)).toEqual({ failed: 0, cancelled: true });
  expect(await savedShardCount(2)).toBe(1);
});
