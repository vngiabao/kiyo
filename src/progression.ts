import { allLessons } from "./content";
import type { Attempt, Session } from "./types";

const lessonIds = new Set(allLessons.map((l) => l.id));

/**
 * Level = 1 + lessons finished at least once (either path). A level is a
 * finished lesson you can name, never points: each level-up says what you
 * can now do.
 */
export function levelOf(sessions: Pick<Session, "lessonId" | "kind">[]) {
  const finished = new Set(
    sessions
      .filter((s) => s.kind === "lesson" && lessonIds.has(s.lessonId))
      .map((s) => s.lessonId),
  );
  return { level: 1 + finished.size, finished };
}

const dayKey = (t: number) => {
  const d = new Date(t);
  return `${d.getFullYear()}-${d.getMonth()}-${d.getDate()}`;
};

/**
 * Consecutive local days with any study (a finished session or a saved
 * attempt). Today counts if you have studied; otherwise the run is still
 * alive until the end of today.
 */
export function streakOf(
  sessions: Pick<Session, "completedAt">[],
  attempts: Pick<Attempt, "at">[],
  now = Date.now(),
) {
  const days = new Set([
    ...sessions.map((s) => dayKey(s.completedAt)),
    ...attempts.map((a) => dayKey(a.at)),
  ]);
  const studiedToday = days.has(dayKey(now));
  let count = 0;
  const cursor = new Date(now);
  if (!studiedToday) cursor.setDate(cursor.getDate() - 1);
  while (days.has(dayKey(cursor.getTime()))) {
    count++;
    cursor.setDate(cursor.getDate() - 1);
  }
  return { days: count, studiedToday };
}
