import { useEffect, useRef, useState } from "react";
import { askPersistentStorage, clipUrls, loadClipUrls, saveAllAudio, savedClipCount, storageInfo, type StorageInfo } from "./offline";
import { dictManifest, saveDictionary, savedShardCount, type DictManifest } from "./offline";

/** Settings → Your data: keep this device's copy safe and usable offline. */
export function OfflinePanel() {
  const [total, setTotal] = useState(() => clipUrls().length);
  useEffect(() => { void loadClipUrls().then((u) => setTotal(u.length)).catch(() => {}); }, []);
  const [saved, setSaved] = useState<number | null>(null),
    [info, setInfo] = useState<StorageInfo | null>(null),
    [progress, setProgress] = useState<number | null>(null),
    [note, setNote] = useState("");
  const abort = useRef<AbortController | null>(null);
  const refresh = () => {
    void savedClipCount().then(setSaved).catch(() => setNote("The browser couldn’t check saved audio. Try opening Settings again."));
    void storageInfo().then(setInfo).catch(() => setInfo(null));
  };
  useEffect(() => {
    refresh();
    return () => abort.current?.abort();
  }, []);
  async function saveAll() {
    abort.current = new AbortController();
    setNote("");
    setProgress(saved ?? 0);
    try {
      const { failed, cancelled } = await saveAllAudio((done) => setProgress(done), abort.current.signal);
      setNote(cancelled ? "Download stopped. Saved clips are kept; resume whenever you’re ready." : failed ? `${failed} clips couldn’t download. Try again when you’re online.` : "All of Sayo’s audio is saved on this device.");
    } catch (e) {
      if (!abort.current.signal.aborted) setNote((e as Error).message);
    } finally {
      setProgress(null);
      refresh();
    }
  }
  async function keep() {
    const granted = await askPersistentStorage();
    setNote(
      granted
        ? "This browser will keep your data even when space runs low."
        : "The browser didn’t allow it. Installing Kiyo as an app usually helps; keep exporting backups either way.",
    );
    refresh();
  }
  return (
    <div className="offline-panel">
      <h3>On this device</h3>
      <dl className="offline-facts">
        <div>
          <dt>Sayo’s audio</dt>
          <dd className="tabular">
            {progress !== null ? `Saving… ${progress} of ${total}` : saved === null ? "…" : `${saved} of ${total} clips saved`}
          </dd>
        </div>
        <div>
          <dt>Storage</dt>
          <dd>
            {info?.persisted ? "Kept: the browser won’t clear it to free space" : "Not protected: the browser may clear it if space runs low"}
            {info?.usedMB != null && <span className="muted tabular"> · {info.usedMB} MB used</span>}
          </dd>
        </div>
      </dl>
      <p className="small">Clips are saved as you hear them. Save them all to study anywhere offline.</p>
      <div className="offline-actions">
        {progress !== null ? (
          <button className="button secondary" onClick={() => abort.current?.abort()}>
            Stop
          </button>
        ) : (
          <button className="button secondary" disabled={saved === total} onClick={() => void saveAll()}>
            {saved === total ? "All audio saved" : "Save all audio for offline"}
          </button>
        )}
        {info && info.persisted === false && (
          <button className="text-button" onClick={() => void keep()}>
            Protect my data on this device
          </button>
        )}
      </div>
      {note && (
        <p className="small" role="status">
          {note}
        </p>
      )}
      <DictionaryPanel />
    </div>
  );
}

/** The offline dictionary: how much is saved, and a button to save it all. */
function DictionaryPanel() {
  const [manifest, setManifest] = useState<DictManifest | null>(null),
    [saved, setSaved] = useState<number | null>(null),
    [progress, setProgress] = useState<number | null>(null),
    [note, setNote] = useState("");
  const abort = useRef<AbortController | null>(null);
  useEffect(() => {
    void dictManifest().then(async (m) => {
      setManifest(m);
      if (m) setSaved(await savedShardCount(m.shards));
    }).catch(() => setNote("The browser couldn’t check saved dictionary files. Try opening Settings again."));
    return () => abort.current?.abort();
  }, []);
  if (!manifest) return null;
  const mb = (manifest.bytes / 1e6).toFixed(0);
  async function save() {
    abort.current = new AbortController();
    setNote("");
    setProgress(saved ?? 0);
    try {
      const { failed, cancelled } = await saveDictionary(manifest!.shards, setProgress, abort.current.signal);
      setNote(cancelled ? "Download stopped. Saved dictionary files are kept; resume whenever you’re ready." : failed ? `${failed} parts couldn’t download. Try again when you’re online.` : "The whole dictionary is saved on this device.");
    } catch (e) {
      if (!abort.current.signal.aborted) setNote((e as Error).message);
    } finally {
      setProgress(null);
      try { setSaved(await savedShardCount(manifest!.shards)); }
      catch { setNote("The browser couldn’t check saved dictionary files. Try opening Settings again."); }
    }
  }
  return (
    <div className="offline-dict">
      <dl className="offline-facts">
        <div>
          <dt>Dictionary</dt>
          <dd className="tabular">
            {progress !== null
              ? `Saving… ${Math.round((progress / manifest.shards) * 100)}%`
              : saved === null
                ? "…"
                : saved === manifest.shards
                  ? `All ${manifest.entries.toLocaleString()} entries saved`
                  : `${Math.round(((saved ?? 0) / manifest.shards) * 100)}% saved · parts load as you look words up`}
          </dd>
        </div>
      </dl>
      <div className="offline-actions">
        {progress !== null ? (
          <button className="button secondary" onClick={() => abort.current?.abort()}>
            Stop
          </button>
        ) : (
          <button className="button secondary" disabled={saved === manifest.shards} onClick={() => void save()}>
            {saved === manifest.shards ? "Dictionary saved" : `Save dictionary for offline (about ${mb} MB)`}
          </button>
        )}
      </div>
      {note && (
        <p className="small" role="status">
          {note}
        </p>
      )}
      <p className="small muted">
        Dictionary: {manifest.attribution} Licence {manifest.license}.
      </p>
    </div>
  );
}
