// Copies stroke-order data (Make Me a Hanzi via hanzi-writer-data, Arphic Public
// License) for every character used in course content into public/hanzi, so
// stroke animation works offline without a CDN.
import { copyFileSync, existsSync, mkdirSync } from "node:fs";
import { phrases } from "../src/content";
import { characters, readings } from "../src/hanzi";
const text = [
  ...phrases.map((p) => p.hanzi),
  ...characters.map((c) => c.hanzi + c.words.map((w) => w.w).join("")),
  ...readings.flatMap((r) => [r.titleZh, ...r.lines.map((l) => l.zh)]),
  "听读见",
].join("");
const chars = new Set(Array.from(text).filter((c) => /\p{Script=Han}/u.test(c)));
mkdirSync("public/hanzi", { recursive: true });
const missing: string[] = [];
for (const c of chars) {
  const src = `node_modules/hanzi-writer-data/${c}.json`;
  if (existsSync(src)) copyFileSync(src, `public/hanzi/${c}.json`);
  else missing.push(c);
}
copyFileSync("node_modules/hanzi-writer-data/ARPHICPL.TXT", "public/licenses/hanzi-writer-data-ARPHICPL.txt");
console.log(`Copied ${chars.size - missing.length} stroke files.${missing.length ? " Missing: " + missing.join("") : ""}`);
