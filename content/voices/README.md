# Sayo voice

The deeper drawl direction is approved for local integration. Active settings are in `roster.json`; earlier auditions remain in `roster-auditions.json` and `output/voice-compare/`.

- `sayo-ref.wav` / `.txt`: the selected, lowered-pitch audition and transcript.
- `sayo-source.wav`: its synthetic parent, used for synthesis before applying -2 semitones once.
- `sayo-library-provenance.json`: model revision, every clip's settings, date and checksum.
- `sayo-audio-check.json`: full-library decode checks and measured loudness.

Run the commands under “Sayo audio generation” in the root README. The application uses `src/audio-assets.json` and MP3s in `public/audio-v2/`. Review 20 sample clips and all single-syllable clips at `/output/voice-review/index.html`. Do not interpret file checks as a pronunciation score.
