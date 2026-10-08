# Project C implementation log

Owner approved all 96 units and removed intermediate review stops on 5 October 2026. Each batch is accepted only after its generated audio and all requested gates pass. Coverage means explicit curriculum introduction, never learner mastery or native certification.

## Batch 01 — s1-u13 to s1-u16 — prepared, acceptance pending

- Units: A friend of a friend; Want to come along?; Wait, which one?; This one or that one?
- Allocation: 72 vocabulary entries, 36 explicit characters, eight grammar cards, four original supplementary scenes/verses. Vocabulary comes from the C1 official remaining inventory; levels are read from the HSK lookup.
- Grammar: 一05 personal pronouns; 一24 subjects; 一03 想/要; 一13 还/也; 一04 question words; 一46 question-word questions; 一06 demonstratives; 一27 attributives. Cards introduce the stated inventory with examples; this does not establish learner mastery.
- Practice: each unit has a 12-turn dialogue, three comprehension questions, a purpose-led reading with three questions and gap fill, eight listening/exam-format tasks, pragmatics and a scripted role-play. Every vocabulary entry occurs in at least two distinct connected practice lines.
- Self-review fixes: removed early 把 constructions; added missing support glosses; repaired citation pinyin and neutral tones; changed an ambiguous pronoun-error example to an unmistakable singular/group mismatch; added gap-fill distractors; gave new characters usage notes with local stroke-data counts rather than invented etymology.
- Bootstrap verification: all 16 existing/new packs compiled; new word readability 99%, 97%, 100%, 100%; pinyin check had zero lines to fix before the explicit-character additions; targeted allocation/practice/audio-manifest tests passed (three tests). These are preparation checks, not the final batch gates.
- Audio: local approved B-half generation completed, but installation is blocked by the pronunciation screen described below. Supplementary lines and their full assembled readings are explicitly collected by the manifest. No human listening or native review is claimed.
- Existing checker warnings: several words were encountered in earlier/base material although the conservative C1 ledger did not count a standalone introduction. They are explicitly consolidated here. Existing earlier-unit thin-context warnings remain visible; no gate has been weakened.

### Native-review flags

- s1-u13: check the country-reference examples and the contextual gloss of 学院 (college/institute, not a foreign qualification). School stages do not assert a universal age.
- s1-u14: the supplementary verse is original rhythmic reading, not a claim that it fits a melody; check 爱看 as fondness. Invitation acceptance/refusal must remain natural.
- s1-u15: check rapid successive clarification questions. 刚才 is a glossed support word, not claimed as a completed grammar target.
- s1-u16: the original verse intentionally omits 是/很 in short poetic lines; ordinary conversation examples retain full forms. Borrowing and demonstrative contrasts require shared visible objects.

### 6 October verification — not accepted; audio blocker

- `npm run packs`: passed, 16/16 packs; the four new units have word readability 99%, 97%, 100%, 100%. `npx tsx scripts/check-pinyin.ts`: 4,522 dictionary matches, zero lines to fix. Eight character entries lack dictionary entries and remain explicitly reported by the existing checker.
- `npx tsc -b`: passed after fixing the image-readiness helper's DOM type.
- `npm test`: 117 passed, one failed: the installed-audio catalog test rejects new task lines because the staged audio has not been installed. No test was weakened or skipped.
- `npm run validate:content`: curriculum validation passed (369 phrases, 102 characters, 41 readings, 60 lessons, 1,310 steps); its required installed-audio check failed. `npm run build` failed at the same required audio check before producing a release.
- Raw generation: 3,949 current jobs completed; automatic screening finished. Failed individual moods can use a screened same-text take of the same identity, with recorded pronunciation-first substitutions. Three texts have no accepted take at any required mood, so `scripts/master-audio-qwen.py --install` refuses installation before expensive mastering. The existing final refusal remains as a second check.
- Real repair attempts: generated new clear takes with natural carrier context; discarded a carrier extraction that cut a multi-clause sentence; regenerated exact full sentences; then regenerated the three child-reference sentences with a natural pause after 小孩儿. Automatic transcripts still consistently omit 儿. This may be an ASR orthography limitation, but it has not been established as correct rhotic pronunciation. The erhuā equivalence gate was not broadened to dismiss the failures.
- Hardened the screening check: a long cropped sentence cannot be accepted just because its full carrier contains the expected ending. Carrier-based equivalence is limited to short targets; longer targets must match their cropped clip's own transcript. A direct check confirms `还有菜` still fails as a transcript of `我有米饭，还有菜。`, while a complete `我想先吃饭。` passes. The blocker was rechecked after this stricter guard.
- Content/audio fixes: bound glyphs 什/么/以/息/儿/孩/弟 keep meaningful word-context speech; corrected the subject-order mistake to `是学生我的朋友。` → `我的朋友是学生。`; replaced the awkward `是，我想先吃饭。` response with the natural `我想先吃饭。`; punctuation and authored pinyin follow the updated sentences.
- Diagnostic latest takes, with the approved profile's selected pitch processing and measured loudness: `output/course-audio-blocker/index.html`; source hashes, screen results and encoding receipts in its `provenance.json`. These are not installed app assets or a native listening certification.
- Current **draft-inclusive** GF2021 explicit vocabulary coverage: L1 261/500, L2 26/772, L3 6/973. Draft-inclusive explicit characters: 99/300, 1/300, 1/300. The new grammar crosswalk has not been accepted or expanded while the batch is blocked. Coverage is introduction evidence, never mastery.
- Protected file SHA-256 audit passed for `src/packs.ts`, `src/dictionary.ts`, `src/Watch.tsx`, `src/ReadingDrill.tsx`, `src/drill.ts` against the C2 start snapshot.
- Branding requested during this run is implemented locally, with the selected leaning signature and a square portrait of the existing waving pose. Desktop/tablet/mobile/320 px captures were checked; source pixels and icon PNG exports were verified. It has not been deployed with an incomplete course build.
- `npx playwright test`: 29 passed, four failed, three conditionally skipped by the unchanged production-only tests (6.5 minutes). All four failures are the new supplementary-reading playback checks: their reader routes and visible content loaded, but Read aloud had no installed bundled mapping and could not request `/audio-v2/`. Existing navigation, accessibility, HSK, word-tap/reaction speech and isolated fake-cloud sync checks passed. The three production service-worker/update/offline checks require a successful production build and remain unverified; they are not counted as passes. No live Google/Supabase verification was attempted in this course run.

#### Exact unresolved pronunciation lines for native review

1. s1-u13 vocabulary 小孩儿 example: `那个小孩儿，是我妹妹。`
2. s1-u13 supplementary scene, turn 1: `这个小孩儿，是你的学生吗？`
3. s1-u13 listening task s1-u13-t2: `那个小孩儿，今年八岁。`

Other native-language uncertainties remain those listed above: 学院 / foreign-country references, invitation register and original rhythmic writing, clarification-dialogue pacing, and poetic omissions in the original u16 verse. They are not marked as reviewed.

The owner's allowed stop condition applies: a required audio gate remains failed after real regeneration attempts. **Four units are drafted, zero new batches accepted; 92 units remain unwritten. No deployment or push has been performed.**

### 6 October continuation — Batch 01 accepted

- Repaired the child-reference blocker without broadening the pronunciation screen: spoken practice now uses 孩子. Because 孩子 was already allocated, the former 小孩儿 vocabulary slot introduces 儿子 instead; the three child-reference sentences and the son example were regenerated. The northern 小孩儿 form remains a recognition-only usage note and does not earn standalone vocabulary coverage.
- Added concrete retrieval tasks for 一02, 一15, 一21 and 一34 using earlier screened course sentences. Each unit now contains nine tasks. Additional previously owned subject, modal, question and demonstrative families recur in the connected practice; native review remains pending.
- Hardened audio installation so accepted clips can install while unresolved texts still produce a nonzero exit and fail release validation. Two fixture tests verify this behavior. Screened exact-text alternate takes retain the same Sayo identity; failed speech is never installed as an accepted take. Assembly reuse checks source and output hashes.
- All final gates passed: packs 16/16 with zero pinyin fixes (4,589 dictionary matches; eight explicitly reported characters without dictionary entries), content and installed-audio validation, 118 unit tests, TypeScript, and production build. Browser suite: 33 passed; its three production-only conditional checks were separately run against the final production build and all three passed. Receipts: `output/gates/batch-01/`.
- Installed audio: 1,596 texts, 4,048 files, 62,921,216 bytes. Supplementary reading playback was verified through real bundled-audio HTTP requests without a device-voice fallback. Automatic screening is not a native listening certificate.
- Accepted GF2021 introduction coverage: vocabulary L1 261/500, L2 26/772, L3 6/973; explicit characters 99/300, 1/300, 1/300. Eight new grammar-owner cards were crosswalked to their explicit inventories; coverage never means learner mastery.
- Native-review flags above remain open; specifically retain the recognition note 小孩儿 (xiǎoháir), college/school wording, invitation register, clarification pacing, and intentional poetic omissions. The three former unresolved spoken lines are superseded by screened 孩子 lines.
- Branding and dictionary/drill production dependencies remain local, including the actual audio catalogs and files. Four new units are accepted; 92 units remain to be accepted. No deployment or push yet; the owner requested deployment at the end of the full run.

## Batch 02 — s1-u17 to s1-u20 — prepared, audio and acceptance pending

- Units: Cooking for the group; Our shared kitchen; Whose charger is this?; What are you doing now? Allocation: 69 vocabulary records and 59 explicit characters. Levels and pronunciation alternatives are read from the existing official lookup; this batch is not yet accepted.
- Grammar owners: 一07 numbers including 二/两 and 半; 一23 quantities; 一08 the eight classifiers; 一37 possession and existence with 有; 一20 的/地; 一26 objects; 一11 temporal/progressive adverbs; 一42 all listed progressive forms, including action + 呢 without 在. Owner cards explain the inventories rather than claiming mastery from incidental use.
- Retrieval task 9 brings back 一40 in u17, 一02/一41 in u18, 一15/一43 in u19, and 一21/一47 in u20. Existing question-word questions recur in u17/u20; ownership and demonstrative phrases recur in u18/u19; quantities recur in u19, and existence/location in u20. Each unit has eight mixed tasks plus this explicit retrieval task, twelve dialogue turns and three questions, a purpose-led core reading with three questions/gaps, and an original supplementary scene or verse.
- Self-review: reviewed Chinese/English/Vietnamese against the communicative goal; kept money amounts arithmetically consistent (three buns at 2.50 = 7.50), removed premature disposal/complement constructions, checked gifts versus purchasing in 得到 contexts, and made the charger’s unknown owner explicit. Replaced the out-of-ledger 口 vocabulary allocation with 手; 口 remains explicitly taught in the classifier grammar card. Corrected glyph readings 干 gān, 地 dì and 得 dé independently of particles/verbs.
- Support words have actual meanings in the tap glossary: 只, 栋, 厨房, 商店/小店, 房/住, 充电器/借/送, 答案/白色, 清楚/大声/着急/事. Some passages still produce the existing “many glossed characters” warning; it is recorded, not suppressed. Bound or ambiguous glyph audio uses 干净, 地上, 得到, 知识, 时候, 电视机, 准备 and 电脑. The standalone vocabulary 地 remains the neutral particle de, not the ground noun dì.
- Preparation gates: packs 20/20, word readability 99%/100%/100%/98%, zero pinyin lines to fix, 6,326 dictionary matches and nine explicitly reported unlisted characters; all three targeted allocation/practice/manifest tests pass. Local generation is in progress. Full content/audio, unit, browser and production checks remain pending.
- Native-review flags: u17 `肉一半做午饭，一半做晚饭。` (portion wording); u18 `洗手间在楼上，洗杯子在楼下。` (intentional clipped verse versus ordinary full sentence); u19 `朋友送我一本书，我得到一本外语课本。` and the longer gift acknowledgment (natural use of 得到); u20 `我读书呢，等一下。` (progressive without 在 and practical delivery). Classifier 口 is restricted to household-member counts. Automatic pinyin/transcript checks do not close these flags.

### Batch 02 acceptance — 6 October

- Accepted s1-u17–s1-u20: 69 vocabulary records, 59 explicit characters and eight grammar-owner families above. Coverage is introduction evidence, never learner mastery. GF2021 words: L1 330/500, L2 26/772, L3 6/973; characters 158/300, 1/300, 1/300.
- Applied audio repairs: isolated words regenerated with natural carrier context, and 够 stays inside 够用 for reader lookup. Replaced the two short, irrelevant price distractors 两块五毛 with 三块钱 after real failed regeneration attempts; the valid full-context price examples remain. Added 认真地读 as a dictionary-checked grammar example. The phonetic comparison now uses authored neutral de only at an exact 地→的 position; ground dì, missing syllables and 小孩儿→小孩 still fail. Two fixture tests cover those distinctions. No erhuā whitelist change.
- Installed 1,961 texts / 5,067 files / 84,507,300 bytes with complete requested mood coverage, source/output hashes, decoding and loudness checks. Failed individual moods use a screened alternate of the same identity with substitutions recorded; no text remains unresolved. Automatic ASR equivalence is not tone or native-language certification.
- Required final gates passed: packs 20/20 with zero pinyin fixes and 99%/100%/100%/98% new-unit word readability; content/audio, types, 119 unit tests, production build. Browser first run: one reply field detached during a concurrent build; focused rerun passed, then the full stable run passed 33 tests. Its three production-only conditions were separately run against the built preview: all three passed. Five protected files still match their C2 start hashes. No test was changed to dismiss a failure.
- Receipts: output/gates/batch-02-*.log. All native-review flags listed in preparation remain open, including the gift wording, quantity wording and original clipped verse. No live Google/Supabase verification in this course run. Eight new units accepted, 88 remaining; no deployment before completion.
- Editorial preflight for later units caught the second GF2021 还 entry: it is huán “return”, not another introduction of hái “still”. Unit 30 source now explicitly teaches the correct reading/verb sense with return-book contexts. Suffix 子/们 source annotations receive credit only from explicit neutral suffix introductions with a source note, never from compound exposure; nine focused audit/plan tests passed.

## Batch 03 — s1-u21 to s1-u24 — prepared, not accepted

- Units: A realistic weekday routine; correcting the class day and time; finding the right bus/entrance; introducing family and friends. Allocation: 68 vocabulary records, 68 explicit characters, nine grammar-owner cards. Owners: 一12 habits/repetition, 一28 circumstance adverbials, 一14 negation, 一48 A-not-A, 一16 location 在, 一29 verb predicates, 一44 dates and clock time, 一17 跟/和 accompaniment, 一19 coordination and choices. Earlier permission, quantities, progressive forms and compliments recur in concrete task 9 retrievals.
- Applied self-review fixes: distinguished 对不起 as a verb and 这边/那边 as pronouns; checked six-o’clock/eleven-o’clock routine details, changed a misleading “tomorrow” correction to the actual weekday/class-time correction; checked 2026-10-06 as Tuesday and boarding/meeting times separately; kept 男朋友/女朋友 separate from 男人/女人 and 男孩儿/女孩儿. Added real glossary meanings for class periods, safety, vehicle/people/tree classifiers, calendar changes and family generations instead of hiding unfamiliar characters.
- Preparation: 24/24 packs compile with 97%/96%/99%/100% new-unit word readability and zero pinyin fixes (8,156 matched dictionary syllables; nine unlisted glyphs reported). The current generation still contains the earlier 二〇二六 spelling; the source now uses 二零二六 so it will be rebuilt and its changed lines regenerated before acceptance. Raw audio is not installed or treated as verified.
- Playback repair: vocabulary entries keep their own reading instead of taking the glyph default. Neutral 地 stays in 认真地读, ground 地 in 地上, dry 干 in 干净, do 干 in 干什么, return 还 in 还书, and suffixes in actual words. The new browser regression currently correctly fails for a not-yet-installed context clip; acceptance requires it to pass with bundled audio responses.
- Native-review flags: u21 `下课后，我和朋友认真地读课文，再说五分钟汉语。` (study-plan wording); u22 `你记星期一晚上七点，那间房不大，人不多。` (clarification pacing); u23 bus-stop/boarding announcements and the original clipped travel verse; u24 `男人是朋友，不是男朋友。女人是老师。` (intentional contrast in an original verse), 男孩儿/女孩儿 delivery and family-reference/register choices. Automatic checks do not certify tone or native naturalness. No native approval recorded; full acceptance gates pending.

### Batch 03 continuation — unresolved speech gate, 6 October

- Rebuilt the date lines as 二零二六年十月六日. The narrowly scoped year-digit comparison accepts the same date written as 2026年10月6日; different years/days still fail. Three screening fixtures and two accepted-only installation fixtures pass. No erhuā acceptance whitelist was broadened.
- Four real repair rounds were attempted after initial generation: natural carriers, deterministic decoding, speaker-only conditioning with the identical approved fixed embedding, then a fresh seeded higher-diversity speaker-only pass. Standalone 男孩儿 now has an accepted exact-transcript take. Ten other texts still fail the original automatic screen. An independent local Whisper large-v3 diagnostic on the preceding round also omitted their 儿 endings. That is an unresolved pronunciation/transcription ambiguity, not evidence of native approval.
- Accepted speech installed locally: 5,970 files, 104,119,896 bytes. Thirty requested mood mappings for ten unresolved texts and fifteen mappings for five dependent assemblies remain absent; the installer exits 1 and the content/build audio gate correctly rejects this state. The printed raw-file missing count of zero does not mean complete accepted mapping coverage.
- Final packs check passes 24/24 with 97%/96%/99%/100% word readability for this batch, 8,156 dictionary matches, nine explicitly reported unlisted characters and zero pinyin lines to fix. TypeScript passes. `validate:content` checks curriculum successfully (539 phrases, 229 characters, 65 readings, 76 lessons, 1,650 steps) but exits 1 on required audio mappings; production build also exits 1 at that gate. Final unit and targeted playback results are recorded below when complete. A failed production build cannot verify production-only service-worker checks.
- All five protected files retain their C2 start SHA-256 hashes. No database name, stored learner data, live services or npm dependencies changed. No commit, push or deployment in this continuation. Branding is prepared locally; it has not shipped from this incomplete course run.
- Accepted new units remain s1-u13–s1-u20 (eight). s1-u21–s1-u24 are compiled drafts, not accepted. Editorial Python sources for s1-u25–s1-u30 and s2-u01–s2-u04 are prepared but not serialized/accepted. Eighty-eight of the requested 96 units still await completion. Accepted GF2021 vocabulary introduction coverage remains L1 330/500, L2 26/772, L3 6/973; explicit characters 158/300, 1/300, 1/300. Do not count draft-inclusive coverage as accepted or as learner mastery.
- The owner's explicit stop condition applies: a required gate remains failed after real repair attempts. Preserve the raw takes, source packs, screening receipts and failed gate logs. Deployment stays blocked rather than shipping missing audio.

#### Exact unresolved spoken texts — native listening/phonetic review still open

1. `没事儿，明天再来。`
2. `没事儿，再记一次。`
3. `女孩儿`
4. `那个男孩儿是我弟弟。`
5. `那个女孩儿是我妹妹。`
6. `没事儿。你先等一下，我看日历。`
7. `没事儿，今天不用等老师，明天也别等。`
8. `那边的男孩儿和女孩儿呢？`
9. `弟弟是那边的男孩儿，妹妹是旁边的女孩儿。`
10. `男孩儿跟女孩儿，小朋友在楼下玩。`

Earlier native-language flags remain open: school/college and country references, invitation register, clarification pacing, original poetic omissions; u17 portion wording, u18 clipped shared-kitchen verse, u19 得到/gift acknowledgment, u20 progressive 呢; and the specific Batch 03 lines above. No line is marked native-reviewed.

#### Final gate receipts for the blocked continuation

- `npm test`: 120 passed, one failed; the unchanged catalog assertion rejects a missing required task-audio mapping.
- Focused Playwright playback/regression suite: four passed, one failed. The three supplementary readings u21–u23 and the taught-reading word-tap test passed with bundled audio requests. u24's scene loaded correctly but timed out waiting for an audio-v2 request because its assembly contains an unresolved spoken line. No timeout or assertion was loosened.
- Logs: `output/gates/batch-03-final-packs.log`, `batch-03-final-types.log`, `batch-03-final-content.log`, `batch-03-final-unit.log`, `batch-03-final-playback.log`, `batch-03-final-build.log`, `batch-03-final-master.log`, and `batch-03-repair-4-{generation,screen}.log`.
- The full browser suite and production-only checks were not claimed as verified for this failed release. Earlier complete checks apply to Batch 02 only. Resume by resolving the exact ten speech texts above, rebuilding/installing the audio plan and running every batch gate; do not deploy the current partial catalog.

### Owner-approved audio policy and Batch 03 acceptance — 6 October

- The owner directly approved all three handoff points: one real audio repair followed by a dated device-speech exception; continued HSK 1–3 course batches with no review stops and deployment after each completed level; original rotating exam banks with about 60 checkpoint/30 sample items per level, retaining old IDs/results. Existing dictionary/drill/branding/course changes are to be committed now. This supersedes the earlier audio-only blocking requirement; every other content, pinyin, readability, answer-key, test and build gate remains strict.
- The ten existing exceptions have individual date/reason/repair receipts and remain `reviewed: false`. Assemblies are derived from their actual manifest parts, not arbitrary substring matches. Accepted audio stays installed; failed takes never become accepted clips. Four mastering fixture tests cover normal success, unlisted failure, documented deferral without installation, and an unrelated exception that cannot hide missing speech. A separate unit test verifies exact-text/assembly scoping.
- Accepted s1-u21–s1-u24 under that explicit policy: 68 vocabulary records, 68 explicit characters, nine grammar-owner cards and concrete retrieval tasks. Native-review flags above remain open. Coverage: GF2021 vocabulary 398/500, 26/772, 6/973; characters 226/300, 1/300, 1/300; level-1 grammar 33 introduced, 6 partial, 9 unmapped. Introduction does not mean mastery or native certification.
- Packs/pinyin, content with declared audio fallback, types and build pass. Initial full unit suite: 121/121; the newly added policy/coverage/plan tests pass (10), and installed-catalog/policy tests pass (6). Full browser run: 33 passed, three production-only conditions, one failed new fallback fixture; corrected the mock utterance constructor, then all four supplementary-reader tests passed, including actual device-speech dispatch for the deferred scene. Its navigation/pinyin checks were retained. The three production-only tests were separately run against the final build and all passed. Final full unit receipt accompanies the commit.
- Build precache: 446 entries / 5,327.25 KiB; dictionary shards and the 104,119,896-byte audio library are runtime data, not installation precache. No live Supabase or Google sign-in test in this course batch. Protected A/B files remain unchanged from their C2 snapshot.
- Current new-course acceptance: 12/96 units, through s1-u24. The previous blocked status is historical and revoked by the owner's approved audio policy. Continue with s1-u25–s1-u28, then s1-u29–s1-u30, and the approved level-2/3 outline; retain all native flags and explicit audio exceptions.

### Batch 04 acceptance — 6 October

- Accepted s1-u25–s1-u28: 68 vocabulary records, 56 explicit characters, ten grammar families. Owners: 一09 degree, 一30 adjective predicates, 一35 exclamations, 一18 比, 一38 comparisons, 一10 collective adverbs, 一39 parallel clauses, 一22 particles, 一33 question forms, 一45 吗. Each unit includes an original scene/verse and concrete retrieval of earlier instruction.
- Self-review fixes: ordinary meanings for 普通/练/但/另/湿/让/选/发; added an actual 看见 context; corrected 先不知道 to 还不知道 and a misleading Mandarin-study adjective example. Compared localizers, comparison reference sets and dialogue details; no invented grades or readiness claims.
- All required gates passed: packs and pinyin with no fixes, word readability at least 95%, types, content/audio, 130 unit tests, 34 browser tests, production build and the three separately required production browser checks. Receipts: output/gates/batch-04-final-*.log. The three conditional production tests in the dev run were run against the final preview, not omitted.
- Installed 6,839 screened/mastered files, 125,917,300 bytes. After a real repair round, nine additional exact texts remain documented device-speech exceptions (19 direct exceptions total; 27 texts including dependent assemblies). Failed takes are not installed and exceptions remain reviewed:false. These are explicit owner-approved audio exceptions; other gates remain strict. Automatic ASR is not native tone certification.
- Native flags: reference sets for 最好/最好看; 饭店 restaurant versus hotel; formal 小姐; clipped original poetry; 一块儿/一下儿 pronunciation; directional/polyphonic verbs. Exact unresolved speech is in content/voices/audio-deferred.json, with dated reasons and repair receipts. Earlier flags remain open.
- All five protected A/B files match their C2-start hashes. No learner data or database name changed, no dependency or paid service added. New-course acceptance is 16/96; 80 remain. Level 1 deployment follows its final two units.

### Batch 05 acceptance — 2026-10-06

- Accepted s1-u29, s1-u30: 34 vocabulary records, 18 explicit characters. Grammar owners: 一01, 一31, 一25, 一32, 一36. Each includes original media writing and retrieval.
- Self-review and applied fixes: Checked map orientation, return versus ongoing-study readings of 还, suffix 们/子 contexts, north-gate meeting constraints, broken-cup refusal and reader answer keys. Corrected source aliases and retained actual gloss support. Native checking of erhua, poetic omissions and map-localizer phrasing remains pending.
- All eight required gates passed; exact receipts and test counts: output/gates/batch-05-final-*.log. Packs/pinyin and word readability remain strict; production-only checks ran separately against the final preview.
- Audio: 35 direct dated exceptions after a real repair. Failed takes remain uninstalled, reviewed:false. Dependent assemblies use the same explicit policy. Automatic transcript screening is not native tone certification.
- Native-review flags remain open:
  - s1-u29: AI-assisted draft; native review pending. GF2021 grammar families: 一01, 一31. Native check: 北门 and east-side entrance geometry, localizer shortening on signs, and relative versus cardinal directions. No claim that every map is north-up. Planned retrieval 一12 / 一28 / 一17 / 一19 / 一10 / 一39: 我常在家读书，她常常上午学习。, 爷爷和奶奶都来。, 我们一边走路，一边聊天。.
  - s1-u30: AI-assisted draft; native review pending. GF2021 grammar families: 一25, 一32, 一36. Native check: 小孩儿 and 面条儿 rhotic pronunciation; short poetic omissions and the last line’s metaphor. 们/子 are explicit neutral suffix entries, never standalone spoken zǐ. 着 is recognized as a continuing state here; its full grammar owner is s2-u28. Planned retrieval 一14 / 一48 / 一09 / 一30 / 一35 / 一22 / 一33 / 一45: 星期日有没有课？, 真好看！, 我可以进去吗？.

### HSK 1 rotating-bank release checks — 6 October

- The final two course units are accepted; all 30 HSK 1 units now introduce GF2021 level-1 words 500/500, characters 300/300 and grammar 48/48. This is introduction evidence, not learner mastery or native approval. New-course acceptance is 18/96.
- Added 54 original items without changing the legacy 36 IDs/keys, yielding exactly 60 checkpoint and 30 sample items. Reading, listening and adapted word-order formats; all four answer positions. Corrected an ordering distractor and actual legacy pool counts. Native ambiguity/pronunciation flags: prompts/research/exam-bank-review.md.
- Rotation counts displayed questions, selects unseen first, then least-seen/oldest. Existing runs/backups retain their schema, identifiers and grades. Found and fixed a backup export aliasing the default settings object. A restored listening checkpoint hides its transcript until explicit help, and supported status survives reload.
- Character speech keeps 着 inside 门开着，请进。 and 场 inside 机场, with 右边/后边 contexts. The approved synthetic voice identity remains unchanged.
- Final gates all passed: packs/pinyin (0 fixes), types, content/audio, 132 unit tests, 35 browser tests and production build; the three conditional production tests passed separately. Receipts: output/gates/batch-51-final-*.log. Verified mobile/desktop exam captures at 1440/768/375/320 px and automated WCAG AA checks.
- Installed 7,508 audio files, 138,642,352 bytes. The content gate covers 3,059 texts; 47 direct/dependent texts use the explicit dated repair-and-deferral policy, never marked reviewed. Precache is 485 entries / 5,741.72 KiB; dictionary/audio are runtime data.
- No protected A/B file, learner database name, dependency or live-service configuration changed. No new live Google/Supabase test was performed during these local course gates.

### HSK 1 release — 6 October 2026

- Source commit `30556cc` pushed to `origin/main`; a detached clean checkout passed `npm ci` and `npm run build`.
- The 30-unit HSK 1 course introduces GF2021 vocabulary 500/500, characters 300/300, grammar families 48/48. This is curriculum evidence, not learner mastery or native approval.
- The practice bank contains 60 checkpoint and 30 sample questions, retaining all 36 legacy IDs. Full release checks: 132 unit tests, 35 browser tests, plus all three production-only browser checks passed.
- The production build preserves the existing Google-only Supabase public configuration. Cloudflare shows successful Git build `30556cc`; the subsequent CLI deployment is `9a350078-4680-4702-b0b7-4d7fedce25d5`, active at 100% on kiyo.gbaonvo.com.
- The existing live browser initially retained its old cached app shell. Deployment is confirmed, but that browser's updated bank and playback are not yet verified. Existing guest progress was not merged, removed or submitted as test learning. No new live sync success is claimed.

### Batch 06 acceptance — 2026-10-06

- Accepted s2-u01, s2-u02, s2-u03, s2-u04: 88 vocabulary records, 36 explicit characters. Grammar owners: 二06, 二37, 二01, 二02, 二75, 二03, 二45, 二05, 二76. Each includes original media writing and retrieval.
- Self-review and applied fixes: Checked invitation conditions, host roles, conditional Saturday plans, restaurant journey versus queue time, and answer keys. Added actual connected-text glosses to keep word readability above 95 percent; fixed source aliases and character contexts. Nine unresolved texts received one real repair; remaining failures are explicitly deferred without native-review approval.
- All eight required gates passed; exact receipts and test counts: output/gates/batch-06-final-*.log. Packs/pinyin and word readability remain strict; production-only checks ran separately against the final preview.
- Audio: 43 direct dated exceptions after a real repair. Failed takes remain uninstalled, reviewed:false. Dependent assemblies use the same explicit policy. Automatic transcript screening is not native tone certification.
- Native-review flags remain open:
  - s2-u01: AI-assisted draft; native review pending. GF2021 grammar families: 二06, 二37, 二01. Native check: northern informal 咱 versus broadly usable 咱们, the metalinguistic phrase card, 群 versus 小组 referents and inclusive invitation register. 读懂 is explicitly recognition-only here; fuller result complements follow later. Planned retrieval 一18 / 一38 / 一01 / 一31: 图书馆比商场安静。, 商场没有图书馆安静。, 北门。学校前边，路的东边。.
  - s2-u02: AI-assisted draft; native review pending. GF2021 grammar families: 二02, 二75. Native check: 请求 versus everyday 请 in the gift context, 随便 used for careless guessing, bottle-to-take-water request, regional host/guest expectations, and clipped original verse. No food restriction is treated as a medical diagnosis. Planned retrieval 一10 / 一39 / 一25 / 一32 / 一36: 我们一边走，一边聊天。, 我们都想走，有些朋友想跑。, 这是学校，是我们学习的地方。, 今天星期六，我二十岁。, 桌上是书，不是饭。, 我有书，也喜欢读书。.
  - s2-u03: AI-assisted draft; native review pending. GF2021 grammar families: 二03, 二45. Native check: avoiding overly formal 请求 in everyday refusals, 心情 versus temporary physical 难受, how direct 不愿意 sounds, and original scene’s dry reassurance. Rest is ordinary social advice, not a medical assessment. Planned retrieval 一22 / 一33 / 一45 / 二06 / 二37 / 二01: 明天考不考？上午还是下午？, 咱们自己先看，小组的书读懂了吗？, 你可以去，他可能会来。大家来了？开始吧。, 你在网上买的吗？, 书和本子，新的书，读书，读懂，大家来了。, 我在家，你呢？.
  - s2-u04: AI-assisted draft; native review pending. GF2021 grammar families: 二05, 二76. Native check: collocations for customer service and dissatisfaction, the nominal use of 快餐/外卖, clipped original verse, and exactly which time interval 多久 refers to. No restaurant recommendation, reservation or objective star rating is claimed. Planned retrieval 一01 / 一31 / 二02 / 二75: 北门。学校前边，路的东边。, 我该带什么？你应该先问主人。, 六点半来，好吗？带书怎么样？, 我带两瓶水，可以吗？行吗？.

### Batch 07 acceptance — 2026-10-06

- Accepted s2-u05, s2-u06, s2-u07, s2-u08: 88 vocabulary records, 36 explicit characters. Grammar owners: 二04, 二11, 二52, 二07, 二38, 二08, 二41, 二46, 二09, 二73. Each includes original media writing and retrieval.
- Self-review and applied fixes: Added a second distinct context for 那么; preserved task budget and actual retrieval. Checked clothing comparisons, calendar references, quantity-classifier examples and opinion versus factual information. Corrected the supplementary-reading browser locator to match the exact title. Pronunciation-context word taps retain taught readings. Unverifiable takes had one real repair and exact dated deferral; no native approval is claimed.
- All eight required gates passed; exact receipts and test counts: output/gates/batch-07-final-*.log. Packs/pinyin and word readability remain strict; production-only checks ran separately against the final preview.
- Audio: 51 direct dated exceptions after a real repair. Failed takes remain uninstalled, reviewed:false. Dependent assemblies use the same explicit policy. Automatic transcript screening is not native tone certification.
- Native-review flags remain open:
  - s2-u05: AI-assisted draft; native review pending. GF2021 grammar families: 二04, 二11, 二52. Native check: conversational 回 as a counter, verb reduplication collocations, the recording/event counter contrast, and clipped original practice verse. Counts of listening and completed homework are never a claimed grade. Planned retrieval 一25 / 一32 / 一36 / 二03 / 二45: 今天星期六，我二十岁。, 这是学校，是我们学习的地方。, 我愿意帮忙，但今晚不方便。, 还是星期六去吧，你想喝茶还是喝咖啡？.
  - s2-u06: AI-assisted draft; native review pending. GF2021 grammar families: 二07, 二38. Native check: the degree/manner contrasts, natural use of 表示 and nominal 的 phrases, and the clipped original scene. The corrected day is Saturday; no new clock time is confirmed. Reference letters/stories are original, not real news. Planned retrieval 二06 / 二37 / 二01 / 二05 / 二76: 咱们自己先看，小组的书读懂了吗？, 你可以去，他可能会来。, 为什么选这里？你想去什么样的饭馆？, 怎样去，要多久？, 谁来，哪里见，什么时候走？, 什么菜，几个人，多少钱，怎么付？.
  - s2-u07: AI-assisted draft; native review pending. GF2021 grammar families: 二08, 二41, 二46. Native check: degree descriptions of colours, natural adjective reduplication, fit versus price, and the informal original verse. Dress expectations are specific to the fictional meeting, not a universal etiquette claim. Planned retrieval 二02 / 二75 / 二04 / 二11 / 二52: 我该带什么？你应该先问主人。, 六点半来，好吗？我带两瓶水，可以吗？, 我看了看题目，我们练习练习。, 这段录音听了两遍，答案检查了三次。, 看一场电影，去一回活动，老师拍三下手。, 看看，说一说，再练习练习。.
  - s2-u08: AI-assisted draft; native review pending. GF2021 grammar families: 二09, 二73. Native check: approximate-number ranges, monetary counter register, 分 as divide versus currency 分, 全 as an adverb, and the clipped original verse. Arithmetic is explicit; no actual income, financial advice or exchange rate is supplied. Planned retrieval 二03 / 二45 / 二07 / 二38: 我愿意帮忙，但今晚不方便。, 还是星期六去吧，你想喝茶还是喝咖啡？, 图片这么小，别那样猜时间。, 新的通知还没有，我去问主办方。.

### Batch 08 acceptance — 2026-10-06

- Accepted s2-u09, s2-u10, s2-u11, s2-u12: 88 vocabulary records, 36 explicit characters. Grammar owners: 二10, 二61, 二12, 二47, 二81, 二13, 二58, 二14, 二39. Each includes original media writing and retrieval.
- Self-review and applied fixes: Checked recipient order, counters, venue temperature versus impression, and portion estimates. Added distinct vocabulary contexts with visible glosses; no universal allergy or portion claim. Calendar and comparative retrieval remain separate from current assessment.
- All eight required gates passed; exact receipts and test counts: output/gates/batch-08-final-*.log. Packs/pinyin and word readability remain strict; production-only checks ran separately against the final preview.
- Audio: 61 direct dated exceptions after a real repair. Failed takes remain uninstalled, reviewed:false. Dependent assemblies use the same explicit policy. Automatic transcript screening is not native tone certification.
- Native-review flags remain open:
  - s2-u09: AI-assisted draft; native review pending. GF2021 grammar families: 二10, 二61. Native check: service-desk collection wording, gifting register, double-object verb restrictions, and classifier choices. Gifts are voluntary; the original scene is not adapted from a show. Planned retrieval 二05 / 二76 / 二08 / 二41 / 二46: 为什么选这里？你想去什么样的饭馆？, 怎样去，要多久？谁来，哪里见，什么时候走？, 绿的又轻又短，黄的还没干。, 衣服干干净净，鞋也干干净净。.
  - s2-u10: AI-assisted draft; native review pending. GF2021 grammar families: 二12, 二47, 二81. Native check: before/after anchors, approaching-change scope, programme/anniversary counter register, and poetic 今天的时间，别送给明天. All dates and transport remain scenario facts, not live schedules. Planned retrieval 二04 / 二11 / 二52 / 二09 / 二73: 我看了看题目，我们练习练习。, 这段录音听了两遍，答案检查了三次。, 看一场电影，去一回活动，老师拍三下手。, 一万不是一千，一亿不是一百万。, 十多个人，一个多小时。.
  - s2-u11: AI-assisted draft; native review pending. GF2021 grammar families: 二13, 二58. Native check: 好 as a degree adverb, 挺…的, 有一点儿 versus adjective+一点儿, comparative 有…这么, and subjective 难听 phrasing. 温度/分贝 are not interchangeable; no unmeasured acoustic score is asserted. Planned retrieval 二07 / 二38 / 二10 / 二61: 图片这么小，别那样猜时间。, 新的通知还没有，我去问主办方。, 一封信，一件衣服，一条围巾。, 我送你一本书。, 我送给你一本书。.
  - s2-u12: AI-assisted draft; native review pending. GF2021 grammar families: 二14, 二39. Native check: liang as a weight sense separate from numeral 两, restaurant portion conventions, noun-phrase head analysis, ordering register and the original verse. No allergy safety is inferred from a dish name; no universal portion weight is asserted. Planned retrieval 二08 / 二41 / 二46 / 二12 / 二47 / 二81: 绿的又轻又短，黄的还没干。, 衣服干干净净，鞋也干干净净。, 我们等十分钟，七点开始。, 开场以前先坐好，散场以后再出去。, 快要七点了，节目就要开始了。.

### Batch 09 acceptance — 2026-10-07

- Accepted s2-u13, s2-u14, s2-u15, s2-u16: 88 vocabulary records, 36 explicit characters. Grammar owners: 二15, 二20, 二80, 二16, 二62, 二69, 二17, 二74, 二18, 二79, 二78. Each includes original media writing and retrieval.
- Self-review and applied fixes: Checked time-versus-duration, message status, clarification and teasing targets. Corrected contextual 还 to huán when returning books and a pen, preserving hái for still/yet; exact tone delivery remains for native review. Replaced ambiguous syllabic interjections with clearly pronounceable language. Added distinct contexts and recognition glosses. Humour is not evidence of agreement.
- All eight required gates passed; exact receipts and test counts: output/gates/batch-09-final-*.log. Packs/pinyin and word readability remain strict; production-only checks ran separately against the final preview.
- Audio: 67 direct dated exceptions after a real repair. Failed takes remain uninstalled, reviewed:false. Dependent assemblies use the same explicit policy. Automatic transcript screening is not native tone certification.
- Native-review flags remain open:
  - s2-u13: AI-assisted draft; native review pending. GF2021 grammar families: 二15, 二20, 二80. Native check: 经过 versus 到站, the range of 才/都/就/正好, 该…了, clipped driver announcements and the original scene. No route, transport estimate or message delivery is asserted beyond the written scenario. Planned retrieval 二09 / 二73 / 二10 / 二61: 一万不是一千，一亿不是一百万。, 十多个人，一个多小时。, 一封信，一件衣服，一条围巾。, 我送你一本书，我送给你一本书。.
  - s2-u14: AI-assisted draft; native review pending. GF2021 grammar families: 二16, 二62, 二69. Native check: complaint strength of 老/老是; 接着 versus 然后 sequencing; conditional 一…就… and telephone 通. Latest-message details and entry conditions are explicit; no guaranteed instant reply. Planned retrieval 二12 / 二47 / 二81: 开场以前先坐好，散场以后再出去。, 快要七点了，节目就要开始了。, 我们等十分钟，七点开始。.
  - s2-u15: AI-assisted draft; native review pending. GF2021 grammar families: 二17, 二74. Native check: emphatic 就 pragmatics; 正是/真正 senses; 从…角度看 and 对… arrangements; 实在 stressed adverb versus neutral adjective. Do not infer anger or consent from emphasis alone. Planned retrieval 二13 / 二58: 这里挺亮，也很凉快。, 里面比外面响，外面不如里面暖和。, 这里又亮又响，我想换个地方。.
  - s2-u16: AI-assisted draft; native review pending. GF2021 grammar families: 二18, 二79, 二78. Native check: 笑话 verb versus 笑话儿 noun and rhotic delivery; questioning 吧 pragmatics; degree of friend-to-friend teasing and clipped humorous scene. A smile or nod does not substitute for asking about an uncertain interpretation. Planned retrieval 二14 / 二39: 四个人，其中一个只要水。, 大多数同意，不等于所有人都同意。, 其他人还没选，先别下单。.
- Gate repair for batch 09: investigated a transient gallery navigation timeout, confirmed all 17 reactions in isolation, corrected the cloze container from p to div to eliminate invalid nested audio-control markup, and reran the full suite: 138 unit tests, 37 development browser tests and all 3 production-only tests passed. Packaging preserves local MP3s and uses bounded static chunks for the existing free deployment.
- Batch 10 operational repair: the generated packs file twice encountered a Windows/OneDrive write lock. Publication now preserves identical files and atomically replaces changed catalogs with bounded retries; validation rules are unchanged. Added tests for unchanged timestamps, complete replacement and failed destination publication. Full batch gates are rerun before acceptance.

### Batch 10 acceptance — 2026-10-07

- Accepted s2-u17, s2-u18, s2-u19, s2-u20: 88 vocabulary records, 36 explicit characters. Grammar owners: 二19, 二66, 二67, 二21, 二40, 二22, 二23, 二24, 二60. Each includes original media writing and retrieval.
- Self-review and applied fixes: Checked conditional weather, host rotation, map orientation and first-meeting chronology. Added genuine contexts for weather, teams, directions and age groups. A weather forecast is not treated as a confirmed outcome; map north is not equated with the direction the learner faces.
- All eight required gates passed; exact receipts and test counts: output/gates/batch-10-final-*.log. Packs/pinyin and word readability remain strict; production-only checks ran separately against the final preview.
- Audio: 78 direct dated exceptions after a real repair. Failed takes remain uninstalled, reviewed:false. Dependent assemblies use the same explicit policy. Automatic transcript screening is not native tone certification.
- Native-review flags remain open:
  - s2-u17: AI-assisted draft; native review pending. GF2021 grammar families: 二19, 二66, 二67. Native check: conditional omissions, 只要 sufficient-condition scope, weather-register collocations and clipped original seasonal verse. Forecast statements are uncertainty examples, not live weather guidance. Planned retrieval 二15 / 二20 / 二80: 朋友已经到了，我还在路上。, 才六点四十，不用急。, 都七点了，他七点才到。, 集合时间到了，我们该出发了。.
  - s2-u18: AI-assisted draft; native review pending. GF2021 grammar families: 二21, 二40. Native check: 举行/进行 collocations, role-assignment politeness, voluntary group register and marked action phrases. No sports skill or proficiency scores are invented. Planned retrieval 二16 / 二62 / 二69: 先看通知，然后报名。, 从学校走到活动地点，先走进东门。, 从教室拿出书，再把书交给老师。.
  - s2-u19: AI-assisted draft; native review pending. GF2021 grammar families: 二22, 二23. Native check: 往/向 targets, compass orientation, 对面 reference, metro/boat route plausibility and short dialogue ellipsis. Distances are fictional exercise facts, not real navigation instructions. Planned retrieval 二17 / 二74: 重点是日期，不是地址。, 我想讨论这个问题，你可以直接问。, 同样的问题，不一定有相同的答案。.
  - s2-u20: AI-assisted draft; native review pending. GF2021 grammar families: 二24, 二60. Native check: 是…的 circumstance focus, 从…看 evidence limits, 那会儿/那时候 register, 老朋友 duration and respectful personal questions. 字 长 is zhǎng in 长大, not cháng. Planned retrieval 二18 / 二79 / 二78: 我以为你同意了，但还没有问清楚。, 点头不一定就是同意。, 不是故意拿的，我现在还给你。, 好吧，我们先别开这个玩笑。.

### Batch 11 acceptance — 2026-10-07

- Accepted s2-u21, s2-u22, s2-u23, s2-u24: 88 vocabulary records, 36 explicit characters. Grammar owners: 二25, 二59, 二27, 二53, 二28, 二55, 二29, 二64. Each includes original media writing and retrieval.
- Self-review and applied fixes: Checked relationship terms, distance and location references, favour requests, source readings and conjunction scope. Used 求朋友帮忙 rather than an unnatural request collocation. Added distinct contexts and actual glosses; no family or relationship practice is claimed universal.
- All eight required gates passed; exact receipts and test counts: output/gates/batch-11-final-*.log. Packs/pinyin and word readability remain strict; production-only checks ran separately against the final preview.
- Audio: 89 direct dated exceptions after a real repair. Failed takes remain uninstalled, reviewed:false. Dependent assemblies use the same explicit policy. Automatic transcript screening is not native tone certification.
- Native-review flags remain open:
  - s2-u21: AI-assisted draft; native review pending. GF2021 grammar families: 二25, 二59. Native check: 实在 adjective citation shízai versus the adverb shízài; 爱人/太太 contextual register; 一样 predicates; figurative final scene. Resemblance and care do not establish private relationships. Planned retrieval 二19 / 二66 / 二67: 只要有空，就可以来。, 如果下雨，就换地方，时间不变。, 多云不等于一定下雨。.
  - s2-u22: AI-assisted draft; native review pending. GF2021 grammar families: 二27, 二53. Native check: distance versus route length, quantity complements, 背 bèi verb recite versus bēi carry and 倒 dǎo versus dào. Body-part 背 ownership remains later. The north-up map and distances are fictional but explicit; no outdoor route recommendation or diagnosis. Planned retrieval 二21 / 二40: 今天我当组长，明天换人。, 我们想办活动，还没有举行。, 目的是让大家练习说汉语。.
  - s2-u23: AI-assisted draft; native review pending. GF2021 grammar families: 二28, 二55. Native check: 求帮助 collocation, 为 beneficiary versus 给 recipient, 有用 evaluation, teacher/school terminology, consent and the original printer scene. No legal representation or automatic registration is implied. Planned retrieval 二22 / 二23: 往东走，路口再向左转。, 看着北边，不是已经往北走。, 出口在右边，别去左边。.
  - s2-u24: AI-assisted draft; native review pending. GF2021 grammar families: 二29, 二64. Native check: 或/或者 and alternative questions, 是…还是… clause scope, 比如说/例如 part-of-speech labels, source 音乐会 pronunciation, terse original scene. No concert schedule or claimed live performance is provided. Planned retrieval 二24 / 二60: 我们是去年在门口认识的。, 从这个消息看，时间还没定。, 从小在南方长大。.

### Batch 12 acceptance — 2026-10-07

- Accepted s2-u25, s2-u26, s2-u27, s2-u28: 88 vocabulary records, 35 explicit characters. Grammar owners: 二30, 二65, 二31, 二51, 二32, 二71, 二33, 二56, 二70. Each includes original media writing and retrieval.
- Self-review and applied fixes: Checked complaint causes, supported versus actual understanding, experience aspect and shared-room object references. Added distinct contexts and visible recognition glosses. A listening attempt is not marked comprehension and an experience is not a promised result.
- All eight required gates passed; exact receipts and test counts: output/gates/batch-12-final-*.log. Packs/pinyin and word readability remain strict; production-only checks ran separately against the final preview.
- Audio: 102 direct dated exceptions after a real repair. Failed takes remain uninstalled, reviewed:false. Dependent assemblies use the same explicit policy. Automatic transcript screening is not native tone certification.
- Native-review flags remain open:
  - s2-u25: AI-assisted draft; native review pending. GF2021 grammar families: 二30, 二65. Native check: connective relations, 虽然 marker omission, 受到重视 collocation, 合宜 in the written note, friendly noise complaint and figurative original scene. No validated behaviour score is claimed. Planned retrieval 二25 / 二59: 我对这个活动有兴趣。, 她跟我一样喜欢看书。, 生活不同，不等于态度不好。.
  - s2-u26: AI-assisted draft; native review pending. GF2021 grammar families: 二31, 二51. Native check: neutral 得 and object repetition, 读懂 versus 读得慢, 篇/节/下/度 classifiers, 长 cháng versus zhǎng and the original numeric joke. No fluency or pronunciation grade is fabricated. Planned retrieval 二27 / 二53: 湖离海很远，我们先去河边。, 这条路比那条路长一公里。, 她背两句话，不是背着一个包。.
  - s2-u27: AI-assisted draft; native review pending. GF2021 grammar families: 二32, 二71. Native check: guo experience particle versus guò motion readings, 会 meeting noun, 骑车 scope, 于 within 用于, passenger/visitor register and postcard joke. Document/transport lines teach verification, not live travel or immigration advice. Planned retrieval 二28 / 二55: 我为朋友打印两页。, 她为这个问题想了很久。, 这个活动很有意义。.
  - s2-u28: AI-assisted draft; native review pending. GF2021 grammar families: 二33, 二56, 二70. Native check: existential 是/有/放着, state versus event 了, head suffix tou, 面1 surface sense distinct from flour, room/rental collocations and original object-consent joke. No rental agreement or legal conclusion is claimed. Planned retrieval 二29 / 二64: 明天读书或者看影片，还没定。, 你想读书还是听音乐？, 或者我先讲，或者你先讲。.

### Batch 13 acceptance — 2026-10-07

- Accepted s2-u29, s2-u30, s2-u31, s2-u32: 88 vocabulary records, 32 explicit characters. Grammar owners: 二34, 二43, 二77, 二35, 二42, 二36, 二44, 二63, 二48, 二54. Each includes original media writing and retrieval.
- Self-review and applied fixes: Checked connective scope, hospital versus pharmacy references, causal reporting and inclusive versus exclusive boundaries. Added genuine contexts and source-specific readings of 得 and 长. Scope is explicit; no clinical advice or universal result is claimed.
- All eight required gates passed; exact receipts and test counts: output/gates/batch-13-final-*.log. Packs/pinyin and word readability remain strict; production-only checks ran separately against the final preview.
- Audio: 108 direct dated exceptions after a real repair. Failed takes remain uninstalled, reviewed:false. Dependent assemblies use the same explicit policy. Automatic transcript screening is not native tone certification.
- Native-review flags remain open:
  - s2-u29: AI-assisted draft; native review pending. GF2021 grammar families: 二34, 二43, 二77. Native check: contextual 啊 realization, 好的 stance, 老/小 surname-prefix pragmatics, 家 role suffix, 什么的 open lists and 呢 topic recovery. 李/小李 are fictional names requiring glosses; no real person or demographic statistic is described. Planned retrieval 二32 / 二71: 她去过这个地方，但今天不在那里。, 以前坐过船，不等于今天已经上船。, 没有去过，还想试一次。.
  - s2-u30: AI-assisted draft; native review pending. GF2021 grammar families: 二35, 二42, 二36. Native check: telephone 喂 pronunciation, conditional 的话 versus literal words, 不一会儿 interval versus 一会儿 duration, home-visit register and figurative cloud scene. Health words are comprehension examples; no diagnosis, drug choice or dose is taught. Planned retrieval 二30 / 二65 / 二33 / 二56 / 二70: 虽然下雨，但是时间没变。, 门开着，不等于可以直接进去。, 桌上放着书，她还没有读。.
  - s2-u31: AI-assisted draft; native review pending. GF2021 grammar families: 二44, 二63. Native check: 越来越 versus explicit 比 comparisons, paired 越 clauses, connective scope with different subjects, 才 focus, neutral 员/家 suffixes and 画儿 erhua. Drawn colours are context for 颜/色, not audited extra vocabulary. Original joke; native review remains pending. Planned retrieval 二31 / 二51 / 二34 / 二43 / 二77: 她说得很清楚。, 带书、笔什么的就行。, 我想看书，你呢？.
  - s2-u32: AI-assisted draft; native review pending. GF2021 grammar families: 二48, 二54. Native check: nominal predicates in age/date/price contexts, inclusive 以上/以下 boundaries, 得 dé obtaining versus de complement particle, 长 zhǎng growing versus cháng long, 省 noun versus saving verb, and the original verse’s compressed wording. Scores are fictional scene facts, not app readiness claims. Planned retrieval 二35 / 二42 / 二36 / 二32 / 二71: 喂，你好，现在方便吗？, 有空的话，我来坐一会儿。, 不一会儿，她回了消息。, 这部影片我看过，但小说还没读。.

### Batch 14 acceptance — 2026-10-07

- Accepted s2-u33, s2-u34: 42 vocabulary records, 16 explicit characters. Grammar owners: 二49, 二50, 二57, 二68, 二26, 二72. Each includes original media writing and retrieval.
- Self-review and applied fixes: Checked completed results, movement relative to the stated speaker, successive actions and distinctions between desire, obligation and certainty. Corrected classifier arithmetic and flour/称/倒 source readings. Added distinct contexts and actual room/furniture glosses. Recipe timings are fictional practice, not food-safety guarantees.
- All eight required gates passed; exact receipts and test counts: output/gates/batch-14-final-*.log. Packs/pinyin and word readability remain strict; production-only checks ran separately against the final preview.
- Audio: 111 direct dated exceptions after a real repair. Failed takes remain uninstalled, reviewed:false. Dependent assemblies use the same explicit policy. Automatic transcript screening is not native tone certification.
- Native-review flags remain open:
  - s2-u33: AI-assisted draft; native review pending. GF2021 grammar families: 二49, 二50, 二57. Native check: 称 chēng weighing, 面2 flour versus 面1 surface, 熟 shú with shóu colloquial variant, 来/去 reference point, linked-action purpose and result-complement distinctions. Time/weight values are fictional scene instructions, not a tested recipe or food-safety certification. Planned retrieval 二44 / 二63 / 二33 / 二56 / 二70: 她不但能读，而且能说。, 越来越清楚，还不是完美。, 桌上放着杯子，门还开着。.
  - s2-u34: AI-assisted draft; native review pending. GF2021 grammar families: 二68, 二26, 二72. Native check: causal versus contrast links, 给 agent/recipient distinction, ordinal recap, classifiers 排/座/道/片, 省 saving versus province, 行人/银行 readings, 干活儿 erhua and verse compression. Original scenes describe no learner exam readiness; native review is pending. Planned retrieval 二48 / 二54 / 二34 / 二43 / 二77: 今天星期三，这本书三十五块。, 姐姐是商人，我是学生。, 我想读报纸，你呢？.
- HSK 2 release self-review correction: replaced the awkward 先看安全 with 先注意安全 in s2-u13, added the recognition gloss, updated English, regenerated the changed speech and reading assembly, and passed all eight release gates. Existing unit/item IDs are preserved; native review remains pending.
- Coverage-audit repair in progress: added exact source-row recognition for classifier/measure-word synonyms, surname prefixes and 称1→称; row markers, pinyin and part of speech still required. Regression checks reject incidental text, wrong function and wrong reading. The s2-u06 一会儿 temporal entry is aligned with the source adverbial classification in editorial source; shadow pack/pinyin checks passed. Reapply that metadata correction and all release gates at the HSK 3 release before reporting final coverage.

### Batch 15 acceptance — 2026-10-07

- Accepted s3-u01, s3-u02, s3-u03, s3-u04: 88 vocabulary records, 28 explicit characters. Grammar owners: 三01, 三02, 三03, 三07, 三04, 三08, 三05, 三57. Each includes original media writing and retrieval.
- Self-review and applied fixes: Checked surname address permission, non-question interrogatives, surprise intensity, and 可 versus 不易 conditions. Added second contexts and explicit recognition glosses. Later grammar retrieval remains separate from the owner instruction. No nickname implies age or a real family relationship.
- All eight required gates passed; exact receipts and test counts: output/gates/batch-15-final-*.log. Packs/pinyin and word readability remain strict; production-only checks ran separately against the final preview.
- Audio: 121 direct dated exceptions after a real repair. Failed takes remain uninstalled, reviewed:false. Dependent assemblies use the same explicit policy. Automatic transcript screening is not native tone certification.
- Native-review flags remain open:
  - s3-u01: AI-assisted draft; native review pending. GF2021 grammar families: 三01, 三02. Native check: 第 order versus quantity, 老/小 surname address pragmatics, neutral suffixes 子/头/们 and erhua 儿, role 家 versus home, 熟人 register and family terminology. Fictional Li is glossed; no assumptions about real family or age. Native review pending. Planned retrieval 二35 / 二42 / 二36 / 二49 / 二50 / 二57: 喂，你好，有空的话来坐一会儿。, 不一会儿，她回了消息。, 先把面粉取出来，再称一百克。, 请她把杯子端出来。.
  - s3-u02: AI-assisted draft; native review pending. GF2021 grammar families: 三03, 三07. Native check: 敢 versus 能/可以, 谁都 with negation and restricted scope, interrogative-word echo constructions, indefinite 点儿什么 and each versus all. Public participation is a fictional event arrangement, not a universal competition policy. Native review pending. Planned retrieval 二44 / 二63 / 二68: 她不但能读，而且能说。, 越练越清楚，还不是完美。, 因为分工清楚，所以没有重复做。.
  - s3-u03: AI-assisted draft; native review pending. GF2021 grammar families: 三04, 三08. Native check: 需要 versus obligation and consent; 志愿 noun use; suffixes 者/员 in connected words; 每/各/任何 scope; 共有 versus 共同; collective-work collocations and original chair joke. No real employment or volunteering arrangement is created. Native review pending. Planned retrieval 二48 / 二54 / 三01 / 三02: 姐姐是商人，我是学生。, 今天星期三，这本书三十五块。, 老李是称呼，不能直接猜他的年龄。, 朋友们看包里头的书，桌子上的笔先别动。.
  - s3-u04: AI-assisted draft; native review pending. GF2021 grammar families: 三05, 三57. Native check: separated forms 帮我一个忙/见一次面/理个发, variable duration constructions, 跟…结婚 versus direct object, shared-subject linked verbs, 亲 adjective in 亲姐妹 and informal metaphor in the original scene. Native review pending; no actual personal appointment is made. Planned retrieval 二49 / 二50 / 二57 / 三03 / 三07: 请她把杯子端出来。, 先取出面粉，再称一百克。, 谁都可以只听，不一定参加比赛。, 不敢参加，不等于没有能力。.
- Live deployment check found an older offline shell intercepting /cdn-cgi/access/authorized after the Google provider returned. Added a Cloudflare internal-route exclusion to navigation fallback. The existing production offline test now also proves the Access callback reaches the network instead of the cached shell; release verification is pending. This preserves authentication protection and learner storage.

### Batch 16 acceptance — 2026-10-07

- Accepted s3-u05, s3-u06, s3-u07, s3-u08: 88 vocabulary records, 28 explicit characters. Grammar owners: 三06, 三46, 三09, 三10, 三11, 三33, 三12, 三58. Each includes original media writing and retrieval.
- Self-review and applied fixes: Checked comparisons and proportions, attempt counts, urgency versus permission, and topic scope. Added actual contexts, contrastive examples and character glosses. A requested act is not recorded as a completed result.
- All eight required gates passed; exact receipts and test counts: output/gates/batch-16-final-*.log. Packs/pinyin and word readability remain strict; production-only checks ran separately against the final preview.
- Audio: 129 direct dated exceptions after a real repair. Failed takes remain uninstalled, reviewed:false. Dependent assemblies use the same explicit policy. Automatic transcript screening is not native tone certification.
- Native-review flags remain open:
  - s3-u05: AI-assisted draft; native review pending. GF2021 grammar families: 三06, 三46. Native check: 打得开/看不见/离不开/完不成 potential forms versus noun-object separables; 到/住/走 achieved results; 文件/纪录/记录 distinction and the title-personification joke. No actual learner file is modified. Native review pending. Planned retrieval 二68 / 三04 / 三08: 因为分工清楚，所以没有重复做。, 每个人都先看自己的任务。, 需要帮忙，先问对方有没有空。, 任何人都可以问，不必已经有答案。.
  - s3-u06: AI-assisted draft; native review pending. GF2021 grammar families: 三09, 三10. Native check: noun classifier collocations, 行 háng and 只 zhī readings, 双 versus 根 quantities, 顿/口/眼 action measures and abbreviated measure phrases. Original meal scenario, no prescribed serving size. Native review pending. Planned retrieval 三01 / 三02 / 三05 / 三57: 老李是称呼，不能直接猜他的年龄。, 朋友们看包里头的书。, 下午理个发，再跟朋友谈一谈话。, 请她问一下朋友，不能替朋友答应。.
  - s3-u07: AI-assisted draft; native review pending. GF2021 grammar families: 三11, 三33. Native check: classifier AA naturalness and bounded scope, one-at-a-time versus per-person patterns, 配/配合 collocations, 富 adjective and nominal 整/整体. The original verse is spoken course writing, not borrowed lyrics. Native review pending. Planned retrieval 三03 / 三07 / 三06 / 三46: 谁都可以只听，不一定参加比赛。, 不敢参加，不等于没有能力。, 文件打得开，日期还没核对。, 找了十分钟，终于找到了。.
  - s3-u08: AI-assisted draft; native review pending. GF2021 grammar families: 三12, 三58. Native check: 比较 versus 比, degree 还 versus continuing 还, 相当 degree use, manner comparison word order, 不比 versus 不如, quantified 比 differences and spoken-versus-sung tone notes. All verse lines are original; no copyrighted lyric or real singer identity. Native review pending. Planned retrieval 三04 / 三08 / 三09 / 三10: 每个人都先看自己的任务。, 需要帮忙，先问对方有没有空。, 两双筷子，通常是四根。, 看了一眼，还要仔细读。.

### Batch 17 acceptance — 2026-10-07

- Accepted s3-u09, s3-u10, s3-u11, s3-u12: 88 vocabulary records, 28 explicit characters. Grammar owners: 三13, 三37, 三14, 三21, 三15, 三51, 三16, 三17. Each includes original media writing and retrieval.
- Self-review and applied fixes: Checked fractions and multiples against the stated denominator, approximate boundaries, result versus potential complements, and consequences versus purpose. Added genuine second contexts and visible glosses. Corrected arithmetic and kept uncertain outcomes conditional.
- All eight required gates passed; exact receipts and test counts: output/gates/batch-17-final-*.log. Packs/pinyin and word readability remain strict; production-only checks ran separately against the final preview.
- Audio: 135 direct dated exceptions after a real repair. Failed takes remain uninstalled, reviewed:false. Dependent assemblies use the same explicit policy. Automatic transcript screening is not native tone certification.
- Native-review flags remain open:
  - s3-u09: AI-assisted draft; native review pending. GF2021 grammar families: 三13, 三37. Native check: 光 sufficiency scope versus 仅 restriction, 就 quantity emphasis, minimum lead time, idiomatic 有的是 versus 有的; price includes total expenses. Paper/chair joke and confirmation validity phrasing need native style review. Native review pending. Planned retrieval 三05 / 三57 / 三11 / 三33: 下午理个发，再跟朋友谈一谈话。, 请她问一下朋友，不能替朋友答应。, 张张纸都有标题，一张一张地看。, 六个人四张纸，还缺两张。.
  - s3-u10: AI-assisted draft; native review pending. GF2021 grammar families: 三14, 三21. Native check: adverb family 本来/才/曾经/从来/赶紧/赶快/立刻/连忙/始终/已/早已, written 已 register, 自从 time anchoring, and economical verse phrasing. No inferred current residence or confirmed future meeting. Native review pending. Planned retrieval 三06 / 三46 / 三12 / 三58: 文件打得开，日期还没核对。, 找了十分钟，终于找到了。, 今天更加清楚，不等于一定更快。, 不比她快，可能一样快。.
  - s3-u11: AI-assisted draft; native review pending. GF2021 grammar families: 三15, 三51. Native check: pragmatic emphasis 总/总是 versus strict frequency, 往往 tendencies, duration word order with an object and continuing 了…了; bottle-personification joke. Nutrition vocabulary is recognition content, not a diet prescription. Native review pending. Planned retrieval 三09 / 三10 / 三13 / 三37: 两双筷子，通常是四根。, 看了一眼，还要仔细读。, 至少提前一天，提前两天也可以。, 材料有的是，名额还要确认。.
  - s3-u12: AI-assisted draft; native review pending. GF2021 grammar families: 三16, 三17. Native check: 再 conditional/sequencing senses versus 又 past repetition, 互相/相互 reciprocity, 尽量 limits, 亲自 versus 独自; 采取措施 versus 采用方法 collocations. Actual partial achievements only; no invented learner grading. Native review pending. Planned retrieval 三11 / 三33 / 三14 / 三21: 张张纸都有标题，一张一张地看。, 六个人四张纸，还缺两张。, 她曾经住这里，旧店早已搬走。, 自从毕业，我们很少见面。.
- Cloudflare callback repair verification: batches 16 and 17 passed all eight gates, including the production offline test with a network-only Access callback. Existing cached browsers without this updated worker may require a hard refresh to complete their current callback; no security bypass or learner-data change was used.

### Final coverage self-review corrections (pending final release gates)

- The audit now recognizes annotated 初/化/性/员/者 entries and the …极了 template only with exact source-row, reading and grammatical evidence; tests reject incidental compounds, the wrong reading and the wrong source row. This does not certify learner mastery.
- s3-u02: replace the repeated fear-verb lesson for 怕 with its GF2021 level-3 cautious-guess adverb sense. New contexts: 这次怕不能马上开始。 and 怕是要再等一会儿，先问清楚，再决定试不试。 Native review of the hedge remains pending. The level-3 release will reserialize this accepted unit and regenerate changed speech before all release gates.
- s3-u28/s3-u29: separate 初 as a lunar-date prefix from 初 as an initial-arrival adverb, swap 教练 into the preceding unit to preserve both approved word budgets, and retain all unit/item IDs. Native flags distinguish those senses.
- s3-u38: classify 米 in the metre sense as the source-list noun rather than a classifier; Chinese examples remain unchanged.
- All source allocation budgets and unique official-row ownership pass. Unpublished shadow checks are preflight only; acceptance still requires every batch gate and the final release gates.
- HSK 3 exam-bank self-review: alternation does not imply a fixed first action; an approximate count does not rule out exactly ten, so the question asks whether the exact count can be established. Clarified asking about a course schedule and the imagined lyric setting. IDs and answer positions remain stable. Release audio/gates and native review are still required.
- Batch 18 gate repair: the growing catalog exposed repeated reads and hashing of the identical approved profile once per clip. Compute that expected SHA once, then retain every per-clip pitch, method and identity assertion. The timeout and all acceptance checks remain unchanged; rerun the complete batch gates.

### Batch 18 acceptance — 2026-10-07

- Accepted s3-u13, s3-u14, s3-u15, s3-u16: 88 vocabulary records, 28 explicit characters. Grammar owners: 三18, 三69, 三19, 三76, 三20, 三29, 三22, 三47. Each includes original media writing and retrieval.
- Self-review and applied fixes: Checked direction relative to the speaker, temporal ordering, ongoing versus completed events, and 把 object/result requirements. Added distinct reading contexts and actual glosses. A promise or future action is not treated as completed evidence.
- All eight required gates passed; exact receipts and test counts: output/gates/batch-18-final-*.log. Packs/pinyin and word readability remain strict; production-only checks ran separately against the final preview.
- Audio: 138 direct dated exceptions after a real repair. Failed takes remain uninstalled, reviewed:false. Dependent assemblies use the same explicit policy. Automatic transcript screening is not native tone certification.
- Native-review flags remain open:
  - s3-u13: AI-assisted draft; native review pending. GF2021 grammar families: 三18, 三69. Native check: 恐怕 pragmatic unwelcome possibility, 大概 versus 大约, adjective 保险 versus insurance noun, 仍 written register, possible versus certain concepts and the friend/plan joke. No claim that forecasts guarantee weather. Native review pending. Planned retrieval 三12 / 三58 / 三15 / 三51: 今天更加清楚，不等于一定更快。, 不比她快，可能一样快。, 通常周末散步，今天只走了二十分钟。, 连续两天不等于坚持了一年。.
  - s3-u14: AI-assisted draft; native review pending. GF2021 grammar families: 三19, 三76. Native check: 白跑, 并 with negation, 反正 versus indifference, 果然 expectation and evidence, strong 绝对, rhetorical question polarity and polite alternatives. Distinguish 纪录 as record from 记录 as recording. No unverified claims marked facts. Native review pending. Planned retrieval 三13 / 三37 / 三16 / 三17: 至少提前一天，提前两天也可以。, 材料有的是，名额还要确认。, 等听清楚了再加快。, 我亲自读，你帮我听。.
  - s3-u15: AI-assisted draft; native review pending. GF2021 grammar families: 三20, 三29. Native check: 由 agent construction versus 由于, 按 and 按照 register, 报到 versus 报道, department/head/member roles, 纪念 activity context and grand-title metaphor. No implication of real institution rules. Native review pending. Planned retrieval 三14 / 三21 / 三18 / 三69: 她曾经住这里，旧店早已搬走。, 自从毕业，我们很少见面。, 她大概六点到，还没确认。, 要是下雨，就在室内见。.
  - s3-u16: AI-assisted draft; native review pending. GF2021 grammar families: 三22, 三47. Native check: directional viewpoint, 上来/上去 and reference floor, 朝 versus 到 endpoint, 背 bēi versus bèi, 箱子运输 wording and informal four-hands joke. No specific safe-weight or lifting-technique claim. Native review pending. Planned retrieval 三15 / 三51 / 三19 / 三76: 通常周末散步，今天只走了二十分钟。, 连续两天不等于坚持了一年。, 活动并没有取消，只是换了房间。, 难道旧图片就能证明今天取消了吗？.

### Batch 19 acceptance — 2026-10-07

- Accepted s3-u17, s3-u18, s3-u19, s3-u20: 88 vocabulary records, 28 explicit characters. Grammar owners: 三23, 三40, 三24, 三41, 三25, 三71, 三26, 三72. Each includes original media writing and retrieval.
- Self-review and applied fixes: Checked priority and concession scope, cultural claims, apology versus excuse, and gift acceptance boundaries. Added genuine vocabulary contexts and recognition glosses. Fictional customs are not represented as universal Chinese practice.
- All eight required gates passed; exact receipts and test counts: output/gates/batch-19-final-*.log. Packs/pinyin and word readability remain strict; production-only checks ran separately against the final preview.
- Audio: 144 direct dated exceptions after a real repair. Failed takes remain uninstalled, reviewed:false. Dependent assemblies use the same explicit policy. Automatic transcript screening is not native tone certification.
- Native-review flags remain open:
  - s3-u17: AI-assisted draft; native review pending. GF2021 grammar families: 三23, 三40. Native check: 为2 wèi emotional object versus earlier 为1 beneficiary and 替 substitution, 对……来说 perspective, 自主 conversational register, 感情/情感 distinction and objective price versus evaluated value. Personal-needs claims are fictional and not universal. Native review pending. Planned retrieval 三16 / 三17 / 三20 / 三29: 等听清楚了再加快。, 我亲自读，你帮我听。, 活动由学生举办。, 按名单分组，不按到达时间。.
  - s3-u18: AI-assisted draft; native review pending. GF2021 grammar families: 三24, 三41. Native check: 向 recipient versus 朝 direction, 像……一样 comparison scope, 文明 adjective versus civilization noun, 华人 and 中华民族 sociocultural register, folk/art genres and metaphorical film joke. No essentialist or universal custom claims. Native review pending. Planned retrieval 三18 / 三69 / 三22 / 三47: 她大概六点到，还没确认。, 要是下雨，就在室内见。, 朝门口走，还没说是否到达。, 我在二楼，你上来。.
  - s3-u19: AI-assisted draft; native review pending. GF2021 grammar families: 三25, 三71. Native check: 由于 versus 因为 register, 因此 causal consequence, apology phrasing, 相关 attributive usage, emotional 伤心 versus physical 伤 and incomplete versus completed repair. Fictional wrong-address incident is not medical guidance. Native review pending. Planned retrieval 三19 / 三76 / 三23 / 三40: 活动并没有取消，只是换了房间。, 难道旧图片就能证明今天取消了吗？, 我为她担心，也尊重她的选择。, 对我来说，安静很重要。.
  - s3-u20: AI-assisted draft; native review pending. GF2021 grammar families: 三26, 三72. Native check: 为了 purpose versus 因为 cause and 为 beneficiary, 适用 versus 适合, 彩色 as modifier, 创作 versus 创造, 金/银 colour-material contrast, gift politeness and gold-plating metaphor. Original card/scene only, no copied lyrics or scripts. Native review pending. Planned retrieval 三20 / 三29 / 三24 / 三41: 活动由学生举办。, 按名单分组，不按到达时间。, 向主人问清楚时间。, 像平时一样，先问时间。.
- Batch 20 gate repair: the character-word catalog test demanded the ambiguous bare spelling 精神 although the app and manifest correctly use 很精神 for the adjective jīngshen. Assert every character word through its actual reading-aware speech context, and extend the compiled-course mapping regression to every existing ambiguous-reading case. This preserves all catalog assertions and avoids generating a misleading bare-spelling clip. The later noun lesson will use 精神力量. Full batch gates rerun.

### Batch 20 acceptance — 2026-10-07

- Accepted s3-u21, s3-u22, s3-u23, s3-u24: 88 vocabulary records, 28 explicit characters. Grammar owners: 三27, 三54, 三28, 三38, 三30, 三70, 三31, 三78. Each includes original media writing and retrieval.
- Self-review and applied fixes: Checked visual inference versus actual reports, comparative scope, causal ordering and concession. Added exact source readings, independent contexts and visible glosses. Retrieval examples do not certify learner mastery.
- All eight required gates passed; exact receipts and test counts: output/gates/batch-20-final-*.log. Packs/pinyin and word readability remain strict; production-only checks ran separately against the final preview.
- Audio: 154 direct dated exceptions after a real repair. Failed takes remain uninstalled, reviewed:false. Dependent assemblies use the same explicit policy. Automatic transcript screening is not native tone certification.
- Native-review flags remain open:
  - s3-u21: AI-assisted draft; native review pending. GF2021 grammar families: 三27, 三54. Native check: colloquial passive 叫/让 with rain as agent, 衬衫 versus 衬衣 overlap by region, 皮 as material noun, natural delivery and landlord register, and the personified-sofa joke. No permission to sign for another person is inferred. Native review pending. Planned retrieval 三22 / 三47 / 三25 / 三71: 朝门口走，还没说是否到达。, 我在二楼，你上来。, 因为我没核对，我发了旧地址。, 由于通知有错，所以先停止传播旧通知。.
  - s3-u22: AI-assisted draft; native review pending. GF2021 grammar families: 三28, 三38. Native check: 普遍 versus universal scope, 除了…也 negation, 收看/观看 and 收听 register, 广大 audience collocation, and the original verse’s ellipsis. No population survey is claimed. Native review pending. Planned retrieval 三23 / 三40 / 三26 / 三72: 我为她担心，也尊重她的选择。, 对我来说，安静很重要。, 为了带书方便，我选这个布袋。, 为了纪念见面，我们做一张贺卡。.
  - s3-u23: AI-assisted draft; native review pending. GF2021 grammar families: 三30, 三70. Native check: conjunction 由于 versus cause-preposition use, connector scope, 认可/同意 distinction, necessary versus sufficient 只有 conditions, and club-rule language. Legal and safety vocabulary are language practice only; no real determination or event safety guarantee is claimed. Native review pending. Planned retrieval 三24 / 三41 / 三27 / 三54: 向主人问清楚时间。, 像平时一样，先问时间。, 衣服被雨弄湿了。, 把这本书交给她。.
  - s3-u24: AI-assisted draft; native review pending. GF2021 grammar families: 三31, 三78. Native check: 精神 adjective jīngshen versus noun jīngshén, 活 for lively delivery, 乐 verb register, 干吗 casual tone, 哈哈 target and written-versus-spontaneous laughter, original verse rhythm, and question intonation preserving lexical tones. Synthesized intonation has not been certified by a native listener. Native review pending. Planned retrieval 三25 / 三71 / 三28 / 三38: 因为没核对，我发了旧通知。, 由于通知有错，所以先停止传播旧通知。, 除了看节目，我还听广播。, 除了周五，其他几天都可以。.

### Batch 21 acceptance — 2026-10-07

- Accepted s3-u25, s3-u26, s3-u27, s3-u28: 88 vocabulary records, 28 explicit characters. Grammar owners: 三32, 三53, 三34, 三68, 三35, 三36, 三39, 三52. Each includes original media writing and retrieval.
- Self-review and applied fixes: Checked four-character paired patterns, larger-topic predicates, 看起来/看上去 evidence, and elapsed time since an event. Differentiated 精神 noun versus adjective source records and 初 prefix use. Added literal second contexts and actual glosses. Fictional symptoms are language practice, not diagnosis.
- All eight required gates passed; exact receipts and test counts: output/gates/batch-21-final-*.log. Packs/pinyin and word readability remain strict; production-only checks ran separately against the final preview.
- Audio: 166 direct dated exceptions after a real repair. Failed takes remain uninstalled, reviewed:false. Dependent assemblies use the same explicit policy. Automatic transcript screening is not native tone certification.
- Native-review flags remain open:
  - s3-u25: AI-assisted draft; native review pending. GF2021 grammar families: 三32, 三53. Native check: 本领 versus 本事 register, apposition 老师张先生, larger-topic scope in 主谓谓语句, 职业 disclosure, 表面 impressions versus evidence, and 作品评价 phrasing. Native review pending. Planned retrieval 三26 / 三72 / 三30 / 三70: 为了带书方便，我选这个布袋。, 为了纪念见面，我们做一张贺卡。, 要是时间合适，就再问她。, 只有她同意，才写她的职业。.
  - s3-u26: AI-assisted draft; native review pending. GF2021 grammar families: 三34, 三68. Native check: concession X是X, fixed 不A不B combinations, 本事/毛病 colloquial register, 精神 noun jīngshén, balanced criticism and original scene rhythm. Medical vocabulary illustrates reports, without diagnosis or treatment claims. Native review pending. Planned retrieval 三27 / 三54 / 三31 / 三78: 衣服被雨弄湿了。, 把这本书交给她。, 哈哈，笑的是我自己。, 你今天也来参加活动？.
  - s3-u27: AI-assisted draft; native review pending. GF2021 grammar families: 三35, 三36. Native check: overlapping 看起来/看上去 uses, 羊 as a general sheep/goat label, animal classifiers, nonjudgmental 胖 use for a model, the banana-as-mountain joke, photograph framing and permission scope. Native review pending. Planned retrieval 三28 / 三38 / 三32 / 三53: 除了看节目，我还听广播。, 除了周五，其他几天都可以。, 老师张先生也来了。, 她汉语说得很流利。.
  - s3-u28: AI-assisted draft; native review pending. GF2021 grammar families: 三39, 三52. Native check: 初 lunar-date prefix versus the later first-arrival adverb lesson, elapsed-time double-了 constructions, 前后 sequence versus approximation, 纪录 versus 记录, 将近 boundaries, 期 magazine classifier and original verse rhythm. Native review pending. Planned retrieval 三30 / 三70 / 三34 / 三68: 要是时间合适，就再问她。, 只有她同意，才写她的职业。, 她不慌不忙地核对地址。, 好是好，不过地点还没确认。.

### Batch 22 acceptance — 2026-10-07

- Accepted s3-u29, s3-u30, s3-u31, s3-u32: 88 vocabulary records, 28 explicit characters. Grammar owners: 三42, 三59, 三43, 三44, 三45, 三56, 三48, 三50. Each includes original media writing and retrieval.
- Self-review and applied fixes: Checked 越 comparisons, object/predicate complements, attributives, method versus purpose, and potential/event-count constructions. Corrected a malformed 发出 example, an unclear distractor and the new-character allocation. Kept 了 liǎo, 头 initial, 化 suffix and 信 verb source senses explicit.
- All eight required gates passed; exact receipts and test counts: output/gates/batch-22-final-*.log. Packs/pinyin and word readability remain strict; production-only checks ran separately against the final preview.
- Audio: 175 direct dated exceptions after a real repair. Failed takes remain uninstalled, reviewed:false. Dependent assemblies use the same explicit policy. Automatic transcript screening is not native tone certification.
- Native-review flags remain open:
  - s3-u29: AI-assisted draft; native review pending. GF2021 grammar families: 三42, 三59. Native check: 初 adverb versus the preceding lunar-date prefix lesson, 工夫 versus 功夫 overlap, 了 liǎo in the fixed expression 没完没了, 头 as initial, verb 连 versus other readings, repeated-verb complement naturalness and 越 comparative linkage. No efficacy guarantee or invented score. Native review pending. Planned retrieval 三31 / 三78 / 三35 / 三36: 哈哈，笑的是我自己。, 你今天也来参加活动？, 她看起来很累，先问本人。, 照片看上去很亮，不说明现场温度。.
  - s3-u30: AI-assisted draft; native review pending. GF2021 grammar families: 三43, 三44. Native check: action/adjective subjects, subject–predicate objects after 希望, 化 suffix productivity, 实验 versus 试验 overlap, 工业 vocabulary and permission wording, original verse rhythm. Language practice is not laboratory operating instruction. Native review pending. Planned retrieval 三32 / 三53 / 三39 / 三52: 老师张先生也来了。, 她汉语说得很流利。, 从下周起，每天先读一段。, 她离开这里三天了。.
  - s3-u31: AI-assisted draft; native review pending. GF2021 grammar families: 三45, 三56. Native check: 城/城市/区 reference, regional direction versus viewpoint, verb and subject–predicate attributives, linked method/purpose clauses, 前往 register and rural visit wording. No current travel recommendation or permission is asserted. Native review pending. Planned retrieval 三34 / 三68 / 三42 / 三59: 她不慌不忙地核对地址。, 好是好，不过地点还没确认。, 越听越累，就先停一下。, 她听汉语听得很认真。.
  - s3-u32: AI-assisted draft; native review pending. GF2021 grammar families: 三48, 三50. Native check: newspaper 报 versus report 报告/报道, verb 信, potential 了 liǎo, noun/pronoun placement with event counts, working-ID 证 reference and original verse rhythm. Embassy and customs content is fictional language practice, never current procedural or financial advice. Native review pending. Planned retrieval 三35 / 三36 / 三43 / 三44: 她看起来很累，先问本人。, 照片看上去很亮，不说明现场温度。, 学习汉语需要时间。, 我希望大家都看懂说明。.
- Batch 23 gate repair and final-batch preflight: completed all three comprehension checks for the dialogue and main reading in s3-u33…u44. Questions target actual details and bounded inferences, with unambiguous distractors; revised the green-tea question to ask for the suggestion rather than an unconfirmed completed choice, and the approximate-count question to ask whether an exact count is specified. No Chinese speech changed. Added the existing three-question acceptance requirement to unpublished preflight too, so the same omission is caught before expensive audio generation. Full checks remain unchanged.

### Batch 23 acceptance — 2026-10-07

- Accepted s3-u33, s3-u34, s3-u35, s3-u36: 88 vocabulary records, 27 explicit characters. Grammar owners: 三49, 三75, 三55, 三77, 三60, 三63, 三61, 三62. Each includes original media writing and retrieval.
- Self-review and applied fixes: Checked degree complements, emphatic negation, passive agent scope, corrective 是, simultaneous states, alternation and two-aspect framing. Corrected missing literal contexts and the 衣架 classifier. Preserved bèi back, suffix 性 and 极了 source records. Injuries and plant stories provide no clinical or agricultural advice.
- All eight required gates passed; exact receipts and test counts: output/gates/batch-23-final-*.log. Packs/pinyin and word readability remain strict; production-only checks ran separately against the final preview.
- Audio: 180 direct dated exceptions after a real repair. Failed takes remain uninstalled, reviewed:false. Dependent assemblies use the same explicit policy. Automatic transcript screening is not native tone certification.
- Native-review flags remain open:
  - s3-u33: AI-assisted draft; native review pending. GF2021 grammar families: 三49, 三75. Native check: friendly humour register, 极了 degree versus measurement, 就是 qualification, 性 suffix productivity, degree-result overlap. No smile is treated as consent. Native review pending. Planned retrieval 三39 / 三52 / 三45 / 三56: 从下周起，每天先读一段。, 她离开这里三天了。, 朋友推荐的旅馆还没订。, 我们去村里了解农业。.
  - s3-u34: AI-assisted draft; native review pending. GF2021 grammar families: 三55, 三77. Native check: 背 bèi versus bēi, classifier 部/步, 被 with omitted agent, 是 corrective emphasis, rack classifier and everyday belongings register. No pain diagnosis or blame inference. Native review pending. Planned retrieval 三42 / 三59 / 三48 / 三50: 越听越累，就先停一下。, 她听汉语听得很认真。, 这些邮件今天处理不了。, 我问了她三次。.
  - s3-u35: AI-assisted draft; native review pending. GF2021 grammar families: 三60, 三63. Native check: coordinated 也 versus 又 scope, 胜/赢 register, sport counters, 游 sense, competition timing. No body judgment or exercise safety guarantee. Native review pending. Planned retrieval 三43 / 三44 / 三49 / 三75: 学习汉语需要时间。, 我希望大家都看懂说明。, 她笑得很开心。, 她一点儿也不生气。.
  - s3-u36: AI-assisted draft; native review pending. GF2021 grammar families: 三61, 三62. Native check: alternating 一会儿 cadence, paired considerations, 任 verb, 幸福 subjective reports, 生 raw versus 生存 and fictional injury vocabulary. No care, safety or diagnostic instruction. Native review pending. Planned retrieval 三45 / 三56 / 三55 / 三77: 朋友推荐的旅馆还没订。, 我们去村里了解农业。, 行李被同学移到门后了。, 我是来领行李的。.

### Batch 24 acceptance — 2026-10-07

- Accepted s3-u37, s3-u38, s3-u39, s3-u40: 88 vocabulary records, 24 explicit characters. Grammar owners: 三64, 三65, 三66, 三67, 三73, 三74, 三79, 三80. Each includes original media writing and retrieval.
- Self-review and applied fixes: Checked ordered actions, 并且 addition, 不仅 inclusion, exclusive alternatives, immediate sequence, approximation, advanced-state 都 and resigned concessions. Separated 调 diào from tiáo and both 为 wéi source senses. Added actual recognition glosses. Native review is specifically needed for 血 xiě versus xuè and colloquial concession delivery.
- All eight required gates passed; exact receipts and test counts: output/gates/batch-24-final-*.log. Packs/pinyin and word readability remain strict; production-only checks ran separately against the final preview.
- Audio: 189 direct dated exceptions after a real repair. Failed takes remain uninstalled, reviewed:false. Dependent assemblies use the same explicit policy. Automatic transcript screening is not native tone certification.
- Native-review flags remain open:
  - s3-u37: AI-assisted draft; native review pending. GF2021 grammar families: 三64, 三65. Native check: first versus second reason, 并且 scope, club and employment register, construction/completion/trading distinction. Fictional business language, not advice or guarantees. Native review pending. Planned retrieval 三48 / 三50 / 三60 / 三63: 这些邮件今天处理不了。, 我问了她三次。, 我也看足球，也跳舞。, 她又高兴又紧张。.
  - s3-u38: AI-assisted draft; native review pending. GF2021 grammar families: 三66, 三67. Native check: paired alternatives, 不光 register, 老太太/老头儿 politeness, 所 classifier/institution, 系 department, area/proportion scope. No actual eligibility, legal status or study recommendation. Native review pending. Planned retrieval 三49 / 三75 / 三61 / 三62: 她笑得很开心。, 她一点儿也不生气。, 我一会儿读，一会儿听。, 一方面想参加，另一方面需要休息。.
  - s3-u39: AI-assisted draft; native review pending. GF2021 grammar families: 三73, 三74. Native check: 任 conjunction, 为 wéi in 作为, 了…就 narrative scope, approximate adjacent numerals, count versus percentage. No investment, purchasing or eligibility advice. Native review pending. Planned retrieval 三55 / 三77 / 三64 / 三65: 行李被同学移到门后了。, 我是来领行李的。, 首先确认时间，然后报名。, 她核对时间，并且问了地点。.
  - s3-u40: AI-assisted draft; native review pending. GF2021 grammar families: 三79, 三80. Native check: 都 advanced-state use, resigned X就X点儿吧, 大夫 neutral fu, 调 diào, 血 xiě versus xuè, respectful private-history wording. Fictional language only; no diagnosis, first-aid or legal instructions. Native review pending. Planned retrieval 三60 / 三63 / 三66 / 三67: 我也看足球，也跳舞。, 她又高兴又紧张。, 不仅有阅读，而且有听力。, 不是这门，就是那门。.

### Batch 25 acceptance — 2026-10-07

- Accepted s3-u41, s3-u42, s3-u43, s3-u44: 87 vocabulary records, 24 explicit characters. Grammar owners: 三81, 三19, 三07, 三48, 三49, 三58, 三54, 三55. Each includes original media writing and retrieval.
- Self-review and applied fixes: Checked X什么啊 pragmatics, indirect questions, degree and comparison, 把 and 被 focus. Added actual 演戏 character context, removed a traditional-character variant, and replaced an ambiguous 重 cloze with 推广 while preserving the 重 chóng introduction. Added all final retrieval slots. Completion means introduction, never level certification or assumed consent.
- All eight required gates passed; exact receipts and test counts: output/gates/batch-25-final-*.log. Packs/pinyin and word readability remain strict; production-only checks ran separately against the final preview.
- Audio: 200 direct dated exceptions after a real repair. Failed takes remain uninstalled, reviewed:false. Dependent assemblies use the same explicit policy. Automatic transcript screening is not native tone certification.
- Native-review flags remain open:
  - s3-u41: AI-assisted draft; native review pending. GF2021 grammar families: 三81, 三19. Native check: X什么啊 humour versus dismissiveness, 并 scope, 为 wéi passive formal register, TV vocabulary and friendly repair. Native review pending. Planned retrieval 三61 / 三62 / 三73 / 三74: 我一会儿读，一会儿听。, 一方面想参加，另一方面需要休息。, 我看了通知就问她。, 十个人左右参加。.
  - s3-u42: AI-assisted draft; native review pending. GF2021 grammar families: 三07, 三48. Native check: indirect questions, pronoun references, 调 tiáo, repeated potential-complement retrieval, 看清 versus 看懂. Fictional props and scene, no weapon or operating instruction. Native review pending. Planned retrieval 三64 / 三65 / 三79 / 三80: 首先确认时间，然后报名。, 她核对时间，并且问了地点。, 都十点了，先结束吧。, 慢就慢点儿吧，先说准确。.
  - s3-u43: AI-assisted draft; native review pending. GF2021 grammar families: 三49, 三58. Native check: original verse rhythm, figurative language, 重 chóng versus zhòng, degree/comparison retrieval, 随 register, 团 noun and_until scope. No copyrighted lyrics, real-person biography or operational guidance. Native review pending. Planned retrieval 三66 / 三67 / 三81: 不仅有阅读，而且有听力。, 不是这门，就是那门。, 怕什么啊，我陪你。, 急什么啊，还没到时间。.
  - s3-u44: AI-assisted draft; native review pending. GF2021 grammar families: 三54, 三55. Native check: 把/被 focus, 属 responsibility and 属于 ownership, 照 according-to versus photography, 左右 approximation versus influence, respectful 去世 register, original group-chat conclusion. No level certification, copyright quotation or assumed consent. Native review pending. Planned retrieval 三73 / 三74 / 三79 / 三80 / 三81: 我看了通知就问她。, 十个人左右参加。, 都十点了，先结束吧。, 慢就慢点儿吧，先说准确。, 急什么啊，还没到时间。.

### Parity repair batch 37 acceptance — 2026-10-07

- Units: s3-u41–44, preserving all 87 vocabulary IDs and existing grammar
  ownership (三81、三19、三07、三48、三49、三58、三54、三55). Rewrote
  all four core dialogues/readings and their 24 comprehension questions;
  regenerated exact text-derived gap fills. Added 59 independent word contexts
  so the stricter two-distinct-context rule continues to hold without padding
  the friends' speech. Original media and older notebooks/examples/tasks are
  still subject to the remaining editorial audit; this is not a blanket
  naturalness acceptance of the whole unit.
- Fixed real gate failures: the scene rewrite removed some required retrieval
  contexts; supplied independently authored contexts and retained the rule.
  A browser selector also counted two different lists together; scoped its
  seven-level assertion to the full roadmap and added a separate three-skill
  assertion. No threshold or check was removed.
- All eight gates pass: packs/readability/pinyin, types, content/audio, unit
  tests (157), playback review, development browsers (39 passed; production-only
  three run separately), build, production browsers (3 passed). Receipts:
  `output/gates/batch-37-final-*`. SHA-backed installed voice catalog has
  29,566 files and zero missing files. Automated recognition is not a native
  tone or naturalness certification.
- Native flags: 笑什么啊 and 别问了 teasing force; 怪不得/好不好 delivery;
  neighbour volume requests; 一快就乱; singing diction; inferred character
  intent versus an explicitly stated reason. Every line remains AI-assisted
  with native review pending.

### Parity repair batch 38 acceptance — 2026-10-07

- Accepted editorial corrections in s3-u37–40, preserving 88 vocabulary IDs,
  progression IDs and grammar ownership: 首先/然后, 并且, 不仅/不光…还/而且,
  不是…就是, 了…就, 左右/大约/adjacent numerals, 都…了 and X就X点儿吧.
  Core dialogues/readings, original media, comprehension keys, tasks, role-play,
  usage and selected word examples now follow real bookshop planning, course
  schedules, shared trip costs and a retirement gathering. Added 42 independent
  contexts; every vocabulary entry retains two distinct retrieval contexts.
- Applied source-sense fixes: 任 is the allocated regardless-of conjunction;
  升 is the rising verb rather than a litre measure; 环 is a concrete ring.
  Removed unnatural 绕湖一环 and corrected抱 to holding rather than confusing
  it with 抱歉. Cost arithmetic stays 120/4 + 180/4 = 75. Glosses supply actual
  meanings; no readability or pinyin requirement was reduced.
- All eight gates passed: packs/readability/pinyin (62,253 matched words, zero
  pinyin problems), types, content/audio, 159 unit tests, playback review,
  development browsers (39 passed), build and three production browser checks.
  The three production-only cases skipped in development ran separately and
  passed. Receipts: `output/gates/batch-38-final-*`.
- Installed catalog: 30,136 provenance-matching files, zero missing files.
  There are 211 direct dated audio exceptions and 44 dependent texts, reported
  as 255 device-voice texts. Each unresolved take had the real repair round;
  none is marked reviewed. Automatic recognition and acoustic flags are not
  native pronunciation certification. Build imports verified 108 units and
  11,996 retained audio texts; optional voice chunks total 706.6 MiB.
- Native review: 并且 in friendly banter; choices of old-man wording 老头儿;
  任 as concession rather than appointment; trip-cost dialogue and 值得;
  resigned 就…点儿吧 delivery; blood readings and respectful retirement/death
  vocabulary. Earlier notebooks and unchanged examples remain in the broader
  naturalness audit; this batch is not a blanket native acceptance.

### Advanced unpublished draft review — 2026-10-07

- HSK 4 u05–08 and u09–12: original verse practice, course schedule, practical
  work help, film disagreement, transport repair, bounded refusal, contextual
  teasing and a scene retelling. Replaced unrelated reply alternatives and made
  scored premises explicit in both languages. No protected runtime file changed.
- HSK 5 u01–04: altered promises, reassurance, figurative original song and
  drama information timing. U05–08: social trade-offs/boundaries, workplace
  proposal and contingent event organisation. U09–12: qualified interview,
  opinion/evidence, irony/repair and performance interpretation. Each has 24
  word records, five cards, two 600-plus-character readings and thirteen tasks.
  Word records include earlier retrieval and repeated senses, not all new words.
- HSK 6 u01: 32 word records; 虽…但/却, 就算…也, 不但没有…反而, 那倒也是,
  X就X吧 and state/recollection 下来/起来. Twenty-four scene turns, two separately
  authored 900-plus-character perspectives and seventeen tasks. Friday18:00
  invitation/18:10 reply and Saturday14:05 question/14:12 answer/14:30 arrival
  remain distinct; next Thursday18:00 arrival is checked at17:30.
- Twenty-five unpublished drafts pass schema, two independent retrieval contexts
  and word readability99–100%; draft-directory pinyin49,527 matched words,
  zero fixes,264 unchecked characters. These are preflight results, not the
  mandatory audio/types/unit/browser/build acceptance. Audio batch39 is active;
  it pins only HSK4u01–04, which are not yet accepted or deployed.
- Self-review fixes: opinion64 visits is not64 unique people;2 staff ×2hours ×
  4evenings=16staff-hours combined. Confirm room before announcement; update
  existing paper/email/webpage separately.24 seats fit24 guests because28total
  includes4organisers. In irony, understanding intent and liking a name differ;
  a later voluntary joke does not cancel a stop request. In performance, a
  corrected detail changes evidence without forcing aesthetic agreement.
- Native review remains pending: X归X; lyric images/rhythm; indirect reassurance;
  teasing and X什么X strength; 从而/加以 register; interview cadence; apology
  and restrained comeback wording. All remain AI-assisted drafts. Neither this
  log nor machine dictionary/transcription checks assert native naturalness.

## Batch 39 — s4-u01–04 accepted, 7 October 2026 evening

- Four original media/social units: new-group meeting, a compliment versus a
  joke, a rainy gathering with fallback and shared costs, and a missed drama
  line. Sixty-four word records include earlier retrieval; they are not all new
  level-four source entries. Cards cover contextual questions, connected causes,
  uncertainty and retelling. Source rows and actual senses remain in the packs.
- Audio generation, transcription screen, one genuine repair, rescreen,
  documented deferral, mastering and review completed. Catalog contains 12,639
  covered texts and 31,192 files with matching provenance. There are 218 direct
  dated exceptions plus dependent assembled readings: 265 fallback texts. No
  deferred line is marked reviewed. Other gates remain strict.
- The first browser run caught four ambiguous notebook selections: all notebooks
  were titled Independent situations. Applied meaningful unit-specific English
  titles and Chinese 词语练习 titles; recompiled the four packs. The manifest count
  stayed unchanged. Source part-of-speech categories are retained without
  guessing a category for blank inventory rows. First-attempt logs are preserved
  in output/gates/batch-39-first-attempt/.
- Final rerun passed packs/pinyin/readability, types, content/audio, 160 unit tests,
  playback review, 39 development-browser tests, production build and all three
  production-only browser tests. Receipt: output/gates/batch-39-final-receipt.json.
  No production-only check was left skipped as acceptance evidence.
- Installed-data round trip retains all fields in 112 units and 12,374 installed
  audio texts. Course text is 2,607,111 bytes, catalog 1,386,755 bytes; deployment
  audio 747.2 MiB in 95 chunks and 2,639 static files. Existing MP3 encoding is
  unchanged. These are local accepted artifacts, not a deployed checkpoint.
- Native checks still requested: joking 你笑什么啊/怕什么啊 register, the invitation
  refusal and quantity banter, connected speech and perceived prosody. Automatic
  transcript matches do not certify those qualities.

## Advanced draft checkpoint — through s6-u07 (not publication acceptance)

- Thirty-one drafts: s4-u01–12, s5-u01–12 and s6-u01–07. HSK6 units2–7 develop
  indirect requests, source-limited incident accounts, a final rehearsal and
  farewell, shifting lyric address, a professional disagreement and multi-person
  chronological retelling. Each has 32 word records, six cards, 24 dialogue turns,
  two independently authored 900-plus-character readings, original media and
  seventeen mixed tasks. Vocabulary contexts are separate from the main scene.
- Applied fixes: replaced mistaken English words inside Chinese prose; added
  real definitions for unsupported characters; replaced 嗯 where its syllabic
  reading does not fit the existing schema, without changing that schema;
  rewrote an uncertain construction instead of teaching it speculatively;
  fixed examples whose inflected/different measure did not actually retrieve the
  introduced headword; removed a second plausible negative answer from a farewell
  question. All notebook titles identify their unit.
- Schema, independent contexts and word-readability preflight passes all31;
  draft-directory production pinyin checker reports72,797 dictionary matches,
  zero lines to fix and584 unchecked characters. Subsequent small edits to
  s6-u01/05 must be rechecked before publication. Preflight is not audio or full
  release acceptance; only s4-u01–04 are accepted in batch39.
- Native flags include apology timing, corrective 罢了, photograph/face teasing,
  X是X and 放着X不Y register, original lyric rhythm and address, rhetorical
  不是…还 questions, workplace/calendar banter, distributed descriptions and
  colloquial chronology. Every advanced pack remains an AI-assisted draft with
  native review pending. No mastery or comprehensive advanced coverage claim.

## Advanced editorial checkpoint — all 36 core drafts (7 October 2026)

- All s4-u01–12, s5-u01–12 and s6-u01–12 have authored source, substantive scenes, independent vocabulary contexts, grammar cards and mixed tasks. Higher readings are independently authored: HSK5 >=600 Han characters each, HSK6 >=900 each. This is the selected media/social route, not full GF2021 lexical inventory.
- Newly authored s6-u08–12 cover film-club participation and causal limits; feature/notice reading; useful discussion and specific consent; casual speech ellipsis and missed clauses; original scene/verse retelling and practical promises. Each has32 word records,6 grammar cards,24 dialogue turns,2 long readings,12 media lines and17 tasks.
- Applied fixes: defined missing gloss words, replaced unsupported syllabic 嗯 with natural replies without changing the schema, lengthened the listening unit with actual referent and partial-viewing events, kept lexical 乐曲 yuèqǔ / 主角 zhǔjué / 收藏 shōucáng / 待会儿 dāihuìr readings, and changed the unnatural 一声雨落 line to 雨声轻轻落在门前.
- All36 draft schemas, independent retrieval contexts and word-readability checks pass (99–100%). Draft pinyin check:88,965 dictionary matches,699 unchecked characters,names etc.,0 lines to fix. These are prechecks, not audio/release acceptance.
- HSK4 bank draft has90 original items (60 checkpoint/30 sample),including two-text comparisons in the existing reading mode. Full bank validator reports0errors; native/English editorial review and audio/release gates remain outstanding. Above-level wording was rewritten,not accepted by loosening the gate.
- Batch40 first attempt detected a stale compiled-course audio manifest before release. Fixed the orchestration to compile new packs before collecting audio; restarted the affected batch. Old logs retained in output/gates/batch-40-first-attempt. No missing line was silently exempted.
- Native flags: lyric collocations and rhythm; friendly bus/door/applause/alarm/letter jokes; 非全称 and双重否定 scope; association and event-notice register; referent repair and 核实/让步 forms. All content remains AI-assisted with native review pending.

## Advanced batch 40 accepted locally — 8 October 2026
- s4-u05–08 passed all eight receipt checks, including development navigation and production offline tests. Source notes record the editorial repairs and native-review flags. Audio-only unresolved takes remain explicitly unreviewed. Receipt: output/gates/batch-40-final-receipt.json. No commit or deployment is implied.


## Editorial and exam checkpoint — 8 October 2026, unpublished work

- HSK 5 and 6 each have 90 original bank drafts (60 checkpoint, 30 sample), with reading, listening, cloze and ordering. The unchanged word-level/pinyin/answer validator passes both. They have not yet been published, voiced, accepted or deployed. HSK 4 bank is published for batch 41, which is still generating audio.
- Exam fixes: removed above-level wording without waiving the lexical ceiling; preserved numbers, chronology and intended answers; repaired ordering choices that could form a second valid sentence; corrected English translations and the old/new entry-card scene. All assessments remain adapted practice with native review pending, not official mock papers or graded writing certification.
- The bank validator now handles the dictionary's u: spelling of ü, matching the existing content pinyin check. Regression tests require the right vowel, tone and level. No pronunciation or word-level requirement was relaxed.
- Manual grammar evidence is installed only for existing cards. Multi-form families remain partial when their other forms are unowned. Advanced lexical coverage remains incomplete and is reported separately from the selected media/social route.
- s3-u29–32 have authored replacement scenes, readings, two independent contexts per target and preserved task IDs. Character speech no longer analyses grammar or adds permission/model disclaimers. Preflight: all 120 source packs pass, word readability remains >=95%, and 77,248 dictionary word matches have zero pinyin problems. Only an ignored shadow tree was changed. Their new Sayo audio and full acceptance remain outstanding.
- Removing incidental earlier character exposure exposed two later glossary dependencies: 藏 in s3-u34's media scene and 依赖 in s4-u08's reading. The queued repairs add the actual meanings at those later uses and preserve their lines and IDs.
- Native flags: liǎo in 没完没了; 功夫/工夫 register; lamp 卡/转; informal travel teasing and 嘛; 信 as trust, not a letter noun; higher-bank pragmatic inference and the lyric's shifting 你 referent. Every authored Chinese line remains pending native review.

## Reading and progress checkpoint — 8 October 2026 (not release acceptance)

- Advanced drafts now contain 57 level-four, 67 level-five and 53 level-six explicit character recognition entries. Each states a source reading, an authored meaning, real stroke count and connected word examples. Contextually different readings do not inherit credit: yù in 参与 does not introduce the source yǔ reading of 与. All 36 draft packs pass the unchanged word/readability and pinyin preflight; these entries still await publication/audio/full batch checks.
- HSK 4 character entries will be installed in four-unit batches 51–53, preserving every other accepted content field. HSK 5–6 entries travel with their own core batches. The course remains a selected advanced media/social route, not comprehensive advanced vocabulary coverage.
- Main progress backups now include the existing separate HSK notebook, with prevalidation before any import. Existing exam runs win by ID, and older backups leave the exam notebook intact. Three focused backup tests and types passed. Database names and keys did not change. HSK cloud sync is still not implemented and is now stated explicitly in the notebook footer.
- Public Kiyo recognizes the owner's Google session. Cloud sync remains paused according to the owner's keep-on-device decision. No upload, deletion or merge was performed. A read-only cloud connection probe uses existing owner authorization and SELECT permissions; it does not call the state-creating pull RPC. Three focused probe tests and types passed; actual live verification awaits deployment.
- Applied a final HSK 4 room-comparison bank repair: distractors now express plausible but unsupported agreement/cancellation/capacity inferences instead of an absurd infinite-room choice. Draft validator passed; this correction joins batch 51 audio and acceptance.
- The five protected dictionary/drill/pack files have no diff in this run. No sibling source was changed. Full release gates and clean-checkout verification remain outstanding for these additions.

## Advanced batch 41 accepted locally — 2026-10-08 05:30 UTC

- Units: s4-u09 (16 word records), s4-u10 (16 word records), s4-u11 (16 word records), s4-u12 (16 word records). Word records include retrieval; not all are new source entries.
- Actual grammar cards: s4-u09: 除非…否则…; 万一…; 才 / 就 with time; 免得 | s4-u10: 不是不…，而是…; 怕…才…; 哪怕…也…; 比 + vague action + 更 / 有用 | s4-u11: 可真 + predicate; 怪…的; 才不 / 才不要 + 呢; 还没…怎么… | s4-u12: 于是 / 因此; 从此 / 后来; 先…又…再…; 不是…只是不….
- Self-review: travel deadline and delayed arrival, friendship-preserving refusal, exaggeration versus stated events, and cause/outcome retelling. Authored fixes and native flags remain in each pack's notes.
- Repairs: added the missing 松 meaning; reused completed takes after GPU memory exhaustion at batch width eight and completed generation at width four. Real failed takes received the configured repair and explicit unreviewed audio-only exceptions.
- All eight checks passed after correcting an outdated offline test that tried answering a listening item before playback. The revised check now saves real question audio, reloads offline, waits for playback before answering, and verifies persistence. No application guard, gate threshold or content criterion was weakened.
- Evidence: output/gates/batch-41-final-receipt.json; 167 unit tests, 43 development browser tests and all 3 production/offline tests passed; production build and installed-data/hash checks passed.
- Native review is pending for every authored line. Acceptance is local; commit, push and deployment remain separate.

## Further unreleased HSK 6 naturalness fixes — 8 October 2026

- s6-u05 and s6-u11: removed voice-identity/tuning language that echoed the production conversation. Replaced it with friends comparing two performances, joking about an overlong voice message and agreeing on an address.
- s6-u07: replaced abstract claims about knowledge and permanent character judgments with a practical group update, an avoided basement trip and five pages kept together.
- s6-u10: replaced commentary about teaching a table method with an actual Friday 6 p.m. reply deadline and people asking the performers.
- Exact task anchors and IDs remain intact. All 144 shadow packs pass the unchanged pinyin/readability validator; preflight output/advanced-naturalness-preflight.log. These four drafts still await their published-batch audio and full gates. No native approval is claimed.
- s6-u10 timing follow-up: the added specific reply is Thursday 6 p.m., consistent with the original before-Friday commitment; Friday venue confirmation remains separate. Task anchors and IDs are unchanged.

## Character batch 51 accepted locally — 8 October 2026

- s4-u01–04: 30 explicit character recognition entries; existing word, grammar, task and lesson IDs preserved. Source readings and bound meanings match the shown connected words; usage aids do not claim etymology.
- Applied early fixes: 觉 jué uses 觉得; 兴 xīng uses its separately screened take; 识/候 notes distinguish neutral connected syllables. Corrected three HSK 4 comparison distractors while preserving answer keys and IDs.
- Stronger real-browser checks found and repaired the advanced saved-run validator, which rejected levels above 3. Installed HSK 4–6 banks now validate with exact bank/level membership; backup/restore and wrong-level rejection have regression tests. The character playback test accounts for automatic wall-cell playback before checking its cached replay, and optional character metadata follows the schema.
- All eight strict gates passed: output/gates/batch-51-final-receipt.json. Earlier failures remain in batch-51-first/second-attempt files. Source is fingerprinted after production/offline checks.
- New takes were generated, screened and repaired. Remaining documented device fallbacks remain unreviewed. Automatic recognition is not a certificate of pronunciation or naturalness.
- Native review remains pending for all new definitions, contextual readings and exam inferences. This is local acceptance, not deployment.

## Earlier naturalness extension queued — 8 October 2026

- Direct reading of s3-u21–28 found report-like speech, assessment-policy cautions and awkward lexical collocations. Added two four-unit editorial batches (54/55) after the already queued corrections.
- Draft batch 54 rewrites s3-u21–24 with a wet delivery, friends catching up on a television show, cooking noodles with chilli on the side and a mistaken date. Every target has two independently authored contexts; factual question anchors and old IDs are preserved. Formal media/rules vocabulary lives in independent written-register examples.
- Applied self-review fixes: 具有 uses an ordinary formal collocation; 念 no longer creates an accidental 信念 segmentation; the false date task now contradicts its own heard line rather than relying on missing earlier context.
- Unchanged all-144-pack shadow preflight passes, including pinyin and >=95% word readability: output/parity-repair-06-preflight.log. Removed incidental exposure requires explicit later meanings for 与, 单独, 平稳, 疑问, 符合, 区域/扫, 拥有, 采纳/依赖 and 款. Those patches preserve all later lines, IDs and characters and generate no new speech.
- Batch 54 is not accepted or published yet. Full audio, repair/exception handling and all eight gates remain mandatory. Native flags include colloquial passive 叫, lively 活, laughter 乐 and formal collocations.
- Unreleased s5-u08 now replaces broad cautions about scanning and permanent judgments after a sorting mistake with an older visitor using the paper notice and a friend returning a dictionary to the right table. Task facts remain intact; audio/full gates await batch 43.

## Earlier editorial batch 55 draft preflight — 8 October 2026

- s3-u25–28: 88 retained word records with two independent contexts each; practical scenes about a classmate's article, film venues in rain, a misleading photo distance and adult beginner swimming lessons. Six text questions per unit and nine or ten mixed tasks have checked anchors; all prior unit/word/task IDs stay intact.
- Applied self-review fixes: 程度 describes degree of understanding rather than unnatural 汉语程度; 班级 includes 里; 精神 as perseverance uses jīngshén, while s3-u24 energetic 精神 uses jīngshen; changed an impossible inside/outside waiting joke and the English narrative tense; 录音 uses ordinary 声音太小. Listening true/false claims contradict or confirm their own heard line, not missing earlier context.
- All 144 combined shadow packs pass the unchanged pinyin and >=95% word-readability checks: output/parity-repair-07-preflight.log. Restored concrete later meanings for 阅读, 固定, 扩大, 几乎, 翻译, 鼓励, 绕, 临时, 咨询, 眼镜, 模型, 与, 结构, 挥 and 犹豫 where removal of incidental exposure made them unavailable. These are glossary definitions at actual uses, not coverage claims.
- Native flags: friendly teasing in the article/photo exchanges; 好是好，就是 concession; 大主语/小主语 wording in retained grammar; 起 and elapsed 了; 精神's contextual reading; bound 录 in 录入; realistic pool-class descriptions. Every new line remains AI-assisted and pending native review.
- This is a draft preflight, not published acceptance. Audio generation/screening/one real repair, dated unreviewed exceptions and all eight batch gates are still required.

## Character batch 52 accepted locally — 2026-10-08 06:53 UTC

- s4-u05–s4-u08: explicit authored glyph meanings, official contextual readings and connected taught words added. Existing unit, vocabulary, task and lesson IDs and all other content were preserved.
- Self-review: character readings must match both the official glyph entry and the shown word; incompatible polyphonic contexts are excluded from that reading's coverage. Stroke counts use the existing stroke data. Usage notes do not invent etymology.
- All eight strict checks passed: output/gates/batch-52-final-receipt.json. New audio followed the same generation, screening, repair and dated unreviewed fallback policy.
- Native review pending for all new recognition definitions and recorded contextual tones. These entries are recognition instruction, not new dedicated character lessons or learner mastery.


## Contextual pinyin repair found during batch 53 — 8 October 2026

- Direct review found 没收到 (not received) had been incorrectly generated as mò shōu dào through a longest-match overlap with 没收 (confiscate). Corrected 12 stored Chinese/pinyin records across s2-u09, s2-u23, s3-u04, s3-u21, s3-u32 and s3-u40. The Chinese texts, audio keys, question IDs and meanings are unchanged; the speech engine already receives Chinese text.
- Future authoring now explicitly treats 没收到 as méi shōu dào. Editorial serialization also repairs retained grammar examples. A data-wide regression checks every installed occurrence, rather than claiming the generic dictionary checker can determine all contextual readings.
- Batch 53's full checks must pass after this correction. It is not separately marked accepted until that complete receipt exists. Native review of the actual recorded negative reading remains pending.

## Earlier editorial batch 56 draft preflight — 8 October 2026

- s3-u01–04: 88 retained word records, 176 independently authored lexical contexts and ordinary connected scenes about group introductions, a quiet first reading turn, a one-hour volunteer shift and a shared photocopying favour. All prior IDs are retained. Nine task replacements per unit have explicit factual anchors; the false listening claim contradicts its own played line.
- Self-review fixes: Xiao Li is 李宁 in the displayed speaker roster; 陈宇 handles the entrance in both the volunteer scene and reading; four friends get four seats; the cat follows despite no food; an impossible inside/outside formulation is removed. Preserved grammar examples receive the negative 没收到 correction. Bound suffixes 者/员 have separate contexts; 志愿 retains its aspiration/application sense outside the casual scene.
- Unchanged combined shadow preflight passes all 144 packs, pinyin and >=95% word readability: output/parity-repair-08-preflight.log. Later glossary definitions for 陪, 邀请, 打招呼 and 允许 replace incidental exposure; no later sentences or IDs change.
- Queued batch 56 after the prior editorial batches. It is not published or accepted yet; the complete audio and eight-gate pipeline remains mandatory. Native flags: forms of address, 志愿 sense, bound forms, 怕是, 亲/亲切, 留个位子/接班, cat/chair teasing and actual negative 收到 tone delivery. All lines remain pending native review.

## Editorial batch 57 draft preflight — 2026-10-08

- s2-u29–u32: 88 existing word records, with 176 independently authored notebook contexts; newspaper acquaintances and Spring Festival plans, a short visit with a novel and a forgotten scarf, a moving cat and an exhibition, and a group visiting a sister's tea shop.
- Self-review fixes: corrected the artist's speaker labels, explicitly contradicted each false listening statement in its own heard line, separated the inclusive count senses of 以上/以下 from “the following”, kept 得 dé and 长 zhǎng contexts, and corrected 画儿 to single-syllable erhua huàr. Later glossary dependencies are defined without changing those later lines or any IDs.
- Combined unpublished 144-unit pack/readability preflight passes; separate pinyin check: 162,150 dictionary matches, 591 unverified characters, 0 problems. Logs: output/parity-repair-09-preflight.log and output/parity-repair-09-pinyin-preflight.log. This is not audio acceptance, native review or deployment.
- Native review flags: suffix 家; 老/小 forms of address; 等 list suffix; 成/成为/实现; inclusive age bounds; 得 dé; 长 zhǎng; concrete medicine nouns; school-subject 科; 画儿 and light teasing. No claim that machine checks certify spoken naturalness.

## Character batch 53 accepted locally — 2026-10-08 07:29 UTC

- s4-u09–s4-u12: explicit authored glyph meanings, official contextual readings and connected taught words added. Existing unit, vocabulary, task and lesson IDs and all other content were preserved.
- Self-review: character readings must match both the official glyph entry and the shown word; incompatible polyphonic contexts are excluded from that reading's coverage. Stroke counts use the existing stroke data. Usage notes do not invent etymology.
- All eight strict checks passed: output/gates/batch-53-final-receipt.json. New audio followed the same generation, screening, repair and dated unreviewed fallback policy.
- Native review pending for all new recognition definitions and recorded contextual tones. These entries are recognition instruction, not new dedicated character lessons or learner mastery.


- Advanced HSK 4 selected media/social core release: committed f012545e75e01695727c33f99fa22a0f37b0cc4c; clean checkout npm ci and build passed; pushed to origin/main and deployed. Live browser verification remains separate. Full vocabulary inventory and independent native review are not claimed.

- Draft editorial batch 58 (s3-u05–08): independently authored file/date correction, dinner for four, six-person reading group and song/concert practice; 88 vocabulary records each have two independent notebook contexts. Combined draft packs/readability and pinyin pass; actual audio and eight acceptance gates remain pending. Self-review corrected 在路上 and referred to the singer/band as 他们 rather than loosely calling them 演员; retained all old task and word IDs. Native flags: 富/整 bound senses, classifier 行/架/支/只, 相当 and 比较 senses, 证明 examples, 倒是 and pen-as-microphone teasing.
- Unpublished advanced s6-u05: replaced five disclaimer-like lyric interpretation paragraphs with concrete listening, rehearsal and childhood-memory scenes. Original lyrics and question facts retained; both long readings still meet the unchanged length gate. Combined draft packs/readability passed. Actual audio and complete batch acceptance remain pending; native check requested for narrative/register and sung-versus-spoken interpretation.

- Draft editorial batch 59 (s3-u09–12): last two Saturday tickets, a relocated bookshop, a short riverside walk, and a two-person rehearsal. 88 existing vocabulary records each receive two independently authored contexts. Combined 144-pack draft/readability validation and pinyin check pass (0 pinyin problems). Self-review fixed the walk duration estimate, replaced a question that presumed the passer-by was a neighbour with an explicit bridge-location question, and aligned speaker roles and renamed the bookshop unit to match its new scene. Old task/word IDs retained. Native flags: written 仅/已/变为/至今, 空 kōng versus kòng, 有的是, 往往/总是, 采取/采用, 成果/成就 and friendly teasing. Audio and eight full acceptance gates are queued, not yet passed.

- Draft editorial batch 60 (s3-u13–16): rain-plan lunch, old cancellation image, student-union exchange, and moving a desk/books. 88 existing words each have two separate contexts; old task IDs preserved. Combined 144-pack/readability gate and pinyin pass, 0 pinyin problems. Corrected the false listening statement to be contradicted by its own final clip, explicitly assigned host Xiao Zhou, speaker positions for upstairs directions, and tools versus books in small/large boxes. Added actual later-use glossary definitions for 古, 一模一样 and 组织. Native flags: 保险 safer/insurance, written 仍, 恐怕, 难道, student titles 部长/主任, representative/token 代表, 朝 cháo and 背 bēi, directional complements and teasing. Audio and all eight acceptance gates remain queued.

- Draft editorial batch 61 (s3-u17–20): quiet tea/book meeting, Grandma’s opera stories, wrong gate apology, birthday book bag/photo card. 88 word records receive two independent contexts, IDs preserved. Combined 144-pack/readability and pinyin gates pass, 0 pinyin problems. Self-review removed awkward 向她问 and 背书不够大, dropped the forced eat-questions joke, aligned speakers/recipient, and updated the opera title. Definitions added for removed incidental introductions at actual later uses. Native flags: 感情/情感/感受, 自主/客观 register, 民族/中华民族/华人, 文明 civilisation/courteous, printed 由于/因此/声明, 补/完善, 创作/创造/创新, 适用/应用, 想得美 and 塞给. Audio and eight full acceptance gates remain queued.

## Editorial batch 62 drafted — 2026-10-08

- Units: s2-u04, s2-u07, s2-u23, s2-u25. All 88 existing vocabulary and 36 task IDs retained; the grammar families remain the existing cause/question forms, colour/adjective descriptions, favour/education expressions and concession/result/request forms. No claim of added coverage or learner mastery.
- Fixed restaurant conversation that sounded like a survey, outfit dialogue with assessment-policy commentary, printing favour with an abstract consent lecture, and activity-room complaints that narrated policy instead of solving an actual problem. Restaurant wait is twenty minutes last week and ten this visit; departure six, ride ten plus walk five. Blue outer layer, white inside, undried yellow garment, red scarves with different shoes. Print pages two/three at two, handover three, Saturday event two. Activity-room clock chimes normally at four; Saturday meetup three. True/false statements checked against their own audio clips.
- Kept usable vocabulary examples and fixed specific awkward ones. Independently authored second context for each word; education/behaviour/action terms use appropriate separate situations. Removed scenes' inherited character dependencies gained contextual definitions in later units; no gate was weakened.
- Unchanged combined packs/readability and pinyin preflight: 144/144 packs, zero errors, all word readability >=95%, zero pinyin problems. Evidence: output/parity-repair-14-preflight.log. Draft only: generation, audio screens and full eight-gate acceptance are queued.
- Native review flags: beneficiary 为; 取得成绩/同意 versus 拿到; 教师/教育/教学/中小学/年级 register; playful 求; 满意/不满/好处/坏处; adjective/色 variants; 站住 request strength; formal 受到/行动/行为 and colloquial 挺好. Not marked native-reviewed.

## Editorial batch 63 prepared — 8 October 2026 (not accepted)

- Four units: s5-u01–04, 96 retained word records and existing grammar cards.
- Independently authored paragraph edits replace moving/singing policy lectures
  with calls, unpacking, dinner plans, missed-song jokes and concrete follow-up.
  Lyric interpretation remains a valid text type; it is not forced into dialogue.
- Applied self-review fixes: Lin An's pronoun continuity, removed an invented
  roadworks detail from the short-drama summary before acceptance, retained all
  assessed times/events and rebuilt passage gaps. Removed incidental earlier
  偶尔 exposure now has an explicit later-unit definition in s5-u06.
- Combined draft check: 144/144 packs, zero errors, word readability ≥95%, zero
  line-pinyin problems. Both advanced readings still exceed 600 Han characters.
  Audio and the eight batch acceptance gates remain pending in the queue.
- Native flags: water-box moving banter; 搬/抬/卷起 collocations; applause and
  self-deprecating jokes; plausible lyric interpretations and mainland diction.
  No line has been marked native-reviewed.

## Editorial batch 64 prepared — 8 October 2026 (not accepted)

- s5-u05–08: retained 96 word records, grammar cards and every task/question ID.
- Rewrote calendar/call diaries and book-event paragraphs as events and ordinary
  banter. Retained genuine formal meeting-time analysis, the 48-minute total,
  unrecorded old preparation, and two-person extra discussion. Half-hour travel,
  8:30 coat reminder, nine/eleven call times, twenty-minute trial and display-only
  book remain consistent with the assessment. Later 劝 usage gained a definition
  where an incidental earlier occurrence was removed.
- Draft-only combined preflight passed 144/144 packs, zero errors/pinyin problems,
  readability ≥95%, and both long readings ≥600 Han characters. Audio/full eight
  acceptance gates pending. Native flags: 塞得太满, 哪有, phone teasing, spoiler
  banter and mainland diary register. No native-reviewed claim.

## Editorial batch 65 prepared — 8 October 2026 (not accepted)

- s5-u09–12: 96 existing word records and grammar retained; original task,
  question and speaker IDs preserved. Soup scene still has three actual speakers.
- Repaired three dialogue lines and their exact task-audio references. Rewrote
  awkward friendship/permission lectures in the cook/newcomer readings as dinner
  events, remembered teasing and follow-up messages. Interview notices, public
  feedback and literary analysis retain their legitimate text types.
- Self-review verified two salt additions, newcomer without taste context,
  stop/apology/cook's own joke, bad-weather irony versus sincere enjoyment,
  five stated classmates, and short/full clip mishearing. Added actual definitions
  for utensils/actions and feedback. Rebuilt passage gap fills.
- Draft preflight: 144/144 packs, zero errors, words ≥95%, zero pinyin problems;
  both extended readings ≥600 Han characters. Audio/full eight gates pending.
- Native flags: salt-bowl joke and 汤救回来, 真有你的/可真 prosody, X什么X
  strength, phone/short-clip mishearing and mainland casual dialogue. No native
  approval is claimed.

## Editorial batch 66 prepared — 8 October 2026 (not accepted)

- s6-u01–04: retained 128 word records, grammar and question/task/speaker IDs.
- Repaired formal-sounding apology/photo utterances and exact task references.
  Revised calendar/camera, borrowing and farewell paragraphs as actual actions;
  corrected the umbrella role (Chen Yu follows Lin An) and provided 稍后 meaning.
- Self-review: 2:12 reply, two versus 2:30, Thursday six/5:30, fifteen-minute
  introduction, three remaining browsing books and Saturday-before-five return
  remain consistent. Last-evening help is shared; return dates remain uncertain.
- Draft-only combined preflight passes 144/144 packs, zero errors/pinyin problems,
  words ≥95%; both long readings ≥900 Han characters. Audio/full eight gates
  pending. Native flags: 咽回去, deadline/table-lifting banter, 台词/告别 register,
  photo eyewitness language and chronological retelling. Nothing native-approved.

## Editorial batch 67 prepared — 8 October 2026 (not accepted)

- s6-u05–08, 128 retained word records, grammar and question/task/speaker IDs.
- Revised singing instructions, spreadsheet-trial narrative, bag investigation
  and film discussion. Work/calculation text stays formal where appropriate;
  friends stop talking like assessments. Original refrain and earlier corrected
  seaside-reading material retained.
- Self-review verified twenty→thirty equals ten percentage points/fifty percent
  relative; five manuscript pages, corridor fourth page, upstairs recovery and
  crease; 9:45 discussion end/10 closure and cleanup interval. Exact changed
  dialogue references update their task audio, while old IDs stay valid.
- Combined draft checks: 144/144 packs, zero errors/pinyin problems, words ≥95%,
  both long readings ≥900 Han characters. Audio/full eight gates pending.
- Native flags: wind-kept lyric joke, 原稿心疼, manuscript handling collocations,
  percentage-point register and follow-along singing omissions. Native pending.

## Editorial batch 68 prepared — 8 October 2026 (not accepted)

- s6-u09–12 retain 128 word records and all grammar, speaker and assessment IDs.
- Revised library timing, work confirmation, phone/menu humour and farewell
  chronology. Notices and practical work analysis retain their appropriate register.
  Arrival is the following evening; the actor's train ticket is dated, while the
  unopened letter and future reunion remain uncertain.
- Self-review checked next week versus tonight, Friday deadline/Thursday six
  confirmation, the ten-minute estimate after the bus arrives, 8:30 meeting and
  nine departure. Questions still distinguish services from opening hours and
  character events from the actor's actual travel.
- Combined draft preflight: 144/144 packs, zero errors and pinyin problems,
  word readability ≥95%; both long readings ≥900 Han characters. Changed audio
  and the complete eight gates remain pending.
- Native flags: book/overtime joke, phone-food ambiguity, programme confirmation,
  lyric interpretation and farewell banter. No native approval is claimed.

## Avoiding duplicate advanced synthesis — 8 October 2026

- Authored editorial sources 16–20 now finalise their four-unit group before
  its first audio collection: advanced batches 43–47 respectively. All eight
  gates still run on each group's revised published text and generated audio.
- Prepared editorial batches 64–68 are therefore incorporated into 43–47;
  they are not independently accepted or separately required for the final run.
  Explicit manual reruns remain available. Batch 63 remains queued because
  batch 42's older readings were already being synthesised.
- Definition dependencies never publish a future unit ahead of its turn.
  Source 18 carries 劝 itself when s6-u04 is actually published.
- This changes synthesis order, not any gate, review status or curriculum ID.
- Changed-task audit additionally restored explicit pricing deferral in s6-u06
  before first publication: the original false pricing item still has direct
  support in its listening audio. Pinyin/readability preflight remains clean.

## Receipt storage optimisation — 8 October 2026

- Mastering provenance and speech-screen checkpoint JSON omit indentation only.
  Every text, source hash, transcript, status and timestamp field is preserved.
  Clip encoding and the transcription decisions are unchanged. Subsequent audio
  steps and content validation read these records normally.
- Per-clip checkpoints remain atomic; no screening work is skipped to gain speed.
  Final sizes will be measured after the next install.
- Advanced exam self-review removed the duplicated phrase 文章原来的文章 from
  the HSK 6 attendance item before publication. Its count, answer and item ID
  are unchanged; all 90 draft items passed the strict publication validator.

## Advanced batch 42 accepted locally — 2026-10-08 12:01 UTC

- Units and grammar cards: s5-u01 (24 word records): 毕竟; 明明; 倒是; 尽管…但是 / 仍然…; 不是…，而是… with a specific concern | s5-u02 (24 word records): X归X，Y…; 再…也…; 动词 / 形容词 + 得 + clause; 在…看来; 先…还是…再…? | s5-u03 (24 word records): 随着…，…; 不是…，而是…; 既…，也…; 不一定…; 把…带进 / 装进… | s5-u04 (24 word records): 直到…才…; 原来…; 再…也不 / 没…; 不然…; 把A当成B. Word records include retrieval and are not all newly distinct source entries.
- Self-review and applied fixes are recorded in each authored pack. Removed unused blank/distractor audio demands by matching the actual study/playback screen; every playable sentence still requires its recording or the owner-approved dated exception. Cached shared MP3s now have real completed-playback checks on every tap.
- All eight receipt checks passed: packs/pinyin/readability, types, content/audio, unit tests, playback review, development browser, build, production offline browser. Receipt: output/gates/batch-42-final-receipt.json.
- Sayo audio was generated, screened, genuinely repaired and installed before these gates. Unresolved exceptions remain dated, unreviewed device-speech fallbacks. No native or proficiency approval is claimed.
- Native flags: teasing/register, longer singing and moving readings, connected-tone delivery. First four HSK 5 readings also have the separately prepared editorial batch 63 queued; this acceptance does not claim that later revision has passed.
- Acceptance is local; commit, push and deployment are separate.

## Sequential advanced publication repair — 8 October 2026

- Batch 43 initially failed the unchanged pack gate: s5-u05 lacked a meaning
  for 圈, which blocked the later units' prerequisites. Added the contextual
  circle/mark gloss in its canonical authored editorial layer before audio.
- The former combined draft preflight could borrow meanings from future units.
  The isolated first-publication fixture now runs both pack and pinyin gates
  after each four-unit prefix, with the real dictionary and stroke references.
  It found and repaired later missing glosses for 傍晚, 逼, 堆 and 盯.
- Applied contextual pinyin repairs for 交还, 盯着 and modal 还是得 / 这回得;
  returning a borrowed object is huán, whereas still/yet stays hái. Clarified
  several not-yet-published return phrases with 还回去 / 归还 / 送回去.
  The unchanged later object-return contexts also have explicit readings.
- All five sequential advanced prefix pack/pinyin checks now pass in isolated
  draft copies. This is preparation, not audio or batch acceptance. The live
  application was not changed by those fixture runs.
- Native tone and naturalness review remains pending; exact return-object
  lines are included in the native-review candidates rather than certified.

## Connected-reading timing repair queued — 8 October 2026

- Self-review of s5-u05–u08 caught two timeline ambiguities. The first singing date in s5-u05 now says next week, matching the second-week cancellation and alternate-week plan. The s5-u06 main reading now explicitly places the confirming message before nine, matching its detail question.
- Changes are authored in parity-repair-16.py. The already-running audio batch retains its original manifest; editorial batch 64 will install these two corrected paragraphs, update referenced tasks, regenerate their audio and rerun all eight gates before the final release. This is preparation, not acceptance.
- The actual sequential pack/pinyin preflight passed at all five unpublished advanced prefixes with these corrections: output/advanced-sequential-publication-check-v4.log. Native review is still pending; no gate was weakened.

## Contextual 得 correction prepared — 8 October 2026

- An editorial audit found 357 pinyin fields across 69 packs in the combined current/future isolated corpus where 得 inherited the wrong dictionary reading. Distinguish complement de, modal děi and lexical dé. 舍不得 and 怪不得 also get the neutral bound citation forms. Preserve every other authored syllable, including telephone yāo, erhua, punctuation, Chinese text, IDs and answer keys.
- The shared contextual rule set explicitly reports unknown contexts rather than silently approving them. Four Python alignment/preservation fixtures and four TypeScript regression fixtures passed. The isolated future-publication check passed packs, dictionary pinyin and the contextual check at all five four-unit prefixes: output/advanced-sequential-publication-check-v5.log.
- Batch 43's running synthesis retains its fixed manifest. Before its final acceptance checks, the preparation hook will correct the actual corpus, rebuild the manifest and refresh the generation plan, cached screening, mastering and review provenance. All eight acceptance checks will then run normally. This paragraph records preparation, not installation or release.
- Recorded contextual 得 and returning-object 还 lines remain exact native-review candidates. Automated speech transcription cannot certify tone accuracy; no line is newly marked native-reviewed by this repair.

- Publication order refined: editorial batches 63–64 now run before the HSK 5 release, so the known date/question fixes do not wait for a later deployment. The remaining default editorial run ends at batch 62; batches 63–64 retain their full eight acceptance checks before HSK 5 ships. No audio or content gate is skipped.

- A second semantic pass caught 找得到 in s5-u01: potential “can find” takes neutral de, unlike lexical 得到 “obtain” dé. Added an explicit potential-complement distinction and a separate regression in both runtimes (now five fixtures each). All five isolated advanced prefixes passed again with that distinction: output/advanced-sequential-publication-check-v6.log. The actual-corpus correction report will record the final installed field count.

- Pre-publication HSK 5 vocabulary self-review also corrected four examples: 难得 uses 在同一天下午都有空; 神情 changes naturally rather than “认真起来”; 客气 uses a dinner invitation; 失误 describes the salty soup without a blanket judgment about the cook. Sources s5-u09/u11 are revised before their first audio generation; subsequent strict prefix and batch gates still apply. No existing teaching or assessment ID changes.

- Final preparation order supersedes the earlier queued batch-64 timing plan: source 16's two date paragraphs will install in batch 43's pre-gate hook, after its in-flight generation finishes. The hook rebuilds the manifest, generates/screens the changed takes, runs genuine repair and deferral steps, masters/reviews, then runs all eight batch-43 gates. Thus no known date ambiguity is locally accepted first. HSK 5 release still runs editorial batch 63; separate batch 64 is no longer required, because its exact source is installed before batch 43 acceptance. Native review remains separate.

### Queued editorial preflight — 8 October 2026

- Tested the next advanced publication prefixes and the later editorial revisions in isolated local copies; this preparation does not accept app batches or recordings.
- HSK 5 unit 1 revision: replaced a stale lost-hour true/false claim with the actual shelf arrangement; changed the reading question to the later dinner update; aligned the mover's she/her references, linked task and gap-fill. Existing task IDs and the false key remain valid.
- Added local meanings in later readings where removing artificial earlier vocabulary-heavy scenes removed incidental definition support. Examples include 平稳, 小厅, 摆, 区域, 估计, 挪, 稿子, 反馈 and 触动; ambiguous 弹/挑/藏 glossary readings are stated explicitly. No Chinese sentence is retained merely to satisfy coverage.
- Contextual 得 rules now include reviewed 改得早 and 高兴得 contexts. Dictionaries and ASR still do not independently certify recorded tones.
- Preparation evidence is under output/advanced-sequential-publication-check-v*.log and its preserved isolated roots. Each actual audio batch still needs all eight passing gates before acceptance or release.

- Isolated editorial preparation completed: output/advanced-sequential-publication-check-v21.log passes five advanced first-publication prefixes and all twelve queued source 03–14 revisions. All three content checks ran for each prefix/revision: pack/readability, dictionary pinyin and contextual 得. The app corpus and audio acceptance were not changed by this isolated check. Native review remains pending.

- Final isolated preflight v22 also passed all five advanced publication prefixes and source 03–14 editorial revisions after the s5-u05 naturalness fix: 暂时跟不上 replaces awkward 听不住; the newcomer asks about next week rather than the narrator declaring the newcomer's feelings. Timed departure remains 8:30, and the passage questions remain supported. This third changed paragraph is part of batch 43's preparation hook and will be regenerated and screened before acceptance. Evidence: output/advanced-sequential-publication-check-v22.log. Python and TypeScript contextual-reading fixtures each pass six tests.

- Final preflight v25 passes the same five advanced prefixes and all twelve queued editorial revisions after further HSK 5/6 naturalness review. s5-u12 now ends with two friends sharing the full/short video and replaying their preferred details. s6-u12's musician account replaces test/answer-policy leakage with concrete singing, staging, packing and next-day messages; its old true/false task retains its ID/false key and now checks that Lin An leaves without opening the letter. Related questions use passage-grounded distractors. Added the actual 拔 meaning for unplugging a cable. The new recordings and actual eight-gate acceptance are still pending; no native review is claimed. Evidence: output/advanced-sequential-publication-check-v25.log.

### Contextual neutral de transcription fix — 8 October 2026

The audio screen previously compared 地→的 only with one token per space, so ordinary word-spaced pinyin such as rènzhēn could not align. It also omitted complement 得→的 even after the independent contextual checker corrected the displayed reading. The screen now parses actual syllables and accepts only the same aligned neutral de spelling difference. 得 additionally requires the reviewed contextual rule to resolve de; modal děi and lexical dé remain failures even if a supplied pinyin field incorrectly says de. Missing syllables, other changed words, ground dì and 小孩儿 omission still fail the fixtures. Five Python tests passed (output/contextual-de-screen-fixtures.log). Existing raw recordings and cached transcripts are preserved. The next complete screening pass reevaluates negative results under this narrow orthographic rule; no recorded-tone or native approval is granted, and all release gates still run.

- Contextual 得 correction accepted with batch 43: 206 fields in 52 current packs changed; its Chinese, IDs, answer keys and other syllables preserved. The separately authored s5-u05/u06 date fixes also installed before acceptance, with changed audio regenerated, screened and genuinely repaired. Manifest and exact audio provenance refreshed; all eight gates passed. Native recorded-tone review remains pending. Evidence: output/contextual-de-corrections.json and output/gates/batch-43-final-receipt.json.

## Advanced batch 43 accepted locally — 2026-10-08 15:44 UTC

- Units: s5-u05 (24 word records), s5-u06 (24 word records), s5-u07 (24 word records), s5-u08 (24 word records). Word records include retrieval; they are not all new distinct source entries.
- Grammar cards actually present: s5-u05: 既然…，就…; 除非…，否则…; V下去; …为的是…; 不是…就… | s5-u06: 怎么…也 / 都不…; X归X，…; A的A，B的B; 为的是…，不是…; …得… | s5-u07: 拿…来说; 以便…; 尽管…，但是…; 一旦…，就…; V下来 / V起来 | s5-u08: 除非…，才…; 从而…; 一…，就…; 或是…; 共计…，包括…. Manual source-family crosswalk remains separate.
- Self-review and applied content fixes: recorded in each pack's notes and its authored source. Readability/pinyin problems were repaired before publication; no non-audio gate was relaxed.
- All eight receipt checks passed: packs/pinyin/readability, types, content/audio, unit tests, playback review, development browser tests, build, and production offline browser tests. Receipt: output/gates/batch-43-final-receipt.json.
- Sayo takes were generated, screened and genuinely repaired; unresolved takes are dated unreviewed exceptions under the owner's audio-only policy. Device speech is not labelled Sayo.
- Native review remains pending for every newly authored line, with particular flags in each pack's notes. No synthetic check certifies natural tone or learner mastery.
- Acceptance is local. A commit, push or deployment must be reported separately after it actually succeeds.

### Batch 44 content review while recording — 8 October 2026

Read the installed s5-u09–u12 question keys and the source-17 editorial changes. The four units contain 96 word records and twenty grammar cards; these counts include retrieval and are not new distinct inventory coverage. Interview questions preserve the six-to-ten attendance comparison and the one-hour session; the opinion unit distinguishes 64 visits from unique visitors and 16 combined staff-hours. Soup dialogue retains three distinct speakers, the double salt addition, a stop request and the cook's later bowl joke. Full/short video questions preserve the letter box, lit lamp, window opening and final pen action; no reunion is invented. The editorial layer removes policy-like explanations from actual speech and replaces them with concrete actions. Native review is still needed for ironic praise, X什么X force, the salt-bowl comeback and original verse delivery. Recording is in progress; this note is self-review evidence, not batch acceptance or native approval.

## Advanced batch 44 accepted locally — 2026-10-08 19:09 UTC

- Units: s5-u09 (24 word records), s5-u10 (24 word records), s5-u11 (24 word records), s5-u12 (24 word records). Word records include retrieval; they are not all new distinct source entries.
- Grammar cards actually present: s5-u09: 拿…来说; 尽管…，还是…; 在…看来; 只凭…，难以…; 先…，再… | s5-u10: 并不…; 即使…，也…; 没有…，就没有…; 尽管…，但…; 凭… / 依据… | s5-u11: 居然…; 明明…，却/还…; 可 + assertion/negative; 真有你的; X什么X | s5-u12: 随着…; 不一定 / 未必; 把…当成…; 既…也…; 跟…相比…. Manual source-family crosswalk remains separate.
- Self-review and applied content fixes: recorded in each pack's notes and its authored source. Readability/pinyin problems were repaired before publication; no non-audio gate was relaxed.
- All eight receipt checks passed: packs/pinyin/readability, types, content/audio, unit tests, playback review, development browser tests, build, and production offline browser tests. Receipt: output/gates/batch-44-final-receipt.json.
- Sayo takes were generated, screened and genuinely repaired; unresolved takes are dated unreviewed exceptions under the owner's audio-only policy. Device speech is not labelled Sayo.
- Native review remains pending for every newly authored line, with particular flags in each pack's notes. No synthetic check certifies natural tone or learner mastery.
- Acceptance is local. A commit, push or deployment must be reported separately after it actually succeeds.

## Editorial batch 63 accepted locally — 2026-10-08 20:06 UTC

- s5-u01: 24 existing word records; grammar: 毕竟; 明明; 倒是; 尽管…但是 / 仍然…; 不是…，而是… with a specific concern. Applied fixes and native flags: 2026-10-08 advanced reading self-review: Moving and singing readings now recount observable actions, ordinary banter and follow-up plans. Removed repeated friendship guarantees, consent analysis and grand claims from the narrator. Lyric discussion remains literary interpretation; its two readings and uncertain addressee are preserved. Corrected Lin An pronoun continuity in the drama summary. Retained all tested times, two missed words, two short performances and original question/task IDs. Native flags: 搬家连水都不肯扔 banter, 抬桌子/收材料 collocations, 鼓掌 misunderstanding and lyric interpretations. Native review pending.
- s5-u02: 24 existing word records; grammar: X归X，Y…; 再…也…; 动词 / 形容词 + 得 + clause; 在…看来; 先…还是…再…?. Applied fixes and native flags: 2026-10-08 advanced reading self-review: Moving and singing readings now recount observable actions, ordinary banter and follow-up plans. Removed repeated friendship guarantees, consent analysis and grand claims from the narrator. Lyric discussion remains literary interpretation; its two readings and uncertain addressee are preserved. Corrected Lin An pronoun continuity in the drama summary. Retained all tested times, two missed words, two short performances and original question/task IDs. Native flags: 搬家连水都不肯扔 banter, 抬桌子/收材料 collocations, 鼓掌 misunderstanding and lyric interpretations. Native review pending.
- s5-u03: 24 existing word records; grammar: 随着…，…; 不是…，而是…; 既…，也…; 不一定…; 把…带进 / 装进…. Applied fixes and native flags: 2026-10-08 advanced reading self-review: Moving and singing readings now recount observable actions, ordinary banter and follow-up plans. Removed repeated friendship guarantees, consent analysis and grand claims from the narrator. Lyric discussion remains literary interpretation; its two readings and uncertain addressee are preserved. Corrected Lin An pronoun continuity in the drama summary. Retained all tested times, two missed words, two short performances and original question/task IDs. Native flags: 搬家连水都不肯扔 banter, 抬桌子/收材料 collocations, 鼓掌 misunderstanding and lyric interpretations. Native review pending.
- s5-u04: 24 existing word records; grammar: 直到…才…; 原来…; 再…也不 / 没…; 不然…; 把A当成B. Applied fixes and native flags: 2026-10-08 advanced reading self-review: Moving and singing readings now recount observable actions, ordinary banter and follow-up plans. Removed repeated friendship guarantees, consent analysis and grand claims from the narrator. Lyric discussion remains literary interpretation; its two readings and uncertain addressee are preserved. Corrected Lin An pronoun continuity in the drama summary. Retained all tested times, two missed words, two short performances and original question/task IDs. Native flags: 搬家连水都不肯扔 banter, 抬桌子/收材料 collocations, 鼓掌 misunderstanding and lyric interpretations. Native review pending.
- Existing unit, word and task IDs are preserved. Believable scenes and independent word examples replace coverage stuffing and policy/grammar analysis inside speech. Related later glossary dependencies gained definitions without changing their lines.
- All eight strict gates passed: output/gates/batch-63-final-receipt.json. Changed audio was generated, screened, genuinely repaired and installed; dated unresolved exceptions remain unreviewed.
- Native review remains pending. No automatic test establishes naturalness, accent certification or learner mastery. This receipt is local acceptance, not deployment.

