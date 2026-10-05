import { test, expect } from "@playwright/test";

test("Sayo's selected mood persists and applies to word taps", async ({ page }) => {
  await page.addInitScript(() => {
    const clips: string[] = [];
    Object.assign(window, { playedClips: clips });
    HTMLMediaElement.prototype.play = function () {
      clips.push(this.src);
      this.dispatchEvent(new Event("playing"));
      return Promise.resolve();
    };
  });
  const lastClip = () => page.evaluate(() => (window as unknown as { playedClips: string[] }).playedClips.at(-1));
  await page.goto("/");
  await page.getByRole("button", { name: /Start without an account/ }).click();
  await page.getByRole("button", { name: "Continue", exact: true }).click();
  await page.getByRole("button", { name: "Continue", exact: true }).click();
  await page.getByRole("checkbox", { name: "Start in quiet mode" }).check();
  await page.getByRole("button", { name: "Meet your first characters" }).click();
  await page.getByRole("button", { name: "Save and exit" }).click();
  await page.getByRole("button", { name: "Settings", exact: true }).first().click();
  await expect(page.getByLabel("Sayo’s voice")).toHaveValue("local:clear");
  await page.getByLabel("Sayo’s voice").selectOption("local:playful");
  await page.getByRole("button", { name: "Preview voice" }).click();
  await expect.poll(lastClip).toContain("-playful-");
  await page.reload();
  await page.getByRole("button", { name: "Settings", exact: true }).first().click();
  await expect(page.getByLabel("Sayo’s voice")).toHaveValue("local:playful");
  await page.getByRole("button", { name: "Dictionary", exact: true }).first().click();
  await page.getByPlaceholder("Try 你好, ni hao, or hello…").fill("你好");
  await page.locator(".word-list button").first().click();
  await expect.poll(lastClip).toContain("-playful-");
  expect(await lastClip()).toContain("/audio-v2/");
});

for (const quiet of [false, true]) {
  test(`word taps and Sayo feedback, quiet mode ${quiet}`, async ({ page }) => {
    await page.addInitScript(() => {
      const clips: string[] = [];
      Object.assign(window, { playedClips: clips });
      HTMLMediaElement.prototype.play = function () {
        clips.push(this.src);
        this.dispatchEvent(new Event("playing"));
        return Promise.resolve();
      };
    });
    const played = () => page.evaluate(() => (window as unknown as { playedClips: string[] }).playedClips);
    await page.goto("/");
    await page.getByRole("button", { name: /Start without an account/ }).click();
    await page.getByRole("button", { name: "Continue", exact: true }).click();
    await page.getByRole("button", { name: "Continue", exact: true }).click();
    if (quiet) await page.getByRole("checkbox", { name: "Start in quiet mode" }).check();
    await page.getByRole("button", { name: "Meet your first characters" }).click();
    await page.getByRole("button", { name: "Hear 一", exact: true }).click();
    await expect.poll(async () => (await played()).length).toBe(1);
    for (let i = 0; i < 3; i++) await page.getByRole("button", { name: "Continue", exact: true }).click();
    await page.getByRole("button", { name: "Hear 一", exact: true }).focus();
    await page.keyboard.press("Enter");
    await expect(page.locator(".glyph-pinyin")).toHaveText("yī");
    await expect.poll(async () => (await played()).length).toBe(2);
    await page.locator(".choice").filter({ hasText: /^\d*\s*one$/ }).click();
    await page.getByRole("button", { name: "Check", exact: true }).click();
    await expect(page.locator(".lesson-mo")).toContainText("Next time, no peeking.");
    if (quiet) {
      await page.waitForTimeout(250);
      expect((await played()).length).toBe(2);
    } else {
      await expect.poll(async () => (await played()).length).toBe(3);
      expect((await played()).at(-1)).toContain("/audio-v2/");
      expect((await played()).at(-1)).toContain("-deadpan-");
      await page.getByRole("button", { name: "Stop Sayo’s voice" }).click();
    }
    await page.getByRole("button", { name: /Hear Sayo:/ }).click();
    await expect.poll(async () => (await played()).length).toBe(quiet ? 3 : 4);
    await page.getByRole("button", { name: "Save and exit" }).click();
    await page.getByRole("button", { name: "Dictionary", exact: true }).first().click();
    await page.getByPlaceholder("Try 你好, ni hao, or hello…").fill("你好");
    await page.locator(".word-list button").first().click();
    await expect.poll(async () => (await played()).length).toBe(quiet ? 4 : 5);
  });
}
