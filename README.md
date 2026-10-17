# Kiyo 清 · Mandarin, crystal clear

A local-first Mandarin study app with a characters-first foundation, conversation rehearsals and media practice. The authored route covers the GF2021 HSK 1–3 foundation and selected HSK 4–6 media/social units. Coverage means explicit curriculum introductions, not learner mastery, complete advanced vocabulary coverage or official exam readiness. All authored material remains an AI-assisted draft pending native review; acceptance and deployment status are recorded in [the course log](prompts/research/course-log.md).

## Run

Use Node.js 22.12+ (a current LTS is recommended) and npm.

```sh
npm ci
npm run dev
```

Open the local URL printed by the server, normally http://127.0.0.1:5173. No account, API key, Python installation, or audio model download is needed to use the app.

For the optimized offline-capable build:

```sh
npm run build
npm run preview
```

Open the printed preview URL, normally http://127.0.0.1:4173. Visit once while connected and allow the service worker to finish installing. The app shell and lessons then work offline. Audio and CJK font slices are cached as used; Settings → Save all audio downloads the complete voice library for offline study. Development mode does not install the offline service worker. Changing the hostname or port creates a separate browser storage origin; export a backup before moving to another origin.

## What works

- **Sayo 小夜, the study mentor**: reacts to answers with short Mandarin lines (Chinese, pinyin, English); level-ups name what you can now do; an optional days-in-a-row count. Final artwork spec in [MASCOT_BRIEF.md](MASCOT_BRIEF.md).
- **Beginner path map**: Read and Listen show a winding, Duolingo-style trail of units (learn → quick check → reading) with Sayo marking where to start, plus a plain-language 10-step “whole journey.”
- **Characters-first reading path** (switchable): starts with counting 一–十 and 66 seed characters in eight lessons, then continues through content-pack characters. Each new character shows its pinyin and audio with stroke-order animation, component breakdowns (meaning / sound / shape), labelled usage aids, example words and optional tracing. Sound and pinyin stay hidden until requested.
- **Graded readings**: original texts and pack dialogues with tap-to-gloss, optional pinyin and per-line English, coverage from your own unaided recognition, and comprehension checks.
- **Character wall** showing every character as not met / met / recognised / secure.

- Three-step onboarding with goals, a choice of path (characters first, side by side, sound first), a 10/20/30/45/60-minute daily budget, and quiet mode.
- **Course library** lists the installed units and their activities by level, with completion filters and links to reading and listening. **More → Your study desk** exposes the additional routes on desktop and mobile while keeping Kiyo's Night Study theme. Content validation reports actual installed totals; planned units are not completion evidence.
- Audio-first comprehension, explicit usage notes, retrieval reflection, character recognition, sentence assembly, recording/replay and supported alternatives.
- Bundled Sayo audio in multiple moods, including dialogue turns in the same voice identity. Audio must finish before an unaided listening response can be submitted. Optional device voices are also available.
- **Watch and sing**: local video or audio with timed SRT/VTT/LRC captions, subtitle/peek/no-subtitle practice, saved lines, notes and Anki export. Media files are never uploaded. Saved lines and watch history are included in device backups; they are currently local and are not part of cloud sync.
- **Branding**: the approved lowercase “kiyo” signature with Sayo leaning over it, plus a separate waving Sayo portrait for the app icon and browser favicon. PNG artwork is preserved; `/favicon.ico` and the old `/icon.svg` URL also display that portrait.
- Independent FSRS memories, due reviews, mistake records, pause/resume and an explainable daily plan based on actual attempts.
- Seed and content-pack conversation rehearsals, with optional local recording and transparent, limited typed-response matching.
- Three-pass Media Lab scene: gist, detail and return without text; segment replay, slower audio, local video, SRT captions and A–B loops.
- A searchable course dictionary, saved-attempt progress, backup export/import and full local reset.
- Responsive navigation, visible keyboard focus, reduced-motion support and text alternatives.

## Adding curriculum (content packs)

Units are written as JSON "content packs" (see `prompts/content-prompt.md` for the ChatGPT prompts and the exact format).

1. Save each unit as `content/packs/<unit-id>.json` (e.g. `s1-u03.json`). Files starting with `_` are ignored.
2. Run `npm run packs`. Every pack is checked in curriculum order:
   - pinyin lines up with the characters;
   - HSK 3.0 levels and pinyin match the official word list (`content/hsk/levels.json`, from the MIT-licensed complete-hsk-vocabulary dataset; refresh with `npx tsx scripts/import-hsk.ts`);
   - answer keys are valid;
   - every character in a text can be looked up;
   - ≥ 95% of the text is known vocabulary;
   - role-play patterns accept their own example replies;
   - ids are unique and prerequisites exist.
3. Packs that pass are published to `src/generated/packs.json` and become lessons automatically: words, grammar & usage, a dialogue and a reading in the reader, and a role-play in Speak. Packs with errors are listed with exact fixes and are not published.

Preview the format with the bundled example: `npm run packs -- --example --publish`. Run `npm run packs` again to return to the real set. Add every playable line, including supplementary readings, to the audio manifest and generate/screen its take before acceptance. Missing required audio fails validation. After one genuine repair attempt, only an explicitly dated, unreviewed entry in `content/voices/audio-deferred.json` may use the owner's approved device-speech exception; all other gates remain strict.

## HSK study room

Open **HSK** in the desktop navigation, or **More → HSK** on mobile (`/#hsk`). Select a target level and exam version. The Source desk links Chinese Testing International's syllabus, official sample papers and demo, plus BLCUP's HSK Standard Course textbook/workbook series. These open on their publishers' sites; book access may require purchase. No textbook pages or official questions are redistributed.

The internal track retains the 36 original HSK 2.0 Level 1 reading items and adds mixed GF2021-based practice banks for levels 1–6, with 90 original items per level: 60 checkpoint and 30 timed-sample items. Level 1's total includes its preserved legacy items. Retakes bring unseen items first, then the least-seen ones, while preserving earlier question IDs and results. Study the notes, then pass each checkpoint with at least 80% unaided and no pinyin help to unlock the next. Answers save locally; the timed sample's deadline continues when you leave. Missed and supported items stay in Mistakes until corrected without help. These are adapted practice tasks, not complete official papers; scores are raw practice results, never official scores or readiness estimates.

The roadmap also covers the combined advanced 7–9 exam, with level-specific entry prerequisites, study targets and sequential source-work checklists. Official external samples complement the internal practice; levels 7–9 have no authored internal bank. Source-work completion is self-reported and saved separately by level and exam version. Standard Course ends at 6; the advanced path links CTI's 7–9 requirements and sample tasks, including writing, translation and speaking. The advanced sample omits some questions, so it is not a complete mock. Legacy books and the 2021 vocabulary standard do not establish full new-syllabus coverage. Confirm the version with your centre.

The HSK notebook keeps its existing separate local database. It is included in **Export learning record** and also has **Export / Restore HSK notebook** controls at the bottom of the study room. It is not part of cloud sync. The installed practice and teacher art work offline; speech clips must first be cached through playback or **Save all audio**. Explicitly deferred device speech depends on the browser's available voice. External source sites need internet access.

Add reading packs as `content/packs/*.hsk.json`, following `hsk-reading.hsk.json`. `npm run packs` validates question structure, pinyin, answer keys and legacy Level 1 vocabulary before generating `src/generated/hsk-practice.json`. These AI-assisted original drafts still need human linguistic review. The new teacher pose preserves Sayo's approved design; her lines use the existing approved local voice.

## Evidence and privacy

The deployed app uses Supabase for Google sign-in and optional progress sync. Analytics, advertising, a remote tutor and cloud speech recognition are not connected. Attempts, review state and preferences are stored in this browser's IndexedDB. Audio recordings and imported media stay in the current tab and are discarded when their screen closes. Bundled voices are local. **Optional device speech voices may contact the browser/operating-system provider**; use the bundled voices for predictable offline behavior.

Use Settings → Export learning record regularly. Browser data can be cleared or evicted. Export includes attempts, schedules, mistakes, sessions, lesson positions and preferences, but no voice recordings or imported videos. Import validates the complete file before a transactional merge; matching IDs are replaced with the imported version after confirmation. Use one active study tab. Optional consent-based cloud sync is implemented but remains disconnected until configured; there is no application-level database encryption.

## Optional cloud sync

Copy `.env.example` to `.env.local` only when configuring an authorized Supabase instance. Keep it blank for local-only learning. Setup, the migration, the RLS verification script, and two-device acceptance checks are in [supabase/README.md](supabase/README.md). Production shares the Shiori Supabase project, with separate Kiyo tables and owner-only access rules.

Sync covers attempts, rebuilt schedules, mistakes, completed sessions and learning preferences. First sign-in with existing guest progress requires consent. Signing out keeps local data. Settings provides the last sync time, Sync now, Export learning record and Delete my cloud data. Cloud deletion pauses uploads and keeps a minimal deletion marker so another device cannot silently restore deleted history. Recordings, imported video, saved media lines/history and unfinished lesson positions stay local. Branding uses the approved lowercase website signature and separate waving square icon described above.

Supported attempts remain supported after help is hidden. Self-reported recall and recordings do not earn a measured pronunciation score. Typed scripted conversations are labeled rehearsal. Completed lessons are not fluency. Formal HSK mappings and exam readiness remain pending; the current exam and the 2021 standard are separate references.

## Validation

```sh
npm run validate:content
npm test
npx tsx scripts/screenshots.ts   # visual QA at 1440 / 768 / 375 into .impeccable/review
npm run test:e2e
```

Browser tests require Google Chrome and a running development server. If Chrome is unavailable, install a Playwright browser and adjust `channel` in `playwright.config.ts`.

To test the production service worker, start the preview server, then run in PowerShell with its actual URL:

```powershell
$env:APP_URL='http://127.0.0.1:4173'
npx playwright test e2e/reliability.spec.ts -g 'installed production'
```

See [QA.md](QA.md) for tested scenarios, exact scope and remaining checks. Content validation checks structural correctness and file coverage; it cannot certify natural Mandarin.

## Project guide

- [PEDAGOGY.md](PEDAGOGY.md): sources, decisions, hypotheses and measurement limits.
- [ARCHITECTURE.md](ARCHITECTURE.md): storage, evidence, curriculum contracts, provider boundaries and publishing architecture.
- [DESIGN.md](DESIGN.md): the implemented visual system.
- [BENCHMARKS.md](BENCHMARKS.md): source-linked product observations.
- [RELEASE_SCOPE.md](RELEASE_SCOPE.md): delivered scope and commercial release gates.
- [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md): audio, fonts, dictionary and software attribution.

`src/content.ts` owns original seed curriculum. `src/learning.ts` owns scheduling and evidence policy. `src/db.ts` owns persistence. Add content with stable IDs and provenance, regenerate audio when necessary, and validate before building. The application uses React, TypeScript, Vite, Dexie and ts-fsrs.

## Sayo audio generation

The app uses one original synthetic Sayo identity in six moods. Clear is the default for teaching and tone drills; Cool and Playful are selectable reading styles. Reactions select Cool, Intense, Soft or Deadpan to fit the line. Dialogue speakers use different moods and pacing, all in Sayo's voice. Word taps and speech bubbles replay their audio; quiet mode suppresses automatic comments.

The current rollout uses local Qwen3-TTS Base in `.voice-design-env` (Python 3.12, qwen-tts 0.1.1, PyTorch 2.6.0+cu124), with mastering and advisory Whisper screening in the same environment. Dependencies are pinned in `scripts/voice-qwen-requirements.txt`. Models and Python are not required to use the app. The pinned model, synthetic references and exact approved takes live in `content/voices/approved-b-half/profile.json`.

```powershell
npm run packs
npm run audio:manifest
.voice-design-env/Scripts/python.exe scripts/generate-audio-qwen.py --batch 6
.voice-design-env/Scripts/python.exe scripts/screen-audio-qwen.py --repeat-short --carrier
.voice-design-env/Scripts/python.exe scripts/master-audio-qwen.py
npx tsx scripts/voice-task-review.ts
.voice-design-env/Scripts/python.exe scripts/review-approved-audio.py
# Resolve screening discrepancies before installing:
.voice-design-env/Scripts/python.exe scripts/master-audio-qwen.py --install
.voice-design-env/Scripts/python.exe scripts/retain-released-audio.py
npm run audio:check
npm run build
```

`content/audio-scripts.json` covers phrases, contextual character pronunciations (`say`), word examples, pack grammar examples, reading lines, dialogue turns, tappable Mandarin answer choices and distractors, the welcome greeting and Sayo reactions. Both content validation and production builds check the fresh catalog against installed audio, rejecting stale manifests, missing moods, broken URLs and changed file hashes. Answer taps wait for the lazy catalog and use Sayo recordings only; English labels and unavailable answer recordings retain the interface sound. Unknown user-provided text can still use a device Mandarin voice, with a visible fallback message.

Restart `npm run dev` after a bulk audio installation so Vite refreshes its public-file inventory before playback tests. A stale development server can otherwise return the HTML shell for an MP3 that is present on disk.

`src/sayo-reactions.ts` supplies 100 lesson reactions in outcome-specific pools. Each pool cycles before repeating; a checked answer keeps its line stable. Ungraded practice is acknowledged without claiming it was correct. Reactions use the same approved identity and existing art. Their additional pitch offset is 0 to −0.5 semitone, putting them between −0.5 and −1 relative to the previous audition. One resampling pass also gently slows lower takes, without additional time stretching. The local rollout page includes all 100 reactions and 20 sample clips; transcription screening is not native-speaker approval.

The owner selected the half-semitone option from the final showdown: **-2.25 semitones from the unprocessed B blend**, or **-0.5 relative to Previous audition**. One fixed speaker representation combines synthetic B/current inputs at 85/15; those weights are not perceptual percentages. Mood references change delivery while the speaker representation stays fixed. Processing uses a single polyphase resample at 8837/7760, with no phase vocoder, time stretch or formant correction. Exact approved reactions bypass that step because they are already processed. No real person's recording is used. Mandarin pronunciation takes priority over theatrical delivery.

The generator resumes only files whose recipe and checksum match. It makes up to four attempts for invalid durations and stops on invalid audio. Outputs are mono 24 kHz / 64 kbps MP3s, trimmed and measured at -16 +/-1 LUFS. Generation and screening receipts remain in `.cache/sayo-qwen-approved`. Pronunciation repairs use a cumulative `--retry-list` JSON mapping entry-id/mood keys to take numbers; retain that map on subsequent runs. Installation checks the complete manifest and screening report before replacing the catalog. `content/voices/sayo-library-provenance.json` records model versions, reference recipes, seeds, processing and SHA-256 per file.

Open `/output/approved-voice-rollout/index.html` for the new task conversations, 20 reproducibly selected clips and every single-syllable clip. Whisper transcription, OpenCC spelling conversion and tone-number pinyin comparisons only identify review candidates; they do not certify tones or naturalness. Inactive installed MP3s and catalog snapshots are archived in `output/audio-backup-before-approved-b/`, outside the PWA. The original Kokoro backup remains untouched. Nothing in this workflow reads learner recordings or contacts a paid service.

Task audio includes `taskAudio()` for base lessons and validated packs. Conversation speakers receive Cool, Playful, then Soft in order of appearance; other task lines use Clear. Dialogue assemblies reuse the finalized line files. `npm run audio:check` rejects missing task mood files or spoken gap brackets. The older CosyVoice revisions described below are historical; the approved profile above is the current source of truth.

For ambiguous short words, `pronunciation-contexts.json` can synthesize a natural carrier followed by the target, then retain only that last clause. Carrier audio, crop boundaries and hashes are preserved. Written homophone cues are explicitly recorded and must retain the target's pinyin and tones. Screening can transcribe the complete carrier without supplying the expected text; this helps separate short-context recognition failures from wrong words. When a mood take remains uncertain, mastering prefers a screened take of the same text in another Sayo mood, usually Clear. Every substitution is listed in provenance; it never substitutes a different word or another voice. Unlisted texts with no screened alternative fail installation. Under the owner's audio-only exception, a dated deferral after a real repair stays unvoiced and unreviewed. Released-file retention restores exact previously committed URLs for cached clients before the audio/build gates run.

## Deployment

Deploy the `dist/` directory to an HTTPS static host at the domain root. Microphone access requires HTTPS or localhost. No service credentials belong in the browser bundle. A public preview is available at https://tingjian-mandarin-preview.gbao-n-vo.chatgpt.site. See HOSTING.md for its identity and update workflow. Establish a tested backup/sync policy, privacy review and content approval process before accepting paying learners.

Friendly drawl revision (October 4): Read and Welcome use Playful; all five reaction moods now ask for a fuller, smiling delivery with a modest phrase-final drawl. Soft means relaxed encouragement at normal volume, not whispering. Every gallery reaction—including Hint through Run—uses high-quality resampling for the two-semitone lowering, accepting a slightly longer duration instead of phase-vocoder pitch shifting. Reaction synthesis runs at normal speed; teaching-word settings remain unchanged. Every changed recipe gets a new filename, so cached older audio cannot masquerade as the revision. A regression check covers processing for all 17 gallery lines, and browser coverage plays each one to completion. File checks do not certify naturalness or perceived timbre; the owner still judges these by ear.

Smile-and-rise follow-up: the owner confirmed the metallic sound was gone but found the delivery grumpy. Reaction instructions now prioritize an audible broad smile, a full lower opening followed by a brighter higher register, wider expressive movement and more outgoing, affectionate humor. Mandarin lexical tones and the spoken text must remain intact. The model generates the intonation; no artificial pitch sweep is applied. The original synthetic reference and clean reaction processing remain the same.

`reactionTakes` can pin a line's direction and synthesis seed after comparing takes; both are included in its recipe hash and provenance. Welcome uses a selected wider-range take. Pitch measurements help compare range but do not establish friendliness, correct tones or naturalness.

Light teasing follow-up: the owner liked the smile-and-rise base and requested more intonation, slightly lighter delivery and a little tsundere personality. Reaction directions add playful question lifts, short pauses and affectionate mock-indifference with warmth underneath. The synthetic reference, reaction pitch processing, speed and greeting seed stay fixed; no dialogue words or teaching settings change. The preceding roster and manifest are preserved in `.cache/sayo-smile-base`, with superseded audio retained in `.cache/sayo-unused-audio`.


Accuracy-first follow-up: reactions are slightly happier and gentler, with synthesis speed at 0.98. The greeting no longer requests a staged pause or abrupt register jump. All HSK-tagged teaching entries now also use high-quality resampling instead of phase-vocoder pitch shifting. `pronunciationTakes` and `reactionTakes` in the roster pin per-line synthesis text, instructions and optional seeds; CosyVoice 3 pronunciation tokens can repair specific words without changing displayed Chinese. Every setting is recorded in each clip's provenance and filename hash.

HSK neutral particles play contextual phrases: 的 → 我的, 吗 → 好吗, 呢 → 你呢, 了 → 好了. Buttons name the actual spoken phrase and show its Chinese, pinyin and meaning. A local Whisper small pass was used to find suspicious takes, not to certify tones: short syllables, homophones and traditional-character transcriptions need human interpretation. The HSK word bank and `/output/voice-review/index.html` remain listening-review surfaces. Non-HSK teaching entries retain their previous processing unless they share an HSK catalog entry.
