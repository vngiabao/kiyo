# Sayo: three new poses (design stays exactly the same)

These poses complete Sayo's reactions in the app (`src/sayo-director.ts`): she peeks when you reveal pinyin, she stamps your finished lessons, and she leans in while you type. **Her design does not change.** Only pose, hands, head angle and expression.

The pale-blue edge around her is added by the app. **Don't ask for an outline or glow.**

## How to run it

1. Open a **new ChatGPT chat** (image generation on).
2. Attach these 4 files from `public/mascot/quiet/` as the reference: `welcome.png`, `hint.png`, `think.png`, `rest.png`.
3. Paste **Prompt 0**. Wait for the 5-bullet confirmation.
4. Paste Prompts 1–3 **one at a time**. Check each against its "Check" line.
5. Save each with the file name given into `public/mascot/quiet/`, then tell Claude. Claude converts them (`python scripts/prepare-mascot.py`) and wires them in.

**If a result drifts**, reply:
> Too different from the reference. Keep the character EXACTLY as attached: same face, eyes, hair, top strand, coat, outfit, collar flower, colours, outline thickness, proportions and flat style. Change ONLY the pose and expression I described.

**If the eyebrows don't show**, reply:
> Draw her eyebrows as thin dark-navy strokes visible ON TOP of the bangs, so the eyebrow shape is clearly readable.

---

## Prompt 0: Design lock (send first, with the 4 images attached)

```
The 4 attached images are one character: Sayo, the mentor mascot of a Mandarin-learning app. I'm going to ask for 3 new poses of her, one at a time.

DESIGN LOCK (never change any of this)
- Face, eye shape, teal eye colour, small mouth, skin tone, blush style.
- Hair: same length, same deep-indigo colour, same shading, same bangs, same single curved strand on top (it may bend with her mood, but keep its shape and size).
- Outfit: the same long black coat, the same dark outfit underneath, the same teal collar flower and ribbon, same shoes. Same coat length in every image.
- Style: same flat colours, same dark-navy outline thickness, same soft cel shading, no gradients, no textures, no glow, no outer outline or sticker border.
- Proportions: same small chibi body, same head-to-body ratio.

CANVAS (every image)
- Square 1254 × 1254 px, transparent background, no shadow, no text, no letters, no symbols, no sparkles, no background objects.
- Full body visible, same size and position in frame as the references: head near the top, feet near the bottom, body centred. Nothing cropped (hair, hands and any prop included).

WHAT CHANGES
- Only her pose, hands, head angle, facial expression, and one small prop where I ask for it.
- EYEBROWS: always thin dark-navy strokes visible on top of her bangs. The brows do the acting.

PERSONALITY
- A cool, exacting sensei: composed, dry, quietly proud of the learner. Never bubbly, never angry, never mocking.

Reply with 5 bullets confirming what must stay the same and what may change. Don't draw yet.
```

---

## Prompt 1 → `peek.png` (you reveal pinyin; she "didn't see that")

```
Using the locked design: standing, both hands raised to cover her eyes, palms toward her face, fingers slightly spread so ONE teal eye peeks through a gap between two fingers. Head tilted a little down and to one side. Eyebrows raised just above her fingers, a tiny knowing smile. The top hair strand curls up playfully. Mood: "I'm not looking... okay, I'm looking a little." Dry and teasing, not shy or scared.
```
Check: at thumbnail size, can you see both hands over her face AND one eye peeking through?

## Prompt 2 → `stamp.png` (she stamps your finished lesson)

```
Using the locked design: standing three-quarter view, holding a small square Chinese seal (a stone seal stamp, about the size of her fist) in one hand, mid-motion, pressing it down onto an invisible surface at waist height in front of her. Her other hand rests on her hip. The seal is plain pale-blue stone with a simple carved top; its stamping face points DOWN and AWAY, so no carving or characters are visible. Eyebrows level and confident, a small satisfied smile, eyes half-closed. The top hair strand bounces up with the motion. Mood: "Approved." Composed pride, like a teacher signing off good work.
```
Check: the seal is clearly a stamp, its face is NOT visible (no characters or symbols anywhere), and it's pale blue, not red or gold.

## Prompt 3 → `watch.png` (she watches you type an answer)

```
Using the locked design: leaning forward from the waist toward the viewer, as if looking down at something just below the frame (a page or a phone screen), hands clasped behind her back. Head tilted slightly, eyes looking down and focused, eyebrows gently raised with interest, mouth a small neutral line. The top hair strand leans forward with her. Keep her feet in place so the full body still fits the frame. Mood: "Go on, I'm watching. Take your time." Attentive and patient, not impatient.
```
Check: does it read as "leaning in to watch" rather than bowing or falling? Is her whole body inside the frame?

---

## After the images are in

Claude will:
- convert them to `public/mascot/web/*.webp` with `scripts/prepare-mascot.py`;
- add `peek`, `stamp` and `watch` as Sayo states, each with a short idle animation;
- switch the cues: reveal pinyin → `peek` (instead of `rest`), typing an answer → `watch` (instead of `think`), finishing a lesson → `stamp` with the seal landing on screen;
- add them to the gallery at `/#companion`.
