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
} from "../src/hsk-model";
import { validateHskPack } from "../src/hsk-pack";
import {
  hskDB,
  saveHskAnswer,
  finishHskRun,
  exportHsk,
  importHsk,
} from "../src/hsk-db";
const pack = JSON.parse(
  readFileSync("content/packs/hsk-reading.hsk.json", "utf8"),
);
const words = JSON.parse(readFileSync("content/hsk/levels.json", "utf8")).words;
beforeEach(async () => {
  vi.useRealTimers();
  await hskDB.runs.clear();
  await hskDB.settings.clear();
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
