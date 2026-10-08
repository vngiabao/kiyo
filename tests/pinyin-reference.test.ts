import { expect, it } from "vitest";
import { normalizePinyinReference } from "../scripts/pinyin-reference";
import { pinyinMatches, syllables } from "../src/packs";

it("keeps the dictionary's two syllables and rejects an actual wrong reading", () => {
  const reference = normalizePinyinReference("hū lu:è");
  expect(syllables(reference)).toEqual(["hū", "lüè"]);
  expect(pinyinMatches("忽略", "hū lüè", reference)).toBe(true);
  expect(pinyinMatches("忽略", "hū lǜ", reference)).toBe(false);
  expect(pinyinMatches("忽略", "hú lüè", reference)).toBe(false);
  expect(pinyinMatches("忽略", "hū lüè le", reference)).toBe(false);
});

it("preserves tone marks and ordinary readings", () => {
  expect(normalizePinyinReference("LÜÈ lüè huán hái")).toBe("LÜÈ lüè huán hái");
  expect(normalizePinyinReference("LU:È")).toBe("LÜÈ");
});
