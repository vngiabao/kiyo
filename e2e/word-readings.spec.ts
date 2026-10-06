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
