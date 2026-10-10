# Cleanup audit, 10 October 2026

Current playback imports `src/audio-assets.json` and resolves `/audio-v2/` URLs.
The maintained generator, screening, mastering, repair and deployment scripts do
not depend on the legacy removal candidates below. Outside references are
historical QA/prompts/licence notes, synthetic test fixtures, and `/audio/`
MIME-type regular expressions in browser tests. Historical records are retained.

## Completed

Removed two reproducible, ignored source archives, totalling 1,300,410,160 bytes
(1.21 GiB). Their ZIP commit comments resolve to existing ancestor commits, and
their full file lists match those commits. Build and deployment logs remain.

- `output/gates/level-2-release-clean.zip`: commit
  `f927e9bd745edc4bee786ba161cd298d882ca0e2`, 19,539 files.
- `output/gates/level-3-release-clean.zip`: commit
  `bb74396c7e67c5d7694c9e65a0eb508dd0289c2a`, 31,635 files.

Either can be recreated using `git archive --format=zip -o <archive> <commit>`.
These were generated copies; no learner data, source content or audio was removed.

## Approved legacy removal

The initial automatic approval review rejected deletion with “blocked by policy”.
The owner subsequently approved this exact list directly in chat. The 395 tracked
files below were then removed through Git, which preserves their history. No
forced removal or unrelated deletion was used. Their staged path set exactly
matches the audited list; all protected catalog/provenance checksums are unchanged.

395 tracked files, 3,514,408 bytes (3.35 MiB):

- `public/audio/`: 353 obsolete Kokoro clips, 3,179,040 bytes.
- `public/audio-reactions/`: 23 obsolete reaction clips, 213,720 bytes.
- `src/audio-reactions.json`: obsolete index, 1,730 bytes.
- The following 18 retired scripts, 119,918 bytes:
  - `scripts/generate-audio.py`
  - `scripts/generate-audio-cosy.py`
  - `scripts/prepare-voice-review.py`
  - `scripts/audition-sayo-b-refinement.py`
  - `scripts/audition-sayo-lower-clean.py`
  - `scripts/audition-sayo-lower-options.py`
  - `scripts/audition-sayo-lower-register.py`
  - `scripts/audition-sayo-qwen.py`
  - `scripts/build-voice-review.py`
  - `scripts/generate-sayo-candidates.py`
  - `scripts/generate-sayo-delivery-audition.py`
  - `scripts/generate-sayo-range.py`
  - `scripts/generate-sayo-reference-followup.py`
  - `scripts/generate-voice-compare.py`
  - `scripts/prepare-sayo-anchor.py`
  - `scripts/review-sayo-audio.py`
  - `scripts/review-sayo-b-refinement.py`
  - `scripts/review-sayo-qwen.py`

The scripts describe past voice auditions. Their source can be restored from
commit `5803ce6d0c651e19de91333c19d86d2f407f5bd9`. Their archived provenance,
approved reference recordings and attribution must remain available.

## Keep

- All `public/audio-v2/` clips, including released compatibility clips for cached
  app versions. Before cleanup: 55,127 MP3s, 1,979,752,948 bytes. Sorted filename
  and SHA-256 inventory digest:
  `a131b1e9a87794f7c5bebe61458da42efbcb3fc942153d8f91c081f4e820fb77`.
- `src/audio-assets.json`, the installed/provenance/compatibility ledgers and
  `content/voices/approved-b-half/`, including the exact approved synthetic
  sources. No pitch, encoding, mood or mapping changes are part of cleanup.
- `.cache/sayo-qwen-approved/`: generation sources, carriers, retry receipts and
  screening evidence needed for repair and reproducibility.
- `.models/` and `.voice-design-env/`: local generation and screening tools.
- `output/` voice backups, audition evidence, native-review records and gate logs.
  Blanket deletion is unsuitable.
- `dist/` and `.deploy-dist/` while checking production or deploying. Both are
  generated and recreated by the build; deleting them offers temporary savings.
- Private reference MP3s and all learner databases, storage keys and progress.

Local audit receipts are in `output/cleanup-audit/`. Validation uses the unchanged
eight-gate course runner with only its output location redirected, so previous
batch evidence is not overwritten. This pass also preserves the existing owner/
Claude CSS, accessibility-test and test-performance edits.

## Initial validation result, before legacy removal

All eight gates passed on 10 October 2026: packs/pinyin/readability, types,
content including exact current/retained audio hashes, 190 unit tests, playback
review, 45 development browser tests, production build and four actual production
offline/update tests. The four production-only cases were skipped in development
and then run successfully against the production build. Fifteen Python helper
tests for installation, screening and retention also passed. No gate was weakened.

The protected catalog, provenance, compatibility and approved-profile checksums
match the pre-cleanup snapshot. All 55,127 current/retained MP3s remain present;
26 approved source/reference records match their hashes and the generator model
remains available. The build confirms all 144 units and 16,822 bundled audio texts
are unchanged, and packs 55,127 clips into 334 lossless deployment chunks. Existing
478 owner-deferred texts remain explicit device-speech exceptions; this cleanup
introduced no new missing audio. No public deployment or learner-data operation
was needed for removal of the ignored archives.

## Post-removal validation

All eight gates passed again after the 395 tracked removals, finishing at
2026-10-10T17:06:57Z. The source fingerprint stayed unchanged throughout:
`43c11aefa5d252717c87db9d65a2671b2156dac06979e258c4aeb4ca65dd1f57`.
Evidence: `output/cleanup-audit/post-removal-receipt.json` and its gate logs.
Results: 190 unit tests, 45 development browser tests and four actual production
offline/update tests passed. Packs, pinyin, contextual pronunciation metadata,
word readability, types, content/audio checks, playback review and build passed.

The production package now uses 2,808 static assets instead of 3,184, exactly
376 fewer obsolete MP3s. Its 55,127 current/retained clips still occupy 334
lossless audio chunks (1,888.0 MiB); their original MP3 bytes and protected audio
catalogs did not change. The installed data check confirms the same 144 units,
16,822 bundled audio texts and existing explicit device-speech exceptions.
Both approved branding exports were verified during the build. No new missing
audio or learner-data operation was introduced.

## Release

Cleanup and the previously reviewed polish were committed as
`d331f54bd8a45a8967349cfb82f9516171fdb813` and pushed to origin/main.
The tested source fingerprint also matched after committing. Wrangler activated
`586b9f7e-988c-46a6-82a9-d53fc5245d70` on kiyo.gbaonvo.com at
2026-10-10T17:07:56Z; the deployment list confirmed 100% traffic on that version.
Only 11 changed app assets uploaded; 2,797 assets, including all current audio
chunks, were reused.

The normal public Edge tab played 还记得吗？ through to completion without a
warning after deployment. It still loaded cached `index-CmSBKDbo.js`, while the
deployed build uses `index-CTVQbk6Q.js`. This verifies retained audio URLs on the
older public shell; fresh-shell behavior is verified by the local production
tests, not claimed as a new public-browser verification. No site data was
cleared, Access policy changed, or learner progress merged.
