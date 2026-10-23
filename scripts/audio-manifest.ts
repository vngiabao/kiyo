import { mkdirSync } from "node:fs";
import { writeGeneratedText } from "./write-generated-text";
import { createHash } from "node:crypto";
import { phrases, grammarById, packScenarios, usageById } from "../src/content";
import {
  characters,
  readings,
  characterSpeech,
  glossFor,
  isHan,
} from "../src/hanzi";
import { baseScenarios, segments } from "../src/dialogue-data";
import { mascotScenes, moLines, welcomeGreeting } from "../src/sayo-lines";
import {
  hskItems,
  hskSpeech,
  hskStudyWords,
  teacherLines,
} from "../src/hsk-model";
import { lessonTasks, taskAudio } from "../src/tasks";
import { compiledPacks, packs } from "../src/pack-content";
import { wordSpeech } from "../src/word-speech";
import { answerAudioTexts } from "./answer-audio";
import answerPronunciations from "../content/voices/audio-pronunciations.json" with { type: "json" };
import { sayoReactions } from "../src/sayo-reactions";
import {
  dialogueMood,
  reactionMood,
  voiceKey,
  type SayoMood,
} from "../src/sayo-voice";

type Part = { text: string; mood: SayoMood };
type Script = {
  id: string;
  text: string;
  pinyin?: string;
  meaning?: string;
  moods: SayoMood[];
  kinds: string[];
  parts?: Part[];
  dialogue?: boolean;
  delivery?: { pitchOffset: number };
};
export function collectAudioScripts(): Script[] {
  const entries = new Map<string, Script>();
  function add(
    text: string,
    kind: string,
    pinyin?: string,
    meaning?: string,
    moods: SayoMood[] = ["clear", "playful", "cool"],
  ) {
    const key = voiceKey(text);
    if (!key) return;
    const old = entries.get(key);
    if (old) {
      old.moods = [...new Set([...old.moods, ...moods])];
      old.kinds = [...new Set([...old.kinds, kind])];
      old.pinyin ||= pinyin;
      old.meaning ||= meaning;
      return;
    }
    entries.set(key, {
      id: createHash("sha256").update(key).digest("hex").slice(0, 16),
      text,
      pinyin,
      meaning,
      moods,
      kinds: [kind],
    });
  }
  function dialogue(
    lines: {
      text: string;
      pinyin?: string;
      meaning?: string;
      speaker?: string;
    }[],
    full: string,
  ) {
    const speakers = [...new Set(lines.map((l) => l.speaker).filter(Boolean))];
    const parts = lines.map((l) => ({
      text: l.text,
      mood: l.speaker
        ? dialogueMood(speakers.indexOf(l.speaker))
        : ("clear" as SayoMood),
    }));
    lines.forEach((l, i) =>
      add(l.text, "dialogue", l.pinyin, l.meaning, [
        ...new Set<SayoMood>(["clear", "playful", "cool", parts[i].mood]),
      ]),
    );
    add(
      full,
      "reading",
      lines.map((l) => l.pinyin ?? "").join(" "),
      lines.map((l) => l.meaning ?? "").join(" "),
    );
    const entry = entries.get(voiceKey(full))!;
    if (lines.length > 1) {
      entry.parts = parts;
      entry.dialogue = speakers.length > 0;
    }
  }
  phrases.forEach((p) => {
    add(
      p.audio.text,
      "word",
      p.audio.text === p.hanzi ? p.pinyin : undefined,
      p.meaning,
    );
    if (p.example) add(p.example.zh, "example", p.example.py, p.example.en);
  });
  characters.forEach((c) => {
    add(
      c.say,
      "character",
      c.say === c.hanzi ? c.pinyin : undefined,
      c.meaning,
    );
    c.words.forEach((w) => {
      const spoken = wordSpeech(w.w, w.p);
      add(spoken, "word", spoken === w.w ? w.p : undefined, w.m);
    });
  });
  Object.values(grammarById).forEach((g) =>
    g.examples.forEach((e) => add(e.zh, "grammar", e.py, e.en)),
  );
  Object.values(usageById).forEach((p) =>
    add(p.natural.zh, "usage", p.natural.py, p.natural.en),
  );
  readings.forEach((r) =>
    dialogue(
      r.lines.map((l) => ({
        text: l.zh,
        pinyin: l.py,
        meaning: l.en,
        speaker: l.speaker,
      })),
      r.lines.map((l) => l.zh).join(""),
    ),
  );
  // Keep supplementary scenes explicit: compiling a reader must never be a
  // prerequisite for discovering its audio. add() deduplicates shared lines.
  packs.forEach((p) =>
    (p.extraReadings ?? []).forEach((r) => {
      dialogue(
        r.lines.map((l) => ({
          text: l.zh,
          pinyin: l.py,
          meaning: l.en,
          speaker: l.speaker,
        })),
        r.lines.map((l) => l.zh).join(""),
      );
      r.lines.forEach((l) => add(l.zh, "extra-reading", l.py, l.en));
    }),
  );
  readings.forEach((r) =>
    r.lines.forEach((l) =>
      Array.from(l.zh)
        .filter(isHan)
        .forEach((ch) => {
          const text = characterSpeech(ch),
            gloss = glossFor(ch);
          add(
            text,
            "reader-lookup",
            text === ch ? gloss?.p : undefined,
            gloss?.m,
          );
        }),
    ),
  );
  [...baseScenarios, ...packScenarios].forEach((s) =>
    s.turns.forEach((t) => {
      add(t.text, "conversation", t.pinyin, t.meaning);
      t.examples.forEach((e) => add(e, "conversation-answer"));
    }),
  );
  dialogue(segments, segments.map((l) => l.text).join(" "));
  add(
    "你好，很高兴认识你。",
    "preview",
    "Nǐ hǎo, hěn gāoxìng rènshi nǐ.",
    "Hello, nice to meet you.",
  );
  const lines = [
    welcomeGreeting,
    ...mascotScenes.map((s) => s.say),
    ...Object.values(moLines).flat(),
  ];
  lines.forEach((l) => add(l.zh, "reaction", l.py, l.en, [reactionMood(l.zh)]));
  sayoReactions.forEach((l) => {
    add(l.zh, "reaction", l.py, l.en, [l.mood]);
    entries.get(voiceKey(l.zh))!.delivery = { pitchOffset: l.pitchOffset };
  });
  Object.values(teacherLines).forEach((l) =>
    add(l.zh, "reaction", l.py, l.en, [reactionMood(l.zh)]),
  );
  hskItems.forEach((q) => {
    add(q.sentence, "hsk-example", q.py, q.en, ["clear"]);
    // Listening and answer review play the complete sentence. Blank prompts,
    // ordering fragments and other distractors have no playback control.
    hskStudyWords([q]).forEach((c) =>
      add(
        hskSpeech(c.zh),
        "hsk-word",
        hskSpeech(c.zh) === c.zh ? c.py : undefined,
        c.en,
        ["clear"],
      ),
    );
  });
  const allTasks = [
    ...Object.values(lessonTasks).flat(),
    ...compiledPacks.flatMap((p) => p.tasks),
  ];
  for (const task of allTasks) {
    if (task.type === "dialogue") {
      const lines = taskAudio(task).map((line, i) => ({
        text: line.zh,
        pinyin: line.py,
        meaning: line.en,
        speaker: task.lines[i].speaker,
      }));
      dialogue(lines, lines.map((line) => line.text).join(""));
    } else {
      for (const line of taskAudio(task))
        add(
          line.zh,
          `task-${line.role}`,
          line.py || undefined,
          line.en || undefined,
          [line.mood],
        );
    }
  }
  // Answer taps include distractors and word-bank fragments, not only the
  // authored correct answer or full sentence. Keep their coverage build-gated.
  const answerTexts = answerAudioTexts();
  const pronounced = answerPronunciations as Record<string, string>;
  for (const text of Object.keys(pronounced))
    if (!answerTexts.some((answer) => answer.text === text))
      throw new Error(`Unused answer pronunciation: ${text}`);
  for (const { text } of answerTexts)
    add(text, "answer-choice", pronounced[text], undefined, ["clear"]);
  return [...entries.values()];
}
if (process.argv[1]?.replace(/\\/g, "/").endsWith("/audio-manifest.ts")) {
  mkdirSync("content", { recursive: true });
  const scripts = collectAudioScripts();
  writeGeneratedText(
    "content/audio-scripts.json",
    JSON.stringify(scripts, null, 2) + "\n",
  );
  console.log(
    `${scripts.length} texts, ${scripts.reduce((n, s) => n + s.moods.length, 0)} mood clips (including assembled readings).`,
  );
}
