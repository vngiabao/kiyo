/**
 * Long-term storage on this device.
 * - Sayo's clips are cached the first time each plays (see vite.config.ts,
 *   cache "sayo-audio"); `saveAllAudio` fills the same cache in one go.
 * - Persistent storage asks the browser not to evict this site's data
 *   (IndexedDB included) when the disk runs low.
 */
import { audioCatalog, loadAudioCatalog } from "./audio-catalog";

export const AUDIO_CACHE = "sayo-audio";

/** Every installed clip, once. Empty until the catalogue has loaded (see loadClipUrls). */
export function clipUrls(): string[] {
  const urls = Object.values(audioCatalog() ?? {}).flatMap((moods) => Object.values(moods));
  return [...new Set(urls)].map((u) => new URL(u, location.origin).href);
}

/** Every installed clip, once, loading the catalogue first if needed. */
export async function loadClipUrls(): Promise<string[]> {
  await loadAudioCatalog();
  return clipUrls();
}

export async function savedClipCount(): Promise<number> {
  if (typeof caches === "undefined") return 0;
  const cache = await caches.open(AUDIO_CACHE);
  return (await missingClips(cache, await loadClipUrls())).saved;
}

const isAudio = (res: Response | undefined) => !!res?.ok && /^audio\//i.test(res.headers.get("content-type") ?? "");

// Match in bounded groups: enumerating tens of thousands of cache keys allocates
// the whole inventory at once and can exceed browser/automation response limits.
async function missingClips(cache: Cache, urls: string[], signal?: AbortSignal) {
  const missing: string[] = [];
  let saved = 0;
  for (let start = 0; start < urls.length && !signal?.aborted; start += 24) {
    const group = urls.slice(start, start + 24);
    const matches = await Promise.all(group.map((url) => cache.match(url)));
    matches.forEach((res, i) => isAudio(res) ? saved++ : missing.push(group[i]));
  }
  return { missing, saved };
}

/** Download every clip not yet cached. Resumable: already-saved clips are skipped. */
export async function saveAllAudio(
  onProgress: (done: number, total: number) => void,
  signal?: AbortSignal,
) {
  if (typeof caches === "undefined")
    throw new Error("This browser can’t store audio for offline use.");
  const cache = await caches.open(AUDIO_CACHE);
  const all = await loadClipUrls();
  const { missing: todo, saved } = await missingClips(cache, all, signal);
  let done = saved, failed = 0, cursor = 0;
  let storageError: Error | undefined;
  onProgress(done, all.length);
  const worker = async () => {
    while (cursor < todo.length && !signal?.aborted && !storageError) {
      const url = todo[cursor++];
      let stored = false;
      for (let attempt = 0; attempt < 3 && !signal?.aborted && !storageError; attempt++) {
        let res: Response;
        try {
          res = await fetch(url, { signal });
        } catch {
          if (signal?.aborted) return;
          continue;
        }
        if (!isAudio(res)) {
          // Retry transient server failures, never login HTML or missing files.
          if (res.status === 429 || res.status >= 500) continue;
          break;
        }
        try {
          await cache.put(url, res);
          stored = isAudio(await cache.match(url));
          if (stored) break;
        } catch (e) {
          storageError = new Error(e instanceof Error && e.name === "QuotaExceededError"
            ? "This device has no room for more audio. Saved clips are kept; free some space and resume."
            : "The browser couldn’t save audio. Saved clips are kept; check available storage and resume.");
        }
      }
      if (signal?.aborted) return;
      if (stored) onProgress(++done, all.length);
      else failed++;
    }
  };
  await Promise.all(Array.from({ length: 6 }, worker));
  if (storageError) throw storageError;
  return { total: all.length, saved: done, failed, cancelled: !!signal?.aborted };
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
  const cache = await caches.open(DICT_CACHE);
  let saved = 0;
  for (let i = 0; i < shards; i++) if (isJson(await cache.match(shardUrl(i)))) saved++;
  return saved;
}
const isJson = (response?: Response) => !!response?.ok && /json/i.test(response.headers.get("content-type") ?? "");
/** Download every dictionary shard not yet cached (resumable, like the audio). */
export async function saveDictionary(shards: number, onProgress: (done: number) => void, signal?: AbortSignal) {
  if (typeof caches === "undefined") throw new Error("This browser can’t store the dictionary for offline use.");
  const cache = await caches.open(DICT_CACHE);
  const todo: string[] = [];
  for (let i = 0; i < shards; i++) if (!isJson(await cache.match(shardUrl(i)))) todo.push(shardUrl(i));
  let done = shards - todo.length,
    failed = 0;
  onProgress(done);
  const worker = async () => {
    while (todo.length && !signal?.aborted) {
      const url = todo.shift()!;
      try {
        const res = await fetch(url, { signal });
        if (isJson(res)) {
          await cache.put(url, res);
          if (isJson(await cache.match(url))) onProgress(++done);
          else failed++;
        } else failed++;
      } catch {
        if (signal?.aborted) return;
        failed++;
      }
    }
  };
  await Promise.all(Array.from({ length: 4 }, worker));
  return { failed, cancelled: !!signal?.aborted };
}
