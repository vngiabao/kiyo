import "fake-indexeddb/auto";
import { beforeEach, expect, it } from "vitest";
import { db, defaultProfile, exportRecord, importRecord } from "../src/db";
import { hskDB } from "../src/hsk-db";
import { makeRun } from "../src/hsk-model";

beforeEach(async () => {
  for (const table of db.tables) await table.clear();
  for (const table of hskDB.tables) await table.clear();
});

it("restores exam runs from a full progress backup without replacing existing exam answers", async () => {
  const run = makeRun("identity");
  await hskDB.runs.add(run);
  const backup = await exportRecord();
  expect(backup.hskNotebook.runs.map((r) => r.id)).toEqual([run.id]);
  await hskDB.runs.clear();
  await importRecord(backup);
  expect(await hskDB.runs.get(run.id)).toEqual(run);
  const changed = { ...run, finishedAt: run.startedAt + 100 };
  await hskDB.runs.put(changed);
  await importRecord(backup);
  expect(await hskDB.runs.get(run.id)).toEqual(changed);
});

it("rejects a corrupt embedded notebook before importing the main learning record", async () => {
  await db.profiles.put({ ...defaultProfile, name: "Local learner" });
  const backup = await exportRecord();
  backup.profiles[0].name = "Must not replace local";
  backup.hskNotebook.runs.push({ ...makeRun("identity"), itemIds: ["missing-item"] });
  await expect(importRecord(backup)).rejects.toThrow("HSK backup");
  expect((await db.profiles.get("learner"))!.name).toBe("Local learner");
});

it("imports an older progress backup without removing the separate exam notebook", async () => {
  const { hskNotebook: _notebook, ...legacy } = await exportRecord();
  const run = makeRun("numbers");
  await hskDB.runs.add(run);
  await importRecord(legacy);
  expect(await hskDB.runs.get(run.id)).toEqual(run);
});
