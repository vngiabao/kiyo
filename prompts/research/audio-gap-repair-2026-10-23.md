# Remaining Sayo recording repair — 23 October 2026

The owner asked to finish the recording repair, rather than stop at a status
explanation. The starting catalog has 161 directly deferred source texts and
75 dependent passages; 24 of the source gaps are Mandarin answer targets.

The first pass queues a new Clear take for every remaining source text. It uses
the same approved B-half fixed speaker embedding, approved anchor delivery and
single-pass mastering. Sampling is 0.7 rather than the prior speaker-only 0.55;
short targets retain pronunciation-matched carriers and an exact final crop.
No curriculum, identity, pitch processing, pronunciation acceptance rule,
database, authentication or design changes are part of this repair.

Preparation now accepts a separate guarded run directory so the previous repair
baseline stays intact. Current snapshots and logs are under
`output/audio-gap-repair-2026-10-23/`. Re-running preparation with the same ID
refuses to overwrite the baseline or increment takes twice.

The generator now overlaps eight independent cached-source checks. Every
waveform is still hashed before reuse; a missing receipt queues generation,
while a changed or missing cached waveform blocks reuse. Three regression
fixtures verify these distinctions. The previous screen, mastering, repair
and released-URL retention tests pass unchanged.

The first pass generated all 161 takes. It recovered 24 source texts directly;
precise transcription-format and pinyin fixes increased that to 32. The remaining
129 texts are receiving a second take with reference delivery, 0.4 sampling and
whole-word synthesis for short targets. Exact-toned written cues disambiguate
the remaining short words; the cue guard rejects changed syllables, tones,
unmatched authored readings, omitted erhua and extra non-Chinese material.
Unchanged syllables may retain authored sandhi; every changed glyph must match
its own authored tone as well as the original full phonetic sequence.

One pack field was wrong: s3-u39's 闭着眼 had `bì zhuó yǎn`, corrected to
`bì zhe yǎn`. Chinese, IDs and answers are unchanged. The existing dictionary
gate accepts multiple readings, so it did not catch this contextual mistake.

ASR's numeral `2` can represent authored 两. Screening now resolves only a
literal Arabic 2 at the exact aligned position of an authored 两; explicit 二,
other values, decimals, negatives, digit sequences and unrelated positions are
not reinterpreted. Existing tone and erhua handling is unchanged. Neutral 地/得
spelling equivalence can also coexist with another independently matching
homophone in the same line, while still requiring authored neutral `de` and the
contextual 得 rule. Regression fixtures retain wrong-tone/omission rejection.

The answer 有条件地继续试周四 lacked pinyin in the manifest. Its authored
neutral reading now lives in `content/voices/audio-pronunciations.json`; the
manifest rejects unused keys and includes the pronunciation in its normal
staleness check. This changes recording metadata only, not the answer or UI.

Second-pass logs are under `output/audio-gap-repair-2026-10-23-round-2/`.
The final targeted pass generated 44 further takes using only still-failing
texts with checked cues. Short cues use a pronunciation-matched carrier and
an exact final target crop. Its logs are under
`output/audio-gap-repair-2026-10-23-round-3/`. All 36 Python helper tests pass
(13 screening, 6 mastering, 4 repair, 5 retention, 3 generation, 5 cue guards).
Across three passes and the precise metadata/orthography fixes, direct source
deferrals fell from 161 to 105. Final affected-reading/answer counts depend on
accepted-only installation and reconciliation, which are in progress.

An independent blind local Whisper large-v3 diagnosis then confirmed 39 of those
105 recordings: 18 exact text matches, 20 matches under the existing phonetic
comparison and one already-supported erhua transcript equivalence. No expected
text was supplied to recognition. `scripts/verify-independent-audio.py` verifies
the pinned local recognizer's hash, the current generation receipt and exact
waveform, then recomputes the unchanged screening criterion. It preserves the
original primary failure alongside the new transcript and model proof. Six
regressions reject stale bytes, another model/target, wrong-tone false-pass
labels and omitted erhua. The resulting 66 failures stay explicitly deferred.
`content/voices/independent-audio-verification.json` retains the full evidence;
mastering carries it into each affected clip's provenance. The audio build gate
also rejects missing, changed or incomplete independent evidence.

The first installation was stopped before catalog publication because serial
cache reads dominated its runtime; its catalog hash still matched the initial
baseline. Encoded checkpoints were retained. Mastering now overlaps independent
source/cache reads and reuses each already-verified MP3 hash when checking its
assembly references. All source/output bytes remain checked. Three additional
mastering tests reject changed raw or encoded files and preserve pending/order
semantics. Installation is resumed from those exact checkpoints.

## Final acceptance

The final catalog restores 137 texts (96 direct sources and 41 dependent
passages), with 17,223 of 17,322 manifest texts voiced. There are 65 direct
exceptions and 34 dependent passages, totaling 99 explicit fallback texts.
Mandarin answers improved from 2,808/2,832 to 2,827/2,832; five unverified choices
retain the interface sound. The installed library has 46,962 active MP3s and
10,233 compatibility files. All 56,783 previously served URLs remain identical.
The pinned profile and staged-roster hashes still match the starting baseline.

The last metadata case was 要，网页还没有跟着改。 A newer take remained
unresolved, but an exact earlier repaired waveform passed after adding the
authored neutral `zhe`. The historical selector inspected 282 recorded repair
receipts and verified the source bytes, profile, delivery, recipe filename and
saved blind transcript before choosing that one take. `highest-takes.json`
preserves the higher attempted number so a future repair stays genuinely new.
The other new metadata entry records 不会，老师说不用多交。 without changing its
words or accepting the unresolved take.

Mastering now leaves hash-checked unexpired compatibility files in place, avoiding
unnecessary archive/restore churn. Exact-byte Git attributes prevent public asset
conversion and preserve the approved CRLF recipe bytes. No protected C2 source,
storage key, database name, dependency, authentication setting or design changed.

All eight final gates passed, including 210 unit tests, 50 development browser
tests and the four actual production offline/update cases. All 52 Python helper
tests passed. The tested source fingerprint is
`7e5f83deff6748de2aa389141d14baf0ac6add7a24ede9504904cd56e0889685`.
The local packaged Worker passed 57,195 route checks and 811 full-body hash
checks, covering all 412 newly mapped URLs; a nonexistent clip returned 404.
Four recovered clips decoded and played to their ended event, including the
historically recovered answer. Public authenticated playback is a separate
observation; no owner browser data or progress was cleared or merged.

Exact local receipts are `result.json`, `gates-receipt.json`,
`python-tests-receipt.json`, `worker-route-audit.log`, `recovered-playback.json`
and `history-applied.json` under `output/audio-gap-repair-2026-10-23/`.

Release reproducibility: detached Git snapshot
`e83165f14cc42c614b98d76adaf2fcc51fbb8873` passed a fresh `npm ci` and full
production build outside the working folder. Exact approved recipe and public
catalog hashes survived checkout; all 57,195 served clips passed the build's
hash checks and lossless packaging. No ignored environment or voice-generation
files were needed. Logs: `clean-ci.log` and `clean-build.log` in the same receipt
folder. The environment-free clean artifact is verification only; deployment
uses the checked main artifact with the existing sign-in configuration.
