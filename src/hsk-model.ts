import packs from "./generated/hsk-practice.json";
import type { HskItem, HskPracticePack } from "./hsk-pack";
import { roadmapFor } from "./hsk-roadmap";

export type HskEdition = "2.0" | "3.0";
export const hskItems = (packs as HskPracticePack[]).flatMap((p) => p.items);
export const hskItemById = Object.fromEntries(hskItems.map((q) => [q.id, q]));
export const hskParticleContext: Record<
  string,
  { zh: string; py: string; en: string }
> = {
  的: { zh: "我的", py: "wǒ de", en: "mine" },
  吗: { zh: "好吗", py: "hǎo ma", en: "okay?" },
  呢: { zh: "你呢", py: "nǐ ne", en: "and you?" },
  了: { zh: "好了", py: "hǎo le", en: "done; ready" },
};
export const hskSpeech = (text: string) => hskParticleContext[text]?.zh ?? text;
export const hskUnits = [
  {
    id: "identity",
    title: "People & identity",
    zh: "认识你",
    py: "Rènshi nǐ",
    description: "Identify people, ask names, and read simple statements.",
    focus: "是 · 不 · 的 · 吗",
    focusPy: "shì · bù · de · ma",
    book: "Study alongside Standard Course 1, lessons 1–5.",
  },
  {
    id: "numbers",
    title: "Numbers & quantities",
    zh: "数清楚",
    py: "Shǔ qīngchu",
    description: "Read quantities, ages, prices and the time without guessing.",
    focus: "个 · 本 · 岁 · 点",
    focusPy: "gè · běn · suì · diǎn",
    book: "Use the book’s number, date, age and time exercises alongside this drill.",
  },
  {
    id: "daily",
    title: "Everyday actions",
    zh: "读懂生活",
    py: "Dú dǒng shēnghuó",
    description: "Connect actions, places and objects in short sentences.",
    focus: "喝 · 吃 · 写 · 买",
    focusPy: "hē · chī · xiě · mǎi",
    book: "Use the book’s everyday-life dialogues and matching workbook exercises.",
  },
] as const;
export const teacherLines = {
  start: {
    zh: "认真一点。开始吧。",
    py: "Rènzhēn yìdiǎn. Kāishǐ ba.",
    en: "Focus. Let’s begin.",
  },
  pass: {
    zh: "不错。下一关。",
    py: "Búcuò. Xià yì guān.",
    en: "Good. Next checkpoint.",
  },
  retry: {
    zh: "先改错，再往前。",
    py: "Xiān gǎicuò, zài wǎng qián.",
    en: "Fix the mistakes. Then move on.",
  },
  exam: {
    zh: "看清题目，别急。",
    py: "Kàn qīng tímù, bié jí.",
    en: "Read the question. Don’t rush.",
  },
};
export const hskSources = {
  checked: "2026-10-04",
  syllabus: "https://www.chinesetest.cn/syllabus",
  official: "https://www.chinesetest.cn/HSK/1",
  samples3:
    "https://hsk-sample-1409982902.cos.ap-beijing.myqcloud.com/HSK3.0.zip",
  demo3: "https://hsk3demo-intl.chinesetest.cn/",
  downloads: "https://admin.chinesetest.cn/godownload.do",
  book: "https://www.blcup.com/EnPInfo/index/77",
  books: "https://www.blcup.com/EnSeriesBook/index/8",
  workbook: "https://www.blcup.com/EnPInfo/index/10373",
  advanced: "https://www.chinesetest.cn/HSK/7-9",
  advancedSample:
    "https://old.chinesetest.cn/userfiles/file/HSK/level7-9/HSK7-9.pdf",
  announcement:
    "https://old.chinesetest.cn/gonewcontent.do?flag=kdnew&id=51336883",
};
const papers = ["H10901", "H20901", "H31001", "H41001", "H51001", "H61001"];
export function officialPaper(level: number) {
  if (level >= 7) return hskSources.advancedSample;
  return `https://admin.chinesetest.cn/userfiles/file/HSK/level${level}/${papers[level - 1]}.pdf`;
}
export const sourceSteps = [
  {
    id: "syllabus",
    title: "Confirm your exam version",
    detail:
      "Check the level and format with your test centre. Read the matching official syllabus before choosing a book.",
  },
  {
    id: "textbook",
    title: "Finish the textbook pass",
    detail:
      "Work through the selected level’s vocabulary, dialogues and grammar. For Standard Course 4–6, finish both A and B. For HSK 3.0, audit gaps against its separate syllabus.",
  },
  {
    id: "workbook",
    title: "Correct the workbook",
    detail:
      "Complete the matching workbook. Explain each wrong answer and redo the missed questions without notes.",
  },
  {
    id: "paper",
    title: "Sit an official reading sample",
    detail:
      "Use the official paper or demo for your selected version. Work under its printed time limit, then use its answer key.",
  },
  {
    id: "repair",
    title: "Repair every missed question",
    detail:
      "Record the topic you missed, find the relevant explanation in your book, and redo it without help on another day.",
  },
] as const;

export function sourceStepsFor(level: number) {
  const plan = roadmapFor(level);
  return sourceSteps.map((step) => {
    if (step.id === "syllabus")
      return {
        ...step,
        detail: `${plan.entry} Confirm your exam version and read its official syllabus.`,
      };
    if (step.id === "textbook")
      return {
        ...step,
        title: level >= 7 ? "Study the advanced source material" : step.title,
        detail:
          plan.work +
          (level < 7
            ? " For HSK 3.0, check new-syllabus gaps separately."
            : ""),
      };
    if (step.id === "workbook" && level >= 7)
      return {
        ...step,
        title: "Correct your section practice",
        detail:
          "Explain reading and listening errors; have a qualified teacher review writing, translation and speaking. Redo weak tasks without notes.",
      };
    if (step.id === "paper" && level >= 7)
      return {
        ...step,
        title: "Work through the combined sample",
        detail:
          "Use the official 7–9 sample and its answer key. It contains omitted items, so do not treat it as a complete mock. Practise full timed papers separately.",
      };
    return step;
  });
}

export interface HskAnswer {
  value: string;
  supported: boolean;
}
export interface HskRun {
  id: string;
  schemaVersion: 1;
  packVersion: 1;
  unit: HskItem["unit"] | "repair";
  itemIds: string[];
  answers: Record<string, HskAnswer>;
  startedAt: number;
  deadline: number | null;
  finishedAt: number | null;
}
export interface HskSettings {
  id: "learner";
  level: number;
  edition: HskEdition;
  studied: string[];
  sourceDone: string[];
}
export const defaultHskSettings: HskSettings = {
  id: "learner",
  level: 1,
  edition: "2.0",
  studied: [],
  sourceDone: [],
};
export function gradeRun(run: HskRun) {
  const correct = run.itemIds.filter(
    (id) => run.answers[id]?.value === hskItemById[id]?.answer,
  ).length;
  const supported = run.itemIds.filter(
    (id) => run.answers[id]?.supported,
  ).length;
  const unaided = run.itemIds.filter(
    (id) =>
      !run.answers[id]?.supported &&
      run.answers[id]?.value === hskItemById[id]?.answer,
  ).length;
  return {
    correct,
    supported,
    unaided,
    total: run.itemIds.length,
    passed:
      !!run.finishedAt &&
      unaided / run.itemIds.length >= 0.8 &&
      supported === 0,
  };
}
export function unitPassed(unit: string, runs: HskRun[]) {
  return runs.some((r) => r.unit === unit && gradeRun(r).passed);
}
export function unitUnlocked(index: number, runs: HskRun[]) {
  return hskUnits.slice(0, index).every((u) => unitPassed(u.id, runs));
}
export function unresolvedItems(runs: HskRun[]) {
  const latest = new Map<string, HskAnswer | undefined>();
  [...runs]
    .filter((r) => r.finishedAt)
    .sort((a, b) => a.finishedAt! - b.finishedAt! || a.id.localeCompare(b.id))
    .forEach((r) => r.itemIds.forEach((id) => latest.set(id, r.answers[id])));
  return [...latest]
    .filter(
      ([id, answer]) =>
        !answer || answer.supported || answer.value !== hskItemById[id]?.answer,
    )
    .map(([id]) => id);
}
export function makeRun(
  unit: HskRun["unit"],
  ids?: string[],
  now = Date.now(),
): HskRun {
  return {
    id: crypto.randomUUID(),
    schemaVersion: 1,
    packVersion: 1,
    unit,
    itemIds: ids ?? hskItems.filter((q) => q.unit === unit).map((q) => q.id),
    answers: {},
    startedAt: now,
    deadline: unit === "sample" ? now + 6 * 60_000 : null,
    finishedAt: null,
  };
}
export function validRun(raw: unknown): raw is HskRun {
  const r = raw as HskRun;
  return (
    !!r &&
    typeof r.id === "string" &&
    r.schemaVersion === 1 &&
    r.packVersion === 1 &&
    ["identity", "numbers", "daily", "sample", "repair"].includes(r.unit) &&
    Array.isArray(r.itemIds) &&
    r.itemIds.length > 0 &&
    r.itemIds.length <= 36 &&
    new Set(r.itemIds).size === r.itemIds.length &&
    r.itemIds.every(
      (id) =>
        !!hskItemById[id] &&
        (r.unit === "repair" || hskItemById[id].unit === r.unit),
    ) &&
    (r.unit === "repair" ||
      r.itemIds.length === hskItems.filter((q) => q.unit === r.unit).length) &&
    Number.isFinite(r.startedAt) &&
    r.startedAt > 0 &&
    (r.unit === "sample"
      ? r.deadline === r.startedAt + 360_000
      : r.deadline === null) &&
    (r.finishedAt === null ||
      (Number.isFinite(r.finishedAt) && r.finishedAt >= r.startedAt)) &&
    !!r.answers &&
    typeof r.answers === "object" &&
    Object.entries(r.answers).every(
      ([id, a]) =>
        r.itemIds.includes(id) &&
        !!a &&
        typeof a.supported === "boolean" &&
        (a.value === "" ||
          hskItemById[id].choices.some((c) => c.zh === a.value)),
    )
  );
}
