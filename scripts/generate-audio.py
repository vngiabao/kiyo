"""Build-time only. Original scripts, locally synthesized with Apache-2.0 Kokoro.
Requires .models files described in README. No learner audio or data is read.
"""
import json
from pathlib import Path
import soundfile as sf
import numpy as np
from misaki import zh
from kokoro_onnx import Kokoro

root = Path(__file__).resolve().parent.parent
models = root / '.models'
out = root / 'public' / 'audio'
out.mkdir(parents=True, exist_ok=True)
g2p = zh.ZHG2P(version='1.1')
kokoro = Kokoro(str(models / 'kokoro-v1.1-zh.onnx'), str(models / 'voices-v1.1-zh.bin'), vocab_config=str(models / 'config.json'))
scripts = json.loads((root / 'content' / 'audio-scripts.json').read_text(encoding='utf-8'))
manifest = {}
for i, entry in enumerate(scripts):
    # Two model voices provide controlled variation, not native-speaker transfer evidence.
    for voice in ['zf_001', 'zm_010']:
        name = f"{entry['id']}-{voice}.mp3"
        target = out / name
        if not target.exists():
            phonemes, _ = g2p(entry['text'])
            # Pin input dtypes explicitly: kokoro-onnx 0.4.7 uses an int speed for
            # input_ids exports, while this model requires float32.
            tokens = kokoro.tokenizer.tokenize(phonemes)
            if len(tokens) > 500:
                raise ValueError('Split the script into shorter reviewed segments.')
            inputs = {'input_ids': np.array([[0, *tokens, 0]], dtype=np.int64),
                      'style': np.array(kokoro.get_voice_style(voice)[len(tokens)], dtype=np.float32),
                      'speed': np.array([1.0], dtype=np.float32)}
            samples = kokoro.sess.run(None, inputs)[0].squeeze()
            sample_rate = 24000
            sf.write(str(target), samples, sample_rate, format='MP3', subtype='MPEG_LAYER_III')
        manifest.setdefault(entry['text'], {})[voice] = '/audio/' + name
    print(f"{i+1}/{len(scripts)} synthesized", flush=True)
(root / 'src' / 'audio-assets.json').write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding='utf-8')
# Assemble the original dialogue from alternating voices, with a short turn gap.
scene_ids = ['scene-8', 'scene-9', 'scene-10', 'scene-11']
scene_text = ' '.join(next(s['text'] for s in scripts if s['id'] == i) for i in scene_ids)
parts = []
for i, key in enumerate(scene_ids):
    voice = 'zf_001' if i % 2 == 0 else 'zm_010'
    samples, rate = sf.read(str(out / f'{key}-{voice}.mp3'))
    parts.extend([samples, np.zeros(int(rate * 0.3))])
sf.write(str(out / 'coffee-dialogue.mp3'), np.concatenate(parts), 24000, format='MP3', subtype='MPEG_LAYER_III')
manifest[scene_text] = {'zf_001': '/audio/coffee-dialogue.mp3', 'zm_010': '/audio/coffee-dialogue.mp3'}
(root / 'src' / 'audio-assets.json').write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding='utf-8')
print('Wrote audio manifest', flush=True)
