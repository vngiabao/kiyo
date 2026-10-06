import { mkdirSync, readFileSync, writeFileSync } from "node:fs";
import { toneBarPath, wordmarkPaths } from "../src/brand-paths";

mkdirSync("public/brand", { recursive: true });
const letters = wordmarkPaths
  .map((d) => `<path d="${d}" fill="#f0f3f5" fill-rule="evenodd"/>`)
  .join("");
writeFileSync(
  "public/brand/wordmark.svg",
  `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 259 94"><title>Kiyo</title><path d="${toneBarPath}" fill="#86a8ff"/>${letters}</svg>`,
);
// The portrait reuses approved raster art; the lettering is real vector geometry.
const portrait = `data:image/webp;base64,${readFileSync("public/mascot/web/welcome.webp").toString("base64")}`;
writeFileSync(
  "public/brand/app-icon.svg",
  `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100"><title>Kiyo · Sayo</title><defs><clipPath id="tile"><rect width="100" height="100" rx="23"/></clipPath></defs><rect width="100" height="100" rx="23" fill="#b3d2f5"/><image href="${portrait}" x="-33" y="-3" width="166" height="166" clip-path="url(#tile)"/></svg>`,
);
console.log(
  "Exported SVG wordmark and portrait app icon; 清 favicon retained.",
);
