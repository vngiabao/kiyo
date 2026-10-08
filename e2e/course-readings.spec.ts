import { expect, test } from "@playwright/test";
import { readFileSync, readdirSync } from "node:fs";
import { isDeferred } from "../scripts/audio-deferred";

// Exercise the latest batch in disposable contexts; do not change the owner's progress.
const selectedIds = process.env.COURSE_UNIT_IDS?.split(",");
const files = selectedIds
  ? selectedIds.map((id) => `${id}.json`)
  : readdirSync("content/packs")
      .filter((name) => /^s[1-6]-u\d+\.json$/.test(name))
      .sort()
      .slice(-4);
const latest = files.map((name) =>
  JSON.parse(readFileSync(`content/packs/${name}`, "utf8")),
);

for (const pack of latest) {
  for (const reading of pack.extraReadings ?? []) {
    const deferred = reading.lines.some((l: { zh: string }) =>
      isDeferred(l.zh),
    );
    test(`${reading.id}: supplementary scene reaches the reader and declared speech provider`, async ({
      page,
    }) => {
      if (deferred)
        await page.addInitScript(() => {
          Object.defineProperty(window, "SpeechSynthesisUtterance", {
            value: class {
              constructor(public text: string) {}
            },
          });
          Object.defineProperty(window.speechSynthesis, "getVoices", {
            value: () => [
              {
                lang: "zh-CN",
                voiceURI: "test-mandarin",
                localService: true,
                name: "Test Mandarin",
                default: true,
              },
            ],
          });
          Object.defineProperty(window.speechSynthesis, "speak", {
            value: (utterance: SpeechSynthesisUtterance) => {
              document.documentElement.dataset.deviceSpeech = utterance.text;
              utterance.onstart?.(new Event("start") as SpeechSynthesisEvent);
              utterance.onend?.(new Event("end") as SpeechSynthesisEvent);
            },
          });
        });
      await page.goto("/");
      await page
        .getByRole("button", { name: /Start without an account/ })
        .click();
      await page.getByRole("button", { name: "Continue", exact: true }).click();
      await page.getByRole("button", { name: "Continue", exact: true }).click();
      await page.getByRole("checkbox", { name: "Start in quiet mode" }).check();
      await page
        .getByRole("button", { name: "Meet your first characters" })
        .click();
      await page.getByRole("button", { name: "Save and exit" }).click();
      await page
        .locator(".main-nav")
        .getByRole("button", { name: "Read", exact: true })
        .click();
      await page.getByRole("tab", { name: "Readings" }).click();
      await page
        .locator(".reading-row")
        .filter({ has: page.getByText(reading.title, { exact: true }) })
        .filter({
          has: page.getByText(reading.titleZh ?? pack.unit.titleZh, {
            exact: true,
          }),
        })
        .click();
      await expect(page.locator(".reader-purpose")).toHaveText(reading.purpose);
      await expect(page.locator(".line-py")).toHaveCount(0);
      await expect(page.locator(".line-zh")).toHaveCount(reading.lines.length);
      const response = deferred
        ? undefined
        : page.waitForResponse(
            (r) =>
              r.url().includes("/audio-v2/") && r.request().method() === "GET",
          );
      await page
        .getByRole("button", { name: "Read aloud", exact: true })
        .click();
      if (deferred) {
        await expect(page.locator("html")).toHaveAttribute(
          "data-device-speech",
          reading.lines.map((l: { zh: string }) => l.zh).join(""),
        );
        await expect(
          page.getByText("Using your device’s Mandarin voice for this line."),
        ).toBeVisible();
      } else {
        const clip = await response!;
        expect([200, 206]).toContain(clip.status());
        expect(clip.headers()["content-type"]).toMatch(/audio/);
        await expect(
          page.getByText("Using your device’s Mandarin voice for this line."),
        ).toHaveCount(0);
      }
      await page.getByRole("button", { name: "Pinyin", exact: true }).click();
      await expect(page.locator(".line-py")).toHaveCount(reading.lines.length);
    });
  }
}
