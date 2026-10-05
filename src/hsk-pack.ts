import {
  expectedSyllables,
  syllables,
  pinyinMatches,
  type HskWord,
} from "./packs";

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

/** Exam drills go through the same publish gate as curriculum packs. */
export function validateHskPack(
  raw: unknown,
  words: Record<string, HskWord>,
): string[] {
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
