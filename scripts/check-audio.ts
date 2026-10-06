import { readFileSync, existsSync } from "node:fs";
import { createHash } from "node:crypto";
import { voiceKey } from "../src/sayo-voice";
import { lessonTasks, taskAudio } from "../src/tasks";
import { compiledPacks } from "../src/pack-content";
import { collectAudioScripts } from "./audio-manifest";
import { isDeferred } from "./audio-deferred";

const read = (path: string) => JSON.parse(readFileSync(path, "utf8"));
const assets = read("src/audio-assets.json") as Record<
  string,
  Record<string, string>
>;
const index = new Map(
  Object.entries(assets).map(([text, voices]) => [voiceKey(text), voices]),
);
const scripts = collectAudioScripts();
const provenance = read("content/voices/sayo-library-provenance.json") as {
  clips: {
    file: string;
    sha256: string;
    sampleRate: number;
    seconds: number;
  }[];
};
const files = new Map(provenance.clips.map((c) => [c.file, c]));
const issues: string[] = [];
const deferred = new Set<string>();
if (
  JSON.stringify(read("content/audio-scripts.json")) !== JSON.stringify(scripts)
)
  issues.push("Audio manifest is stale. Run npm run audio:manifest.");
// Also validate unused mappings: a bad URL must not hide behind a covered text.
for (const [text, voices] of Object.entries(assets))
  for (const [mood, url] of Object.entries(voices)) {
    if (
      !url.startsWith("/audio-v2/") ||
      !existsSync("public" + url) ||
      !files.has("public" + url)
    )
      issues.push(`Invalid mapping ${text} [${mood}]: ${url}`);
  }
const tasks = [
  ...Object.values(lessonTasks).flat(),
  ...compiledPacks.flatMap((p) => p.tasks),
];
for (const task of tasks)
  for (const line of taskAudio(task)) {
    if (/[【】]/u.test(line.zh))
      issues.push(`Unexpanded gap in task ${task.id}`);
    if (!index.get(voiceKey(line.zh))?.[line.mood]) {
      if (isDeferred(line.zh)) deferred.add(line.zh);
      else issues.push(`Task ${task.id}: missing ${line.mood}: ${line.zh}`);
    }
  }
for (const s of scripts)
  for (const mood of s.moods) {
    const url = index.get(voiceKey(s.text))?.[mood];
    if (!url?.startsWith("/audio-v2/")) {
      if (isDeferred(s.text)) deferred.add(s.text);
      else issues.push(`Missing ${mood}: ${s.text}`);
      continue;
    }
    const file = "public" + url;
    const record = files.get(file);
    if (!record || !existsSync(file)) {
      issues.push(`Missing file/provenance: ${file}`);
      continue;
    }
    if (record.sampleRate !== 24000 || record.seconds <= 0)
      issues.push(`Invalid metadata: ${file}`);
  }
for (const [file, record] of files) {
  if (!existsSync(file)) {
    issues.push(`Missing ${file}`);
    continue;
  }
  const hash = createHash("sha256").update(readFileSync(file)).digest("hex");
  if (hash !== record.sha256) issues.push(`Changed audio: ${file}`);
}
if (issues.length) throw new Error(issues.join("\n"));
if (deferred.size)
  console.warn(
    `⚠ ${deferred.size} texts ship without a Sayo clip by owner decision (content/voices/audio-deferred.json); the device voice reads them.`,
  );
console.log(
  `${scripts.length} texts covered; ${files.size} audio files match their provenance; ${tasks.length} tasks have their requested moods.`,
);
