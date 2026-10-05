# Cross-project prompt: make Kiyo (Chinese) and Shiori (Japanese) twins

Open a NEW chat with the folder `C:\Users\vngia\OneDrive - Umich\Desktop\My startups\Language Learning` (the parent of both projects) and paste the box. The new chat has no memory of earlier conversations; everything it needs is in the box and in the two project folders.

```
You're the lead of two sibling language-learning apps I'm building for myself, both in this folder:
- Chinese/  = "Kiyo 清" (Mandarin). Mascot: Sayo 小夜, an Ado-style cool sensei (introverted, dry, sudden bursts of intensity). Theme: "Night Study" (midnight navy, pale blue).
- Japanese/ = "Shiori" (Japanese). Mascot: Violetto, a Violet Evergarden-inspired letter-writer (composed, precise, sincere). Theme: antique letters (Prussian blue, ivory, emerald, ribbon red, honey gold).
Different AI sessions built them, so each is better at some things.

THE GOAL: TWINS WITH DIFFERENT SOULS
The two apps should be the SAME product in everything structural and different ONLY in character:
SAME in both (one shared standard):
- information architecture and navigation order; onboarding order; Today screen structure; lesson flow and exercise types; path map; reader; review queue; mistakes; levels and days-in-a-row; exam room structure (HSK room ⇄ JLPT room); Media Lab; Speak/role-plays; dictionary; settings; sign-in, sync, backup;
- layout grid, spacing scale, type scale roles, component set (buttons, choices, verdict bar, speech bubbles, cards, path stones, sheets), motion rules, accessibility standard;
- the expression system: same mascot moods and moments (welcome, listen, speak, read, write, think, hint, celebrate, quiet pride, encourage, gentle correction, review, rest, error, level up, keep going, exam teacher), same reaction logic, same voice-mood pipeline;
- learning engine (FSRS per skill, supported vs unaided evidence, honest progress), content-pack schema and validator strictness, content quality bar and the "vibe" of the content (realistic adult situations, recurring cast, natural modern language, register/politeness teaching);
- docs and QA standards.
DIFFERENT by character only:
- colour tokens and theme motifs (Night Study vs antique letters), fonts where the script requires it (Chinese vs Japanese typefaces), icons/ornaments (e.g. stepping stones vs wax-sealed envelopes), mascot art, persona wording, voice timbre and acting, brand name/logo;
- language-specific teaching (tones/pinyin/hanzi components vs kana/furigana/kanji readings/pitch/keigo), and HSK vs JLPT specifics.
Every screen should feel built around its character, with the same effectiveness.

SKILLS AND WORKING METHOD (use these on BOTH apps, the same way)
Design skills, applied IN SEQUENCE (don't run them all at once):
1. Taste: subtract first; every element must earn its place; calm density for daily, repeated study.
2. Hallmark (anti-AI-slop structure): installed at Chinese/.agents/skills/hallmark (read its SKILL.md and references; run its audit). No generic card grids or dashboard rhythm; each screen has its own structure; roman (never italic) headings; no invented metrics; locked tokens.
3. Impeccable (hierarchy, typography, spacing, states, accessibility, polish): both projects have a .impeccable/ folder from earlier runs. If the skill isn't available to you, install it from its official source (npx impeccable install). Run critique → polish → audit.
4. Emil Kowalski design engineering (motion and micro-interactions): if missing, install with npx skills@latest add emilkowalski/skills (emil-design-eng, review-animations, improve-animations, mobile-native, break-ui). Rules: transform/opacity only; ease-out cubic-bezier(0.23,1,0.32,1); UI motion under 300 ms; press scale 0.97; never scale from 0; no animation on keyboard-driven or 100×/day actions; hover only under (hover:hover) and (pointer:fine); prefers-reduced-motion keeps state, drops movement.
Also use any of these available to you: design critique, accessibility audit, design system, UX writing/copy, interaction design.
Working method (what made these apps good; keep doing it):
- Pre-flight: read existing tokens, fonts and components before changing anything; build on them.
- Screenshot QA: a script captures every main screen at 1440 / 768 / 375 / 320 px; LOOK at the images after each change (don't just trust tests). Check full-page and in-viewport.
- Automated accessibility (axe WCAG 2.1 AA) in the browser tests; real contrast numbers for every text token; keyboard path through every flow; no horizontal overflow at 320 px.
- Honest evidence: unit tests prove learning logic (supported answers don't count, per-skill memories), validators gate content, and the QA notes say plainly what was and wasn't verified.
- Small batches: change, run all checks, screenshot, critique, refine; at least two critique rounds before calling anything finished.
- Asset hygiene: trim mascot images to one shared frame, convert to WebP, keep originals, record provenance; keep offline precache small.

GROUND RULES
- Read both projects' AGENTS.md, README, PRODUCT/DESIGN/PEDAGOGY/PERSONA docs and QA/AUDIT notes first, and respect their rules. Never change either app's database name or storage keys; use additive migrations.
- Never blend identities: Sayo stays Sayo, Violetto stays Violetto. Don't change their approved artwork designs.
- OTHER AI CHATS MAY BE EDITING EITHER FOLDER RIGHT NOW. Before editing files in a folder, ask me "Is the Chinese/Japanese chat idle?" and wait for my yes. Until then, only read, run checks and write reports in the parent folder.
- No publishing, pushing, live services or paid APIs without my OK.
- Be honest: separate what you verified (ran, measured, saw) from what you inferred.

STEP 1: RUN BOTH (read-only)
In each project: install if needed; run type check, unit tests, content/pack validators, audio checks, browser tests (each on its own dev-server port) and its screenshot script. Record results and anything broken. Take matching screenshots of every main screen in both apps at 1440 and 375 px for side-by-side comparison.

STEP 2: AUDIT → write Language Learning/REVIEW.md
For each area, score BOTH apps 0–5 with a one-line reason and file references, and name which app has the better implementation:
learning engine · curriculum amount & progression (real counts, no inflation) · content quality & vibe · content pipeline & validators · exam room · listening/audio & voice moods · reader · speaking/role-play/AI-partner readiness · data durability (backup, sync, migrations) · mascot & persona use · design & layout · navigation & order · motion & accessibility · performance (bundle, offline size) · tests & docs · CHARACTER DESIGN · BRANDING.

CHARACTER DESIGN AUDIT (Sayo and Violetto, every pose in public/mascot/ and the teacher poses):
- Readability: silhouette and face at 36, 64, 96 and 360 px on each app's backgrounds (light and dark where they exist); does the pale edge/outline separate her from the background?
- Pose clarity: can each mood be told apart at thumbnail size without its caption? Which poses look too similar?
- Expression range: brows, eyes, mouth and the top strand of hair actually acting; persona fit (Sayo cool and Ado-style with bursts; Violetto composed and sincere).
- Consistency: same face, proportions, outfit details, colours, line weight and framing across all poses (no size jumps between poses); consistent style with the app's theme.
- Integration: placement, sizes and motion in each screen; speech bubbles; reduced-motion behaviour; image weight.
- Originality and likeness: note where the art closely resembles an existing person or character (fine for private use; flag for any public launch).
- Missing or weak poses per the shared expression list. Write ready-to-paste image-generation prompts that change only those poses and keep the approved design locked.

BRANDING AUDIT (both apps):
- Name, logo/mark, wordmark, app icon, favicon, social/OG image, splash/loading, masthead lockup and the Welcome hero; how each reads at 16, 32, 60, 180 and 1024 px on light and dark backgrounds.
- Fit with character and theme; consistency between the brand and the in-app UI; vector quality (SVG, no fonts, clean paths); a complete icon set for web/PWA/iOS/Android.
- Kiyo's current state: placeholder 清 stroke-data mark + KĪYO wordmark; candidate concepts in Chinese/output/kiyo-review-v2/ (A: Sayo leaning on the wordmark; B: Sayo portrait tile + KĪYO). Shiori's brand is provisional; review what exists.
- Give a recommended brand system for each (same structure: mark, wordmark, icon, favicon, hero, OG), with ready-to-paste prompts to produce the final vector assets, and note that a trademark search is needed before any public launch.
Then list every structural DIFFERENCE between the apps (screen order, flows, components, features one has and the other lacks), and for each decide: adopt Kiyo's way / adopt Shiori's way / merge into something better.

STEP 3: SHARED STANDARD → write Language Learning/SHARED-SPEC.md
The single source of truth both apps follow:
1. Navigation and screen order; onboarding steps; Today layout.
2. Lesson flow and the full exercise-type list (union of the best from both).
3. Component inventory with anatomy (verdict bar, choices, speech bubble, path stone, unit banner, sheet, tabs…) and the shared spacing/type/motion tokens; then a THEME TABLE mapping each shared role to Kiyo's and Shiori's values (colour, font, ornament).
4. Expression system: the list of mascot moments → pose, line style, voice mood, where it appears; then Sayo's and Violetto's versions side by side.
5. Learning-engine rules, content-pack schema (one shared schema with language-specific fields), validator checklist, content style guide (cast, situations, register, lengths per stage).
6. Exam room structure (HSK ⇄ JLPT), progress/levels/streak rules, sync/backup rules, QA checklist.
7. Character standard: shared pose list, framing/size rules per placement, image pipeline, persona-writing rules (Sayo vs Violetto columns).
8. Brand standard: the asset list and sizes every app ships, how the mascot appears in the brand, and each app's values.
9. Skills & method: the design-skill sequence and QA routine above, so every future session follows them.
Also produce two ranked task lists to reach the spec:
- Language Learning/TASKS-kiyo.md and Language Learning/TASKS-shiori.md (what, why, files, how to verify, size S/M/L; quick wins marked; biggest learning impact first).
Add an honest verdict for each app: how far it is from HSK 5–6 / JLPT N2–N1 and professional level, and the shortest credible path.
STOP and show me: the scores table, the top differences with your decision for each, and the two top-10 task lists.

STEP 4: BRING BOTH TO THE SPEC (only after I confirm a folder's chat is idle)
Work one app at a time in small verified batches, top-down from its task list. After each batch run that app's full checks (types, unit tests, validators, audio check, browser tests, build) and compare screenshots side by side with the other app; fix regressions before continuing. Keep each app's theme and persona; share structure, not skin. Update each app's AGENTS.md (link to SHARED-SPEC.md as the shared standard), QA and README.
Finish with before/after scores for both apps, side-by-side screenshots of the same screen in each, and a plain-English report: changed / verified / still needs my ears, eyes or decisions.
```
