// Validates content/packs/*.json in curriculum order and publishes the packs
// that pass to src/generated/packs.json (the only file the app reads).
//
//   npm run packs                 check + publish all packs
//   npm run packs -- s1-u03.json  check one pack (and everything before it)
//   npm run packs -- --example    check content/packs/_example.json only
//   npm run packs -- --example --publish   preview the example in the app
//
// Files starting with "_" are ignored (drafts, the example). Errors block a
// pack; warnings are printed but don't block. Exit code 1 if anything failed.
import { existsSync, readdirSync, readFileSync, writeFileSync, mkdirSync } from "node:fs";
import { basePhrases, lessons, readingLessons } from "../src/content";
import { baseCharacters, baseReadings } from "../src/hanzi";
import { isHan, validatePack, type ContentPack, type HskWord, type ValidationContext } from "../src/packs";
import { wordsOf, type DictEntry } from "../src/dictionary";
import { validateHskPack, type HskPracticePack } from "../src/hsk-pack";

const dir = "content/packs";
const args = process.argv.slice(2);
const onlyExample = args.includes("--example");
const only = args.find((a) => a.endsWith(".json"));

const hskFile = "content/hsk/levels.json";
const hsk: Record<string, HskWord> | undefined = existsSync(hskFile)
  ? JSON.parse(readFileSync(hskFile, "utf8")).words
  : undefined;
if (!hsk) console.warn("⚠ content/hsk/levels.json missing: HSK levels and pinyin won't be checked (run: npx tsx scripts/import-hsk.ts).");
const strokeDir = "node_modules/hanzi-writer-data";
const strokeData = existsSync(strokeDir)
  ? new Set(readdirSync(strokeDir).filter((f) => f.endsWith(".json")).map((f) => f.slice(0, -5)))
  : undefined;

const hanOf = (s: string) => Array.from(s).filter(isHan);
// Word-level readability uses the offline dictionary (npm run dict). Without it, the gate
// falls back to the character check only, and says so.
const dict = new Map<string, DictEntry[]>();
if (existsSync("public/dict/manifest.json"))
  for (const f of readdirSync("public/dict").filter((f) => /^\d{3}\.json$/.test(f)))
    for (const [k, v] of Object.entries(JSON.parse(readFileSync(`public/dict/${f}`, "utf8")) as Record<string, DictEntry[]>)) dict.set(k, v);
else console.warn("⚠ public/dict missing: word-level readability isn't checked (run: npm run dict).");
const splitWords = dict.size ? (line: string) => wordsOf(line, (w) => dict.get(w)) : undefined;
const ctx: ValidationContext = {
  knownUnits: new Set([...lessons, ...readingLessons].map((l) => l.id)),
  seenIds: new Set(basePhrases.map((p) => p.id)),
  knownChars: new Set([
    ...basePhrases.flatMap((p) => hanOf(p.hanzi)),
    ...baseCharacters.map((c) => c.hanzi),
    ...baseReadings.flatMap((r) => r.lines.flatMap((l) => hanOf(l.zh))),
  ]),
  knownWords: new Set(basePhrases.map((p) => p.hanzi)),
  hsk,
  strokeData,
  wordsOf: splitWords,
};
// Words the base course has shown: its phrases split into words, its characters, its readings.
if (splitWords) {
  for (const p of basePhrases) for (const w of splitWords(p.hanzi)) ctx.knownWords.add(w);
  for (const c of baseCharacters) ctx.knownWords.add(c.hanzi);
  for (const r of baseReadings) for (const l of r.lines) for (const w of splitWords(l.zh)) ctx.knownWords.add(w);
}

mkdirSync(dir, { recursive: true });
const files = onlyExample
  ? ["_example.json"]
  : readdirSync(dir).filter((f) => f.endsWith(".json") && !f.startsWith("_") && !f.endsWith(".hsk.json"));
type Loaded = { file: string; pack?: ContentPack; parseError?: string };
const loaded: Loaded[] = files.map((file) => {
  try {
    return { file, pack: JSON.parse(readFileSync(`${dir}/${file}`, "utf8")) };
  } catch (e) {
    return { file, parseError: (e as Error).message };
  }
});
loaded.sort((a, b) =>
  a.pack && b.pack ? a.pack.unit?.stage - b.pack.unit?.stage || a.pack.unit?.order - b.pack.unit?.order : a.pack ? -1 : 1,
);

const accepted: ContentPack[] = [];
let failed = 0;
for (const { file, pack, parseError } of loaded) {
  if (parseError || !pack) {
    failed++;
    console.log(`\n✗ ${file}: not valid JSON: ${parseError}`);
    continue;
  }
  const r = validatePack(pack, ctx);
  const label = `${file}  (${pack.unit?.id} · ${pack.unit?.title})`;
  const statText = Object.entries(r.stats).map(([k, v]) => `${k} ${v}`).join(", ");
  if (r.errors.length) {
    failed++;
    console.log(`\n✗ ${label}: ${r.errors.length} error(s), ${r.warnings.length} warning(s)  [${statText}]`);
  } else console.log(`\n✓ ${label}: ok, ${r.warnings.length} warning(s)  [${statText}]`);
  for (const e of r.errors) console.log(`   ✗ ${e}`);
  for (const w of r.warnings) console.log(`   ⚠ ${w}`);
  if (only && file === only) break;
  if (r.errors.length) continue;
  // Publish and extend the context for later packs.
  accepted.push(pack);
  ctx.knownUnits.add(pack.unit.id);
  ctx.knownUnits.add(`${pack.unit.id}-usage`);
  const ids = [
    pack.unit.id,
    ...pack.vocabulary.map((v) => v.id),
    ...(pack.grammar ?? []).map((g) => g.id),
    pack.dialogue?.id,
    pack.reading?.id,
    ...(pack.extraReadings ?? []).map((r) => r.id),
    pack.conversation?.id,
  ].filter((x): x is string => !!x);
  ids.forEach((id) => ctx.seenIds.add(id));
  for (const v of pack.vocabulary) {
    ctx.knownWords.add(v.hanzi);
    hanOf(v.hanzi).forEach((c) => ctx.knownChars.add(c));
  }
  for (const c of pack.characters ?? []) ctx.knownChars.add(c.hanzi);
  const texts = [pack.dialogue, pack.reading, ...(pack.extraReadings ?? [])];
  for (const t of texts) t?.lines.forEach((l) => hanOf(l.zh).forEach((c) => ctx.knownChars.add(c)));
  // After a unit, its glossed words and the words of its texts count as met.
  for (const t of texts) for (const g of t?.glosses ?? []) ctx.knownWords.add(g.hanzi);
  if (splitWords)
    for (const l of [...texts.flatMap((t) => t?.lines ?? []), ...(pack.grammar ?? []).flatMap((g) => g.examples)])
      for (const w of splitWords(l.zh)) ctx.knownWords.add(w);
}

// --example --publish: load the example into the app to preview the format (undo with `npm run packs`).
if (onlyExample && args.includes("--publish")) {
  mkdirSync("src/generated", { recursive: true });
  writeFileSync("src/generated/packs.json", JSON.stringify(accepted));
  console.log(`
Preview: published the example pack. Run \`npm run packs\` to restore the real set.`);
}
if (!onlyExample && !only) {
  mkdirSync("src/generated", { recursive: true });
  writeFileSync("src/generated/packs.json", JSON.stringify(accepted));
  console.log(`\nPublished ${accepted.length} of ${loaded.length} pack(s) to src/generated/packs.json.`);
}
if (!onlyExample && !only) {
  const hskPacks: HskPracticePack[] = [];
  for (const file of readdirSync(dir).filter(f => f.endsWith(".hsk.json") && !f.startsWith("_"))) {
    try {
      const pack = JSON.parse(readFileSync(`${dir}/${file}`, "utf8"));
      const errors = validateHskPack(pack, hsk ?? {});
      if (errors.length) throw new Error(errors.join("\n"));
      hskPacks.push(pack);
      console.log(`Validated ${file}: ${pack.items.length} HSK practice items.`);
    } catch (error) { failed++; console.error(`${file}: ${String(error)}`); }
  }
  if (!failed) writeFileSync("src/generated/hsk-practice.json", JSON.stringify(hskPacks));
}
if (failed) {
  console.log(`${failed} pack(s) have errors and were not published. Fix them (or ask ChatGPT with Prompt 4) and run again.`);
  process.exitCode = 1;
}
