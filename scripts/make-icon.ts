// Builds public/icon.svg (app icon + favicon) from the 清 stroke data (stroke 4, the top bar of 青, is the blue tone mark), so the
// icon and the in-app <BrandMark> are the same drawing.
import { writeFileSync } from "node:fs";
import glyph from "hanzi-writer-data/清.json";

const paths = glyph.strokes
  .map((d: string, i: number) => `<path d="${d}" fill="${i === 3 ? "#b3d2f5" : "#f0f3f5"}"/>`)
  .join("");
const svg = `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024"><rect width="1024" height="1024" rx="232" fill="#101b2b"/><g transform="translate(112 112) scale(0.78)"><g transform="scale(1,-1) translate(0,-900)">${paths}</g></g></svg>`;
writeFileSync("public/icon.svg", svg);
console.log(`Wrote public/icon.svg (${svg.length} bytes)`);
