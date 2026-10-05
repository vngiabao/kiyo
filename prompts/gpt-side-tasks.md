# GPT side tasks for Kiyo (one at a time)

Each box is a separate job for a GPT chat that has this folder open. Every job writes a **report only**; it never edits course content. Claude applies the fixes, so the content gates (`npm run packs`, `npm run validate:content`, `npm run check:pinyin`) keep checking everything.

**Never edit (all jobs):** `content/packs/*.json`, `src/**`, `scripts/build-packs.ts`, `scripts/check-pinyin.ts`, `scripts/validate-content.ts`, `tests/**`, `e2e/**`. The voice pipeline files (`scripts/audio-manifest.ts`, `scripts/generate-audio-cosy.py`, `src/audio-assets.json`, `content/voices/**`) belong to the voice chat.

---

## 1. Native-speaker naturalness review

```
Read content/packs/s1-u01.json … s1-u12.json (the HSK 1 course of a personal Mandarin app; mainland Mandarin, casual social register unless a line says otherwise).
For every Chinese line (vocabulary examples, grammar examples, dialogue, reading, conversation turns, pragmatics, tasks), judge: would a native speaker in mainland China say or write this, in this situation?
Write prompts/review/naturalness.md with one row per problem:
| unit | where (field + line number) | current | problem | suggested fix | confidence (high/medium) |
Only list real problems: unnatural word choice, wrong measure word, wrong register, odd word order, a pragmatics note that is wrong for mainland usage. Don't restyle lines that are already natural. Don't rewrite whole dialogues.
Keep every fix inside HSK 1–2 vocabulary where possible, and say when a fix needs a new word.
Do NOT edit any file except prompts/review/naturalness.md.
```

## 2. Answer-key and distractor audit

```
Read the "tasks", "dialogue.questions" and "reading.questions" / "reading.cloze" in content/packs/s1-u*.json, and src/tasks.ts (lessonTasks) for the 20 base lessons.
For each item, check that exactly ONE choice is defensible:
- reply: could a native speaker reasonably give any distractor as the reply? (e.g. both 好的 and 好啊 fit = ambiguous)
- cloze: could any bank word fit any blank grammatically and meaningfully, other than its answer?
- truefalse: is the statement unambiguously true or false from the audio line alone?
- questions: is the answer stated or clearly implied by the text, and are the distractors clearly wrong?
Write prompts/review/answer-keys.md: | unit/lesson | task id | problem | which choice is also defensible | suggested fix |.
Do NOT edit any file except that report.
```

## 3. Dictionary check for words outside the HSK list

```
scripts/check-pinyin.ts verifies pinyin against the HSK 3.0 word list. Words outside that list (蛋糕, 微信, 字幕, 电视剧, 屏幕, names, glosses) are only checked against the pack's own entries.
Download CC-CEDICT (https://www.mdbg.net/chinese/dictionary?page=cc-cedict; the project's scripts/reference-check.ts shows the URL it uses) and, in a NEW script scripts/cedict-report.ts, compare every vocabulary item and gloss in content/packs/s1-u*.json (hanzi + pinyin + meaning) against it.
Output prompts/review/cedict.md: | unit | word | our pinyin | CC-CEDICT pinyin | our meaning | CC-CEDICT gist | verdict |.
Flag only real mismatches (wrong tone or syllable, wrong sense). Tone sandhi (yí ge, bú shì) and erhua are fine.
Do NOT edit packs or existing scripts; the new script and the report are the only files you create.
```

## 4. Vietnamese meanings

```
Every vocabulary item in content/packs/s1-u*.json has "meaningVi" (the learner is a Vietnamese and English speaker).
Check each one: is it the natural Vietnamese equivalent for THIS sense of the word (not a dictionary list)? Prefer what a Vietnamese learner would recognise immediately; note Sino-Vietnamese cognates where helpful (e.g. 汉字 = chữ Hán).
Write prompts/review/vietnamese.md: | unit | word | current meaningVi | suggested | why |. List only items that should change.
Do NOT edit any file except that report.
```

---

When a report is done, hand it to Claude: "apply prompts/review/<file>.md". Claude makes the changes in the packs and reruns every gate.
