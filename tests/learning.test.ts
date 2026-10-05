import "fake-indexeddb/auto";
import { beforeEach, describe, expect, it } from "vitest";
import { db, saveAttempt, exportRecord, importRecord } from "../src/db";
import { dailyPlan, skillEvidence, updateMemory } from "../src/learning";
import { parseSrt } from "../src/MediaLab";
import { validateContent } from "../scripts/validate-content";
import { exercisesFor, readingLessons, charactersThrough, phraseById } from "../src/content";
import { charStatus } from "../src/Characters";
import { levelOf, streakOf } from "../src/progression";
import type { Attempt } from "../src/types";
const attempt = (overrides: Partial<Attempt> = {}): Attempt => ({
  id: crypto.randomUUID(),
  phraseId: "hello",
  modality: "listening",
  correct: true,
  answer: "Hello",
  expected: "Hello",
  at: Date.now(),
  latencyMs: 1400,
  support: "none",
  context: "test",
  ...overrides,
});
beforeEach(async () => {
  await db.transaction("rw", db.tables, async () => {
    for (const t of db.tables) await t.clear();
  });
});
describe("evidence and memory", () => {
  it("failed listening persists atomically without changing reading memory", async () => {
    await saveAttempt(attempt({ modality: "reading" }));
    const reading = await db.memories.get("hello:reading");
    await saveAttempt(attempt({ correct: false, answer: "Thank you" }));
    expect(await db.memories.get("hello:reading")).toEqual(reading);
    expect((await db.memories.get("hello:listening"))?.failures).toBe(1);
    expect((await db.memories.get("hello:listening"))?.due).toBeGreaterThan(
      Date.now() - 1000,
    );
    expect((await db.mistakes.get("hello:listening"))?.answer).toBe(
      "Thank you",
    );
    expect(await db.attempts.count()).toBe(2);
  });
  it("does not award unaided recognition for captions, pinyin, or self-report", () => {
    for (const support of ["transcript", "pinyin", "self-report"] as const)
      expect(updateMemory(undefined, attempt({ support }))).toBeNull();
    expect(
      updateMemory(undefined, attempt({ modality: "speaking" })),
    ).toBeNull();
    expect(
      updateMemory(undefined, attempt({ modality: "conversation" })),
    ).toBeNull();
    expect(updateMemory(undefined, attempt({ modality: "media" }))).toBeNull();
    expect(
      skillEvidence([attempt({ support: "transcript" })], "listening").count,
    ).toBe(0);
  });
  it("replaying a transaction is idempotent", async () => {
    const a = attempt();
    await saveAttempt(a);
    await saveAttempt(a);
    expect(await db.attempts.count()).toBe(1);
    expect((await db.memories.get("hello:listening"))?.successes).toBe(1);
  });
  it("records repeated mistakes and uses real FSRS schedules", async () => {
    await saveAttempt(attempt({ correct: false }));
    await saveAttempt(attempt({ correct: false, at: Date.now() + 600000 }));
    expect((await db.mistakes.get("hello:listening"))?.count).toBe(2);
    const m = await db.memories.get("hello:listening");
    expect(m?.card.reps).toBe(2);
    expect(m?.due).toBeGreaterThan(Date.now() + 600000);
  });
  it("adapts listening allocation only with evidence and preserves duration", () => {
    const evidence = [
      ...Array.from({ length: 3 }, () => attempt({ correct: false })),
      ...Array.from({ length: 3 }, () => attempt({ modality: "reading" })),
    ];
    const base = dailyPlan(30, [], 0),
      adapted = dailyPlan(30, evidence, 4);
    expect(
      adapted.items.find((i) => i.route === "listening")!.minutes,
    ).toBeGreaterThan(base.items.find((i) => i.route === "listening")!.minutes);
    for (const minutes of [10, 20, 30, 45, 60])
      expect(
        dailyPlan(minutes, evidence, 5).items.reduce(
          (n, i) => n + i.minutes,
          0,
        ),
      ).toBe(minutes);
  });
  it("exports and restores review dates as Dates", async () => {
    await saveAttempt(attempt());
    const backup = JSON.parse(JSON.stringify(await exportRecord()));
    await db.memories.clear();
    await importRecord(backup);
    expect((await db.memories.get("hello:listening"))?.card.due).toBeInstanceOf(
      Date,
    );
    await saveAttempt(attempt({ at: Date.now() + 86400000 }));
    expect((await db.memories.get("hello:listening"))?.card.reps).toBe(2);
  });
  it("rejects corrupt backups without partial writes", async () => {
    await saveAttempt(attempt());
    const backup = JSON.parse(JSON.stringify(await exportRecord()));
    backup.memories[0].card.stability = -1;
    await expect(importRecord(backup)).rejects.toThrow("schedule");
    expect(await db.attempts.count()).toBe(1);
  });
});
describe("characters-first track", () => {
  it("meeting a character is exposure, not evidence; reading recognition is scheduled separately", async () => {
    await saveAttempt(attempt({ phraseId: "c:人", modality: "reading", correct: null }));
    expect(await db.memories.get("c:人:reading")).toBeUndefined();
    await saveAttempt(attempt({ phraseId: "c:人", modality: "reading", correct: false, answer: "mouth" }));
    const m = await db.memories.get("c:人:reading");
    expect(m?.failures).toBe(1);
    expect((await db.mistakes.get("c:人:reading"))?.answer).toBe("mouth");
    expect(charStatus(m, true)).toBe("met");
    await saveAttempt(attempt({ phraseId: "c:人", modality: "reading", at: Date.now() + 600000 }));
    expect(charStatus(await db.memories.get("c:人:reading"), true)).toBe("recognised");
  });
  it("revealing pinyin makes a reading answer supported practice", () =>
    expect(
      updateMemory(undefined, attempt({ phraseId: "c:人", modality: "reading", support: "pinyin" })),
    ).toBeNull());
  it("every character is met before it is quizzed, and words use only known characters", () => {
    for (const lesson of readingLessons) {
      const met = new Set<string>();
      const known = charactersThrough(lesson.id);
      for (const e of exercisesFor(lesson)) {
        if (e.kind === "meet") met.add(e.phraseId);
        if (["glyph", "pick", "spot", "count"].includes(e.kind)) expect(met.has(e.phraseId), e.id).toBe(true);
        if (e.kind === "read")
          for (const ch of phraseById[e.phraseId].hanzi) expect(known.has(ch), e.id).toBe(true);
      }
      expect(met.size).toBe(lesson.phrases.length);
    }
  });
  it("characters-first plans still include listening and speaking every day", () => {
    for (const minutes of [10, 20, 30, 45, 60]) {
      const plan = dailyPlan(minutes, [], 3, "characters");
      expect(plan.items.reduce((n, i) => n + i.minutes, 0)).toBe(minutes);
      for (const route of ["characters", "reading", "listening", "speak"])
        expect(plan.items.find((i) => i.route === route)?.minutes).toBeGreaterThan(0);
    }
  });
});
describe("levels and days in a row", () => {
  const day = 86400000;
  const noon = new Date(2026, 9, 4, 12).getTime();
  it("a level is a finished lesson, counted once; checks and readings don't inflate it", () => {
    const s = (lessonId: string) => ({ lessonId, kind: "lesson" as const });
    expect(levelOf([]).level).toBe(1);
    expect(levelOf([s("read-1"), s("read-1"), s("listening:read-1"), s("read:p-horse"), s("first")]).level).toBe(3);
  });
  it("counts consecutive local study days and keeps yesterday's run alive today", () => {
    const at = (t: number) => ({ at: t });
    expect(streakOf([], [at(noon), at(noon - day), at(noon - 2 * day)], noon)).toEqual({ days: 3, studiedToday: true });
    expect(streakOf([], [at(noon - day), at(noon - 2 * day)], noon)).toEqual({ days: 2, studiedToday: false });
    expect(streakOf([], [at(noon - 3 * day)], noon).days).toBe(0);
    expect(streakOf([{ completedAt: noon }], [], noon).days).toBe(1);
  });
});
describe("curriculum and media", () => {
  it("has internally consistent content and answer keys", () =>
    expect(validateContent()).toEqual([]));
  it("parses captions with CRLF, Unicode, comma or dot milliseconds", () => {
    expect(
      parseSrt(
        "1\r\n00:00:01,500 --> 00:00:03.000\r\n你好\r\n\r\n2\r\n00:00:03,000 --> 00:00:04,000\r\n再见",
      ),
    ).toEqual([
      { start: 1.5, end: 3, text: "你好" },
      { start: 3, end: 4, text: "再见" },
    ]);
  });
  it("rejects invalid caption timing", () =>
    expect(parseSrt("1\n00:00:05,000 --> 00:00:01,000\nNo")).toEqual([]));
});
