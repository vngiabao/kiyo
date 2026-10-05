// Builds content/hsk/levels.json from the open "complete-hsk-vocabulary"
// dataset (MIT, github.com/drkameleon/complete-hsk-vocabulary).
// Usage: npx tsx scripts/import-hsk.ts            (downloads)
//        npx tsx scripts/import-hsk.ts file.json  (local copy)
// Levels: "hsk3" = HSK 3.0 / GF 0025-2021 (levels 1–6, 7 = band 7–9),
// "old" = HSK 2.0 (1–6). Used only by validation scripts; never shipped.
import { mkdirSync, readFileSync, writeFileSync } from "node:fs";

const source =
  "https://raw.githubusercontent.com/drkameleon/complete-hsk-vocabulary/main/complete.json";
type Entry = {
  simplified: string;
  level?: string[];
  forms?: { transcriptions?: { pinyin?: string } }[];
};
const data: Entry[] = process.argv[2]
  ? JSON.parse(readFileSync(process.argv[2], "utf8"))
  : await (await fetch(source)).json();

const out: Record<string, { hsk3?: number; old?: number; pinyin: string[] }> = {};
for (const e of data) {
  const levels = e.level ?? [];
  const pick = (prefix: string) => {
    const l = levels.find((x) => x.startsWith(prefix + "-"));
    return l ? Number(l.split("-")[1]) : undefined;
  };
  const pinyin = [
    ...new Set((e.forms ?? []).map((f) => f.transcriptions?.pinyin ?? "").filter(Boolean)),
  ];
  const prev = out[e.simplified];
  out[e.simplified] = {
    hsk3: Math.min(prev?.hsk3 ?? 99, pick("new") ?? 99),
    old: Math.min(prev?.old ?? 99, pick("old") ?? 99),
    pinyin: [...new Set([...(prev?.pinyin ?? []), ...pinyin])],
  };
  for (const k of ["hsk3", "old"] as const) if (out[e.simplified][k] === 99) delete out[e.simplified][k];
}
mkdirSync("content/hsk", { recursive: true });
writeFileSync(
  "content/hsk/levels.json",
  JSON.stringify({
    source,
    license: "MIT, complete-hsk-vocabulary contributors",
    note: "hsk3 = HSK 3.0 (2021 standard); 7 means band 7–9. Verify against the official syllabus before exam use.",
    words: out,
  }),
);
const counts: Record<number, number> = {};
for (const w of Object.values(out)) if (w.hsk3) counts[w.hsk3] = (counts[w.hsk3] ?? 0) + 1;
console.log(`Wrote content/hsk/levels.json: ${Object.keys(out).length} words; HSK3.0 per level`, counts);
