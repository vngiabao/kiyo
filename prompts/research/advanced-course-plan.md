# Media and social bridge, through HSK 6

Owner-authorised scope, 7 October 2026: use HSK 5 as the main goal and HSK 6
as a stretch route for drama subtitles, songs and social conversation. The
recommendation is an editorial inference from the official competency
descriptions, not a published claim that a particular HSK score guarantees
understanding music or fast unscripted speech.

Sources: [CTI competency descriptions](https://hsk.cn-bj.ufileos.com/3.0/HSK3.0考试能力描述.pdf),
[current exam syllabus](https://www.chinesetest.cn/syllabus), and the
[GF2021 inventory](https://admin.chinesetest.cn/newhsk/standardsAction.do).
The retrieved rows are in `gf2021-advanced-inventory.json`. Separate the
GF2021 inventory, the newer examination syllabus and classic Standard Course
books. Do not use one set of counts to imply completion of another.

## Shape and prerequisites

Twelve core units per level, authored and accepted four at a time. Every unit
has at least sixteen context-selected vocabulary entries, explicit grammar
formation/contrast, a substantial dialogue and purpose-led reading, an original
subtitle scene or lyric, independent second word contexts, role-play and mixed
tasks. This is a **selected competency route**, not a complete vocabulary
inventory or an official full-length mock. Coverage reports must expose the
remaining words and grammar families; a unit's target label is not evidence
that its entire source level has been covered.

Require both the preceding word lesson and its grammar/usage lesson. Keep old
IDs and saved results intact. Advanced units use stage 3, order 109 onwards.
Never force a source word into a conversation merely to increase a count.
Independent vocabulary contexts can use a written or workplace register when
that is genuinely the word's usual use. Gloss unfamiliar words with actual
meanings; pinyin and pronunciation need contextual checks, particularly 得、还、
为、重、调、行、长、乐 and neutral syllables.

## Core sequence

HSK 4:
1. Meet a new group; find a shared interest.
2. Check whether a remark was a compliment or a joke.
3. Coordinate a gathering, fallback venue and shared costs.
4. Recover a missed drama line; distinguish clues from interpretation.
5. Sing an original verse; tell literal wording from an image.
6. Choose a course that fits a real weekly routine.
7. Ask for help at work; clarify task, deadline and register.
8. Disagree about a film without treating taste as a fact.
9. Repair a travel plan when transport changes.
10. Decline an invitation without closing the friendship.
11. Follow friendly exaggeration and playful complaints.
12. Retell a social/drama scene and connect its causes and consequences.

HSK 5:
1. Negotiate a promise when circumstances change.
2. Reassure a friend without dismissing the problem.
3. Follow figurative language in an original song.
4. Track what two drama characters know at different times.
5. Explain a trade-off between social plans and personal goals.
6. Set a boundary and respond to disappointment.
7. Present a workplace proposal and answer objections.
8. Organise a shared event with contingencies.
9. Understand an interview with qualified answers and examples.
10. Read an opinion piece; separate evidence and position.
11. Follow teasing, irony and understatement in context.
12. Discuss a performance and support an interpretation with details.

HSK 6:
1. Repair a relationship after a disputed memory.
2. Follow indirect requests and refusals across several turns.
3. Compare two accounts of the same incident.
4. Follow a longer drama scene with unstated motives.
5. Explain ambiguity and shifting imagery in an original lyric.
6. Negotiate a professional disagreement politely and precisely.
7. Retell a complex event with chronology and perspective intact.
8. Evaluate an argument and its limits.
9. Read a dense article with examples, qualifications and a conclusion.
10. Lead a discussion without monopolising it.
11. Recover fast casual speech through repair and context.
12. Integrated media/social transfer: retell, infer, discuss and write.

## Acceptance and honest limits

Only authored, audio-mapped, gated units are published. Full pipeline after
each batch: packs/pinyin/readability, content/audio, types, unit tests, real
browser playback, production build and production offline tests. A native
review is a separate remaining requirement, never an automatic-screen label.
The owner's audio-only exception remains dated and explicit; all other checks
remain strict. No visual redesign, new npm dependency, database rename,
progress merge or paid generation service.

Drafts s4-u01–12 pass the unpublished schema/readability/context preflight
(word readability 99–100%) and the unchanged pinyin checker applied to the
draft directory (12,943 matched words, zero lines to fix). They have not yet
passed publication audio and the full acceptance gates. HSK 5–6 remain planned.
The 192 HSK 4 vocabulary introductions include earlier-level retrieval and repeated
entries; they must not be reported as 192 newly covered HSK 4 source entries.
Self-review corrected a malformed noodle joke, clarified the invitation refusal,
and replaced an ambiguous character-count joke with an early-arrival tease.
Real definitions were added for unfamiliar passage words rather than reducing
the readability or character-meaning requirements.

HSK 5 drafts s5-u01–04 now pass the same unpublished schema, two-context and
readability preflight (99–100% words) and the production pinyin checker applied
to the draft directory. The latter reports 22,777 matched dictionary words,
149 unchecked characters, and zero lines to fix across all sixteen drafts.
These are preflight results, not audio or publication acceptance. Each HSK 5
unit has 24 word introductions, at least 18 dialogue turns, five grammar cards,
two separately authored readings of at least 600 Han characters, original
media, role-play and thirteen mixed tasks. The longer readings develop
different perspectives instead of filling scenes with unrelated inventory.

Self-review of u03 made the door drawing explicitly removable paper and kept
both home and romance interpretations possible. Its questions ask for stated
details and supporting clues, not a supposedly unique interpretation of art.
Self-review of u04 separates a sent message from a read message and gives
characters different information at each point. The 10:00 dead phone precedes
the 10:05 move; the 10:40 borrowed call resolves the problem; the walk takes
five minutes. Approximate waiting is not promoted to an exact timestamp.
The dictionary's `u:` spelling is normalised to `ü` before syllable checking;
regression tests still reject a wrong tone, a wrong syllable and an extra
syllable. No checker threshold or protected C2 file was changed.

Native review remains pending for the original lyric's imagery and rhythm,
the force of teasing and reassurance, X归X concessions, and oral retellings.
No draft establishes complete level vocabulary coverage or learner readiness.

## Draft checkpoint — 7 October 2026

All twelve HSK 5 core sources are authored, plus the first HSK 6 unit. Together
with the twelve HSK 4 drafts, twenty-five drafts pass the unchanged schema,
independent two-context and readability preflight (99–100% word support).
The production pinyin checker applied to the draft directory reports 49,527
matched words, 264 characters without dictionary entries and zero lines to fix.
Those remaining characters are not a native reading certification.

HSK 5 u05–08: bounded social time and contact, a workplace proposal assessed
with preparation/follow-up costs included, and a changed book-exchange venue.
U09–12: qualified community interview, two opinion perspectives, contextual
irony and an original performance with complete/incomplete versions. Twenty-four
introductions per unit include revisited words and senses; 288 records are not
288 additional distinct source entries. Each has 18 dialogue turns, two separately
authored 600-plus-character readings, original media and thirteen mixed tasks.

HSK 6 u01 has 32 word records, 24 dialogue turns, six grammar cards, two
900-plus-character perspectives and seventeen tasks. It keeps a finishing-work
time distinct from arrival, checks the full agreement, retracts unsupported
frequency claims, and allows feelings to outlast factual clarification. The
remaining eleven HSK 6 core units, advanced exam banks and whole-route review
are still outstanding. No advanced draft is marked native-reviewed.

Applied self-review: replaced unrelated reply distractors in HSK 4 u05–12 and
HSK 5 u01–06; tightened both Chinese and English prompts where the scored claim
needed a stated premise. Added actual meanings for missing words rather than
weakening the readability check. HSK 5 u12 explicitly uses 弹 tán and 归还 to
avoid a contextless 还 reading. Source part-of-speech metadata is retained for
new unpublished entries; a blank source category is not guessed as full sense
coverage. The four HSK 4 units in batch 39 remain pinned while their audio is
screened; this draft checkpoint is not their acceptance receipt.

Native flags: interview qualification and shoulder banter; 人次 and staff-hour
wording; 加以 collocations; 真有你的/可真/X什么X teasing force; original verse
rhythm; the lamp/box/window imagery; apology and 那倒也是/X就X吧 pragmatics.
Synthetic recognition is separate from native tone, rhythm and perceived intent.

The coverage script now accepts the actual researched levels and can run with
`--advanced`. Its regression test preserves incidental-versus-introduced words,
explicit character instruction and unmapped grammar. Default HSK 1–3 reports
remain reproducible. The six-level report currently describes the 112 source
packs on disk, including batch 39 pending acceptance; it does not count the
unpublished drafts or assert comprehensive advanced coverage.

## Editorial checkpoint: all36 core drafts

The complete12-unit route at each of HSK4,5,6 is drafted and passes schema, independent-context and pinyin prechecks (0problems;99–100% supported word readability). HSK4u01–04 are locally accepted;u05–08 are in repaired audio verification. HSK5/6 units remain unpublished drafts until their individual four-unit batches pass all eight gates. HSK4 mixed-practice bank is drafted and structurally validated;5/6 banks and full editorial review remain outstanding. The older checkpoints above are historical. No draft, label or source-word presence certifies native review, full inventory coverage or learner readiness.
