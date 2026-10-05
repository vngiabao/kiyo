# Sayo: pose revisions (design stays exactly the same)

**Goal:** make each mood instantly readable at small sizes, add visible eyebrows, and draw the two missing poses. **Her design does not change:** same face, eyes, hair, top strand, coat, outfit, collar flower, colours, outline, proportions and style. Only the pose, hands, head angle and expression change.

The pale-blue edge around her is added by the app in code. **Don't ask ChatGPT for an outline or glow.**

---

## How to run it

1. Open a **new ChatGPT chat**.
2. Attach these 4 current files from `public/mascot/quiet/` as the reference: `welcome.png`, `celebrate.png`, `smug.png`, `rest.png`.
3. Paste **Prompt 0** (the design lock). Wait for the 5-bullet confirmation.
4. Paste the pose prompts **one at a time** (Prompts 1–11). After each image, check it against the "check" line.
5. Save each result **with the file name given** and put it in `public/mascot/quiet/`, replacing the old file. Keep a copy of the old ones in case you prefer them.
6. Tell me when they're in. I'll convert them and switch the app over.

**If a result drifts**, reply with:
> Too different from the reference. Keep the character EXACTLY as attached: same face, eyes, hair, top strand, coat, outfit, collar flower, colours, outline thickness, proportions and flat style. Change ONLY the pose and expression I described.

**If the eyebrows don't show**, reply with:
> Draw her eyebrows as thin dark-navy strokes visible ON TOP of the bangs (or through a small gap in the hair), so the eyebrow shape is clearly readable.

---

## Prompt 0: Design lock (send first, with the 4 images attached)

```
The 4 attached images are one character: Sayo, the mentor mascot of a Mandarin-learning app. I'm going to ask for new poses of her, one at a time.

DESIGN LOCK (never change any of this)
- Face, eye shape, teal eye colour, small mouth, skin tone, blush style.
- Hair: same length, same deep-indigo colour, same shading, same bangs, same single curved strand on top (it may bend with her mood, but keep its shape and size).
- Outfit: the same long black coat, the same dark outfit underneath, the same teal collar flower/ribbon, same shoes. Same coat length in every image.
- Style: same flat colours, same dark-navy outline thickness, same soft cel shading, no gradients, no textures, no glow, no outer outline or sticker border.
- Proportions: same small chibi body, same head-to-body ratio.

CANVAS (every image)
- Square 1254 × 1254 px, transparent background, no shadow, no text, no letters, no symbols, no sparkles, no background objects.
- Full body visible, same size and position in frame as the references: head near the top, feet near the bottom, body centred. Nothing cropped (hair and hands included).

WHAT CHANGES
- Only her pose, hands, head angle and facial expression.
- EYEBROWS: from now on, always draw her eyebrows as thin dark-navy strokes visible on top of her bangs, so her expression reads clearly. The brows do the acting: raised, flat or furrowed.

PERSONALITY
- A cool, exacting sensei: composed, dry, quietly proud of the learner. Never bubbly, never angry, never mocking.

Reply with 5 bullets confirming what must stay the same and what may change. Don't draw yet.
```

---

## Moods that need clearer poses

**Prompt 1 → `grumpy.png`** ("声调呢？", a missed tone)
```
Using the locked design: arms crossed firmly over her chest, head turned slightly away (about 20°) while her eyes stay on the viewer, flat unamused mouth with a tiny pout, eyebrows flat and slightly lowered, the top hair strand drooping to one side. Weight on one leg. Mood: "Really? The tone?", unimpressed but not angry.
```
Check: can you tell it's "unamused" at thumbnail size, without the text?

**Prompt 2 → `encourage.png`** ("再来。", after a wrong answer)
```
Using the locked design: one open palm extended gently toward the viewer at chest height (a calm "again" gesture), the other hand relaxed at her side, head tilted slightly, eyes softer than usual (a little less half-lidded), eyebrows slightly raised in the middle (patient), mouth a calm flat line. Mood: firm but kind, "Again. You can do it."
```
Check: kind, not disappointed or sad.

**Prompt 3 → `hint.png`** ("下次不看提示。", a hint was used)
```
Using the locked design: one index finger raised beside her face, leaning slightly forward from the waist, ONE eyebrow clearly raised and the other flat, a faint knowing half-smile. Mood: "Here's a clue, don't get used to it."
```
Check: the single raised eyebrow is obvious.

**Prompt 4 → `review.png`** ("还记得吗？", reviews are due)
```
Using the locked design: holding up a small blank white card between two fingers beside her face (card completely blank, no marks), one eyebrow raised, looking straight at the viewer, slight head tilt toward the card. Mood: "Still remember this?"
```
Check: the card is blank and clearly beside her face.

**Prompt 5 → `think.png`** ("想一想。", recall or loading)
```
Using the locked design: head tilted to one side, eyes looking up and to the side, one finger resting on her chin, the other arm crossed under it supporting the elbow, eyebrows slightly drawn together in concentration, mouth small and closed. The top hair strand curls a little more than usual.
```
Check: eyes clearly looking up and away, not at the viewer.

**Prompt 6 → `listen.png`** ("再听一遍。", listening)
```
Using the locked design: one hand clearly cupped BEHIND her ear (the cupped hand fully visible, not hidden by hair; tuck the hair behind that ear), head tilted toward that side, eyes closed, eyebrows relaxed, calm concentrated expression. The other hand relaxed at her side.
```
Check: the cupped hand behind the ear reads instantly.

**Prompt 7 → `welcome.png`** ("来了？开始吧。", Today screen)
```
Using the locked design: a clear, confident wave with her hand raised ABOVE shoulder height, palm open toward the viewer, fingers slightly spread; the other hand on her hip. Faint one-sided smile, one eyebrow slightly raised. Mood: "You're here? Let's begin."
```
Check: the waving hand is above the shoulder and clearly visible.

**Prompt 8 → `error.png`** ("又断了。", connection or audio error)
```
Using the locked design: holding up a black cable in one hand at face height, with its plug end clearly UNPLUGGED and dangling free below (the plug visible and separate, not attached to anything). Deadpan stare at the viewer, eyebrows flat, the top hair strand drooping. Mood: dry "Cut off again."
```
Check: the unplugged plug is obvious at small size.

## Missing poses

**Prompt 9 → `thumbsup.png`** ("升级了！", level up)
```
Using the locked design: a confident thumbs-up toward the viewer at chest height, a small wink (one eye closed), a faint proud one-sided smile, eyebrows relaxed and slightly raised. Weight on one leg, the other foot slightly forward, hair lifted a little as if by a light breeze. Mood: rare, composed approval.
```

**Prompt 10 → `run.png`** ("天天来。", days in a row)
```
Using the locked design: mid-stride running toward the viewer's right, one knee raised, arms bent and swinging naturally, long hair and coat hem flowing behind her, the top strand bent back by the wind. Determined calm expression, eyebrows slightly lowered, mouth a flat line. Keep the whole body and trailing hair inside the frame. No speed lines or dust.
```

## Consistency pass

**Prompt 11 (only if needed)**
```
Compare all the images you've made in this chat with the 4 original references. List any differences in the collar flower, coat length, hair colour, eye colour or outline thickness. Then redraw only the images that differ, fixing just those details.
```

---

## Not now: originality update before a public launch

When you're ready for a public or App Store launch, run this as a **separate** chat. It deliberately changes two design details: the collar rosette becomes a blue peony, and she gets her own signature item, black headphones. That moves her further from the real singer's avatar. **Skip it for now.**

```
Using the attached Sayo references, keep everything identical EXCEPT two details: (1) replace the teal collar ribbon/rosette with a small pale-blue peony pin with a teal centre; (2) add matte black over-ear headphones with a thin pale-blue ring on each ear cup, worn around her neck. Same pose as the reference, same canvas, same style, transparent background, no text.
```
