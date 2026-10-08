# HSK parity and media/conversation expansion — 7 October 2026

Owner-authorized scope: compare Shiori, apply the naturalness correction to Kiyo,
repair functional exam/offline gaps without a visual redesign, reduce unnecessary
size, and extend toward HSK 5 with HSK 6 as the stretch target. Existing database
names, records, approved Sayo identity and the five C2 protected files stay intact.
No paid model calls, new dependencies or independently invented HSK assignments.

## Target and evidence

The target is an editorial recommendation for social conversation, dramas and
singing, not a claim that a test certificate guarantees any of those abilities.
CTI's current [competency profile](https://hsk.cn-bj.ufileos.com/3.0/HSK3.0%E8%80%83%E8%AF%95%E8%83%BD%E5%8A%9B%E6%8F%8F%E8%BF%B0.pdf)
describes level 5 as accurate/appropriate communication in work and academic
settings and level 6 as rich/fluent communication in workplace, academic and
general professional settings. It does not give a drama/song threshold. Media
transfer therefore needs an explicit original-scene/lyrics route and the user's
own material, alongside general-language study.

Keep GF0025-2021 teaching inventory separate from the new exam syllabus and from
classic HSK 2.0. [CTI syllabus portal](https://www.chinesetest.cn/syllabus),
[classic level-5 structure](https://www.chinesetest.cn/HSK/5) and
[level-6 structure](https://www.chinesetest.cn/HSK/6) checked 7 October. A browser
page showing classic timings is not evidence of the new syllabus's timings.

## Comparison snapshot

- Kiyo has 108 core packs: 30 / 34 / 44 at GF2021 levels 1 / 2 / 3. The recorded
  conservative introduction audit has 500 / 772 / 973 source vocabulary entries,
  300 new explicit characters at each level, and 48 / 81 / 81 grammar families.
  Introduction is not mastery or native approval.
- Its installed practice banks have 90 questions per level for HSK 1–3: 60
  checkpoint and 30 sample items. Attempts select 10 / 12; they are adapted
  original drills, not complete official papers.
- Shiori's inspected N3 screen has six explicit study milestones and a starting
  skills self-check. Its saved bank review documents 90 items per N5–N1 level.
  Its generated aggregate contained 154 packs at the snapshot; it is still being
  edited, so this is not a stable completion or quality verdict.
- Read the supplied Claude critique and saved Japanese outline/continuation and
  N3/N2/N1/bank reviews. They establish naturalness, source attribution, explicit
  grammar formation and preservation requirements; no Japanese-only instruction
  is silently executed against Kiyo.
- Kiyo's core later dialogues show the same stuffed vocabulary and app-policy
  leakage. These must be repaired before using their inventory counts to argue
  that the course is educationally complete.

## Working order

1. Fix resumable audio download cancellation, retention, transient failures and
   quota reporting; keep HTML/login fallbacks out of the cache. Match inventory
   in bounded batches instead of enumerating all cached audio keys.
2. Correct mixed-skill checkpoint labels/assignments, keyboard operation and
   visible entry/preparation guidance. Preserve saved question and stage IDs.
3. Rewrite affected HSK 1–3 connected speech as believable situations, beginning
   with s3-u41–44. Repair matching tasks, keys, pinyin and text-derived gap fills.
   Never pad a scene to force all new words into it. Use independent vocabulary
   contexts for words that do not belong in the scene. Review the remaining
   scenes and readings against the same rules.
4. Build advanced core routes for levels 4–6 in four-unit batches. Situations
   include casual chat, invitations/refusals, relationship repair, longer drama
   scenes, original lyrics, inferential reading, workplace register and sustained
   retelling. Final unit allocations must follow the source inventory and actual
   prerequisites. No claim of complete level coverage without the crosswalk.
5. Add original advanced rotating exam banks with level/source checks, answer
   keys, varied distractors and Sayo audio. Preserve older IDs and attempts.
6. Profile runtime/install size separately from local synthesis tooling. Retain
   approved reference/raw recordings and current offline models. No lossy voice
   transformation merely to reduce storage.
7. All batch gates, then full release checks, commit/push and final deployment
   under the owner's existing authorization. Record native-review limits plainly.

## Editorial correction 01 — s3-u41–44

Replaced all four core dialogues and readings with ordinary conversations about
coffee/drama night, missing a subtitle line, a club's original song, and dinner
plans. Kept passage IDs, vocabulary IDs and assessment anchors. Rewrote three
literal/inferential questions per dialogue and three per reading, six per unit.
Regenerated gap fills from the revised text and supplied
real glosses for 吓了一跳、隔壁、露出、吉他、岸边. Vocabulary remains independently
taught; the old recycling quota is not forced into speech. Added 59 separate
retrieval situations after the strict two-context test exposed losses caused by
the scene rewrites. Packs: zero errors, zero pinyin problems, word readability
at least 95%. Batch 37 passed all eight acceptance gates: 157 unit tests,
39 development browser tests and all 3 production offline/update tests. This
acceptance covers the four revised core passages and their new contexts; it
does not assert that every older notebook, example or task is fully natural.
None is marked native-reviewed.

Native review still needed: the teasing force of 笑什么啊/别问了, contextual 好不好
and 怪不得 delivery, neighbour-related volume request, colloquial 一快就乱,
singing diction and tone accuracy. The readings and all remaining source content
are AI-assisted drafts, not independently certified assessments.

## Verified build-size correction

The first encoder build was bypassed by Vite's JSON loader. Reordering those
plugins fixed the actual production output; a postbuild check now imports the
built modules and compares every field to the full source. Verified: 108 units
and 11,824 audio texts unchanged, course data 2,462,715 bytes, catalog 1,301,539
bytes. Initial offline precache fell from 11,770.61 KiB to 10,242.80 KiB.
Audio encoding/quality is unchanged; the optional full voice download is
685.9 MiB. These install sizes must not be confused with the local model and
Python environment sizes. Production offline checks also run after this fix.

## Editorial correction 02 — draft self-review

Prepared s3-u37–40 with bookshop planning, course selection, shared trip costs
and leaving a retirement gathering. Revised the core passages, media, keys,
tasks, pragmatic examples and role-play. Replaced stiff or semantically wrong
vocabulary examples. Source-sense review caught 任: its allocated row is the
conjunction meaning “regardless of,” not the hold-office verb. 升's allocated
row is the rising verb, not the litre measure. Corrected those senses and
replaced the unnatural 绕湖一环 with a concrete ring example. The arithmetic
is 120/4 + 180/4 = 75 per person. Native review remains pending; publication
and audio acceptance are separate gates.

## Current-build authentication check — 8 October 2026

The release-4 production preview at http://127.0.0.1:4173 completed the actual
Google account chooser and Supabase callback for the owner's existing account.
Its Settings page showed the current 33,847-clip catalog and Course library/More
navigation. The read-only Check cloud connection reported that the Google account
and cloud storage were reachable. That probe performs reads, not merge/upload.

Important limitation: this preview origin already contained a consented sync
profile. It resumed automatic sync on sign-in and reported Your progress is
synced (last observed 05:08:01 AM local). No Add device progress, Sync now or
Delete cloud data button was pressed. Therefore this session must not be
reported as an entirely write-free login test. Signed out of the preview after
the check; local history was retained. Public-site current-release login remains
unverified because the existing public browser kept serving an older cached
shell. Cloudflare's dashboard independently shows release 46b0f1fc active and
the f012545 Git build. No Access policy or site data was changed.

## Read-only Shiori review follow-up — 8 October 2026

- Read output/course-progress.md and review-n2.md/review-n1.md again. The latest
  logged Japanese checkpoint is N1 unit 9; this is a documentation snapshot,
  not a claim that other concurrent Japanese edits have stopped.
- Its N2 review explicitly says long readings have no full narration; words,
  examples, scenes and task stimuli do have audio. Kiyo additionally synthesises
  full reading paragraphs and assembled passages. Model/environment footprint
  and this audio policy therefore matter when comparing folder sizes.
- Apply the shared editorial lessons: ordinary dialogue, evidence-supported
  answers, concrete times/actors, contextual polyphonic readings, independent
  vocabulary practice, and native-review limits. No Japanese files were edited.
- Kiyo's new advanced route and exam banks remain adapted original practice;
  they do not certify a complete official paper or full advanced inventory.

## Released-audio compatibility — 8 October 2026

An editorial replacement removes an old URL from the active teaching catalog.
Cached app versions may still request it. `retain-released-audio.py` restores
previously committed MP3s under their exact old URLs for a 90-day window. It
checks each byte hash against the origin commit's provenance. The separate
ledger cannot add a line to current coverage or mark a failed take reviewed.
Expired records are tombstones, not renewed implicitly; the next mastering
installation archives inactive files as before. Deploy packing includes active
and retained URLs, while current teaching validation stays catalog-based.

Verified on isolated fixtures: four Python restoration tests and thirteen
TypeScript retention/transport tests passed. Missing/tampered files, invalid
paths, duplicate receipts, invalid dates, renewed expiry, and current-catalog
exclusion are exercised. Actual retained-file count and deployment playback
remain to be checked after the next installed library. No local progress,
voice identity or audio encoding changes.

## Exam audio demand correction — 8 October 2026

Read the actual Hsk/HskExam playback sites. Study and answer review play each
complete `sentence`; the study vocabulary plays choices from cloze/legacy
items only. Blank `prompt` strings, ordering fragments and other distractors
have no playback button. The old collector nevertheless requested all of them,
including strings such as `她虽然笑着说，要求___很明确。`.

Shared `hskStudyWords` now preserves the exact study-screen selection/order and
supplies its audio collection. Every complete exam sentence is still required.
No answer key, saved ID, pinyin/readability gate or audio recognition criterion
changed. The existing blank remains visible until answering; no audio hint is
introduced before submission. This is removal of unused synthesis inputs,
not acceptance of an unverified recording.

Audit of the current installed-unit sources: 15,008 previous manifest texts,
13,408 current playback/teaching texts, 1,600 unused texts removed and zero new
texts required. Fifteen focused contract/retention/transport tests passed.
The running batch's audio plan predates this correction; refresh it and rerun
all eight gates before acceptance/deployment. `output/audio-demand-audit.json`
records the exact removed strings. Actual final voice/storage totals follow
installation; the earlier counts are not final release figures.

## Cached character and word playback checks — 8 October 2026

Two character sheets can share one contextual recording (矛 and 盾 use 矛盾).
Repeated playback may use the browser's cache without another response event.
The browser checks require a successful network load once per unique URL and
the real media `ended` event at the exact mapped URL on every word/sheet replay.
No MP3 playback is mocked. Explicit owner-deferred speech retains its separate
routing and warning checks. The larger character suite gets a per-glyph total
time budget, while each individual replay still has a 15-second completion limit.

Both focused browser tests passed on s5-u01–04 (34 new glyphs plus contextual
reading regressions). Full acceptance must still pass before publication.
The installed compatibility ledger contains 1,200 retained released recordings,
each verified against the origin commit's hash; they are excluded from current
coverage and retained for the stated bounded compatibility window.

## Japanese review refresh — 8 October 2026

The tail of `course-progress.md` is older than the sibling's individual reviews.
`review-n1.md` now records completion of twelve N1 cores, and `review-keigo.md`
records all twelve workplace scenarios: 103 packs, 4,192 authored entries,
345 lessons, 289 notes, 167 scenes and 96 readings at that checkpoint. These
are the sibling's recorded figures, not independently established proficiency
or a claim that its concurrently edited files have stopped changing.

Applied comparison criteria remain natural dialogue, precise actor/time/count
facts, keeping proposed actions distinct from completed ones, contextual speech
readings, preserved old recordings and honest native-review status. Kiyo's
selected advanced media/social route is not claimed to match all of Shiori's
workplace or vocabulary-deck breadth. No sibling source files were changed.

The later `release-report.md` supersedes that intermediate checkpoint: it
records 154 packs, 963 lessons, 8,777 word/chunk/name records, 73 vocabulary
decks, 2,013 kanji reference pages and 450 original written practice items.
Its final optional audio library is about 2 GB, while the installed shell is
14,759.60 KiB. Those are the sibling's reported release figures, not a fresh
independent audit of every source row. Its report also explicitly leaves native
review and the owner's two-device sync test uncertified. It notes that an
existing in-app browser may retain the older offline app, matching the stale
Kiyo navigation observed in our live verification browser. We did not clear
browser data or infer current public-site behavior from a local test.

## Storage snapshot during batch 43 — 8 October 2026

The read-only recursive audit completed with zero filesystem errors in both
folders: Chinese 26.354 GiB / 359,735 files, Japanese 11.382 GiB / 113,906 files,
ratio 2.32. This is an in-flight snapshot, not the final release measurement.
Chinese's offline models are 9.334 GiB, its Python voice runtime 5.305 GiB and
caches 5.762 GiB. Authored packs are 0.006 GiB; the much larger content root also
contains artwork and audio provenance. Kiyo's current public assets (0.957 GiB)
are smaller than Shiori's (2.278 GiB). Folder size therefore mainly reflects
different voice tooling and working caches, not a larger authored curriculum.

The screen still uses Whisper medium. The large-v3 model is retained for the
existing independent transcript diagnostic and small for the earlier audition
tools; removing them would break those reproducible tools. Current generation
and provenance caches stay until final acceptance. No runtime source, approved
reference, learner data or sibling file was removed for this snapshot.
Evidence: output/folder-size-audit-current.json and
output/folder-size-audit-during-batch43.log.

## Guard against source edits during validation — 8 October 2026

The gate runner now stamps the actual source before its first check as well as
at the end. If source, curriculum or visual assets change while the eight
checks are running, acceptance fails and all eight must be rerun. The existing
release check still rejects edits made after acceptance. This strengthens the
checks; it does not skip, loosen or substitute any validation. PowerShell
syntax and source whitespace checks passed. The change enters batch 63's full
receipt before the next release; its runtime acceptance is not claimed here.
