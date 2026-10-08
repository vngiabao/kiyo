import { expect, test } from "@playwright/test";
import { readFileSync } from "node:fs";
import type { ContentPack } from "../src/packs";
import { wordSpeech } from "../src/word-speech";
import { voiceKey } from "../src/sayo-voice";

test("course word taps use the taught reading instead of the glyph default", async ({ page }) => {
  await page.goto("/");
  await page.getByRole("button", { name: /Start without an account/ }).click();
  await page.getByRole("button", { name: "Continue", exact: true }).click();
  await page.getByRole("button", { name: "Continue", exact: true }).click();
  await page.getByRole("checkbox", { name: "Start in quiet mode" }).check();
  await page.getByRole("button", { name: "Meet your first characters" }).click();
  await page.getByRole("button", { name: "Save and exit" }).click();
  await page.getByRole("button", { name: "Dictionary", exact: true }).first().click();
  const clips = JSON.parse(readFileSync("src/audio-assets.json", "utf8")) as Record<string, Record<string, string>>;
  const packs = JSON.parse(readFileSync("src/generated/packs.json", "utf8")) as ContentPack[];
  const words = packs.flatMap((p) => p.vocabulary).filter((p) => /^s[123]-u\d+-w/u.test(p.id) && ["干", "地", "还", "们", "子"].includes(p.hanzi));
  expect(words.length).toBeGreaterThan(0);
  for (const p of words) {
    await page.getByPlaceholder("Try 你好, ni hao, or hello…").fill(p.hanzi);
    const url = clips[voiceKey(wordSpeech(p.hanzi, p.pinyin))]?.clear;
    expect(url, `${p.id}: ${p.pinyin}`).toBeTruthy();
    const response = page.waitForResponse((r) => new URL(r.url()).pathname === url && [200, 206].includes(r.status()));
    await page.locator(".word-list button").filter({ hasText: p.meaning }).first().click();
    await response;
    await expect(page.getByText(/Using your device’s Mandarin voice/u)).toHaveCount(0);
  }
});
import { charByHanzi } from "../src/hanzi";
import { isDeferred } from "../scripts/audio-deferred";

// Run the batch's actual character entries, including the repaired source readings.
const characterPacks = JSON.parse(readFileSync("src/generated/packs.json", "utf8")) as ContentPack[];
const batchIds = process.env.COURSE_UNIT_IDS?.split(",") ?? characterPacks.slice(-4).map((p) => p.unit.id);
const batchGlyphs = [...new Set([
  "觉", "兴", "识", "候",
  ...characterPacks.filter((p) => batchIds.includes(p.unit.id)).flatMap((p) => (p.characters ?? []).map((c) => c.hanzi)),
])];

test("batch character sheets play their contextual recordings or explicitly declared device fallback", async ({ page }) => {
  test.setTimeout(180000);
  await page.addInitScript(() => {
    const play = HTMLMediaElement.prototype.play;
    HTMLMediaElement.prototype.play = function () {
      this.addEventListener("ended", () => {
        document.documentElement.dataset.characterAudioEnded = this.src;
      }, { once: true });
      return play.call(this);
    };
    // This stub checks routing only for owner-deferred lines, not their sound quality.
    Object.defineProperty(window, "SpeechSynthesisUtterance", {
      value: class { constructor(public text: string) {} },
    });
    Object.defineProperty(speechSynthesis, "getVoices", {
      value: () => [{ lang: "zh-CN", voiceURI: "test-mandarin", localService: true,
        name: "Test Mandarin", default: true }],
    });
    Object.defineProperty(speechSynthesis, "speak", {
      value: (utterance: SpeechSynthesisUtterance) => {
        document.documentElement.dataset.characterDeviceSpeech = utterance.text;
        utterance.onstart?.(new Event("start") as SpeechSynthesisEvent);
        utterance.onend?.(new Event("end") as SpeechSynthesisEvent);
      },
    });
  });
  await page.goto("/");
  await page.getByRole("button", { name: /Start without an account/ }).click();
  await page.getByRole("button", { name: "Continue", exact: true }).click();
  await page.getByRole("button", { name: "Continue", exact: true }).click();
  await page.getByRole("checkbox", { name: "Start in quiet mode" }).check();
  await page.getByRole("button", { name: "Meet your first characters" }).click();
  await page.getByRole("button", { name: "Save and exit" }).click();
  await page.locator(".main-nav").getByRole("button", { name: "Read", exact: true }).click();
  await page.getByRole("tab", { name: "All characters", exact: true }).click();
  const clips = new Map(Object.entries(
    JSON.parse(readFileSync("src/audio-assets.json", "utf8")) as Record<string, Record<string, string>>,
  ).map(([text, moods]) => [voiceKey(text), moods]));
  for (const glyph of batchGlyphs) {
    const entry = charByHanzi[glyph];
    expect(entry, glyph).toBeTruthy();
    const deferred = isDeferred(entry.say);
    const url = clips.get(voiceKey(entry.say))?.clear;
    if (!deferred) expect(url, `${glyph}: ${entry.say}`).toBeTruthy();
    // Opening the wall cell already plays and caches this recording.
    const response = !deferred ? page.waitForResponse((r) =>
      new URL(r.url()).pathname === url && r.ok(), { timeout: 15000 }) : null;
    await page.locator(".char-wall button").filter({ hasText: new RegExp(`^${glyph}$`) }).click();
    if (response) await response;
    const sheet = page.getByRole("dialog", { name: `Character ${glyph}`, exact: true });
    await expect(sheet.locator(".anatomy-pinyin")).toHaveText(entry.pinyin);
    await page.evaluate(() => {
      delete document.documentElement.dataset.characterAudioEnded;
      delete document.documentElement.dataset.characterDeviceSpeech;
    });
    if (deferred) {
      await sheet.getByRole("button", { name: "Say it", exact: true }).click();
      await expect.poll(() => page.evaluate(() => document.documentElement.dataset.characterDeviceSpeech)).toBe(entry.say);
      await expect(sheet.getByRole("alert")).toContainText("Using your device’s Mandarin voice");
    } else {
      await sheet.getByRole("button", { name: "Say it", exact: true }).click();
      await expect.poll(() => page.evaluate(() => document.documentElement.dataset.characterAudioEnded), { timeout: 15000 }).toBe(new URL(url!, page.url()).href);
      await expect(sheet.getByRole("alert")).toHaveCount(0);
    }
    await sheet.getByRole("button", { name: "Close", exact: true }).click();
  }
});
