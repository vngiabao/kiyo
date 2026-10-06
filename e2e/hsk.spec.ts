import { test, expect, type Page } from "@playwright/test";
import AxeBuilder from "@axe-core/playwright";
import { readFileSync } from "node:fs";
import type { HskPracticePack, AnyHskPack } from "../src/hsk-pack";
import type { HskRun } from "../src/hsk-model";
import { mascotScenes } from "../src/sayo-lines";
import { reactionMood } from "../src/sayo-voice";
const audioAssets = JSON.parse(readFileSync("src/audio-assets.json", "utf8"));
const pack: HskPracticePack = JSON.parse(
  readFileSync("content/packs/hsk-reading.hsk.json", "utf8"),
);
const installed: AnyHskPack[] = JSON.parse(readFileSync("src/generated/hsk-practice.json", "utf8"));
const itemById = Object.fromEntries(installed.flatMap((p) => p.items).map((q) => [q.id, q]));
async function savedRun(page: Page): Promise<HskRun> {
  return page.evaluate(async () => new Promise<HskRun>((resolve, reject) => {
    const request = indexedDB.open("kiyo-hsk-v1");
    request.onerror = () => reject(request.error);
    request.onsuccess = () => {
      const db = request.result;
      const rows = db.transaction("runs", "readonly").objectStore("runs").getAll();
      rows.onerror = () => { db.close(); reject(rows.error); };
      rows.onsuccess = () => {
        const pending = rows.result.filter((r) => !r.finishedAt).sort((a, b) => b.startedAt - a.startedAt);
        db.close();
        if (pending[0]) resolve(pending[0]); else reject(new Error("No saved practice run"));
      };
    };
  }));
}
async function answerRun(page: Page, run: HskRun) {
  for (let i = 0; i < run.itemIds.length; i++) {
    await page.locator(`input[type=radio][value=${JSON.stringify(itemById[run.itemIds[i]].answer)}]`).check();
    if (i < run.itemIds.length - 1)
      await page.getByRole("button", { name: "Next question" }).click();
  }
}

test("a restored listening checkpoint hides its transcript and keeps revealed help supported", async ({ page }) => {
  await enter(page);
  const pool = installed.flatMap((p) => p.items.map((q) => ({ ...q, level: p.level })))
    .filter((q) => q.level === 1 && q.unit === "identity");
  const listening = pool.find((q) => q.format === "listening")!;
  expect(listening).toBeTruthy();
  const run: HskRun = {
    id: "restored-listening-checkpoint", schemaVersion: 1, packVersion: 2, level: 1,
    unit: "identity", itemIds: [listening.id, ...pool.filter((q) => q.id !== listening.id).slice(0, 9).map((q) => q.id)],
    seenItemIds: [], answers: {}, startedAt: Date.now(), deadline: null, finishedAt: null,
  };
  await page.evaluate(async (row) => new Promise<void>((resolve, reject) => {
    const request = indexedDB.open("kiyo-hsk-v1");
    request.onerror = () => reject(request.error);
    request.onsuccess = () => {
      const db = request.result, tx = db.transaction("runs", "readwrite");
      tx.objectStore("runs").put(row);
      tx.oncomplete = () => { db.close(); resolve(); };
      tx.onerror = () => { db.close(); reject(tx.error); };
    };
  }), run);
  await page.reload();
  await page.getByRole("button", { name: "Resume practice" }).click();
  await expect(page.getByText(listening.sentence, { exact: true })).toHaveCount(0);
  const audio = page.waitForResponse((r) => r.url().endsWith(audioAssets[listening.sentence].clear) && r.ok());
  await page.getByRole("button", { name: "Play question", exact: true }).click();
  await audio;
  await page.getByRole("button", { name: /Show words and pinyin/ }).click();
  await expect(page.getByText(listening.sentence, { exact: true })).toBeVisible();
  await page.locator(`input[type=radio][value=${JSON.stringify(listening.answer)}]`).check();
  await page.getByRole("button", { name: "Save & leave" }).click();
  await page.reload();
  await page.getByRole("button", { name: "Resume practice" }).click();
  await expect(page.getByText(listening.sentence, { exact: true })).toBeVisible();
  const restored = await savedRun(page);
  expect(restored.answers[listening.id]).toEqual({ value: listening.answer, supported: true });
  expect(restored.seenItemIds).toContain(listening.id);
  for (const width of [1440, 768, 375, 320]) {
    await page.setViewportSize({ width, height: 900 });
    expect(await page.evaluate(() => document.documentElement.scrollWidth <= innerWidth)).toBe(true);
    await page.screenshot({ path: `.impeccable/review/hsk-listening-${width}.png`, fullPage: true });
  }
  expect((await new AxeBuilder({ page }).include(".hsk-exam").withTags(["wcag2a","wcag2aa","wcag21aa"]).analyze()).violations).toEqual([]);
});
async function enter(page: Page) {
  await page.goto("/");
  await page.getByRole("button", { name: /Start without an account/ }).click();
  await page.getByRole("button", { name: "Continue", exact: true }).click();
  await page.getByRole("button", { name: "Continue", exact: true }).click();
  await page.getByRole("checkbox", { name: "Start in quiet mode" }).check();
  await page
    .getByRole("button", { name: "Meet your first characters" })
    .click();
  await page.getByRole("button", { name: "Save and exit" }).click();
  await page.goto("/#hsk");
  await expect(
    page.getByRole("heading", { name: "HSK study room." }),
  ).toBeVisible();
}
test("HSK word buttons name the actual spoken phrase and play corrected clear audio", async ({
  page,
}) => {
  await enter(page);
  await page
    .getByRole("button", { name: "Study the notes", exact: true })
    .click();
  const assets = audioAssets as Record<string, Record<string, string>>;
  for (const [word, spoken] of [
    ["什么", "什么"],
    ["很", "很"],
    ["的", "我的"],
    ["吗", "好吗"],
    ["呢", "你呢"],
    ["了", "好了"],
  ]) {
    const entry = page.locator(".hsk-word-bank > div").filter({
      has: page.locator("dt", { hasText: new RegExp(`^${word}$`) }),
    });
    if (word !== spoken) {
      await expect(entry).toContainText("Neutral tone in a phrase");
      await expect(entry.locator(".pinyin")).toHaveCount(2);
    }
    const response = page.waitForResponse(
      (r) => r.url().endsWith(assets[spoken].clear) && r.ok(),
    );
    await entry
      .getByRole("button", { name: `Hear ${spoken}`, exact: true })
      .click();
    await response;
    await expect(
      entry.getByRole("button", { name: `Hear ${spoken}`, exact: true }),
    ).toBeVisible();
  }
  for (const width of [1440, 768, 375, 320]) {
    await page.setViewportSize({ width, height: 900 });
    expect(
      await page.evaluate(
        () => document.documentElement.scrollWidth <= innerWidth,
      ),
    ).toBe(true);
    await page.evaluate(() => window.scrollTo(0, 0));
    if (width !== 320)
      await page.screenshot({
        path: `.impeccable/review/hsk-audio-words-${width}.png`,
        fullPage: true,
      });
  }
  expect(
    (
      await new AxeBuilder({ page })
        .include(".hsk-study")
        .withTags(["wcag2a", "wcag2aa", "wcag21aa"])
        .analyze()
    ).violations,
  ).toEqual([]);
});
test("HSK prerequisites, supported answers, reload, repair and source isolation", async ({
  page,
}) => {
  await enter(page);
  await expect(
    page.getByRole("button", { name: "Start timed sample", exact: true }),
  ).toBeDisabled();
  await expect(
    page.getByRole("button", { name: "Take checkpoint", exact: true }),
  ).toBeDisabled();
  await page
    .getByRole("button", { name: "Study the notes", exact: true })
    .click();
  await page.getByRole("button", { name: /I’ve studied these/ }).click();
  await page
    .getByRole("button", { name: "Take checkpoint", exact: true })
    .click();
  const run = await savedRun(page);
  await page.getByRole("button", { name: /Show (option pinyin|words and pinyin)/ }).click();
  await answerRun(page, run);
  await expect(
    page.getByText(`${run.itemIds.length} of ${run.itemIds.length} answered · Saved on this device`, { exact: true }),
  ).toBeVisible();
  await page.reload();
  await page.getByRole("button", { name: "Resume practice" }).click();
  await page
    .getByRole("button", { name: `Question ${run.itemIds.length}, answered`, exact: true })
    .click();
  await page
    .getByRole("button", { name: "Submit answers", exact: true })
    .click();
  await expect(
    page.getByRole("heading", { name: "Keep the mistakes. Fix them." }),
  ).toBeVisible();
  await expect(
    page.getByText(`${run.itemIds.length - 1} unaided · 1 supported · 0 unanswered`),
  ).toBeVisible();
  await page.getByRole("button", { name: "Return to the pathway" }).click();
  await expect(page.locator(".hsk-path>li").nth(1)).toContainText("Locked");
  await page.getByRole("button", { name: "Mistakes (1)", exact: true }).click();
  await page.getByRole("button", { name: "Practise these again" }).click();
  await page.locator(`input[type=radio][value=${JSON.stringify(itemById[run.itemIds[0]].answer)}]`).check();
  await page
    .getByRole("button", { name: "Submit answers", exact: true })
    .click();
  await page.getByRole("button", { name: "Return to the pathway" }).click();
  await expect(page.getByText("0 to revisit")).toBeVisible();
  await page.getByRole("button", { name: "Source desk", exact: true }).click();
  await page
    .getByRole("checkbox", { name: /Confirm your exam version/ })
    .check();
  await expect(
    page.getByRole("checkbox", { name: /Finish the textbook pass/ }),
  ).toBeEnabled();
  await page.getByLabel("Exam version", { exact: true }).selectOption("3.0");
  await expect(
    page.getByRole("checkbox", { name: /Confirm your exam version/ }),
  ).not.toBeChecked();
  await expect(
    page.getByRole("checkbox", { name: /Finish the textbook pass/ }),
  ).toBeDisabled();
});
test("HSK fits small screens and has accessible reading controls", async ({
  page,
}) => {
  await enter(page);
  for (const width of [1440, 768, 375, 320]) {
    await page.setViewportSize({ width, height: 900 });
    await page.evaluate(() => window.scrollTo(0, 0));
    if (width <= 375) {
      const action = await page.locator(".hsk-quick-start").boundingBox();
      expect(action!.y + action!.height).toBeLessThan(700);
      await page.screenshot({
        path: `.impeccable/review/hsk-viewport-${width}.png`,
      });
    }
    await expect
      .poll(() =>
        page.evaluate(() => document.documentElement.scrollWidth <= innerWidth),
      )
      .toBe(true);
    if (width !== 320)
      await page.screenshot({
        path: `.impeccable/review/hsk-${width}.png`,
        fullPage: true,
      });
  }
  expect(
    (
      await new AxeBuilder({ page })
        .include(".hsk-home")
        .withTags(["wcag2a", "wcag2aa", "wcag21aa"])
        .analyze()
    ).violations,
  ).toEqual([]);
  await page.getByRole("button", { name: "Source desk", exact: true }).click();
  await page.screenshot({
    path: ".impeccable/review/hsk-sources-320.png",
    fullPage: true,
  });
  expect(
    (
      await new AxeBuilder({ page })
        .include(".hsk-home")
        .withTags(["wcag2a", "wcag2aa", "wcag21aa"])
        .analyze()
    ).violations,
  ).toEqual([]);
});

test("unaided checkpoints unlock a timed sample that survives leaving and expires", async ({
  page,
}) => {
  test.setTimeout(90000);
  await enter(page);
  for (const unit of ["identity", "numbers", "daily"]) {
    await page
      .getByRole("button", { name: "Study the notes", exact: true })
      .click();
    await page.getByRole("button", { name: /I’ve studied these/ }).click();
    await page
      .getByRole("button", { name: "Take checkpoint", exact: true })
      .click();
    const run = await savedRun(page);
    expect(run.unit).toBe(unit);
    await answerRun(page, run);
    await page
      .getByRole("button", { name: "Submit answers", exact: true })
      .click();
    await expect(
      page.getByRole("heading", { name: "Checkpoint cleared." }),
    ).toBeVisible();
    await page.getByRole("button", { name: "Return to the pathway" }).click();
  }
  await expect(
    page.getByText("3 / 3 checkpoints", { exact: true }),
  ).toBeVisible();
  await page.clock.install({ time: new Date() });
  await page
    .getByRole("button", { name: "Start timed sample", exact: true })
    .click();
  await expect(
    page.getByRole("button", { name: /Show option pinyin/ }),
  ).toHaveCount(0);
  await page.screenshot({
    path: ".impeccable/review/hsk-exam-1440.png",
    fullPage: true,
  });
  await page.setViewportSize({ width: 375, height: 812 });
  await page.screenshot({
    path: ".impeccable/review/hsk-exam-375.png",
    fullPage: true,
  });
  expect(
    (
      await new AxeBuilder({ page })
        .include(".hsk-exam")
        .withTags(["wcag2a", "wcag2aa", "wcag21aa"])
        .analyze()
    ).violations,
  ).toEqual([]);
  await page.getByRole("button", { name: "Save & leave", exact: true }).click();
  const sample = await savedRun(page);
  await page.clock.fastForward(sample.deadline! - sample.startedAt + 1000);
  await page.getByRole("button", { name: "Resume practice" }).click();
  await expect(
    page.getByRole("heading", { name: "Keep the mistakes. Fix them." }),
  ).toBeVisible();
  await expect(
    page.getByText(`0 unaided · 0 supported · ${sample.itemIds.length} unanswered`),
  ).toBeVisible();
});

test("installed HSK notebook and new teacher audio work offline", async ({
  page,
  context,
}) => {
  test.skip(!process.env.APP_URL, "Requires the production service worker.");
  await enter(page);
  await page.evaluate(() => navigator.serviceWorker.ready);
  await page.reload();
  await expect(
    page.getByRole("heading", { name: "HSK study room." }),
  ).toBeVisible();
  // Audio is saved on first playback rather than included in the shell precache.
  const firstPlay = page.waitForResponse(
    (r) => r.url().includes("/audio-v2/") && r.ok(),
  );
  await page.locator(".hsk-intro .mo-bubble").click();
  const teacherUrl = (await firstPlay).url();
  await expect.poll(() => page.evaluate(async (url) =>
    Boolean(await caches.match(url)), teacherUrl)).toBe(true);
  await context.setOffline(true);
  await page.reload();
  await expect(
    page.getByRole("heading", { name: "HSK study room." }),
  ).toBeVisible();
  await expect
    .poll(() =>
      page
        .locator(".hsk-intro img")
        .evaluate(
          (img: HTMLImageElement) => img.complete && img.naturalWidth > 0,
        ),
    )
    .toBe(true);
  const played = page.waitForResponse(
    (r) => r.url().includes("/audio-v2/") && r.ok(),
  );
  await page.locator(".hsk-intro .mo-bubble").click();
  await played;
  await page
    .getByRole("button", { name: "Study the notes", exact: true })
    .click();
  await page.getByRole("button", { name: /I’ve studied these/ }).click();
  await page
    .getByRole("button", { name: "Take checkpoint", exact: true })
    .click();
  await expect(page.locator(".masthead")).toBeHidden();
  await expect(page.locator(".tabbar")).toBeHidden();
  await page.locator("input[type=radio]").first().check();
  const run = await savedRun(page);
  await expect(
    page.getByText(`1 of ${run.itemIds.length} answered · Saved on this device`, { exact: true }),
  ).toBeVisible();
  await page.getByRole("button", { name: "Save & leave" }).click();
  await page.reload();
  await page.getByRole("button", { name: "Resume practice" }).click();
  await expect(page.locator("input[type=radio]:checked")).toHaveCount(1);
});

test("all-level roadmap and combined advanced sources stay distinct", async ({
  page,
}) => {
  await enter(page);
  await page.getByText("Full route · HSK 1–9", { exact: true }).click();
  await expect(page.locator(".hsk-roadmap li")).toHaveCount(7);
  await page.screenshot({
    path: ".impeccable/review/hsk-roadmap-expanded.png",
    fullPage: true,
  });
  await page.getByLabel("Target level", { exact: true }).selectOption("6");
  await expect(
    page.getByRole("heading", { name: "HSK 6 · Handle dense material" }),
  ).toBeVisible();
  await page.getByLabel("Target level", { exact: true }).selectOption("7");
  await expect(page.getByLabel("Exam version", { exact: true })).toHaveValue(
    "3.0",
  );
  await expect(page.getByLabel("Exam version", { exact: true })).toBeDisabled();
  await expect(
    page.getByText("Standard Course ends at 6.", { exact: false }).first(),
  ).toBeVisible();
  await page.getByRole("button", { name: "Source desk", exact: true }).click();
  await expect(
    page.getByRole("link", { name: "Open official 7–9 sample (PDF)" }),
  ).toHaveAttribute("href", /level7-9\/HSK7-9.pdf/);
  await expect(
    page.getByText("Some items are omitted", { exact: false }),
  ).toBeVisible();
  await page.setViewportSize({ width: 375, height: 900 });
  await page.screenshot({
    path: ".impeccable/review/hsk-advanced-375.png",
    fullPage: true,
  });
  expect(
    (
      await new AxeBuilder({ page })
        .include(".hsk-home")
        .withTags(["wcag2a", "wcag2aa", "wcag21aa"])
        .analyze()
    ).violations,
  ).toEqual([]);
});

test("all gallery reactions play their revised mood clips through to completion", async ({
  page,
}) => {
  test.setTimeout(90000);
  await page.goto("/#companion");
  for (const scene of mascotScenes) {
    const text = scene.say.zh;
    await page
      .locator(".mascot-pose-grid button")
      .filter({ hasText: text })
      .click();
    const audio = page.waitForResponse(
      (r) => r.url().includes("/audio-v2/") && r.ok(),
    );
    await page
      .getByRole("button", { name: "Hear this line", exact: true })
      .click();
    expect((await audio).url()).toContain(`-${reactionMood(text)}-`);
    await expect(
      page.getByRole("button", { name: "Hear this line", exact: true }),
    ).toBeVisible();
  }
  await page
    .locator(".mascot-pose-grid button")
    .filter({ hasText: "来了？开始吧。" })
    .click();
  for (const width of [1440, 768, 375]) {
    await page.setViewportSize({ width, height: 900 });
    await page.evaluate(() => window.scrollTo(0, 0));
    await page.screenshot({
      path: `.impeccable/review/sayo-cheeky-${width}.png`,
    });
  }
});
