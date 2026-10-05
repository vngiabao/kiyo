import { expect, it } from "vitest";
import { backupDue } from "../src/backup";

const DAY = 86_400_000;
const now = 100 * DAY;

it("stays quiet before any study, and for the first couple of days", () => {
  expect(backupDue({ now })).toBe(false);
  expect(backupDue({ now, firstStudyAt: now - DAY })).toBe(false);
  expect(backupDue({ now, firstStudyAt: now - 2 * DAY })).toBe(true);
});
it("asks again a week after the last backup", () => {
  expect(backupDue({ now, firstStudyAt: now - 30 * DAY, lastBackupAt: now - 6 * DAY })).toBe(false);
  expect(backupDue({ now, firstStudyAt: now - 30 * DAY, lastBackupAt: now - 7 * DAY })).toBe(true);
});
it("'Later' hides it for three days", () => {
  const base = { now, firstStudyAt: now - 30 * DAY, lastBackupAt: now - 20 * DAY };
  expect(backupDue({ ...base, snoozedAt: now - 2 * DAY })).toBe(false);
  expect(backupDue({ ...base, snoozedAt: now - 3 * DAY })).toBe(true);
});
it("is unnecessary while cloud sync is recent", () => {
  const base = { now, firstStudyAt: now - 30 * DAY };
  expect(backupDue({ ...base, lastSyncAt: now - DAY })).toBe(false);
  expect(backupDue({ ...base, lastSyncAt: now - 8 * DAY })).toBe(true);
});
