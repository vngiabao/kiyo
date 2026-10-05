"""Existing female voice: new reaction clips, review baselines and synthetic anchor.

Run with .audio-env/Scripts/python.exe. Does not replace the lesson manifest.
"""
import hashlib
import json
from pathlib import Path
import numpy as np
import soundfile as sf
from misaki import zh
from kokoro_onnx import Kokoro

root = Path(__file__).resolve().parent.parent
out = root / 'output/voice-compare'
out.mkdir(parents=True, exist_ok=True)
reactions = root / 'public/audio-reactions'
reactions.mkdir(exist_ok=True)
g2p = zh.ZHG2P(version='1.1')
model = Kokoro(str(root/'.models/kokoro-v1.1-zh.onnx'), str(root/'.models/voices-v1.1-zh.bin'), vocab_config=str(root/'.models/config.json'))

def synth(text, target):
    if target.exists():
        return
    phonemes, _ = g2p(text)
    tokens = model.tokenizer.tokenize(phonemes)
    audio = model.sess.run(None, {
        'input_ids': np.array([[0, *tokens, 0]], dtype=np.int64),
        'style': np.array(model.get_voice_style('zf_001')[len(tokens)], dtype=np.float32),
        'speed': np.array([1.0], dtype=np.float32),
    })[0].squeeze()
    if not np.isfinite(audio).all() or len(audio) < 2400 or np.max(np.abs(audio)) < .005:
        raise ValueError(f'Invalid synthesis: {text}')
    sf.write(str(target), audio, 24000)
    print(target.name, flush=True)

sentences = ['妈 麻 马 骂', '你好', '我没听懂', '可以再说一次吗？', '一共三十五块', '你想吃米饭还是面？', '来了？开始吧。', '声调呢？', '太棒了！', '不错嘛。', '没关系，再试试。', '升级了！']
(out/'sentences.json').write_text(json.dumps(sentences, ensure_ascii=False), 'utf-8')
for i, text in enumerate(sentences):
    synth(text, out/f'baseline-{i}.mp3')

anchor = '你好，我是小夜。今天我们慢慢来。先听清楚，再说一遍。没关系，不用着急。每个声调都要说清楚。准备好了，我们就开始吧。'
synth(anchor, out/'synthetic-reference.wav')
(out/'synthetic-reference.txt').write_text(anchor, 'utf-8')

manifest = {}
provenance = []
for i, text in enumerate(json.loads((root/'content/voices/reactions.json').read_text('utf-8'))):
    target = reactions/f'sayo-{i:02d}.mp3'
    synth(text, target)
    info = sf.info(str(target))
    if info.duration < .1 or info.duration > 15:
        raise ValueError(f'Unexpected duration: {target}')
    manifest[text] = {'zf_001': f'/audio-reactions/{target.name}'}
    provenance.append({'text': text, 'file': str(target.relative_to(root)), 'sha256': hashlib.sha256(target.read_bytes()).hexdigest(), 'seconds': info.duration})
(root/'src/audio-reactions.json').write_text(json.dumps(manifest, ensure_ascii=False, indent=2), 'utf-8')
(root/'content/voices/reaction-provenance.json').write_text(json.dumps({'generatedOn': '2026-10-04', 'settings': {'sampleRate': 24000, 'speed': 1.0, 'format': 'MP3 mono'}, 'model': 'Kokoro v1.1 zh ONNX', 'voice': 'zf_001', 'note': 'Existing voice, temporary until voice review approval. No real-person reference.', 'files': provenance}, ensure_ascii=False, indent=2), 'utf-8')
