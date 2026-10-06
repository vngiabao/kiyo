# Learning model and evidence registry

Research checked 4 October 2026. This is an evidence-informed implementation, not an efficacy-validated course. Original seed scripts remain AI-assisted drafts until qualified review. No claim is made that completing these exercises confers proficiency.

## Controlling outcome
Useful Mandarin understood and produced in an unfamiliar conversation. The working sequence is hear → understand → notice → imitate → retrieve → respond → revisit. Reading and typing support communication; handwriting and essays are not gates.

## Functional capabilities, not a completion score
**Evidence:** ACTFL's [2024 guidelines and official-use policy](https://www.actfl.org/use-of-actfl-proficiency-guidelines-and-issuing-of-official-actfl-tests) and [Can-Do framework](https://www.actfl.org/educator-resources/ncssfl-actfl-can-do-statements) separate capabilities and acknowledge uneven skill profiles. The full 2024 PDF search result was located but direct retrieval returned 404; do not treat its full text as reviewed.

**Decision:** Store listening, reading, typing, speaking practice, conversation rehearsal and media evidence separately. Show attempt counts and denominators. No ACTFL rating, CEFR equivalence, exam prediction, or percent fluent.

**Measurement:** Later, collect unfamiliar-speaker, unseen-scenario and spontaneous oral assessments with reviewed rubrics. Current scripted typed conversation and familiar listening checkpoints are rehearsal, not transfer tests.

## Four Strands
**Evidence:** Nation (2007), [The Four Strands](https://doi.org/10.2167/illt039.0), identifies meaning-focused input, meaning-focused output, deliberate language study, and fluency development, with approximately balanced time. The publisher abstract was available through search; full article access was blocked.

**Decision:** Include each strand, with oral activity emphasized within them. Listening-first does not mean reading is undesirable. The daily time allocation is a product heuristic, not a scientifically optimized ratio. A learner chooses 10–60 minutes. With sufficient observed reading/listening disparity, allocate more listening.

**Measurement:** Track activity mix, retention and transfer. Time suggestions are planning budgets, not measured task-duration guarantees. Do not optimize for longest session.

## Retrieval and spacing
**Evidence:** [Cepeda et al. (2006), distributed practice review](https://doi.org/10.1037/0033-2909.132.3.354) is a foundational reference to review in full before commercial claims. Implementation uses the maintained [ts-fsrs scheduler](https://open-spaced-repetition.github.io/ts-fsrs/), not handcrafted intervals.

**Decision:** A memory is phrase × tested modality. Persist FSRS card state and review evidence atomically. Again for an unaided incorrect answer; Good for an unaided correct objective answer. Self-report, captions, and pinyin do not update an unaided recognition memory. Scripted conversation matching and scene comprehension are not promoted into isolated-phrase recognition review. FSRS is a scheduling model; its 0.90 retention setting is not a promise about this learner.

**Measurement:** Separate 1-, 7-, 30- and 90-day recall by modality when sufficient longitudinal observations exist. The app currently shows counts rather than invented retention estimates.

## Characters-first path (learner choice)

Decision: let the learner start with character recognition (shape, components, meaning) and defer sound until asked, or start with sound, or do both side by side. Rationale: this learner prioritises reading; most characters are semantic–phonetic compounds, so explicit component instruction gives a transferable decoding strategy rather than rote shape memory. Implementation: seven 8-character lessons ordered pictographs → indicatives → compound ideas → meaning+sound compounds → high-frequency function words → speech/mouth components → people/places; every character is met before it is quizzed; char→meaning, meaning→char and "spot the component" checks are interleaved; words close each lesson only when every character in them has been met. Origin notes are labelled *origin*, *traditional explanation* or *memory aid* so mnemonics are never presented as etymology. Guard rails: the daily plan for this path still schedules listening and speaking every day; revealing pinyin marks an answer as supported; reading recognition and listening recognition remain separate memories, so reading progress never counts as listening progress. Graded readings show coverage computed only from unaided recognition. Measurement still needed: whether component instruction improves recognition of *unseen* characters relative to whole-character study.

## Tone perception and production
**Evidence:** Wang, Jongman & Sereno (2003), [acoustic and perceptual evaluation before and after tone-perception training](https://pubmed.ncbi.nlm.nih.gov/12597196/); [author-hosted paper](https://kuppl.ku.edu/sites/kuppl/files/documents/publications/Wang_Jongman_Sereno_training_production_JASA_2003.pdf). Perceptual training can support production, but outcomes vary.

**Decision:** Begin with clear contrasts and short explicit explanations. Give an immediate useful phrase. Introduce voice variation after a clear model. Show idealized pitch contours, never pretend they measure a learner. Record and replay locally. An ASR transcript would not be a phonetic or tone score.

**Measurement:** Later native-listener intelligibility and unfamiliar-voice discrimination. Synthesized voices are not a substitute for validated native recordings. Tone 3 is often low in context; don't teach a full dip everywhere. Display lexical pinyin with usage notes for sandhi.

## Caption and pinyin support
**Evidence:** Montero Perez, Van Den Noortgate & Desmet (2013), [captioned video meta-analysis](https://biblio.ugent.be/publication/8673620); [publisher DOI](https://doi.org/10.1016/j.system.2013.07.013). Captions can improve comprehension and vocabulary. This evidence does not prove that a particular fading sequence is optimal.

**Decision:** Keep support available, then return without it. An attempt remembers whether support was ever revealed, even if hidden before answering. The no-text pass is a product hypothesis to test, not an established cure for “caption dependency.” Chinese typography leads; pinyin remains revealable. Accessibility takes precedence over a no-caption challenge.

**Measurement:** Compare supported and unsupported comprehension using matched content and delayed tests. Do not infer dependency from one short clip. Local video playback supports timed SRT captions and A–B looping; original audio scenes are explicitly labeled.

## Conversational utility and language provenance
**Evidence:** Cai & Brysbaert (2010), [SUBTLEX-CH](https://www.ugent.be/pp/experimentele-psychologie/en/research/documents/subtlexch/cai.pdf), uses film-subtitle frequency as a useful lexical source, not a universal spoken ranking. [CC-CEDICT via MDBG](https://www.mdbg.net/chinese/dictionary?page=cc-cedict) supplies dictionary references under CC BY-SA 4.0.

**Decision:** Prioritize repair, response, plans, introductions, and high-use chunks. `utilityScore` is an authored priority heuristic; it is not presented as a corpus measurement. The downloaded dictionary evidence includes 48 exact seed matches and flags composed phrases for constituent review. Match presence does not confer human approval. Citation tone and connected-speech sandhi may differ; store and explain the distinction rather than silently replacing one with the other.

**Measurement:** Native educator checks on meaning, pinyin, classifiers, tone realization, social register, naturalness and topic usefulness before publication. More than one native reviewer for socially sensitive language.

## Feedback and accessibility
Correct one meaningful issue at a time. A missed choice gives the target, meaning and replay. Scripted pattern matching acknowledges valid replies outside its grammar. Quiet mode, text alternatives, focus indicators and reduced motion are first-class. Do not conflate a disability accommodation with a failed skill.

## Lesson shape: textbook unit, HSK task formats
Phrase lessons follow the shape of a good textbook unit and use the task types HSK and standard course books use (`src/content.ts` `exercisesFor`, tasks in `src/tasks.ts`):
1. **Meet:** hear each phrase, then see how it works. Its comprehension check comes after the *next* phrase is introduced, so the learner holds it in memory instead of echoing what they just heard. Character lessons wait two characters before each meaning check.
2. **Conversation listening:** a short dialogue using the phrases, played line by line with no text (each speaker in their own Sayo mood). Gist, detail and intent questions come first; the transcript comes after.
3. **Mixed practice in exam formats:** true/false (判断对错), choose the reply (选择回应) and fill in what you hear (听写填空; hanzi or pinyin, tones optional), interleaved so consecutive steps never test the same thing. Every new word is used in a *new* sentence.
4. **Reading in context:** a word-bank gap-fill (选词填空) or matching, then build, speak and read without pinyin.
Readings carry a real-world format (chat, post, note, story) and a stated purpose ("read to find out…"). Their questions are labelled main idea, detail or read-between-the-lines, and they end with "lock it in": a gap-fill done from memory with the text hidden.
Showing the transcript, words or pinyin turns any task into supported practice. Only unaided answers update unaided memory. Content packs supply `tasks`, and a pack's dialogue with questions becomes a listening task automatically. `npm run validate:content` and `npm run packs` gate both (`checkTask`).

## Localization and formal benchmarks
English is the implemented instructional locale. Vietnamese glosses and `L1Profile` expansion points are architecture, not a completed Vietnamese course. Do not encode unreviewed L1 stereotypes. [Official HSK resources](https://www.chinesetest.cn/HSK) are the current-exam source; the 2021 nine-level standard is modeled separately from exam delivery. No readiness number is shown without a reviewed mapping and sufficient evidence.

## Required pilot before commercial learning claims
English- and Vietnamese-speaking beginner cohorts, baseline and delayed tests, interviews, observed hesitation, microphone avoidance, pinyin use, uncaptioned comprehension, and a real conversation outside the training environment. Predefine success measures and compare retention/transfer, not just engagement. Native content and assessment review remain release gates.

## Proposed course expansion (C1, awaiting approval)

`prompts/research/course-plan.md` uses the GF0025-2021 inventories as a broad learning baseline and keeps the newer exam syllabus separate. `scripts/coverage-report.ts` measures explicit curriculum introduction, including standalone character words, rather than learner mastery or incidental appearance in text. Official grammar codes identify families; proposed completion tracking must include their subpatterns and two later retrievals.

The outline proposes 96 additional social units and alternating original drama scenes/lyrical readings. Exact word and character allocations precede each four-unit batch. All content remains AI-assisted until native review; automated pinyin, readability, task and audio checks do not certify natural Chinese or correct spoken tones. Proposed level-3 core readings remain within 300 characters, with longer stretch readings optional. These course decisions require approval before content writing and do not set timed-drill speed targets.
