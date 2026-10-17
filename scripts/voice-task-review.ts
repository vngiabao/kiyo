import { writeFileSync, mkdirSync, readFileSync } from "node:fs";
import { lessonTasks, taskAudio } from "../src/tasks";
import { compiledPacks } from "../src/pack-content";
import { voiceKey } from "../src/sayo-voice";
import { allLessons, exercisesFor } from "../src/content";
import { answerSpeechText } from "../src/answer-text";

const tasks = [
  ...Object.values(lessonTasks).flat(),
  ...compiledPacks.flatMap((p) => p.tasks),
];
const lines = tasks.flatMap((task) =>
  taskAudio(task).map((line) => ({ ...line, taskId: task.id })),
);
const unique = new Map(
  lines.map((line) => [`${voiceKey(line.zh)}:${line.mood}`, line]),
);
const installed = new Map(Object.entries(JSON.parse(readFileSync("src/audio-assets.json", "utf8")))
  .map(([text, voices]) => [voiceKey(text), voices as Record<string, string>]));
function reviewChoice(task: (typeof tasks)[number]) {
  if (task.type !== "dialogue") return undefined;
  for (let question = 0; question < task.questions.length; question++)
    for (const text of task.questions[question].choices) {
      const spoken = answerSpeechText(text);
      const url = spoken && installed.get(voiceKey(spoken))?.clear;
      if (url && text.length <= 12)
        return { question, text, url };
    }
}
const choiceTask = tasks.find(task => reviewChoice(task));
if (!choiceTask) throw new Error("No recorded Mandarin dialogue answer exists for playback review.");
const selected = [
  ...tasks.filter((t) => ["names-d", "rescue-d", "meet-d"].includes(t.id)),
  ...tasks.filter((t) => t.type === "listenfill").slice(0, 5),
  choiceTask,
];
mkdirSync("output/approved-voice-rollout", { recursive: true });
writeFileSync(
  "output/approved-voice-rollout/tasks.json",
  JSON.stringify(
    {
      taskCount: tasks.length,
      distinctTexts: new Set(lines.map((line) => voiceKey(line.zh))).size,
      moodClips: unique.size,
      perMood: Object.fromEntries(
        ["clear", "cool", "playful", "soft"].map((mood) => [
          mood,
          [...unique.values()].filter((line) => line.mood === mood).length,
        ]),
      ),
      allLines: [...unique.values()],
      spotChecks: selected.map((task) => {
        const lesson = allLessons.find((lesson) =>
          exercisesFor(lesson).some(
            (exercise) => exercise.task?.id === task.id,
          ),
        )!;
        return {
          id: task.id,
          type: task.type,
          lessonId: lesson.id,
          lessonTitle: lesson.title,
          libraryAction: `Open ${lesson.packPart ? lesson.packPart === "words" ? "New words" : "Grammar & usage" : lesson.title}`,
          step: exercisesFor(lesson).findIndex(
            (exercise) => exercise.task?.id === task.id,
          ),
          lines: taskAudio(task),
          reviewChoice: reviewChoice(task),
        };
      }),
    },
    null,
    2,
  ) + "\n",
);
