# Kiyo branding extension

Recorded 6 October 2026. This is a narrow extension of the incumbent Night Study interface, documenting the owner's selected asset roles. It does not establish a new visual world or revise the product/design specifications.

## Owner's asset roles

- **Website Welcome signature:** the owner selected `output/kiyo-review-v2/concept-a.png`, the existing lowercase Kiyo composition with Sayo leaning over the lettering. Its shipping copy is `public/brand/signature.png`. `BrandSignature` in `src/brand.tsx` displays it in `src/Welcome.tsx`; its intrinsic dimensions are 1774 × 887, and `src/night.css` gives it fluid width with proportional height. The component's accessible name is “Kiyo — Sayo leaning over the wordmark”.
- **Compact website wordmark:** the established uppercase SVG lettering remains in `Wordmark`, using `src/brand-paths.ts`. `public/brand/wordmark.svg` is its export. This is vector lettering, distinct from the raster Welcome signature.
- **Installed app tile:** reuse the existing waving Sayo pose at `public/mascot/web/welcome.webp`. `BrandMark` and `public/brand/app-icon.svg` frame this raster inside a pale-blue rounded square. In the SVG's 100 × 100 coordinate space, the corner radius is 23 and the embedded image is at x = −33, y = −3, width = height = 166. The tile background is `#b3d2f5`; these are asset-specific values, not a new global palette.
- **Small browser favicon:** retain the existing 清 stroke mark at `public/icon.svg`, referenced by `index.html`.

The app tile contains approved raster character artwork inside an SVG container. It is not newly drawn vector Sayo art, and this extension introduces no new character pose. The two website lettering treatments serve their documented roles; the Welcome signature does not replace every compact wordmark.

## Provenance and pixel fidelity

`output/kiyo-review-v2/prompts.json` records the original review concepts, their full prompts, the built-in `image_gen` tool, and the reference `output/sayo-review-v1/thumbsup.png`. Concept A's recorded original generated file is `C:\Users\vngia\.codex\generated_images\01a107a7-2da8-7c60-823f-623992227538\exec-366aa660-f80c-47dd-898b-ea751693ae6f.png`. Its old review-only status is historical; the owner's later selection authorizes the shipping signature documented here.

Decoded RGBA comparison on 6 October confirms that `public/brand/signature.png` and `output/kiyo-review-v2/concept-a.png` have identical dimensions and pixels. Their file hashes differ because shipping metadata was added. The common decoded pixel SHA-256 is `bad3a486ff0fda659a1fc3e96be463e4f441a1b7bbc94e44983e61d5d78da257`.

The shipping signature retains its `caBX` C2PA chunk and carries a custom `tEXt` chunk keyed `impeccable:prompt`. The three icon PNGs also carry that provenance key, identifying their rendered size, source SVG, source WebP and reuse of existing artwork. Presence of a C2PA chunk is not a claim that its signature has been independently validated.

The shipping signature's custom origin metadata now includes the original Concept A prompt from `output/kiyo-review-v2/prompts.json`, along with the selected source and unchanged-pixel reuse. The earlier incorrect “prompt unavailable” metadata was corrected after the documentation handoff.

## Preserved visual system

The authoritative current visual system remains `src/night.css` and DESIGN.md's “Night Study v2” section, following `../SHARED-SPEC.md`. The extension retains the adult study setting, Chinese-first learning hierarchy, Newsreader / Instrument Sans / Noto Serif SC typography, existing controls and layouts, and the approved Sayo identity. It adds no mascot location in lessons or tables and changes no assessment evidence rules, curriculum, audio or learner storage.

Existing documentation drift is recorded rather than repaired: PRODUCT.md and DESIGN.md's initial title/frontmatter still use the historical Tingjian name, and `.impeccable/design.json` still describes the earlier Night Study system. DESIGN.md's earlier branding paragraph describes the prior Welcome lettering role, superseded locally by the owner-selected signature recorded here. DESIGN.md's later Night Study v2 section remains the current interface authority. PRODUCT.md, DESIGN.md and `.impeccable/design.json` are unchanged by this documentation pass.

## Reproducible exports and references

From the repository root:

```powershell
npx tsx scripts/make-brand.ts
npx tsx scripts/export-brand-icons.ts
```

The first command exports `public/brand/wordmark.svg` and `public/brand/app-icon.svg` from the established lettering paths and existing waving WebP. The second uses installed Google Chrome through Playwright to render `public/brand/app-icon-180.png`, `app-icon-192.png` and `app-icon-512.png` at their named square dimensions. `npm run build` invokes `scripts/make-brand.ts`; it does not invoke the PNG export script.

PNG screenshots produced by `scripts/export-brand-icons.ts` do not preserve the custom provenance metadata. After regenerating these PNGs, re-embed the `impeccable:prompt` origin text before treating the exports as finished. The currently checked outputs have that metadata embedded. Do not rasterize or regenerate the selected Welcome signature to export the app tile.

`vite.config.ts` declares 192 px and 512 px PNG app icons plus the SVG fallback with `purpose: "any"`. `index.html` points the Apple touch icon to `/brand/app-icon-180.png` and the favicon to `/icon.svg`. These declarations are implementation evidence, not proof of platform installation behavior.

## Finish evidence and limitations

The finish reviewer returned **ship** for request fidelity and visual fit, with no material fixes at 1440, 768, 375 and 320 px. The handoff's evidence files are `.impeccable/review/brand-welcome-1440.png`, `brand-welcome-768.png`, `brand-welcome-375.png` and `brand-welcome-320.png`. This documentation pass verified asset roles against the component/CSS/export/configuration sources, signature pixel identity, icon dimensions and embedded provenance chunks.

The reviewer disposition is limited to this branding surface. Subsequent local checks: TypeScript passed; the full browser run had 29 passes, four new-course audio failures and three production-only conditional skips. Welcome accessibility and desktop/mobile layout checks passed. The required production build is blocked by the unfinished course audio catalog, so installed-app icon behavior and deployed branding remain unverified. No publication, push, paid connection or broader design-system refresh occurred.
