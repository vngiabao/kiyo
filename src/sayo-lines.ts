/** A short line Sayo says: Chinese first, pinyin under it, English last. */
export type MoLine = { zh: string; py: string; en: string };
const line = (zh: string, py: string, en: string): MoLine => ({ zh, py, en });

/**
 * Sayo 小夜 — a cool, exacting mentor. She is brief, never gushes, never
 * shames. Every line is real, useful Mandarin, so her reactions teach too.
 * Each pose uses its own artwork, preserving the approved character design.
 */
export const mascotScenes = [
  {
    id: "teacher",
    name: "Exam tutor",
    say: line("认真一点。开始吧。", "Rènzhēn yìdiǎn. Kāishǐ ba.", "Focus. Let’s begin."),
    use: "HSK study, reading checkpoints and exam preparation.",
  },
  {
    id: "welcome",
    name: "Welcome",
    say: line(
      "来了？开始吧。",
      "Lái le? Kāishǐ ba.",
      "You’re here? Let’s begin.",
    ),
    use: "Today and returning to study.",
  },
  {
    id: "listen",
    name: "Listen",
    say: line("再听一遍。", "Zài tīng yí biàn.", "Listen once more."),
    use: "Listening lessons, audio playback and Media.",
  },
  {
    id: "speak",
    name: "Speak",
    say: line("大声说。", "Dàshēng shuō.", "Say it out loud."),
    use: "Speaking practice and recording.",
  },
  {
    id: "read",
    name: "Read",
    say: line("看清楚。", "Kàn qīngchu.", "Look closely."),
    use: "Meeting a new character and reading texts.",
  },
  {
    id: "write",
    name: "Write",
    say: line("一笔一笔来。", "Yì bǐ yì bǐ lái.", "One stroke at a time."),
    use: "Optional tracing. The notebook never shows an answer.",
  },
  {
    id: "think",
    name: "Think",
    say: line("想一想。", "Xiǎng yi xiǎng.", "Think it through."),
    use: "Recall and loading a saved lesson.",
  },
  {
    id: "hint",
    name: "Hint",
    say: line(
      "下次不看提示。",
      "Xià cì bú kàn tíshì.",
      "Next time, no peeking.",
    ),
    use: "Correct with pinyin or a transcript revealed.",
  },
  {
    id: "celebrate",
    name: "Celebrate",
    say: line("太棒了！", "Tài bàng le!", "Fantastic!"),
    use: "Correct, unaided answers and finished lessons.",
  },
  {
    id: "smug",
    name: "Not bad",
    say: line("不错嘛。", "Bú cuò ma.", "Not bad at all."),
    use: "A streak of correct answers; her highest praise.",
  },
  {
    id: "encourage",
    name: "Again",
    say: line("再来。", "Zài lái.", "Again."),
    use: "A missed answer. Calm, never punishing.",
  },
  {
    id: "grumpy",
    name: "The tone?",
    say: line("声调呢？", "Shēngdiào ne?", "And the tone?"),
    use: "A missed tone or sound contrast.",
  },
  {
    id: "review",
    name: "Remember",
    say: line("还记得吗？", "Hái jìde ma?", "Still remember?"),
    use: "Reviews that are due.",
  },
  {
    id: "rest",
    name: "Rest",
    say: line("今天够了。", "Jīntiān gòu le.", "That’s enough for today."),
    use: "An empty review queue.",
  },
  {
    id: "error",
    name: "Reconnect",
    say: line("又断了。", "Yòu duàn le.", "Cut off again."),
    use: "Audio, recording, storage and connection errors.",
  },
  {
    id: "thumbsup",
    name: "Level up",
    say: line("升级了！", "Shēngjí le!", "Level up!"),
    use: "Finishing a lesson for the first time.",
  },
  {
    id: "run",
    name: "Keep going",
    say: line("天天来。", "Tiāntiān lái.", "Come back every day."),
    use: "Your days-in-a-row count.",
  },
] as const;
export type MascotState = (typeof mascotScenes)[number]["id"];
export const sceneById = Object.fromEntries(
  mascotScenes.map((s) => [s.id, s]),
) as Record<MascotState, (typeof mascotScenes)[number]>;

/** Rotating lines, picked deterministically so a step never changes its mind. */
export const moLines = {
  right: [
    line("太棒了！", "Tài bàng le!", "Fantastic!"),
    line("对了。", "Duì le.", "That’s right."),
    line("很好。", "Hěn hǎo.", "Very good."),
    line("漂亮！", "Piàoliang!", "Nicely done!"),
  ],
  cool: line("不错嘛。", "Bú cuò ma.", "Not bad at all."),
  supported: line(
    "下次不看提示。",
    "Xià cì bú kàn tíshì.",
    "Next time, no peeking.",
  ),
  wrong: [
    line("再来。", "Zài lái.", "Again."),
    line("差一点。", "Chà yìdiǎn.", "So close."),
    line(
      "没关系，再试试。",
      "Méi guānxi, zài shìshi.",
      "No problem. Try again.",
    ),
  ],
  tone: line("声调呢？", "Shēngdiào ne?", "And the tone?"),
  start: line("从这儿开始。", "Cóng zhèr kāishǐ.", "Start here."),
  levelUp: line("升级了！", "Shēngjí le!", "Level up!"),
  done: line("今天学得不错。", "Jīntiān xué de bú cuò.", "Good work today."),
};
export const pickLine = (lines: readonly MoLine[], seed: string) => {
  let h = 0;
  for (const ch of seed) h = (h * 31 + ch.charCodeAt(0)) >>> 0;
  return lines[h % lines.length];
};
