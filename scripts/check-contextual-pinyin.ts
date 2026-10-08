import { readFileSync, readdirSync } from "node:fs";
import { checkDePinyin } from "./contextual-de";

const root = process.argv[2] ?? "content/packs";
let checked = 0,
  failures = 0;
function walk(value: unknown, location: string) {
  if (!value || typeof value !== "object") return;
  if (Array.isArray(value)) {
    value.forEach((child, i) => walk(child, `${location}/${i}`));
    return;
  }
  const row = value as Record<string, unknown>;
  const text = ["zh", "text", "sentence", "hanzi"]
    .map((key) => row[key])
    .find((v) => typeof v === "string");
  const py = ["py", "pinyin"]
    .map((key) => row[key])
    .find((v) => typeof v === "string");
  if (
    typeof text === "string" &&
    typeof py === "string" &&
    text.includes("得")
  ) {
    checked++;
    for (const issue of checkDePinyin(text, py)) {
      console.error(`${location}: ${issue}`);
      failures++;
    }
  }
  for (const [key, child] of Object.entries(row))
    walk(child, `${location}/${key}`);
}
for (const file of readdirSync(root).filter(
  (name) => name.endsWith(".json") && !name.startsWith("_"),
))
  walk(JSON.parse(readFileSync(`${root}/${file}`, "utf8")), file);
console.log(
  `Contextual 得: ${checked} fields checked, ${failures} problems. Dictionary approval is separate from sentence tone review.`,
);
if (failures) process.exitCode = 1;
