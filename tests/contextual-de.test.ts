import { describe, expect, it } from "vitest";
import { checkDePinyin } from "../scripts/contextual-de";

describe("contextual 得 readings", () => {
  it("keeps a potential complement distinct from obtaining", () => {
    expect(
      checkDePinyin(
        "找得到书，才得到答案。",
        "zhǎo de dào shū, cái dé dào dá àn.",
      ),
    ).toEqual([]);
    expect(checkDePinyin("找得到书。", "zhǎo dé dào shū.")).toEqual([
      "得 needs de, found dé",
    ]);
  });
  it("separates a complement, obligation, and actual obtaining", () => {
    expect(
      checkDePinyin(
        "我得走了，她说得很清楚，也得到了答复。",
        "wǒ děi zǒu le, tā shuō de hěn qīng chǔ, yě dé dào le dá fù.",
      ),
    ).toEqual([]);
    expect(checkDePinyin("我得走了。", "wǒ dé zǒu le.")).toEqual([
      "得 needs děi, found dé",
    ]);
    expect(checkDePinyin("她说得很清楚。", "tā shuō dé hěn qīng chǔ.")).toEqual(
      ["得 needs de, found dé"],
    );
  });
  it("keeps bound source forms distinct and does not infer a bare citation", () => {
    expect(
      checkDePinyin("舍不得，也只得走了。", "shě bu de, yě zhǐ dé zǒu le."),
    ).toEqual([]);
    for (const py of ["dé", "de", "děi"])
      expect(checkDePinyin("得", py)).toEqual([]);
    expect(checkDePinyin("这个安排得改。", "zhè ge ān pái děi gǎi.")).toEqual(
      [],
    );
  });
  it("aligns compact pinyin and erhua without moving other syllables", () => {
    expect(checkDePinyin("有空儿就得来。", "yǒukòngr jiùděilái.")).toEqual([]);
    expect(checkDePinyin("她读得很清楚。", "tā dúde hěnqīngchǔ.")).toEqual([]);
  });
  it("distinguishes scoring from potential and degree complements", () => {
    expect(
      checkDePinyin(
        "她得了三分，高兴得想跳起来，箱子也拿得动。",
        "tā dé le sān fēn, gāo xìng de xiǎng tiào qǐ lái, xiāng zi yě ná de dòng.",
      ),
    ).toEqual([]);
    expect(checkDePinyin("得很", "de hěn")).toEqual([]);
    expect(checkDePinyin("得很", "dé hěn")).toEqual([
      "得 needs de, found dé",
    ]);
  });
  it("fails unknown contexts and broken alignment rather than guessing", () => {
    expect(checkDePinyin("这得行。", "zhè dé xíng.")[0]).toContain(
      "Unreviewed",
    );
    expect(() => checkDePinyin("她说得好。", "tā de hǎo.")).toThrow(
      "Cannot align",
    );
  });
});
