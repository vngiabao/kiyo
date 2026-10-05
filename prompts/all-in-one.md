# All-in-one prompt for the work chat (next big round)

Paste everything in the box into the work chat. It runs in phases and stops at the two points where your decision is needed.

```
Read AGENTS.md first and follow its rules. This is the next big round of work, in phases. Work autonomously inside each phase; STOP only where it says STOP. After each phase run: npx tsc -b, npm test, npm run validate:content, the audio check, and the browser tests; inspect screenshots at 1440/768/375. Report each phase in plain English (done / verified / not verified). No publishing, pushing, live Supabase or paid API calls without my explicit OK.

PHASE 1: FIXES
1. Today lead card: pinyin must be smaller than the characters (about 30–35% of the hanzi size), sit under them, and never overflow the tile at any width.
2. HSK notebook: include it in cloud sync (new record kinds in the migration + allow-list, schema_version stays versioned) and in the main Export/Import backup. Keep its own export too.
3. Offline size: stop precaching all audio. Precache the app shell, fonts, stroke data and the audio for the current + next lesson only; cache other clips on first play (CacheFirst, size-limited). Add a "Download this unit for offline" button per unit. Report the new precache size.
4. Navigation: main nav = Today · Read · Listen · Speak · HSK · Media. Practice, Review, Progress, Dictionary, Settings go under More (desktop: a compact "More" menu; phone: the existing drawer).
5. Link Read and HSK: finishing a Read unit marks the matching HSK foundation notes as studied (not as a passed checkpoint: checkpoints still need 80% unaided).

PHASE 2: APPLY THE KIYO BRAND (decided)
Use the concepts in output/kiyo-review-v2/ (concept-a.png, concept-b.png):
- Wordmark: ONE wordmark everywhere = B's capitals "KĪYO" with the blue bar over the I; straighten the K's curved leg so it matches the other letters. Redraw it as clean vector SVG paths (no fonts, no raster), in light and dark versions.
- App icon: B's portrait tile, re-cropped tighter on Sayo's eyes, bangs and top hair strand, slightly simplified so it reads at 60 px. Export PNG icons: 1024 (App Store/master), 512 and 192 (PWA, plus maskable versions with a safe margin), 180 (apple-touch-icon), and an Android adaptive foreground/background pair.
- Favicon (16/32 px): the existing 清 mark SVG (a face can't be read that small).
- Hero lockup (Welcome screen, README, social/OG image 1200×630): concept A's composition (Sayo leaning on the wordmark) but with the KĪYO capitals.
- Wire it in: index.html (favicons, apple-touch-icon, theme colour, OG/Twitter meta + image), vite PWA manifest icons, the masthead (small tile + wordmark), the Welcome screen hero, the loading screen. Keep src/brand.tsx as the single source of name/tagline.
- Put all brand files in public/brand/ and a one-page brand sheet at output/brand/brand-sheet.html. Screenshot the Welcome screen, masthead, the phone home-screen icon (simulate on a dark and a light wallpaper) and the browser tab.
STOP and show me the brand sheet + screenshots before moving on.

PHASE 3: CONTENT (the biggest gap: write the curriculum yourself)
Write Stage 1 as content packs, following prompts/content-prompt.md EXACTLY (Prompt 0 rules + schema; content/packs/_example.json is a passing reference):
- Use the HSK 3.0 level 1 words in content/hsk/levels.json as the target list; plan ~12 units first (Prompt 1 style unit map saved to content/packs/PLAN-stage1.md), each unit 12–15 new words, 2–3 grammar points, dialogue, reading, role-play, "say it naturally" items, review items. Recurring cast as in the prompt; all audio is Sayo's voice (moods per speaker).
- Write units s1-u01 … s1-u12 into content/packs/, run npm run packs, and fix every ✗ until all pass. Then do a strict self-review per Prompt 3 (naturalness, register, pinyin, folk etymologies) and fix what you find; record remaining doubts in each pack's "notes".
- Generate audio for all pack phrases, examples, dialogue and reading lines with Sayo's locked voice ("clear" mood for teaching lines), and add them to the manifest.
- Report: words taught, characters, grammar points, minutes of study added, coverage stats, and every warning you chose to keep.

PHASE 4: GRAMMAR
- Grammar reference page (under More and linked from the dictionary): every grammar point from all packs, searchable by pattern/English/Chinese, grouped by stage; each page shows the pattern card, examples with audio, mistakes, and "seen in unit X".
- Review queue: include grammar examples (build-the-sentence from word tiles) and "say it naturally" items (choose the natural phrasing), scheduled with FSRS like everything else, unaided answers only.

PHASE 5: AI CONVERSATION PARTNER (build locally, don't connect paid services)
- A Supabase Edge Function proxy that calls the Claude API (default model claude-sonnet-5-5, configurable; key ONLY in the server secret, never in the browser). Rate-limit per user, cap tokens per turn, log no conversation content.
- The partner IS Sayo (persona per AGENTS.md: cool, brief, sincere; stays in Mandarin; uses only the learner's known vocabulary + at most 2 new words per reply, glossed). Use each pack's conversation.aiPartnerBrief and goal.
- During the chat: correct only errors that break meaning. After the chat: a short report (communication / naturalness / register / 3 better phrasings / words to learn), each phrasing playable in Sayo's voice.
- Typed input first; voice input optional via the browser's speech recognition with a clear "accuracy not guaranteed" note. Keep the scripted role-plays as the offline fallback.
- Test with a local mock of the function (no real API calls). Write setup steps (secret name, deploy command, cost note) in README.
STOP and ask me before deploying the function or adding the API key.

PHASE 6: WRAP-UP
Update AGENTS.md (state + next tasks), README, QA.md and DESIGN.md (brand section). Give me a short final report: what changed, what was verified, what still needs my ears/eyes or a decision.
```
