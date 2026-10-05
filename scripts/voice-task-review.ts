import { writeFileSync, mkdirSync } from "node:fs";
import { lessonTasks, taskAudio } from "../src/tasks";
import { compiledPacks } from "../src/pack-content";
import { voiceKey } from "../src/sayo-voice";
import { lessons, exercisesFor } from "../src/content";

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
const selected = [
  ...tasks.filter((t) => ["names-d", "rescue-d", "meet-d"].includes(t.id)),
  ...tasks.filter((t) => t.type === "listenfill").slice(0, 5),
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
        const lesson = lessons.find((lesson) =>
          exercisesFor(lesson).some(
            (exercise) => exercise.task?.id === task.id,
          ),
        )!;
        return {
          id: task.id,
          type: task.type,
          lessonId: lesson.id,
          lessonTitle: lesson.title,
          step: exercisesFor(lesson).findIndex(
            (exercise) => exercise.task?.id === task.id,
          ),
          lines: taskAudio(task),
        };
      }),
    },
    null,
    2,
  ) + "\n",
);
