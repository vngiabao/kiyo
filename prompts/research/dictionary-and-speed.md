# Dictionary and reading-speed drill: research notes and decisions

Built by Claude (October 2026). Projects A and B of `prompts/gpt-next-phase.md`. The course (Project C) is GPT's.

## A. Offline dictionary

**Source:** CC-CEDICT (MDBG and contributors), downloaded from the URL `scripts/reference-check.ts` already used. Licence CC BY-SA 4.0: the adapted data in `public/dict/` carries the same licence, with attribution in `THIRD_PARTY_NOTICES.md`, `public/dict/manifest.json` and Settings → "On this device". The app's own code is not affected by share-alike; only the dictionary data is.

**Build** (`npm run dict` → `scripts/build-dictionary.ts`):
- 121,581 entries. Numbered pinyin is converted to tone marks (ü, neutral tone, erhua, capitalised proper nouns). The first 3 senses and measure words are kept. 3,612 "variant of" entries are dropped; erhua forms such as 一点儿 get their base word's meaning; HSK 3.0 levels come from `content/hsk/levels.json`.
- Common readings come first for about 55 multi-reading characters (看 kàn before kān, 了 le, 行 xíng…), from a hand-checked table, because the source's own order is arbitrary.
- 256 shards, keyed by first character: 17.4 MB raw, 5.6 MB gzipped in total, about 68 KB raw (about 22 KB gzipped) per shard. A lookup loads only the shards for the characters in the line.
- Not precached, so the install stays small. The service worker caches shards stale-while-revalidate in `kiyo-dict`, only for real JSON responses. Settings can save all of it for offline use.

**Word splitting** (`src/dictionary.ts`): forward and backward longest-match against the dictionary. When the two disagree it takes:
1. fewer words;
2. then the split containing the longer word (好久不见/了);
3. then fewer single characters;
4. then backward (看/中国, not 看中/国).

Neighbouring numerals are joined and given a value and pinyin (二十五 = 25). No new dependency.

**Measured** on 98 hand-split subtitle and lyric lines (`tests/dictionary.test.ts`): **96.6% of word boundaries correct.** Most remaining differences are defensible alternatives where the dictionary has a longer real word: 有空, 不想, 生日快乐, 什么样, 不舒服. The test fails if accuracy drops below 95%.

**Not done yet:** reviewing saved words in the spaced-repetition queue. Attempts and memories require a known phrase id, and backup import checks that, so this needs a careful additive design (personal ids registered before validation). Saved words do export to Anki today.

## B. Timed reading drill

**Reference points** (checked 5 Oct 2026):
- [Netflix Simplified Chinese Timed Text Style Guide](https://partnerhelp.netflixstudios.com/hc/en-us/articles/215986007-Chinese-Simplified-Timed-Text-Style-Guide): up to **9 characters/second** for adult programmes and **7** for children's; 16 characters per line; at most two lines. (SDH: 11 and 9.)
- [Netflix Timed Text Style Guide: General Requirements](https://partnerhelp.netflixstudios.com/hc/en-us/articles/215758617): a subtitle event lasts **5/6 of a second minimum, 7 seconds maximum**.

**Design** (`src/drill.ts`, `src/ReadingDrill.tsx`, Practice → Reading speed):
- **Material:** only lines from finished lessons, units and readings, made entirely of characters the course has taught, 4–16 characters long, each with an English meaning. The pool unlocks at 8 lines.
- **Display:** time on screen = characters ÷ pace, clamped to 5/6 s–7 s.
- **Check:** pick the meaning from 3 choices, with the answer's position varied. No help is possible mid-line, so every answer is unaided.
- **Pace rule:** a staircase starting at 3/s, or at the last session's pace. Two correct in a row → ×1.15; a miss → ÷1.15. Range 1.5–12/s.
- **Saved:** sessions go to `readingSpeed` (Dexie v4, included in backups). The chart shows pace after each session, with the 7/s and 9/s reference lines.

**Evidence, honestly:** the subtitle figures are industry norms, not learning research. Whether flashed-line training transfers to normal reading is mixed in the research literature. The drill is designed so it can't overstate progress: it only measures recognition of the meaning of lines you've studied, at a pace, without help. It's a speed check on known material, not a comprehension test of new text.

**Not done yet:**
- A karaoke mode inside the drill. The Watch player already does karaoke with `.lrc`, and course song verses will come with GPT's units.
- A Today plan item for the drill.
