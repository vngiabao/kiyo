// Lines the owner chose to ship without a Sayo clip (content/voices/audio-deferred.json).
// Only exact listed texts and manifest assemblies containing them are deferred.
import { readFileSync } from "node:fs";
import { voiceKey } from "../src/sayo-voice";

const listed: string[] = JSON.parse(readFileSync("content/voices/audio-deferred.json", "utf8")).texts;
type Assembly = { text: string; parts?: { text: string }[] };
export function deferredKeys(texts: string[], scripts: Assembly[]) {
  const keys = new Set(texts.map(voiceKey));
  for (let changed = true; changed;) {
    changed = false;
    for (const script of scripts)
      if (!keys.has(voiceKey(script.text)) && script.parts?.some(p => keys.has(voiceKey(p.text)))) {
        keys.add(voiceKey(script.text));
        changed = true;
      }
  }
  return keys;
}
const keys = deferredKeys(listed, JSON.parse(readFileSync("content/audio-scripts.json", "utf8")));
export const deferredTexts = listed;
export const isDeferred = (text: string) => keys.has(voiceKey(text));
