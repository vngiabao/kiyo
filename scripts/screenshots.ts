// Visual QA: walks the main screens and saves screenshots at three widths.
// Usage: npm run dev (separately), then `npx tsx scripts/screenshots.ts [url]`.
import { chromium, type Page } from "@playwright/test";
import { mkdirSync } from "node:fs";

const url = process.argv[2] ?? "http://127.0.0.1:5173";
const out = ".impeccable/review";
mkdirSync(out, { recursive: true });
const widths: [string, number, number][] = [
  ["1440", 1440, 900],
  ["768", 768, 1024],
  ["375", 375, 812],
];
const only = process.env.ONLY?.split(",");
const wait = (p: Page, ms = 500) => p.waitForTimeout(ms);
const click = (p: Page, name: string | RegExp) =>
  p.getByRole("button", { name }).first().click();

const browser = await chromium.launch({ channel: "chrome" });
for (const [label, width, height] of widths) {
  if (only && !only.includes(label)) continue;
  const ctx = await browser.newContext({
    viewport: { width, height },
    reducedMotion: "reduce",
    deviceScaleFactor: 1,
  });
  const page = await ctx.newPage();
  const shot = async (name: string, full = true) => {
    await wait(page, 700);
    await page.screenshot({ path: `${out}/${name}-${label}.png`, fullPage: full });
  };
  await page.goto(url);
  await shot("welcome", false);
  await click(page, /Start without an account/);
  await page.getByPlaceholder("Your first name").fill("Alex");
  await shot("onboarding-1");
  await click(page, "Continue");
  await shot("onboarding-2");
  await click(page, "Continue");
  await click(page, /Meet your first characters/);
  await page.locator(".kind-meet").waitFor();
  await shot("lesson-meet", false);
  await click(page, "Continue");
  await click(page, "Continue");
  await click(page, "Continue");
  await page.locator(".kind-glyph").waitFor();
  await page.locator(".choice").nth(1).click();
  await shot("lesson-glyph", false);
  await click(page, "Check");
  await shot("lesson-verdict", false);
  // Walk forward until a "Find" (pick) step, answering whatever comes up.
  for (let i = 0; i < 14; i++) {
    if (await page.locator(".kind-pick").count()) break;
    if (await page.locator(".kind-count").count() && !(await page.locator(".kind-count.shot").count())) {
      await shot("lesson-count", false);
      await page.evaluate(() => document.querySelector(".kind-count")?.classList.add("shot"));
    }
    if (await page.getByRole("button", { name: "Check", exact: true }).count()) {
      await page.locator(".choice").first().click();
      await click(page, "Check");
    }
    await click(page, "Continue");
    await wait(page, 200);
  }
  if (await page.locator(".kind-pick").count()) await shot("lesson-pick", false);
  await click(page, "Save and exit");
  await page.locator(".today").waitFor();
  await shot("today");
  await page.goto(url);
  await wait(page, 600);
  const nav = async (name: string) => {
    await wait(page, 450);
    if (width <= 820) {
      const tab = page.locator(".tabbar").getByRole("button", { name });
      if (await tab.count()) return tab.click();
      await page.locator(".tabbar").getByRole("button", { name: "More" }).click();
      await wait(page, 350);
      return page.locator(".drawer").getByRole("button", { name }).click();
    }
    return page.locator(".main-nav").getByRole("button", { name, exact: true }).click();
  };
  await nav("Read");
  await shot("read-path");
  await page.getByRole("tab", { name: "Readings" }).click();
  await shot("read-texts");
  await page.getByRole("tab", { name: "All characters" }).click();
  await page.locator(".wall-cell").nth(18).click();
  await shot("read-sheet", false);
  await page.keyboard.press("Escape");
  await page.getByRole("tab", { name: "Readings" }).click();
  await page.locator(".reading-row").first().click();
  await page.locator(".rch").nth(2).click();
  await shot("reader", false);
  await click(page, "Back");
  await nav("Listen");
  await shot("listen");
  await nav("Speak");
  await shot("speak");
  await nav("Practice");
  await shot("practice");
  await nav("Media");
  await shot("media");
  await nav("Progress");
  await shot("progress");
  if (width > 820) await page.getByRole("button", { name: "Dictionary" }).click();
  else await nav("Dictionary");
  await page.getByPlaceholder(/Try/).fill("hao");
  await page.locator(".word-list button").first().click();
  await shot("dictionary");
  if (width > 820) await page.getByRole("button", { name: "Settings" }).click();
  else await nav("Settings");
  await shot("settings");
  if (width <= 820) {
    await page.locator(".tabbar").getByRole("button", { name: "More" }).click();
    await shot("drawer", false);
  }
  await ctx.close();
  console.log(`captured ${label}`);
}
await browser.close();
