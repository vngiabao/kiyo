# Voice mapping for the new practice tasks (paste into the voice / work chat)

Paste the box into the chat that's building Sayo's voice pack. It explains which new lines need audio, which mood each one gets, and how to add them without touching anything else.

```
NEW CONTENT NEEDS SAYO'S VOICE: practice tasks (HSK-style listening and reading)

WHAT CHANGED (another chat built this; don't edit these files, just read them)
Lessons now teach like a real course: meet the phrases, then hear a short conversation with NO text and answer questions, then mixed practice in HSK formats. New files:
- src/tasks.ts: `lessonTasks` (authored tasks for the 20 phrase lessons) plus a helper, `taskAudio(task)`, that lists every line a task plays or shows, with its mood already decided.
- src/TaskView.tsx: plays them. Conversations play line by line via browserSpeech.speak(zh, { mood }). Everything else plays through AudioButton with mood "clear". "Fill in what you hear" also has a "Slower" button that plays the same clip at rate 0.75 (no separate clip needed; it uses playbackRate with preservesPitch).
- src/packs.ts: compiled packs now expose `tasks` (the unit dialogue as a listening task, plus any pack "tasks").
- src/hanzi.ts: readings gained a `cloze` ("lock it in"). Every cloze line is an existing reading line, so no new audio is needed there.
Until clips exist, these lines fall back to the device voice. With no device voice, conversations show an error, the learner has to tap "Show the words", and the answer counts only as supported. Generating them is what makes unaided listening possible.

THE MOOD MAP (one voice, Sayo; moods only, no male voices)
1. Conversation lines (task.type "dialogue"): each speaker keeps one mood for the whole conversation, by order of first appearance: 1st speaker → cool, 2nd → playful, 3rd → soft (dialogueMood(i) from src/sayo-voice.ts, the same rule your dialogue() helper uses). taskAudio() already returns this per line; use its `mood`.
   Acting: natural conversational pace, as two different people would talk, without caricature. The difference between speakers must still be clear at normal speed, because the learner has no text.
2. True/false audio (truefalse.audio), reply prompts (reply.prompt) and fill-in sentences (listenfill.line): "clear". Exam-announcer clarity: steady pace, full tones, no sighs or laughs. For listenfill, the gapped word must be fully articulated (no swallowed neutral tones that change the answer).
3. Reply choices (reply.choices: short Chinese replies such as 我叫安娜。): "clear". They're shown as text now, but the transcript after checking lets the learner replay them, so voice them.
4. Cloze and match lines (cloze.lines, match pairs): "clear". They appear with a play button after checking.
Blanks are written 【like this】 in the source. ALWAYS voice the full sentence: use plain(zh) from src/tasks.ts (taskAudio already does this). Never voice the brackets or a gap.

HOW TO ADD THEM (in scripts/audio-manifest.ts, which is your file)
  import { lessonTasks, taskAudio } from "../src/tasks";
  import { compiledPacks } from "../src/pack-content";
  const allTasks = [...Object.values(lessonTasks).flat(), ...compiledPacks.flatMap((p) => p.tasks)];
  for (const t of allTasks) {
    if (t.type === "dialogue") {
      const lines = taskAudio(t).map((l, i) => ({ text: l.zh, pinyin: l.py, meaning: l.en, speaker: t.lines[i].speaker }));
      dialogue(lines, lines.map((l) => l.text).join(""));
    } else for (const l of taskAudio(t)) add(l.zh, `task-${l.role}`, l.py || undefined, l.en || undefined, [l.mood]);
  }
Check that your dialogue() helper stores each line with the mood dialogueMood(speakerIndex) and keys it by voiceKey(text), because the app looks clips up as index[voiceKey(text)][mood]. If a line already exists in another mood (common short lines like 你好！ or 再见！), add() merges the mood; don't create a second entry.
Size (measured): 140 tasks, including 19 conversations with 91 lines. That's 155 distinct texts, 90 of which have no audio at all yet. With moods, about 200 clips are needed; some already exist, because common words and phrases are already voiced in "clear".

CHECKS
- npm run audio:manifest, then generate (resume by hash as usual), then npm run audio:check.
- Spot-listen: names-d, rescue-d, meet-d (the conversations) and five listenfill lines. Can you hear the blank word clearly? Do the two speakers sound like different people?
- Unit tests: tests/tasks.test.ts already checks that dialogue speakers get distinct moods and that task audio never contains 【】. Run npm test.
- Add a check to audio:check (or audio-catalog.test.ts) that every taskAudio() line has a clip in its mood.
- Don't edit src/tasks.ts, src/TaskView.tsx, src/LessonPlayer.tsx, src/content.ts or src/night.css. If a line sounds wrong in Chinese (unnatural or a tone error), list it in your report instead of changing it, and I'll fix the content.

REPORT BACK: clips added per mood, any lines you flagged, and audio:check output.
```
