import { updateMemory } from "./learning";
import type { Attempt, Memory, Mistake, Profile, Session } from "./types";

export const SYNC_SCHEMA = 1;
export const profileFields = [
  "name",
  "minutes",
  "goals",
  "locale",
  "onboarded",
  "pinyin",
  "quiet",
  "examMode",
  "path",
  "toneColors",
  "mascotEnabled",
  "mascotMotion",
  "showStreak",
  "updatedAt",
  "updatedBy",
] as const;
export type CloudProfile = Pick<Profile, "id" | (typeof profileFields)[number]>;
export type SyncKind =
  "attempts" | "sessions" | "memories" | "mistakes" | "profiles";
export type SyncRow = {
  kind: SyncKind;
  id: string;
  schema_version: number;
  payload: unknown;
};
export type LearningSnapshot = {
  attempts: Attempt[];
  sessions: Session[];
  memories: Memory[];
  mistakes: Mistake[];
  profile?: CloudProfile;
};
export type SyncState = {
  id: "local";
  deviceId: string;
  ownerId?: string;
  enabled: boolean;
  consentDeclinedFor?: string;
  epoch?: string;
  revision?: number;
  lastSync?: number;
  acknowledged?: string;
  pending?: boolean;
};
export const compareId = (a: string, b: string) => (a < b ? -1 : a > b ? 1 : 0);
export const compareAttempts = (a: Attempt, b: Attempt) =>
  a.at - b.at || compareId(a.id, b.id);
export function canonical(value: unknown): string {
  if (value instanceof Date) return JSON.stringify(value.toISOString());
  if (Array.isArray(value)) return `[${value.map(canonical).join(",")}]`;
  if (value && typeof value === "object")
    return `{${Object.entries(value)
      .filter(([, v]) => v !== undefined)
      .sort(([a], [b]) => compareId(a, b))
      .map(([k, v]) => `${JSON.stringify(k)}:${canonical(v)}`)
      .join(",")}}`;
  return JSON.stringify(value);
}
export function cloudProfile(profile: Profile): CloudProfile {
  const result: Record<string, unknown> = { id: "learner" };
  for (const key of profileFields)
    if (profile[key] !== undefined) result[key] = profile[key];
  return result as CloudProfile;
}
export function latestProfile(a?: CloudProfile, b?: CloudProfile) {
  if (!a) return b;
  if (!b) return a;
  const order =
    (a.updatedAt ?? 0) - (b.updatedAt ?? 0) ||
    compareId(a.updatedBy ?? "", b.updatedBy ?? "") ||
    compareId(canonical(a), canonical(b));
  return order >= 0 ? a : b;
}
function union<T extends { id: string }>(a: T[], b: T[]): T[] {
  const records = new Map(a.map((r) => [r.id, r]));
  for (const r of b) {
    const old = records.get(r.id);
    if (old && canonical(old) !== canonical(r))
      throw new Error(
        "Two different immutable records share an ID. Export a backup before resolving this conflict.",
      );
    records.set(r.id, r);
  }
  return [...records.values()].sort((a, b) => compareId(a.id, b.id));
}
export function mergeSnapshots(
  local: LearningSnapshot,
  remote: LearningSnapshot,
): LearningSnapshot {
  const attempts = union(local.attempts, remote.attempts).sort(compareAttempts);
  const memories = new Map<string, Memory>(),
    mistakes = new Map<string, Mistake>();
  // Evidence is the source of truth; fuzz is disabled in the shared scheduler.
  for (const attempt of attempts) {
    const key = `${attempt.phraseId}:${attempt.modality}`;
    const memory = updateMemory(memories.get(key), attempt);
    if (memory) memories.set(key, memory);
    if (attempt.correct === false)
      mistakes.set(key, {
        id: key,
        phraseId: attempt.phraseId,
        modality: attempt.modality,
        answer: attempt.answer,
        expected: attempt.expected,
        at: attempt.at,
        count: (mistakes.get(key)?.count ?? 0) + 1,
        context: attempt.context,
      });
  }
  return {
    attempts,
    sessions: union(local.sessions, remote.sessions),
    memories: [...memories.values()],
    mistakes: [...mistakes.values()],
    profile: latestProfile(local.profile, remote.profile),
  };
}
export function rowsOf(data: LearningSnapshot): SyncRow[] {
  const rows: SyncRow[] = [];
  for (const kind of ["attempts", "sessions", "memories", "mistakes"] as const)
    for (const record of data[kind])
      rows.push({
        kind,
        id: record.id,
        schema_version: SYNC_SCHEMA,
        payload: record,
      });
  if (data.profile)
    rows.push({
      kind: "profiles",
      id: "learner",
      schema_version: SYNC_SCHEMA,
      payload: data.profile,
    });
  return rows.sort((a, b) =>
    compareId(`${a.kind}:${a.id}`, `${b.kind}:${b.id}`),
  );
}
const object = (v: unknown): v is Record<string, unknown> =>
  !!v && typeof v === "object" && !Array.isArray(v);
const finite = (v: unknown) =>
  typeof v === "number" && Number.isFinite(v) && v >= 0;
const text = (v: unknown) => typeof v === "string" && v.length <= 20000;
const modalities = [
  "listening",
  "reading",
  "recall",
  "speaking",
  "typing",
  "tone",
  "media",
  "conversation",
];
export function snapshotOf(rows: SyncRow[]): LearningSnapshot {
  const result: LearningSnapshot = {
    attempts: [],
    sessions: [],
    memories: [],
    mistakes: [],
  };
  for (const row of rows) {
    if (row.schema_version !== SYNC_SCHEMA)
      throw new Error(
        "Cloud data uses a different format. Update Kiyo before syncing; your local data is safe.",
      );
    const p = row.payload;
    if (!object(p) || !text(row.id) || row.id !== p.id)
      throw new Error("Invalid cloud record. Local data was not replaced.");
    if (row.kind === "attempts") {
      if (
        !text(p.phraseId) ||
        !modalities.includes(p.modality as string) ||
        ![true, false, null].includes(p.correct as boolean | null) ||
        !finite(p.at) ||
        !finite(p.latencyMs) ||
        !text(p.answer) ||
        !text(p.expected) ||
        !text(p.context) ||
        !["none", "pinyin", "transcript", "self-report"].includes(
          p.support as string,
        )
      )
        throw new Error("Invalid cloud attempt.");
      const {
        id,
        phraseId,
        modality,
        correct,
        answer,
        expected,
        at,
        latencyMs,
        support,
        context,
      } = p;
      result.attempts.push({
        id,
        phraseId,
        modality,
        correct,
        answer,
        expected,
        at,
        latencyMs,
        support,
        context,
      } as Attempt);
    } else if (row.kind === "sessions") {
      if (
        !text(p.lessonId) ||
        !finite(p.completedAt) ||
        !finite(p.seconds) ||
        !finite(p.attempts) ||
        !["lesson", "conversation", "media", "assessment"].includes(
          p.kind as string,
        )
      )
        throw new Error("Invalid cloud session.");
      const { id, lessonId, completedAt, seconds, attempts, kind } = p;
      result.sessions.push({
        id,
        lessonId,
        completedAt,
        seconds,
        attempts,
        kind,
      } as Session);
    } else if (row.kind === "profiles") {
      if (
        p.id !== "learner" ||
        !text(p.name) ||
        ![10, 20, 30, 45, 60].includes(p.minutes as number) ||
        !["en-US", "vi-VN"].includes(p.locale as string) ||
        !Array.isArray(p.goals) ||
        !p.goals.every(text) ||
        !finite(p.updatedAt) ||
        !text(p.updatedBy)
      )
        throw new Error("Invalid cloud profile.");
      for (const k of ["onboarded", "pinyin", "quiet", "examMode"])
        if (typeof p[k] !== "boolean")
          throw new Error("Invalid cloud preference.");
      for (const k of [
        "toneColors",
        "mascotEnabled",
        "mascotMotion",
        "showStreak",
      ])
        if (p[k] !== undefined && typeof p[k] !== "boolean")
          throw new Error("Invalid cloud preference.");
      if (
        p.path !== undefined &&
        !["characters", "sound", "together"].includes(p.path as string)
      )
        throw new Error("Invalid cloud learning path.");
      result.profile = cloudProfile(p as unknown as Profile);
    } else if (row.kind !== "memories" && row.kind !== "mistakes")
      throw new Error("Unknown cloud record type.");
    // Remote caches are never trusted as evidence. Reconstruct them from attempts.
  }
  return result;
}
