# Prompt for the Chinese (Kiyo) chat: shared-spec parity pass

Ready to send now: Shiori's version is built and tested (5 Oct 2026). Kiyo already matches most of SHARED-SPEC; this is a short list. Make sure the Chinese chat is idle first.

```
SHARED-SPEC PARITY PASS (from me, after a Claude audit of both apps)

Read ../SHARED-SPEC.md. It is now the shared standard for Kiyo and its sibling Shiori (../Japanese). Kiyo's Today and lesson screens were its main model, so most of it is already true here. Add "Follows ../SHARED-SPEC.md" to AGENTS.md. Keep Night Study, Sayo's art and persona, and the database identity tingjian-v1. One voice only (Sayo's, with moods).

Make these changes, in small batches. After each: tsc -b, npm test, validate:content, audio check, e2e with axe, build; screenshots at 1440/768/375/320, compared with the same Shiori screen.

1. Navigation: rename "Media Lab" to "Media" everywhere (nav, More drawer, headings). Order stays Today · Read · Listen · Speak · HSK · Practice · Media · Progress.

2. Lesson screen and Sayo's bubble (Shiori's built version is the reference: ../Japanese/src/study-layout.css, "Focus mode" to "The verdict"):
- Sayo currently sits in the far bottom-right corner, with a large empty area between her and the task. On desktop (≥1100px) make the lesson body a grid: task column up to 720px plus a 200px companion column, 56px apart. Sayo (140px) is sticky at the top of her column; her bubble appears directly beneath her with the tail pointing up, so she can never cover an answer. Below 1100px she moves into normal flow after the task (96px tablet, 64px phone) with the bubble to her left.
- Bubble: Chinese line 18–20px / pinyin 14px (always shown) / English 14px at 4.5:1 contrast or better (it's too dim now) / "Hear Sayo" as a 44px target, 14px corners. It shows only on reactions and clears on Continue; while idle there's no bubble. On phones it collapses to one line and taps open.
- Remove the FIND / LISTEN eyebrow above task headings; the heading already names the task. Make a single-character prompt large (about 96px, 80px phone).
- Task column starts about 12vh from the top, so short tasks (e.g. "Which one means 'eight'?") don't leave the bottom two-thirds empty.
- Verdict: keep it fixed at the bottom, but make it a reading-surface sheet instead of a full teal/peach wash: 3px top edge in the state colour, the icon in a filled state-colour circle, "Right." / "Not quite." in ink, one evidence line ("Recalled without help." / "Pinyin was shown, so this counts as supported."), Continue on the right. Less colour, same meaning.
- Disabled primary buttons: full opacity, accent-wash fill, quiet text (not 0.38 opacity).

3. Today:
- Sayo at 200px desktop / 140 tablet / 96 phone, with at least 24px clearance below the header (she currently touches the header rule). Bubble to her left, same anatomy as the lesson bubble.
- Add the 10–60 min session selector next to "Today's session" (adopted from Shiori), replacing the static "30 min".
- Plan rows: keep the plain numerals; add a → arrow at the right of each row.
- Stats table: move "Next milestone" to the top row and phrase it as a human goal (e.g. "First Contact: greet and introduce yourself").
- Lead lesson: show "Hear it" beside Continue whenever the lesson has audio.

4. Update DESIGN.md and .impeccable/design.json to match. Report with before/after screenshots of Today and a lesson step (correct + wrong) at 1440 and 375, side by side with Shiori.
```

---

## Optional: Sayo readability (ChatGPT image prompt)

Only if you want to improve Sayo. This keeps her design and only helps her read on the midnight background at small sizes, where her navy hair and dark coat blend in.

Attach the current poses from `public/mascot/quiet/`.

```
Edit the attached sprite of my character Sayo. Keep her design exactly: face, eyes, ahoge, long navy-blue hair, black coat, teal brooch and cravat, proportions, line style and pose. Change only two things so she reads on a very dark navy background (#101b2b) at 56–132 px: (1) make the pale outer rim around her whole silhouette a consistent 3 px soft blue-white (#cfe0f5) line, and (2) lift the hair highlights one step lighter (#3b57a8 range) so the hair mass separates from the coat. Do not change colours anywhere else. Transparent background, same canvas size and framing.
```

Run it on one pose first, check it at 56px on Today and in a lesson, then batch the rest.
