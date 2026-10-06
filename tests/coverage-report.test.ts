import { describe, expect, it } from "vitest";
import {
  alternatives,
  auditCoverage,
  type Inventory,
} from "../scripts/coverage-report";
import type { ContentPack } from "../src/packs";

const inventory = (): Inventory => ({
  standard: "fixture",
  source: "fixture",
  levels: {
    "1": {
      words: [
        ["1", "一级", "妈妈∣妈", "māma∣mā", "名"],
        ["2", "一级", "花", "huā", "名"],
      ],
      characters: [["1", "一级", "花", "huā"]],
      grammar: [["1", "一级", "", "", "", "能"]],
    },
    "2": {
      words: [
        ["3", "二级", "花", "huā", "动"],
        ["4", "二级", "语法", "yǔfǎ", "名"],
      ],
      characters: [
        ["2", "二级", "花", "huā"],
        ["3", "二级", "语", "yǔ"],
        ["4", "二级", "语", "yù"],
      ],
      grammar: [
        ["2", "二级", "", "", "", "※cross-reference"],
        ["3", "二级", "", "", "", "可能"],
      ],
    },
    "3": { words: [], characters: [], grammar: [] },
  },
});
const input = () => ({
  baseWords: ["妈", "花"],
  characters: ["花"],
  packs: [] as ContentPack[],
  text: "语法 appears here incidentally",
  grammar: [],
});

describe("course coverage audit", () => {
  it("does not credit another reading of an already-taught spelling", () => {
    const ref = inventory();
    ref.levels["1"].words = [
      ["1", "一级", "还", "hái", "副"],
      ["2", "一级", "还", "huán", "动"],
    ];
    const pack = {
      vocabulary: [{ hanzi: "还", pinyin: "hái", pos: "adverb", hskLevel: 1 }],
      grammar: [],
    } as unknown as ContentPack;
    const r = auditCoverage(ref, { ...input(), packs: [pack] }, {}).levels[0];
    expect(r.words.introduced).toBe(1);
    expect(r.words.remainingEntries[0].pinyin).toBe("huán");
  });
  it("counts a grouped alternative once and never counts incidental exposure", () => {
    const r = auditCoverage(inventory(), input(), {});
    expect(r.levels[0].words.introduced).toBe(2);
    expect(r.levels[1].words.introduced).toBe(0);
    expect(r.levels[1].words.incidentalOnlyCandidates).toHaveLength(1);
    expect(r.levels[1].words.repeatedFormNeedsReview).toHaveLength(1);
  });
  it("counts new characters separately from supplementary readings", () => {
    const r = auditCoverage(inventory(), input(), {}).levels[1];
    expect(r.characters.officialUnique).toBe(1);
    expect(r.characters.supplementaryReadings).toHaveLength(1);
    expect(r.characters.remaining).toEqual(["语"]);
  });
  it("excludes unnumbered grammar cross-references from printed codes", () => {
    const r = auditCoverage(inventory(), input(), {}).levels[1];
    expect(r.grammar.officialItems).toBe(1);
    expect(r.grammar.items[0].code).toBe("二01");
    expect(r.grammar.items[0].sourceNo).toBe("3");
  });
  it("requires explicit level evidence for a repeated word form", () => {
    const pack = {
      vocabulary: [{ hanzi: "花", hskLevel: 2 }],
      grammar: [],
    } as unknown as ContentPack;
    expect(
      auditCoverage(inventory(), { ...input(), packs: [pack] }, {}).levels[1]
        .words.introduced,
    ).toBe(1);
  });
  it("does not strip lexical suffix annotations into a different sense", () => {
    expect(alternatives("家（科学家）")).toEqual(["家（科学家）"]);
    expect(alternatives("第（第二）")).toEqual(["第"]);
  });
  it("requires an explicit neutral suffix lesson, not a compound or full-tone noun", () => {
    const ref = inventory();
    ref.levels["1"].words = [["1", "一级", "子（桌子）", "zi (zhuōzi)", "后缀"]];
    const evidence = (hanzi: string, pinyin: string, pos: string, usageNote?: string) =>
      auditCoverage(ref, { ...input(), baseWords: ["桌子"], packs: [{
        vocabulary: [{ hanzi, pinyin, pos, usageNote, hskLevel: 1 }], grammar: [],
      } as unknown as ContentPack] }, {}).levels[0].words.introduced;
    expect(evidence("桌子", "zhuōzi", "noun")).toBe(0);
    expect(evidence("子", "zǐ", "noun", "子（桌子）")).toBe(0);
    expect(evidence("子", "zi", "suffix")).toBe(0);
    expect(evidence("子", "zi", "suffix", "Official suffix entry 子（桌子）; neutral zi in 桌子.")).toBe(1);
  });
  it("rejects unverifiable grammar evidence", () => {
    expect(() =>
      auditCoverage(
        inventory(),
        {
          ...input(),
          grammar: [
            {
              code: "一01",
              cards: ["missing"],
              status: "introduced",
              note: "",
            },
          ],
        },
        {},
      ),
    ).toThrow("Unknown grammar card");
    const pack = {
      vocabulary: [],
      grammar: [{ id: "g" }],
    } as unknown as ContentPack;
    const e = {
      code: "一01",
      cards: ["g"],
      status: "partial" as const,
      note: "",
    };
    const r = auditCoverage(
      inventory(),
      { ...input(), packs: [pack], grammar: [e] },
      {},
    );
    expect(r.levels[0].grammar.partial).toBe(1);
    expect(r.levels[0].grammar.introduced).toBe(0);
    expect(() =>
      auditCoverage(
        inventory(),
        { ...input(), packs: [pack], grammar: [e, e] },
        {},
      ),
    ).toThrow("Duplicate grammar");
  });
});
