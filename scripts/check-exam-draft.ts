import { readFileSync } from "node:fs";
import { validateHskPack } from "../src/hsk-pack";
const file = process.argv[2];
if (!file) throw new Error("Pass an authored exam pack to validate.");
const words = JSON.parse(readFileSync("content/hsk/levels.json", "utf8")).words;
const pack = JSON.parse(readFileSync(file, "utf8"));
const errors = validateHskPack(pack, words);
if (errors.length) {
  console.error(errors.join("\n"));
  process.exitCode = 1;
} else console.log(`${pack.id}: ${pack.items.length} original items passed the publication validator. Native review remains pending.`);
