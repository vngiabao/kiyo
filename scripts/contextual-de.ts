import { readFileSync } from "node:fs";
import { syllables, isHan } from "../src/packs";

const rules = JSON.parse(
  readFileSync(
    new URL("../content/hsk/contextual-de.json", import.meta.url),
    "utf8",
  ),
) as {
  lexemes: Record<string, string>;
  exactContexts: Record<string, string>;
  complementStems: string[];
  modalTails: string[];
  modalHeads: string[];
};

export function deReading(text: string, index: number): string | undefined {
  if (text === "得很" && index === 0) return "de";
  for (const field of [rules.exactContexts, rules.lexemes]) {
    for (const [word, tone] of Object.entries(field).sort(
      (a, b) => b[0].length - a[0].length,
    )) {
      const start = index - word.indexOf("得");
      if (start >= 0 && text.slice(start, start + word.length) === word)
        return tone;
    }
  }
  const before = text.slice(0, index),
    after = text.slice(index + 1);
  if (rules.complementStems.some((stem) => before.endsWith(stem))) return "de";
  if (rules.modalTails.some((tail) => after.startsWith(tail))) return "děi";
  if (rules.modalHeads.some((head) => before.endsWith(head))) return "děi";
}

export function checkDePinyin(text: string, pinyin: string) {
  text = text.replace(/[【】]/g, "");
  const han = Array.from(text).filter(isHan),
    tokens = syllables(pinyin);
  const issues: string[] = [];
  let si = 0,
    fullIndex = 0;
  for (const char of han) {
    fullIndex = text.indexOf(char, fullIndex);
    if (
      char === "儿" &&
      si &&
      /r$/i.test(tokens[si - 1]) &&
      !/^[eēéěè]r$/i.test(tokens[si - 1])
    ) {
      fullIndex++;
      continue;
    }
    if (si >= tokens.length)
      throw new Error(`Cannot align authored pinyin: ${text}`);
    if (char === "得") {
      const expected = deReading(text, fullIndex);
      if (expected && tokens[si].toLowerCase() !== expected)
        issues.push(`得 needs ${expected}, found ${tokens[si]}`);
      if (!expected && text !== "得")
        issues.push(
          `Unreviewed 得 context: ${text.slice(Math.max(0, fullIndex - 6), fullIndex + 7)}`,
        );
    }
    si++;
    fullIndex++;
  }
  if (si !== tokens.length)
    throw new Error(`Cannot align authored pinyin: ${text}`);
  return issues;
}
