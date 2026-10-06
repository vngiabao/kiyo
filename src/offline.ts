/**
 * Long-term storage on this device.
 * - Sayo's clips are cached the first time each plays (see vite.config.ts,
 *   cache "sayo-audio"); `saveAllAudio` fills the same cache in one go.
 * - Persistent storage asks the browser not to evict this site's data
 *   (IndexedDB included) when the disk runs low.
 */
import assets from "./audio-assets.json";

export const AUDIO_CACHE = "sayo-audio";

/** Every installed clip, once. */
export function clipUrls(): string[] {
  const urls = Object.values(
    assets as Record<string, Record<string, string>>,
  ).flatMap((moods) => Object.values(moods));
  return [...new Set(urls)].map((u) => new URL(u, location.origin).href);
}

export async function savedClipCount(): Promise<number> {
  if (typeof caches === "undefined") return 0;
  const cache = await caches.open(AUDIO_CACHE);
  const have = new Set((await cache.keys()).map((r) => r.url));
  return clipUrls().filter((u) => have.has(u)).length;
}

/** Download every clip not yet cached. Resumable: already-saved clips are skipped. */
export async function saveAllAudio(
  onProgress: (done: number, total: number) => void,
  signal?: AbortSignal,
) {
  if (typeof caches === "undefined")
    throw new Error("This browser can’t store audio for offline use.");
  const cache = await caches.open(AUDIO_CACHE);
  const have = new Set((await cache.keys()).map((r) => r.url));
  const all = clipUrls();
  const todo = all.filter((u) => !have.has(u));
  let done = all.length - todo.length,
    failed = 0;
  onProgress(done, all.length);
  const worker = async () => {
    while (todo.length && !signal?.aborted) {
      const url = todo.shift()!;
      try {
        const res = await fetch(url, { signal });
        // Access redirects and SPA fallbacks can return HTML with status 200.
        if (res.ok && /^audio\//i.test(res.headers.get("content-type") ?? ""))
          await cache.put(url, res);
        else failed++;
      } catch {
        if (signal?.aborted) return;
        failed++;
      }
      onProgress(++done, all.length);
    }
  };
  await Promise.all(Array.from({ length: 6 }, worker));
  return { total: all.length, failed };
}

export type StorageInfo = {
  persisted: boolean | null;
  usedMB: number | null;
  quotaMB: number | null;
};
export async function storageInfo(): Promise<StorageInfo> {
  const s = navigator.storage;
  const [persisted, est] = await Promise.all([
    s?.persisted?.() ?? null,
    s?.estimate?.() ?? null,
  ]);
  return {
    persisted,
    usedMB: est?.usage != null ? Math.round(est.usage / 1e5) / 10 : null,
    quotaMB: est?.quota != null ? Math.round(est.quota / 1e6) : null,
  };
}
/** Ask once the learner has real progress worth keeping. Browsers may grant silently or decline. */
export async function askPersistentStorage(): Promise<boolean | null> {
  try {
    return (await navigator.storage?.persist?.()) ?? null;
  } catch {
    return null;
  }
}

// ---------- Dictionary ----------
export const DICT_CACHE = "kiyo-dict";
export interface DictManifest {
  shards: number;
  entries: number;
  bytes: number;
  gzipBytes: number;
  version: string;
  attribution: string;
  license: string;
}
const shardUrl = (i: number) => new URL(`/dict/${String(i).padStart(3, "0")}.json`, location.origin).href;
export async function dictManifest(): Promise<DictManifest | null> {
  try {
    const res = await fetch("/dict/manifest.json");
    return res.ok && /json/i.test(res.headers.get("content-type") ?? "") ? ((await res.json()) as DictManifest) : null;
  } catch {
    return null;
  }
}
export async function savedShardCount(shards: number): Promise<number> {
  if (typeof caches === "undefined") return 0;
  const have = new Set((await (await caches.open(DICT_CACHE)).keys()).map((r) => r.url));
  return Array.from({ length: shards }, (_, i) => shardUrl(i)).filter((u) => have.has(u)).length;
}
/** Download every dictionary shard not yet cached (resumable, like the audio). */
export async function saveDictionary(shards: number, onProgress: (done: number) => void, signal?: AbortSignal) {
  if (typeof caches === "undefined") throw new Error("This browser can’t store the dictionary for offline use.");
  const cache = await caches.open(DICT_CACHE);
  const have = new Set((await cache.keys()).map((r) => r.url));
  const todo = Array.from({ length: shards }, (_, i) => shardUrl(i)).filter((u) => !have.has(u));
  let done = shards - todo.length,
    failed = 0;
  onProgress(done);
  const worker = async () => {
    while (todo.length && !signal?.aborted) {
      const url = todo.shift()!;
      try {
        const res = await fetch(url, { signal });
        if (res.ok && /json/i.test(res.headers.get("content-type") ?? "")) await cache.put(url, res);
        else failed++;
      } catch {
        if (signal?.aborted) return;
        failed++;
      }
      onProgress(++done);
    }
  };
  await Promise.all(Array.from({ length: 4 }, worker));
  return { failed };
}
