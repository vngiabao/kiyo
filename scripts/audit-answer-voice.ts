// How many Chinese answers can Sayo read aloud when tapped (src/answer-voice.ts)?
// Counts distinct answer texts the learner can tap, across every lesson, task and tile.
import { allLessons, exercisesFor } from "../src/content";
import { characterSpeech } from "../src/hanzi";
import { hasSayoClip } from "../src/audio";

const han = /\p{Script=Han}/u;
const plain = (s: string) => s.replace(/[【】]/g, "");
const listening = ["dialogue", "truefalse", "reply", "listenfill", "dictation"];
const asked = new Set<string>();
for (const lesson of allLessons)
  for (const e of exercisesFor(lesson)) {
    if (!e.task) {
      if (listening.includes(e.kind)) continue;
      for (const c of e.choices ?? []) if (han.test(c)) asked.add(c);
      if (e.kind === "reorder") for (const t of e.tokens ?? []) asked.add(t);
      continue;
    }
    const t = e.task as unknown as Record<string, unknown> & { type: string };
    if (t.type === "reply") for (const c of t.choices as string[]) asked.add(c);
    if (t.type === "dialogue") for (const q of (t.questions as { choices: string[] }[]) ?? []) for (const c of q.choices) if (han.test(c)) asked.add(c);
    if (t.type === "cloze") for (const w of t.bank as string[]) asked.add(w);
    if (t.type === "match") for (const p of t.pairs as { right: { zh: string } }[]) asked.add(plain(p.right.zh));
  }
const voiced = [...asked].filter((raw) => {
  const text = Array.from(raw).length === 1 ? characterSpeech(raw) : raw;
  return hasSayoClip(text) || hasSayoClip(raw);
});
const missing = [...asked].filter((x) => !voiced.includes(x));
console.log(`${asked.size} distinct Chinese answers; Sayo reads ${voiced.length} (${((voiced.length / asked.size) * 100).toFixed(1)}%). The rest pop instead.`);
console.log("Examples without a clip:", missing.slice(0, 15).join(" · "));
