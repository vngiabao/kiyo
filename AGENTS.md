# AGENTS.md: start here

> Follows ../SHARED-SPEC.md (shared structure with the Japanese sibling, Shiori). Visual source of truth: `src/night.css` + DESIGN.md "Night Study v2". Don't reintroduce filled verdict bars, uppercase stats labels, mascots inside tables, or a second mascot position in lessons (Today's framed Sayo card is a deliberate exception, 11 Oct 2026).

You're continuing work on **Kiyo 清**, a Mandarin-learning web app for one serious adult learner (the owner). The goals are years of study, real conversation, professional-level Mandarin and a high HSK score. Reading characters matters a lot. Read this whole file before changing anything.

## 1. Run it

```sh
npm ci            # once
npm run dev       # http://127.0.0.1:5173
```

Checks (run all before saying something works):

```sh
npx tsc -b                 # types
npm test                   # unit tests (vitest), 190 tests
npm run validate:content   # curriculum consistency
npm run check:pinyin       # every pack line's pinyin vs the HSK 3.0 dictionary (also runs in packs/build)
npm run test:e2e           # browser tests (needs `npm run dev` running and Google Chrome)
npm run build              # production build (also runs `npm run packs`)
```

Visual QA: `npx tsx scripts/screenshots.ts` saves screenshots at 1440 / 768 / 375 px to `.impeccable/review/`. Look at them after UI changes.

## 2. What the app is (map of the code)

- **Stack:** React 19 + TypeScript + Vite, local-first. Data is in IndexedDB via Dexie (`src/db.ts`, database name `tingjian-v1`). **Never rename the database or storage keys:** it would erase the learner's progress. The PWA works offline.
- **Screens:** `src/App.tsx` contains the shell, Today, Listen path, Progress, Dictionary and Settings.
- **Characters and reader:** `src/Characters.tsx` (character path, reader, stroke animation via hanzi-writer).
- **Lessons:** `src/LessonPlayer.tsx` (every exercise type, level-up screen, Sayo reactions).
- **Speak and Media:** `src/Conversation.tsx` (scripted role-plays), `src/MediaLab.tsx`, `src/Practice.tsx` (practice and review queue).
- **Curriculum:**
  - `src/content.ts`: base phrase lessons and exercise generators; merges content packs.
  - `src/hanzi.ts`: 66 characters in 8 reading lessons, starting with counting 一–十, plus 5 graded readings.
- **Content packs (how new curriculum gets in):** `src/packs.ts` (format, checker, lesson builder) and `scripts/build-packs.ts` (`npm run packs`). Packs live in `content/packs/*.json`; only passing packs are written to `src/generated/packs.json`. The format reference is `content/packs/_example.json`, and the ChatGPT prompts are in `prompts/content-prompt.md`. HSK 3.0 word list for checking: `content/hsk/levels.json`.
- **Learning logic:** `src/learning.ts` (FSRS spaced repetition per skill; daily plan), `src/progression.ts` (level = lessons finished; days in a row).
- **Mascot:** `src/Mascot.tsx` + `src/mascot.css`. 小夜 **Sayo**, a cool sensei who speaks in short Mandarin lines (Chinese → pinyin → English). Art is in `public/mascot/quiet/*.png` (originals) → `public/mascot/web/*.webp` (what the app loads, made by `python scripts/prepare-mascot.py`).
- **Brand:** `src/brand.tsx`. App name **Kiyo 清**, logo drawn from 清 stroke data; the top bar of 青 is lit blue as the qīng tone mark. `scripts/make-icon.ts` builds `public/icon.svg`.
- **Sign-in:** `src/auth.ts` + `src/Welcome.tsx`. Supabase (Google, Apple, email code), off until `VITE_SUPABASE_URL` / `VITE_SUPABASE_ANON_KEY` are set. "Start without an account" always works.
- **Audio:** Sayo clips in `public/audio-v2/` from local Qwen3-TTS (`scripts/generate-audio-qwen.py` → `screen-audio-qwen.py` → `master-audio-qwen.py`, env `.voice-design-env`; steps in README "Sayo audio generation"); device voices are the fallback.
- **Design:** read `DESIGN.md` first. Dark "Night Study" theme: midnight navy, pale-blue accent, Newsreader + Instrument Sans + Noto Serif SC. Motion: transform/opacity only, ease-out, under 300 ms, and `prefers-reduced-motion` respected.

## 3. Rules (don't break these)

1. **Honesty over hype.** No fake scores, no invented HSK readiness, no pretend pronunciation grading. Supported answers (pinyin or transcript shown) never count as unaided.
2. **Don't change Sayo's design.** The owner likes the current art. Only the poses listed in `prompts/sayo-pose-revisions.md` are being regenerated. The name "Ado" must not appear anywhere: legal risk, since that's a real singer.
3. **Curriculum goes through packs.** Don't hand-write lessons into `content.ts`. Add `content/packs/<unit>.json` and run `npm run packs`. Never let a model guess HSK levels; the checker uses the official list.
4. **Every new word shows its pinyin.** Quizzes start without pinyin; revealing it marks the answer as supported.
5. **Chinese leads, pinyin second, English third.** Simplified characters and mainland Putonghua.
6. **Keep it accessible.** Keyboard works everywhere, visible focus, WCAG AA contrast (the e2e suite runs axe), and nothing breaks at 320 px.
7. **Don't publish anything, push, or connect paid services without asking the owner.** Never put API keys in browser code.
8. **The app is built around one personality: Sayo.** Ado-style vibe: introverted, cool and composed, with sudden bursts of intensity. All audio is her single voice in different moods (clear, cool, intense, soft, deadpan, playful). No male voices and no other character voices. Copy, reactions and UI tone should sound like her: brief, dry, sincere.
9. **Match the existing code style.** Small, readable files; comments only where the "why" isn't obvious.

## 4. Current state (October 2026)

- **HSK 1 course:** 12 units in `content/packs/s1-u01…u12.json` (social situations; units 11–12 feed songs and dramas). Each unit: words → listening conversation → grammar & usage → mixed exam-format tasks; reading with a purpose and a gap-fill. Today continues from the 20 base lessons into these units. AI-assisted drafts: native review still needed (`prompts/gpt-side-tasks.md`).
- **Lessons teach like a course:** checks come one item after introduction; HSK task formats live in `src/tasks.ts` + `src/TaskView.tsx`; answer positions are varied and tested; review brings back the task you missed (`reviewTaskFor`).
- **Media = Watch & sing:** your own video/song + .srt/.vtt/.lrc (`src/captions.ts`, `src/Watch.tsx`): three rungs (subtitles → peek → none), counted peeks/look-ups, saved lines (Dexie v3 `savedLines`, `watchLog`, in backups) and Anki export; plus the six-stage route.
- **Dictionary (offline, CC-CEDICT, CC BY-SA 4.0):** `npm run dict` builds `public/dict/` (256 shards, loaded per lookup, cache `kiyo-dict`, never precached). `src/dictionary.ts` splits lines into words (96.6% boundary accuracy on the test set in `tests/dictionary.test.ts`); `src/WordCard.tsx` is the tap card used by the Watch player and the reader. Saved words: Dexie v4 `personalWords` (in backups, Anki export). Research notes: `prompts/research/dictionary-and-speed.md`.
- **Reading-speed drill:** Practice → Reading speed (`src/drill.ts`, `src/ReadingDrill.tsx`). Only lines from finished content, made of taught characters, flashed at your pace; unaided meaning check; staircase pace; Netflix reference of 9 chars/s (adults), 7 (children). Sessions: Dexie v4 `readingSpeed` (in backups).
- **Fitting 150 units on screen (11 Oct 2026):** Listen puts one unit on the stepping-stone trail ("Where you are") and lists the rest in a Foundation / HSK 1–6 level strip with a unit grid (`Learn` in `src/App.tsx`); a finished unit gets a green banner with Sayo celebrating (`src/PathMap.tsx`). Speak groups role-plays by the same strip; the Dictionary pages 60 rows at a time. A days-in-a-row chip (`StreakChip`) sits in the masthead and obeys "Show days in a row". Never render the whole course as one list again.
- **Lasting:** audio is cached on first play (`sayo-audio` cache) with "Save all audio" in Settings; persistent-storage request; weekly backup reminder on Today until sync is live.

- **Done and working:**
  - onboarding with sign-in;
  - characters-first path (counting first), graded reader with tap-to-see meanings;
  - phrase lessons, role-plays, Media Lab;
  - FSRS review, levels and days in a row;
  - the Sayo mentor;
  - the Kiyo brand;
  - the content-pack pipeline with validation.
- **Content is small:** about 78 phrases and 66 characters, roughly HSK 1. Growth comes from content packs the owner generates with ChatGPT.
- **Waiting on the owner:**
  - regenerated Sayo poses (`thumbsup.png` and `run.png` are new; others are revised);
  - first real content packs;
  - a Supabase project (for sign-in to switch on).

## 5. Next tasks, in order

1. **Cloud sync** (most important: the learner will put in years of progress). Use the existing Supabase sign-in.
   - Sync attempts, memories, mistakes, sessions and the profile.
   - Attempts are immutable UUID records, so merge by id.
   - For profile conflicts, last write wins.
   - Keep working offline: queue changes and sync when online.
   - Never sync voice recordings.
   - Add `.env.example` and setup steps to the README.
2. **AI conversation partner** for each pack's role-play (`conversation.aiPartnerBrief` already exists in packs).
   - Call the Claude API **through a server or edge function** (e.g. a Supabase Edge Function). Never from the browser with a key.
   - Correct only meaning-breaking errors during the chat; give a short register note at the end.
   - Ask the owner before connecting anything paid.
3. **Grammar in review:** add grammar-example and "say it naturally" items to the review queue (`src/Practice.tsx` → `Review`).
4. **Audio for packs:** add pack phrases and texts to `scripts/audio-manifest.ts`, then follow README "Sayo audio generation" (Qwen pipeline).
5. **New Sayo art:**
   - when the PNGs land in `public/mascot/quiet/`, run `python scripts/prepare-mascot.py`;
   - delete `pending` and `fallback` from `thumbsup` and `run` in `src/Mascot.tsx`;
   - check the gallery at `/#companion`.

After each task: run the checks in section 1, look at screenshots, and tell the owner plainly what's done, what was verified and what's left.

## 6. Current course handoff (5 October 2026)

- The owner split the next phase: Claude handles the dictionary and timed reading drill (A/B); GPT handles course research, content packs and Sayo audio (C). Brief: `prompts/gpt-next-phase.md`.
- C1 plan: `prompts/research/course-plan.md` and its JSON ledger. Approved for all 96 units on 5 October 2026; the owner revoked intermediate review stops. Claude implemented `extraReadings` and the word-readability gate. Do not edit `src/packs.ts`, `src/dictionary.ts`, `src/Watch.tsx`, `src/ReadingDrill.tsx`, or `src/drill.ts` during C2.
- Reproduce the audit: `npx tsx scripts/coverage-report.ts --write`. Evidence is curriculum introduction, never learner mastery. GF0025-2021 vocabulary, characters and grammar are separate from the newer exam syllabus.
- Current conservative GF2021 word coverage: level 1 189/500, level 2 26/772, level 3 6/973. The 96-unit proposal includes grammar ownership and later retrieval slots; exact lexical/character allocations are finalized before each batch. Research files are not app assets or precache inputs.
- Preserve the approved B-half Sayo identity and existing audio checks. A/B storage, UI and dictionary work remains Claude's scope. Shared-check results and handoff limitations: `prompts/research/c1-validation.md`.

## 7. Current factual handoff — 10 October 2026

Earlier dated state and counts are historical. The completed run has 144 course units: 30/34/44 foundation units for GF2021 levels 1/2/3 and 12 selected media/social units per advanced level 4/5/6. Foundation introduction coverage is 500/772/973 source words, 300 new explicit characters per level and 48/81/81 grammar families. The advanced route is selected content, not full level inventory coverage or learner mastery. The six rotating practice banks have 90 original items per level (60 checkpoint, 30 sample); Level 1 preserves its legacy IDs. These are adapted practice, not full official papers.

The final acceptance run has 190 unit tests, 45 development browser cases and four separate production offline/update cases. Current evidence and exact source fingerprint are in QA.md; detailed fixes, word/grammar crosswalks and batch receipts are described in prompts/research/course-log.md. Native approval is still pending: prompts/research/native-review-lines.json contains exact candidates.

The approved brand is the lowercase Sayo-over-kiyo website signature plus a separate square waving app icon, including favicon exports. Do not regenerate the older stroke-glyph/capital-letter logo. Course library and the desktop/phone study-desk drawer are installed; retain Night Study styling.

Current audio uses the approved B-half identity and local generation/screening pipeline, not the historical Kokoro-only setup. Under the owner's later audio-only exception, a line that fails verification after a genuine repair may be explicitly dated and deferred in content/voices/audio-deferred.json, with device speech and native review still pending. All other gates remain strict, and unexpected missing clips must fail. Audio download remains separate from the small initial install. Never treat a speech-transcription match as tone certification.

Supabase and Google-only sign-in are configured for the shared owner project with separate app tables. The owner chose to keep guest progress on this device; do not merge or clear it. Real public two-device sync remains a separate verification limit. Preserve tingjian-v1 and kiyo-hsk-v1 and their existing data. The owner's explicit authorization covers commits, pushes and these course deployments; it does not authorize new paid services, dependencies or security-policy changes.
