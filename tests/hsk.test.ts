import "fake-indexeddb/auto";
import { beforeEach, expect, it, vi } from "vitest";
import { readFileSync } from "node:fs";
import {
  hskItems,
  makeRun,
  gradeRun,
  unitUnlocked,
  unresolvedItems,
  validRun,
  makeBankRun,
  hskUnitsFor,
} from "../src/hsk-model";
import { validateHskPack } from "../src/hsk-pack";
import {
  hskDB,
  saveHskAnswer,
  finishHskRun,
  exportHsk,
  importHsk,
  markHskItemSeen,
} from "../src/hsk-db";
const pack = JSON.parse(
  readFileSync("content/packs/hsk-reading.hsk.json", "utf8"),
);
const words = JSON.parse(readFileSync("content/hsk/levels.json", "utf8")).words;
it("keeps saved checkpoint IDs while describing higher-level mixed skills honestly", () => {
  expect(hskUnitsFor(3).map((u) => u.id)).toEqual(hskUnitsFor(1).map((u) => u.id));
  expect(hskUnitsFor(3).map((u) => u.title).join(" ")).not.toContain("People & identity");
  expect(hskUnitsFor(2)[1].title).toBe("Connect the details");
});
beforeEach(async () => {
  vi.useRealTimers();
  await hskDB.runs.clear();
  await hskDB.settings.clear();
});
it("starts and restores every installed advanced bank while rejecting mismatched levels", async () => {
  const levels = [...new Set(hskItems.map((item) => item.level))].filter((level) => level >= 4);
  expect(levels.length).toBeGreaterThan(0);
  for (const level of levels) {
    const run = makeBankRun("identity", level as 4 | 5 | 6, []);
    expect(validRun(run)).toBe(true);
    expect(validRun({ ...run, level: 7 })).toBe(false);
    expect(validRun({ ...run, level: 1 })).toBe(false);
    await hskDB.runs.put(run);
  }
  const backup = await exportHsk();
  await hskDB.runs.clear();
  await importHsk(backup);
  expect(await hskDB.runs.count()).toBe(levels.length);
  for (const run of await hskDB.runs.toArray()) expect(validRun(run)).toBe(true);
});
function completed(unit: "identity" | "numbers" | "daily") {
  const r = makeRun(unit);
  r.itemIds.forEach(
    (id) =>
      (r.answers[id] = {
        value: hskItems.find((q) => q.id === id)!.answer,
        supported: false,
      }),
  );
  r.finishedAt = r.startedAt + 100;
  return r;
}
it("validates original pack vocabulary, pinyin and answer keys before publication", () => {
  expect(validateHskPack(pack, words)).toEqual([]);
  const bad = structuredClone(pack);
  bad.items[0].answer = "不在选项中";
  bad.items[1].choices[0].py = "cuò";
  expect(validateHskPack(bad, words).length).toBeGreaterThan(1);
});
it("supported results and out-of-order passes cannot unlock the path", () => {
  const r = completed("identity");
  expect(unitUnlocked(1, [r])).toBe(true);
  r.answers[r.itemIds[0]].supported = true;
  expect(gradeRun(r).passed).toBe(false);
  expect(unitUnlocked(1, [r])).toBe(false);
  expect(unitUnlocked(2, [completed("numbers")])).toBe(false);
});
it("repair only clears a missed question after later unaided evidence", () => {
  const first = completed("identity"),
    id = first.itemIds[0];
  first.answers[id].value = "";
  const repair = makeRun("repair", [id]);
  repair.finishedAt = first.finishedAt! + 100;
  repair.answers[id] = {
    value: hskItems.find((q) => q.id === id)!.answer,
    supported: true,
  };
  expect(unresolvedItems([repair, first])).toContain(id);
  repair.answers[id].supported = false;
  expect(unresolvedItems([repair, first])).toEqual([]);
});
it("saving help is sticky even after the answer changes", async () => {
  const r = makeRun("identity"),
    id = r.itemIds[0];
  await hskDB.runs.add(r);
  await saveHskAnswer(r.id, id, "", true);
  await saveHskAnswer(r.id, id, "是", false);
  expect((await hskDB.runs.get(r.id))!.answers[id]).toEqual({
    value: "是",
    supported: true,
  });
});
it("expired exams reject late answers, submit once and retain their deadline", async () => {
  vi.useFakeTimers({ toFake: ["Date"] });
  vi.setSystemTime(new Date("2026-10-04T20:00:00Z"));
  const r = makeRun("sample"),
    id = r.itemIds[0];
  await hskDB.runs.add(r);
  vi.setSystemTime(r.deadline! + 1000);
  await saveHskAnswer(r.id, id, "是", false);
  await finishHskRun(r.id);
  await finishHskRun(r.id);
  const saved = (await hskDB.runs.get(r.id))!;
  expect(saved.answers).toEqual({});
  expect(saved.finishedAt).toBe(r.deadline);
  vi.useRealTimers();
});
it("backup restore merges attempts without overwriting existing progress", async () => {
  const r = completed("identity");
  await hskDB.runs.add(r);
  const backup = await exportHsk();
  await hskDB.runs.clear();
  await importHsk(backup);
  expect(await hskDB.runs.count()).toBe(1);
  const altered = structuredClone(backup);
  altered.runs[0].answers = {};
  await importHsk(altered);
  expect(gradeRun((await hskDB.runs.get(r.id))!).passed).toBe(true);
  expect(validRun({ ...r, itemIds: ["unknown"] })).toBe(false);
  await expect(
    importHsk({ ...backup, runs: [{ ...r, itemIds: ["unknown"] }] }),
  ).rejects.toThrow();
});

it("advanced notebook backups preserve the combined exam and reject legacy mislabelling", async () => {
  const backup = await exportHsk();
  backup.settings.level = 7;
  backup.settings.edition = "3.0";
  await importHsk(backup);
  expect((await exportHsk()).settings.level).toBe(7);
  backup.settings.edition = "2.0";
  await expect(importHsk(backup)).rejects.toThrow();
});

it("keeps legacy results valid and restores rotating-bank exposure without overwriting it", async () => {
  const legacy = completed("identity");
  const bank = makeBankRun("identity", 1, [legacy]);
  expect(bank.itemIds).toHaveLength(10);
  expect(bank.itemIds.every((id) => !legacy.itemIds.includes(id))).toBe(true);
  expect(validRun(legacy)).toBe(true);
  await hskDB.runs.bulkAdd([legacy, bank]);
  await markHskItemSeen(bank.id, bank.itemIds[0]);
  await markHskItemSeen(bank.id, bank.itemIds[0]);
  await markHskItemSeen(bank.id, "not-in-run");
  const backup = await exportHsk();
  expect(backup.runs.find((r) => r.id === bank.id)!.seenItemIds).toEqual([bank.itemIds[0]]);
  for (const row of backup.runs) expect(validRun(row), JSON.stringify(row)).toBe(true);
  await hskDB.runs.clear();
  await importHsk(backup);
  expect(gradeRun((await hskDB.runs.get(legacy.id))!).passed).toBe(true);
  expect((await hskDB.runs.get(bank.id))!.seenItemIds).toEqual([bank.itemIds[0]]);
  const corrupted = structuredClone(backup);
  corrupted.runs.find((r) => r.id === bank.id)!.level = 2;
  await expect(importHsk(corrupted)).rejects.toThrow();
  expect(await hskDB.runs.count()).toBe(2);
});

it("publishes a varied 60-checkpoint and 30-sample level-1 bank with stable legacy IDs", () => {
  const bank = JSON.parse(readFileSync("content/packs/hsk-1-bank.hsk.json", "utf8"));
  expect(validateHskPack(bank, words)).toEqual([]);
  const items = hskItems.filter((q) => q.level === 1);
  expect(items).toHaveLength(90);
  expect(items.filter((q) => q.unit === "sample")).toHaveLength(30);
  expect(items.filter((q) => q.unit !== "sample")).toHaveLength(60);
  expect(pack.items.every((q: { id: string }) => items.some((i) => i.id === q.id))).toBe(true);
  expect(new Set(items.filter((q) => q.format).map((q) => q.format))).toEqual(new Set(["reading","listening","ordering"]));
  const positions = bank.items.map((q: { answer: string; choices: { zh: string }[] }) => q.choices.findIndex((c) => c.zh === q.answer));
  expect(new Set(positions).size).toBe(4);
});
