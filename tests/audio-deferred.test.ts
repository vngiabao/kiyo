import { expect, it } from "vitest";
import { deferredKeys } from "../scripts/audio-deferred";
import { voiceKey } from "../src/sayo-voice";

it("defers manifest assemblies without exempting arbitrary substring matches", () => {
  const keys = deferredKeys(["女孩儿"], [
    { text: "女孩儿。你好。", parts: [{ text: "女孩儿" }, { text: "你好。" }] },
    { text: "她说女孩儿。", parts: [{ text: "她说" }, { text: "女孩儿。你好。" }] },
  ]);
  expect(keys.has(voiceKey("女孩儿。"))).toBe(true);
  expect(keys.has(voiceKey("女孩儿。你好。"))).toBe(true);
  expect(keys.has(voiceKey("她说女孩儿。"))).toBe(true);
  expect(keys.has(voiceKey("那个女孩儿会游泳。"))).toBe(false);
  expect(keys.has(voiceKey("你好。"))).toBe(false);
});
