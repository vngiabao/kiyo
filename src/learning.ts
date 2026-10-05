import { createEmptyCard, fsrs, Rating } from "ts-fsrs";
import type { Attempt, Memory, Modality } from "./types";
export const scheduler = fsrs({ request_retention: 0.9, enable_fuzz: false });
export function updateMemory(
  previous: Memory | undefined,
  attempt: Attempt,
): Memory | null {
  if (
    attempt.correct === null ||
    attempt.support !== "none" ||
    ["speaking", "conversation", "recall", "media"].includes(attempt.modality)
  )
    return null;
  const now = new Date(attempt.at);
  const card = previous?.card ?? createEmptyCard(now)!;
  const rating = attempt.correct ? Rating.Good : Rating.Again;
  const next = scheduler.next(card, now, rating).card;
  return {
    id: `${attempt.phraseId}:${attempt.modality}`,
    phraseId: attempt.phraseId,
    modality: attempt.modality,
    card: next,
    due: next.due.getTime(),
    successes: (previous?.successes ?? 0) + Number(attempt.correct),
    failures: (previous?.failures ?? 0) + Number(!attempt.correct),
    lastEvidence: attempt.at,
  };
}
export function skillEvidence(attempts: Attempt[], modality: Modality) {
  const eligible = attempts.filter(
    (a) =>
      a.modality === modality && a.correct !== null && a.support === "none",
  );
  return {
    count: eligible.length,
    correct: eligible.filter((a) => a.correct).length,
    accuracy: eligible.length
      ? Math.round(
          (100 * eligible.filter((a) => a.correct).length) / eligible.length,
        )
      : null,
  };
}
export type PlanItem = {
  label: string;
  detail: string;
  minutes: number;
  route: "review" | "listening" | "lesson" | "speak" | "characters" | "reading";
};
/**
 * Split today's minutes. Path decides the emphasis; evidence adjusts it.
 * Characters-first learners still hear and say a little every day.
 */
export function dailyPlan(
  minutes: number,
  attempts: Attempt[],
  due: number,
  path: "characters" | "sound" | "together" = "sound",
) {
  const listening = skillEvidence(attempts, "listening");
  const reading = skillEvidence(attempts, "reading");
  const needsListening =
    listening.count >= 3 &&
    reading.count >= 3 &&
    (reading.accuracy ?? 0) > (listening.accuracy ?? 0) + 15;
  const review = due ? Math.max(2, Math.round(minutes * 0.2)) : 0;
  const listenDetail = needsListening
    ? "Your recent reading is stronger than listening"
    : "Start with sound and a little context";
  const listenLabel = needsListening ? "Hear it without the text" : "Listen for meaning";
  const reviewItem: PlanItem[] = due
    ? [{ label: "Bring it back", detail: `${due} memories ready to revisit`, minutes: review, route: "review" }]
    : [];
  if (path !== "sound") {
    const rest = minutes - review;
    const share = path === "characters" ? [0.4, 0.25, 0.2] : [0.3, 0.15, 0.3];
    if (needsListening) share[2] += 0.1;
    const chars = Math.max(2, Math.round(rest * share[0]));
    const read = Math.max(2, Math.round(rest * share[1]));
    const listen = Math.max(2, Math.round(rest * share[2]));
    const speak = rest - chars - read - listen;
    return {
      items: [
        ...reviewItem,
        { label: "Meet new characters", detail: "Shape, parts and meaning first", minutes: chars, route: "characters" },
        { label: "Read a short text", detail: "Tap anything you don’t know", minutes: read, route: "reading" },
        { label: listenLabel, detail: listenDetail, minutes: listen, route: "listening" },
        { label: "Say something", detail: "A phrase you can already read", minutes: speak, route: "speak" },
      ] as PlanItem[],
      reason: needsListening
        ? "A little more listening today: your reading is running ahead of your ear."
        : path === "characters"
          ? "Characters first, then a text to read them in. A few minutes of sound keeps your ear awake."
          : "Characters and sound side by side, so what you read and what you hear grow together.",
    };
  }
  const listen = Math.round(minutes * (needsListening ? 0.4 : 0.3));
  const speak = Math.max(2, Math.round(minutes * 0.25));
  const lesson = minutes - review - listen - speak;
  return {
    items: [
      ...reviewItem,
      { label: listenLabel, detail: listenDetail, minutes: listen, route: "listening" },
      { label: "Learn something useful", detail: "Continue your next small conversation", minutes: lesson, route: "lesson" },
      { label: "Say it in a conversation", detail: "Retrieve, respond, and ask something back", minutes: speak, route: "speak" },
    ] as PlanItem[],
    reason: needsListening
      ? "A little more listening today: your last attempts show a gap between reading and hearing."
      : due
        ? "A little retrieval, a new encounter, and a chance to speak."
        : "Begin with sound. Learn a useful phrase. Try it in a conversation.",
  };
}
export const normalize = (s: string) =>
  s
    .normalize("NFKC")
    .replace(/[\s，。！？,.!?、]/g, "")
    .toLowerCase();
export const searchNormalize = (s: string) =>
  s
    .normalize("NFD")
    .replace(/[\u0300-\u036f\s1-5]/g, "")
    .toLowerCase();
