# Sayo's voice: design prompt

Use with the voice-upgrade task (`prompts/voice-upgrade.md`). Paste the box into the work chat. It contains the voice description, the exact CosyVoice instructions per mood, a reference script, and how to check quality.

```
Design Sayo's voice: ONE voice for the whole app, used in different moods. This is a personal project and the target is an Ado-style voice (the Japanese singer): get as close to her vocal character as you can from the description. The one limit: don't use Ado's actual recordings (songs, clips, interviews) as reference audio for cloning. Build it from text instructions and designed reference clips.

WHO SHE IS (personality the voice must carry)
Sayo (小夜, "the night") has Ado's energy: a shy, introverted person off-stage who becomes ferocious when she performs. Cool, exacting, few words, dry humour, rebellious edge, sincere underneath. She swings from a near-whisper to a full-power, gritty burst in one line. She never sounds childish, sweet or "cute idol".

TIMBRE (Ado-style, the same in every mood)
- Female, early 20s, low-mid chest voice with a strong, dark core: deeper and fuller than typical TTS voices.
- Natural grit/rasp that comes forward when she pushes (vocal-fry growl on emphasis), breathy and airy when quiet.
- Very sharp attacks and crisp consonants (zh/ch/sh, j/q/x, z/c/s), clipped and punchy endings, wide dynamic range.
- Fast emotional switches: deadpan murmur → sudden intensity → back to cool, within a sentence or two.
- Close-mic, intimate, dry studio sound: no reverb, no music.
- Not robotic, not newsreader-formal, not sweet, not high-pitched idol.

PRONUNCIATION
- Standard Mandarin (Putonghua) with clear, correct tones in ALL lesson audio: tones 1–4 fully realised, neutral tones light, 一/不 and third-tone changes applied naturally.
- Sayo's personal reaction lines (and casual dialogue if I like it) may carry a light-to-moderate Japanese-speaker accent in Mandarin: Japanese-style syllable timing, softer r, flatter neutral tones, the way a Japanese singer speaking Chinese would sound. Keep the four tones recognisable. Make it a separate mood "cool-accent" so I can compare and choose how much to keep.

MOODS (same timbre; CosyVoice instruct text in brackets)
- clear (DEFAULT for lessons and tone drills): calm, precise, medium-slow, every tone very clear.
  [用清晰、标准、平稳的普通话，语速稍慢，每个声调都很准确，声音低沉干净]
- cool: low, unhurried, a little bored, slight downward finish.
  [用冷静、低沉、略带沙哑、有点慵懒的语气说，句尾轻轻下沉]
- intense: sudden on-stage power, louder, faster, gritty edge on the stressed word. For praise and level-ups.
  [用突然爆发、充满力量、带点沙哑和狠劲、干脆有力的语气说，重音加强，像在舞台上喊出来，但发音清楚]
- growl (level-ups and big moments only): short rough rock-style shout on the key word, then an instant drop back to cool.
  [前半句低声冷静，关键词突然用沙哑有力的嗓音爆发出来，然后马上恢复冷淡]
- whisper: close, breathy, almost secretive. For quiet hints and "rest" moments.
  [贴近耳边、气声很重、几乎是悄悄话的语气说]
- soft: quiet, gentle, a little shy, warm. For encouragement after mistakes.
  [用轻柔、温和、有点害羞但真诚的语气小声说]
- deadpan: flat, dry, minimal pitch movement except the tones; dry humour.
  [用面无表情、平淡、带一点冷幽默的语气说]
- playful: lighter, a small smile in the voice, a bit quicker. For casual chat lines.
  [用轻松、带点笑意、自然随意的语气说]
- cool-accent (OPTIONAL): like cool, with a Japanese-speaker accent in Mandarin; tones still recognisable.
  [用冷静低沉的语气说，带一点日本人说中文的口音，但声调要能听清楚]

REFERENCE SCRIPT (generate in the base timbre, about 15 seconds, to lock her voice)
来了？开始吧。今天先学十个字，一个一个来。声调要准——妈、麻、马、骂。……不错嘛。再来一次——你，可以的！

STEPS
1. Generate 6 candidate base timbres reading the reference script, ranging from "cool and husky" to "maximum Ado-style grit and power". Save them in output/voice-compare/base/ and pick none yourself.
2. Add them to the comparison page (output/voice-compare/index.html) with each mood applied to:
   妈 麻 马 骂 · 你好 · 我没听懂 · 一共三十五块 · 你想吃米饭还是面？ · 来了？开始吧。 · 声调呢？ · 太棒了！ · 没关系，再试试。
3. Stop and let me choose: one base timbre, and whether "cool-accent" stays.
4. Lock the chosen timbre: save its reference clip + transcript as content/voices/sayo-ref.wav / .txt and record every mood's instruct text, speed and seed in content/voices/roster.json, so all future audio sounds the same.

QUALITY CHECKS (before generating the full app)
- Tones: the four 妈/麻/马/骂 clips must be clearly distinguishable in the "clear" mood. If not, reduce huskiness/speed and regenerate.
- Consistency: the same sentence in two different sessions should sound like the same person.
- No artefacts: no clipped starts, no breaths longer than ~0.3 s, no mumbled final syllables.
- Loudness about -16 LUFS; leading/trailing silence trimmed.
```

## Range refinement (October 4, 2026)

The low register should be deeper, stronger and full-bodied. The high register should rise noticeably for exaggerated surprise and comic reactions. Preserve one adult female identity through sudden low-to-high-to-low switches. High comic moments are welcome; this updates the earlier blanket instruction against high pitch. Keep standard Mandarin and stable tone delivery in lessons. The linked video at 3:15 is a user-supplied performance reference, not a cloning source; its audio was not accessible during this pass.

Focused audition: `output/voice-compare/range-v5/`, three instruction-driven takes of identical Mandarin text. No digital pitch shift. Performance labels are targets, pending listening review.

## Introverted humor refinement (October 4, 2026)

Favor reserved, awkwardly funny delivery: short hesitation, deadpan teasing, an embarrassed compliment, a brief surprised pitch jump, then composure. Retain an adult, solid low-mid female timbre. Make the Japanese-speaker inflection more noticeable in reactions, while preserving intelligible Mandarin tones. Lesson delivery stays standard Mandarin. Compare the three unapproved takes in `output/voice-compare/introvert-v6/`; exact instructions live in `content/voices/introvert-v6.json`. These are synthesis targets, not verified accent or personality claims.

## Drawl and dry teasing refinement (October 4, 2026)

Prioritize a deeper, reserved, playful delivery with Japanese-speaker inflection. Stretch selected final vowels (especially reaction particles 啊 and 嘛), leaving the surrounding speech conversational. Use short startled reactions followed by immediate dry composure. Treat the supplied breath percentages, dB jumps and BPM as descriptive suggestions, not calibrated synthesis controls. Do not put unrecognized acting tags into the spoken text.

`content/voices/drawl-v7.json` compares natural pitch, a clearly labeled two-semitone downward pitch shift, and a brief breath/emphasis reaction using supported model tokens. All are unapproved, reaction-only auditions. No playlist audio was accessible or used. Pronunciation and performance still require listening review.
