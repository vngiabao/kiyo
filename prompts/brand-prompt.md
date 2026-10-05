# Brand prompts: Kiyo 清 (logo, icon, brand system)

Logos and icons are simple enough for ChatGPT to write as **real SVG code** (true vector). These prompts ask for SVG code blocks, not images. Paste the SVG into a `.svg` file, or open it in Figma or Illustrator to check and refine it. Send the prompts in order, in one chat.

---

## Prompt A: Brand brief (send first)

```
You are a senior brand designer and SVG engineer. We're building the brand for "Kiyo 清", a premium Mandarin-learning app. Read this brief, reply with 5 bullet points confirming the direction, and wait.

NAME
- Kiyo (Japanese きよ, "clear, pure") written with 清, the same character read qīng in Mandarin ("clear"). Two syllables, stage-name-like, the way a singer's mononym is: cool, sharp, clean. Clear listening, clear tones, clear speech.
- Lockups: "KIYO" wordmark, the 清 mark, and the combination "清 KIYO".
- Tagline: "Mandarin, crystal clear."

PERSONALITY
- Cool, nocturnal, precise, a little rebellious, premium. Japanese street-poster sharpness meets editorial restraint. Think late-night studio, not classroom.
- Avoid: cute bubbly mascots in the logo, red-and-gold, dragons, lanterns, brush-calligraphy clichés, rainbow gradients, generic "speech bubble" or "graduation cap" icons, AI sparkles.

MASCOT CONTEXT (not in the logo)
- The app's mentor is Sayo 小夜 ("the night"), a cool sensei with deep-indigo hair, black Tang-suit jacket, pale-blue frog buttons and black headphones with pale-blue ring lights. The logo should feel like it belongs in her world, not depict her.

COLOUR SYSTEM (use these exact hex values)
- Midnight #101B2B (primary background), Night #17263A (raised surface), Deep #0B1424 (deepest/outline)
- Ink White #F0F3F5 (primary foreground), Mist #C7D3DF (secondary)
- Signal Blue #B3D2F5 (THE accent; use sparingly, one element per mark)
- Teal #9BCDBC (success only), Peach #F2B29E (errors only)

THE CORE IDEA (keep this)
- In pinyin, qīng carries a FLAT TONE MARK (ˉ) over the i. The top horizontal stroke of 青 (the right side of 清) is also flat. In the mark, that top stroke is lit in Signal Blue, so one shape is both part of the character and the tone mark. Everything else is Ink White.

CONSTRUCTION RULES
- The 清 must be CONSTRUCTED from geometric shapes (rectangles, rounded-end bars, simple bezier sweeps), not typed from a font, and must not copy any existing typeface's glyph. It must still be correctly written and instantly readable as 清 (11 strokes: left radical 氵 = dot, dot, rising flick; right side 青 = top horizontal, second horizontal, vertical through them, longer third horizontal, then 月 below = left vertical-sweep, right hook frame, two short inner horizontals).
- The three dots of 氵 may be drawn as sharp teardrop/wedge shapes, like water drops: the one organic detail. Keep them clearly separate.
- Stroke style: modern, slightly condensed, flat terminals with a subtle 15° angled cut on the rising flick of 氵 (one sharp "edge" detail: the attitude).
- Optical balance on a 1024 grid, 8 px subgrid, consistent stroke weight (~92 px at 1024).
```

## Prompt B: The mark + app icons (SVG code)

```
Now output SVG CODE (not an image) for each item below, each in its own ```svg code block. Requirements for every SVG: valid standalone SVG 1.1, explicit viewBox, NO <text> elements, NO external fonts, NO raster images, NO filters, all shapes as <path>/<rect>, fills from the brand palette only, no strokes on the glyph (use filled paths), paths rounded to 1 decimal, readable id names.

1. mark.svg: viewBox 0 0 1024 1024, transparent background, the constructed 清 in Ink White with the top horizontal stroke in Signal Blue. Glyph occupies the central 70% (live area 154–870).
2. app-icon-ios.svg: 1024×1024 full-bleed square (no rounded corners; iOS masks it), Midnight #101B2B background with a very subtle 4% lighter radial lift behind the glyph (a single flat circle at 6% opacity of #B3D2F5 is acceptable instead of a gradient), mark centred at 62% of icon size.
3. app-icon-android-foreground.svg: 432×432 viewBox, transparent, mark centred inside the 288×288 safe zone (66% rule) for adaptive icons.
4. app-icon-android-background.svg: 432×432 flat Midnight.
5. app-icon-maskable.svg: 512×512, Midnight background, mark within the central 80% safe circle.
6. app-icon-monochrome.svg: 432×432, single-colour #000000 glyph only (Android themed icons); the tone bar stays part of the glyph.
7. favicon.svg: 32×32 viewBox, SIMPLIFIED for tiny sizes: thicker strokes (≥3 px), fewer details, Midnight rounded square (rx 7) with the glyph in Ink White and the top bar in Signal Blue; must stay legible at 16 px.
8. splash.svg: 1290×2796 (iPhone portrait), Midnight background, mark at 28% width centred, wordmark below (from Prompt C) at 18% width.

After the code, list: the stroke weights used, the live-area box, and how you ensured the 清 is correctly written.
```

## Prompt C: Wordmark + lockups (SVG code)

```
Now design the KIYO wordmark and lockups, again as SVG CODE in separate ```svg blocks, same technical rules (no <text>, outlined paths only).

WORDMARK "KIYO"
- Custom geometric capitals drawn as paths (not a font). Wide tracking (≈ +16%), slightly extended, heavy-but-not-black weight (similar optical weight to the 清 mark).
- Signature detail: a short Signal Blue bar floating above the I, echoing the flat tone mark in qīng (and the blue stroke in the 清 mark).
- K with a sharp, clean diagonal junction; Y with arms meeting exactly at x-height middle; O a perfect circle with a thin horizontal cut through its centre line, like a soundwave or a closed eye.
- Colour: Ink White on dark, Midnight on light. The only accent is the bar over the I.

Deliver:
1. wordmark-dark.svg: KIYO in Ink White, transparent bg, viewBox tightly fitted with 8% padding.
2. wordmark-light.svg: KIYO in Midnight.
3. lockup-horizontal.svg: mark (on a Night #17263A rounded tile, rx = 22% of tile) + 32 px gap + wordmark, vertically centred.
4. lockup-stacked.svg: mark above wordmark, centred, wordmark width = 1.4 × mark width.
5. lockup-with-tagline.svg: horizontal lockup + tagline "Find your voice in Mandarin." BUT since text elements are forbidden, leave a clearly marked empty rectangle (id="tagline-slot", no fill, 1 px Mist stroke) where the tagline will be typeset by the developer in the app font (Newsreader 500).

Then give the clear-space rule (minimum = height of the tone bar × 2) and minimum sizes (mark 16 px, wordmark 64 px wide).
```

## Prompt D: Brand system sheet (one image, for reference)

```
Now create ONE presentation image (not code) of the full brand system on a Midnight background, flat vector style: the app icon at large size and at small iPhone home-screen size, the favicon at 16 px and 32 px, the mark on Midnight and on Ink White, the horizontal and stacked lockups, the colour palette as six flat swatches with their roles, and a sample phone screen (dark UI) showing the icon on a home screen. Keep it minimal, editorial, generous spacing, no mock device chrome beyond a simple phone outline, no extra slogans, no lorem ipsum.
```

## Prompt E: UI icon set (optional, SVG code)

```
Design a 12-icon UI set for the app as SVG code, one ```svg block each, 24×24 viewBox, 1.75 px stroke, round caps and joins, stroke="currentColor", fill="none", no text, consistent optical size, slightly sharp personality matching the KIYO wordmark (one angled cut per icon where natural):
today (sunrise over line), read (open book), listen (headphones), speak (sound waves from a mouth arc), practice (target), media (play in a rounded rectangle), progress (stepped bars), review (circular arrow with a dot), dictionary (magnifier), settings (gear with 6 teeth), streak (running figure simplified to 4 strokes), level (shield with a flat bar on top, echoing the tone mark).
```

---

### Before you ship

- **Trademark search** "Kiyo" (and "Kiyo 清", "Sayo") in the US (USPTO) and Vietnam (IP Viet Nam), software and education classes. Both are common Japanese words and names, so expect existing marks; ask your lawyer whether a distinguishing form like "Kiyo Mandarin" is needed.
- **Check SVGs:** run ChatGPT's SVGs through a validator (open them in a browser), then tidy them in Figma. AI-written paths often need small optical fixes.
- **Install in the app:** send me the final SVGs and I'll update `public/icon.svg`, the manifest icons and `src/brand.tsx` (the app already uses Kiyo 清 with a stroke-data placeholder logo).
