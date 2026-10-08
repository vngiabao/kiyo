import { readFileSync, writeFileSync } from "node:fs";
import { verifiedBankText, type HskBankPack } from "../src/hsk-pack";
const file = process.argv[2];
const out = process.argv[3];
if (!file || !out) throw new Error("Pass draft path and a diagnostic output path.");
const pack: HskBankPack = JSON.parse(readFileSync(file, "utf8"));
const words = JSON.parse(readFileSync("content/hsk/levels.json", "utf8")).words;
const bad = pack.items.flatMap((q) => [
  { text: q.sentence, py: q.py },
  ...(q.format === "cloze" ? [] : [{ text: q.prompt, py: q.promptPy ?? "" }]),
  ...q.choices.map((c) => ({ text: c.zh, py: c.py })),
  ...(q.segments ?? []).map((c) => ({ text: c.zh, py: c.py })),
].filter((s) => !verifiedBankText(s.text, s.py, words, pack.level)));
writeFileSync(out, bad.map((s) => JSON.stringify(s)).join("\n"));
console.log(`${bad.length} diagnostic fields written; no validation rule changed.`);
