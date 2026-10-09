import { chromium } from "@playwright/test";
import { mkdirSync } from "node:fs";
mkdirSync(".impeccable/navigation", { recursive: true });
const browser = await chromium.launch({ channel: "chrome" });
try {
  for (const width of [1440, 768, 375, 320]) {
    const context = await browser.newContext({ viewport: { width, height: 1000 }, reducedMotion: "reduce" });
    const page = await context.newPage();
    await page.goto("http://127.0.0.1:5173/");
    await page.getByRole("button", { name: /Start without an account/ }).click();
    await page.getByRole("button", { name: "Continue", exact: true }).click();
    await page.getByRole("button", { name: "Continue", exact: true }).click();
    await page.getByRole("checkbox", { name: "Start in quiet mode" }).check();
    await page.getByRole("button", { name: "Meet your first characters" }).click();
    await page.getByRole("button", { name: "Save and exit" }).click();
    await page.goto("http://127.0.0.1:5173/#library");
    await page.getByRole("heading", { name: "Course library." }).waitFor();
    await page.getByLabel("Level", { exact: true }).selectOption("4");
    await page.locator(".library-unit summary").first().click();
    await page.evaluate(() => document.fonts.ready);
    await page.screenshot({ path: `.impeccable/navigation/library-${width}.png` });
    await page.locator(width <= 820 ? ".tabbar" : ".masthead-tools").getByRole("button", { name: "More", exact: true }).click();
    await page.getByRole("dialog", { name: "Your study desk" }).waitFor();
    await page.screenshot({ path: `.impeccable/navigation/more-${width}.png` });
    await context.close();
  }
} finally { await browser.close(); }
