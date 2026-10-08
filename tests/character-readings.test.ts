import { expect, it } from "vitest";
import { charByHanzi, characterSpeech } from "../src/hanzi";

it("觉 teaches jué through 觉得 without borrowing the jiào reading from 睡觉", () => {
  const entry = charByHanzi["觉"];
  expect(entry.pinyin).toBe("jué");
  expect(entry.say).toBe("觉得");
  expect(characterSpeech("觉")).toBe("觉得");
  expect(entry.words[0]).toMatchObject({ w: "觉得", m: "feel; think" });
  expect(entry.note).toContain("jiào");
});

it("兴 keeps the xīng source reading distinct from 高兴 xìng", () => {
  const entry = charByHanzi["兴"];
  expect(entry.pinyin).toBe("xīng");
  expect(entry.say).toBe("兴");
  expect(characterSpeech("兴")).toBe("兴");
  expect(entry.meaning).toContain("rise; flourish");
  expect(entry.note).toContain("xìng");
});

it("connected neutral syllables are explained rather than mistaken for different lexical readings", () => {
  expect(charByHanzi["识"].pinyin).toBe("shí");
  expect(charByHanzi["识"].say).toBe("知识");
  expect(charByHanzi["识"].note).toContain("neutral");
  expect(charByHanzi["候"].pinyin).toBe("hòu");
  expect(charByHanzi["候"].say).toBe("时候");
  expect(charByHanzi["候"].note).toContain("neutral");
});
