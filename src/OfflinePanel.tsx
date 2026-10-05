import { useEffect, useRef, useState } from "react";
import { askPersistentStorage, clipUrls, saveAllAudio, savedClipCount, storageInfo, type StorageInfo } from "./offline";

/** Settings → Your data: keep this device's copy safe and usable offline. */
export function OfflinePanel() {
  const total = clipUrls().length;
  const [saved, setSaved] = useState<number | null>(null),
    [info, setInfo] = useState<StorageInfo | null>(null),
    [progress, setProgress] = useState<number | null>(null),
    [note, setNote] = useState("");
  const abort = useRef<AbortController | null>(null);
  const refresh = () => {
    void savedClipCount().then(setSaved);
    void storageInfo().then(setInfo);
  };
  useEffect(() => {
    refresh();
    return () => abort.current?.abort();
  }, []);
  async function saveAll() {
    abort.current = new AbortController();
    setNote("");
    try {
      const { failed } = await saveAllAudio((done) => setProgress(done), abort.current.signal);
      setNote(failed ? `${failed} clips couldn’t download. Try again when you’re online.` : "All of Sayo’s audio is saved on this device.");
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
    </div>
  );
}
