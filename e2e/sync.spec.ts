import { test, expect } from "@playwright/test";
import AxeBuilder from "@axe-core/playwright";

// Test-only local transport; no Supabase project or credentials are used.
test("consent, manual sync, deletion, backup and sign-out work at 320px", async ({
  page,
}) => {
  test.skip(
    !!process.env.APP_URL,
    "Uses Vite source modules and an isolated fake cloud.",
  );
  await page.setViewportSize({ width: 320, height: 900 });
  await page.goto("/");
  await page
    .getByRole("button", { name: /Start without an account/ })
    .waitFor();
  // Match Vite's currently loaded module URLs, including any HMR timestamps.
  const source = await (await page.request.get("/src/App.tsx")).text();
  const dbPath = source.match(/from "([^"\n]*\/db\.ts[^"\n]*)"/)![1];
  const syncPath = source.match(/from "([^"\n]*\/sync\.ts[^"\n]*)"/)![1];
  await page.evaluate(
    async ({ dbPath, syncPath }) => {
      const { db, defaultProfile, saveAttempt } = await import(dbPath);
      const sync = await import(syncPath);
      let cloud = {
        revision: 0,
        epoch: "test",
        deleted: false,
        schema_version: 1,
        rows: [] as any[],
      };
      sync.setSyncTransportForTests(() => ({
        pull: async () => structuredClone(cloud),
        push: async (_state: unknown, rows: any[]) => {
          const old = new Map(
            cloud.rows.map((row) => [`${row.kind}:${row.id}`, row]),
          );
          rows.forEach((row) => old.set(`${row.kind}:${row.id}`, row));
          cloud = {
            ...cloud,
            rows: [...old.values()],
            revision: cloud.revision + 1,
            deleted: false,
          };
          return cloud;
        },
        remove: async () =>
          (cloud = {
            ...cloud,
            rows: [],
            deleted: true,
            epoch: "deleted",
            revision: cloud.revision + 1,
          }),
      }));
      await db.profiles.put({
        ...defaultProfile,
        name: "Local learner",
        entry: "guest",
        onboarded: true,
      });
      await saveAttempt({
        phraseId: "hello",
        modality: "listening",
        correct: true,
        answer: "Hello",
        expected: "Hello",
        latencyMs: 1000,
        support: "none",
        context: "browser test",
      });
      await sync.acceptAccount({
        id: "test-account",
        name: "Local learner",
        email: "long-learner-name@example.test",
        provider: "email",
      });
    },
    { dbPath, syncPath },
  );
  await expect(
    page.getByRole("heading", {
      name: "Add this device’s progress to your account?",
    }),
  ).toBeVisible();
  expect((await new AxeBuilder({ page }).analyze()).violations).toEqual([]);
  await page.screenshot({
    path: ".impeccable/review/sync-consent-320.png",
    fullPage: true,
  });
  await page.getByRole("button", { name: "Keep on this device" }).click();
  await page.getByRole("button", { name: "Settings", exact: true }).click();
  await page.getByRole("button", { name: "Enable sync again" }).click();
  await page
    .getByRole("button", { name: "Add progress and enable sync" })
    .click();
  await expect(
    page.getByText("Your progress is synced.", { exact: true }),
  ).toBeVisible();
  await page.getByRole("button", { name: "Sync now", exact: true }).click();
  await expect(
    page.getByText("Your progress is synced.", { exact: true }),
  ).toBeVisible();
  expect(
    await page.evaluate(
      () => document.documentElement.scrollWidth <= innerWidth,
    ),
  ).toBe(true);
  expect((await new AxeBuilder({ page }).analyze()).violations).toEqual([]);
  for (const width of [1440, 768, 375, 320]) {
    await page.setViewportSize({ width, height: 900 });
    await page.evaluate(() => window.scrollTo(0, 0));
    expect(await page.evaluate(() => document.documentElement.scrollWidth <= innerWidth)).toBe(true);
    await page.screenshot({ path: `.impeccable/review/sync-settings-${width}.png`, fullPage: true });
  }
  const download = page.waitForEvent("download");
  await page.getByRole("button", { name: "Export learning record" }).click();
  expect((await download).suggestedFilename()).toContain(".json");
  await page
    .getByRole("button", { name: "Delete my cloud data", exact: true })
    .click();
  await page.getByRole("button", { name: "Confirm cloud deletion" }).click();
  await expect(page.getByText(/Cloud learning data deleted/)).toBeVisible();
  await page.getByRole("button", { name: "Sign out", exact: true }).click();
  await expect(
    page.getByText("Studying without an account", { exact: true }),
  ).toBeVisible();
  expect(
    await page.evaluate(async (path) => {
      const { db } = await import(path);
      return db.attempts.count();
    }, dbPath),
  ).toBe(1);
});

test("all sixteen installed Sayo poses load with no pending placeholders", async ({
  page,
}) => {
  await page.goto("/#companion");
  await expect(page.locator(".mascot-gallery")).toBeVisible();
  for (const pose of [
    "welcome",
    "listen",
    "grumpy",
    "encourage",
    "hint",
    "review",
    "think",
    "error",
    "thumbsup",
    "run",
    "smug",
    "speak",
    "read",
    "write",
    "celebrate",
    "rest",
    "peek",
    "watch",
    "stamp",
  ]) {
    const response = await page.request.get(`/mascot/web/${pose}.webp`);
    expect(response.ok(), pose).toBe(true);
    expect(response.headers()["content-type"]).toContain("image/webp");
  }
  await expect(page.getByText(/Art coming/)).toHaveCount(0);
  await page.screenshot({
    path: ".impeccable/review/sayo-installed-1440.png",
    fullPage: true,
  });
});
