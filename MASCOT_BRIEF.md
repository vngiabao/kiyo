> The full character spec and ready-to-paste generation prompts are in `prompts/mascot-prompt.md` (two-tone indigo hair, brushstroke ahoge, black headphones with pale-blue ring lights, Tang-style jacket, blue peony). Where this brief differs, the prompt file wins.

> **Status:** the current Sayo art is kept for now. Only `thumbsup` and `run` are missing; see `prompts/sayo-pose-revisions.md`. The redesign below is for a later, commissioned version.

# Illustrator brief: 小夜 Sayo, Tingjian's study mentor

**Purpose:** commission an original character to replace the current placeholder artwork. The placeholders were AI-generated and resemble a real performer. The commissioned design must be clearly original, must not depict or evoke any real person, and must not reuse any existing character, costume or promotional artwork (music labels, streaming services, film or anime characters).

**Deliverable rights:** full commercial rights assigned to the product owner, including app stores, marketing and merchandise; or a written exclusive licence. Ask for source files.

## Who she is

- **Name:** 小夜 Sayo ("the night"; Xiǎoyè in Mandarin). Do not use any other name in files, metadata or sketches.
- **Role:** a cool, exacting study mentor. Calm, dry, a little deadpan, quietly proud of you. She is never bubbly and never mocking.
- **Voice in the app:** short Mandarin lines, such as 来了？开始吧。 ("You're here? Let's begin.") and 不错嘛。 ("Not bad at all.").
- **Audience:** adults and older kids learning Chinese from zero. She has to read clearly at 36px and at 380px.

## Design direction

| Element | Direction |
|---|---|
| Proportions | Chibi, about 2.5 heads tall, slender, small face. |
| Hair | Deep indigo, long. The single top strand (ahoge) should read as **one cursive brushstroke**: a calligraphic sweep with a thick start and a tapered end. |
| Outfit | Modern, sleek black **Tang-suit jacket (唐装)**: mandarin collar and frog buttons (盘扣), clean tailoring, no gold. Dark trousers or skirt, simple shoes. |
| Accessory | A small **blue peony (牡丹)** at the collar, matching the app's pale blue (#b3d2f5) and teal (#9bcdbc). No rose. |
| Eyes | Teal, half-lidded by default. Expressions come from brows and mouth, not big sparkles. |
| Line | Uniform dark navy outline (≈ #0b1424), flat colour with at most one soft shade tone. No gradients, glow or texture. |
| Background | Transparent. No ground shadow; the app sits her on dark navy (#101b2b) and on the lighter panel colour (#17263a). Check contrast on both. |
| Avoid | Dragons, lanterns, fake calligraphy text, red-and-gold, fans, anything stereotyped. Chinese culture comes through the tailoring and the peony only. Props must never show readable Chinese characters, because she appears next to quiz questions. |

## Technical spec

- **Canvas:** 2048 × 2048 px PNG, transparent.
- **Framing:** the **same frame for every pose**. Head top at about 6% from the top edge, feet at about 96%, body centred horizontally. Poses must not jump in size when the app swaps them.
- **Sources:** layered PSD, Procreate or Krita file, plus SVG or vector if drawn in vector.
- **Handover:** drop the PNGs into `public/mascot/quiet/` and run `python scripts/prepare-mascot.py`, which outputs 480 px WebP files to `public/mascot/web/<id>.webp`. Keep the file names below exactly.

## The 16 poses

| id | Pose and expression | App moment | Her line |
|---|---|---|---|
| `welcome` | Small, cool wave at chest height; slight smile | Today, start of study | 来了？开始吧。 |
| `listen` | Hand cupped to ear, eyes closed | Listening, audio playing | 再听一遍。 |
| `speak` | Hand near mouth as if prompting; mouth open | Speaking practice | 大声说。 |
| `read` | Holding a closed book under one arm, looking forward | New character, readings | 看清楚。 |
| `write` | Brush or pen raised over a blank notebook (no characters) | Optional tracing | 一笔一笔来。 |
| `think` | Finger to chin, eyes up-left | Recall, loading | 想一想。 |
| `hint` | One finger raised, one eyebrow up | Correct, but with a hint | 下次不看提示。 |
| `celebrate` | Both fists up, small hop, closed-eye smile | Correct answer | 太棒了！ |
| `smug` | Arms crossed, side-eye, tiny smirk (her top praise) | Correct, unaided | 不错嘛。 |
| `encourage` | Calm open palm toward viewer, gentle look | Wrong answer | 再来。 |
| `grumpy` | Unamused flat stare, slight pout, arms crossed | Missed tone | 声调呢？ |
| `review` | Holding a card up, eyebrow raised | Reviews due | 还记得吗？ |
| `rest` | Sitting, sipping tea, eyes closed | Nothing due | 今天够了。 |
| `error` | Holding an unplugged cable, deadpan | Errors, offline | 又断了。 |
| **`thumbsup`** *(new)* | Confident thumbs-up, wink, peony prominent | **Level up** (first finish of a lesson) | 升级了！ |
| **`run`** *(new)* | Mid-stride run, jacket flaring, determined | **Days in a row** | 天天来。 |

`thumbsup` and `run` currently show placeholders (`celebrate` and `review`). When their files arrive, remove `pending` and `fallback` from those two entries in `src/Mascot.tsx`.

## Review checklist before accepting

- [ ] Reads clearly at 36 px (silhouette, hair strand, peony).
- [ ] No resemblance to a real person or to any existing character or campaign.
- [ ] All 16 poses share one frame, line weight and palette.
- [ ] No readable text on any prop.
- [ ] Rights assignment signed; source files delivered.
