/** Verify the actual built modules, rather than just the encoder in isolation. */
import { readFileSync, readdirSync, statSync } from "node:fs";
import { resolve } from "node:path";
import { pathToFileURL } from "node:url";
import { isDeepStrictEqual } from "node:util";
import assert from "node:assert/strict";

const files = readdirSync("dist/assets");
async function built(prefix: string, expected: unknown) {
  const candidates = files.filter((file) => file.startsWith(prefix + "-") && file.endsWith(".js"));
  assert.equal(candidates.length, 1, `Expected one installed ${prefix} module`);
  const module = await import(pathToFileURL(resolve("dist/assets", candidates[0])).href);
  assert(Object.values(module).some((value) => isDeepStrictEqual(value, expected)),
    `Installed ${prefix} differs from the complete source data`);
}
const course = JSON.parse(readFileSync("src/generated/packs.json", "utf8"));
const audio = JSON.parse(readFileSync("src/audio-assets.json", "utf8"));
await built("course-data", course);
await built("audio-catalog", audio);
const pages = files.filter((file) => /^course-page-\d+-.*\.js$/.test(file));
assert(pages.length > 1, "Course data must be split into installed pages");
const courseBytes = [...pages, ...files.filter((f) => /^course-data-.*\.js$/.test(f))]
  .reduce((total, file) => total + statSync(resolve("dist/assets", file)).size, 0);
const audioBytes = files.filter((f) => /^audio-catalog-.*\.js$/.test(f))
  .reduce((total, file) => total + statSync(resolve("dist/assets", file)).size, 0);
assert(courseBytes < Buffer.byteLength(JSON.stringify(course)) * 0.85,
  "Production course encoding is not reducing the installed data");
assert(audioBytes < Buffer.byteLength(JSON.stringify(audio)) * 0.8,
  "Production audio catalog encoding is not reducing the installed data");
for (const page of pages)
  assert(statSync(resolve("dist/assets", page)).size < 1_500_000,
    `${page} exceeds the bounded course-page budget`);
console.log(`Installed data verified: ${course.length} units and ${Object.keys(audio).length} audio texts unchanged; course ${courseBytes.toLocaleString()} bytes, catalog ${audioBytes.toLocaleString()} bytes.`);
