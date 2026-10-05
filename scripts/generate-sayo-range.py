"""Small, unapproved vocal-range audition using only a synthetic reference."""
import os
os.environ['HF_HUB_OFFLINE'] = '1'
os.environ['TOKENIZERS_PARALLELISM'] = 'false'
import hashlib
import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

root = Path(__file__).resolve().parent.parent
sys.path[:0] = [str(root/'.tts'), str(root/'.tts/third_party/Matcha-TTS')]
import numpy as np
import soundfile as sf
import torch
import pyloudnorm as pyln
from cosyvoice.cli.cosyvoice import AutoModel

parser = argparse.ArgumentParser()
parser.add_argument('--spec', type=Path, help='Optional local audition specification.')
args = parser.parse_args()
spec = json.loads(args.spec.read_text('utf-8')) if args.spec else None
out = root/'output/voice-compare'/(spec['revision'] if spec else 'range-v5')
out.mkdir(exist_ok=True)
reference = root/'output/voice-compare/synthetic-reference-solid-v4.wav'
text = '来了？开始吧。声调呢？你又忘了？不错嘛！这次全对了！好，再来一次。'
directions = [
    ('low', 'Deep and firm', 'A solid low register, firm attacks, dry comic pauses.', '用非常低沉、浑厚结实、有胸腔共鸣的年轻女声说，态度坚定自信，低音有力量，不是气声。冷着脸调侃，停顿干脆，字音清晰。', .96),
    ('high', 'High and funny', 'A higher register, exaggerated surprise, cheeky timing.', '同一个成年女性，用高音区、夸张惊讶、活泼搞笑的语气说。声音突然扬高，俏皮地反问，像在逗朋友笑。不是小女孩，也不是甜美撒娇。发音清楚。', 1.02),
    ('switch', 'Low → high → low', 'Deep opening, a sudden comic jump, then a dry low finish.', '同一个年轻女性，音域跨度很大。来了开始吧用很低沉浑厚有力量的胸声。声调呢你又忘了突然升到很高的音区，夸张惊讶地搞笑反问。不错嘛这次全对了高声兴奋。好再来一次立刻回到低沉冷静。重音鲜明，反差强烈，汉语发音清楚。', 1.0),
]
if spec:
    text = spec['text']
    directions = [(m['id'],m['label'],m['description'],m['instruct'],m['speed']) for m in spec['takes']]
if not torch.cuda.is_available():
    raise RuntimeError('CUDA required for local generation.')
torch.set_num_threads(4)
model_dir = root/'.models/Fun-CosyVoice3-0.5B-2512'
model = AutoModel(model_dir=str(model_dir), fp16=False)
records = []
for id, label, description, direction, speed in directions:
    take = next((m for m in spec['takes'] if m['id'] == id), {}) if spec else {}
    spoken_text = take.get('text', text)
    pitch_shift = take.get('pitchShift', 0)
    path = out/f'{id}.wav'
    instruction = 'You are a helpful assistant. '+direction+'<|endofprompt|>'
    seed = spec['seed'] if spec else 5217  # Same seed and words isolate delivery.
    if not path.exists():
        torch.manual_seed(seed)
        torch.cuda.manual_seed_all(seed)
        parts = list(model.inference_instruct2(spoken_text, instruction, str(reference), stream=False, speed=speed, text_frontend=False))
        audio = torch.cat([p['tts_speech'].cpu() for p in parts], dim=1).squeeze().numpy()
        if not np.isfinite(audio).all() or np.max(np.abs(audio)) < .005:
            raise ValueError(f'Empty or invalid signal: {id}')
        nz = np.flatnonzero(np.abs(audio) > .005)
        pad = int(.08*model.sample_rate)
        audio = audio[max(0,nz[0]-pad):min(len(audio),nz[-1]+pad)]
        seconds = len(audio)/model.sample_rate
        if not 4 < seconds < 24:
            raise ValueError(f'Suspicious duration: {id} {seconds}')
        if pitch_shift:
            import librosa
            audio = librosa.effects.pitch_shift(audio, sr=model.sample_rate, n_steps=pitch_shift)
        meter = pyln.Meter(model.sample_rate)
        audio = pyln.normalize.loudness(audio,meter.integrated_loudness(audio),-16)
        audio *= min(1,.98/np.max(np.abs(audio)))
        sf.write(path,audio,model.sample_rate,subtype='PCM_16')
    audio, rate = sf.read(path)
    assert rate == 24000 and audio.ndim == 1 and np.isfinite(audio).all()
    assert .005 < np.max(np.abs(audio)) < .981
    records.append(dict(id=id,label=label,description=description,file=path.name,text=spoken_text,instruct=instruction,speed=speed,seed=seed,pitchShift=pitch_shift,seconds=len(audio)/rate,sha256=hashlib.sha256(path.read_bytes()).hexdigest()))
    print(f'Ready: {id}, {len(audio)/rate:.2f}s',flush=True)
manifest = dict(status='Unapproved performance targets; needs listening review. No video audio used.',generatedAt=datetime.now(timezone.utc).isoformat(),model=json.loads((model_dir/'revision.json').read_text()),codeRevision='074ca6dc9e80a2f424f1f74b48bdd7d3fea531cc',reference=str(reference.relative_to(root)),referenceSha256=hashlib.sha256(reference.read_bytes()).hexdigest(),format='mono 24 kHz PCM16 WAV',loudness='-16 LUFS target, peak capped at 0.98',clips=records)
(out/'provenance.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n','utf-8')
