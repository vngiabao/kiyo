import "fake-indexeddb/auto";
import { beforeEach, describe, expect, it } from "vitest";
import { readFileSync } from "node:fs";
import { db, defaultProfile, exportRecord, saveAttempt } from "../src/db";
import {
  canonical,
  cloudProfile,
  mergeSnapshots,
  snapshotOf,
  type LearningSnapshot,
  type SyncRow,
} from "../src/sync-model";
import {
  acceptAccount,
  allowDeviceProgress,
  deleteCloudData,
  detachSync,
  getSyncStatus,
  localSyncState,
  pauseSync,
  setSyncTransportForTests,
  syncNow,
} from "../src/sync";
import {
  SyncConflict,
  type CloudSnapshot,
  type SyncTransport,
} from "../src/sync-transport";
import type { Account, Attempt } from "../src/types";

const user: Account = {
  id: "user-a",
  email: "a@example.test",
  name: "A",
  provider: "email",
};
const empty = (): LearningSnapshot => ({
  attempts: [],
  sessions: [],
  memories: [],
  mistakes: [],
});
const attempt = (
  id: string,
  at: number,
  extra: Partial<Attempt> = {},
): Attempt => ({
  id,
  at,
  phraseId: "hello",
  modality: "listening",
  correct: true,
  answer: "Hello",
  expected: "Hello",
  latencyMs: 1000,
  support: "none",
  context: "sync test",
  ...extra,
});
const time = Date.UTC(2026, 0, 1);
class FakeCloud implements SyncTransport {
  data: CloudSnapshot = {
    revision: 0,
    epoch: "initial",
    deleted: false,
    schema_version: 1,
    rows: [],
  };
  failPush = false;
  loseAck = false;
  conflict = false;
  pushes = 0;
  onPull?: () => Promise<void>;
  onPush?: () => Promise<void>;
  async pull(knownRevision?: number) {
    await this.onPull?.();
    return knownRevision === this.data.revision && !this.data.deleted
      ? { ...structuredClone(this.data), rows: [], unchanged: true }
      : structuredClone(this.data);
  }
  async push(state: CloudSnapshot, rows: SyncRow[], resume: boolean) {
    this.pushes++;
    await this.onPush?.();
    if (this.failPush) throw new Error("Offline test");
    if (this.conflict) {
      this.conflict = false;
      this.data.revision++;
      throw new SyncConflict();
    }
    if (
      state.revision !== this.data.revision ||
      state.epoch !== this.data.epoch
    )
      throw new SyncConflict();
    if (this.data.deleted && !resume) throw new Error("Deleted");
    const values = new Map(this.data.rows.map((r) => [`${r.kind}:${r.id}`, r]));
    for (const row of rows)
      values.set(`${row.kind}:${row.id}`, structuredClone(row));
    this.data.rows = [...values.values()];
    this.data.revision++;
    this.data.deleted = false;
    if (this.loseAck) {
      this.loseAck = false;
      throw new Error("Connection lost after commit");
    }
    return this.data;
  }
  async remove() {
    this.data = {
      ...this.data,
      rows: [],
      epoch: "deleted-epoch",
      revision: this.data.revision + 1,
      deleted: true,
    };
    return this.data;
  }
}
let cloud: FakeCloud;
beforeEach(async () => {
  await detachSync();
  await db.transaction("rw", db.tables, async () => {
    for (const table of db.tables) await table.clear();
  });
  cloud = new FakeCloud();
  setSyncTransportForTests(() => cloud);
  Object.defineProperty(navigator, "onLine", {
    value: true,
    configurable: true,
  });
});
describe("deterministic evidence merge", () => {
  it("sorts ties by ID, deduplicates, and converges regardless of arrival order", () => {
    const a = attempt("b", time, { correct: false }),
      b = attempt("a", time),
      c = attempt("c", time + 86400000);
    const x = mergeSnapshots(
      { ...empty(), attempts: [c, a] },
      { ...empty(), attempts: [a, b] },
    );
    const y = mergeSnapshots(
      { ...empty(), attempts: [b, a] },
      { ...empty(), attempts: [c, a] },
    );
    expect(x.attempts.map((r) => r.id)).toEqual(["a", "b", "c"]);
    expect(canonical(x)).toBe(canonical(y));
    expect(x.memories[0].successes).toBe(2);
    expect(x.mistakes[0].count).toBe(1);
  });
  it("never upgrades supported or unscored answers", () => {
    const x = mergeSnapshots(
      {
        ...empty(),
        attempts: [
          attempt("a", time, { support: "pinyin" }),
          attempt("b", time, { correct: null }),
        ],
      },
      empty(),
    );
    expect(x.memories).toEqual([]);
  });
  it("rejects conflicting immutable IDs rather than choosing silently", () => {
    expect(() =>
      mergeSnapshots(
        { ...empty(), attempts: [attempt("a", time)] },
        { ...empty(), attempts: [attempt("a", time, { correct: false })] },
      ),
    ).toThrow("immutable");
  });
  it("uses latest profile timestamp and a stable tie breaker", () => {
    const a = cloudProfile({
      ...defaultProfile,
      name: "Old",
      updatedAt: 10,
      updatedBy: "a",
    });
    const b = { ...a, name: "New", updatedAt: 20, updatedBy: "b" };
    expect(
      mergeSnapshots({ ...empty(), profile: a }, { ...empty(), profile: b })
        .profile?.name,
    ).toBe("New");
    a.updatedAt = 20;
    expect(
      mergeSnapshots({ ...empty(), profile: b }, { ...empty(), profile: a })
        .profile?.name,
    ).toBe("New");
  });
  it("rejects unknown schema and invalid cloud content before local writes", () => {
    expect(() =>
      snapshotOf([
        {
          kind: "attempts",
          id: "a",
          schema_version: 2,
          payload: attempt("a", time),
        },
      ]),
    ).toThrow("different format");
    expect(() =>
      snapshotOf([
        { kind: "attempts", id: "a", schema_version: 1, payload: {} },
      ]),
    ).toThrow();
  });
  it("strips account identity, device voice preference and extra recording fields", () => {
    const profile = cloudProfile({
      ...defaultProfile,
      account: user,
      voiceURI: "device-voice",
      updatedAt: time,
      updatedBy: "a",
    });
    expect(profile).not.toHaveProperty("account");
    expect(profile).not.toHaveProperty("voiceURI");
    const safe = snapshotOf([
      {
        kind: "attempts",
        id: "a",
        schema_version: 1,
        payload: { ...attempt("a", time), recording: "private bytes" },
      },
    ]);
    expect(safe.attempts[0]).not.toHaveProperty("recording");
  });
});
describe("local queue, consent and account separation", () => {
  it("restores an existing cloud profile on a fresh device without newer default preferences", async () => {
    cloud.data.rows = [
      {
        kind: "profiles",
        id: "learner",
        schema_version: 1,
        payload: cloudProfile({
          ...defaultProfile,
          name: "Returning learner",
          minutes: 45,
          onboarded: true,
          updatedAt: time,
          updatedBy: "other-device",
        }),
      },
    ];
    await acceptAccount(user);
    await syncNow();
    expect(getSyncStatus().phase).toBe("ready");
    expect(await db.profiles.get("learner")).toMatchObject({
      name: "Returning learner",
      minutes: 45,
      onboarded: true,
    });
  });
  it("does not upload guest progress until explicitly accepted", async () => {
    await db.profiles.put({ ...defaultProfile, onboarded: true });
    await saveAttempt(attempt("a", time));
    await acceptAccount(user);
    await syncNow();
    expect(getSyncStatus().phase).toBe("consent");
    expect(cloud.pushes).toBe(0);
    await allowDeviceProgress();
    expect(cloud.data.rows.some((r) => r.kind === "attempts")).toBe(true);
    expect(getSyncStatus().lastSync).toBeTruthy();
  });
  it("declining keeps guest progress local", async () => {
    await saveAttempt(attempt("a", time));
    await acceptAccount(user);
    await pauseSync();
    await syncNow();
    expect(cloud.pushes).toBe(0);
    expect(await db.attempts.count()).toBe(1);
    await detachSync();
    await acceptAccount(user);
    expect(getSyncStatus().phase).toBe("paused");
  });
  it("survives an offline reload and sends saved records after reconnecting", async () => {
    await saveAttempt(attempt("a", time));
    await acceptAccount(user);
    Object.defineProperty(navigator, "onLine", {
      value: false,
      configurable: true,
    });
    await allowDeviceProgress();
    expect(getSyncStatus().phase).toBe("offline");
    await detachSync();
    await acceptAccount(user);
    Object.defineProperty(navigator, "onLine", {
      value: true,
      configurable: true,
    });
    await syncNow();
    expect(cloud.data.rows.filter((r) => r.kind === "attempts")).toHaveLength(
      1,
    );
  });
  it("lost acknowledgement retries do not double-count progress", async () => {
    await saveAttempt(attempt("a", time, { correct: false }));
    await acceptAccount(user);
    cloud.loseAck = true;
    await allowDeviceProgress();
    expect(getSyncStatus().phase).toBe("error");
    await syncNow();
    expect(await db.attempts.count()).toBe(1);
    expect((await db.mistakes.toArray())[0].count).toBe(1);
    expect(cloud.data.rows.filter((r) => r.kind === "attempts")).toHaveLength(
      1,
    );
  });
  it("keeps local data on sign-out and blocks a different account", async () => {
    await saveAttempt(attempt("a", time));
    await acceptAccount(user);
    await allowDeviceProgress();
    await detachSync();
    expect(await db.attempts.count()).toBe(1);
    await acceptAccount({ ...user, id: "user-b" });
    expect(getSyncStatus().phase).toBe("account-mismatch");
    const count = cloud.pushes;
    await syncNow();
    expect(cloud.pushes).toBe(count);
  });
  it("does not overwrite an edit made while a download is in flight", async () => {
    await saveAttempt(attempt("a", time));
    await acceptAccount(user);
    cloud.onPull = async () => {
      await saveAttempt(attempt("b", time + 10000));
    };
    await allowDeviceProgress();
    expect(await db.attempts.count()).toBe(2);
  });
  it("retries revision conflicts", async () => {
    await saveAttempt(attempt("a", time));
    await acceptAccount(user);
    cloud.conflict = true;
    await allowDeviceProgress();
    expect(getSyncStatus().phase).toBe("ready");
  });
  it("keeps edits made during upload pending for the next sync", async () => {
    await saveAttempt(attempt("a", time));
    await acceptAccount(user);
    cloud.onPush = async () => {
      await saveAttempt(attempt("b", time + 10000));
    };
    await allowDeviceProgress();
    expect(await db.attempts.count()).toBe(2);
    expect((await localSyncState()).pending).toBe(true);
    cloud.onPush = undefined;
    await syncNow();
    expect(cloud.data.rows.filter((r) => r.kind === "attempts")).toHaveLength(
      2,
    );
  });
  it("blocks an old in-flight download after switching accounts", async () => {
    await saveAttempt(attempt("a", time));
    await acceptAccount(user);
    cloud.onPull = async () => {
      await acceptAccount({ ...user, id: "user-b" });
    };
    await allowDeviceProgress();
    expect(cloud.pushes).toBe(0);
    expect(getSyncStatus().phase).toBe("account-mismatch");
    expect(await db.attempts.count()).toBe(1);
  });
  it("checks unchanged cloud revisions without re-uploading or clearing local evidence", async () => {
    await saveAttempt(attempt("a", time));
    await acceptAccount(user);
    await allowDeviceProgress();
    const pushes = cloud.pushes;
    await syncNow();
    expect(cloud.pushes).toBe(pushes);
    expect(await db.attempts.count()).toBe(1);
    expect(getSyncStatus().phase).toBe("ready");
  });
  it("rejects future schemas without replacing local evidence", async () => {
    await saveAttempt(attempt("a", time));
    await acceptAccount(user);
    cloud.data.schema_version = 2;
    await allowDeviceProgress();
    expect(getSyncStatus().phase).toBe("error");
    expect(await db.attempts.count()).toBe(1);
    expect(cloud.pushes).toBe(0);
  });
  it("deletes cloud rows, retains local records and pauses until explicit consent", async () => {
    await saveAttempt(attempt("a", time));
    await acceptAccount(user);
    await allowDeviceProgress();
    await deleteCloudData();
    await syncNow();
    expect(cloud.data.rows).toEqual([]);
    expect(cloud.data.deleted).toBe(true);
    expect(await db.attempts.count()).toBe(1);
    expect((await localSyncState()).enabled).toBe(false);
    await allowDeviceProgress();
    expect(cloud.data.deleted).toBe(false);
  });
  it("another device's deletion cannot silently be undone", async () => {
    await saveAttempt(attempt("a", time));
    await acceptAccount(user);
    await allowDeviceProgress();
    await cloud.remove();
    await syncNow();
    expect(getSyncStatus().phase).toBe("paused");
    expect(cloud.data.rows).toEqual([]);
  });
  it("still exports the original backup format without sync credentials", async () => {
    await saveAttempt(attempt("a", time));
    await acceptAccount(user);
    await allowDeviceProgress();
    const backup = await exportRecord();
    expect(backup.schemaVersion).toBe(1);
    expect(backup.attempts).toHaveLength(1);
    expect(backup).not.toHaveProperty("syncState");
  });
});
describe("SQL security contract (static; live RLS checks documented separately)", () => {
  const sql = readFileSync(
    "supabase/migrations/202610040001_learning_sync.sql",
    "utf8",
  );
  it("enables and forces RLS on every new table with owner checks", () => {
    const tables = [...sql.matchAll(/create table public\.(\w+)/g)].map(
      (m) => m[1],
    );
    expect(tables).toHaveLength(2);
    for (const table of tables) {
      expect(sql).toContain(
        `alter table public.${table} enable row level security`,
      );
      expect(sql).toContain(
        `alter table public.${table} force row level security`,
      );
      expect(sql).toMatch(
        new RegExp(
          `on public\\.${table} for all to authenticated\\s+using \\(user_id = \\(select auth\\.uid\\(\\)\\)\\) with check \\(user_id = \\(select auth\\.uid\\(\\)\\)\\)`,
        ),
      );
    }
  });
  it("RPCs derive identity from auth, lock the search path and revoke public execution", () => {
    expect(sql.match(/security definer set search_path = ''/g)).toHaveLength(3);
    expect(sql.match(/if learner is null then raise exception/g)).toHaveLength(
      3,
    );
    expect(sql).toContain("from public, anon");
    expect(sql).not.toMatch(/p_user_id/);
  });
});
