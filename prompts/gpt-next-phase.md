# GPT work scope: HSK 1–3 course research and content

Owner agreed on 5 October 2026: Claude owns Projects A and B (dictionary and timed reading drill); GPT owns Project C (course research, packs and Sayo audio). The 96-unit plan is approved and intermediate review stops are revoked. Preserve shared formats and complete four-unit batches with every required gate before proceeding.

```
NEXT PHASE FOR KIYO (Mandarin app, folder Language Learning/Chinese). Read this whole brief before doing anything.

0) CONTEXT YOU MUST KNOW
Learner: one adult (me), English + Vietnamese speaker, studying daily for years. Goals, in priority order:
  1. Socialising and conversation with Chinese speakers (mainland Mandarin).
  2. Reading burned-in Chinese subtitles in dramas at full speed.
  3. Singing along to Chinese songs from hanzi lyrics (not pinyin, not romanisation).
  4. HSK alongside: HSK 3 is the first real milestone, HSK 4 the comfortable one, HSK 5 for most dramas.
Current state (verify by reading the code; don't trust this summary blindly):
  - 20 base phrase lessons + 8 character lessons + 12 HSK 1 units (content/packs/s1-u01…s1-u12.json). C1 audit: 189 of GF2021 level 1's 500 vocabulary entries introduced, including standalone words taught in character lessons. The imported lookup's 506 surface forms are not 506 official entries.
  - Lessons teach like a course: introduce → delayed check → listening conversation (no text until answered) → HSK-format tasks (src/tasks.ts formats: dialogue, truefalse, reply, listenfill, cloze, match; rendered by src/TaskView.tsx).
  - Media tab = Watch & sing (src/Watch.tsx, src/captions.ts): own video/song + .srt/.vtt/.lrc, three rungs (subtitles → peek → none), counted peeks/look-ups, saved lines, Anki export, six-stage route. Tap-to-look-up only knows course characters (glossFor in src/hanzi.ts) and shows "Not in your course yet" for everything else. That is gap A.
  - Audio: Sayo, one voice with moods (src/sayo-voice.ts). Clips are cached on first play (cache "sayo-audio", vite.config.ts); Settings → "Save all audio for offline" (src/offline.ts).
  - Data: Dexie DB "tingjian-v1", currently version 3. Backups: exportRecord/importRecord in src/db.ts.
Read first: AGENTS.md, DESIGN.md (Night Study v2), PEDAGOGY.md, prompts/content-prompt.md, ../SHARED-SPEC.md, src/packs.ts (validatePack), scripts/build-packs.ts, scripts/check-pinyin.ts, scripts/validate-content.ts, src/content.ts (exercisesFor, packExercisesFor, reviewTaskFor), src/Watch.tsx, src/captions.ts, src/hanzi.ts (glossFor), src/db.ts, THIRD_PARTY_NOTICES.md.

1) NON-NEGOTIABLE RULES
- Never rename the database "tingjian-v1" or any storage key. Schema changes are additive Dexie versions only (next is version 4). Every new table must be included in exportRecord/importRecord. Old backups without the table must still import.
- Honest evidence: only unaided answers count as unaided. Pinyin shown, look-ups, peeks, slowed playback and transcripts are support, and are recorded as such. No invented scores, no "readiness %", no pass predictions.
- Content is data: curriculum goes into content/packs/*.json through the gates, never hand-written into content.ts. Every unit's notes say "AI-assisted draft" until a native speaker has reviewed it.
- Copyright: never put copyrighted song lyrics, film scripts or subtitles into the app or content packs. In-app songs and drama scenes must be ORIGINAL. My own .srt/.lrc files stay on my device and are never uploaded or committed.
- Keep the install small: no new data file over 200 KB may be precached. Big data (dictionary) loads on first use, then works offline.
- Design: follow DESIGN.md "Night Study v2" and src/night.css tokens. Apply the design skills in sequence (Taste → Hallmark → Impeccable → Emil Kowalski motion rules). Sayo has one place on lesson screens. WCAG AA (axe in e2e), keyboard paths, reduced motion, no horizontal overflow at 320 px.
- Gates after EVERY batch: npx tsc --noEmit -p . ; npm test ; npm run packs (includes check:pinyin) ; npm run validate:content (includes the audio check) ; npx playwright test ; npm run build. Then screenshots at 1440, 768, 375 and 320 px that you actually look at. Fix before moving on. Report results honestly: what you ran, what you saw, what you did not verify.
- No new paid services and nothing live without asking me. Asking first is required before adding any npm dependency.

==================================================================
PROJECT C: THE COURSE: FINISH HSK 1, THEN HSK 2, THEN HSK 3
==================================================================
Goal: enough real, natural content to reach HSK 3, socially focused, with songs and drama reading built in.

C1. RESEARCH AND PLAN (prompts/research/course-plan.md)
  1. The official HSK 3.0 standard (GF0025-2021, 国际中文教育中文水平等级标准): per level 1–3, the character list, the word list (cross-check content/hsk/levels.json and report any differences) and the GRAMMAR POINT list (the standard has a graded grammar inventory; cite the exact source and use its item codes). Also the official topic and task descriptions per level.
  2. Coverage audit (write scripts/coverage-report.ts): which HSK 1–3 words, characters and grammar points are already taught (base lessons + packs), and which are left. Print counts per level.
  3. Unit plan: group the remaining items into units built around SOCIAL situations a young adult actually meets (making friends, group chats, dating and relationships at a polite level, roommates, parties, karaoke, ordering for a group, splitting the bill, inviting and declining, apologising, complaining politely, compliments, travel with friends, festivals and red envelopes, gaming and hobbies, work small talk, asking for and giving help, gossip at a safe level, social media comments).
     - Each unit: 15–25 new words, 2–3 official grammar points of that level, recycling earlier words.
     - Estimated count: finish HSK 1 in about 12–14 more units (s1-u13…); HSK 2 about 30 units (s2-u01…); HSK 3 about 35–40 units (s3-u01…). Adjust from your audit.
     - Spread the grammar so every official point is taught exactly once and recycled at least twice later.
  4. Native-quality strategy: how you will make the Chinese natural (mainland, casual or neutral register as appropriate), and how each unit is self-reviewed against a checklist before the gates.
  **STOP: show me the coverage numbers and the full unit list (titles, situations, grammar per unit) before writing units.**

C2. WRITE (batches of 4 units; the first batch of each level is a STOP for my review)
  Every unit follows the schema in prompts/content-prompt.md and passes validatePack with 0 errors. It contains:
  - vocabulary with an example per word (an example that contains the word), meaningVi (natural Vietnamese; add the Sino-Vietnamese reading where it helps, e.g. 汉字 = chữ Hán), usage notes where useful, correct hskLevel or null.
  - grammar: 2–3 points with ≤ 70-word explanations, ≥ 2 examples, common mistakes.
  - dialogue: 8–12 lines (HSK 1), 12–16 (HSK 2), 14–20 (HSK 3), 2–3 speakers from the recurring cast (林安, 陈宇, 安娜, 大明, 王老师; add new cast in HSK 2–3 if useful), with 3 questions: gist, detail, intent or inference. Only answerable by listening.
  - reading: a real-world format (WeChat chat, post, note, email, menu, sign, schedule, review) with a "purpose", 3 questions and a cloze with a distractor. Lengths: HSK 1 60–150 characters, HSK 2 150–300, HSK 3 300–500.
  - EVERY unit also includes ONE of these, alternating:
      (a) an ORIGINAL song verse (4–8 lines, singable, rhyme where natural, recycling the unit's words) as a second reading with format "note" and title marked as a song, plus an .lrc-style timing plan for when Sayo sings or reads it (record the line timings in the notes); or
      (b) an ORIGINAL drama scene written as subtitles (5–10 short lines, ≤ 16 characters per line, real subtitle rhythm), as a "message" format reading with speakers, with questions that need the whole scene.
  - conversation role-play (3–4 turns with accept regexes that are generous but not trivial), pragmatics (2–3 situations: natural vs too formal vs too blunt, mainland norms), and 8–10 tasks (about half the true/false answers false, plausible distractors, exactly one defensible answer, 【blanks】 with blankPy, answers in varied positions).
  - notes: "AI-assisted draft" plus anything a native reviewer should check.
  After each batch: npm run packs (validatePack + check:pinyin must show 0 errors and 0 pinyin problems), npm run validate:content, npm test, e2e, build. Generate Sayo audio for every new line with the existing mood rules (dialogue speakers by order of appearance: cool, playful, soft; everything else clear; songs in a sung or rhythmic reading style if the voice supports it, otherwise clear), then npm run audio:check. Screenshot one new unit's listening step, reading and song or drama scene at 1440 and 375.
  Self-review each batch with this checklist and fix what fails BEFORE the gates:
    natural mainland Chinese · right register · every new word used ≥ 2 times in context · no untaught characters outside glosses (coverage ≥ 95%) · distractors unambiguous · answers not guessable without the text or audio · pragmatics notes accurate for mainland China in the 2020s · Vietnamese meanings natural.
  Apply fixes yourself; don't just report them. Keep a changelog per batch in prompts/research/course-log.md.

==================================================================
ORDER, STOPS AND REPORTING
==================================================================
Order: approved C1 → C2 HSK 1 → HSK 2 → HSK 3, four units per batch with local audio and all gates. Claude handles A/B separately; do not edit the five protected files listed in AGENTS.md section 6.
At every STOP, give me a short plain-English summary: what you found or built, numbers, screenshots, what you verified, what you did NOT verify, and what you need from me.
Update AGENTS.md (current state, new commands and tables), PEDAGOGY.md (reading-speed method, dictionary and support rules), THIRD_PARTY_NOTICES.md (dictionary licence) and the QA notes as you go.
If anything in this brief conflicts with the code or with a better approach you find, say so and propose the change instead of silently deviating.
```

### Handoff boundaries

- GPT does not modify Watch, dictionary, reading-speed UI, storage migrations or sync for this work.
- Claude owns those app features. Schema gaps (such as an additional song/drama reading) must be proposed before implementation; no unsupported fields silently dropped.
- All speakers remain Sayo, with cool / playful / soft delivery by order of appearance. Existing approved B-half identity stays fixed.
- Completing a list is not an HSK pass prediction or a promise of drama comprehension. Distinguish GF0025-2021 learning benchmarks from the current examination syllabus.
- Stop only for an unfixable gate after a real repair attempt, a paid/live service or new npm dependency, a database/existing-data change, or an outline error needing the owner's decision. The owner authorized deployment after the completed run passes its checks.
