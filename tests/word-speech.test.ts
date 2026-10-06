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
  expect(wordSpeech("头", "tou")).toBe("里头");
  expect(wordSpeech("头", "tóu")).toBe("头");
  expect(wordSpeech("得", "de")).toBe("说得清楚");
  expect(wordSpeech("得", "dé")).toBe("得到");
  expect(wordSpeech("得", "děi")).toBe("我得去");
  expect(wordSpeech("过", "guo")).toBe("去过");
  expect(wordSpeech("过", "guò")).toBe("过");
  expect(wordSpeech("长", "zhǎng")).toBe("长大");
  expect(wordSpeech("长", "cháng")).toBe("很长");
  expect(wordSpeech("行", "háng")).toBe("一行字");
  expect(wordSpeech("行", "xíng")).toBe("行");
  expect(wordSpeech("只", "zhī")).toBe("一只猫");
  expect(wordSpeech("只", "zhǐ")).toBe("只");
  expect(wordSpeech("了", "liǎo")).toBe("没完没了");
  expect(wordSpeech("了", "le")).toBe("了");
  expect(wordSpeech("精神", "jīng shen")).toBe("很精神");
  expect(wordSpeech("精神", "jīng shén")).toBe("精神力量");
  expect(wordSpeech("你好", "nǐ hǎo")).toBe("你好");
});

it("compiled course word audio retains its taught reading", () => {
  for (const p of phrases.filter((p) => p.id.startsWith("s") && ["干", "地", "还", "们", "子", "头", "得", "过", "长", "行", "只"].includes(p.hanzi)))
    expect(p.audio.text, `${p.id}: ${p.pinyin}`).toBe(wordSpeech(p.hanzi, p.pinyin));
});
