import { expect, it } from "vitest";
import { isDeferred } from "../scripts/audio-deferred";
import scripts from "../content/audio-scripts.json";
import { phrases, grammarById, packScenarios } from "../src/content";
import { characters, readings, characterSpeech, isHan } from "../src/hanzi";
import { mascotScenes, moLines } from "../src/sayo-lines";
import { reactionMood, voiceKey } from "../src/sayo-voice";
import { readFileSync } from "node:fs";
import { createHash } from "node:crypto";
import { lessonTasks, taskAudio } from "../src/tasks";
import { compiledPacks } from "../src/pack-content";
import assets from "../src/audio-assets.json";

const index = new Map(scripts.map((s) => [voiceKey(s.text), s]));
it("the installed voice uses the exact approved identity and one-pass clean processing", () => {
  const roster = JSON.parse(readFileSync("content/voices/roster.json", "utf8"));
  const profile = JSON.parse(
    readFileSync("content/voices/approved-b-half/profile.json", "utf8"),
  );
  const receipt = JSON.parse(
    readFileSync("content/voices/sayo-library-provenance.json", "utf8"),
  );
  expect(roster.approvedProfile).toBe(
    "content/voices/approved-b-half/profile.json",
  );
  expect(receipt.model).toEqual(profile.model);
  const profileSha256 = createHash("sha256")
    .update(readFileSync(roster.approvedProfile))
    .digest("hex");
  for (const clip of receipt.clips.filter(
    (c: { parts?: unknown }) => !c.parts,
  )) {
    expect(clip.pitchMethod, clip.text).toBe("resample");
    expect(clip.pitchShift, clip.text).toBe(
      -2.25 + (clip.delivery?.pitchOffset ?? 0),
    );
    expect(clip.profileSha256).toBe(profileSha256);
  }
  for (const selected of profile.clips.filter(
    (c: { id: string }) => c.id !== "words",
  )) {
    const clip = receipt.clips.find(
      (c: { text: string; mood: string }) =>
        voiceKey(c.text) === voiceKey(selected.text) &&
        c.mood === reactionMood(selected.text),
    );
    expect(clip?.approvedTake, selected.text).toBe(true);
    expect(clip?.alreadyProcessed, selected.text).toBe(true);
    expect(clip?.rawSha256, selected.text).toBe(selected.approved.sha256);
  }
});
it("every task line has both a generation entry and installed audio in its required mood", () => {
  const installed = new Map(
    Object.entries(assets).map(([text, voices]) => [
      voiceKey(text),
      voices as Record<string, string>,
    ]),
  );
  const tasks = [
    ...Object.values(lessonTasks).flat(),
    ...compiledPacks.flatMap((p) => p.tasks),
  ];
  for (const task of tasks)
    for (const line of taskAudio(task)) {
      expect(line.zh, task.id).not.toMatch(/[【】]/u);
      // Owner-deferred lines ship without a Sayo clip (content/voices/audio-deferred.json).
      if (isDeferred(line.zh)) continue;
      expect(
        index.get(voiceKey(line.zh))?.moods,
        task.id + " " + line.zh,
      ).toContain(line.mood);
      expect(
        installed.get(voiceKey(line.zh))?.[line.mood],
        task.id + " " + line.zh,
      ).toMatch(/^\/audio-v2\//);
    }
});
it("every installed gallery reaction avoids the old phase-vocoder processing", () => {
  const receipt = JSON.parse(
    readFileSync("content/voices/sayo-library-provenance.json", "utf8"),
  ) as { clips: { text: string; mood: string; pitchMethod?: string }[] };
  for (const scene of mascotScenes) {
    const clip = receipt.clips.find(
      (c) =>
        voiceKey(c.text) === voiceKey(scene.say.zh) &&
        c.mood === reactionMood(scene.say.zh),
    );
    expect(clip?.pitchMethod, scene.name).toBe("resample");
  }
});
it("the generation catalog covers teaching text and contextual character pronunciation", () => {
  const text = [
    ...phrases.flatMap((p) => [
      p.audio.text,
      ...(p.example ? [p.example.zh] : []),
    ]),
    ...characters.flatMap((c) => [c.say, ...c.words.map((w) => w.w)]),
    ...Object.values(grammarById).flatMap((g) => g.examples.map((e) => e.zh)),
    ...readings.flatMap((r) => [
      ...r.lines.map((l) => l.zh),
      r.lines.map((l) => l.zh).join(""),
    ]),
    ...readings.flatMap((r) =>
      r.lines.flatMap((l) =>
        Array.from(l.zh).filter(isHan).map(characterSpeech),
      ),
    ),
    ...packScenarios.flatMap((s) => s.turns.map((t) => t.text)),
  ];
  for (const value of text) {
    expect(index.get(voiceKey(value)), value).toBeDefined();
    expect(index.get(voiceKey(value))?.moods, value).toContain("clear");
    expect(index.get(voiceKey(value))?.moods, value).toContain("playful");
  }
});
it("every Sayo reaction has its requested mood in the generation catalog", () => {
  const lines = [
    ...mascotScenes.map((s) => s.say),
    ...Object.values(moLines).flat(),
  ];
  for (const line of lines)
    expect(index.get(voiceKey(line.zh))?.moods, line.zh).toContain(
      reactionMood(line.zh),
    );
  expect(reactionMood("不错嘛。")).toBe("deadpan");
  expect(reactionMood("来了？开始吧。")).toBe("playful");
  expect(reactionMood("没关系，再试试。")).toBe("soft");
  expect(reactionMood("升级了！")).toBe("intense");
});
