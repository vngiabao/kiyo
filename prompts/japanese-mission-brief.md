# Mission brief: the Japanese thread (Shiori × Violetto)

Paste the box into the Japanese chat (folder `Language Learning/Japanese`). It restates the whole mission from the beginning, then gives the next big task: the serious JLPT grind corner.

```
MISSION BRIEF: read this fully, then read AGENTS.md, PRODUCT.md, DESIGN.md, PEDAGOGY.md, PERSONA.md and AUDIT.md in this folder. This brief restates the mission from the start and sets the next work. Where it conflicts with older docs, this brief wins; update the docs to match.

1) WHO AND WHY
One adult learner (me): English/Vietnamese speaker, starting from zero, studying daily for years. I want to understand anime, drama, YouTube and real people without subtitles; hold real conversations; read manga, novels and articles; write messages; and reach professional Japanese with correct keigo. Reading matters a lot; handwriting is optional. JLPT N5 → N1 runs alongside: communication is the spine, and the JLPT corner is where I grind seriously for the exam. This is a personal project.

2) IDENTITY
- App: Shiori (working name; brand lives in src/brand.ts). Database identity shiori-japanese-v1 must never change.
- Mascot: Violetto, a Violet Evergarden-inspired chibi letter-writer (blonde braids, blue eyes, navy coat, ivory skirt, emerald brooch, red ribbons). Persona per PERSONA.md: composed, precise, sincere, quietly caring; she never scolds or guilt-trips. One female voice with mood variations.
- World: antique letters and correspondence. Light "Morning letter" / dark "Night post"; the latest palette preference is predominantly blue with hints of red and some violet, tiny gold, emerald for correct/known. Mincho for Japanese, a classical serif for headings, a clean sans for UI, a typewriter accent for letters.

3) TWIN OF KIYO
The sibling Chinese app (../Chinese, "Kiyo" with mascot Sayo) is the structural reference. Both apps should be the same product in structure (navigation order, onboarding, Today, lesson flow, exercise types, path map, reader, review, levels, exam room, sync/backup, components, motion, accessibility, expression system, content-pack standard) and differ only in character, theme, voice and language-specific teaching. If Language Learning/SHARED-SPEC.md exists, follow it. Kiyo's HSK room is the twin of your JLPT corner: read Chinese/src/Hsk.tsx and hsk-*.ts for ideas (don't copy its theme or persona).

4) NON-NEGOTIABLES
- Honest evidence: only unaided answers count. Furigana, hints, transcripts and shown answers are supported work. Self-report and book checkboxes are never scores. No invented JLPT scores, pass predictions or "readiness %".
- Content is data (content/packs) and goes through the content gate; keep provenance; AI-generated Japanese stays labelled "AI-assisted draft" until reviewed.
- Data safety: additive migrations only; export/import keeps working; nothing local is cleared to fix a bug.
- Accessibility: keyboard, focus, WCAG AA contrast (axe in browser tests), reduced motion, no overflow at 320 px.

5) NEXT BIG TASK: THE JLPT GRIND CORNER (upgrade the existing JLPT room; keep its data and tests)
A serious, focused corner for exam grinding, all levels N5–N1.

5a. Entering the corner
- A distinct "study hall" mode: quieter, denser, more serious than the rest of the app (same theme family, lower ornament, more structure). Clear "Exit to the course" control.
- Level picker N5–N4–N3–N2–N1 + exam date (optional; plans the remaining weeks around the July/December sessions and shows a reminder to check official registration dates).

5b. Pathway built on well-known prep material (map to the books I own; don't reproduce their pages)
For each level, a clear sequence of steps with prerequisites, built around the standard series learners actually use:
- N5–N4: Genki I/II (3rd ed.) or Minna no Nihongo Shokyu I/II for the core; Nihongo Sō-matome N4/N5 and TRY! N5/N4 for exam focus.
- N3–N1: Nihongo Sō-matome (漢字・語彙・文法・読解・聴解), Shin Kanzen Master (文法・読解・聴解・語彙・漢字), TRY! (grammar through reading); optional 耳から覚える for listening/grammar.
- All levels: the official JLPT sample questions and Official Practice Workbooks (公式問題集) for mocks.
Model each book as chapters/weeks with a daily quota (e.g. Sō-matome's week/day layout). Each chapter gets: what to study (book + pages/chapter), the key points as MY OWN notes field, and an original quick check written by you in the same format (never copied from the books). Order per level: entry self-check (prerequisites from the level below) → 文字・語彙 → 文法 → 読解 → 聴解 → timed section samples → full mock from the official workbook (I enter my raw section scores) → review of weak areas. Unlock the next step with ≥ 80% unaided on its checkpoint; book checkboxes alone never unlock exam steps.
Show the whole route at a glance (all levels), the current step, and what's required to move on.

5c. Practice and sample exams
- Original questions in the official question formats, covering the core modes per level (not every mode needed):
  - 文字・語彙: 漢字読み, 表記, 文脈規定, 言い換え類義, (用法 at N3+).
  - 文法: 文法形式の判断, 文の組み立て (★ ordering), 文章の文法.
  - 読解: 内容理解 short/mid, 情報検索; at N2–N1 add 統合理解 and 主張理解.
  - 聴解 with audio in Violetto's "clear" voice: 課題理解, ポイント理解, 即時応答.
- Timed section samples with the official time ratios; auto-submit; review screen with explanations in English + the Japanese grammar point; every miss goes into a mistake notebook and FSRS review.
- Score honestly: show raw scores per section and the official sectional minimum rule. Never convert to scaled scores or predict a pass. Say clearly that internal samples are short and not calibrated.
- Grow the bank through the content gate (target per level: at least 60 checkpoint items + 30 sample items to start), with a validator for answer keys, ★ ordering integrity, distractor uniqueness, level-appropriate vocabulary (against the JLPT word list with provenance) and audio presence.

5d. Teacher Violetto (serious mode)
- Teacher pose set, consistent with her approved design: slim oval glasses, closed folio, fountain pen. Poses: lecture (pen raised), assign (handing a folio), checking (glasses adjusted, reading a paper), timer start (pocket watch), stern focus (arms folded, folio), passed (small approving nod, faint smile), missed (calm, pointing to the line in the text), break (tea, glasses off). Same chibi proportions, framing and line style as her other poses; write the image prompts next to the art (as you already do) and integrate via the existing asset pipeline.
- Teacher voice mood: "lecture": slower, precise, firm, polite です/ます; same voice identity.
- Lines (Japanese → reading → English), e.g.:
  - 始めましょう。集中してください。 (Let's begin. Please focus.)
  - 今日の課題はこちらです。 (Here is today's assignment.)
  - 時間です。ペンを置いてください。 (Time's up. Please put your pen down.)
  - よくできました。次の段階へ進みましょう。 (Well done. Let's move to the next step.)
  - ここをもう一度確認しましょう。 (Let's check this part once more.)
  - 少し休憩しましょう。 (Let's take a short break.)
  Keep all lines in content/voices/violetto.json with readings and acting notes; generate audio for them.

6) AFTER THE JLPT CORNER (in this order)
1. Align with Kiyo per SHARED-SPEC.md (when it exists).
2. Grow the course through validated content packs (N5 core first), labelled AI-assisted drafts.
3. Cloud sync (mirror Kiyo's Supabase design: RLS, deterministic replay, consent before merging guest data); include the JLPT notebook in sync and backups.
4. AI conversation partner via a server proxy (no keys in the browser).
Ask me before connecting any live or paid service.

7) SKILLS AND METHOD
- Apply the design skills in sequence: Taste (subtract) → Hallmark (anti-generic structure) → Impeccable (hierarchy, states, accessibility, polish) → Emil Kowalski (motion: transform/opacity, ease-out, under 300 ms, press 0.97, reduced motion). Install any that are missing from their official sources (npx impeccable install; npx skills@latest add emilkowalski/skills; Hallmark from ../Chinese/.agents/skills/hallmark).
- Work in small batches. After each: types, unit tests, content gate, JLPT validator, audio check, browser tests with axe, build; then screenshots at 1440/768/375/320 and look at them. At least two critique rounds before calling it done.

8) STOP POINTS AND REPORTING
- STOP after drafting the JLPT corner's structure (route map for all levels, book mapping, screen layouts) and the teacher pose prompts: show me before generating art or large question banks.
- STOP before installing new Violetto art.
- Finish with a plain-English report: what changed, what was verified, counts (questions per level/mode, chapters mapped), and what still needs my eyes, ears or decisions. Update AGENTS.md, AUDIT.md and QA notes.
```
