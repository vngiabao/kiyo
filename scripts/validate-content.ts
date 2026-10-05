import { existsSync, readFileSync } from "node:fs";
import hskPacks from "../src/generated/hsk-practice.json";
import { validateHskPack } from "../src/hsk-pack";
import audio from "../src/audio-assets.json";
import {
  lessons,
  phrases,
  basePhrases,
  packLessons,
  allLessons,
  phraseById,
  exercisesFor,
  readingLessons,
} from "../src/content";
import { characters, baseCharacters, readings, glossFor, isHan } from "../src/hanzi";
import { checkTask, plain } from "../src/tasks";
export function validateContent() {
  const errors: string[] = [];
  const hskWords = JSON.parse(readFileSync("content/hsk/levels.json", "utf8")).words;
  for (const pack of hskPacks) errors.push(...validateHskPack(pack, hskWords));
  const phraseIds = new Set<string>(),
    texts = new Set<string>();
  for (const p of phrases) {
    if (phraseIds.has(p.id)) errors.push(`Duplicate phrase id ${p.id}`);
    phraseIds.add(p.id);
  }
  for (const p of basePhrases) {
    if (texts.has(p.hanzi))
      errors.push(`Duplicate phrase ${p.id}`);
    texts.add(p.hanzi);
    for (const key of [
      "hanzi",
      "traditional",
      "pinyin",
      "meaning",
      "vi",
      "usage",
    ] as const)
      if (!p[key].trim()) errors.push(`${p.id}: missing ${key}`);
    if (!/^[a-züāáǎàēéěèīíǐìōóǒòūúǔùǖǘǚǜ\s]+$/i.test(p.pinyin))
      errors.push(`${p.id}: invalid pinyin characters`);
    if (p.tones.some((t) => t < 1 || t > 5))
      errors.push(`${p.id}: invalid tone`);
    if (p.audio.text !== p.hanzi)
      errors.push(`${p.id}: missing or mismatched speech text`);
    if (!p.provenance.status || !p.provenance.version)
      errors.push(`${p.id}: missing provenance`);
    if (p.utilityScore < 0 || p.utilityScore > 100)
      errors.push(`${p.id}: invalid utility score`);
  }
  for (const voices of Object.values(audio))
    for (const file of Object.values(voices))
      if (!existsSync("public" + file))
        errors.push(`Missing audio asset: ${file}`);
  // Bundled audio is required for the base course; content packs fall back to device voices until generated.
  for (const p of basePhrases)
    if (!(p.hanzi in audio)) errors.push(`${p.id}: no bundled audio`);
  const seen = new Set<string>();
  for (const l of lessons) {
    if (seen.has(l.id)) errors.push(`Duplicate lesson ${l.id}`);
    for (const req of l.prerequisites)
      if (!seen.has(req))
        errors.push(`${l.id}: missing or forward prerequisite ${req}`);
    seen.add(l.id);
    for (const id of l.phrases)
      if (!phraseById[id]) errors.push(`${l.id}: unknown phrase ${id}`);
    if (l.phrases.length < 4) errors.push(`${l.id}: insufficient seed content`);
    for (const e of exercisesFor(l)) {
      if (!phraseById[e.phraseId]) errors.push(`${e.id}: broken reference`);
      if (
        e.choices &&
        (new Set(e.choices).size !== e.choices.length ||
          !e.choices.includes(e.correct!))
      )
        errors.push(`${e.id}: invalid choices or missing answer`);
      if (
        e.tokens &&
        Array.from(e.tokens.join("")).sort().join("") !==
          Array.from(e.correct!).sort().join("")
      )
        errors.push(`${e.id}: impossible assembly`);
      if (e.task) errors.push(...checkTask(e.task, new Set(l.phrases)));
    }
  }
  // Content-pack lessons (already checked in depth by scripts/build-packs.ts)
  for (const l of packLessons) {
    for (const id of l.phrases) if (!phraseById[id]) errors.push(`${l.id}: unknown phrase ${id}`);
    for (const e of exercisesFor(l)) {
      if (!phraseById[e.phraseId]) errors.push(`${e.id}: broken reference`);
      if (e.choices && (new Set(e.choices).size !== e.choices.length || !e.choices.includes(e.correct!)))
        errors.push(`${e.id}: invalid choices or missing answer`);
      if (e.tokens && Array.from(e.tokens.join("")).sort().join("") !== Array.from(e.correct!).sort().join(""))
        errors.push(`${e.id}: impossible assembly`);
    }
  }
  // Characters-first track
  const pinyinOk = /^[a-züāáǎàēéěèīíǐìōóǒòūúǔùǖǘǚǜ\s']+$/i;
  const charSeen = new Set<string>();
  for (const c of characters) {
    if (charSeen.has(c.hanzi)) errors.push(`Duplicate character ${c.hanzi}`);
    charSeen.add(c.hanzi);
    if (Array.from(c.hanzi).length !== 1) errors.push(`${c.id}: not one character`);
    if (!pinyinOk.test(c.pinyin)) errors.push(`${c.id}: invalid pinyin`);
    if (!c.meaning.trim() || !c.note.trim()) errors.push(`${c.id}: missing meaning or note`);
    if (!c.parts.length) errors.push(`${c.id}: no parts`);
    if (c.strokes < 1 || c.strokes > 30) errors.push(`${c.id}: implausible stroke count`);
    if (!existsSync(`public/hanzi/${c.hanzi}.json`)) errors.push(`${c.id}: no stroke data`);
    if (baseCharacters.includes(c) && !(c.say in audio)) errors.push(`${c.id}: no bundled audio for ${c.say}`);
    for (const w of c.words)
      if (!w.w.includes(c.hanzi) || !w.p.trim() || !w.m.trim())
        errors.push(`${c.id}: bad example word ${w.w}`);
  }
  const taught = new Set<string>();
  for (const l of readingLessons) {
    if (l.phrases.length < 6 || l.phrases.length > 10) errors.push(`${l.id}: expected 6–10 characters`);
    for (const id of l.phrases) {
      if (!phraseById[id]) errors.push(`${l.id}: unknown character ${id}`);
      if (taught.has(id)) errors.push(`${l.id}: ${id} taught twice`);
      taught.add(id);
    }
    for (const e of exercisesFor(l)) {
      if (!phraseById[e.phraseId]) errors.push(`${e.id}: broken reference`);
      if (e.choices && (new Set(e.choices).size !== e.choices.length || !e.choices.includes(e.correct!)))
        errors.push(`${e.id}: invalid choices or missing answer`);
    }
  }
  for (const r of readings) {
    if (!allLessons.some((l) => l.id === r.after)) errors.push(`${r.id}: unknown lesson ${r.after}`);
    const curated = readingLessons.some((l) => l.id === r.after);
    for (const line of r.lines) {
      if (!line.py.trim() || !line.en.trim()) errors.push(`${r.id}: incomplete line`);
      if (curated && !(line.zh in audio)) errors.push(`${r.id}: no audio for ${line.zh}`);
      for (const ch of Array.from(line.zh).filter(isHan))
        if (!glossFor(ch)) errors.push(`${r.id}: no gloss for ${ch}`);
    }
    for (const q of r.questions)
      if (new Set(q.choices).size !== q.choices.length || !q.choices.includes(q.answer))
        errors.push(`${r.id}: invalid question “${q.q}”`);
    if (r.cloze) {
      errors.push(...checkTask({ type: "cloze", id: `${r.id}-lock`, phrase: "", title: r.title, lines: r.cloze.lines, bank: r.cloze.bank }));
      for (const l of r.cloze.lines)
        if (!r.lines.some((x) => x.zh === plain(l.zh))) errors.push(`${r.id}: gap-fill line “${plain(l.zh)}” is not a line of the text`);
    }
  }
  return errors;
}
const errors = validateContent();
if (errors.length) {
  console.error(errors.join("\n"));
  process.exitCode = 1;
} else
  console.log(
    `Validated ${phrases.length} phrases, ${characters.length} characters, ${readings.length} readings, ${allLessons.length} lessons (${packLessons.length} from content packs) and ${allLessons.reduce((n, l) => n + exercisesFor(l).length, 0)} exercise steps. Linguistic/native review remains a human publishing gate.`,
  );
