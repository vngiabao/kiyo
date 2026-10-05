/**
 * Content packs: one curriculum unit as data (see prompts/content-prompt.md).
 *
 * Pipeline: content/packs/*.json → scripts/build-packs.ts (validatePack) →
 * src/generated/packs.json (only packs without errors) → compilePack() turns
 * each into the app's own phrases, characters, lessons, readings, grammar and
 * conversation scenarios. Pure functions; no file or browser access here.
 */
import type { Lesson, Phrase, Provenance, Task } from "./types";
import { checkTask, plain, taskAudio } from "./tasks";

// ---------- Schema ----------
export type Register = "casual" | "neutral" | "polite" | "formal" | "written" | "internet";
export interface Line { zh: string; py: string; en: string; speaker?: string }
export interface Question { type?: string; q: string; choices: string[]; answer: string }
export interface PackVocab {
  id: string;
  hanzi: string;
  traditional?: string;
  pinyin: string;
  pos?: string;
  meaning: string;
  meaningVi?: string;
  register?: Register;
  measureWord?: string;
  isChunk?: boolean;
  hskLevel?: number | null;
  example: Line;
  collocations?: string[];
  usageNote?: string;
  confusableWith?: string[];
}
export interface PackCharacter {
  hanzi: string;
  pinyin: string;
  meaning: string;
  strokes: number;
  parts: { form: string; role: "whole" | "meaning" | "sound" | "shape"; gloss: string }[];
  noteKind: "origin" | "memory aid" | "traditional explanation" | "usage";
  note: string;
  words: { w: string; p: string; m: string }[];
}
export interface PackGrammar {
  id: string;
  pattern: string;
  purpose: string;
  explanation: string;
  examples: Line[];
  commonMistakes?: { wrong: string; right: string; why: string }[];
  contrastWith?: string;
  register?: Register;
}
export interface PackText {
  id: string;
  title: string;
  titleZh?: string;
  blurb?: string;
  setting?: string;
  format?: string;
  register?: Register;
  speakers?: { id: string; name: string }[];
  lines: Line[];
  glosses?: { hanzi: string; pinyin: string; meaning: string }[];
  questions?: Question[];
  /** Readings: what the learner reads to find out (shown before the text). */
  purpose?: string;
  /** Readings: "lock it in" gap-fill; every line must be a line of the text with 【blanks】. */
  cloze?: { lines: Line[]; bank: string[] };
}
export interface PackConversation {
  id: string;
  title: string;
  place: string;
  context: string;
  goal: string;
  partner?: { name: string; persona?: string };
  turns: { text: string; pinyin: string; meaning: string; intent: string; examples: string[]; accept?: string[] }[];
  aiPartnerBrief?: string;
}
export interface PackPragmatics {
  situation: string;
  natural: { zh: string; py: string; en?: string };
  tooFormal?: { zh: string; py: string };
  tooBlunt?: { zh: string; py: string };
  note?: string;
}
export interface ContentPack {
  packVersion: 1;
  unit: {
    id: string;
    stage: number;
    order: number;
    title: string;
    titleZh?: string;
    canDo: string[];
    hskTarget?: { standard: string; level: number };
    prerequisites?: string[];
    estimatedMinutes?: number;
  };
  vocabulary: PackVocab[];
  characters?: PackCharacter[];
  grammar?: PackGrammar[];
  dialogue?: PackText;
  reading?: PackText;
  conversation?: PackConversation;
  pragmatics?: PackPragmatics[];
  review?: { type: string; prompt: string; zh?: string; choices?: string[]; answer?: string }[];
  /**
   * Practice in exam formats (see src/tasks.ts): truefalse, reply, listenfill,
   * cloze, match, or an extra dialogue. Each task's "phrase" is a vocabulary id.
   * The unit's dialogue becomes a listening task on its own when it has questions.
   */
  tasks?: Task[];
  notes?: string;
}

// ---------- Pinyin helpers ----------
const V = "aeiouüvāáǎàēéěèīíǐìōóǒòūúǔùǖǘǚǜ";
const syllableRe = new RegExp(
  `(zh|ch|sh|[bpmfdtnlgkhjqxrzcsyw])?[${V}]+(?:ng(?![${V}])|n(?![${V}]))?(?:r(?![${V}]))?`,
  "gi",
);
const marks = ["āēīōūǖ", "áéíóúǘ", "ǎěǐǒǔǚ", "àèìòùǜ"];
export const toneOfSyllable = (s: string) => {
  const lower = s.toLowerCase();
  for (let t = 0; t < 4; t++) if ([...lower].some((c) => marks[t].includes(c))) return t + 1;
  return 5;
};
export const syllables = (py: string) => py.match(syllableRe) ?? [];
export const isHan = (ch: string) => /\p{Script=Han}/u.test(ch);
export const hanCount = (zh: string) => Array.from(zh).filter(isHan).length;
/** Pinyin syllables expected for a Chinese string (儿 after a syllable is usually -r). */
export function expectedSyllables(zh: string, py: string) {
  // Erhua: a syllable ending in -r (diǎnr, zhèr) carries the 儿; a standalone ér/èr does not.
  const erhua = syllables(py).filter((s) => /r$/i.test(s) && !/^[eēéěè]r$/i.test(s)).length;
  return hanCount(zh) - Math.min(erhua, (zh.match(/儿/g) ?? []).length);
}
const pinyinChars = new RegExp(`^[a-z${V}${V.toUpperCase()}ĀÁǍÀĒÉĚÈĪÍǏÌŌÓǑÒŪÚǓÙǕǗǙǛ'’\\s,.!?;:"“”‘’·…—-]+$`, "i");
/** Compare authored pinyin with a reference, tolerating 一/不 tone changes, neutral-tone variants, spacing and case. */
export function pinyinMatches(hanzi: string, authored: string, reference: string) {
  const norm = (s: string) => s.toLowerCase().replace(/[\s'’]/g, "");
  if (norm(authored) === norm(reference)) return true;
  const a = syllables(authored).map((s) => s.toLowerCase()),
    b = syllables(reference.replace(/\s+r\b/g, "r")).map((s) => s.toLowerCase());
  if (a.length !== b.length) return false;
  const chars = Array.from(hanzi).filter(isHan);
  const bare = (s: string) => s.normalize("NFD").replace(/[̀-ͯ]/g, "");
  return a.every((s, i) => {
    if (s === b[i]) return true;
    if (bare(s) !== bare(b[i])) return false;
    const ch = chars[i];
    if (ch === "一" || ch === "不") return true; // spoken tone change
    return toneOfSyllable(s) === 5 || toneOfSyllable(b[i]) === 5; // neutral-tone variants
  });
}

// ---------- Validation ----------
export interface HskWord { hsk3?: number; old?: number; pinyin: string[] }
export interface ValidationContext {
  /** Unit ids and lesson ids that exist before this pack. */
  knownUnits: Set<string>;
  /** Every id used so far (across packs). */
  seenIds: Set<string>;
  /** Characters the learner has met before this pack (base course + earlier packs). */
  knownChars: Set<string>;
  /** Words taught before this pack. */
  knownWords: Set<string>;
  /** Official word list, if available. */
  hsk?: Record<string, HskWord>;
  /** Characters with stroke data available. */
  strokeData?: Set<string>;
}
export interface Report { errors: string[]; warnings: string[]; stats: Record<string, number | string> }

const registers = ["casual", "neutral", "polite", "formal", "written", "internet"];
const isStr = (v: unknown): v is string => typeof v === "string" && v.trim().length > 0;

export function validatePack(raw: unknown, ctx: ValidationContext): Report {
  const errors: string[] = [],
    warnings: string[] = [],
    stats: Report["stats"] = {};
  const err = (m: string) => errors.push(m),
    warn = (m: string) => warnings.push(m);
  if (!raw || typeof raw !== "object") return { errors: ["Not a JSON object."], warnings, stats };
  const p = raw as ContentPack;
  if (p.packVersion !== 1) err("packVersion must be 1.");
  const u = p.unit;
  if (!u || !isStr(u.id) || !/^s\d+-u\d+$/.test(u.id)) {
    err('unit.id must look like "s1-u03".');
    return { errors, warnings, stats };
  }
  const prefix = u.id + "-";
  if (ctx.knownUnits.has(u.id) || ctx.seenIds.has(u.id)) err(`Duplicate unit id ${u.id}.`);
  for (const k of ["title", "titleZh"] as const) if (k === "title" && !isStr(u[k])) err(`unit.${k} missing.`);
  if (!Number.isInteger(u.stage) || u.stage < 1) err("unit.stage must be a positive integer.");
  if (!Number.isInteger(u.order) || u.order < 1) err("unit.order must be a positive integer.");
  if (!Array.isArray(u.canDo) || !u.canDo.length) err("unit.canDo needs at least one goal.");
  for (const pre of u.prerequisites ?? [])
    if (!ctx.knownUnits.has(pre)) err(`Prerequisite ${pre} doesn't exist (or comes later).`);

  const ids = new Set<string>();
  const claim = (id: unknown, where: string) => {
    if (!isStr(id)) return err(`${where}: missing id.`);
    if (!id.startsWith(prefix)) err(`${where}: id "${id}" must start with "${prefix}".`);
    if (ids.has(id) || ctx.seenIds.has(id)) err(`${where}: duplicate id "${id}".`);
    ids.add(id);
  };
  const checkLine = (l: Line | undefined, where: string, strictPinyin = true) => {
    if (!l || !isStr(l.zh) || !isStr(l.py) || !isStr(l.en)) return err(`${where}: needs zh, py and en.`);
    if (!pinyinChars.test(l.py)) err(`${where}: pinyin has characters that aren't pinyin: "${l.py}".`);
    const got = syllables(l.py).length,
      want = expectedSyllables(l.zh, l.py);
    if (got !== want) (strictPinyin ? err : warn)(`${where}: ${want} characters but ${got} pinyin syllables ("${l.zh}" / "${l.py}").`);
  };
  const checkQuestions = (qs: Question[] | undefined, where: string) => {
    (qs ?? []).forEach((q, i) => {
      if (!isStr(q.q) || !Array.isArray(q.choices) || !isStr(q.answer)) return err(`${where} question ${i + 1}: needs q, choices, answer.`);
      if (new Set(q.choices).size !== q.choices.length) err(`${where} question ${i + 1}: duplicate choices.`);
      if (q.choices.filter((c) => c === q.answer).length !== 1) err(`${where} question ${i + 1}: answer must appear exactly once in choices.`);
      if (q.choices.length < 3) warn(`${where} question ${i + 1}: fewer than 3 choices.`);
    });
  };

  // Vocabulary
  const vocab = Array.isArray(p.vocabulary) ? p.vocabulary : [];
  if (!vocab.length) err("vocabulary is empty.");
  const newWords = new Set<string>();
  let offList = 0;
  vocab.forEach((v, i) => {
    const where = `vocabulary[${i}] ${v?.hanzi ?? ""}`;
    claim(v?.id, where);
    if (!isStr(v?.hanzi) || ![...v.hanzi].some(isHan)) return err(`${where}: hanzi missing.`);
    if (!isStr(v.meaning)) err(`${where}: meaning missing.`);
    if (!isStr(v.pinyin)) return err(`${where}: pinyin missing.`);
    if (!pinyinChars.test(v.pinyin)) err(`${where}: invalid pinyin "${v.pinyin}".`);
    const got = syllables(v.pinyin).length,
      want = expectedSyllables(v.hanzi, v.pinyin);
    if (got !== want) err(`${where}: ${want} characters but ${got} pinyin syllables ("${v.pinyin}").`);
    if (v.register && !registers.includes(v.register)) err(`${where}: unknown register "${v.register}".`);
    if (newWords.has(v.hanzi)) err(`${where}: listed twice in this pack.`);
    newWords.add(v.hanzi);
    if (ctx.knownWords.has(v.hanzi)) warn(`${where}: already taught earlier; reuse it instead of re-teaching.`);
    checkLine(v.example, `${where} example`);
    if (v.example && isStr(v.example.zh) && !v.example.zh.includes(v.hanzi)) warn(`${where}: example sentence doesn't contain the word.`);
    const official = ctx.hsk?.[v.hanzi];
    if (ctx.hsk) {
      if (!official) {
        offList++;
        if (v.hskLevel) err(`${where}: says HSK ${v.hskLevel}, but it isn't on the HSK 3.0 list. Set hskLevel to null.`);
      } else {
        if (v.hskLevel != null && official.hsk3 && v.hskLevel !== official.hsk3)
          err(`${where}: says HSK ${v.hskLevel}; the HSK 3.0 list says ${official.hsk3 === 7 ? "7–9" : official.hsk3}.`);
        if (official.pinyin.length && !official.pinyin.some((r) => pinyinMatches(v.hanzi, v.pinyin, r)))
          warn(`${where}: pinyin "${v.pinyin}" differs from the reference (${official.pinyin.join(" / ")}). Check it.`);
      }
    }
  });
  if (ctx.hsk && vocab.length && offList / vocab.length > 0.15)
    warn(`${offList} of ${vocab.length} words aren't on the HSK 3.0 list (over 15%). Fine for chunks, but check.`);
  stats.newWords = vocab.length;

  // Characters
  (p.characters ?? []).forEach((c, i) => {
    const where = `characters[${i}] ${c?.hanzi ?? ""}`;
    if (!isStr(c?.hanzi) || Array.from(c.hanzi).length !== 1 || !isHan(c.hanzi)) return err(`${where}: must be one Chinese character.`);
    if (!isStr(c.pinyin) || syllables(c.pinyin).length !== 1) err(`${where}: pinyin must be one syllable.`);
    if (!isStr(c.meaning) || !isStr(c.note)) err(`${where}: meaning and note required.`);
    if (!Number.isInteger(c.strokes) || c.strokes < 1 || c.strokes > 40) err(`${where}: implausible stroke count.`);
    if (!Array.isArray(c.parts) || !c.parts.length) err(`${where}: parts required.`);
    for (const part of c.parts ?? [])
      if (!["whole", "meaning", "sound", "shape"].includes(part.role)) err(`${where}: part role "${part.role}" invalid.`);
    if (!["origin", "memory aid", "traditional explanation", "usage"].includes(c.noteKind)) err(`${where}: noteKind invalid.`);
    if (ctx.strokeData && !ctx.strokeData.has(c.hanzi)) warn(`${where}: no stroke-order data; it will show as a plain glyph.`);
  });

  // Grammar
  (p.grammar ?? []).forEach((g, i) => {
    const where = `grammar[${i}] ${g?.pattern ?? ""}`;
    claim(g?.id, where);
    if (!isStr(g.pattern) || !isStr(g.purpose) || !isStr(g.explanation)) err(`${where}: pattern, purpose and explanation required.`);
    if (isStr(g.explanation) && g.explanation.split(/\s+/).length > 90) warn(`${where}: explanation is long (keep it under ~70 words).`);
    if (!Array.isArray(g.examples) || g.examples.length < 2) err(`${where}: at least 2 examples.`);
    (g.examples ?? []).forEach((ex, j) => checkLine(ex, `${where} example ${j + 1}`));
  });

  // Texts
  const texts: [PackText | undefined, string][] = [[p.dialogue, "dialogue"], [p.reading, "reading"]];
  for (const [t, name] of texts) {
    if (!t) continue;
    claim(t.id, name);
    if (!isStr(t.title)) err(`${name}: title required.`);
    if (!Array.isArray(t.lines) || !t.lines.length) err(`${name}: lines required.`);
    (t.lines ?? []).forEach((l, i) => checkLine(l, `${name} line ${i + 1}`, false));
    if (t.speakers?.length)
      for (const l of t.lines ?? [])
        if (l.speaker && !t.speakers.some((s) => s.id === l.speaker)) err(`${name}: speaker "${l.speaker}" not in speakers.`);
    checkQuestions(t.questions, name);
    if (t.cloze) {
      for (const problem of checkTask({ type: "cloze", id: `${t.id}-lock`, phrase: "", title: t.title, lines: t.cloze.lines, bank: t.cloze.bank })) err(`${name}: ${problem}`);
      for (const l of t.cloze.lines)
        if (!(t.lines ?? []).some((x) => x.zh === plain(l.zh))) err(`${name}: gap-fill line "${plain(l.zh)}" isn't a line of the text.`);
    }
  }
  if (!p.dialogue && !p.reading) warn("No dialogue or reading: the unit has no connected text to read or hear.");
  if (p.dialogue && !(p.dialogue.questions ?? []).length) warn("dialogue: add 2–3 questions (gist, detail, intent) so it becomes a listening task.");

  // Practice tasks
  const vocabIds = new Set(vocab.map((v) => v.id));
  for (const task of p.tasks ?? []) {
    if (!task || typeof task !== "object" || !isStr(task.id)) {
      err("tasks: each task needs an id.");
      continue;
    }
    claim(task.id, "tasks");
    for (const problem of checkTask(task, vocabIds)) err(problem);
    const lines = task.type === "dialogue" ? task.lines : task.type === "cloze" ? task.lines : task.type === "truefalse" ? [task.audio] : task.type === "reply" ? [task.prompt] : task.type === "listenfill" ? [task.line] : task.type === "match" ? task.pairs.map((x) => x.right) : [];
    lines.forEach((l, i) => checkLine({ ...l, zh: plain(l.zh), en: l.en || "-" }, `task ${task.id} line ${i + 1}`));
  }
  if (!(p.tasks ?? []).length) warn("No practice tasks: add truefalse / reply / listenfill and a cloze so words are used in new sentences.");

  // Coverage: characters in the texts the learner should already know (proxy for word coverage).
  const glossChars = new Set([...(p.dialogue?.glosses ?? []), ...(p.reading?.glosses ?? [])].flatMap((g) => Array.from(g.hanzi)));
  const known = new Set([...ctx.knownChars, ...[...newWords].flatMap((w) => Array.from(w)), ...(p.characters ?? []).map((c) => c.hanzi)]);
  for (const [t, name] of texts) {
    if (!t) continue;
    const chars = (t.lines ?? []).flatMap((l) => Array.from(l.zh ?? "").filter(isHan));
    const own = new Set((t.glosses ?? []).flatMap((g) => Array.from(g.hanzi)));
    const missing = [...new Set(chars.filter((c) => !known.has(c) && !own.has(c)))];
    if (missing.length) err(`${name}: no meaning available for ${missing.join("")}. Add them to ${name}.glosses (names too, e.g. 陈宇 = "Chen Yu, a name").`);
  }
  const textChars = [...(p.dialogue?.lines ?? []), ...(p.reading?.lines ?? [])].flatMap((l) => Array.from(l.zh ?? "").filter(isHan));
  if (textChars.length) {
    const outside = textChars.filter((c) => !known.has(c));
    const coverage = Math.round((100 * (textChars.length - outside.length)) / textChars.length);
    stats.coverage = `${coverage}%`;
    const list = [...new Set(outside)].join("");
    if (coverage < 85) err(`Only ${coverage}% of characters in the dialogue/reading are known or new this unit (need ≥ 95%). Outside the learner's vocabulary: ${list}. Simplify.`);
    else if (coverage < 95) warn(`Coverage ${coverage}% (aim ≥ 95%). Glossed or unknown: ${list}.`);
    if (glossChars.size > 8) warn(`${glossChars.size} glossed characters: the texts may be above the learner's level.`);
  }
  // Recycling: each new word should appear at least twice in context.
  const context = [
    ...(p.dialogue?.lines ?? []),
    ...(p.reading?.lines ?? []),
    ...(p.grammar ?? []).flatMap((g) => g.examples ?? []),
    ...(p.tasks ?? []).flatMap((task) => (task && typeof task === "object" && "type" in task ? taskAudio(task) : [])),
  ].map((l) => l.zh ?? "").join("\n") + (p.review ?? []).map((r) => `${r.zh ?? ""}${r.prompt}`).join("\n");
  const thin = vocab.filter((v) => isStr(v?.hanzi) && context.split(v.hanzi).length - 1 < 2).map((v) => v.hanzi);
  if (thin.length) warn(`Appear fewer than 2 times in context: ${thin.join("、")}.`);

  // Conversation
  const c = p.conversation;
  if (c) {
    claim(c.id, "conversation");
    if (!Array.isArray(c.turns) || !c.turns.length) err("conversation: turns required.");
    (c.turns ?? []).forEach((t, i) => {
      const where = `conversation turn ${i + 1}`;
      if (!isStr(t.text) || !isStr(t.intent)) err(`${where}: text and intent required.`);
      if (!Array.isArray(t.examples) || !t.examples.length) err(`${where}: at least one example reply.`);
      let tests: RegExp[] = [];
      try {
        tests = (t.accept ?? []).map((r) => new RegExp(r));
      } catch (e) {
        err(`${where}: invalid accept pattern (${(e as Error).message}).`);
      }
      for (const ex of t.examples ?? [])
        if (tests.length && !tests.some((r) => r.test(ex))) err(`${where}: its own example "${ex}" would be rejected by the accept patterns.`);
    });
  }

  // Pragmatics and review
  (p.pragmatics ?? []).forEach((x, i) => {
    if (!x?.natural || !isStr(x.natural.zh) || !isStr(x.situation)) err(`pragmatics[${i}]: situation and natural.zh required.`);
  });
  (p.review ?? []).forEach((r, i) => {
    if (r.choices && r.answer && r.choices.filter((ch) => ch === r.answer).length !== 1) err(`review[${i}]: answer must appear exactly once in choices.`);
  });
  return { errors, warnings, stats };
}

// ---------- Compile into app content ----------
export interface CompiledGrammar extends PackGrammar { unitId: string }
export interface CompiledScenario {
  id: string;
  title: string;
  place: string;
  context: string;
  goal: string;
  partner: string;
  turns: { text: string; pinyin: string; meaning: string; intent: string; examples: string[]; phrase: string; test: (s: string) => boolean }[];
}
export interface CompiledText {
  id: string;
  title: string;
  titleZh: string;
  after: string;
  blurb: string;
  lines: { zh: string; py: string; en: string; speaker?: string }[];
  questions: { q: string; choices: string[]; answer: string; kind?: "gist" | "detail" | "inference" }[];
  glosses: { hanzi: string; pinyin: string; meaning: string }[];
  format?: "chat" | "post" | "note" | "story";
  purpose?: string;
  cloze?: { lines: Line[]; bank: string[] };
}
/** Pack text formats map onto the reader's four layouts. */
const layoutOf = (f?: string): CompiledText["format"] =>
  f === "message" || f === "chat" ? "chat" : f === "post" ? "post" : f === "story" || f === "article" ? "story" : f ? "note" : undefined;
const questionKinds = ["gist", "detail", "inference"] as const;
const kindOf = (t?: string) => questionKinds.find((k) => k === t);

const provenance: Provenance = {
  status: "AI-assisted draft",
  author: "Content pack (AI-assisted)",
  reviewer: null,
  version: 1,
  sources: ["HSK 3.0 word list (complete-hsk-vocabulary)"],
  lastReviewed: null,
};
const phraseFrom = (id: string, hanzi: string, pinyin: string, meaning: string, topic: string, extra: Partial<Phrase> = {}): Phrase => ({
  id,
  hanzi,
  traditional: hanzi,
  pinyin,
  meaning,
  vi: "",
  tones: syllables(pinyin).map(toneOfSyllable),
  register: "neutral",
  usage: "",
  utilityScore: 80,
  topic,
  audio: { provider: "local", text: hanzi },
  provenance,
  hskAlignment: [],
  ...extra,
});
const clean = (s: string) => s.replace(/[\s，。！？、,.!?]/g, "");

export function compilePack(p: ContentPack) {
  const u = p.unit;
  const topic = `stage-${u.stage}`;
  const phrases: Phrase[] = p.vocabulary.map((v) =>
    phraseFrom(v.id, v.hanzi, v.pinyin, v.meaning, topic, {
      traditional: v.traditional || v.hanzi,
      vi: v.meaningVi ?? "",
      register: v.register ?? "neutral",
      usage: [v.usageNote, v.measureWord ? `Measure word: ${v.measureWord}.` : ""].filter(Boolean).join(" "),
      example: v.example,
      hskAlignment: v.hskLevel
        ? [{ standardVersion: "HSK3.0", level: v.hskLevel, categories: ["vocabulary"], source: "complete-hsk-vocabulary", status: "provisional", effectiveDate: "2021-07-01", syllabusReference: null }]
        : [],
    }),
  );
  // Grammar examples and natural phrasings become phrases too, so attempts and review can track them.
  const grammar: CompiledGrammar[] = (p.grammar ?? []).map((g) => ({ ...g, unitId: u.id }));
  for (const g of grammar) {
    const ex = g.examples[0];
    phrases.push(phraseFrom(`${g.id}-ex`, ex.zh, ex.py, ex.en, "grammar", { usage: `${g.pattern}: ${g.purpose}` }));
  }
  const usage = (p.pragmatics ?? []).map((x, i) => {
    const id = `${u.id}-usage-${i + 1}`;
    phrases.push(phraseFrom(id, x.natural.zh, x.natural.py, x.natural.en ?? x.situation, "usage", { usage: x.note ?? "" }));
    return { id, ...x };
  });
  const lessons: Lesson[] = [
    {
      id: u.id,
      unit: `Stage ${u.stage}`,
      title: u.title,
      description: u.canDo.join(" · "),
      minutes: Math.max(8, Math.round((u.estimatedMinutes ?? 40) / 2)),
      phrases: p.vocabulary.map((v) => v.id),
      prerequisites: u.prerequisites ?? [],
      notice: "",
      mission: u.canDo.join(". ") + ".",
      context: p.dialogue?.setting ?? u.title,
      track: "pack",
      packPart: "words",
      provenance,
    },
  ];
  if (grammar.length || usage.length)
    lessons.push({
      id: `${u.id}-usage`,
      unit: `Stage ${u.stage}`,
      title: `${u.title}: grammar & usage`,
      description: grammar.map((g) => g.pattern).join(" · ") || "Natural ways to say it",
      minutes: Math.max(6, Math.round((u.estimatedMinutes ?? 40) / 3)),
      phrases: [...grammar.map((g) => `${g.id}-ex`), ...usage.map((x) => x.id)],
      prerequisites: [u.id],
      notice: "",
      mission: grammar.map((g) => g.purpose).join(". ") || "Choose the natural phrasing.",
      context: "",
      track: "pack",
      packPart: "usage",
      provenance,
    });
  const text = (t: PackText | undefined, fallback: string): CompiledText | null =>
    t
      ? {
          id: t.id,
          title: t.title,
          titleZh: t.titleZh ?? u.titleZh ?? fallback,
          after: u.id,
          blurb: t.blurb ?? t.setting ?? "",
          lines: t.lines.map((l) => ({ ...l, speaker: l.speaker ? (t.speakers?.find((s) => s.id === l.speaker)?.name ?? l.speaker) : undefined })),
          questions: (t.questions ?? []).map((q) => ({ q: q.q, choices: q.choices, answer: q.answer, kind: kindOf(q.type) })),
          glosses: t.glosses ?? [],
          format: layoutOf(t.format) ?? (t.speakers?.length ? "chat" : undefined),
          purpose: t.purpose,
          cloze: t.cloze,
        }
      : null;
  const texts = [text(p.dialogue, "对话"), text(p.reading, "阅读")].filter((x): x is CompiledText => !!x);
  const c = p.conversation;
  const scenario: CompiledScenario | null = c
    ? {
        id: c.id,
        title: c.title,
        place: c.place,
        context: c.context,
        goal: c.goal,
        partner: c.partner?.name ?? "林安",
        turns: c.turns.map((t) => {
          const accept = (t.accept ?? []).map((r) => new RegExp(r));
          const examples = t.examples.map(clean);
          return {
            text: t.text,
            pinyin: t.pinyin,
            meaning: t.meaning,
            intent: t.intent,
            examples: t.examples,
            phrase: p.vocabulary[0].id,
            test: (s: string) => accept.some((r) => r.test(s)) || examples.includes(clean(s)),
          };
        }),
      }
    : null;
  // The unit's dialogue becomes a listening task (no text until you answer), followed by the pack's own tasks.
  const d = p.dialogue;
  const dialogueTask: Task[] =
    d && (d.questions ?? []).length
      ? [
          {
            id: `${d.id}-listen`,
            type: "dialogue",
            phrase: p.vocabulary[0].id,
            title: d.title,
            setting: d.setting ?? d.blurb ?? "",
            lines: d.lines.map((l) => ({ ...l, speaker: l.speaker ? (d.speakers?.find((s) => s.id === l.speaker)?.name ?? l.speaker) : "" })),
            questions: (d.questions ?? []).map((q) => ({
              kind: (["gist", "detail", "inference", "intent"] as const).find((k) => k === q.type) ?? "detail",
              q: q.q,
              choices: q.choices,
              answer: q.answer,
            })),
          },
        ]
      : [];
  const tasks: Task[] = [...dialogueTask, ...(p.tasks ?? [])];
  return { unit: u, phrases, characters: p.characters ?? [], lessons, texts, grammar, usage, scenario, tasks };
}
export type CompiledPack = ReturnType<typeof compilePack>;
