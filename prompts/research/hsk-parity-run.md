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
