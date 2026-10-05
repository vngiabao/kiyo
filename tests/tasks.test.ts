import { describe, expect, it } from "vitest";
import { allLessons, allTaskSteps, exercisesFor, lessons, reviewTaskFor, scramble, stepOf } from "../src/content";
import { readingLessons as readingLessonsForTest } from "../src/hanzi";
import { lessonTasks, checkTask, fillMatches, taskAudio, withGaps, plain, blanksOf } from "../src/tasks";

describe("practice tasks", () => {
  it("every authored task passes the content gate for its own lesson", () => {
    for (const [lessonId, tasks] of Object.entries(lessonTasks)) {
      const lesson = lessons.find((l) => l.id === lessonId);
      expect(lesson, lessonId).toBeTruthy();
      for (const t of tasks) expect(checkTask(t, new Set(lesson!.phrases)), t.id).toEqual([]);
    }
  });
  it("every phrase lesson has a conversation or listening practice", () => {
    for (const l of lessons) expect(lessonTasks[l.id]?.length ?? 0, l.id).toBeGreaterThan(0);
  });
  it("task ids are unique", () => {
    const ids = Object.values(lessonTasks).flat().map((t) => t.id);
    expect(new Set(ids).size).toBe(ids.length);
  });
  it("accepts hanzi, toned pinyin, toneless pinyin and tone numbers in fill-ins", () => {
    expect(fillMatches("谢谢", "谢谢", "xièxie")).toBe(true);
    expect(fillMatches("xièxie", "谢谢", "xièxie")).toBe(true);
    expect(fillMatches("xie xie", "谢谢", "xièxie")).toBe(true);
    expect(fillMatches("xie4xie", "谢谢", "xièxie")).toBe(true);
    expect(fillMatches("再见", "谢谢", "xièxie")).toBe(false);
    expect(fillMatches("xiexi", "谢谢", "xièxie")).toBe(false);
    expect(fillMatches("", "谢谢", "xièxie")).toBe(false);
  });
  it("blank helpers show gaps and play the full sentence", () => {
    expect(withGaps("你好，【谢谢】！")).toBe("你好，＿＿！");
    expect(plain("你好，【谢谢】！")).toBe("你好，谢谢！");
    expect(blanksOf("【明天】你有空吗？【几】点")).toEqual(["明天", "几"]);
  });
  it("gives each dialogue speaker their own mood and every other task Sayo's clear voice", () => {
    const d = lessonTasks.names.find((t) => t.type === "dialogue")!;
    const lines = taskAudio(d);
    const bySpeaker = new Map(lines.map((l) => [l.role, l.mood]));
    expect(new Set(bySpeaker.values()).size).toBe(bySpeaker.size);
    const tf = lessonTasks.names.find((t) => t.type === "truefalse")!;
    expect(taskAudio(tf).every((l) => l.mood === "clear" && !l.zh.includes("【"))).toBe(true);
  });
});

describe("lesson order", () => {
  it("never checks a phrase in the step right after it was introduced", () => {
    for (const l of lessons) {
      const steps = exercisesFor(l);
      steps.forEach((s, i) => {
        if (s.kind !== "choice") return;
        const prev = steps[i - 1];
        expect(prev.phraseId === s.phraseId && ["notice", "hear"].includes(prev.kind), `${l.id} step ${i}`).toBe(false);
      });
    }
  });
  it("never shows a character's meaning check right after meeting it", () => {
    for (const l of readingLessonsForTest) {
      const steps = exercisesFor(l);
      steps.forEach((s, i) => {
        if (s.kind !== "glyph") return;
        expect(steps[i - 1].kind === "meet" && steps[i - 1].phraseId === s.phraseId, `${l.id} step ${i}`).toBe(false);
      });
    }
  });
  it("places the conversation after every phrase has been met", () => {
    for (const l of lessons) {
      const steps = exercisesFor(l);
      const d = steps.findIndex((s) => s.kind === "dialogue");
      if (d < 0) continue;
      const lastNotice = steps.map((s) => s.kind).lastIndexOf("notice");
      expect(d, l.id).toBeGreaterThan(lastNotice);
    }
  });
  it("step ids are unique within a lesson", () => {
    for (const l of [...lessons, ...readingLessonsForTest]) {
      const ids = exercisesFor(l).map((s) => s.id);
      expect(new Set(ids).size, l.id).toBe(ids.length);
    }
  });
  it("scrambles build tiles out of order and not simply reversed", () => {
    for (const tiles of [["你", "叫", "什么", "名字"], ["a", "b", "c"], ["a", "b"]]) {
      const out = scramble(tiles);
      expect([...out].sort()).toEqual([...tiles].sort());
      expect(out).not.toEqual(tiles);
      if (tiles.length > 2) expect(out).not.toEqual([...tiles].reverse());
    }
  });
  it("never lets the answer's position give it away", () => {
    const positions: number[] = [];
    for (const l of allLessons)
      for (const e of exercisesFor(l)) {
        const t = e.task;
        if (t?.type === "dialogue") t.questions.forEach((q) => positions.push(q.choices.indexOf(q.answer)));
        else if (t?.type === "reply") positions.push(t.choices.indexOf(t.answer));
        else if (e.choices && e.correct) positions.push(e.choices.indexOf(e.correct));
      }
    expect(positions.every((p) => p >= 0)).toBe(true);
    // With 3–4 options, no single slot should hold the key for more than 40% of items.
    for (const slot of [0, 1, 2, 3]) expect(positions.filter((p) => p === slot).length / positions.length, `slot ${slot + 1}`).toBeLessThan(0.4);
  });
});

describe("review brings back tasks, not bare words", () => {
  const DAY = 86_400_000;
  it("brings back the exact task you missed", () => {
    const missed = allTaskSteps().find((e) => e.id === "first-first-tf1")!;
    const memory = { phraseId: missed.phraseId, modality: missed.modality, due: 40 * DAY };
    expect(reviewTaskFor(memory, "first-first-tf1")?.id).toBe("first-first-tf1");
    // A miss made during review is traced back to its lesson step too.
    expect(reviewTaskFor(memory, `review:first-first-tf1:${30 * DAY}`)?.id).toBe("first-first-tf1");
  });
  it("otherwise rotates through tasks that use the same phrase and skill", () => {
    const memory = { phraseId: "namequestion", modality: "listening", due: 0 };
    const seen = new Set(Array.from({ length: 6 }, (_, d) => reviewTaskFor({ ...memory, due: d * DAY })?.id));
    expect(seen.size).toBeGreaterThan(1);
    for (const id of seen) {
      const e = allTaskSteps().find((x) => x.id === id)!;
      expect([e.phraseId, e.modality]).toEqual(["namequestion", "listening"]);
    }
  });
  it("falls back to a plain review when no task uses the phrase", () => {
    expect(reviewTaskFor({ phraseId: "hemp", modality: "reading", due: 0 })).toBeNull();
  });
  it("traces review contexts back to lesson steps", () => {
    expect(stepOf("review:names-names-d:1728000000000")).toBe("names-names-d");
    expect(stepOf("names-names-d")).toBe("names-names-d");
  });
});
