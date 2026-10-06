// Render the approved SVG tile into the PNG sizes required by installed apps.
import { readFileSync } from "node:fs";
import { chromium } from "@playwright/test";

const svg = readFileSync("public/brand/app-icon.svg").toString("base64");
const browser = await chromium.launch({ channel: "chrome" });
try {
  for (const size of [180, 192, 512]) {
    const page = await browser.newPage({
      viewport: { width: size, height: size },
    });
    await page.setContent(
      `<html><body style="margin:0;background:transparent"><img width="${size}" height="${size}" src="data:image/svg+xml;base64,${svg}"></body></html>`,
    );
    await page.locator("img").evaluate((img: HTMLImageElement) => img.decode());
    await page.screenshot({
      path: `public/brand/app-icon-${size}.png`,
      omitBackground: true,
    });
    await page.close();
  }
} finally {
  await browser.close();
}
console.log("Rendered approved waving tile at 180, 192 and 512 px.");
