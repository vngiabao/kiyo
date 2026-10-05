# Mascot prompts: 小夜 Sayo, the cool sensei

> **Status:** the app keeps the current Sayo art for now. This file is for a possible future full redesign. To fill the two missing poses in the current style, use `prompts/sayo-pose-revisions.md`.

Paste these into ChatGPT one at a time, in order, in the **same chat** so the character stays consistent. Paste **Prompt 0** first, then every later prompt starts with "Using the Sayo model sheet above…".

> **About "vector":** ChatGPT's image generator makes raster images (PNG), not true vector files. The prompts ask for a flat, vector-ready style (clean closed shapes, flat fills, uniform lines) so the art converts cleanly afterwards. Convert with Adobe Illustrator → Image Trace (6–12 colours, "Ignore white" on), or vectorizer.ai. For a real animation rig, give the traced SVGs and the layer list in Prompt 5 to an illustrator or animator (Rive or Lottie).

---

## Prompt 0: Character bible (send first, no image yet)

```
You are the lead character designer for "Kiyo 清", a premium Mandarin-learning app. I'll ask you for several images of one ORIGINAL mascot. Read this whole bible, confirm you understand it in 5 bullet points, and wait. Don't draw anything yet.

CHARACTER: 小夜 Sayo (Japanese: sayo, "the night"; read Xiǎoyè in Mandarin)
ROLE: a cool sensei. A sharp, stylish mentor who keeps the learner disciplined through hard vocabulary, tones and sentence structure. Not a cheerleader. Not cute-bubbly. Her approval is rare and small, so it means something.

ORIGINALITY (hard rules)
- Sayo is an original character. Her vibe is a nocturnal, late-night-studio cool: think a mysterious singer's stage persona, but she is NOT based on any real singer. She must not resemble any real person, singer, VTuber, idol, or existing anime/game character, nor any existing official avatar or album art.
- No blue rose. No gloves. No military cap. No eyepatch. No headset microphone on her face. No visible brand logos.
- No text, letters or Chinese characters anywhere in the artwork (she appears next to quiz answers, so props must never show readable writing).

AGE & PROPORTIONS
- She is a young adult (early 20s). Chibi stylisation only: about 2.5 heads tall, slender limbs, small face, adult bearing. Never childlike or sexualised.
- Posture: upright, composed, weight on one leg, shoulders relaxed.

HAIR (her silhouette signature)
- Very long, straight, floor-skimming hair in deep indigo-navy (#1E2A5A) with a cooler bright-blue underlayer (#3D5BA9) visible on the inside and tips. Two-tone, sleek, few large clumps, sharp tapered ends.
- Straight bangs cut slightly uneven, with ONE longer strand falling between the eyes.
- ONE ahoge (top strand) shaped like a single calligraphy brushstroke: thick at the root, sweeping in an S-curve, tapering to a sharp point. It reacts to her mood (droops, perks up, flicks).

FACE
- Eyes: teal-cyan iris (#3FB6B2) with a darker teal ring (#1F7F7C), one small white highlight, heavy half-lidded upper lid line. Default look: calm, assessing, unimpressed.
- Thin, straight, expressive eyebrows do most of the acting.
- Tiny mouth; default is a flat line or a faint one-sided smirk.
- Subtle pale-blue blush marks only in the "celebrate" and "level up" poses.

SIGNATURE PROP: HEADPHONES (the app is about listening and voice)
- Matte black over-ear headphones (#14161C) with a thin pale-blue ring light on each ear cup (#B3D2F5).
- Default: worn around her neck. In "listen" she wears them on her ears; in "level up" the ring lights glow.

OUTFIT: modern Tang-suit tailoring, minimal and sharp
- Black jacket (#16181F) with a mandarin stand collar, asymmetric diagonal front closure, three knotted frog buttons (盘扣) in pale blue (#B3D2F5), slim fit, hem to upper thigh, slightly flared sleeves with clean cuffs.
- One small blue peony pin on the left collar: pale-blue petals (#B3D2F5 / #8FB6E6), teal centre (#3FB6B2).
- Slim charcoal trousers (#23262F), black ankle boots (#101217) with a thin pale-blue sole edge.
- Optional prop: a slim black brush pen she uses as a pointer (never shows writing).

STYLE (vector-ready)
- Flat vector illustration. Clean closed shapes, flat fills, ONE cel-shade tone per colour (10–15% darker), no gradients, no textures, no glow except the headphone rings, no soft airbrushing.
- Uniform outline in deep navy (#0B1424), about 1.2% of image width, rounded joins. Inner detail lines slightly thinner.
- Limited palette: only the colours above plus skin #F6E3D6, skin shade #E7C7B5, white #FFFFFF, outline #0B1424.
- Transparent background. No floor shadow. Full body visible, centred, head top at about 6% from the top and feet at about 96%, in a square canvas.
- She must read clearly both at 1024 px and shrunk to 40 px: strong silhouette (hair mass + ahoge + headphones).

PERSONALITY → BODY LANGUAGE
- Cool, exacting, dry humour, quietly proud of the learner. Never mocks, never insults, never sarcastic about ability.
- Signature gestures: arms crossed; one hand on hip; pointing the brush pen; pushing hair back; a single slow blink; adjusting the headphones.
- Praise scale: a small nod → a faint smirk → (rarely) a thumbs-up with a wink.
```

---

## Prompt 1: Model sheet (front, 3/4, back)

```
Using the Sayo bible above, create a CHARACTER MODEL SHEET on a transparent background: three full-body views of Sayo side by side (front, three-quarter, back), same scale, standing neutral with arms relaxed and headphones around her neck. Under each view leave empty space (no text). Flat vector style, uniform navy outlines, flat fills, one cel-shade tone, no gradients, no text. This sheet is the single source of truth for all later images, so keep it clean, symmetric and precise.
```

## Prompt 2: Expression sheet

```
Using the Sayo model sheet above, draw an EXPRESSION SHEET: 12 head-and-shoulders busts of Sayo in a 4×3 grid, same scale, transparent background, no text. Expressions, in order:
1 neutral assessing (half-lidded), 2 faint smirk, 3 slow blink (eyes closed, calm), 4 one eyebrow raised (sceptical), 5 unamused flat stare with a tiny pout, 6 small approving nod (eyes softly closed, slight smile), 7 focused listening (eyes closed, headphones ON), 8 speaking/prompting (mouth open, eyebrows up), 9 thinking (eyes up-left), 10 rare proud smile with pale-blue blush, 11 wink, 12 deadpan surprise (eyes slightly wide, mouth small "o").
The ahoge must change with each mood (droop, perk, flick). Keep hair, headphones, collar and peony identical across all 12.
```

## Prompts 3a–3d: The 16 app poses (4 per image)

Ask for each set as a separate image. Each pose is full body, in its own square cell, transparent background, same framing (head at 6%, feet at 96%), no text.

```
3a — Using the Sayo model sheet, draw 4 full-body poses in a 2×2 grid, each in an equal square cell, transparent background, identical scale and framing, no text:
• WELCOME: one hand raised in a small, cool wave at chest height; faint smirk; weight on one leg.
• LISTEN: headphones ON her ears, eyes closed, one hand pressing an ear cup; ring lights softly lit.
• SPEAK: brush pen held up like a conductor's baton, mouth open mid-word, eyebrows lifted, prompting the viewer to repeat.
• READ: a closed dark book under one arm, other hand on hip, looking straight at the viewer, assessing.
```

```
3b — Same rules, 4 poses:
• WRITE: brush pen poised over an open notebook whose pages are completely blank (no marks, no letters); focused eyes.
• THINK: finger to chin, eyes up-left, ahoge curled into a question-mark shape.
• HINT: one finger raised, one eyebrow up, slight lean forward: "here's a clue, don't get used to it".
• CELEBRATE: both fists at chest height, small hop with one foot lifted, eyes closed in a rare happy smile, pale-blue blush, hair swinging.
```

```
3c — Same rules, 4 poses:
• NOT BAD (her top praise): arms crossed, side glance at the viewer, small one-sided smirk, ahoge perked.
• AGAIN (after a mistake): calm open palm toward the viewer, patient half-lidded look: firm but kind, NOT angry.
• THE TONE? (missed tone): flat unamused stare, tiny pout, one hand on hip, ahoge drooped sideways.
• REMEMBER (review due): holding up a small blank flashcard between two fingers, one eyebrow raised.
```

```
3d — Same rules, 4 poses:
• REST: sitting cross-legged on the floor, holding a small teacup with both hands, eyes closed, serene; headphones around her neck.
• RECONNECT (error/offline): holding an unplugged headphone cable up, deadpan stare at the viewer, ahoge drooped.
• LEVEL UP: confident thumbs-up toward the viewer, wink, headphones' pale-blue rings glowing brightly, peony prominent, hair lifted slightly as if by a breeze.
• KEEP GOING (daily streak): mid-stride running pose, jacket hem and hair flowing behind, determined eyes, brush pen in hand.
```

## Prompt 4: Clean single exports (repeat per pose)

```
Using the Sayo model sheet, redraw ONLY the "[POSE NAME]" pose as a single full-body image on a 1024×1024 transparent canvas. Head top at 6% from the top edge, feet at 96%, body centred. Flat vector style, uniform navy outline, flat fills + one cel-shade tone, no gradients, no text, no shadow, no background.
```

File names the app expects, after conversion (drop the PNGs into `public/mascot/quiet/`, then run `python scripts/prepare-mascot.py`):
`welcome, listen, speak, read, write, think, hint, celebrate, smug, encourage, grumpy, review, rest, error, thumbsup, run`

## Prompt 5: Animation rig spec (for an animator, or ask ChatGPT for a layer breakdown)

```
Using the Sayo model sheet, produce a LAYER BREAKDOWN sheet for rigging her in Rive/Lottie: show each body part separated and labelled with a number (no words inside the art; put the legend as a list in your text reply). Parts: back hair mass, front hair/bangs, between-eyes strand, ahoge, head, ears, eye whites, irises, upper eyelids, lower lids, eyebrows (L/R), mouth set (closed line, smirk, small o, open "ah", smile), neck, headphones (band + each cup + ring lights), torso/jacket, collar, peony pin, frog buttons, upper arms, forearms, hands (open, fist, point, thumbs-up, holding pen), brush pen, legs, boots. Extend hidden areas under overlaps so parts can rotate without gaps. Flat vector style, transparent background.
```

Motion behaviour to give the animator (subtle, premium, never distracting):

| Moment | Motion | Timing |
|---|---|---|
| Idle | breathing scale 1–1.5%, hair tips sway, ahoge micro-bob | 4 s loop, ease-in-out |
| Blink | single blink; occasional double | random every 3–6 s |
| Audio playing | headphone ring lights pulse with the audio; head tilts 2° | while playing |
| Correct | small nod + smirk | 300 ms, ease-out |
| Correct, unaided streak | pushes hair back + "not bad" smirk | 600 ms |
| Wrong | slow blink, open palm rises | 400 ms, no shake, no red |
| Missed tone | one eyebrow up, ahoge droops | 350 ms |
| Level up | thumbs-up + wink, rings glow, hair lifts | 700 ms, one small hop |
| Reduced motion | swap static poses only, no movement | — |

Rules: transform and opacity only; never loop a reaction; never animate while the learner is answering; nothing louder than the lesson.

## Persona: how Sayo talks (already the model for the app's lines)

- **Brief.** Two to six Chinese characters, then pinyin, then a short English line.
- **Exacting, never cruel.** Corrects the thing, never the person. No sarcasm about ability.
- **Rare praise.** Ladder: 对了 → 很好 → 不错嘛 (top) → 太棒了 (level-ups only).
- **Disciplined.** 再来 ("Again"), 声调呢？ ("The tone?"), 下次不看提示 ("Next time, no hints").
- **Dry humour.** 又断了 ("Cut off again", for offline), 今天够了 ("Enough for today").
- **Never says:** "Yay!", "Amazing job!!", emoji, exclamation strings, guilt trips about streaks.
