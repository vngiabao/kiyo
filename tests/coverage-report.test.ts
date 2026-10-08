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
  it("audits added levels without promoting incidental words or unmapped grammar", () => {
    const ref = inventory();
    ref.levels["6"] = {
      words: [["60", "六级", "道歉", "dào∥qiàn", ""], ["61", "六级", "此前", "cǐqián", "名"]],
      characters: [["60", "六级", "歉", "qiàn"]],
      grammar: [["60", "六级", "", "", "", "就算…也…"]],
    };
    const result = auditCoverage(ref, { ...input(),
      packs: [{ vocabulary: [{ hanzi: "道歉", pinyin: "dào qiàn", pos: "verb", hskLevel: 6,
        usageNote: "[GF2021:L6:60] Source: 道歉" }], grammar: [] } as unknown as ContentPack],
      text: "此前 appears only in a passage",
    }, {});
    const level = result.levels.find(l => l.level === 6)!;
    expect(level.words.introduced).toBe(1);
    expect(level.words.remainingEntries[0].entry).toBe("此前");
    expect(level.characters.introduced).toBe(0);
    expect(level.grammar.items[0].code).toBe("六01");
    expect(level.grammar.unmapped).toBe(1);
  });
  it("requires exact source evidence for prefixes, classifiers and numbered senses", () => {
    const ref = inventory();
    ref.levels["2"].words = [
      ["20", "二级", "老（老王）", "lǎo (Lǎo Wáng)", "前缀"],
      ["21", "二级", "下", "xià", "量"],
      ["22", "二级", "称1", "chēng", "动"],
    ];
    ref.levels["1"].words.push(["19", "一级", "下", "xià", "名"]);
    const words = [
      { hanzi: "老", pinyin: "lǎo", pos: "prefix", usageNote: "[GF2021:L2:20] 老（老王）" },
      { hanzi: "下", pinyin: "xià", pos: "classifier", usageNote: "[GF2021:L2:21] action count" },
      { hanzi: "称", pinyin: "chēng", pos: "verb", usageNote: "[GF2021:L2:22] weigh" },
    ];
    const count = (vocabulary: typeof words) => auditCoverage(ref, { ...input(),
      packs: [{ vocabulary, grammar: [] } as unknown as ContentPack],
    }, {}).levels[1].words.introduced;
    expect(count(words)).toBe(3);
    expect(count(words.map(w => ({ ...w, usageNote: "incidental appearance" })))).toBe(0);
    expect(count(words.map(w => ({ ...w, pos: "noun" })))).toBe(0);
    expect(count(words.map(w => ({ ...w, pinyin: "chèn" })))).toBe(0);
  });
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
  it("credits a higher-level sense through its exact source row without changing the minimum level", () => {
    const count = (pinyin: string, pos: string, usageNote: string) =>
      auditCoverage(inventory(), { ...input(), packs: [{
        vocabulary: [{ hanzi: "花", hskLevel: 1, pinyin, pos, usageNote }], grammar: [],
      } as unknown as ContentPack] }, {}).levels[1].words.introduced;
    expect(count("huā", "verb", "[GF2021:L2:3] spend money")).toBe(1);
    expect(count("huā", "noun", "[GF2021:L2:3] flower")).toBe(0);
    expect(count("huà", "verb", "[GF2021:L2:3] spend money")).toBe(0);
    expect(count("huā", "verb", "[GF2021:L2:4] wrong row")).toBe(0);
    expect(count("huā", "verb", "incidental appearance")).toBe(0);
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
  it("requires row-specific evidence for annotated suffixes and numbered lexical senses", () => {
    const ref = inventory();
    ref.levels["2"].words = [
      ["10", "二级", "家（科学家）", "jiā (kēxuéjiā)", "后缀"],
      ["11", "二级", "面1", "miàn", "名、量"],
      ["12", "二级", "面2", "miàn", "名"],
    ];
    const pack = { vocabulary: [
      { hanzi: "家", pinyin: "jiā", pos: "noun", hskLevel: 1 },
      { hanzi: "面", pinyin: "miàn", pos: "noun", hskLevel: 1,
        usageNote: "[GF2021:L2:12] noodles" },
    ], grammar: [] } as unknown as ContentPack;
    expect(auditCoverage(ref, { ...input(), packs: [pack] }, {}).levels[1].words.introduced).toBe(1);
    pack.vocabulary[0].pos = "suffix";
    pack.vocabulary[0].usageNote = "[GF2021:L2:10] 家（科学家） denotes an occupation specialist.";
    expect(auditCoverage(ref, { ...input(), packs: [pack] }, {}).levels[1].words.introduced).toBe(2);
  });
  it("requires the taught morpheme or template, its reading, sense and exact source row", () => {
    const ref = inventory();
    ref.levels["3"].words = [
      ["20", "三级", "初（初一）", "chū (chūyī)", "前缀"],
      ["21", "三级", "化（现代化）", "huà (xiàndàihuà)", "后缀"],
      ["22", "三级", "…极了", "…jí le", ""],
    ];
    const pack = { vocabulary: [
      { hanzi: "初", pinyin: "chū", pos: "prefix", hskLevel: 3,
        usageNote: "[GF2021:L3:20] 初（初一） is the lunar-date prefix." },
      { hanzi: "化", pinyin: "huà", pos: "suffix", hskLevel: 3,
        usageNote: "[GF2021:L3:21] 化（现代化） indicates transformation." },
      { hanzi: "极了", pinyin: "jí le", pos: "particle", hskLevel: 3,
        usageNote: "[GF2021:L3:22] …极了 follows a gradable adjective." },
    ], grammar: [] } as unknown as ContentPack;
    const count = () => auditCoverage(ref, { ...input(), packs: [pack] }, {}).levels[2].words.introduced;
    expect(count()).toBe(3);
    pack.vocabulary[0].hanzi = "初一";
    pack.vocabulary[0].pinyin = "chū yī";
    pack.vocabulary[0].pos = "noun";
    expect(count()).toBe(2);
    pack.vocabulary[1].usageNote = "[GF2021:L3:21] incidental mention";
    expect(count()).toBe(1);
    pack.vocabulary[2].pinyin = "jǐ le";
    expect(count()).toBe(0);
    pack.vocabulary[2].pinyin = "jí le";
    pack.vocabulary[2].usageNote = "[GF2021:L3:23] wrong row";
    expect(count()).toBe(0);
  });
});
