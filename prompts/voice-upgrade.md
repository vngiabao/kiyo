# Prompt for the work chat: free, better voices (CosyVoice, local GPU)

Paste everything in the box into the work chat that has this folder open.

```
New task (after cloud sync, or in parallel if it doesn't touch the same files): replace the robotic Kokoro voices with better, FREE, local Mandarin voices. Read AGENTS.md first. Don't touch sync code.

MACHINE: Windows, NVIDIA RTX 4070 SUPER (12 GB). Python env for the old audio is .audio-env; models live in .models/ (both git-ignored).

1) SET UP COSYVOICE (open source, Apache-2.0)
- Make a separate env .tts-env (use the Python version the CosyVoice README requires, CUDA PyTorch build) and clone https://github.com/FunAudioLLM/CosyVoice into .tts/ (git-ignored).
- Download the newest CosyVoice 0.5B model (CosyVoice2-0.5B or Fun-CosyVoice3-0.5B, from Hugging Face or ModelScope) into .models/.
- Before each download, tell me the file name, source and approximate size; then go ahead.
- If CosyVoice won't install on Windows, try IndexTTS2 (Bilibili, open source) instead and tell me why.

2) ONE VOICE, MANY MOODS (the whole app is built around one character's personality)
There is exactly ONE voice identity: Sayo. Young adult woman, low-mid pitch, cool, slightly husky, crisp diction, an "Ado-style" vibe: introverted and composed most of the time, with sudden bursts of intensity. NO male voices and NO other characters' voices; everything is spoken by her in different moods. Build it from one base timbre (CosyVoice instruct mode, or a reference clip if I put one at content/voices/sayo-ref.wav + sayo-ref.txt). Don't clone any real person's voice; design an original one with this vibe.
Moods (same timbre, different delivery):
- clear: calm, precise, medium pace, very clean tones. DEFAULT for lessons, words and tone drills.
- cool: low, unhurried, slightly bored. Sayo's everyday lines (来了？开始吧。, 声调呢？).
- intense: sharper, louder, faster, "on-stage" energy. Praise, level-ups (太棒了！, 升级了！) and exclamations.
- soft: quiet, gentle, a little shy. Encouragement after mistakes (没关系，再试试), rest moments.
- deadpan: flat, dry humour. Errors and teasing (又断了。, 不错嘛。).
- playful: lighter, a smile in the voice. Casual dialogue lines and chat messages.
Keep every mood's settings in content/voices/roster.json (id, description, instruct text or reference, speed, pitch shift if used).

3) COMPARISON PAGE FIRST (don't change the app yet)
Generate these sentences in every mood, PLUS the current Kokoro files for comparison:
妈 麻 马 骂 · 你好 · 我没听懂 · 可以再说一次吗？ · 一共三十五块 · 你想吃米饭还是面？ · 来了？开始吧。 · 声调呢？
Write output/voice-compare/index.html (a simple table: sentence × mood, with play buttons). Open it, tell me where it is, and STOP for my choice.

4) AFTER I PICK, GENERATE EVERYTHING
- New script scripts/generate-audio-cosy.py, driven by content/audio-scripts.json (rebuild it with npx tsx scripts/audio-manifest.ts, and extend that script to include content-pack phrases, grammar examples, dialogue and reading lines).
- Output to public/audio-v2/ (keep public/audio/ until I approve).
- Write src/audio-assets.json in the SAME format the app already reads: { "<text>": { "<voiceId>": "/audio-v2/<file>.mp3" } }.
- Voice mapping (all moods of the one Sayo voice):
  - lessons, words, examples and tone drills → clear (plus playful as a second take for listening variety);
  - Sayo's lines in src/Mascot.tsx → the mood that fits each line (cool / intense / soft / deadpan);
  - dialogues with several speakers → give each speaker a different mood and a slightly different speed, so turns are easy to tell apart;
  - single characters and particles stay voiced inside a word, as now (the `say` field).
- Update src/audio.ts and Settings: the picker becomes "Sayo's voice: clear / cool / playful" (default: clear); keep device voices as a fallback.
- Quality pass on every clip:
  - trim leading/trailing silence;
  - normalise loudness to about -16 LUFS;
  - MP3 or Opus at 24 kHz;
  - fail loudly on any empty or broken file;
  - re-generate any clip that's suspiciously long or short for its text.
- Spot-check: list 20 random clips for me to listen to, plus every single-syllable clip; mono-syllables are where TTS most often gets the tone wrong.

5) FINISH
- Update content/audio-provenance.json (model, version, voice, settings, date, SHA-256 per file) and THIRD_PARTY_NOTICES.md (CosyVoice, Apache-2.0).
- Run npx tsc -b, npm test, npm run validate:content and npm run test:e2e.
- Precache: make sure the PWA still stays reasonably small (audio-v2 total size; tell me the number).
- Only after I approve by ear: delete public/audio/ and the Kokoro references.
- Report plainly: what's done, what was verified, what's left.
```
