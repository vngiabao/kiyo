import { readFileSync, readdirSync } from "node:fs";
import { expect, it } from "vitest";
import type { ContentPack, Line } from "../src/packs";
import { taskAudio } from "../src/tasks";
import { collectAudioScripts } from "../scripts/audio-manifest";
import { dialogueMood, voiceKey } from "../src/sayo-voice";
import { characterSpeech } from "../src/hanzi";

it("explicit pack glyphs do not replace bound-syllable word audio", () => {
  expect(characterSpeech("什")).toBe("什么");
  expect(characterSpeech("么")).toBe("什么");
  expect(characterSpeech("以")).toBe("可以");
});

const plan = JSON.parse(
  readFileSync("prompts/research/course-plan.json", "utf8"),
) as {
  units: {
    id: string;
    wordBudget: number;
    prerequisite: string;
    grammar: { code: string }[];
  }[];
};
const packs = readdirSync("content/packs")
  .filter((f) => /^s[123]-u\d+\.json$/.test(f))
  .map(
    (f) =>
      JSON.parse(readFileSync(`content/packs/${f}`, "utf8")) as ContentPack,
  )
  .filter((p) => plan.units.some((u) => u.id === p.unit.id));

it("new course units meet the approved allocation, connected practice and media shape", () => {
  for (const p of packs) {
    const u = plan.units.find((u) => u.id === p.unit.id)!;
    expect(p.vocabulary, p.unit.id).toHaveLength(u.wordBudget);
    expect(p.unit.prerequisites).toEqual([u.prerequisite]);
    expect(p.grammar?.map((g) => g.id)).toEqual(
      u.grammar.map((g) => `${u.id}-g${g.code}`),
    );
    expect(p.tasks!.length).toBeGreaterThanOrEqual(8);
    expect(p.tasks!.length).toBeLessThanOrEqual(10);
    expect(p.extraReadings?.length).toBeGreaterThanOrEqual(1);
    expect(p.dialogue!.questions).toHaveLength(3);
    expect(p.reading!.questions).toHaveLength(3);
    const context: Line[] = [
      ...p.dialogue!.lines,
      ...p.reading!.lines,
      ...p.extraReadings!.flatMap((r) => r.lines),
      ...p.grammar!.flatMap((g) => g.examples),
      ...p.tasks!.flatMap((t) => taskAudio(t)),
    ];
    for (const v of p.vocabulary) {
      expect(
        v.meaningVi?.trim(),
        `${u.id} ${v.hanzi}: Vietnamese meaning`,
      ).toBeTruthy();
      expect(
        new Set(context.filter((l) => l.zh.includes(v.hanzi)).map((l) => l.zh))
          .size,
        `${u.id} ${v.hanzi}: distinct contexts`,
      ).toBeGreaterThanOrEqual(2);
    }
  }
});

it("every supplementary reading line has the declared Sayo moods and an assembled full reading", () => {
  const scripts = new Map(
    collectAudioScripts().map((s) => [voiceKey(s.text), s]),
  );
  for (const p of packs)
    for (const r of p.extraReadings ?? []) {
      const speakers = [
        ...new Set(r.lines.map((l) => l.speaker).filter(Boolean)),
      ];
      for (const l of r.lines) {
        const script = scripts.get(voiceKey(l.zh))!;
        expect(script, `${r.id} ${l.zh}`).toBeDefined();
        expect(script.moods).toContain("clear");
        if (l.speaker)
          expect(script.moods).toContain(
            dialogueMood(speakers.indexOf(l.speaker)),
          );
        expect(script.kinds).toContain("extra-reading");
      }
      const full = scripts.get(voiceKey(r.lines.map((l) => l.zh).join("")))!;
      expect(full.parts).toHaveLength(r.lines.length);
    }
});
