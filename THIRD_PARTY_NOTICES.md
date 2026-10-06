# Third-party notices

## Runtime software and fonts

Actual license texts are distributed in `public/licenses/` and copied to `dist/licenses/` on build. Runtime components:

- @fontsource-variable/newsreader: OFL-1.1
- @fontsource-variable/instrument-sans: OFL-1.1
- hanzi-writer 3.7.3: MIT
- hanzi-writer-data: Arphic Public License (stroke data derived from Make Me a Hanzi / AR PL fonts); copied per character into `public/hanzi/`
- @fontsource/noto-serif-sc 5.3.0: OFL-1.1
- @phosphor-icons/react 2.1.10: MIT
- dexie 4.4.6: Apache-2.0
- dexie-react-hooks 4.4.0: Apache-2.0
- react 19.3.0: MIT
- react-dom 19.3.0: MIT
- scheduler 0.28.0: MIT
- ts-fsrs 5.4.2: MIT
- workbox-window 7.4.1: MIT
- workbox-core 7.4.1: MIT
- workbox-precaching 7.4.1: MIT
- workbox-routing 7.4.1: MIT
- workbox-strategies 7.4.1: MIT
- workbox-cacheable-response 7.4.1: MIT
- workbox-expiration 7.4.1: MIT

Newsreader, Instrument Sans and Noto Serif SC are self-hosted; no Google Fonts network request is needed. Their SIL Open Font License notices are included. Application code is a private project; this file does not assign a new public license to original project work.

## Synthesized speech

The approved B-half rollout in `public/audio-v2/` uses **Qwen3-TTS 1.7B Base** (Apache-2.0), revision `fd4b254389122332181a7c3db7f27e918eec64e3`, with qwen-tts 0.1.1. Its original synthetic B anchor came from VoiceDesign revision `5ecdb67327fd37bb2e042aab12ff7391903235d3`. One fixed speaker representation combines that anchor with three earlier synthetic Sayo clips, at 85/15 model-input weights. These weights are not perceptual percentages. Six reference deliveries share that identity. No real-person recording is used. Approved processing uses SciPy (BSD-3-Clause) polyphase resampling, -2.25 semitones from the unprocessed source. `content/audio-provenance.json` identifies the installed per-file settings, dates and SHA-256 records.

Earlier Sayo references and the archived previous library use **Fun-CosyVoice3-0.5B-2512** (Apache-2.0), revision `29e01c4e8d000f4bcd70751be16fa94bf3d85a18`, with **CosyVoice** code revision `074ca6dc9e80a2f424f1f74b48bdd7d3fea531cc`. Their metadata and audio are retained in `output/audio-backup-before-approved-b/`. The historical audition notes below describe their state at the time of each experiment; the approved profile and installed provenance are authoritative for the current library.

Local advisory screening uses OpenAI Whisper medium (MIT), opencc-python-reimplemented 0.1.7 (Apache-2.0) for traditional/simplified spelling, and pypinyin 0.55.0 (MIT) for tone-number homophone comparisons. None is shipped in the web app. Screening does not certify pronunciation, lexical tones or native naturalness.

Build-time audio processing uses librosa (ISC), SoundFile (BSD-3-Clause), pyloudnorm (MIT), imageio-ffmpeg (BSD-2-Clause), and its local FFmpeg binary (GPL-3.0-or-later, per the binary's `-L` output). The generated MP3 files are shipped; the models, FFmpeg binary and Python environment are not shipped in the web app. FFmpeg normalizes loudness and encodes mono 24 kHz MP3. Measured corrections account for short syllables using an explicitly recorded smaller loudness window. Checks validate audio integrity and levels, not linguistic accuracy.

The retained legacy backup files under `public/audio/` (185 original clips plus 150 for the characters track and graded readings) were generated locally from original seed scripts using [Kokoro-82M-v1.1-zh](https://huggingface.co/hexgrad/Kokoro-82M-v1.1-zh), identified by its publisher as Apache-2.0. Voices: zf_001 and zm_010. Generation used [kokoro-onnx](https://github.com/thewh1teagle/kokoro-onnx), MIT, and Misaki Chinese grapheme-to-phoneme processing. The source model, voice bank and tools are not shipped in the browser application. The legacy provenance and SHA-256 snapshot is retained in `output/audio-backup-kokoro/audio-provenance.json`. Apache-2.0 text is included for reference; model licensing does not by itself establish linguistic quality or a separate copyright status for generated output.

Scripts are original AI-assisted drafts. The audio is synthetic, not a native human recording and not an impersonation of any named real person. Lin An and Chen Yu are fictional scenario characters. All clips still need educator review. No competitor audio, television footage or proprietary lesson content has been copied.

## Dictionary reference data

`content/reference-check.json` contains extracted entries from **CC-CEDICT contributors, via MDBG**, retrieved 4 October 2026. Source: https://www.mdbg.net/chinese/export/cedict/cedict_1_0_ts_utf-8_mdbg.txt.gz . Dictionary data is licensed under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/). Changes: exact-match subset selected, wrapped in JSON and associated with original phrase IDs and authored pinyin. Extracted/adapted dictionary data retains CC BY-SA 4.0. The evidence file is development material and is not included in the browser bundle. No source endorses this app.

Reference definitions were retained as evidence, not republished as a purportedly independent commercial dictionary. Curriculum explanations and scenario scripts were authored separately. Future content sourced or adapted from dictionaries must retain appropriate attribution and licensing per item.

## Local voice auditions and Sayo reactions

`public/audio-reactions/` extends the existing Kokoro `zf_001` female voice with 23 authored Sayo lines. Settings and per-file SHA-256 checksums are recorded in `content/voices/reaction-provenance.json`. These legacy reaction files are retained as backups and excluded from the new PWA precache.

The local-only auditions in `output/voice-compare/expressive-v2/`, `output/voice-compare/japanese-v3/`, `output/voice-compare/solid-v4/`, `output/voice-compare/base/`, `output/voice-compare/range-v5/`, `output/voice-compare/introvert-v6/` and `output/voice-compare/drawl-v7/` use [Fun-CosyVoice3-0.5B-2512](https://huggingface.co/FunAudioLLM/Fun-CosyVoice3-0.5B-2512), Apache-2.0, model revision `29e01c4e8d000f4bcd70751be16fa94bf3d85a18`, with [CosyVoice](https://github.com/QwenAudio/CosyVoice) code revision `074ca6dc9e80a2f424f1f74b48bdd7d3fea531cc`. The initial reference WAV was synthesized from the existing Kokoro female voice. The stronger reference and six candidate references were derived locally using CosyVoice; their lineage and hashes are recorded in the audition provenance. No recordings from the user's video links are used as a voice reference or bundled. Model weights and the Python runtime stay outside the application. Audition provenance includes the reference hash, instructions, speeds, seeds and output hashes. The deeper drawl direction was approved for local integration on October 4, 2026; individual generated clips still require listening and Mandarin pronunciation review.

## Local Qwen voice-design audition

`output/voice-base-review/` contains 18 local review WAVs from [Qwen3-TTS](https://github.com/QwenLM/Qwen3-TTS), Apache-2.0. The VoiceDesign model revision is `5ecdb67327fd37bb2e042aab12ff7391903235d3`; the 1.7B Base model revision is `fd4b254389122332181a7c3db7f27e918eec64e3`. Runtime: qwen-tts 0.1.1, PyTorch 2.6.0+cu124, Python 3.12.14. Model metadata and license declarations are retained with the local weights. The existing Apache-2.0 license text applies to these model packages.

Three original synthetic voices were designed from text. Each synthetic introduction was then reused as that candidate's sole reference for five shorter lines. No real-person recording was used as synthesis conditioning. Processing trims outer silence and limits peak gain without changing pitch, formants or tempo. These auditions are not part of the app or PWA. Per-file SHA-256, prompts, seeds and reference lineage are in the audition's `provenance.json`; the runtime dependency snapshot is `runtime-requirements.txt` in the same directory. Local OpenAI Whisper small and medium (MIT) provide advisory transcripts, not tone or pronunciation certification. The existing app voice remains installed.

The follow-up `output/voice-b-refinement/` uses the same pinned Qwen3-TTS Base model. Its experimental fixed speaker representation combines the selected synthetic B voice (weight 0.85) with the mean representation of three existing synthetic Sayo clips (weight 0.15); B's reference speech codes remain unchanged. These weights are internal model inputs, not perceptual mixture percentages. All source hashes, parameters and output hashes are recorded locally. Twelve new WAVs (eight refinement takes and four B controls) were generated; four earlier B controls are reused. Neither the installed library nor its provenance is replaced.

`output/voice-b-refinement-35/` adds eight local WAV auditions using a 0.65/0.35 B/current synthetic speaker representation. The same pinned model, reference speech codes, source lineage and absence of pitch/tempo processing apply. Prior audition files are retained for comparison, and neither blend is installed.

The local `output/voice-lower-register/` and `output/voice-lower-clean/` auditions derive from the prior 85/15 synthetic B/current takes. The first uses the existing local FFmpeg binary's Rubber Band filter at -1.25 semitones with formant preservation. The second uses SciPy (BSD-3-Clause) polyphase resampling at -1.75 semitones, with no time stretching or formant correction. Source and output hashes, measured pitch changes and advisory Whisper transcripts are retained per audition. Neither is installed or bundled with the PWA.

`output/voice-lower-options/` adds 16 WAVs using the same SciPy processing and synthetic source lineage: two further pitch options, 1 and 1.5 semitones below `voice-lower-clean` (total shifts -2.75 and -3.25). Each is rendered directly from the original blend, not by repeatedly processing an earlier audition. Local source hashes, output hashes, settings and Whisper screening transcripts are included. Production audio remains unchanged.

The final local shortlist `output/voice-final-showdown/` uses that same synthetic source and SciPy resampling. The new half-semitone option totals -2.25 semitones from the original blend; the -2.75 option is byte-identical to the prior one-semitone audition. Its provenance retains settings, hashes and advisory transcripts.

## User media

No external video library is bundled. Local media is supplied by its user and remains in that user's tab. No rights are granted by the app over imported material.

The explicitly labeled lowered-pitch drawl auditions use librosa (ISC) for a two-semitone pitch shift. This processing and measured loudness are recorded in their audition provenance; it does not certify accent or pronunciation quality.
# HSK study sources and original practice

The HSK study room links Chinese Testing International's official syllabus, demo and sample papers, and Beijing Language and Culture University Press's HSK Standard Course series. External material remains on its owner's site; no textbook pages or official exam questions are bundled. The 36 questions in `content/packs/hsk-reading.hsk.json` are original AI-assisted Kiyo practice, with human linguistic review pending. Vocabulary validation uses the existing MIT-licensed complete-hsk-vocabulary dataset's legacy levels. These practice results are not official HSK scores.

## CC-CEDICT (offline dictionary data)

- Source: CC-CEDICT, https://www.mdbg.net/chinese/dictionary?page=cc-cedict (MDBG and contributors).
- Licence: Creative Commons Attribution-ShareAlike 4.0 International (https://creativecommons.org/licenses/by-sa/4.0/).
- Used for: the tap-to-look-up dictionary in the Watch player and the reader.
- Changes made (scripts/build-dictionary.ts): numbered pinyin converted to tone marks; first three senses kept; variant-only entries dropped and erhua forms given their base word's meaning; measure words reformatted; HSK 3.0 levels added; common readings ordered first; data split into 256 files in public/dict/.
- The adapted data in public/dict/ is distributed under the same CC BY-SA 4.0 licence. Attribution is shown in Settings → "On this device" and recorded in public/dict/manifest.json.
