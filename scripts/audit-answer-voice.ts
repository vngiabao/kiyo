// Read installed data directly: the browser's lazy catalogue starts empty in Node.
import { readFileSync, mkdirSync, writeFileSync } from "node:fs";
import { voiceKey } from "../src/sayo-voice";
import { answerAudioTexts } from "./answer-audio";
import { isDeferred } from "./audio-deferred";

const assets = JSON.parse(readFileSync("src/audio-assets.json", "utf8"));
const index = new Map(
  Object.entries(assets).map(([text, voices]) => [voiceKey(text), voices]),
);
const asked = answerAudioTexts();
const missing = asked.filter(({ text }) => !index.has(voiceKey(text)));
console.log(
  `${asked.length} distinct Chinese answers; Sayo reads ${asked.length - missing.length}. ${missing.length} have no installed clip.`,
);
console.log(
  `${missing.filter((x) => isDeferred(x.text)).length} are explicit pronunciation deferrals; ${missing.filter((x) => !isDeferred(x.text)).length} need new recordings.`,
);
console.log(
  "Examples without a clip:",
  missing
    .slice(0, 15)
    .map((x) => x.raw)
    .join(" · "),
);
if (process.argv.includes("--write")) {
  mkdirSync("output/audio-gap-repair", { recursive: true });
  writeFileSync(
    "output/audio-gap-repair/answer-gaps.json",
    JSON.stringify({ total: asked.length, missing }, null, 2) + "\n",
  );
}
