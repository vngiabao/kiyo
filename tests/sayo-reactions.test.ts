import { expect, it } from "vitest";
import {
  nextReaction,
  sayoReactions,
  type ReactionKind,
} from "../src/sayo-reactions";
import { collectAudioScripts } from "../scripts/audio-manifest";
import { welcomeGreeting } from "../src/sayo-lines";
import { voiceKey } from "../src/sayo-voice";

it("rotates every reaction in a category before repeating", () => {
  const kinds = [
    ...new Set(sayoReactions.map((r) => r.kind)),
  ] as ReactionKind[];
  expect(new Set(sayoReactions.map((r) => r.zh)).size).toBe(100);
  for (const kind of kinds) {
    const size = sayoReactions.filter((r) => r.kind === kind).length;
    const cycle = Array.from({ length: size }, () => nextReaction(kind).zh);
    expect(new Set(cycle).size).toBe(size);
    expect(nextReaction(kind).zh).toBe(cycle[0]);
  }
});

it("keeps every reaction and the welcome greeting in the fresh audio catalog", () => {
  const catalog = collectAudioScripts();
  for (const line of [welcomeGreeting, ...sayoReactions])
    expect(
      catalog.find((s) => voiceKey(s.text) === voiceKey(line.zh)),
    ).toBeDefined();
  for (const line of sayoReactions) {
    const script = catalog.find((s) => s.text === line.zh)!;
    expect(script.moods).toContain(line.mood);
    expect(script.delivery?.pitchOffset).toBeGreaterThanOrEqual(-0.5);
    expect(script.delivery?.pitchOffset).toBeLessThanOrEqual(0);
    expect(line.py).not.toBe("");
    expect(line.en).not.toBe("");
  }
});
