# C1 validation and handoff — 5 October 2026

Scope: GPT course research and planning only. Claude's A/B changes were present and evolving in the same checkout. No new packs, generated speech, runtime UI, storage or sync changes were made by this C1 pass; no push/deployment was performed.

## Research checks

- `npx tsx scripts/coverage-report.ts --write`: current GF2021 introduced word entries 189 / 26 / 6; remaining 311 / 746 / 967. Explicit new-character coverage 63 / 1 / 1. Grammar counts 48 / 81 / 81, not 48 / 82 / 81.
- `npx vitest run tests/coverage-report.test.ts tests/course-plan.test.ts`: **8 passed**. Seven audit tests cover grouped forms, repeated readings/senses, incidental exposure, new vs supplementary characters, unnumbered grammar cross-references and verified card evidence. The plan test checks 96 IDs, prerequisites, 15–25-entry budgets, 2–3 family labels per unit, all 210 owners and two later retrievals.
- MOE scanned standard downloaded; benchmark/topic/character pages and representative Appendix A code pages visually inspected. CTI query rows fetched completely, preserving source numbers. Newer exam PDF vocabulary numbering 1–1000 and per-level recognition-character numbering checked for continuity. Web release-page retrieval timed out; the original PDF and official query were available.
- The audit is curriculum evidence, not learner progress, native approval or spoken-tone validation. Exact vocabulary/character allocations and broad grammar subpattern schedules remain C2 pre-writing work.

## Shared app checks

- `npx tsc -b`: **passed** on the final checkout. Initial failure was a case collision between Claude's in-progress ReadingDrill/readingDrill files; that was resolved during A/B work without C1 editing those files.
- `npm test`: **113 tests passed in 15 files** on the final run; the eight research/plan tests are included in that total.
- `npm run validate:content`: **passed**. 281 phrases, 66 characters, 29 readings, 52 lessons, 1,142 exercise steps; 1,215 audio texts, 3,023 provenance-matching files and 277 task mood mappings.
- `npm run build`: **passed**, including pack validation, pinyin, stroke copying, audio checks, SVG brand generation, types and Vite. All 12 existing packs compiled. Pinyin check: 2,887 words matched, two characters without an entry (e.g. names), zero lines to fix.
- Existing-pack warnings remain: each of the 12 packs has a warning, mostly insufficient contextual repetition; one flags many glossed characters. These are not newly written C1 packs. The larger-than-700-KB JS chunk warning also remains. Build success does not mean these stronger quality/performance goals are all met.
- `npm run test:e2e` against dev server: **28 passed, 3 production-only skipped, 1 timeout**. The timeout was `word taps and Sayo feedback, quiet mode false`, still at onboarding step 2 while waiting for the final onboarding button. **It passed alone on retry** (`npx playwright test e2e/voice.spec.ts --grep 'quiet mode false'`, 4.3 seconds). No persistent failure reproduced, but this was not a clean single full-suite run; an onboarding timing flake remains a candidate for A/B's test hardening.
- The three skipped production tests were run against the existing local preview at port 4173: **3 passed** (installed HSK offline, explicit app refresh, installed production routes/audio offline).
- PWA build precache: **362 entries, 3,227.69 KiB**. Research JSON/Markdown is outside app assets and absent from the service-worker precache. Audio/dictionary remain demand-loaded according to the shared app configuration.
- `git diff --check -- AGENTS.md PEDAGOGY.md`: passed. No UI screenshots are claimed for this research-only pass. Browser suite captures its own responsive evidence; new unit visuals wait until C2 exists.

## Approval and remaining work

Review `course-plan.md` / `course-plan.json`: 18 further level-1 units, 34 level-2 units, 44 level-3 units, covering a budget of 2,024 remaining GF2021 entries. Approve the additive second-reading seam, grammar family/subpattern tracking and core/stretch reading lengths before C2. Then allocate and write s1-u13–s1-u16, reconcile needed source-sense discrepancies, repair existing quality warnings as appropriate, generate the approved Sayo audio, run gates and stop again for the first-batch review.

Native Chinese/Vietnamese review, exact sense-level allocations, pronunciation review, a current-exam item crosswalk and human proficiency outcomes are **not verified** by C1. Claude's dictionary/drill research is `dictionary-and-speed.md`; runtime ownership remains with Claude.
