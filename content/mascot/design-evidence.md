# Ado design extension evidence

This narrow documentation merge records the implemented Ado extension to the incumbent **Reading Room**. It updates only the illustration exception, mascot motion exception, and companion policy in `DESIGN.md`; no shared colour, type, or layout token changes were made.

Sources inspected: `.impeccable/surface-briefs/ado.md`, `content/mascot/README.md`, `src/Mascot.tsx`, `src/mascot.css`, and the relevant route/preferences in `src/App.tsx`. The twelve PNG filenames in `public/mascot/` match the twelve component states. The component and CSS establish decorative rendering, bounded whole-pose motion, persistent preference behavior, and the system reduced-motion override. Prompt provenance is recorded by the asset README and `provenance.json`; this documentation pass does not revalidate PNG metadata.

Visual evidence inspected: `.impeccable/review/ado-desktop.jpg` shows the twelve-pose collection using the incumbent paper, typography, and controls; `.impeccable/review/ado-lesson-mobile.jpg` shows a small companion above the learning content while the Chinese specimen remains dominant. Still screenshots establish composition, not animation timing; duration and suppression behavior are evidenced by the implementation. This pass did not rerun browser interactions, learning tests, or the production build; their recorded results remain in the asset README.

Known pre-existing documentation drift is intentionally untouched: `.impeccable/design.json` still describes the earlier Quiet Study Room world, and `.impeccable/surface-briefs/app.md` retains that historical rail/nav design and a now-stale no-shipping-raster statement. Neither is authority for the Reading Room or this mascot extension. This ordinary extension does not repair or regenerate those unrelated files.

Finish verdict: **ship** for the scored fixes. The reviewer confirmed the persistent motion preference is honored in the collection, the narrow DESIGN.md exceptions match the extension, and seed provenance is explicitly historical rather than retrospectively invented. Published as Sites version 2; the public collection capture is `.impeccable/review/ado-public.jpg`.

## Chibi revision record

The user corrected the first set as too stiff and requested a squat, cute Ado with meme-like and angry-cute expressions informed by the supplied reel and screenshot. The current fourteen poses live in `public/mascot/chibi/`; `grumpy` and `smug` join twelve redrawn learning states. `content/mascot/chibi-provenance.json` records the current exact prompts and source paths. The twelve previous PNGs are retained in `content/mascot/archive-v1/`, preserving the historical evidence above rather than silently relabeling it as current.

Inspected the revised surface brief, `src/Mascot.tsx`, `src/mascot.css`, the current provenance record, asset filenames, and `.impeccable/review/ado-chibi-desktop.jpg` plus `ado-chibi-mobile.jpg`. These captures show the squat silhouette, exaggerated expressions, all fourteen thumbnails, and grumpy as the initial selected pose, within the existing Reading Room. The component points image and download URLs to `/mascot/chibi/`. Notebook/card prompts specify no readable answer characters; the prior 人 prop is not the policy for this revision.

CSS evidence establishes a 1100ms grumpy stomp, 900ms error stomp, 1100ms smug lean, and a stronger 1050ms squash/leap/landing cheer. Overall motion remains bounded to 650–3200ms, with unchanged persistent preferences and the system reduced-motion override. These are complete-pose transforms, not articulated, skeletal, lip-synced, or frame-by-frame animation. Still screenshots do not prove motion timing.

This documentation update changes only the Ado subsection of `DESIGN.md`, the current asset README, and this appended record. Shared tokens, unrelated narrative, old sidecar drift, and the historical app brief are untouched. No fresh build, learning test run, browser interaction check, or PNG metadata audit was performed in this documentation pass. The fresh chibi reviewer is running separately; the first-version ship verdict above is historical and is not a verdict on this revision.

Fresh chibi finish review: **ship** for the scored correction after DESIGN.md and FIRST VIEWPORT count were reconciled. Reviewed desktop/mobile captures support the squat silhouette, expression differentiation, transparent edges, and all fourteen states. The optimized production build passed; the detector returned no findings, and all fourteen shipping PNGs passed prompt-metadata coverage. Learning tests were not rerun for this artwork/CSS/copy revision; the earlier fourteen-test result remains historical.

Published as Sites version 3. The live collection visibly shows all fourteen chibi states; selecting smug and grumpy works, and all fifteen displayed images (featured plus thumbnails) loaded successfully. Public proof: .impeccable/review/ado-chibi-public.jpg. The existing offline worker required closing the site and reopening after installation before the new collection appeared.


## Quiet Ado and Night Study revision record

Current authority is the user-approved `exec-f5923449-08b7-4bc1-8597-e45f2b2946e9.png` reference and `.impeccable/surface-briefs/quiet-ado.md`. The user approved the slender, small-face, subtle-expression character and requested the remaining set plus integration, while pinning an Oura phone-app inspired palette. This is an authorized palette adaptation and asset replacement within established layouts; no new direction workshop or seed is claimed.

Fourteen current transparent PNGs live in `public/mascot/quiet/`, with exact prompts/source paths in `content/mascot/quiet-provenance.json` and the pack `ado-quiet-set.zip`. The previous fourteen chibi assets are preserved in `content/mascot/archive-v2/`; first-version assets remain in `archive-v1/`. Earlier verdicts and publication records above remain historical.

This pass inspected the current root CSS variables, mascot component and motion CSS, asset filenames, surface contract, and screenshots `quiet-gallery-desktop.jpg`, `quiet-today-mobile.jpg`, and `quiet-lesson-mobile.jpg` under `.impeccable/review`. They show the small-face approved direction and midnight palette while retaining the editorial layout and Chinese specimen hierarchy. The additional gallery-mobile and Today-desktop captures are available to the finish reviewer. Still captures do not establish motion timing.

The implementation now uses midnight navy surfaces, soft white/blue text, pale blue action fill with deep lettering, quiet teal success, peach correction, and native dark colour-scheme. `DESIGN.md` has token-bearing frontmatter extracted from actual CSS; the formerly stale `.impeccable/design.json` was regenerated for this authorized system change, with current component snippets and extension metadata. The aesthetic paragraph in `PRODUCT.md` and the mascot direction brief agree with the new authority. Existing typography/layout and unrelated product/learning truth remain preserved.

CSS assigns grumpy/error to a gentle thought tilt (1100/900ms), quiet smug settling (1100ms), and a 6px celebration (1050ms); runs remain finite at 650–3200ms. Old stomp keyframes are present but unused by current states. Persistent visibility/motion, preference-loading suppression, and system reduced motion remain authoritative. No full-rig, articulation, lip-sync, or frame-by-frame capability is claimed.

The existing literal `#000` behind local video is documented as a media-only letterbox/backdrop role rather than a general theme surface. The observed 400ms lesson-progress transition is recorded as an existing exception to typical 160–300ms interface motion. No code changes were made in this documentation pass.

Implementation handoff reports the production build and all 14 existing learning tests passed. This documenter did not rerun those checks or re-audit embedded PNG metadata. No final fresh reviewer verdict or new publication is asserted here. The historical app brief still records the former rail world; it is history, not current visual authority.

Additional finish evidence: `.cache/mascot-qa/quiet-contrast.json` records 40 palette pairs, all passing (count/result checked during documentation). The implementation handoff reports no failures in rendered lesson text checks and working phone gallery Rest selection and pause controls. The supplementary `quiet-media-desktop.jpg` viewport capture is available. Design sidecar JSON parsed successfully; its 25 colour roles and nine component references agree with the current design frontmatter, with no old DM Sans/blue-token world remaining in the sidecar.

Fresh scoped finish review: disposition **ship**, no material fixes for Quiet Ado and Night Study. Published as Sites version4; deployment succeeded with unchanged public audience. All14 quiet states are the shipping collection.


Public proof: .impeccable/review/quiet-public.jpg shows the deployed navy gallery and14quiet states. Live DOM confirmed15images (featured plus thumbnails),0broken, and the new navy body color. Public URL remains https://tingjian-mandarin-preview.gbao-n-vo.chatgpt.site/#ado .

