import { test, expect, type Page } from "@playwright/test";
import { readFileSync } from "node:fs";
import AxeBuilder from "@axe-core/playwright";
/** First screen is sign-in; tests study as a guest. */
async function enter(page: Page) {
  const guest = page.getByRole("button", { name: /Start without an account/ });
  await guest.waitFor({ timeout: 4000 }).catch(() => undefined);
  if (await guest.isVisible()) await guest.click();
}

async function onboard(page: Page) {
  await page.goto("/");
  await enter(page);
  await page.getByPlaceholder("Your first name").fill("Alex");
  await page.getByRole("button", { name: "Continue", exact: true }).click();
  await page.getByRole("radio", { name: /Sound first/ }).click();
  await page.getByRole("button", { name: "Continue", exact: true }).click();
  await page.getByRole("checkbox", { name: "Start in quiet mode" }).check();
  await page.getByRole("button", { name: "Hear your first words" }).click();
  await expect(
    page.getByRole("heading", { name: "First, just listen." }),
  ).toBeVisible();
}
/** Navigate by label: masthead on wide screens, tab bar or "More" drawer on phones. */
async function go(page: Page, label: string) {
  const top = page
    .locator(".main-nav")
    .getByRole("button", { name: label, exact: true });
  if (await top.isVisible()) {
    await top.click();
    return;
  }
  const tab = page
    .locator(".tabbar")
    .getByRole("button", { name: label, exact: true });
  if (await tab.isVisible()) return tab.click();
  await page.locator(".tabbar").getByRole("button", { name: "More" }).click();
  await page
    .getByRole("dialog", { name: "Your study desk" })
    .getByRole("button", { name: label, exact: true })
    .click();
  await expect(page.getByRole("dialog", { name: "Your study desk" })).toBeHidden();
}

test("navigation survives refresh and browser back; skip link preserves the screen", async ({
  page,
}) => {
  await onboard(page);
  await page.getByRole("button", { name: "Save and exit" }).click();
  await go(page, "Media");
  await expect(page).toHaveURL(/#media$/);
  await expect(
    page.getByRole("heading", { name: "Watch and sing", exact: true }),
  ).toBeVisible();
  await page.reload();
  await expect(
    page.getByRole("heading", { name: "Watch and sing", exact: true }),
  ).toBeVisible();
  await go(page, "Progress");
  await page.goBack();
  await expect(
    page.getByRole("heading", { name: "Watch and sing", exact: true }),
  ).toBeVisible();
  await page.getByRole("link", { name: "Skip to content" }).focus();
  await page.getByRole("link", { name: "Skip to content" }).press("Enter");
  await expect(page.locator("#main")).toBeFocused();
  await expect(page).toHaveURL(/#media$/);
  await expect(
    page.getByRole("heading", { name: "Watch and sing", exact: true }),
  ).toBeVisible();
});

for (const width of [1440, 768, 375, 320]) {
  test(`course library filters and study-desk navigation work at ${width}px`, async ({ page }) => {
    await page.setViewportSize({ width, height: 900 });
    await onboard(page);
    await page.getByRole("button", { name: "Save and exit" }).click();
    await go(page, "Course library");
    await expect(page.getByRole("heading", { name: "Course library." })).toBeVisible();
    await page.getByLabel("Level", { exact: true }).selectOption("4");
    await page.getByLabel("Find a lesson").fill("new group");
    await expect(page.locator(".library-unit")).toHaveCount(1);
    if (width === 1440) {
      expect((await new AxeBuilder({ page }).include(".course-library").withTags(["wcag2a", "wcag2aa", "wcag21aa"]).analyze()).violations).toEqual([]);
    }
    await page.getByRole("button", { name: "Open New words", exact: true }).click();
    await expect(page.getByRole("button", { name: "Save and exit" })).toBeVisible();
    await page.getByRole("button", { name: "Save and exit" }).click();
    await page.reload();
    await expect(page.getByRole("heading", { name: "Course library." })).toBeVisible();
    await page.getByLabel("Show activities").selectOption("finished");
    await expect(page.getByText("No activities match these filters.", { exact: false })).toBeVisible();
    const trigger = page.locator(width <= 820 ? ".tabbar" : ".masthead-tools").getByRole("button", { name: "More", exact: true });
    await trigger.click();
    const desk = page.getByRole("dialog", { name: "Your study desk" });
    await expect(desk).toBeVisible();
    if (width === 1440) {
      expect((await new AxeBuilder({ page }).include(".study-menu").withTags(["wcag2a", "wcag2aa", "wcag21aa"]).analyze()).violations).toEqual([]);
    }
    await page.keyboard.press("Escape");
    await expect(desk).toBeHidden();
    await expect(trigger).toBeFocused();
    await trigger.click();
    await desk.getByRole("button", { name: "Dictionary", exact: false }).click();
    await expect(page).toHaveURL(/#dictionary$/);
    await expect(desk).toBeHidden();
    await page.goBack();
    await expect(page.getByRole("heading", { name: "Course library." })).toBeVisible();
    expect(await page.evaluate(() => document.documentElement.scrollWidth <= innerWidth)).toBe(true);
  });
}

test("watch captions and saved lines work; changing media clears old captions", async ({
  page,
}) => {
  await onboard(page);
  await page.getByRole("button", { name: "Save and exit" }).click();
  await go(page, "Media");
  const watch = page.locator(".watch");
  const assets = JSON.parse(readFileSync("src/audio-assets.json", "utf8"));
  const clip = readFileSync(`public${assets["你好"].clear}`);
  const media = watch.locator('input[type="file"][accept="video/*,audio/*"]');
  await media.setInputFiles({
    name: "practice.mp3",
    mimeType: "audio/mpeg",
    buffer: clip,
  });
  await watch
    .locator('input[type="file"][accept=".srt,.vtt,.lrc,.txt"]')
    .setInputFiles({
      name: "practice.srt",
      mimeType: "text/plain",
      buffer: Buffer.from("1\n00:00:00,000 --> 00:00:02,000\n你好。\n"),
    });
  await expect(watch.locator(".watch-line.now")).toHaveText("你好。");
  await watch.getByRole("button", { name: "Save line", exact: true }).click();
  await watch
    .getByPlaceholder("What it means, or why you saved it")
    .fill("Greeting");
  await watch
    .getByPlaceholder("What it means, or why you saved it")
    .press("Enter");
  await expect(watch.locator(".watch-saved")).toContainText("你好。");
  await watch.getByRole("button", { name: "End session", exact: true }).click();
  await expect(
    watch.getByRole("heading", { name: "Session finished.", exact: true }),
  ).toBeVisible();
  await media.setInputFiles({
    name: "another.mp3",
    mimeType: "audio/mpeg",
    buffer: clip,
  });
  await expect(watch.locator(".watch-line.now")).toHaveCount(0);
  await expect(
    watch.getByRole("button", { name: "Replay line", exact: true }),
  ).toBeDisabled();
  await page.reload();
  await expect(page.locator(".watch-saved")).toContainText("Greeting");
});
test("characters-first path: meet, read, miss, and look up without pinyin", async ({
  page,
}) => {
  const errors: string[] = [];
  page.on("pageerror", (e) => errors.push(e.message));
  await page.goto("/");
  await enter(page);
  await page.getByRole("button", { name: "Continue", exact: true }).click();
  await expect(
    page.getByRole("radio", { name: /Characters first/ }),
  ).toHaveAttribute("aria-checked", "true");
  await page.getByRole("button", { name: "Continue", exact: true }).click();
  await page
    .getByRole("button", { name: "Meet your first characters" })
    .click();
  // Lesson 1 is counting; every new character arrives with its pinyin.
  await expect(page.locator(".anatomy-meaning")).toHaveText("one");
  await expect(page.locator(".anatomy-pinyin")).toHaveText("yī");
  // Meaning checks come two characters later, read from memory.
  for (let i = 0; i < 3; i++)
    await page.getByRole("button", { name: "Continue", exact: true }).click();
  await expect(page.locator(".big-glyph")).toHaveText("一");
  await page.locator(".choice").filter({ hasText: "two" }).click();
  await page.getByRole("button", { name: "Check", exact: true }).click();
  await expect(page.locator(".verdict")).toContainText("“one”");
  await page.getByRole("button", { name: "Save and exit" }).click();
  await go(page, "Read");
  await page.getByRole("tab", { name: "Readings" }).click();
  await page.locator(".reading-row").first().click();
  await expect(page.locator(".line-py")).toHaveCount(0);
  await page.locator(".rch", { hasText: "马" }).first().click();
  await expect(page.locator(".gloss")).toContainText("horse");
  expect(errors).toEqual([]);
});
test("onboarding, fallback, answer persistence, resume, search and backup", async ({
  page,
}) => {
  const errors: string[] = [];
  page.on("pageerror", (e) => errors.push(e.message));
  await onboard(page);
  await page.getByRole("button", { name: "Show the words" }).click();
  await page.getByRole("button", { name: "Continue", exact: true }).click();
  await expect(
    page.getByRole("heading", { name: "Connect the sound to meaning." }),
  ).toBeVisible();
  await page.getByRole("button", { name: "Continue", exact: true }).click();
  // The second phrase is introduced before the first is checked.
  await page.getByRole("button", { name: "Show the words" }).click();
  await page.getByRole("button", { name: "Continue", exact: true }).click();
  await page.getByRole("button", { name: "Continue", exact: true }).click();
  await page.getByRole("button", { name: "Show the words" }).click();
  await page.locator(".choice").filter({ hasText: "Thank you" }).click();
  await page.getByRole("button", { name: "Check", exact: true }).click();
  await expect(page.getByText("Not quite.")).toBeVisible();
  await page.getByRole("button", { name: "Continue", exact: true }).click();
  await page.getByRole("button", { name: "Save and exit" }).click();
  await expect(
    page.getByRole("heading", { level: 1, name: /Alex\./ }),
  ).toBeVisible();
  await page.reload();
  await expect(
    page.getByRole("heading", { level: 1, name: /Alex\./ }),
  ).toBeVisible();
  await page.locator(".lead").getByRole("button", { name: "Continue" }).click();
  await expect(page.getByText("6 / 22", { exact: true })).toBeVisible();
  await page.getByRole("button", { name: "Save and exit" }).click();
  await page.getByRole("button", { name: "Dictionary", exact: true }).click();
  await page.getByPlaceholder("Try 你好, ni hao, or hello…").fill("xiexie");
  await page
    .locator(".word-list button", { hasText: "Thank you" })
    .first()
    .click();
  await expect(page.locator(".word-detail")).toContainText("Thank you");
  await page.getByRole("button", { name: "Settings", exact: true }).click();
  const download = page.waitForEvent("download");
  await page.getByRole("button", { name: "Export learning record" }).click();
  expect((await download).suggestedFilename()).toContain("tingjian-backup");
  expect(errors).toEqual([]);
});
test("guided conversation completes and records practice without speech scoring", async ({
  page,
}) => {
  await onboard(page);
  await page.getByRole("button", { name: "Save and exit" }).click();
  await go(page, "Speak");
  await page.getByRole("button", { name: "Begin conversation" }).click();
  for (const [i, reply] of [
    "你好",
    "我叫安娜",
    "我在学中文",
    "好啊",
  ].entries()) {
    await expect(page.locator(".turn-count")).toHaveText(`${i + 1} / 4`);
    await page.getByRole("textbox").fill(reply);
    await page.getByRole("button", { name: "Reply", exact: true }).click();
  }
  await expect(
    page.getByRole("heading", { name: "You kept it going." }),
  ).toBeVisible();
  await go(page, "Progress");
  await expect(
    page.getByText("1 completed study sessions · 4 saved attempts"),
  ).toBeVisible();
});
test("media support does not masquerade as unaided listening", async ({
  page,
}) => {
  await onboard(page);
  await page.getByRole("button", { name: "Save and exit" }).click();
  await go(page, "Media");
  await page.getByRole("button", { name: "Reveal transcript" }).click();
  await page
    .getByRole("button", { name: "Making a plan to meet", exact: true })
    .click();
  await page.getByRole("button", { name: "Hide transcript" }).click();
  await page.getByRole("button", { name: "Check understanding" }).click();
  await expect(
    page.getByText("Saved as supported practice.", { exact: false }),
  ).toBeVisible();
  await go(page, "Progress");
  await expect(
    page.locator(".capability-row").filter({ hasText: "Media listening" }),
  ).toContainText("Not measured yet");
});
test("all primary surfaces fit mobile, tablet and desktop; capture visual evidence", async ({
  page,
}) => {
  test.setTimeout(150000);
  await page.goto("/");
  await enter(page);
  await page.screenshot({
    path: ".impeccable/review/onboarding-desktop.png",
    fullPage: true,
  });
  await onboard(page);
  await page.screenshot({
    path: ".impeccable/review/lesson-desktop.png",
    fullPage: true,
  });
  await page.getByRole("button", { name: "Save and exit" }).click();
  for (const width of [1440, 768, 375, 320, 414]) {
    await page.setViewportSize({ width, height: 1000 });
    for (const label of [
      "Today",
      "Read",
      "Listen",
      "Practice",
      "Speak",
      "Media",
      "Progress",
    ]) {
      await go(page, label);
      await page.locator("main h1").waitFor();
      await page.evaluate(() => document.fonts.ready);
      await page.mouse.move(0, 0);
      expect(
        await page.evaluate(
          () => document.documentElement.scrollWidth <= innerWidth,
        ),
        `${label} at ${width}`,
      ).toBe(true);
      if ([1440, 768, 375].includes(width))
        await page.screenshot({
          path: `.impeccable/review/${label.toLowerCase().replace(" ", "-")}-${width}.png`,
          fullPage: true,
        });
    }
  }
});
