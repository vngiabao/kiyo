/**
 * Until cloud sync is switched on, progress lives only in this browser.
 * A gentle weekly nudge to export a backup, so years of study can't vanish
 * with cleared site data. Pure rule + one download helper.
 */
import { exportRecord } from "./db";

const DAY = 86_400_000;
export const BACKUP_EVERY_DAYS = 7;
/** First nudge comes after a couple of days of real study, not on day one. */
export const FIRST_BACKUP_AFTER_DAYS = 2;
export const SNOOZE_DAYS = 3;

export function backupDue({
  now,
  firstStudyAt,
  lastBackupAt,
  snoozedAt,
  lastSyncAt,
}: {
  now: number;
  firstStudyAt?: number;
  lastBackupAt?: number;
  snoozedAt?: number;
  /** Last successful cloud sync, when sync is enabled. */
  lastSyncAt?: number;
}): boolean {
  if (!firstStudyAt) return false;
  if (lastSyncAt && now - lastSyncAt < BACKUP_EVERY_DAYS * DAY) return false;
  if (snoozedAt && now - snoozedAt < SNOOZE_DAYS * DAY) return false;
  return lastBackupAt
    ? now - lastBackupAt >= BACKUP_EVERY_DAYS * DAY
    : now - firstStudyAt >= FIRST_BACKUP_AFTER_DAYS * DAY;
}

/** Download the learning record as a dated JSON file. */
export async function downloadBackup() {
  const record = await exportRecord();
  const url = URL.createObjectURL(new Blob([JSON.stringify(record, null, 2)], { type: "application/json" }));
  const a = document.createElement("a");
  a.href = url;
  a.download = `tingjian-backup-${new Date().toISOString().slice(0, 10)}.json`;
  a.click();
  setTimeout(() => URL.revokeObjectURL(url), 1000);
}
