import { useState, useSyncExternalStore } from "react";
import {
  allowDeviceProgress,
  deleteCloudData,
  getSyncStatus,
  pauseSync,
  subscribeSync,
  syncNow,
} from "./sync";

export const useSyncStatus = () =>
  useSyncExternalStore(subscribeSync, getSyncStatus, getSyncStatus);
export function SyncConsent() {
  const [busy, setBusy] = useState(false),
    [error, setError] = useState("");
  const state = useSyncStatus();
  return (
    <main className="recovery sync-consent">
      <h1>Add this device’s progress to your account?</h1>
      <p>
        Signed in as <strong>{state.account?.email}</strong>. Adding combines
        this device’s study history with your account. Matching attempts are
        counted once.
      </p>
      <p>
        Choosing “Keep on this device” leaves cloud sync paused. Voice
        recordings and unfinished lesson positions stay here either way.
      </p>
      <div className="sync-actions">
        <button
          className="button"
          disabled={busy}
          onClick={async () => {
            setBusy(true);
            try {
              await allowDeviceProgress();
            } catch (e) {
              setError((e as Error).message);
            } finally {
              setBusy(false);
            }
          }}
        >
          Add this device’s progress
        </button>
        <button
          className="button secondary"
          disabled={busy}
          onClick={() => void pauseSync()}
        >
          Keep on this device
        </button>
      </div>
      {error && (
        <p className="inline-error" role="alert">
          {error}
        </p>
      )}
    </main>
  );
}
export function SyncPanel() {
  const state = useSyncStatus();
  const [confirmDelete, setConfirmDelete] = useState(false),
    [confirmResume, setConfirmResume] = useState(false),
    [busy, setBusy] = useState(false),
    [error, setError] = useState("");
  const allowed =
    !!state.account &&
    !["consent", "account-mismatch", "unconfigured"].includes(state.phase);
  const run = async (task: () => Promise<void>) => {
    setBusy(true);
    setError("");
    try {
      await task();
    } catch (e) {
      setError((e as Error).message);
    } finally {
      setBusy(false);
    }
  };
  return (
    <section className="sync-panel" aria-labelledby="sync-heading">
      <h3 id="sync-heading">Cloud sync</h3>
      <p role="status" aria-live="polite">
        {state.message}
      </p>
      <p className="small">
        Last sync:{" "}
        {state.lastSync ? new Date(state.lastSync).toLocaleString() : "Not yet"}
        {state.pending && state.account ? " · Changes saved locally" : ""}
      </p>
      {allowed && (
        <div className="sync-actions">
          {state.phase === "paused" ? (
            <button
              className="button secondary"
              disabled={busy}
              onClick={() => setConfirmResume(true)}
            >
              Enable sync again
            </button>
          ) : (
            <button
              className="button secondary"
              disabled={
                busy || state.phase === "syncing" || state.phase === "offline"
              }
              onClick={() => void run(() => syncNow())}
            >
              {state.phase === "syncing" ? "Syncing…" : "Sync now"}
            </button>
          )}
          <button
            className="text-button"
            disabled={
              busy || state.phase === "syncing" || state.phase === "offline"
            }
            onClick={() => setConfirmDelete(true)}
          >
            Delete my cloud data
          </button>
        </div>
      )}
      {confirmResume && (
        <div className="confirm-box">
          <p>
            Add this device’s progress to your account? If cloud data was
            deleted, this uploads your local progress again.
          </p>
          <button
            className="button"
            disabled={busy}
            onClick={() =>
              void run(async () => {
                await allowDeviceProgress();
                setConfirmResume(false);
              })
            }
          >
            Add progress and enable sync
          </button>
          <button
            className="text-button"
            disabled={busy}
            onClick={() => setConfirmResume(false)}
          >
            Cancel
          </button>
        </div>
      )}
      {confirmDelete && (
        <div className="confirm-box danger">
          <p>
            Delete all cloud study history and preferences for{" "}
            <strong>{state.account?.email}</strong>? Your local data and sign-in
            account stay. Sync pauses; other devices must get permission before
            uploading again. A small deletion marker remains to enforce that
            pause.
          </p>
          <button
            className="button danger"
            disabled={busy}
            onClick={() =>
              void run(async () => {
                await deleteCloudData();
                setConfirmDelete(false);
              })
            }
          >
            Confirm cloud deletion
          </button>
          <button
            className="text-button"
            disabled={busy}
            onClick={() => setConfirmDelete(false)}
          >
            Cancel
          </button>
        </div>
      )}
      {error && (
        <p className="inline-error" role="alert">
          {error}
        </p>
      )}
    </section>
  );
}
