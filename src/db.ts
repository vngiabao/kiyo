import Dexie, { type EntityTable } from "dexie";
import type {
  Profile,
  Attempt,
  Memory,
  Mistake,
  Session,
  Draft,
} from "./types";
import { updateMemory } from "./learning";
import { phraseById } from "./content";
import { profileFields, type SyncState } from "./sync-model";
const profileWriter = crypto.randomUUID();
class LearningDB extends Dexie {
  profiles!: EntityTable<Profile, "id">;
  attempts!: EntityTable<Attempt, "id">;
  memories!: EntityTable<Memory, "id">;
  mistakes!: EntityTable<Mistake, "id">;
  sessions!: EntityTable<Session, "id">;
  drafts!: EntityTable<Draft, "id">;
  syncState!: EntityTable<SyncState, "id">;
  constructor() {
    super("tingjian-v1");
    this.version(1).stores({
      profiles: "id",
      attempts: "id,phraseId,modality,at",
      memories: "id,phraseId,modality,due",
      mistakes: "id,modality,at",
      sessions: "id,lessonId,completedAt",
      drafts: "id",
    });
    this.version(2).stores({ syncState: "id" });
    this.profiles.hook("creating", (_key, profile, tx) => {
      if ((tx as typeof tx & { fromCloud?: boolean }).fromCloud) return;
      profile.updatedAt = Date.now();
      profile.updatedBy = profileWriter;
    });
    this.profiles.hook("updating", (changes, _key, _old, tx) => {
      if ((tx as typeof tx & { fromCloud?: boolean }).fromCloud) return;
      if (profileFields.some((key) => key !== "updatedAt" && key !== "updatedBy" && key in changes))
        return { updatedAt: Date.now(), updatedBy: profileWriter };
    });
  }
}
export const db = new LearningDB();
export const defaultProfile: Profile = {
  id: "learner",
  name: "",
  minutes: 30,
  goals: ["Reading", "Conversation", "Friends & socializing"],
  locale: "en-US",
  onboarded: false,
  pinyin: true,
  quiet: false,
  voiceURI: "",
  examMode: false,
  path: "characters",
  toneColors: true,
};
export async function saveAttempt(
  data: Omit<Attempt, "id" | "at"> & { id?: string; at?: number },
) {
  const attempt: Attempt = {
    ...data,
    id: data.id ?? crypto.randomUUID(),
    at: data.at ?? Date.now(),
  };
  await db.transaction(
    "rw",
    db.attempts,
    db.memories,
    db.mistakes,
    async () => {
      if (await db.attempts.get(attempt.id)) return;
      await db.attempts.add(attempt);
      const key = `${attempt.phraseId}:${attempt.modality}`;
      const memory = updateMemory(await db.memories.get(key), attempt);
      if (memory) await db.memories.put(memory);
      if (attempt.correct === false) {
        const old = await db.mistakes.get(key);
        await db.mistakes.put({
          id: key,
          phraseId: attempt.phraseId,
          modality: attempt.modality,
          answer: attempt.answer,
          expected: attempt.expected,
          at: attempt.at,
          count: (old?.count ?? 0) + 1,
          context: attempt.context,
        });
      }
    },
  );
}
export async function exportRecord() {
  const [profiles, attempts, memories, mistakes, sessions, drafts] =
    await Promise.all([
      db.profiles.toArray(),
      db.attempts.toArray(),
      db.memories.toArray(),
      db.mistakes.toArray(),
      db.sessions.toArray(),
      db.drafts.toArray(),
    ]);
  return {
    schemaVersion: 1,
    exportedAt: new Date().toISOString(),
    profiles,
    attempts,
    memories,
    mistakes,
    sessions,
    drafts,
  };
}
export async function importRecord(raw: unknown) {
  if (!raw || typeof raw !== "object")
    throw new Error("This file is not a Tingjian backup.");
  const r = raw as Record<string, unknown>;
  if (r.schemaVersion !== 1)
    throw new Error("This backup version is not supported.");
  for (const key of [
    "profiles",
    "attempts",
    "memories",
    "mistakes",
    "sessions",
    "drafts",
  ])
    if (!Array.isArray(r[key]) || (r[key] as unknown[]).length > 100000)
      throw new Error("The backup is incomplete or too large.");
  const data = r as unknown as Awaited<ReturnType<typeof exportRecord>>;
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
  const finite = (n: unknown) =>
    typeof n === "number" && Number.isFinite(n) && n >= 0;
  for (const p of data.profiles)
    if (
      p.id !== "learner" ||
      typeof p.name !== "string" ||
      p.name.length > 100 ||
      ![10, 20, 30, 45, 60].includes(p.minutes) ||
      !["en-US", "vi-VN"].includes(p.locale) ||
      !Array.isArray(p.goals) ||
      p.goals.some((g) => typeof g !== "string") ||
      typeof p.onboarded !== "boolean" ||
      typeof p.pinyin !== "boolean" ||
      typeof p.quiet !== "boolean" ||
      (p.mascotEnabled !== undefined && typeof p.mascotEnabled !== "boolean") ||
      (p.mascotMotion !== undefined && typeof p.mascotMotion !== "boolean") ||
      (p.showStreak !== undefined && typeof p.showStreak !== "boolean") ||
      (p.entry !== undefined && !["account", "guest"].includes(p.entry)) ||
      (p.account != null &&
        (typeof p.account !== "object" ||
          typeof p.account.id !== "string" ||
          typeof p.account.email !== "string" ||
          !["google", "apple", "email"].includes(p.account.provider))) ||
      typeof p.voiceURI !== "string"
    )
      throw new Error("The backup profile is invalid.");
  for (const a of data.attempts)
    if (
      typeof a.id !== "string" ||
      !phraseById[a.phraseId] ||
      !modalities.includes(a.modality) ||
      !finite(a.at) ||
      !finite(a.latencyMs) ||
      ![true, false, null].includes(a.correct) ||
      typeof a.answer !== "string" ||
      typeof a.expected !== "string" ||
      typeof a.context !== "string" ||
      !["none", "pinyin", "transcript", "self-report"].includes(a.support)
    )
      throw new Error("The backup contains an invalid attempt.");
  for (const m of data.memories) {
    if (
      !phraseById[m.phraseId] ||
      !modalities.includes(m.modality) ||
      m.id !== `${m.phraseId}:${m.modality}` ||
      !m.card ||
      !finite(m.due) ||
      !finite(m.successes) ||
      !finite(m.failures)
    )
      throw new Error("The backup contains an invalid memory.");
    m.card.due = new Date(m.card.due);
    if (m.card.last_review) m.card.last_review = new Date(m.card.last_review);
    if (
      !Number.isFinite(m.card.due.getTime()) ||
      m.card.due.getTime() !== m.due ||
      (m.card.last_review && !Number.isFinite(m.card.last_review.getTime()))
    )
      throw new Error("A review date is invalid.");
    if (![0, 1, 2, 3].includes(m.card.state))
      throw new Error("A review schedule is invalid.");
    for (const key of [
      "stability",
      "difficulty",
      "elapsed_days",
      "scheduled_days",
      "reps",
      "lapses",
      "state",
      "learning_steps",
    ] as const)
      if (!finite(m.card[key]))
        throw new Error("A review schedule is invalid.");
  }
  for (const s of data.sessions)
    if (
      typeof s.id !== "string" ||
      typeof s.lessonId !== "string" ||
      !finite(s.completedAt) ||
      !finite(s.seconds) ||
      !finite(s.attempts) ||
      !["lesson", "conversation", "media", "assessment"].includes(s.kind)
    )
      throw new Error("A session is invalid.");
  for (const d of data.drafts)
    if (
      typeof d.id !== "string" ||
      !Number.isInteger(d.step) ||
      d.step < 0 ||
      d.step > 1000 ||
      !finite(d.updatedAt)
    )
      throw new Error("A saved lesson is invalid.");
  for (const m of data.mistakes)
    if (
      typeof m.id !== "string" ||
      !phraseById[m.phraseId] ||
      !modalities.includes(m.modality) ||
      typeof m.answer !== "string" ||
      typeof m.expected !== "string" ||
      !finite(m.count) ||
      !finite(m.at)
    )
      throw new Error("A mistake record is invalid.");
  await db.transaction("rw", db.tables, async () => {
    await db.profiles.bulkPut(data.profiles);
    await db.attempts.bulkPut(data.attempts);
    await db.memories.bulkPut(data.memories);
    await db.mistakes.bulkPut(data.mistakes);
    await db.sessions.bulkPut(data.sessions);
    await db.drafts.bulkPut(data.drafts);
  });
}
