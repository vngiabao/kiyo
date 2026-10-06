import { expect, it } from "vitest";
import { wordSpeech } from "../src/word-speech";
import { phrases } from "../src/content";

it("separates the reading of a word from its glyph's default reading", () => {
  expect(wordSpeech("地", "de")).toBe("认真地读");
  expect(wordSpeech("地", "dì")).toBe("地上");
  expect(wordSpeech("干", "gàn")).toBe("干什么");
  expect(wordSpeech("干", "gān")).toBe("干净");
  expect(wordSpeech("还", "huán")).toBe("还书");
  expect(wordSpeech("还", "hái")).toBe("还");
  expect(wordSpeech("们", "men")).toBe("朋友们");
  expect(wordSpeech("子", "zi")).toBe("桌子");
  expect(wordSpeech("子", "zǐ")).toBe("子");
  expect(wordSpeech("你好", "nǐ hǎo")).toBe("你好");
});

it("compiled course word audio retains its taught reading", () => {
  for (const p of phrases.filter((p) => p.id.startsWith("s") && ["干", "地", "还", "们", "子"].includes(p.hanzi)))
    expect(p.audio.text, `${p.id}: ${p.pinyin}`).toBe(wordSpeech(p.hanzi, p.pinyin));
});
