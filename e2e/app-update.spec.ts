import { test, expect, type Page } from "@playwright/test";
import { createServer } from "node:http";
import { existsSync, readFileSync, statSync } from "node:fs";
import path from "node:path";
import type { AddressInfo } from "node:net";

async function savedName(page: Page) {
  return page.evaluate(() => new Promise<string>((resolve, reject) => {
    const request = indexedDB.open("tingjian-v1");
    request.onerror = () => reject(request.error);
    request.onsuccess = () => {
      const database = request.result;
      const rows = database.transaction("profiles", "readonly").objectStore("profiles").getAll();
      rows.onerror = () => { database.close(); reject(rows.error); };
      rows.onsuccess = () => { database.close(); resolve(rows.result[0]?.name); };
    };
  }));
}

test("installed production shell adopts a release without replacing an active lesson or losing saved audio", async ({ page, context }) => {
  test.skip(!process.env.APP_URL, "Requires the real production worker and built assets.");
  test.setTimeout(180000);
  const root = path.resolve("dist");
  page.on("pageerror", (error) => console.error("Production update fixture page error:", error.message));
  page.on("console", (message) => {
    if (message.type() === "error") console.error("Production update fixture console:", message.text());
  });
  let revision = 1;
  const server = createServer((request, response) => {
    const name = decodeURIComponent(new URL(request.url!, "http://localhost").pathname);
    const file = path.resolve(root, "." + (name === "/" ? "/index.html" : name));
    if (!file.startsWith(root + path.sep) || !existsSync(file) || !statSync(file).isFile()) {
      console.error("Production update fixture: unavailable asset", name);
      response.writeHead(404).end();
      return;
    }
    const mime: Record<string, string> = {
      ".js": "application/javascript", ".html": "text/html", ".css": "text/css",
      ".json": "application/json", ".svg": "image/svg+xml", ".mp3": "audio/mpeg",
      ".png": "image/png", ".webp": "image/webp", ".woff2": "font/woff2",
    };
    response.setHeader("Content-Type", mime[path.extname(file)] ?? "application/octet-stream");
    response.setHeader("Cache-Control", "no-store");
    response.end(name === "/sw.js"
      ? readFileSync(file, "utf8") + `\n// release adoption test ${revision}\n`
      : readFileSync(file));
  });
  await new Promise<void>((resolve) => server.listen(0, "127.0.0.1", resolve));
  const origin = `http://127.0.0.1:${(server.address() as AddressInfo).port}`;
  try {
    await page.goto(origin);
    await page.getByRole("button", { name: /Start without an account/ }).click();
    await page.getByPlaceholder("Your first name").fill("Release Reader");
    await page.getByRole("button", { name: "Continue", exact: true }).click();
    await page.getByRole("radio", { name: /Sound first/ }).click();
    await page.getByRole("button", { name: "Continue", exact: true }).click();
    await page.getByRole("checkbox", { name: "Start in quiet mode" }).check();
    await page.getByRole("button", { name: "Hear your first words" }).click();
    await expect(page.getByRole("heading", { name: "First, just listen." })).toBeVisible();
    await page.evaluate(() => navigator.serviceWorker.ready);
    await page.waitForFunction(() => Boolean(navigator.serviceWorker.controller));
    const catalog = JSON.parse(readFileSync("src/audio-assets.json", "utf8"));
    const clip = catalog["你好"].clear as string;
    await page.evaluate(async (url) => {
      const response = await fetch(url);
      if (!response.ok) throw new Error("Recording did not load");
      await (await caches.open("sayo-audio")).put(url, response);
      (window as any).releaseDocumentMarker = "active lesson";
    }, clip);
    expect(await savedName(page)).toBe("Release Reader");
    revision++;
    await page.evaluate(async () => (await navigator.serviceWorker.getRegistration())!.update());
    await expect(page.getByRole("status").filter({ hasText: "An update is ready." })).toBeVisible({ timeout: 60000 });
    expect(await page.evaluate(() => (window as any).releaseDocumentMarker)).toBe("active lesson");
    await expect(page.getByRole("heading", { name: "First, just listen." })).toBeVisible();
    await page.getByRole("button", { name: "Save and exit", exact: true }).click();
    await page.getByRole("button", { name: "Refresh", exact: true }).click();
    await page.waitForFunction(() => (window as any).releaseDocumentMarker === undefined);
    await expect(page.locator(".main-nav").getByRole("button", { name: "Course library", exact: true })).toBeVisible();
    expect(await savedName(page)).toBe("Release Reader");
    await context.setOffline(true);
    await page.reload();
    await expect(page.locator(".lead")).toBeVisible();
    expect(await savedName(page)).toBe("Release Reader");
    const duration = await page.evaluate(async (url) => {
      const response = await (await caches.open("sayo-audio")).match(url);
      if (!response) throw new Error("Saved recording lost after the update");
      const decoder = new AudioContext();
      try { return (await decoder.decodeAudioData(await response.arrayBuffer())).duration; }
      finally { await decoder.close(); }
    }, clip);
    expect(duration).toBeGreaterThan(0.3);
  } finally {
    await context.setOffline(false);
    server.closeAllConnections();
    await new Promise<void>((resolve, reject) => server.close((error) => error ? reject(error) : resolve()));
  }
});
