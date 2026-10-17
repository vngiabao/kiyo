import { allLessons, exercisesFor } from "../src/content";
import { answerSpeechText } from "../src/answer-text";
import { plain } from "../src/tasks";

/** Exact data-say targets exposed by LessonPlayer and TaskView, including distractors. */
export function answerAudioTexts(): { raw: string; text: string }[] {
  const answers = new Set<string>();
  const add = (text: string) => {
    if (answerSpeechText(text)) answers.add(plain(text));
  };
  for (const lesson of allLessons)
    for (const exercise of exercisesFor(lesson)) {
      const task = exercise.task;
      if (!task) {
        if (
          ![
            "dialogue",
            "truefalse",
            "reply",
            "listenfill",
            "dictation",
          ].includes(exercise.kind)
        )
          exercise.choices?.forEach(add);
        if (exercise.kind === "reorder") exercise.tokens?.forEach(add);
      } else if (task.type === "reply") task.choices.forEach(add);
      else if (task.type === "dialogue")
        task.questions.forEach((q) => q.choices.forEach(add));
      else if (task.type === "cloze") task.bank.forEach(add);
      else if (task.type === "match")
        task.pairs.forEach((p) => add(p.right.zh));
    }
  return [...answers].map((raw) => ({ raw, text: answerSpeechText(raw)! }));
}
