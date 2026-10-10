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

## Public playback and draft question follow-up — 8 October 2026

A fresh Edge tab on kiyo.gbaonvo.com played 还记得吗？ and the Today lead's
口 recording: each returned from its speaking/stop state to the replay button
without a load or device-voice warning. This followed normal sign-in to the
existing Cloudflare dashboard account; it does not establish the reason for
the earlier failures. The public tab still loaded index-CmSBKDbo.js, showed
901 character entries and lacked Course library. The current deployment's
index references index-CoiNlxMi.js. Returning-browser navigation is therefore
not yet verified as current. No site data, learner history, Access policy or
cookies were cleared or changed. The earlier public Google callback worked,
but cloud sync remained paused; no device-progress merge was performed.

Read the remaining source 08/09 comprehension questions against their actual
scenes and passages. The supported facts are: the third member arrives before
reading starts; the left passage is shorter; Chen Yu handles the entrance and
Xiao Zhou takes over the list at three; two original pages plus one requested
page make three; a half-hour visit ends before the friend's five-o'clock nap;
the forgotten scarf stays behind; Thursday opening resolves unavailable
weekends; four of five group members visit because one works; phone payment
follows the forgotten card. Distractors do not establish those facts. This is
an editorial evidence check, not native-speaker approval or batch acceptance.

## Release source guard follow-through — 8 October 2026

The release helper now rechecks the accepted source fingerprint after staging,
after clean-checkout verification and immediately before deployment. This
closes the gap between initial receipt validation and a later commit/upload.
A mismatch stops release without deleting or discarding work. PowerShell
syntax and whitespace checks pass; the next full batch includes this source,
and actual release execution remains pending. No acceptance requirement,
question key, learner data or hosting policy was weakened.

## Installed HSK 6 heading regression — 8 October 2026

Batch 45's first browser run passed 48 cases and failed the old external-source-only heading assertion. The captured screen contained HSK 6 selected, its 90-item bank, three skill checkpoints, prerequisites and the correct full-route button. The test now requires both the roadmap's “HSK 6 · Handle dense material” button and the installed “HSK 6 · skill checkpoints” heading; before a bank is installed it still requires the external-source heading. This preserves both behavioral checks instead of hiding the failure. The focused case passed. All eight batch checks are being rerun on the amended source before acceptance; the failed receipt was not accepted. No curriculum, pronunciation, audio screening, answer key or storage identity changed for this repair.

Reviewed source 19's paired lost-bag account against its complete opening and title. Its first-person narrator is Chen Yu, while the main reading is Lin An's account. The apparent insertion/open-bag actor conflict is therefore not a content error. The provisional third-person edit was reverted before publication or audio generation; the original paired speaker and wording are preserved. The interrupted checks are not an acceptance receipt; all eight are restarted on the final source state. The provisional isolated shadow log is not evidence for installing an edit.

## Actual worker refresh follow-through — 8 October 2026

Shiori's follow-up describes real installed-worker update preservation. Kiyo's previous update-button regression used a simulated registration, while its existing offline tests used the real worker. Added an independent local server serving the actual built shell/Workbox assets and a changed worker release comment, with real installation, active lesson, saved learner name, explicit refresh and saved-audio decoding after offline reload. The initial fixture needed URL-decoding for static filenames; the subsequent real test reached Refresh and showed that it could wait forever for a controller change that had already happened.

UpdateNotice now tracks the previous controller dynamically, including the first installation's takeover, and reloads on request if the saved waiting worker is already activated or redundant. It never automatically reloads the open lesson or clears data. A Vite-only diagnostic build exercises the change locally; that is not a completed production build gate or authorization to release partially generated course audio. The next complete audio batch must pass all eight gates on these sources, including the new real production-worker test. The original simulated button test is retained as separate narrow coverage. No source, provider, database or design token changed in the Japanese sibling.

The focused real-worker regression passes after the state correction (8 seconds total): release adoption leaves the open lesson/document intact, explicit Refresh actually replaces it, the saved learner name remains, Course library is visible, and the previously cached real Sayo MP3 decodes after offline reload. Evidence: output/installed-update-focused.log. The diagnostic used an isolated local origin and synthetic learner; it does not certify the current public browser or real account sync. Full batch 46 acceptance and deployment remain pending.

## Concrete HSK 6 follow-through — 8 October 2026

A further full-paragraph self-review found genuine remaining report-like prose in the lost-bag, noisy-phone and capstone-letter accounts. This is separate from the previously reverted, unnecessary narrator correction. The lost-bag paired narrator remains Chen Yu; the main narrator remains Lin An. The newly authored bag layer replaces repeated epistemic lectures with returning books, asking the volunteer, checking pages, labelling the personal table, rehearsing and choosing later copies. Five unique pages, page four in the corridor, upstairs recovery, the new crease, readable new material and continuing borrowing stay explicit. Its missing standalone 副 definition was caught and added without relaxing readability.

The noisy-phone layer keeps arriving later, going inside first, no food ordered yet/water allowed, the cinema-side red door without crossing the bridge, the ten-minute estimate only after the bus arrives, and sound versus plot misunderstanding. The capstone audience account now debates the unopened letter, restores chairs and meets Lin An at 8:30 before the nine-o'clock train. The next-evening arrival message fulfils the explicit promise; the lyric still supplies no next-meeting date. Earlier task IDs, answer keys and the separate musician account remain intact, including the already-authored correction of the old hidden-letter task.

Exact contextual-pinyin approval for 笑声录得特别清楚 records complement 得 as neutral de, not obtaining dé or obligation děi. This follows the Ministry of Education dictionary's verb/adjective + result/state description, https://dict.revised.moe.edu.tw/dictView.jsp?ID=1928&la=0&powerMode=0 . That primary source supplements this construction only, not a replacement for the pinned mainland course inventory or a recorded-tone certification. Unknown nearby 录得这个 remains rejected. Eight Python and eight TypeScript contextual regressions pass, including wrong-tone rejection. No universal 录 stem rule was added.

Both editorial layers pass the isolated 144-pack word-readability and dictionary-pinyin checks with zero errors and zero contextual-pinyin problems. The phonetic checks matched 169,860 dictionary words after both layers; proper names/unknown dictionary characters remain reported. Logs: output/preflight-bag-actions-v2.log and output/preflight-phone-letter-actions-v2.log. This preflight is not eight-gate acceptance and installs no audio. Batch 46's existing generation manifest is untouched. Release 6 now requires a complete changed-audio batch 67 for the new bag layer after the existing required farewell batch 66; the phone/letter layer enters batch 47 before its first generation. Native flags include 台词丢了 banter, meal-menu teasing, lyric interpretation, 原稿心疼, calculator/percentage-point register and goodbye phrasing. Native review remains pending.

Follow-through: unit s6-u10 previously justified reading first solely by an early performer departure, while its paired account worried that a long reading would leave no music time. Corrected the proposal in the scene, main account and participant's account: the two performers want to hear a short passage before playing. The organiser limits reading duration, retains the eight-o'clock departure and asks the performers about splitting songs. Thursday-dinner reply and Friday room/date confirmation remain separate and pending. Existing tested contact, four-chair afternoon task, newcomer sharing and equipment follow-up facts are preserved. The combined final preflight matches 169,875 dictionary words, zero pinyin errors and zero contextual 得 problems; this remains isolated language preflight, not audio/batch acceptance.

Library follow-through: s6-u09's sixteen extra staff-hours lacked an explicit normal closing-duty finish, despite keeping readers until eight and staff until 8:30. The future batch 47 layer now states normal lending ends at six, staff finish at 6:30, and event-night staff finish at 8:30. Two extra hours per person over four evenings therefore means sixteen staff-hours total and eight per person. A chat line about hypothetical nine/ten-o'clock departures now simply asks who stays to put chairs away. The passage ends with a rota and the organisers arranging to return, rather than a staffing lecture. Original calculation answers and task IDs are preserved. Isolated preflight passes 144 packs, 169,911 dictionary word matches, zero line-pinyin errors and zero contextual-pinyin problems (906 fields). Evidence: output/preflight-phone-letter-actions-v3.log. Current batch 46 audio manifest remains unchanged; batch 47 generation and all eight gates still must accept these edits. Native notice register and staffing-account phrasing remain pending.

Actor follow-through: s6-u11's main account has its narrator phone Lin An and check the sister's name while Chen Yu sits beside them. The paired account incorrectly assigned that check to Chen Yu. Its rewritten fourth paragraph now identifies the interlocutor as the friend; the next paragraph has Chen Yu, separately beside them, suggest that the three watch together later. Arrival, ordering, temporary timing and all assessment answers remain unchanged. Final combined isolated checks pass 144 packs, 169,934 dictionary word matches and zero line/contextual-pinyin errors (906 fields). Evidence: output/preflight-phone-letter-actors.log. This is a genuine three-person continuity correction, distinct from the discarded lost-bag narrator edit; batch 47 audio and full checks remain pending.

Earlier-course follow-through: source 04's tea dialogue now agrees with its reading: the character says she doesn't want sugar while still adding it. Source 06's delivery account now traces trousers to the other chair, the old quilt joining them, then both being removed to free the seat. These edits pass isolated unchanged pack/readability/pinyin checks; full audio batches 49 and 54 are still pending. Their notes explicitly log the applied fixes. Evidence: output/preflight-tea-joke.log and output/preflight-quilt-chair.log.

Fresh navigation visual review: captured Course library and Your study desk at 1440, 768, 375 and 320 pixels using synthetic guest progress. Inspected the desktop, tablet and narrow-phone layouts: the approved leaning web logo remains, filters stack without overlap, the desktop menu sits below More and narrow screens retain the five-tab navigation. Existing browser tests also check filter/open/reload/back navigation, Escape/focus restoration and horizontal overflow at all four widths. These screenshots show 140 locally published units during unfinished audio generation, not a claim that those units are publicly released. Evidence: .impeccable/navigation/ and output/navigation-screenshots-current.log. Full batch 46 acceptance is still pending.

Song follow-through: source 19 now replaces s6-u05's main rehearsal paragraph six and paired paragraph seven with actual stop/restart, marked lyrics, cold tea, playback and saving two takes. Removed voice-identity and “cold rules” discussion from the lesson prose. Chen Yu remains the main reader/singer and Lin An the paired co-writer; the specific omitted 留 and later overlong 留 obscuring 给我 still support the existing tasks. Separate spoken-word and melody practice remains. The combined isolated preflight passes all 144 packs with 170,027 matched dictionary words and zero line/contextual-pinyin errors (907 fields); output/preflight-rehearsal-actions.log. Changed narration will be generated and checked in the mandatory batch 67 before HSK 6 first release. Native lyric phrasing and rhythm remain pending; no automatic gate certifies sung Mandarin tones.

Saved Shiori review cross-check (8 October follow-through): read the available N5/N4/N3/N2/N1, workplace-keigo, vocabulary-deck and exam-bank review records, including the applied N5 ambiguity fixes and the later N3 naturalness correction. The peer's latest progress notes also distinguish real installed-worker update tests from native/perceptual approval and keep teacher reactions mapped to mood/pose. Kiyo already rotates its 100 reactions by outcome through interleaved mood lanes; the approved B-half timbre and gentle pitch-based slowdown remain unchanged. This comparison uses saved review files and the owner's pasted critique, not a claim of access to every Claude chat. Peer source accounting, community levels and JLPT banks are not converted into official HSK equivalences. The concrete actor/date/quantity/answer-support standards are being applied to the pending Kiyo batches; all final audio and eight-gate receipts remain required.

Page-action pronunciation follow-through: a read of the actual bag layer found 晃 labelled huǎng in a physical shaking/waving context. The pinned inventory lists both readings but cannot establish the intended sense. The education ministry dictionary distinguishes huàng (shake/sway) from huǎng (light/flash): https://dict.revised.moe.edu.tw/dictView.jsp?ID=5265&la=0&powerMode=0 . The upcoming batch 67 now says 陈宇把纸举起来给大家看, with matching English, and explicitly removes the unused 晃 glossary aid; no universal pronunciation override was added. Named obsolete aids are removed only when absent from that passage. Isolated checks pass 144 packs, 170032 dictionary matches, zero line-pinyin problems and zero contextual 得 problems across 907 fields. Verified the raised-page line/pinyin and absence of unused 晃 in the final shadow bag unit. Evidence: output/preflight-bag-page-action.log. This does not approve the old batch 46 take: the new line still needs fresh audio and all eight checks in batch 67 before first release. Native performance review remains pending.

Return-action follow-through: checked each aligned 还 occurrence in the final shadow bag unit against its clause. Returning an object was already huán in the other aligned contexts, while still/yet remained hái; two clauses wrongly inherited hái for a return action. The paired account now says 林安说早上把空袋子放到门右边; the first role-play cue says 林安早上放下的是空袋子, retaining its question about the later-added pages. This explicit physical placement also avoids suggesting that a hand-to-hand return had occurred when she only left the bag at the entrance. Original practised response, intent and acceptance expression are preserved. No global 还 rule was added. Fresh isolated checks pass 144 packs, 170031 matched words, zero line-pinyin problems and zero contextual 得 problems across 907 fields; output/preflight-bag-return-placement.log. Verified the new written pinyin and unchanged response rule. Batch 67 must generate and screen these changed texts before the first HSK 6 release. Automatic transcription does not independently certify recorded tones.

Native-report scope follow-through (9 October): the prior report glob included the six new banks but omitted 36 retained reading-practice items. Expanded only the report's input list to include all seven installed HSK practice files, and added their original standard/level metadata; the older reading bank remains labelled HSK 2.0. Generator execution produced 2409 priority candidates at this point. Verified all 540 current practice IDs occur exactly within the expected ID set and every report row remains native review pending. No curriculum, answer key, audio manifest, storage identity or gate changed. This reporting source will be included in the forthcoming full batch 47 source fingerprint; audio screening is still active.

## Farewell glossary dependency repair — 9 October 2026

Batch 66 initially stopped at strict pack preparation, before generating or installing its changed audio. Replacing incidental prose exposed missing definitions for 嗓子 and later uses of 情绪 and 盏. Added passage glossary definitions in source 18 and declared later dependencies for s6-u05/s6-u12; retained the same aids in sources 19/20 so later publication cannot remove them. No checker or threshold changed. The corrected corpus passes all 144 packs, 152439 dictionary matches, zero line-pinyin problems and zero contextual 得 problems across 796 fields. The failed preparation is not an acceptance receipt. Batch 66 is explicitly rerunning fresh audio and all eight checks before release, despite the already-present authoring marker. Evidence: output/farewell-definition-dependency-check.log and output/parity-resume-final.log. Native performance and phrasing review remain pending.

## Bag passage glossary repair — 9 October 2026

Batch 67 stopped before audio generation at strict preparation: s6-u07 lacked reading definitions for 摇 (摇头) and 摸 (摸了摸折痕), causing prerequisite failures in the later units. Added only passage definitions in source 19 for shaking one's head and feeling a crease with a hand. No prose, IDs, assessment key, checker or threshold changed. Republished s6-u05–u08; all 144 packs pass with 152700 dictionary matches, zero line-pinyin problems and zero contextual 得 problems across 801 fields. Evidence: output/bag-reading-aids-check.log. The failed batch is not accepted. Rerun 67 explicitly before the release helper, because its authoring marker already exists in the failed attempt.

## Release staging lock repair — 9 October 2026

Batch 67 passed all eight gates, including all four production browser cases. Initial HSK 6 release stopped at git staging with an existing empty .git/index.lock. No Git process was running; an exclusive open succeeded and the lock contained zero bytes. Preserved it nonrecursively at output/git-index-lock-before-release-20261009.bak before retrying the release. No source, data, gate or index content was removed or modified. Existing tested source fingerprint remains required by the release helper.

## First HSK 6 core release — 9 October 2026

Released committed revision 3a999e9a871247a119939bf1093a6822312a888c after accepted batches 45–47, 66 and 67, clean checkout npm ci/build, and push to origin/main. Cloudflare version e2adbeab-2309-415e-b1e6-d5e64fc7b3a4 serves kiyo.gbaonvo.com. Upload completed: 638 changed files and 2430 already uploaded. This is selected media/social core, not full HSK 4–6 inventory coverage or an official readiness certification. Native report currently lists 2426 exact-line priority candidates, all unreviewed.

Live Edge check: a new verification tab loaded the older index-CmSBKDbo.js bundle/901-character catalog, despite normal reloads. The deployed checkout uses index-B0daMQTL.js. Hear Sayo for 还记得吗？ entered speaking state and returned to Hear Sayo without a warning. This confirms that observed playback, not latest public navigation adoption or an account sync roundtrip. No browser/site data was cleared, no Access policy changed, and no progress was merged. Latest navigation remains independently covered by responsive and production installed-worker tests. Continue investigating the public cached shell after the remaining editorial batches rather than claiming it is updated.

- Public cached-shell follow-up: normal /cdn-cgi/access/login navigation was blocked by Microsoft Edge (ERR_BLOCKED_BY_CLIENT). Did not bypass the browser protection or change Access. Returned via browser Back to Kiyo Today. Latest public shell adoption remains unverified; local real installed-worker tests passed. This does not block the independent course/audio batch run.

## Remaining foundation continuity review — 9 October follow-through

Read source 09's four later HSK 2 scenes, accounts and assessment questions, plus source 13's HSK 3 social scenes and related questions. Rechecked the 4:30–5:00 visit, novel/paper photo, forgotten scarf, Thursday exhibition opening, five-member group with four visitors, and phone payment after the forgotten card. For the social visits, the quiet-shop book/road memory agrees with the paired banter, Sunday arrival and dinner are separate from the future National Day outing, the old west-gate address explains the ten-minute east-gate walk, and the gold-coloured five-yuan button is explicitly ordinary rather than real gold. These are written continuity/answer-support checks, not native approval or full batch acceptance. No additional source change was needed; each upcoming batch must still generate its changed audio and pass all eight gates. Informal jokes, gift phrasing and opera-related register remain for native review.

Bag wording follow-through: the coat-rack account described one visible blue bag as 蓝色行李. Revised source 04 to 蓝色包 with aligned English. Source 05 applies that same narrow change to the earlier unit and all passage/gap references in batch 50, so the currently generating batch 49 remains internally consistent and no generated take is silently relabelled. 行李 retains two independently taught examples and explicit collecting-luggage contexts; vocabulary/task IDs and answer keys are unchanged. The isolated corpus passes all 144 packs, word readability and line/contextual pinyin (907 contextual fields, zero problems). Evidence: output/preflight-blue-bag.log. This isolated test is not audio or batch acceptance; batch 50 must generate and screen the changed paragraph and pass all eight gates before final release.

Next-batch word-example follow-through: replaced the weak collocations 打破安静 and 属他负责 with 他的一句玩笑打破了沉默 and 这块地属学校所有, and the awkward laughter-driven 带动 sentence with 她的热情带动了大家. Added exact glossary aids for 沉默, 热情 and the ownership use of 所有; 属 stays explicitly formal. Source 05 records these fixes in each reviewed pack. The isolated corpus again passes the unchanged pack/readability and pinyin checks; no current published line was mutated during batch 49. These edits require fresh batch 50 audio and the full acceptance suite, and none gains native approval from this editorial pass.

## Offline notebook fixture repair — 9 October 2026

Batch 49's first full run passed packs, types, content/audio, 190 unit tests, playback review, 45 development browser tests and build. Production passed three cases but stopped on the notebook test before any offline action: the randomly rotated ten-item checkpoint contained no listening item, contradicting the fixture's claimed deterministic setup. The rotating bank intentionally ranks unseen items first and does not guarantee a listening item in each draw; product selection and saved results were unchanged.

The fixture now takes a real listening item from the same installed level and checkpoint, places it first and retains the original run length and unique IDs. All actual cache, completed-playback answer lock, offline reload, saved answer and navigation assertions remain. The focused production notebook case passed (14.4 seconds). Preserved the first failed log/receipt at output/gates/batch-49-first-production-failure.log and batch-49-first-failed-receipt.json. The focused pass is not batch acceptance: rerun all eight gates on the changed test source before logging batch 49 or continuing to 50. The accepted audio library is unchanged by this test-only repair.

## Bag gap-reference repair — 9 October 2026

Batch 49 passed its complete rerun: 190 unit tests, 45 development browser cases and four production cases, with all eight gates at fingerprint a8eed793476541c89e2113c576f2949f06e1eaec1437c091a308a69b434bcef1. Batch 50 then failed strict preparation before generation: the blue-bag paragraph had changed, but its old cloze wrapped 行李 in brackets, so the narrow string replacement had not found it. That one stale gap reference caused later prerequisite/definition cascades (47 rejected packs). The earlier combined isolated test masked this transition by regenerating source 04's gaps first; it was not evidence of audio acceptance.

Source 05 now rebuilds that reading's three gaps from the actual revised lines, using the same passage/vocabulary selection rule, and deduplicates repeated review notes on rerun. Saved IDs and standalone task keys remain; passage gap answers are derived from the current text. No gate was changed. Direct publication followed by strict packs/pinyin passes all 144 packs, 157131 matched dictionary words, zero line-pinyin problems and zero contextual 得 problems across 800 fields. Evidence: output/batch50-gap-reference-repair.log and the preserved output/gates/batch-50-first-prepare-failure.log. Explicitly restart 50 with fresh audio and all eight gates before continuation. Native review remains pending.

## Batch 50 initial navigation timeout — 9 October 2026

The first full batch50 attempt passed packs, types, content/audio, 190 unit tests and playback review. Development browser checks passed 44 cases but the navigation case timed out at its initial page.goto while waiting for document load, before any navigation or learner interaction. The failure has no captured page snapshot. The same unchanged focused test immediately passed in 6.1 seconds (actual assertions 5.2 seconds). No timeout, retry policy, product code or assertion changed; the initial timeout's cause is not established. Preserve output/gates/batch-50-first-browser-failure.log and batch-50-first-failed-receipt.json. The focused pass is not acceptance. Rerun all eight gates and stop again on any failure before recording acceptance or continuing to 54.

2026-10-09 continuation: batch50 accepted all eight gates (receipt fingerprint 9193df4d1f4315163271b07961f33c186a05f703a2f09e291e06fa234fee7cb8). Batch54 preparation stopped on the missing reading glossary for 挪 in the revised quilt scene; subsequent prerequisite errors were a cascade. Added the precise meaning and pinyin in source06, republished, and packs passed all144, with0 line-pinyin and0 contextual problems. Preserved first failure log. No validator or threshold changed; full audio and eight-gate acceptance still required.

Sequential isolated preflight of sources07–14 passed all144 packs, strict pinyin/contextual checks after each source. This is advance editorial evidence only; each still needs root audio and all8 acceptance. Direct reread identified s3-u27 照片后面 as a misleading literal location: source07 now says 你看照片里的那座桥, with aligned English. No answer key or ID changes. s3-u01 already explicitly assigns 李宁/陈宇 and correctly reverses its paired-scene speaker order; no name repair needed. Rechecked swimming/class arrival times, volunteer handover at3, four dinner places/four pairs of chopsticks, six-person supplies, Saturday7pm ticket/Thursday purchase,20-minute walk roundtrip and7pm room-change notice against their tasks. Native review remains pending.

Batch54 first audio pass:936 new takes generated; the automatic screen queued7 genuine replacement jobs. ASR transcription matches, including homophone transcripts, do not certify tones: for example the 插队 cool transcript was 查对, a syllable-level match with an unresolved tone distinction. Existing native-review pending status applies; no native or recorded-tone approval claimed. Replacements/rescreen/full8 gates remain pending.

Batch54 mastering finished clip processing but Windows denied atomic replacement of content/audio-provenance.json (WinError5; target is not read-only). Preserved failed log and temporary candidate in output. Master writer now creates a unique exclusive sibling, flushes it, then retries replacement up to12 times only for Windows lock/access errors5/32/33; persistent failure still throws and preserves both ledgers. Two filesystem tests verify transient success and permanent failure without truncating the old target. All6 mastering tests pass. No audio hash, acceptance status or validation rule changed. Rerun master, compatibility retention, review and all8 gates before acceptance.

Follow-through written review: sources11/12 scenes and their actual questions remain aligned. Rechecked Thursday booking/Saturday7pm performance, row3 seats,3pm moved-bookshop meeting,20-minute walking roundtrip, slow rehearsal before music and narrator/Chen first/second duet lines. Rechecked class-blocked morning vs2pm lunch/tea and later dry-weather walk, last-month cancellation image vs today's second-floor7pm venue/four friends, nine-o'clock registration/two-minute representative talk, and old entrance table for tools before assembly and south-facing upstairs desk/books in smaller loads. No additional scene changes required; native register/teasing and actual recorded tones still pending. Pending full batch59/60 audio and acceptance required.

Batch55 accepted all8: 190 unit tests,45 development tests and4 production tests;916 initial takes,5 replacements,354 direct exceptions,44,824 installed mastered files/1,613,770,784 bytes/missing0. Exact pending recorded-tone flags for 插队 (ASR查对) and 你报的初级游泳课，什么时候开始？ (ASR抱) are now retained by the native-review report generator. These observations trigger human listening, not a declaration that those tones are wrong or right. This report-generator change precedes batch56 gates and must be covered by the remaining final source fingerprint.


Batch56 live-source self-review: reread all four core dialogues and their gist/detail/inference keys. s3-u01's Li/Chen names and friendly Xiao Li address are consistent; the southern hometown and habitual early-arrival joke support their questions. s3-u02 distinguishes today's open reading event from next month's competition and supports listening before the first-sentence attempt. s3-u03 assigns the entrance to Chen and names/list work to Lin, with2–3pm service, four chairs/two each and Xiao Zhou's handover. s3-u04 postpones contacting the haircutting Xiao Zhou until afternoon and allows3or4pm, with the page-copy favour separate. No source change required. Register, abbreviated 报比赛 and the chair/tea joke remain for native review; pending audio/all8 acceptance is not replaced by this written check.


Additional batch56 written review found a physical/digital ambiguity in s3-u04 photocopying: 发给我 implied a sent file while the scene teaches copying an original paper page. Source08's reproducible text now uses 拿给我/交给我. Source09 will apply that narrow follow-through to the already-published unit only when batch57 begins, after batch56's current audio/gates finish. The updated page response, paragraph, English, answer and accepted response stay aligned; digital address sending is unchanged. Sequential isolated sources07–14 again pass all144 packs/pinyin/contextual checks. This is preflight only; fresh changed-line audio and batch57 full8 remain required. The earlier 'no source change required' note describes the earlier core-dialogue pass, not this later reading/physical-medium fix.


Shiori follow-up read: inspected the latest available course-progress tail and written N2/N1 bank review. Their review keeps permissions, proposals and obligations distinct, narrows unsupported choices, preserves old bank objects, labels short drafted practice honestly and separates dictionary evidence from native approval. Kiyo's scene/answer-support review follows the same distinctions; no Japanese code changed. Shiori's returning-tab note reports a harmless ?release=revision query refreshed an old HTML response without clearing data. At final Kiyo live QA, try the normal root URL with the final revision query; this is a cache refresh, not an Access-policy change or a bypass of the blocked login endpoint. Public latest-shell adoption and two-device sync remain unverified until separately observed.


Batch58 live dialogue reread: the six-person/two-group supply plan correctly lacks2sheets from4, then assigns3toeach group/twopens pergroup and addsone sheet for an extra friend. Singing-practice counts3vs2 become equal after one repeat; station6:30, doors7 and concert8 are separate and their questions are supported. No additional source change from these checks; native phrasing/recorded-tone review remains pending and full8 acceptance is still required.


Batch58 first full browser suite passed44 development cases and skipped4 production-only cases, but the navigation case exhausted its40-second whole-test budget during onboarding before any navigation assertions. The failure snapshot contains the visible Sound first radio. No root cause is established. The same unchanged focused case passed immediately; preserve the original log, failed receipt and error-context snapshot. Do not loosen assertions, timeouts or retries. The focused pass is not acceptance: rerun all eight gates on the unchanged installed source before logging acceptance or starting59.


Batch59 live-source reread confirmed Saturday seven-o'clock ticket facts, the moved bookshop's new address/three-o'clock meeting, the twenty-minute walk and the slow-first rehearsal. Naturalness follow-through: the s3-u10 key-placement joke becomes 每次…都不一样; 从来 remains in its independent vocabulary contexts. Reproducible source11 is corrected; source12 will apply the exact-line change only when batch60 begins, after batch59's fixed audio plan and checks finish. Word/task records and question keys were compared unchanged. A contextual check of the old combined shadow first failed439 stale 得 fields; no root content or gate changed. Refreshed only the unpublished shadow from the current root packs, overlaid the five intended draft units, then strict packs/readability and line-pinyin checks passed for144 units, and the contextual checker passed890 fields/0problems. Original stale-shadow failure is not app acceptance. Actual fresh audio and batch60 all8 remain required; native review pending.


The same batch60 follow-through also replaces the friends' formal 上次那个场所 with 上次那个地方 in s3-u09; 场所 retains its independent contexts. Chinese and English are aligned; unit/word/task records, grammar and both units' question keys were compared unchanged. Updated six-unit isolated preflight again passes all144 packs with strict word readability,0 line-pinyin and890 contextual fields/0problems. No current batch59 manifest or published line was changed during its generation. Fresh audio/installation and full60 acceptance remain required.


## Batch 59 first browser failure — 9 October 2026

Audio generation (901 initial takes, six genuine repair jobs), rescreening, explicit deferral (361 direct texts), installation, compatibility retention and playback review completed. The first full browser suite passed 44 development cases but its navigation case exhausted the unchanged 40-second budget before guest onboarding. Snapshot contained only the brand image. Preserved the failed receipt, log and snapshot as output/gates/batch-59-first-*. The identical focused navigation case passed in 5.4 seconds (6.0 seconds total). The underlying timing cause is not established; this is not proof that a product bug was fixed. No assertion, timeout, retry policy or gate was changed. Full eight-check rerun is required before acceptance and before proceeding to60.

## Final HSK2 restaurant wording refinement — 10 October 2026

Source14 for62 replaces 一个鸡蛋菜和一个青菜 with 点了炒鸡蛋和一盘青菜 and aligns the English as scrambled eggs and a plate of greens. Precise passage glosses support the dish and plate classifier without guessing a curriculum level: the local official word index places standalone 炒 in GF2021 level6, so the early passage aid is not labelled a newly introduced level2 vocabulary record. Existing target vocabulary IDs remain; the concrete dish wording is not forced vocabulary recycling.

Before refreshing the existing isolated shadow, a conservative Windows attribute guard stopped at .cache's ReparsePoint attribute. Inspection then established no link type/target, no symbolic links, real paths entirely within the intended shadow, and zero lstat reparse tags for all four involved directories. Only the verified shadow's pack copies and generated draft data were written; protected app files were unchanged. All144 shadow packs, word readability and line pinyin pass, with170020 dictionary matches and0 lines to fix. Existing vocabulary/task IDs and two distinct contexts per word are asserted by the draft preflight. This is not batch acceptance or native approval:62 must publish the authored repair, regenerate its changed audio and pass all8 gates.
The isolated restaurant corpus also passes contextual 得:917 fields,0 problems (output/gates/batch-62-restaurant-contextual.log). No protected root file was modified.
