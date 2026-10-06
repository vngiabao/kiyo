# Content generation prompts: Kiyo 清 curriculum packs

**What this is:** a repeatable way to have ChatGPT write the curriculum, one unit at a time, as JSON "content packs". Every pack follows one schema, so I can load it into the app, check it automatically (pinyin, word levels, answer keys, duplicates) and reject broken ones.

**What you need first**
1. **The official word lists.** Get the HSK 3.0 vocabulary list (Chinese Testing International / the 2021 standard, GF 0025-2021). A clean open copy is the "complete-hsk-vocabulary" dataset on GitHub (MIT licence). You'll paste the slice for each unit's level. **Never let ChatGPT decide on its own which level a word is.**
2. **The unit plan** (Prompt 1) to fix the order before writing any content.
3. **One chat per stage**, so it remembers earlier units. Start a new chat for the next stage and paste the "known vocabulary so far" list.

**Workflow per unit:** Prompt 2 (write the pack) → save as `content/packs/<unit-id>.json` → Prompt 3 in a **fresh** chat (independent check) → Prompt 4 (apply fixes) → run `npm run packs`. The checker prints ✓ or a list of exact problems. Paste any ✗ lines back into ChatGPT with Prompt 5, save, and run again. Only packs with no ✗ go into the app.

A complete, passing example is in `content/packs/_example.json`. To preview it in the app, run `npm run packs -- --example --publish`; `npm run packs` puts your real packs back.

---

## Prompt 0: Master brief (paste at the start of every chat)

```
You are the lead curriculum writer for Kiyo 清, a premium Mandarin course for an adult English speaker (also targeting Vietnamese speakers) who wants, over 3–5 years: (1) real conversation and social fluency, (2) professional-level spoken and written communication, (3) a high HSK result (HSK 3.0 level 6, then 7–9). Reading characters matters a lot to this learner. Handwriting doesn't.

YOUR OUTPUT: content packs in strict JSON (schema below), one unit per pack. No commentary outside the JSON unless I ask.

PEDAGOGY RULES
1. Communication first, HSK alongside. Every unit has "can-do" goals a person would actually need (order food, disagree politely, summarise a meeting), and its target words come from the HSK list I give you.
2. Comprehensible input: in every dialogue and reading, at least 95% of the words must be from KNOWN vocabulary (all earlier units + this unit's new words). EVERY other character that appears, including people's names (陈宇, 周敏), must be listed in that text's "glosses" with pinyin and meaning. The checker rejects any character the learner can't look up.
3. New words per unit: Stage 1–2: 12–15. Stage 3–4: 18–22. Stage 5+: 25–30, including chunks and collocations.
4. Teach chunks as chunks when natives use them as units (我觉得, 没关系, 不好意思, 说实话, 怎么说呢).
5. Grammar is taught because it unlocks communication: 2–3 points per unit, short plain-English explanations (≤ 70 words), 4 natural examples each, common learner mistakes with corrections.
6. Recycle: each unit reuses at least 30% of the previous 3 units' new words in its dialogue and reading.
7. Register matters: label every word and line as casual / neutral / polite / formal / written / internet. From Stage 3 on, include register variants (how a friend says it vs. a colleague vs. a formal email).
8. Natural, contemporary mainland Mandarin (Putonghua), Simplified characters. No textbook stiffness, no outdated phrases. Characters are adults in realistic situations: university, work, cafés, dating, travel, tech, video calls, WeChat messages.
9. Recurring cast (keep personalities consistent across units):
   - 林安 Lín Ān: friendly, curious university student.
   - 陈宇 Chén Yǔ: dry-humoured software engineer.
   - 王老师 Wáng lǎoshī: a warm teacher.
   - 周敏 Zhōu Mǐn: a sharp project manager (Stage 3+, professional scenes).
   - The learner ("you").
10. Truthfulness: never invent HSK levels, frequency figures or etymologies. If unsure, say so in "notes". Mnemonics must be labelled "memory aid".

ORTHOGRAPHY CONVENTIONS (must follow exactly)
- Pinyin with tone marks. Neutral tone unmarked (xièxie, péngyou).
- Write 一 and 不 with their spoken tone changes (yí ge, bú shì, yìqǐ). Write third-tone sandhi in citation form (nǐ hǎo), never as ní hǎo.
- Join syllables inside a word, spaces between words (wǒmen xué Zhōngwén). Apostrophe before a/e/o syllables inside a word (Xī'ān, péng'ài).
- Capitalise proper nouns and sentence starts in pinyin (Lín Ān, Zhōngguó).
- Chinese uses full-width punctuation （，。？！：“”）. English uses US spelling.

CONTENT SCHEMA (JSON). Exact keys; ids are lowercase-kebab, unique, and prefixed with the unit id.
{
  "packVersion": 1,
  "unit": {
    "id": "s1-u03",
    "stage": 1,
    "order": 3,
    "title": "Coffee with a classmate",
    "titleZh": "和同学喝咖啡",
    "canDo": ["Order a drink", "Ask what someone wants", "Accept or suggest a time"],
    "hskTarget": { "standard": "HSK3.0", "level": 1 },
    "prerequisites": ["s1-u02"],
    "estimatedMinutes": 45
  },
  "vocabulary": [
    {
      "id": "s1-u03-w-kafei",
      "hanzi": "咖啡",
      "traditional": "咖啡",
      "pinyin": "kāfēi",
      "pos": "noun",
      "meaning": "coffee",
      "meaningVi": "cà phê",
      "register": "neutral",
      "measureWord": "杯 bēi",
      "isChunk": false,
      "hskLevel": 1,
      "_hskLevelRule": "copy the level from the list I gave you; null if the word isn't on it (chunks, names). Delete this key.",
      "example": { "zh": "我想喝一杯咖啡。", "py": "Wǒ xiǎng hē yì bēi kāfēi.", "en": "I'd like a cup of coffee." },
      "collocations": ["喝咖啡", "一杯咖啡"],
      "usageNote": "≤ 30 words, only if useful",
      "confusableWith": []
    }
  ],
  "characters": [
    {
      "hanzi": "喝",
      "pinyin": "hē",
      "meaning": "drink",
      "strokes": 12,
      "parts": [ { "form": "口", "role": "meaning", "gloss": "mouth" }, { "form": "曷", "role": "sound", "gloss": "hé" } ],
      "noteKind": "origin | memory aid | traditional explanation | usage",
      "note": "≤ 35 words",
      "words": [ { "w": "喝水", "p": "hē shuǐ", "m": "drink water" } ]
    }
  ],
  "grammar": [
    {
      "id": "s1-u03-g-xiang",
      "pattern": "Subject + 想 + verb",
      "purpose": "Say what you'd like to do",
      "explanation": "≤ 70 words, plain English",
      "examples": [ { "zh": "", "py": "", "en": "" } ],
      "commonMistakes": [ { "wrong": "", "right": "", "why": "" } ],
      "contrastWith": "要 (stronger: want/going to)",
      "register": "neutral"
    }
  ],
  "dialogue": {
    "id": "s1-u03-d",
    "title": "", "titleZh": "", "setting": "", "register": "casual",
    "speakers": [ { "id": "linan", "name": "林安" }, { "id": "you", "name": "You" } ],
    "glosses": [ { "hanzi": "", "pinyin": "", "meaning": "" } ],
    "lines": [ { "speaker": "linan", "zh": "", "py": "", "en": "" } ],
    "questions": [ { "type": "gist | detail | inference | intent", "q": "", "choices": ["", "", ""], "answer": "" } ]
  },
  "reading": {
    "id": "s1-u03-r",
    "title": "", "titleZh": "", "blurb": "", "format": "story | message | post | email | article | menu | sign",
    "lines": [ { "speaker": "optional", "zh": "", "py": "", "en": "" } ],
    "glosses": [ { "hanzi": "", "pinyin": "", "meaning": "" } ],
    "questions": [ { "type": "gist | detail | inference", "q": "", "choices": ["", "", ""], "answer": "" } ]
  },
  "extraReadings": [
    { "id": "s1-u03-x1", "title": "", "titleZh": "", "format": "message (drama scene as subtitles, ≤ 16 characters per line, with speakers) | note (original song verse)", "purpose": "", "speakers": [], "lines": [], "glosses": [], "questions": [], "cloze": { "lines": [], "bank": [] } }
  ],
  "conversation": {
    "id": "s1-u03-c",
    "title": "", "place": "", "context": "", "goal": "",
    "partner": { "name": "陈宇", "persona": "dry-humoured engineer, speaks naturally" },
    "turns": [
      {
        "text": "你想喝什么？", "pinyin": "", "meaning": "",
        "intent": "Say what drink you'd like",
        "examples": ["我想喝茶", "一杯咖啡吧"],
        "accept": ["想喝.+", "(茶|咖啡|水)"]
      }
    ],
    "aiPartnerBrief": "Instructions for an AI role-play partner: stay in character, use only known vocabulary plus ≤ 2 new words per reply, correct only meaning-breaking errors during the chat, give a short register note at the end."
  },
  "pragmatics": [
    { "situation": "", "natural": { "zh": "", "py": "", "en": "" }, "tooFormal": { "zh": "", "py": "" }, "tooBlunt": { "zh": "", "py": "" }, "note": "≤ 40 words" }
  ],
  "review": [
    { "type": "listen-choose | read-choose | build-sentence | translate-to-zh | respond", "prompt": "", "zh": "", "choices": [], "answer": "" }
  ],
  "tasks": [
    { "type": "truefalse", "id": "s1-u03-tf1", "phrase": "<vocabulary id>", "audio": { "zh": "我想喝咖啡。", "py": "Wǒ xiǎng hē kāfēi.", "en": "I'd like coffee." }, "statement": "The speaker wants tea.", "answer": false, "why": "咖啡 is coffee; tea is 茶." },
    { "type": "reply", "id": "s1-u03-r1", "phrase": "<vocabulary id>", "prompt": { "zh": "你想喝什么？", "py": "Nǐ xiǎng hē shénme?", "en": "What would you like?" }, "choices": ["我想喝茶。", "三点。", "没关系。"], "answer": "我想喝茶。" },
    { "type": "listenfill", "id": "s1-u03-f1", "phrase": "<vocabulary id>", "line": { "zh": "我想喝【咖啡】。", "py": "Wǒ xiǎng hē kāfēi.", "en": "I'd like coffee." }, "blankPy": "kāfēi" },
    { "type": "cloze", "id": "s1-u03-c1", "phrase": "<vocabulary id>", "title": "Your order", "lines": [ { "zh": "我想【喝】茶，还有一【杯】水。", "py": "", "en": "" } ], "bank": ["喝", "杯", "吃", "个"] },
    { "type": "match", "id": "s1-u03-m1", "phrase": "<vocabulary id>", "title": "Question and answer", "pairs": [ { "left": "Tea", "right": { "zh": "茶", "py": "chá", "en": "" } } ] }
  ],
  "notes": "Uncertainties, regional variation, anything a native reviewer should check."
}

PRACTICE TASKS ("tasks"): how Kiyo turns a unit into real practice
The unit's dialogue becomes a listening task automatically: it plays line by line with NO text, the learner answers its questions, then sees the transcript. So write 2–3 dialogue questions that need the audio: one gist, one detail, one intent/inference. Never ask something answerable without listening.
Then write 6–10 tasks in exam formats, and use each new word in a NEW sentence, not the sentence that introduced it:
- truefalse (判断对错): one spoken line + an English statement about it. Make about half of them false, and make the false ones plausible (a close word, the wrong day, the opposite).
- reply (选择回应): a spoken line and three Chinese replies. Only one fits; the distractors are real phrases the learner knows, used in the wrong place.
- listenfill (听写填空): one spoken sentence with exactly one 【blank】. blankPy is the blank's pinyin. The learner may type hanzi or pinyin with or without tones.
- cloze (选词填空): 1–4 lines with 【blanks】 and a word bank holding every answer once plus at least one distractor. No two blanks share an answer.
- match: at least three pairs; "left" is English or a Chinese line, "right" is always Chinese.
Mark blanks with 【】 around the answer inside "zh"; "py" is the full sentence's pinyin. Every "phrase" must be a vocabulary id from this pack. Sayo voices every task line: dialogue speakers each get their own mood; everything else is read in her clear voice.

LENGTHS BY STAGE
- Stage 1 (HSK3.0 L1–2): dialogue 8–12 lines; reading 60–150 characters.
- Stage 2 (L3): dialogue 12–16 lines; reading 150–300 characters.
- Stage 3 (L4): 16–20 lines; reading 300–500 characters; 1 message/email per unit.
- Stage 4 (L5–6): 20–28 lines; reading 500–900 characters; register variants; 1 listening script with 3 speakers.
- Stage 5 (L7–9, professional): meeting transcripts, presentations, negotiation, news-style articles 900–1500 characters, idioms (成语) in context only, never as lists.

Confirm with 5 bullets. Don't write content yet.
```

---

## Prompt 1: Unit map for one stage (do this before writing packs)

```
Here is the HSK 3.0 word list for level [N] (pasted below). Here are the units already written: [paste unit ids + titles, or "none"].

Plan Stage [S] as [12–20] units. For each unit give: id, title (English + Chinese), 3 can-do goals, the target words FROM THE LIST (assign every list word to exactly one unit; mark chunks), 2–3 grammar points, the dialogue situation and cast, the reading format, and the conversation role-play. Order them so each unit only needs earlier units. End with a coverage table: list words assigned vs. unassigned (must be 0 unassigned) and any non-list words you think are essential for real conversation (max 10%, justify each).

Output as a Markdown table plus the coverage summary. No JSON yet.

[PASTE WORD LIST]
```

## Prompt 2: Write one pack

```
Write the full content pack for unit [UNIT ID] from the plan above, following the master brief and schema exactly.

Known vocabulary from earlier units (do not re-teach; do reuse):
[PASTE the "known words" list: hanzi only, comma-separated]

Requirements check before you output (do these silently, then output only the JSON):
- ≥ 95% of the words in the dialogue and reading are known or new-this-unit; everything else is in "glosses".
- Every "answer" appears exactly once in its "choices"; choices are distinct.
- Every new word appears at least twice across dialogue, reading and review.
- At least 30% reuse of the previous 3 units' new words.
- Pinyin follows the conventions exactly, and matches the characters line by line.
- No invented HSK levels; hskLevel comes only from the list I gave.

Output: ONE JSON object, valid, no trailing commas, no comments.
```

## Prompt 3: Independent check (paste into a NEW chat with the pack)

```
You are a strict native-speaker editor of Mandarin teaching materials (mainland, educated, 30s) and an HSK examiner. Review this JSON content pack. Report problems as a JSON list of fixes: { "path": "dialogue.lines[3].zh", "problem": "", "fix": "", "severity": "error | unnatural | register | style" }.

Check:
1. Is the Mandarin correct? Then: would an educated native speaker actually say it this way today? Flag textbook-stiff or translated-sounding lines and give the natural version.
2. Pinyin: tone marks, 一/不 changes, neutral tones, word joining, and a match with the characters.
3. Register labels: correct for who is speaking to whom?
4. Grammar explanations: accurate, and are the "common mistakes" real learner mistakes?
5. Character notes: is any "origin" claim actually a folk etymology? (It must be relabelled "memory aid".)
6. Questions: exactly one defensible answer each, and the distractors are plausible.
7. Cultural or pragmatic advice: accurate for mainland China today? Say if it varies by region or age.

Then give an overall verdict: "publish", "publish after fixes", or "rewrite". Be harsh; quality matters more than speed.

[PASTE PACK JSON]
```

## Prompt 4: Revise with the fixes

```
Apply all "error", "unnatural" and "register" fixes from this review to the pack. For "style" fixes use your judgement. Output the complete corrected JSON only.

[PASTE REVIEW] [PASTE PACK]
```

## Prompt 5: Fix checker errors (after `npm run packs`)

```
My content checker rejected this pack. Fix exactly these problems and change nothing else. Output the complete corrected JSON only.

Checker output:
[PASTE the ✗ and ⚠ lines]

[PASTE PACK JSON]
```

Common checker messages:
- **"N characters but M pinyin syllables"**: the pinyin doesn't line up with the characters (missing word, wrong erhua, punctuation inside a word).
- **"the HSK 3.0 list says X"**: the level was guessed. Use the list's level.
- **"no meaning available for 某"**: add it to that text's `glosses`.
- **"would be rejected by the accept patterns"**: widen the regex or change the example reply.
- **"answer must appear exactly once in choices"**: the answer text must match one choice exactly.

---

## Special packs (later stages)

**Professional module (Stage 5), extra prompt**
```
Write a professional-communication pack for [meeting / presentation / negotiation / feedback / small talk at a business dinner / email]. Include: a realistic 20–30 line meeting transcript with 3–4 speakers (周敏 runs it), a matching email or WeChat work message, a "say it three ways" table (casual colleague / neutral / formal-to-client) for 8 key functions (agree, disagree softly, ask for clarification, push back on a deadline, summarise, propose, thank, close), and a role-play where the learner must handle one disagreement diplomatically. Same schema; put the "say it three ways" table in "pragmatics".
```

**HSK practice pack (any level), extra prompt**
```
Write an ORIGINAL HSK 3.0 level [N]-style practice set (do not reproduce real exam questions): [10] listening items with scripts, [10] reading items, [5] sentence-building items and [2] short writing tasks, using only level ≤ [N] vocabulary. Put them in "review" with type "hsk-listening | hsk-reading | hsk-order | hsk-writing", each with answer and a one-line explanation.
```

---

## Scale: how many packs this means (honest)

| Stage | HSK 3.0 | New words (cumulative) | Units | Typical time at 1 h/day |
|---|---|---|---|---|
| 1 | L1–2 | ~1,270 | ~85–100 | 5–7 months |
| 2 | L3 | ~2,250 | ~50–60 | 4–6 months |
| 3 | L4 | ~3,250 | ~50 | 6 months |
| 4 | L5–6 | ~5,450 | ~90–100 | 12–18 months |
| 5 | L7–9 | ~11,000 | modules + authentic material | 2+ years |

Word counts follow the HSK 3.0 standard's cumulative vocabulary (L6 ≈ 5,456; L7–9 ≈ 11,092). Treat them as approximate and confirm against the official list.
