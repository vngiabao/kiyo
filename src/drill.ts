/**
 * Timed reading drill: a line you've learned flashes for as long as a subtitle would
 * stay on screen at your current rate, then you pick its meaning without the text.
 *
 * Reference points (Netflix Simplified Chinese Timed Text Style Guide, checked Oct 2026):
 * adult programmes up to 9 characters per second, children's up to 7; 16 characters per
 * line; a subtitle stays between 5/6 of a second and 7 seconds.
 * Only unaided correct answers raise the rate; there is no way to get help mid-line.
 */
import { allLessons, phraseById, characters } from "./content";
import { compiledPacks } from "./pack-content";
import { readings } from "./hanzi";
import { lessonTasks, plain, taskAudio } from "./tasks";

export const SUBTITLE_RATE = { adult: 9, children: 7 } as const;
export const MAX_LINE = 16;
export const MIN_SHOW = 5 / 6;
export const MAX_SHOW = 7;
export const START_RATE = 3;
export const MIN_RATE = 1.5;
export const MAX_RATE = 12;
export const STEP = 1.15;

export interface DrillLine {
  zh: string;
  en: string;
}
const isHan = (ch: string) => /\p{Script=Han}/u.test(ch);
export const hanLength = (s: string) => Array.from(s).filter(isHan).length;

/** Seconds a line stays on screen at a given rate (characters per second). */
export const showFor = (zh: string, rate: number) => Math.min(MAX_SHOW, Math.max(MIN_SHOW, hanLength(zh) / rate));

/**
 * Staircase: two unaided correct answers in a row → 15% faster; any miss → 15% slower.
 * Returns the new rate and the new streak of correct answers.
 */
export function nextRate(rate: number, streak: number, correct: boolean): { rate: number; streak: number } {
  if (!correct) return { rate: Math.max(MIN_RATE, round(rate / STEP)), streak: 0 };
  if (streak + 1 >= 2) return { rate: Math.min(MAX_RATE, round(rate * STEP)), streak: 0 };
  return { rate, streak: streak + 1 };
}
const round = (n: number) => Math.round(n * 100) / 100;

/**
 * Lines you've already studied, made only of characters the course has taught you.
 * `done` is the set of finished lesson ids from sessions (as stored: "first", "s1-u03",
 * "s1-u03-usage", "read-2", "read:p-door").
 */
export function drillMaterial(done: Set<string>): DrillLine[] {
  const finished = allLessons.filter((l) => done.has(l.id));
  // Taught characters: words and characters from finished lessons.
  const taught = new Set<string>();
  for (const l of finished)
    for (const id of l.phrases) {
      const p = phraseById[id];
      if (p) for (const ch of Array.from(p.hanzi).filter(isHan)) taught.add(ch);
    }
  for (const c of characters) if (finished.some((l) => l.track === "read" && l.phrases.includes(`c-${c.hanzi}`))) taught.add(c.hanzi);

  const lines: DrillLine[] = [];
  const add = (zh: string | undefined, en: string | undefined) => {
    if (!zh || !en) return;
    const z = plain(zh).trim();
    const n = hanLength(z);
    if (n >= 4 && n <= MAX_LINE && Array.from(z).filter(isHan).every((ch) => taught.has(ch))) lines.push({ zh: z, en: en.trim() });
  };
  for (const l of finished) {
    for (const id of l.phrases) {
      const p = phraseById[id];
      add(p?.hanzi, p?.meaning);
      add(p?.example?.zh, p?.example?.en);
    }
    for (const t of lessonTasks[l.id] ?? []) for (const a of taskAudio(t)) add(a.zh, a.en);
  }
  for (const pack of compiledPacks) {
    if (!done.has(pack.unit.id)) continue;
    for (const t of pack.texts) for (const line of t.lines) add(line.zh, line.en);
    for (const t of pack.tasks) for (const a of taskAudio(t)) add(a.zh, a.en);
  }
  for (const r of readings) if (done.has(`read:${r.id}`)) for (const line of r.lines) add(line.zh, line.en);
  // One copy per sentence, and never two lines with the same meaning (they'd make bad distractors).
  const seen = new Set<string>(),
    seenEn = new Set<string>();
  return lines.filter((l) => {
    const key = l.en.toLowerCase();
    if (seen.has(l.zh) || seenEn.has(key)) return false;
    seen.add(l.zh);
    seenEn.add(key);
    return true;
  });
}

/** Three meanings: the right one and two from other lines, in a varying position. */
export function meaningChoices(line: DrillLine, pool: DrillLine[], seed: number): string[] {
  const others = pool.filter((l) => l.en !== line.en);
  const picks: string[] = [];
  for (let k = 0; picks.length < 2 && k < others.length; k++) {
    const cand = others[(seed * 7 + k * 13) % others.length].en;
    if (!picks.includes(cand)) picks.push(cand);
  }
  const at = seed % (picks.length + 1);
  return [...picks.slice(0, at), line.en, ...picks.slice(at)];
}
