import { useEffect, useState } from "react";

// Sayo's clip catalogue (text → mood → URL) is ~2.3 MB of data. It is loaded on its own
// right after the first screen paints, not as part of the first download; nothing needs
// it until the first sound plays. Playback is synchronous once it has arrived.
export type AudioCatalog = Record<string, Record<string, string>>;

let catalog: AudioCatalog | null = null;
let loading: Promise<AudioCatalog> | null = null;
const listeners = new Set<() => void>();

export const audioCatalog = () => catalog;

export function loadAudioCatalog(): Promise<AudioCatalog> {
  loading ??= import("./audio-assets.json").then(
    (m) => {
      catalog = m.default as unknown as AudioCatalog;
      listeners.forEach((l) => l());
      return catalog;
    },
    (error) => {
      loading = null; // allow a retry, e.g. once back online
      throw error;
    },
  );
  return loading;
}

export function onAudioCatalog(listener: () => void) {
  listeners.add(listener);
  return () => void listeners.delete(listener);
}

/** Re-render once the catalogue is in, starting the load if nothing has yet. */
export function useAudioCatalogReady() {
  const [ready, setReady] = useState(() => catalog !== null);
  useEffect(() => {
    if (catalog) return setReady(true);
    const stop = onAudioCatalog(() => setReady(true));
    void loadAudioCatalog().catch(() => {});
    return stop;
  }, []);
  return ready;
}
