# AGENTS.md: start here

> Follows ../SHARED-SPEC.md (shared structure with the Japanese sibling, Shiori). Visual source of truth: `src/night.css` + DESIGN.md "Night Study v2". Don't reintroduce filled verdict bars, uppercase stats labels, mascots inside tables, or a second mascot position in lessons.

You're continuing work on **Kiyo 清**, a Mandarin-learning web app for one serious adult learner (the owner). The goals are years of study, real conversation, professional-level Mandarin and a high HSK score. Reading characters matters a lot. Read this whole file before changing anything.

## 1. Run it

```sh
npm ci            # once
npm run dev       # http://127.0.0.1:5173
```

Checks (run all before saying something works):

```sh
npx tsc -b                 # types
npm test                   # unit tests (vitest), 27 tests
npm run validate:content   # curriculum consistency
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
- **Audio:** bundled MP3s in `public/audio/` from a local Kokoro TTS model (`scripts/generate-audio.py`, Python env `.audio-env`, models in `.models/`); device voices are the fallback.
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
4. **Audio for packs:** add pack phrases and texts to `scripts/audio-manifest.ts`, then run `scripts/generate-audio.py`.
5. **New Sayo art:**
   - when the PNGs land in `public/mascot/quiet/`, run `python scripts/prepare-mascot.py`;
   - delete `pending` and `fallback` from `thumbsup` and `run` in `src/Mascot.tsx`;
   - check the gallery at `/#companion`.

After each task: run the checks in section 1, look at screenshots, and tell the owner plainly what's done, what was verified and what's left.
