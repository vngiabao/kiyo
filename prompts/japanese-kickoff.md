# Kickoff prompt: Japanese learning platform (Violet Evergarden edition)

Paste everything inside the box into a new chat in a new, empty project folder. It's long on purpose: it carries over everything learned building the Mandarin app (Kiyo), so the new project starts at that level instead of from scratch.

If the chat can read files on your computer, point it at the Mandarin project as a working reference:
`C:\Users\vngia\OneDrive - Umich\Desktop\My startups\Language Learning\Chinese`

---

```
You are building a complete, personal Japanese-learning web app for me, from absolute zero to natural, high-level Japanese. Work autonomously: inspect, plan briefly, build, run, test, screenshot, critique, refine. Don't stop at a plan or a mockup. Don't ask me trivial questions. Ask only when a decision is genuinely mine.

=====================================================================
1. WHO I AM AND WHAT I WANT
=====================================================================
- Native/strong English speaker (also Vietnamese). Starting from zero.
- Goal over years: understand people and anime/drama/YouTube without subtitles, hold real conversations, read manga, light novels and articles, write messages, and eventually speak politely and professionally (keigo).
- Reading matters a lot to me. Handwriting doesn't (optional only).
- JLPT matters as a secondary benchmark: I want to pass N5 → N1 along the way. Communication is the spine and JLPT is mapped alongside it, never the other way round.
- I'll use this daily for years. It must stay valuable after the beginner phase.

=====================================================================
2. PEDAGOGY (product rules, not theory)
=====================================================================
Write a short PEDAGOGY.md that turns these into rules, with reasons:
- Learning loop: Hear → Understand → Notice → Imitate → Recall → Respond → Use → Meet again → Generalise.
- Four Strands (Nation), weighted toward listening and speaking, with reading strong because I care about it.
- Spaced repetition with FSRS (use the ts-fsrs library). Track SEPARATE memories per skill: reading (kanji → meaning), reading aloud (kanji → reading), listening (audio → meaning), recall (meaning → Japanese), typing. Reading a word is not the same as hearing it.
- Honest evidence: only unaided answers count. Revealing furigana, romaji or a transcript marks the answer as supported. No fake fluency scores, no invented JLPT predictions.
- Comprehensible input: every text is at least 95% known words; everything else is glossed.
- Teach chunks as chunks: よろしくお願いします, ちょっと待って, そうなんだ, なるほど, 〜てもいいですか.

JAPANESE-SPECIFIC RULES
- Three ways in. Let me choose at onboarding and switch any time:
  a) "Kana first": hiragana → katakana → first kanji, reading-led.
  b) "Sound first": listening and phrases first, kana alongside.
  c) "Side by side".
- Romaji is scaffolding for about the first 2 weeks only, then it fades. Furigana replaces it and is always shown on NEW words. Quizzes start without furigana; revealing it marks the answer as supported. Track "read with furigana" and "read without" separately.
- Kana: teach by shape families, with original mnemonics labelled "memory aid", plus stroke-order animation. Dakuten and handakuten, small ゃゅょっ, long vowels, katakana loanword patterns.
- Kanji: radicals/components, meaning and sound parts, on'yomi vs kun'yomi explained simply, and words that use each kanji. Prioritise by frequency and usefulness, cross-checked against JLPT and the Jōyō list.
- Pitch accent: teach it explicitly but lightly at first (visual high/low line over words, minimal pairs like 箸/橋/端, 雨/飴). Deepen it later. Never fake pitch scoring.
- Politeness is a core skill, not a footnote: casual (タメ口) ↔ polite (です/ます) ↔ keigo (尊敬語/謙譲語). Every word and line is labelled with its register. Exercises include "Which fits this situation?" and "Say it three ways".
- Grammar through communication: particles (は vs が first, explained by function), verb groups and forms (て-form early), counters, giving/receiving (あげる/くれる/もらう), sentence-final particles (ね/よ/な/かな) for social meaning.
- Listening ladder: clear single speaker → natural speed → casual contractions (〜ちゃう, 〜じゃん, って) → multiple speakers → anime/drama style → no subtitles.
- Media Lab: clip loop of gist, then detail, then transcript, then shadowing, then the same clip again with no text. Track subtitle dependence.

=====================================================================
3. CURRICULUM SHAPE
=====================================================================
- Stage 0: Sounds and kana (hiragana in about 8 short lessons, katakana in about 6), first greetings, numbers 1–10 and counting, self-introduction.
- Stages 1–5 map onto JLPT N5 → N1 (about 800 / 1,500 / 3,700 / 6,000 / 10,000 words, roughly 100 / 300 / 650 / 1,000 / 2,000 kanji). Treat these figures as approximate.
- Curriculum is DATA, not code: JSON "content packs", one unit each (vocabulary with kanji, kana and furigana, pitch pattern, JLPT level, register, example; kanji entries; grammar points; dialogue; reading; role-play; "say it naturally" items; review items). A validator script checks:
  - kana/kanji/reading alignment;
  - JLPT level against an open word list;
  - answer keys;
  - every kanji in a text is known or glossed;
  - ≥ 95% coverage;
  - role-play accept patterns accept their own examples.
  Only passing packs reach the app.
- Use open data: JMdict / KANJIDIC2 (EDRDG), KanjiVG (stroke order SVGs), an open JLPT word list, and Tatoeba sentences for reference. Generated Japanese must be checked against them and marked "AI-assisted draft" until reviewed.
- Seed a REAL first slice (several hours of study), not an empty shell: all of hiragana and katakana, about 40 first words and phrases, 6 graded readings with tap-to-gloss, 3 role-plays.
- Recurring cast with stable personalities, appearing across units, so the course feels like a serialised story.

=====================================================================
4. DESIGN: VIOLET EVERGARDEN, "ANTIQUE ELEGANCE"
=====================================================================
Visual direction: Violet Evergarden. Post-war European elegance, letters and typewriters, the postal company, fountain-pen ink, ribbons, brooches, quiet emotion. The app should feel like a beautifully kept writing desk where you learn to understand people's words. Feelings conveyed through words is literally the theme of the series and of learning a language.

PALETTE (define as CSS tokens; light AND dark themes; check WCAG AA contrast and adjust values if needed)
Light, "Morning letter" (default):
  paper #F6F1E7 (ivory)       card #FBF8F1 (cream)        rule #DDD3C2
  ink #1F2A44 (Prussian blue) ink-2 #4A5470               ink-3 #6B7186
  accent #1F6B57 (emerald, Gilbert's brooch: buttons, links, progress)
  accent-wash #E1EEE8         ribbon #A8323E (Violet's ribbon: alerts and wrong answers, sparingly)
  honey #C9A15A (her hair: borders, highlights, active states; never for body text on light)
Dark, "Night post":
  paper #121B2E  card #1A2540  rule #2E3A58  ink #F3EDE1  ink-2 #CFC6B5
  accent #5FB79A  ribbon #E0727C  honey #E2C07F
Correct answers use emerald, errors use ribbon red, highlights use honey. Prussian blue is the identity colour. Nothing neon, no gradients except a soft paper vignette.

TYPOGRAPHY
- Japanese display and reading: a Mincho serif (Shippori Mincho or Noto Serif JP). Large, airy, generous line-height (1.8+ for reading).
- English headings: a classical serif (Cormorant Garamond or EB Garamond), upright, never italic headings.
- UI and body: a clean humanist sans (e.g. Inter Tight or Source Sans 3) at 17px minimum.
- A typewriter accent for "letters" moments (Courier Prime or IBM Plex Mono).
- Hierarchy: Japanese > furigana > romaji (early only) > English. Furigana uses <ruby> and is never bigger than 50% of the kanji size.

SIGNATURE FEATURES (theme-driven, but they must teach)
- "Letters": short letters from the cast are the reading texts. The learner reads them (tap any word for its meaning, furigana toggle), answers questions, and later writes short replies. The typewriter animation is a reveal effect only, not a slowdown.
- "Auto Memory Doll" mentor mascot: an elegant, composed young-woman letter-writer, Violet-inspired: blonde braided hair, deep-blue coat, red ribbon, emerald brooch, mechanical silver hands as a detail. Persona: polite, precise, sincerely trying to understand feelings. She speaks in short Japanese lines (Japanese → furigana/romaji → English) that are themselves learnable phrases, with a reaction set:
  - welcome: いらっしゃいませ / ようこそ
  - correct: その通りです
  - correct with a hint: 次はヒントなしで
  - wrong: もう一度
  - wrong politeness level: 少し失礼かもしれません
  - level up: お見事です
  Design about 16 poses (welcome, listen, speak, read, write at a typewriter, think, hint, celebrate, quietly proud, encourage, the politeness correction, review, rest with tea, error, level up, keep going) and keep her framing consistent.
- Path map: a winding route of stamped postal envelopes or wax seals as lesson stones, units as postmarked banners, the mascot at "start here". Plus a plain-language whole journey (10 steps from "Kana and hello" to "Keigo at work").
- Delight with restraint: wax-seal stamp on lesson completion, a subtle paper texture, ribbon underline on the active tab. Motion follows Emil Kowalski's rules: transform/opacity only, ease-out (cubic-bezier(0.23,1,0.32,1)), under 300 ms, press scale 0.97, no animation on keyboard-driven actions, reduced-motion respected.

DESIGN PROCESS
Apply in sequence:
1. Taste: subtract until every element earns its place.
2. Hallmark: no generic card grids or AI-dashboard rhythm; each screen gets its own structure.
3. Impeccable: hierarchy, spacing, states, accessibility.
4. Emil Kowalski: motion and micro-interactions.
Build → screenshot at 1440 / 768 / 375 px → critique → refine, at least twice. Write DESIGN.md once it's stable.

=====================================================================
5. PRODUCT STRUCTURE
=====================================================================
- Navigation: Today · Read (かな/漢字) · Listen · Speak · Practice · Media · Progress. On phones: bottom tab bar plus a "More" drawer.
- Today answers "what should I do now?": a lead lesson, a timed plan (10/20/30/45/60 min, adapting to my weak skills), something to read, reviews due, level, days in a row (gentle, can be turned off).
- Levels = lessons finished, each level-up says "Now you can…". No meaningless XP.
- Progress shows separate skills (reading, listening, speaking practice, typing, politeness) and kana/kanji status (not met → met → recognised → secure), plus a JLPT alignment view with an honest "mapping pending" until verified.
- Dictionary: search by kana, kanji, romaji or English; kanji pages with stroke order and components.
- Speak: scripted role-plays with accept patterns now; architect an AI conversation partner later, called through a server so keys never reach the browser.
- Sign-in screen first, with the mascot greeting; local guest mode always works; cloud sync designed for later.

=====================================================================
6. ENGINEERING
=====================================================================
- React + TypeScript + Vite, PWA (offline), Dexie/IndexedDB local-first, ts-fsrs, @fontsource fonts (self-hosted).
- Stroke order: KanjiVG (or hanzi-writer-style animation on KanjiVG data) for kana and kanji.
- Audio: local TTS to start (Kokoro has Japanese voices), device voices as fallback; architecture ready for better voices. Sentence and word audio; Space replays.
- Tests: unit tests for learning logic (supported answers don't count; listening misses don't touch reading memory; FSRS schedules; pack validator), Playwright end-to-end tests including axe accessibility at desktop and phone sizes.
- Docs: README (how to run), PEDAGOGY.md, DESIGN.md, AGENTS.md (a handoff note for future AI sessions: map, commands, rules, next tasks).

=====================================================================
7. FIRST RESPONSE
=====================================================================
Before coding, reply with:
1. A one-paragraph product summary in your own words.
2. Three app-name options. Short, Japanese, two syllables with an a–o or i–o vowel pattern if possible (my taste: names like Ado, Shiro, Sayo, Kiyo), each with kanji and meaning tied to words, letters or voice.
3. The mascot's name and a one-line persona.
4. The build order for the first vertical slice (no more than 10 steps).
Then start building immediately, in the same turn if you can.
```
