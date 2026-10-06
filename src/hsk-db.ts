import Dexie, { type EntityTable } from "dexie";
import {
  defaultHskSettings,
  validRun,
  type HskRun,
  type HskSettings,
} from "./hsk-model";

// A separate, explicitly local study notebook. Existing learning/sync data is untouched.
class HskDB extends Dexie {
  settings!: EntityTable<HskSettings, "id">;
  runs!: EntityTable<HskRun, "id">;
  constructor() {
    super("kiyo-hsk-v1");
    this.version(1).stores({ settings: "id", runs: "id,unit,startedAt" });
  }
}
export const hskDB = new HskDB();
export async function markHskItemSeen(id: string, item: string) {
  await hskDB.transaction("rw", hskDB.runs, async () => {
    const run = await hskDB.runs.get(id);
    if (!run || run.packVersion !== 2 || run.finishedAt ||
      !run.itemIds.includes(item) || run.seenItemIds?.includes(item) ||
      (run.deadline !== null && Date.now() >= run.deadline)) return;
    await hskDB.runs.update(id, { seenItemIds: [...(run.seenItemIds ?? []), item] });
  });
}
export async function saveHskAnswer(
  id: string,
  item: string,
  value: string,
  supported: boolean,
) {
  return hskDB.transaction("rw", hskDB.runs, async () => {
    const r = await hskDB.runs.get(id);
    if (!r || r.finishedAt || (r.deadline !== null && Date.now() >= r.deadline))
      return;
    const updated = {
      ...r,
      answers: {
        ...r.answers,
        [item]: {
          value,
          supported: supported || r.answers[item]?.supported || false,
        },
      },
    };
    if (!validRun(updated))
      throw new Error("This answer could not be saved. Reload the study area.");
    await hskDB.runs.put(updated);
  });
}
export async function finishHskRun(id: string) {
  await hskDB.transaction("rw", hskDB.runs, async () => {
    const r = await hskDB.runs.get(id);
    if (r && !r.finishedAt)
      await hskDB.runs.update(id, {
        finishedAt: Math.min(Date.now(), r.deadline ?? Infinity),
      });
  });
}
export async function changeHskSettings(update: Partial<HskSettings>) {
  await hskDB.transaction("rw", hskDB.settings, async () => {
    const old = (await hskDB.settings.get("learner")) ?? defaultHskSettings;
    await hskDB.settings.put({ ...old, ...update, id: "learner" });
  });
}
export async function exportHsk() {
  return {
    kind: "kiyo-hsk-backup",
    schemaVersion: 1,
    exportedAt: new Date().toISOString(),
    settings: (await hskDB.settings.get("learner")) ?? structuredClone(defaultHskSettings),
    runs: await hskDB.runs.toArray(),
  };
}
export async function importHsk(raw: unknown) {
  const p = raw as Awaited<ReturnType<typeof exportHsk>>;
  const s = p?.settings;
  if (
    p?.kind !== "kiyo-hsk-backup" ||
    p.schemaVersion !== 1 ||
    !Array.isArray(p.runs) ||
    p.runs.length > 10000 ||
    !p.runs.every(validRun) ||
    !s ||
    s.id !== "learner" ||
    !Number.isInteger(s.level) ||
    s.level < 1 ||
    s.level > 7 ||
    (s.level === 7 && s.edition !== "3.0") ||
    !["2.0", "3.0"].includes(s.edition) ||
    !Array.isArray(s.studied) ||
    !Array.isArray(s.sourceDone) ||
    ![...s.studied, ...s.sourceDone].every(
      (x) => typeof x === "string" && x.length < 100,
    )
  )
    throw new Error(
      "This is not a valid HSK backup for the installed practice pack.",
    );
  await hskDB.transaction("rw", hskDB.runs, hskDB.settings, async () => {
    // Immutable completed runs merge by id; an existing run is never overwritten.
    for (const r of p.runs)
      if (!(await hskDB.runs.get(r.id))) await hskDB.runs.add(r);
    const old = await hskDB.settings.get("learner");
    await hskDB.settings.put({
      ...s,
      studied: [...new Set([...s.studied, ...(old?.studied ?? [])])],
      sourceDone: [...new Set([...s.sourceDone, ...(old?.sourceDone ?? [])])],
    });
  });
}
