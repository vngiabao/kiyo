import {
  expectedSyllables,
  syllables,
  pinyinMatches,
  type HskWord,
} from "./packs";
import { normalizePinyinReference } from "./pinyin-reference";

export interface HskChoice {
  zh: string;
  py: string;
  en: string;
}
export interface HskItem {
  id: string;
  unit: "identity" | "numbers" | "daily" | "sample";
  prompt: string;
  sentence: string;
  py: string;
  en: string;
  choices: HskChoice[];
  answer: string;
  explanation: string;
  format?: "cloze" | "reading" | "listening" | "ordering";
  promptPy?: string;
  segments?: HskChoice[];
}
export interface HskPracticePack {
  kind: "hsk-practice";
  version: 1;
  id: string;
  standard: "HSK 2.0";
  level: 1;
  provenance: { author: string; status: string; sources: string[] };
  items: HskItem[];
}
export interface HskBankPack {
  kind: "hsk-practice";
  version: 2;
  id: string;
  standard: "GF2021 practice";
  level: 1 | 2 | 3 | 4 | 5 | 6;
  provenance: HskPracticePack["provenance"];
  items: HskItem[];
}
export type AnyHskPack = HskPracticePack | HskBankPack;

/** Exam drills go through the same publish gate as curriculum packs. */
export function validateHskPack(
  raw: unknown,
  words: Record<string, HskWord>,
): string[] {
  if ((raw as HskBankPack)?.version === 2) return validateBank(raw, words);
  const errors: string[] = [];
  const p = raw as HskPracticePack;
  if (
    !p ||
    p.kind !== "hsk-practice" ||
    p.version !== 1 ||
    p.standard !== "HSK 2.0" ||
    p.level !== 1 ||
    !Array.isArray(p.items)
  )
    return ["Invalid HSK practice pack schema/version"];
  if (
    !p.provenance?.author ||
    !p.provenance.status ||
    !p.provenance.sources?.length
  )
    errors.push("Missing provenance");
  const ids = new Set<string>();
  for (const q of p.items) {
    if (!q.id || ids.has(q.id))
      errors.push(`Duplicate/missing question id: ${q.id}`);
    ids.add(q.id);
    if (!["identity", "numbers", "daily", "sample"].includes(q.unit))
      errors.push(`${q.id}: unknown unit`);
    if (
      ![q.prompt, q.sentence, q.py, q.en, q.answer, q.explanation].every(
        (s) => typeof s === "string" && s.trim(),
      )
    ) {
      errors.push(`${q.id}: missing text`);
      continue;
    }
    if (
      q.prompt.split("___").length !== 2 ||
      q.prompt.replace("___", q.answer) !== q.sentence
    )
      errors.push(`${q.id}: blank/answer mismatch`);
    if (syllables(q.py).length !== expectedSyllables(q.sentence, q.py))
      errors.push(`${q.id}: sentence pinyin length`);
    if (!Array.isArray(q.choices) || q.choices.length !== 4) {
      errors.push(`${q.id}: need four choices`);
      continue;
    }
    if (
      new Set(q.choices.map((c) => c.zh)).size !== 4 ||
      q.choices.filter((c) => c.zh === q.answer).length !== 1
    )
      errors.push(`${q.id}: duplicate/absent answer`);
    for (const c of q.choices) {
      const reference = words[c.zh];
      if (!c.en || !c.py || !reference || reference.old !== 1)
        errors.push(`${q.id}: ${c.zh} is not verified legacy HSK 1 vocabulary`);
      else if (!reference.pinyin.some((py) => pinyinMatches(c.zh, c.py, py)))
        errors.push(`${q.id}: wrong pinyin for ${c.zh}`);
    }
    // Segment every Chinese run against the imported legacy-level list.
    for (const run of q.sentence.match(/[\p{Script=Han}]+/gu) ?? []) {
      const reachable = new Set([0]);
      for (let i = 0; i < run.length; i++)
        if (reachable.has(i))
          for (let j = i + 1; j <= run.length; j++)
            if (words[run.slice(i, j)]?.old === 1) reachable.add(j);
      if (!reachable.has(run.length))
        errors.push(`${q.id}: unverified HSK 1 text ${run}`);
    }
  }
  for (const unit of ["identity", "numbers", "daily", "sample"])
    if (p.items.filter((q) => q.unit === unit).length < 8)
      errors.push(`${unit}: at least eight items required`);
  return errors;
}

/** Require an actual dictionary reading and level for every connected word. */
export function verifiedBankText(
  text: string,
  py: string,
  words: Record<string, HskWord>,
  level: number,
): boolean {
  if (!text?.trim() || !py?.trim()) return false;
  const chars = Array.from(text).filter((c) => /\p{Script=Han}/u.test(c));
  const sounds = syllables(py);
  if (!chars.length || sounds.length !== expectedSyllables(text, py)) return false;
  const reachable = new Set(["0:0"]);
  for (let ci = 0; ci < chars.length; ci++)
    for (let si = 0; si < sounds.length; si++) {
      if (!reachable.has(`${ci}:${si}`)) continue;
      for (let end = ci + 1; end <= Math.min(ci + 8, chars.length); end++) {
        const word = chars.slice(ci, end).join("");
        const ref = words[word];
        if (!ref || typeof ref.hsk3 !== "number" || ref.hsk3 > level) continue;
        for (const rawReading of ref.pinyin) {
          const reading = normalizePinyinReference(rawReading);
          const length = syllables(reading).length;
          if (length && pinyinMatches(word, sounds.slice(si, si + length).join(" "), reading))
            reachable.add(`${end}:${si + length}`);
        }
      }
    }
  return reachable.has(`${chars.length}:${sounds.length}`);
}

function validateBank(raw: unknown, words: Record<string, HskWord>): string[] {
  const p = raw as HskBankPack;
  if (!p || p.kind !== "hsk-practice" || p.version !== 2 ||
      p.standard !== "GF2021 practice" || ![1, 2, 3, 4, 5, 6].includes(p.level) ||
      !p.id?.trim() || !Array.isArray(p.items)) return ["Invalid HSK bank schema/version"];
  const errors: string[] = [];
  if (!p.provenance?.author || !p.provenance.status || !p.provenance.sources?.length)
    errors.push("Missing provenance");
  const ids = new Set<string>();
  for (const q of p.items) {
    if (!q.id || ids.has(q.id)) errors.push(`Duplicate/missing question id: ${q.id}`);
    ids.add(q.id);
    if (!["identity", "numbers", "daily", "sample"].includes(q.unit)) errors.push(`${q.id}: unknown unit`);
    if (!["cloze", "reading", "listening", "ordering"].includes(q.format ?? "")) errors.push(`${q.id}: unknown format`);
    if (![q.prompt, q.sentence, q.py, q.en, q.answer, q.explanation].every((s) => typeof s === "string" && s.trim())) {
      errors.push(`${q.id}: missing text`); continue;
    }
    if (!verifiedBankText(q.sentence, q.py, words, p.level)) errors.push(`${q.id}: unverified sentence level/pinyin`);
    if (!Array.isArray(q.choices) || q.choices.length !== 4) { errors.push(`${q.id}: need four choices`); continue; }
    if (new Set(q.choices.map((c) => c.zh)).size !== 4 || q.choices.filter((c) => c.zh === q.answer).length !== 1)
      errors.push(`${q.id}: duplicate/absent answer`);
    for (const c of q.choices)
      if (!c.en?.trim() || !verifiedBankText(c.zh, c.py, words, p.level)) errors.push(`${q.id}: unverified choice ${c.zh}`);
    if (q.format === "cloze") {
      if (q.prompt.split("___").length !== 2 || q.prompt.replace("___", q.answer) !== q.sentence)
        errors.push(`${q.id}: blank/answer mismatch`);
    } else if (!verifiedBankText(q.prompt, q.promptPy ?? "", words, p.level)) errors.push(`${q.id}: unverified question level/pinyin`);
    if (q.format === "ordering") {
      if (!q.segments || q.segments.length < 3 || q.segments.length > 6 ||
          q.segments.map((c) => c.zh).join("") !== q.answer || q.sentence !== q.answer)
        errors.push(`${q.id}: ordering segments/answer mismatch`);
      for (const c of q.segments ?? [])
        if (!c.en?.trim() || !verifiedBankText(c.zh, c.py, words, p.level)) errors.push(`${q.id}: unverified ordering segment`);
      const letters = (text: string) => Array.from(text).filter((c) => /\p{Script=Han}/u.test(c)).sort().join("");
      for (const c of q.choices)
        if (letters(c.zh) !== letters(q.answer)) errors.push(`${q.id}: ordering choice changes the supplied characters`);
    } else if (q.segments) errors.push(`${q.id}: unexpected ordering segments`);
  }
  for (const unit of ["identity", "numbers", "daily", "sample"])
    if (p.items.filter((q) => q.unit === unit).length < 8) errors.push(`${unit}: at least eight items required`);
  return errors;
}
