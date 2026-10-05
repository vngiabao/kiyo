---
name: Tingjian 听见
description: Night Study — the Reading Room in midnight navy, with quiet Sayo company.
colors:
  paper: "#101b2b"
  paper-deep: "#1b2c41"
  sheet: "#17263a"
  ink: "#f0f3f5"
  ink-2: "#c7d3df"
  ink-3: "#aabccd"
  ink-4: "#9aafc3"
  rule: "#304359"
  rule-strong: "#657f98"
  accent: "#b3d2f5"
  accent-hover: "#d2e5fc"
  accent-wash: "#263d57"
  on-accent: "#102238"
  good: "#9bcdbc"
  good-wash: "#1b3937"
  bad: "#f2b29e"
  bad-wash: "#422d32"
  sound: "#dcc098"
  t1: "#f2b29e"
  t2: "#e2c492"
  t3: "#9bcdbc"
  t4: "#b3d2f5"
  t5: "#afbecd"
  scrim: "rgb(3 9 18 / 0.72)"
  video-backdrop: "#000"
typography:
  display:
    fontFamily: "'Newsreader Variable', 'Noto Serif SC', Georgia, serif"
    fontSize: "clamp(34px, 4.4vw, 52px)"
    fontWeight: 500
    lineHeight: 1.15
    letterSpacing: "-0.012em"
  title:
    fontFamily: "'Newsreader Variable', 'Noto Serif SC', Georgia, serif"
    fontSize: "clamp(24px, 2.4vw, 30px)"
    fontWeight: 500
    lineHeight: 1.15
    letterSpacing: "-0.012em"
  ui:
    fontFamily: "'Instrument Sans Variable', 'Noto Serif SC', system-ui, sans-serif"
    fontSize: "17px"
    fontWeight: 400
    lineHeight: 1.6
  han:
    fontFamily: "'Noto Serif SC', 'Songti SC', 'STSong', serif"
    fontSize: "clamp(44px, 7vw, 72px)"
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: "0.04em"
  label:
    fontFamily: "'Instrument Sans Variable', 'Noto Serif SC', system-ui, sans-serif"
    fontSize: "13px"
    fontWeight: 500
    lineHeight: 1.6
    letterSpacing: "0.08em"
rounded:
  r-sm: "6px"
  r: "10px"
  r-lg: "16px"
  circle: "50%"
spacing:
  compact: "8px"
  related: "10px"
  control: "14px"
  section: "28px"
  gutter: "clamp(16px, 4vw, 48px)"
components:
  button-primary:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.on-accent}"
    rounded: "{rounded.r}"
    padding: "0 22px"
  button-primary-hover:
    backgroundColor: "{colors.accent-hover}"
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    rounded: "{rounded.r}"
    padding: "0 22px"
  button-danger:
    backgroundColor: "{colors.bad}"
    textColor: "{colors.on-accent}"
    rounded: "{rounded.r}"
    padding: "0 22px"
  field:
    backgroundColor: "{colors.sheet}"
    textColor: "{colors.ink}"
    rounded: "{rounded.r}"
    padding: "0 14px"
  navigation:
    textColor: "{colors.ink-3}"
    padding: "0 12px"
    height: "64px"
  goal-chip:
    textColor: "{colors.ink-2}"
    rounded: "{rounded.r}"
    padding: "0 14px"
  answer-choice:
    backgroundColor: "{colors.sheet}"
    textColor: "{colors.ink}"
    rounded: "{rounded.r}"
    padding: "12px 18px"
  audio-disc:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.on-accent}"
    rounded: "{rounded.circle}"
    width: "84px"
    height: "84px"
  text-teaser:
    backgroundColor: "{colors.sheet}"
    textColor: "{colors.ink-3}"
    rounded: "{rounded.r}"
    padding: "22px 24px"
---

# Design System: Tingjian 听见

## Overview

**Creative North Star: "Night Study in the Reading Room"**

An editorial study instrument in midnight navy, with elevated blue surfaces, soft white text, pale blue actions, and quiet Sayo company. The user pinned Oura phone-app colour relationships and approved the exact slender, small-face mascot reference. This is a palette adaptation and character replacement within established surfaces; typography, layout, learning content, and evidence rules retain their authority.

**Chinese characters are the primary imagery**, set large on a faint 米字格 practice grid, drawing themselves stroke by stroke. The user-requested Sayo companion is the sole illustration exception: small, decorative support in learning surfaces, with a dedicated collection for the full artwork. Everything else steps back.

**Key Characteristics:**
- Chinese leads; pinyin follows; English supports.
- Midnight surfaces, pale blue actions, quiet teal success, warm peach errors.
- Editorial typography and ruled, task-specific layouts.
- Slender, small-face Sayo with restrained expressions and finite motion.

The palette is inspired by the referenced Oura app relationships, not a claim to reproduce proprietary Oura tokens, navigation, or health features. Exact implemented values live in this frontmatter and `src/styles.css`; `.impeccable/design.json` carries extensions and component states.

The Reading Room's established structure remains: subtraction removed the rail, avatar card, saved-device pill, footer quote, decorative waveform, sub-brand tagline, and navy hero card. Today answers what next with one lead and a numbered plan. Today is an editorial front page; Read is a table of contents with character previews; All characters is a specimen sheet; the reader is a typeset page; Progress is a ruled table. No invented claims or italic headings.

## Colors

The incumbent CSS names `paper`, `sheet`, and `ink` are retained for compatibility; they now describe night surfaces and light foregrounds.

- **Midnight Page / Elevated Blue / Recessed Blue** (`paper`, `sheet`, `paper-deep`): the base, reading surfaces, and hover/recessed regions.
- **Soft White through Quiet Blue** (`ink` through `ink-4`): primary to secondary text hierarchy. Keep body and control text at AA contrast on their actual backgrounds; dim/disabled states are distinct from readable secondary text.
- **Pale Blue** (`accent`) with **Bright Blue** (`accent-hover`), **Blue Wash** (`accent-wash`), and **Deep Action Ink** (`on-accent`): links, focus, selection, progress, and pale-filled actions. Accent also marks the meaning component in character anatomy and radical strokes.
- **Quiet Teal / Teal Wash** (`good`, `good-wash`) and **Warm Peach / Peach Wash** (`bad`, `bad-wash`): evidence-based verdicts, always with words and icons.
- **Warm Sound** (`sound`): the sound component in character anatomy.
- **Tone colours** (`t1`–`t5`): optional, on by default, and functional pinyin tone cues.
- **Rules / Strong Rules** (`rule`, `rule-strong`): structural dividers and interactive outlines; **Night Scrim** (`scrim`) separates drawers from content.
- **Video Black** (`video-backdrop`): the existing `#000` local-video letterbox/backdrop only. This media role is documented from a literal CSS value, not a new CSS variable or general surface colour.

Native controls use `color-scheme: dark`. Text selection uses accent/on-accent; native select options use sheet/ink, placeholder text uses ink-4, and scrollbars use rule-strong/paper. Browser and PWA chrome follow the night palette.

**The Meaningful Color Rule.** Preserve text and icons alongside state colour; a companion reaction or a coloured surface is not assessment evidence.

Character status remains not met (ink-4) → met (ink-2) → recognised (accent) → secure (ink, semibold).

## Typography

- **Display:** Newsreader 500, roman only, for page titles, lesson titles, numerals, and meanings. Title sizes remain fluid as extracted above.
- **UI:** Instrument Sans for controls, body, and pinyin. Body is 17px/1.6. The established hierarchy includes 13 / 15 / 17 / 19 / 24 / 30 / 44–52px roles rather than a newly imposed scale.
- **Han:** Noto Serif SC (Songti fallbacks), 400 at display sizes, 600 for small emphasis. The frontmatter han role describes the reusable phrase; specimens may be much larger.
- **Eyebrows:** 13px uppercase, 0.08em tracking, often prefixed with the section character (读 Read, 听 Listen, 说 Speak).
- **Reader:** 28–38px Songti lines; Chinese learning content remains prominent and never reduced to a small decorative label.

**The Chinese First Rule.** Hierarchy is Chinese > pinyin > English; revealable reading support must not compete with the phrase or specimen.

## Layout

- Desktop retains a sticky 64px masthead with wordmark, text navigation and underline, search, and settings. Content is capped at 1180px with the fluid gutter token.
- At 1080px masthead spacing compacts; at 900px task columns stack. At 820px the masthead keeps wordmark and tools, with a five-slot tab bar (今天 读 听 说 ⋯); More opens a bottom drawer. Further phone refinements occur at 640px.
- Focus mode retains a 60px header, 3px progress rule, a 760px column, and fixed verdict footer. Success/error use the corresponding dark wash and light state colour.
- Lists are ruled, with stronger leading rules and quieter row separators. Rounded containers identify interactive choices, text teasers, conversation space, and sheets.
- The Sayo collection preserves its existing composition. At 700px it stacks with the selected pose above copy and two larger thumbnail columns. Its gallery layout is not a pattern for lessons.

## Elevation & Depth

Tonal surfaces and rules do most of the work. Inset shadows form control outlines, not floating card elevation. A floating reader gloss uses `0 12px 32px rgb(3 9 18 / 0.35)`; the night scrim handles modal separation. Keep ordinary lesson rows flat.

## Shapes

The shared radii are small (6px), control (10px), and sheet (16px). Audio controls are circular. Choices use a 58px minimum row height; primary buttons and fields use 48px minimum height. Follow implemented component measurements rather than introducing a new shape scale.

## Components

### Controls and navigation

Primary buttons use pale blue with deep action ink, 16px medium UI text, 48px minimum height, and the extracted padding. Hover uses accent-hover; secondary buttons use a transparent surface with an inset strong rule and a recessed-blue hover. Destructive buttons use bad/on-accent. Button press scale is 0.97; disabled buttons use opacity 0.38.

Fields use sheet/ink, a strong-rule border, 17px text, and minimum height 48px. Their focus outline is 2px accent without offset. General focus is a 2px accent outline offset by 3px. Goal chips use an inset strong rule; selected chips invert to ink/paper. Main navigation uses an ink underline, not pills. Hover changes are constrained to fine pointers in the shared interface.

### Learning primitives

- **HanziStage:** square practice grid, hanzi-writer SVG, radical strokes in accent, Watch the strokes, optional tracing (never scored). Falls back to the font glyph.
- **CharacterAnatomy:** meaning (display), sound behind How does it sound? on the characters path, parts row (glyph / role / gloss joined by +), labelled note (origin · traditional explanation · memory aid · usage), and example words.
- **Choice:** 58px rows with numbered key; 1–4 select and Enter checks. Selected, correct, incorrect, and dim states use their token roles and explicit feedback. The glyph-choices variant is four columns, two on phones.
- **Reader:** untaught characters have dotted underlines; tap for a floating gloss card; pinyin and English are toggles.
- **Audio:** the primary disc is 84px, pale blue with deep icon ink. Playback changes state; explanatory text and inline errors remain the source of meaning.
- **Text teaser:** a sheet surface, fine border, and restrained corner radius frames useful Chinese rather than decorative art.

### Motion

Interface transitions are generally 160–300ms, with ease-out curves; the existing lesson-progress transform is 400ms. Selection communicates through colour, outline, and opacity, without a new animated sequence. Press feedback and short step/gloss entry acknowledge action. Reduced motion collapses animation and structural movement, removes the relevant press transforms, and holds the audio equalizer still. Mascot motion has its own stricter suppression rule below.

### Quiet Sayo companion

The approved character has slender proportions, a **small face**, subtle eyes and mouth, narrow cheeks, and calm poses. Preserve midnight navy hair, turquoise eyes, black coat-dress, and teal brooch. The previously wide, squat face and exaggerated meme expressions are superseded. Approval is tied to `exec-f5923449-08b7-4bc1-8597-e45f2b2946e9.png`, recorded in the current surface brief; no new layout choice or seed is implied.

Sixteen transparent square PNGs ship in `public/mascot/quiet/`: grumpy, smug, welcome, listen, speak, read, write, think, hint, celebrate, encourage, review, rest, error, thumbsup and run. Ten owner-approved revisions from `output/sayo-review-v1/` are installed; six original poses are retained. Revision prompts and provenance are preserved in `content/mascot/approved-revisions/`; the previous shipping PNGs are backed up in `content/mascot/pre-approved-poses-backup/`. The older `mascot-quiet-set.zip` is an archive, not the current sixteen-pose bundle.

Keep Sayo subordinate to Chinese and nearby instructions. The image is decorative (`alt=""`, `aria-hidden="true"`, `pointer-events: none`); nearby text carries feedback and controls remain separate. No custom cursor or pointer following. Notebook/cards must carry no readable answer character; instructional props stay outside independent checks. Use encouragement for mistakes and unscored attempts, and never treat a reaction as evidence.

Sayo's app-wide presentation is enlarged by 35% from the previous base sizes, with square, proportional frames. Lesson prompts use 140px frames (110px on phones), and answer reactions use 152px (104px on phones). Welcome, onboarding, path guides and gallery have larger responsive sizes too. Lesson spacing and the reaction's bottom offset reserve room for the enlarged art; the artwork itself is unchanged.

`src/Mascot.tsx` and `src/mascot.css` apply finite whole-pose transforms. Grumpy and error use a gentle thought tilt (1100ms and 900ms), smug settles with ±1px movement (1100ms), and celebration rises only 6px (1050ms). The prior stomp keyframes remain in CSS but are not assigned to current states. Total runs remain 650–3200ms, including two 1600ms listening sways or two 900ms speaking nods. They never block controls or loop indefinitely. These are **not fully articulated, skeletal, lip-synced, or frame-by-frame animation**.

Settings persist **Show Sayo** and **Animate Sayo**. Hiding Sayo removes her from ordinary learning; the deliberately opened collection still displays the artwork. Motion is initially suppressed while preferences load. The persistent motion setting applies to learning and collection, and the system's reduced-motion preference overrides both with no mascot animation or transform. Replay cannot override either preference.

The `/#companion` collection remains available before onboarding, starts with Welcome, and offers all sixteen states, replay/pause, and a selected-original download from `/mascot/quiet/`.

## Do's and Don'ts

### Do:
- **Do** preserve Chinese > pinyin > English and task-specific layouts.
- **Do** use the night tokens for shared surfaces, controls, focus, and text.
- **Do** keep mascot expressions quiet and faithful to the approved small-face reference.
- **Do** respect persistent preferences and system reduced motion.
- **Do** pair feedback with words and preserve learning evidence boundaries.

### Don't:
- **Don't** reintroduce wide squat faces, exaggerated stomping, or answer-bearing mascot props.
- **Don't** add gradients, glass, glow, confetti, streak pressure, stock imagery, or Orientalist decoration.
- **Don't** add pills except toggle chips or italic headings.
- **Don't** turn the gallery composition into a lesson layout.
- **Don't** claim a score or animation capability the implementation does not support.


## Beginner path map and Sayo (added)

- **Path map** (`src/PathMap.tsx`): units are rounded banners in `accent-wash` with the unit's characters; lessons are 80px stepping stones on a gentle S-curve (`--swing` 46px desktop, 14px phone; rows narrow so the curve never clips). States: open (sheet + ring + 6px "ledge" shadow that presses down on tap), next (accent fill, Sayo with a "Start here!" bubble), done (good wash + check badge). Nothing is locked.
- **Journey**: ten plain-language stages ("Hello and numbers" → "Lifelong Chinese"); cards on desktop, a compact timeline on phones; "You are here" marked with Sayo.
- **Sayo assets**: poses are served from `public/mascot/web/*.webp` (480px, trimmed to one shared frame so poses don't jump; ~30 KB each). The original PNGs stay in `public/mascot/quiet/` for the gallery download.
- **Pinyin**: every new character and new phrase shows tone-coloured pinyin and a "Say it" button; quizzes still start without pinyin (revealing it marks the answer as supported).


## Sayo 小夜: persona, reactions, levels (added)

- **Name and persona:** Sayo (小夜, “the night”), a cool, exacting study mentor. She is brief, never gushes and never shames. Every line is real Mandarin shown as Chinese, then tone-coloured pinyin, then English (`MoSays` in `src/Mascot.tsx`), so her reactions are learnable phrases. The bubble text stays readable even when the artwork is hidden in Settings.
- **Reaction map:**
  - correct and unaided: 太棒了 / 对了 / 很好 / 漂亮, and occasionally a smug 不错嘛 (her top praise);
  - correct with a hint: 下次不看提示;
  - wrong: 再来 / 差一点 / 没关系，再试试;
  - missed tone: grumpy 声调呢？
  - Lines are picked deterministically per exercise, so they never flicker.
- **Placement:** after checking an answer, Sayo rises beside the verdict bar. On screens ≥1200px she sits in the empty right margin with the bubble above her. Below that she sits bottom-left, and the exercise gets extra bottom padding so answers can scroll clear.
- **Levels** (`src/progression.ts`): level = 1 + lessons finished at least once. Quick checks and readings don't count. A first finish shows the level-up screen: thumbs-up pose, 升级了！, a level badge, then "Now you can …" with the lesson's mission and the new characters. Never points.
- **Days in a row:** consecutive local days with any study. Shown quietly on Today and the level-up screen, with a Settings switch. It never blocks or punishes.
- **Art status:** all sixteen states have their own artwork, including the approved thumbs-up and running poses. No pending placeholders remain. Conversion: `python scripts/prepare-mascot.py`.
- CSS uses neutral `mascot-*` and `mo-*` class names; the gallery lives at `#companion`.

## Optional cloud-sync controls

Settings adds Cloud sync within the existing Account column: a plain-language status, last successful sync time, Sync now and an explicitly confirmed Delete my cloud data action. A separate consent screen asks whether to add existing device progress before any upload. Declining keeps learning available. Confirmation, error, paused and offline states use existing controls and palette; no extra animation is introduced. File inputs and account names wrap within narrow screens. The new Kiyo logo concepts remain uninstalled by owner request.


## Night Study v2 (current; supersedes earlier colour notes) — `src/night.css`

Loaded last and owned by this section. Direction: a late-night studio (Oura's dusk screens × Sayo/Ado). Follows `../SHARED-SPEC.md`.

- **Base:** deep blue-black (`#0b1323`) with one soft moonlight glow top-right (accent at 13%) and a faint teal haze top-left. No flat grey anywhere.
- **Surfaces:** `--sheet #111a2b` / `--sheet-2 #172338`; rules are translucent blue (`rgb(148 170 214 / .14–.28)`); top bars are frosted glass (`--glass` + 14 px blur).
- **One luminous accent:** blue-rose `#86a8ff` on `#0a1430` text, with a soft glow under primary buttons. Success `#72d9b9`, error `#ff9a92`, used only on the verdict bar and the chosen answer. Tone colours: coral, amber, mint, blue, grey.
- **One coloured plane per screen:** the verdict bar is dark glass with a lit 2 px top edge in the state colour (it draws in left→right, 260 ms) and a faint wash. It never fills the whole bar with mud.
- **Labels:** uppercase eyebrows only for task type in lessons and the lead-lesson line. Stats labels, the dateline and table labels are sentence case.
- **Sayo (shared spec §4):** Today 200/140/96 px beside the greeting, bubble to her left, ≥ 24 px below the header. Lessons: one home (`.lesson-mo`) in the right gutter, 24 px from the column, feet 16 px above the verdict bar (tracks the bar's real height via `--verdict-h`). Idle pose without a bubble; after Check, her reaction pose + bubble (Chinese 20 / pinyin 14 / English 14 / "Hear Sayo"). At ≥ 1280 px she's fixed in the right gutter (132 px). Below 1280 px there's no gutter, so she joins the page flow after the task, right-aligned with her bubble to her left (96 px tablet, 64 px phone, where the bubble shows one line until tapped). After Check, the page scrolls just enough to show her reaction above the verdict bar, and the lesson's bottom padding follows `--verdict-h`, so she never covers an answer at any width (measured at 1440/1024/768/375). Never a folded-arms pose for a correct answer.
- **Disabled primary buttons:** full opacity, accent-wash fill, quiet ink-3 text, no glow (not a 0.38 fade).
- **Today:** lead tile with the 米字格 grid and a soft inner glow; 10–60 min pill selector (stacks under the heading on phones); plan rows end with a → that nudges 3 px on hover; stats: Milestone · Level · Days in a row · Review · Characters, as plain text (no badges, no mini mascots).
- **hanzi-writer colours must be hex/rgb() without alpha** (`--writer-outline`); the library silently fails on `rgb(… / a)`.
