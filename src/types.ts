import type { Card } from "ts-fsrs";
export type Modality =
  | "listening"
  | "reading"
  | "recall"
  | "speaking"
  | "typing"
  | "tone"
  | "media"
  | "conversation";
export type Locale = "en-US" | "vi-VN";
export type ContentStatus =
  | "AI-assisted draft"
  | "reference-verified"
  | "linguistically reviewed"
  | "pedagogically reviewed"
  | "audio reviewed"
  | "published"
  | "deprecated";
export interface Alignment {
  standardVersion: string;
  level: number;
  categories: string[];
  source: string;
  status: "provisional" | "verified";
  effectiveDate: string | null;
  syllabusReference: string | null;
}
export interface Provenance {
  status: ContentStatus;
  author: string;
  reviewer: string | null;
  version: number;
  sources: string[];
  lastReviewed: string | null;
}
export interface Phrase {
  id: string;
  /** An example sentence in context (content packs). */
  example?: { zh: string; py: string; en: string };
  hanzi: string;
  traditional: string;
  pinyin: string;
  meaning: string;
  vi: string;
  tones: number[];
  register: string;
  usage: string;
  utilityScore: number;
  topic: string;
  audio: { provider: "local" | "browser"; text: string };
  provenance: Provenance;
  hskAlignment: Alignment[];
}
export interface Lesson {
  id: string;
  unit: string;
  title: string;
  description: string;
  minutes: number;
  phrases: string[];
  prerequisites: string[];
  notice: string;
  mission: string;
  context: string;
  tone?: number;
  track?: "read" | "speak" | "pack";
  /** For content-pack lessons: the words lesson or the grammar-and-usage lesson. */
  packPart?: "words" | "usage";
  provenance: Provenance;
}
export interface Memory {
  id: string;
  phraseId: string;
  modality: Modality;
  card: Card;
  due: number;
  successes: number;
  failures: number;
  lastEvidence: number;
}
export interface Attempt {
  id: string;
  phraseId: string;
  modality: Modality;
  correct: boolean | null;
  answer: string;
  expected: string;
  at: number;
  latencyMs: number;
  support: "none" | "pinyin" | "transcript" | "self-report";
  context: string;
}
export interface Mistake {
  id: string;
  phraseId: string;
  modality: Modality;
  answer: string;
  expected: string;
  at: number;
  count: number;
  context: string;
}
export interface Session {
  id: string;
  lessonId: string;
  completedAt: number;
  attempts: number;
  seconds: number;
  kind: "lesson" | "conversation" | "media" | "assessment";
}
/** A subtitle or lyric line the learner saved from the Watch player. */
export interface SavedLine {
  id: string;
  text: string;
  note: string;
  /** File name of the video, episode or song. */
  source: string;
  /** Seconds into the media. */
  start: number;
  at: number;
}
/** A word saved from the dictionary card (Watch player or reader). */
export interface PersonalWord {
  /** The word itself (simplified), so saving twice keeps one copy. */
  id: string;
  pinyin: string;
  meaning: string;
  /** The line it was found in, and where. */
  line: string;
  source: string;
  at: number;
}
/** One timed-reading drill session. Rates are characters per second. */
export interface ReadingSpeed {
  id: string;
  at: number;
  startRate: number;
  endRate: number;
  lines: number;
  /** Unaided correct answers (the only ones that raise the rate). */
  correct: number;
}
/** One Watch session: how much help was needed, honestly counted. */
export interface WatchLog {
  id: string;
  source: string;
  media: "video" | "audio";
  rung: "subtitles" | "peek" | "none";
  /** Seconds actually played. */
  seconds: number;
  /** Lines revealed on the peek rung, and characters looked up. */
  peeks: number;
  lookups: number;
  /** Subtitle or lyric lines that played. */
  lines: number;
  at: number;
}
export interface Account {
  id: string;
  provider: "google" | "apple" | "email";
  email: string;
  name: string;
}
export interface Profile {
  updatedAt?: number;
  updatedBy?: string;
  id: "learner";
  name: string;
  minutes: number;
  goals: string[];
  locale: Locale;
  onboarded: boolean;
  pinyin: boolean;
  quiet: boolean;
  voiceURI: string;
  examMode: boolean;
  /** Which door the learner walks through first. */
  path?: LearningPath;
  toneColors?: boolean;
  mascotEnabled?: boolean;
  mascotMotion?: boolean;
  /** Show the days-in-a-row count. Secondary by design. */
  showStreak?: boolean;
  /** How the learner came in: an account, or straight in as a guest. */
  entry?: "account" | "guest";
  account?: Account | null;
  /** Device-only (never synced): when this browser last exported a backup. */
  lastBackupAt?: number;
  /** Device-only: "Later" on the backup reminder. */
  backupSnoozedAt?: number;
}
export type LearningPath = "characters" | "sound" | "together";
export interface Draft {
  id: string;
  step: number;
  updatedAt: number;
}
export type ExerciseKind =
  | "hear"
  | "notice"
  | "choice"
  | "recall"
  | "reorder"
  | "record"
  | "read"
  | "dictation"
  | "meet"
  | "glyph"
  | "pick"
  | "spot"
  | "count"
  | "grammar"
  | "register"
  | "dialogue"
  | "truefalse"
  | "reply"
  | "listenfill"
  | "cloze"
  | "match";
export interface Exercise {
  id: string;
  kind: ExerciseKind;
  phraseId: string;
  prompt: string;
  modality: Modality;
  choices?: string[];
  correct?: string;
  tokens?: string[];
  /** For character steps: the cue shown in a "spot" exercise. */
  cue?: string;
  /** For HSK-style practice tasks (dialogue, true/false, reply, fill-ins, matching). */
  task?: Task;
}
/** One spoken or written line. Blanks are marked 【like this】 in zh. */
export interface TaskLine {
  zh: string;
  py: string;
  en: string;
  speaker?: string;
}
export interface TaskQuestion {
  kind: "gist" | "detail" | "inference" | "intent";
  q: string;
  choices: string[];
  answer: string;
}
interface TaskBase {
  id: string;
  /** The lesson phrase this task gives evidence for. */
  phrase: string;
}
export type Task = TaskBase &
  (
    | { type: "dialogue"; title: string; setting: string; lines: TaskLine[]; questions: TaskQuestion[] }
    | { type: "truefalse"; audio: TaskLine; statement: string; answer: boolean; why: string }
    | { type: "reply"; prompt: TaskLine; choices: string[]; answer: string; why?: string }
    | { type: "listenfill"; line: TaskLine; blankPy: string }
    | { type: "cloze"; title: string; lines: TaskLine[]; bank: string[] }
    | { type: "match"; title: string; pairs: { left: string | TaskLine; right: TaskLine }[] }
  );
