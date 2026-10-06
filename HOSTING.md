# Kiyo hosting

## Current deployment — 5 October 2026

- Address: https://kiyo.gbaonvo.com
- Host: Cloudflare Workers static assets, project `kiyo`, connected to the private `vngiabao/kiyo` GitHub repository, production branch `main`.
- Build command: `npm run build`. Deploy command: `npx wrangler deploy`. Root directory: `/`.
- Configuration: `wrangler.jsonc` serves `dist/` with SPA navigation handling and binds `kiyo.gbaonvo.com` as a custom domain.
- Cloudflare Access protects all Worker traffic with the `Kiyo owner only` Allow policy, restricted to `gbao.n.vo@gmail.com`. Other identities are denied by default. The existing Google and Cloudflare identity providers are available.
- The production `workers.dev` address, preview URLs, and preview builds are disabled.
- No new paid service, domain purchase, or database was required. The deployment reuses the account's existing build credential; no secret is stored in this repository.
- Supabase is configured through the existing Cloudflare build variables. Kiyo and Shiori share the owner's project with separate progress tables. Google-only sign-in is enabled; Cloudflare Access login and optional learning sync remain separate. A CLI release must load the same public `VITE_SUPABASE_URL`, publishable `VITE_SUPABASE_ANON_KEY`, `VITE_AUTH_MODE=google-only` and `VITE_AUTH_PROVIDERS=google` into the Vite build. An ignored `.env.local` holds these settings on this machine. Never put a service-role key in Vite variables.
- Verified: Cloudflare build/deployment succeeded; the custom domain presents the Access gate, the owner's existing Cloudflare login reaches Kiyo, onboarding and the Sayo gallery load, and the gallery has no broken images. Full learning tests passed locally before deployment; remote-device and live-Supabase tests are still separate checks.

## Historical public preview

> Update: the mascot has been renamed Mo (墨墨). The gallery URL is now `#companion`; the entries below are a historical log.

Live URL: https://tingjian-mandarin-preview.gbao-n-vo.chatgpt.site

Published 4 October 2026 through Sites with public access. The site is hosted remotely and does not require the local computer to stay online. Anyone with the URL can open it.

Site project ID: `appgprj_6ac29861c7408191ac91ce3d16f8e67a`
Saved version: `appgprj_6ac29861c7408191ac91ce3d16f8e67a~appgver_8b4c238c46948191bf36c33fcd774c73` (version 4, Quiet Ado and Night Study)
Source commit: `f7b6285b8a42a6ca3b8dd3c95f2c5d7d8af0e994`
Deployment ID: `appgdep_6ac2b327f8948191b9dc5bde9f9fa300`

Ado collection: https://tingjian-mandarin-preview.gbao-n-vo.chatgpt.site/#ado

The Ado update includes 14 transparent chibi poses, bounded CSS animations, preferences, and offline precaching. Existing open PWA tabs may keep the old service worker until all tabs for this site close; reopen after the update finishes downloading to activate it.

The hosting checkout is `.cache/hosted-preview/`, with its identity in `.openai/hosting.json` inside that checkout. It contains a snapshot of the compiled root `dist/` output in checkout `build/`, the directory declared by the hosting manifest. The main app source remains in the project root. Future source edits are not automatically published: build the application, update the hosted snapshot, obtain a fresh repository credential for the existing Site, and follow the Sites save/deploy workflow. Reuse this Site ID and preserve public access unless requested otherwise. Never store credentials in this file or the checkout.

The Sites helper on this Windows machine requires Git Bash ahead of Windows bash in the child process PATH and TAR_OPTIONS=--force-local for Windows archive paths. These were process-local settings; global system configuration was not changed.

Learning progress remains local to each browser and origin. A remote device starts with its own record. To move existing progress from localhost, export in the old app and import the backup on the public site. Microphone permission remains optional.

Verification: this chibi revision passed the optimized production build, prompt coverage, detector, and desktop/mobile visual review. The earlier 14 learning tests passed before this artwork/CSS/copy revision; they were not rerun for it. Native hosting returned deployment succeeded and public access. The hosted Ado collection loaded after reopening the previous cached app tab; its image endpoint returned 200. Phone-sized and desktop layouts and mascot controls were tested locally. No physical remote-device regression run was performed.

Version 3 live verification: the served HTML references the current production bundle, the new grumpy PNG returns 200, and the public gallery shows fourteen states after cache activation. Smug/grumpy selection worked with zero broken images. Capture: .impeccable/review/ado-chibi-public.jpg.

Version 4: all14 slender small-face quiet PNG poses replace the exaggerated set; Oura-inspired navy semantic palette across the app and PWA chrome; gentler finite animations. Build and all14 learning tests passed,40colorpairs passed, prompt metadata14/14, fresh scoped design reviewer disposition ship. Earlier version verification above remains historical.

Version4 live browser verification: Quiet company heading, /mascot/quiet download paths, navy rgb(16,27,43) body,15 displayed images with0broken. Public screenshot: .impeccable/review/quiet-public.jpg. Existing cache required reopening after update installation.

