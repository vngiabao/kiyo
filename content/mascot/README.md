# Ado mascot collection

The current **Quiet Ado** collection contains fourteen generated transparent 1280 × 1280 PNGs in `public/mascot/quiet/`. It follows the user's explicitly approved reference `exec-f5923449-08b7-4bc1-8597-e45f2b2946e9.png`: slender proportions, a small face, subtle expression, navy hair, turquoise eyes, a black coat-dress, and a teal brooch. The previous wide, squat face and exaggerated reactions are superseded.

Exact current prompts and source paths are recorded in `quiet-provenance.json` and embedded in each PNG. The full transparent set is `ado-quiet-set.zip`. The twelve first-version poses remain in `archive-v1/` with `provenance.json`; the fourteen squat chibi poses remain in `archive-v2/` with `chibi-provenance.json`. Earlier assets are retained locally and no longer ship.

Open `/#ado` to select all fourteen poses, replay finite motion, or download the selected transparent original from `/mascot/quiet/`. The collection starts with `grumpy` (Hmph! / Just a little hmph.) and is available before onboarding.

## States

- `grumpy`: the collection's default quiet pout and gentle tilt; never a judgment of the learner.
- `smug`: a subtle knowing expression and restrained settling gesture in the collection.
- `welcome`: onboarding and Today.
- `listen`: large audio controls; short motion begins with actual playback.
- `speak`: speaking overview, quiet speaking, and recording controls.
- `read`: character introductions and the reading path in onboarding.
- `write`: optional tracing in the character sheet.
- `think`: independent checks and loading a saved lesson.
- `hint`: revealed support and transcripts.
- `celebrate`: correct answers and completed lessons, readings, conversations, and reviews.
- `encourage`: incorrect answers and saved unscored practice.
- `review`: review overview before a check.
- `rest`: no reviews due.
- `error`: storage recovery, audio failure, recording failure, and save errors in exercise/media feedback.

## Motion and accessibility

`src/Mascot.tsx` uses whole-pose artwork with finite CSS transforms from `src/mascot.css`. Grumpy gently tilts for 1100ms; error uses that same quiet thought movement for 900ms. Smug settles over 1100ms with only ±1px translation; the 1050ms celebration rises 6px with slight anticipation and settling. The old stomp keyframes are unassigned to current states. Total runs remain 650–3200ms, including active listening and recording gestures; nothing loops indefinitely or delays a learning control. This is **not fully articulated or skeletal animation, lip sync, or a frame-by-frame sprite sequence**.

Settings persist **Show Ado** and **Animate Ado**. Hiding Ado removes her from learning surfaces; the deliberately opened collection still displays the artwork. Motion remains off while preferences load, and the persistent motion setting applies to both learning and collection. System reduced motion overrides all mascot animation and transforms. Replay cannot bypass these controls.

Images are decorative, non-interactive, empty-alt, and hidden from assistive technology; nearby text carries meaning. No custom cursor or pointer tracking. Notebook/card props must remain free of readable answer characters and outside independent checks. Unscored practice gets encouragement rather than an asserted correct-answer reaction. Learning evidence and scheduling are unchanged.

## Current revision evidence

- All fourteen filenames match the scenario set and use `/mascot/quiet/`.
- The implementation handoff reports the production build and all 14 existing learning tests passed.
- Recorded palette checks in `.cache/mascot-qa/quiet-contrast.json` contain 40 passing pairs. The implementation handoff also reports no failures in the rendered lesson text check, plus working phone collection selection and pause controls.
- Current captures: `.impeccable/review/quiet-gallery-desktop.jpg`, `quiet-gallery-mobile.jpg`, `quiet-today-desktop.jpg`, `quiet-today-mobile.jpg`, and `quiet-lesson-mobile.jpg`.
- A supplementary Media Lab viewport capture is `.impeccable/review/quiet-media-desktop.jpg`.
- Current CSS establishes the finite motion and suppression rules; still screenshots establish composition, not animation timing.
- `DESIGN.md` and `.impeccable/design.json` now record the approved Night Study palette and actual current controls.
- Fresh review/publication are separate. This documentation update claims no final reviewer verdict or new deployment.

## Chibi revision evidence (historical)

The former chibi set used `/mascot/chibi/`; its fourteen-state captures are `ado-chibi-desktop.jpg` and `ado-chibi-mobile.jpg` under `.impeccable/review`. It used stronger squash, a 1050ms leap/landing cheer, and grumpy/error stomps. Those appearances and motion assignments are superseded by Quiet Ado. The recorded release result below remains historical.

## First-version verification (historical)

The following recorded checks apply to the original twelve-pose release, not by themselves to the revised chibi assets:

- Production TypeScript/Vite build and the existing 14 learning tests pass.
- Desktop and phone captures are under `.impeccable/review/ado-*.jpg`.
- Browser checks covered gallery selection, pause/replay controls, zero broken gallery images, listening activation, hint reveal, wrong-answer encouragement, persistent visibility and motion preferences, and onboarding.
- All 12 PNGs carry prompt provenance. The production service worker precaches them for offline use after installation completes.
- Real remote-phone testing, microphone recording permission, and an exhaustive all-lesson regression are not claimed.

## Chibi release result (historical)

The subsequent chibi finish review cleared the scoped correction. Production build, prompt coverage, and desktop/mobile captures passed. Version 3 is published; the public gallery shows fourteen states, selection works, and all images load. Full transparent PNG pack: ado-chibi-set.zip. Exact prompts and source paths: chibi-provenance.json. See design-evidence.md for the revision and publication evidence.
