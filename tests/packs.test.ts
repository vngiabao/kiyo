import { readFileSync } from "node:fs";
import { describe, expect, it } from "vitest";
import {
  compilePack,
  expectedSyllables,
  pinyinMatches,
  syllables,
  validatePack,
  type ContentPack,
  type ValidationContext,
} from "../src/packs";
import { basePhrases, lessons, readingLessons, wordTiles } from "../src/content";
import { baseCharacters, baseReadings, isHan } from "../src/hanzi";

const example: ContentPack = JSON.parse(readFileSync("content/packs/_example.json", "utf8"));
const hsk = JSON.parse(readFileSync("content/hsk/levels.json", "utf8")).words;
const han = (s: string) => Array.from(s).filter(isHan);
const ctx = (): ValidationContext => ({
  knownUnits: new Set([...lessons, ...readingLessons].map((l) => l.id)),
  seenIds: new Set(basePhrases.map((p) => p.id)),
  knownChars: new Set([
    ...basePhrases.flatMap((p) => han(p.hanzi)),
    ...baseCharacters.map((c) => c.hanzi),
    ...baseReadings.flatMap((r) => r.lines.flatMap((l) => han(l.zh))),
  ]),
  knownWords: new Set(basePhrases.map((p) => p.hanzi)),
  hsk,
});
const clone = (): ContentPack => JSON.parse(JSON.stringify(example));

describe("pinyin rules", () => {
  it("splits syllables including erhua, apostrophes and standalone ér", () => {
    expect(syllables("yǒudiǎnr")).toEqual(["yǒu", "diǎnr"]);
    expect(expectedSyllables("有点儿", "yǒudiǎnr")).toBe(2);
    expect(expectedSyllables("女儿", "nǚ'ér")).toBe(2);
    expect(syllables("Xī'ān")).toEqual(["Xī", "ān"]);
  });
  it("accepts 一/不 tone changes and neutral-tone variants against the reference", () => {
    expect(pinyinMatches("一共", "yígòng", "yī gòng")).toBe(true);
    expect(pinyinMatches("谢谢", "xièxie", "xiè xiè")).toBe(true);
    expect(pinyinMatches("一会儿", "yíhuìr", "yī huì r")).toBe(true);
    expect(pinyinMatches("米饭", "mǐfān", "mǐ fàn")).toBe(false);
  });
  it("splits sentences into word tiles from the pinyin spacing", () => {
    expect(wordTiles("你想吃米饭还是面？", "Nǐ xiǎng chī mǐfàn háishi miàn?")).toEqual(["你", "想", "吃", "米饭", "还是", "面"]);
  });
});

describe("content pack validation", () => {
  it("the example pack passes with no errors", () => {
    expect(validatePack(example, ctx()).errors).toEqual([]);
  });
  it("rejects pinyin that doesn't match the characters", () => {
    const p = clone();
    p.vocabulary[1].pinyin = "mǐ";
    expect(validatePack(p, ctx()).errors.join()).toMatch(/2 characters but 1 pinyin syllables/);
  });
  it("rejects an HSK level that contradicts the official list", () => {
    const p = clone();
    p.vocabulary[0].hskLevel = 4; // 饿 is HSK 3.0 level 1
    expect(validatePack(p, ctx()).errors.join()).toMatch(/HSK 3\.0 list says 1/);
  });
  it("rejects answers that aren't exactly one of the choices", () => {
    const p = clone();
    p.dialogue!.questions![0].answer = "Soup";
    expect(validatePack(p, ctx()).errors.join()).toMatch(/answer must appear exactly once/);
  });
  it("rejects role-play patterns that would reject their own example replies", () => {
    const p = clone();
    p.conversation!.turns[0].accept = ["米饭"];
    expect(validatePack(p, ctx()).errors.join()).toMatch(/would be rejected/);
  });
  it("rejects text characters the reader can't explain", () => {
    const p = clone();
    p.reading!.lines[0].zh = "陈宇，昨天的面好吃吗？鬱";
    p.reading!.lines[0].py = "Chén Yǔ, zuótiān de miàn hǎochī ma? yù";
    expect(validatePack(p, ctx()).errors.join()).toMatch(/no meaning available for 鬱/);
  });
  it("rejects ids without the unit prefix and duplicate units", () => {
    const p = clone();
    p.vocabulary[0].id = "e";
    const c = ctx();
    c.knownUnits.add("s1-u01");
    const errors = validatePack(p, c).errors.join();
    expect(errors).toMatch(/must start with "s1-u01-"/);
    expect(errors).toMatch(/Duplicate unit id/);
  });
});

describe("compiling packs into lessons", () => {
  it("produces a words lesson, a usage lesson, two texts and a working role-play", () => {
    const c = compilePack(example);
    expect(c.lessons.map((l) => l.packPart)).toEqual(["words", "usage"]);
    expect(c.lessons[0].phrases).toHaveLength(11);
    expect(c.texts.map((t) => t.id)).toEqual(["s1-u01-d", "s1-u01-r"]);
    expect(c.texts[0].lines[0].speaker).toBe("林安");
    const turn = c.scenario!.turns[0];
    expect(turn.test("来一碗面")).toBe(true);
    expect(turn.test("我要一碗面。")).toBe(true);
    expect(turn.test("我要米饭")).toBe(false);
    expect(c.phrases.find((p) => p.id === "s1-u01-g-haishi-ex")?.hanzi).toBe("你想吃米饭还是面？");
  });
});
