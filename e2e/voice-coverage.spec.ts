import { expect, test } from "@playwright/test";

test("welcome plays bundled Sayo audio without a device fallback", async ({
  page,
}) => {
  await page.goto("/");
  const response = page.waitForResponse(
    (r) => r.url().includes("/audio-v2/") && r.request().method() === "GET",
  );
  await page.getByRole("button", { name: /Hear Sayo: 你好/ }).click();
  const audio = await response;
  expect([200, 206]).toContain(audio.status());
  expect(audio.headers()["content-type"]).toMatch(/audio/);
  await expect(
    page.getByText("Using your device’s Mandarin voice for this line."),
  ).toHaveCount(0);
  await expect(page.getByText("Hear Sayo", { exact: true })).toBeVisible({
    timeout: 10000,
  });
});
