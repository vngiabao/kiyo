// Export the approved art; trim margins and the icon's stray exterior pixels.
import { mkdirSync, readFileSync, writeFileSync } from "node:fs";
import { createHash } from "node:crypto";
import { chromium } from "@playwright/test";

const digest = (bytes: Uint8Array) =>
  createHash("sha256").update(bytes).digest("hex");
const browser = await chromium.launch({ channel: "chrome" });
const exports: Record<
  string,
  { src: string; width: number; height: number; sha256: string }
> = {};
mkdirSync("public/brand", { recursive: true });
try {
  for (const [name, sizes] of [
    ["website", [null]],
    ["app-icon", [32, 180, 192, 512]],
  ] as const) {
    const source = readFileSync(`content/branding/${name}-approved.png`);
    const page = await browser.newPage();
    for (const size of sizes) {
      const rendered = await page.evaluate(
        async ({ image, size }) => {
          const img = new Image();
          img.src = image;
          await img.decode();
          const source = document.createElement("canvas");
          source.width = img.naturalWidth;
          source.height = img.naturalHeight;
          const context = source.getContext("2d")!;
          context.drawImage(img, 0, 0);
          const pixels = context.getImageData(
            0,
            0,
            source.width,
            source.height,
          ).data;
          let left = source.width,
            top = source.height,
            right = -1,
            bottom = -1;
          for (let y = 0; y < source.height; y++)
            for (let x = 0; x < source.width; x++) {
              if (pixels[(y * source.width + x) * 4 + 3] > 0) {
                left = Math.min(left, x);
                right = Math.max(right, x);
                top = Math.min(top, y);
                bottom = Math.max(bottom, y);
              }
            }
          if (right < left) throw new Error("Approved branding image is empty");
          if (size) {
            // Bounds of the approved pale-blue tile, excluding exterior speckles.
            left = 53;
            top = 59;
            right = 1199;
            bottom = 1199;
          }
          const width = right - left + 1,
            height = bottom - top + 1;
          const canvas = document.createElement("canvas");
          canvas.width = size ?? width;
          canvas.height = size ?? height;
          const output = canvas.getContext("2d")!;
          output.imageSmoothingQuality = "high";
          if (size) {
            output.beginPath();
            output.roundRect(0, 0, size, size, size * 0.205);
            output.clip();
            // Centre within a square without stretching or cutting off the wave.
            const scale = size / Math.max(width, height);
            output.drawImage(
              source,
              left,
              top,
              width,
              height,
              (size - width * scale) / 2,
              (size - height * scale) / 2,
              width * scale,
              height * scale,
            );
          } else
            output.drawImage(
              source,
              left,
              top,
              width,
              height,
              0,
              0,
              width,
              height,
            );
          return {
            data: canvas.toDataURL("image/png").split(",")[1],
            width: canvas.width,
            height: canvas.height,
          };
        },
        { image: `data:image/png;base64,${source.toString("base64")}`, size },
      );
      const bytes = Buffer.from(rendered.data, "base64");
      const sha256 = digest(bytes);
      const filename = `${name}-${sha256.slice(0, 12)}${size ? `-${size}` : ""}.png`;
      writeFileSync(`public/brand/${filename}`, bytes);
      exports[size ? `icon${size}` : "signature"] = {
        src: `/brand/${filename}`,
        width: rendered.width,
        height: rendered.height,
        sha256,
      };
    }
    await page.close();
  }
} finally {
  await browser.close();
}
writeFileSync("src/brand-assets.json", JSON.stringify(exports, null, 2) + "\n");
const html = readFileSync("index.html", "utf8")
  .replace(/\/brand\/app-icon-[a-f0-9]+-32\.png/g, exports.icon32.src)
  .replace(/\/brand\/app-icon-[a-f0-9]+-180\.png/g, exports.icon180.src);
writeFileSync("index.html", html);
console.log("Exported approved website signature and waving app icons.");
