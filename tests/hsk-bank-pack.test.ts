import { readFileSync } from "node:fs";
import { expect, it } from "vitest";
import { validateHskPack, verifiedBankText, type HskBankPack, type HskItem } from "../src/hsk-pack";
const words = JSON.parse(readFileSync("content/hsk/levels.json", "utf8")).words;
const choices = [
  { zh: "水", py: "shuǐ", en: "water" },
  { zh: "茶", py: "chá", en: "tea" },
  { zh: "书", py: "shū", en: "book" },
  { zh: "米饭", py: "mǐ fàn", en: "rice" },
];
function fixture(): HskBankPack {
  const items: HskItem[] = [];
  for (const unit of ["identity", "numbers", "daily", "sample"] as const)
    for (let i = 0; i < 8; i++) items.push({
      id: `test-${unit}-${i}`, unit, format: "cloze", prompt: "我喝___。",
      sentence: "我喝水。", py: "wǒ hē shuǐ", en: "I drink water.",
      choices, answer: "水", explanation: "水 supplies the stated object of 喝.",
    });
  return { kind: "hsk-practice", version: 2, standard: "GF2021 practice", level: 1,
    id: "test-bank", provenance: { author: "test", status: "fixture", sources: ["local official inventory"] }, items };
}
it("rejects wrong readings, above-level words and answer-key damage", () => {
  expect(validateHskPack(fixture(), words)).toEqual([]);
  const bad = fixture();
  bad.items[0].py = "wǒ hē shū";
  bad.items[1].answer = "茶";
  bad.items[2].choices = [...choices.slice(0, 3), { zh: "参加", py: "cān jiā", en: "participate" }];
  const errors = validateHskPack(bad, words);
  expect(errors.some((s) => s.includes("sentence level/pinyin"))).toBe(true);
  expect(errors.some((s) => s.includes("blank/answer mismatch"))).toBe(true);
  expect(errors.some((s) => s.includes("unverified choice 参加"))).toBe(true);
});
it("requires a dictionary-backed question and correct ordering segments", () => {
  const pack = fixture();
  pack.items[0] = { ...pack.items[0], format: "listening", prompt: "喝什么？", promptPy: "hē shén me" };
  pack.items[1] = { ...pack.items[1], format: "reading", prompt: "喝什么？", promptPy: "hē shén me" };
  pack.items[2] = { ...pack.items[2], format: "ordering", prompt: "怎么说？", promptPy: "zěn me shuō", sentence: "我喝水", answer: "我喝水",
    segments: [{ zh: "我", py: "wǒ", en: "I" }, { zh: "喝", py: "hē", en: "drink" }, choices[0]],
    choices: [
      { zh: "我喝水", py: "wǒ hē shuǐ", en: "I drink water." },
      { zh: "喝我水", py: "hē wǒ shuǐ", en: "Scrambled: drink / I / water." },
      { zh: "水我喝", py: "shuǐ wǒ hē", en: "Scrambled: water / I / drink." },
      { zh: "我水喝", py: "wǒ shuǐ hē", en: "Scrambled: I / water / drink." },
    ] };
  expect(validateHskPack(pack, words)).toEqual([]);
  pack.items[0].promptPy = "hē shū";
  pack.items[2].segments!.reverse();
  expect(validateHskPack(pack, words)).toEqual(expect.arrayContaining([
    expect.stringContaining("unverified question"), expect.stringContaining("ordering segments/answer mismatch"),
  ]));
});
it("uses a reading that actually segments the whole phrase, not glyph defaults", () => {
  expect(verifiedBankText("什么", "shén me", words, 1)).toBe(true);
  expect(verifiedBankText("什么", "shí me", words, 1)).toBe(false);
  expect(verifiedBankText("还书", "huán shū", words, 1)).toBe(true);
  expect(verifiedBankText("参加", "cān jiā", words, 1)).toBe(false);
  expect(verifiedBankText("参加", "cān jiā", words, 2)).toBe(true);
});
