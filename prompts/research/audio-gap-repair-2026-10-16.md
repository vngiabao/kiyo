# Sayo audio gap repair — 16 October 2026

The owner asked to repair the missing-recording report. Use the existing local
approved B-half profile, fixed speaker embedding and single-pass mastering. Do
not retrain, change identity, relax pronunciation checks, claim native
approval or modify learner data.

## Baseline and causes

- 369 directly deferred texts affect 478 effective manifest texts once assembled
  passages are included. These are genuine previous repairs that failed the
  advisory transcription screen, not 478 separately missing recordings.
- The old answer audit counted 91 gaps. Six were English labels mentioning
  Chinese; those should keep the interface sound. Among the 85 Mandarin gaps,
  63 overlap with direct deferrals and 22 require new manifest entries.
- Answer taps used a synchronous lookup against a lazy catalogue. A first tap
  before catalogue loading could incorrectly pop even for an installed recording.
- The command-line audit also used the browser's unloaded catalogue. It now
  reads installed mappings directly and distinguishes deferrals from new gaps.
- Dialogue question choices did not set `data-say`, even when written in Chinese.
  The generic choice renderer now tags Mandarin choices independently of its
  display-style flag, using the same English-label exclusion as playback.
- Ten saved failed transcripts contained integer percentage notation such as
  `20%` for spoken `百分之二十`. The screener now expands that exact notation before
  its existing number normalization. Wrong values, decimals not yet supported,
  negative values and percentage-point substitutions remain rejected by tests.
  Erhua handling and all tone/pinyin comparisons stay unchanged.
- Sixty saved failed transcripts use traditional `著` where the authored aspect
  marker is `着`. An exact aligned spelling equivalence is allowed only with the
  authored neutral `zhe`; changed words, omitted markers and `zhù` still fail.
  The same existing homophone-transcript review category records this ambiguity.
- Repeated-word screening previously dropped an already saved carrier transcript,
  causing an unnecessary repeat probe and source scan. Both receipts now survive;
  a model-free integration fixture proves a failing word remains unaccepted and
  terminates after exactly the original, carrier and repeated probes. Each pass
  also reuses its exact-hash-verified receipt snapshot for its final count, rather
  than rereading all receipts. No waveform hash check or probe is skipped.
- Repair/defer source verification now overlaps eight independent file reads.
  It still hashes every waveform and requires each matching screening receipt;
  four model-free tests prove changed bytes, missing receipts and missing screen
  records fail, while output order and failure statuses are preserved. Screening
  finished before this optimization; only its still-running source recheck was
  restarted, from the completed screening ledger, using the concurrent verifier.
  Mastering also overlaps receipt-metadata reads; its chosen-source, encoded-output
  and assembly-part hash checks remain unchanged. All six installation tests pass.

## Implementation

`scripts/answer-audio.ts` enumerates the Chinese choices, distractors, reorder
tokens, cloze banks and matching cards that the current UI exposes. The audio
manifest includes their exact contextual speech targets in Clear; the existing
audio/build checks therefore reject future unlisted omissions. English labels
containing Chinese examples remain interface sounds.

`src/answer-voice.ts` waits for a cold catalogue, discards older queued choices,
respects quiet/read-choice settings and forces the single Sayo narrator. Answer
taps explicitly disable device fallback on failed recordings; ordinary teaching
audio retains the owner's existing documented device-speech exception. Tests
cover loading, rapid taps, cancellation, failures, contextual character readings,
mixed English labels and device-voice preferences.

The first complete browser pass exposed an existing source-checklist race in
`src/Hsk.tsx`: its optimistic check was removed when the write completed, before
Dexie published the new settings, allowing one unchecked frame. The selection now
waits for observed acknowledgement and rolls back on a failed write. The original
HSK prerequisites/supported-answer/reload/isolation test passes three consecutive
runs after this fix. No database schema, stored records or test assertions changed.
The first failure evidence is kept in `output/audio-gap-repair/checklist-race-error.md`.

That rerun found two MP3 playback failures caused by the long-running Vite server's
stale public-file inventory after bulk replacement: a present, hash-valid MP3
returned HTTP 200 `text/html`. Restarting only that development server restored
HTTP 200 `audio/mpeg` with the exact 4,268-byte file. Checks and assertions are
unchanged. The prior errors are preserved in `output/audio-gap-repair/`; the README
now documents the required development-server restart after bulk installation.
All ten focused reading/character playback tests then passed unchanged, including
completed character-sheet recordings; the final complete browser run passed too.

## Recording repair

`scripts/prepare-audio-gap-repair.py` saved the pre-install ledgers and hashes in
`output/audio-gap-repair/before/` and recorded all queued recipes in `baseline.json`.
It queued one genuinely new Clear take for each of the 369 directly deferred
texts. Of those, 150 use a short pronunciation-matched carrier followed by the
exact target; only the final clause may be retained. Long lines retain their
exact written Chinese. All use the pinned speaker and a calm speaker-only prompt.
The new 22 answer choices are also included in the full generation plan.

Generation is resumable from exact recipe/hash receipts. Do not rerun preparation:
its baseline guard prevents accidentally incrementing takes a second time.
Log: `output/audio-gap-repair/generate.log`. Reuse the existing plan and cache for
screening, one genuine repair of any newly failing choices, accepted-only mastering,
deferral pruning and exact released-URL retention. Failed takes must stay absent
and unreviewed; no gate should be weakened to make the count reach zero.

At this point the focused answer/provider tests and types pass. Full content,
audio, browser, unit and production gates remain pending until installation.

## Run checkpoint

All 391 planned new takes (369 repairs plus 22 answer choices) were generated
successfully in `output/audio-gap-repair/generate.log`. Transcription is resumed
from its checkpointed cache with the spelling fixes above. The local finishing
runner is `output/audio-gap-repair/finish-audio.ps1`; it screens, genuinely retries
new failed choices, prunes/document deferrals, installs only accepted takes,
restores released URLs, builds a listening checklist and runs the audio gate.
Its stage log is `output/audio-gap-repair/finish.log`.

Before installation: all 200 then-current unit tests passed; one additional
bare-character fallback regression was then added and its focused tests pass.
Nine screen-helper tests, six installation-helper tests, five retention-helper
tests and four concurrent-repair verification tests pass. The strict erhua regression remains in the screen suite. The new
answer guard never substitutes a bare polyphonic glyph for a missing contextual
reading. Final all-gate acceptance and deployment remain pending.

## Installed result

The resumed finishing pipeline passed generation screening, the new-choice retry
audit (zero further jobs required), dated deferral reconciliation, accepted-only
installation, history-aware released-file retention and the installed audio gate.
All 22 genuinely new answer choices obtained an accepted recording. Of 369 direct
deferrals, 208 recovered; 34 dependent assembled passages recovered too. Across
the original gaps and newly added choices, 264 texts now have Sayo audio.

The 17,322-text manifest now has 17,086 installed texts and 47,127 mood mappings,
using 46,611 active MP3s. There are 960 new MP3 files; all 55,823 pre-repair released
files remain represented with identical hashes. The compatibility ledger retains
10,172 inactive released clips for cached clients. Profile and staged-roster hashes
still match the baseline, preserving the approved B-half identity and processing.

Of 2,832 actual Mandarin answer targets, 2,808 are voiced. The remaining 24 are
documented pronunciation deferrals; no answer is missing merely because it was
never recorded. In total, 161 direct texts and 75 dependent assembled passages
(236 texts) remain deferred after genuine repairs. Ordinary lesson playback uses
the documented device fallback; unavailable answer choices retain the interface
sound. English explanations mentioning hanzi are excluded from this Mandarin count.

Exact failed lines, repair evidence and recovered recordings for native listening
are in `prompts/research/audio-gap-repair-native-review.json`. Nothing there is
marked native-reviewed. Transcript agreement is not tone/naturalness certification.
Machine-readable reconciliation: `output/audio-gap-repair/result.json`.

## Acceptance

All eight final gates passed on unchanged source fingerprint
`3cb15283d14ec48f722c1bdec70b402fdce7170794282771b235040c843f251e`:
packs (including pinyin/readability), types, content/audio, 201 unit tests,
playback fixtures, 46 development browser tests, production build and four actual
production offline/update tests. The four production cases skipped in development
were all executed separately, not waived. The build verifies 144 units and 17,086
installed audio texts unchanged during bundling. Deployment packaging contains
56,783 clips in 385 lossless chunks (2,098.8 MiB), with 2,867/20,000 static files.

Source-checklist timing and stale-server errors were repaired before this final
acceptance. No checks were skipped or weakened. Native listening remains pending
for the exact candidates in the linked JSON; no tone certification is claimed.

The packaged production Worker passed the exhaustive local route audit: 56,783
HEAD responses had the expected status, audio MIME and exact byte length. Full GET
hashes matched for 1,353 bodies, covering all 960 new files plus the random sample.
A nonexistent MP3 returned a clean 404. The audit consumes only local requests.
Receipt: `output/audio-gap-repair/worker-route-audit.log`.
