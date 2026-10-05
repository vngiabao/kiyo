"""Create a firmer synthetic performance reference; no real-person recordings."""
import os
os.environ['HF_HUB_OFFLINE'] = '1'
os.environ['TOKENIZERS_PARALLELISM'] = 'false'
import hashlib
import json
import sys
from pathlib import Path
root = Path(__file__).resolve().parent.parent
sys.path[:0] = [str(root/'.tts'), str(root/'.tts/third_party/Matcha-TTS')]
import numpy as np
import soundfile as sf
import torch
import pyloudnorm as pyln
from cosyvoice.cli.cosyvoice import AutoModel

out = root/'output/voice-compare'
reference = out/'synthetic-reference.wav'
target = out/'synthetic-reference-solid-v4.wav'
text = '来了？开始吧。听清楚，再说一遍。不错嘛，这次有进步。声调呢？别急，再来。好，这就对了！'
instruction = 'You are a helpful assistant. 请用低沉、厚实、有力量的年轻女声说话，态度自信，咬字干脆，带一点调侃的笑意，像一个有气场又幽默的动画角色。<|endofprompt|>'
if target.exists():
    raise RuntimeError('Reference already exists; use a new version rather than overwriting it.')
if not torch.cuda.is_available():
    raise RuntimeError('CUDA required for this local audition.')
torch.set_num_threads(4)
torch.manual_seed(2093)
torch.cuda.manual_seed_all(2093)
model_dir = root/'.models/Fun-CosyVoice3-0.5B-2512'
model = AutoModel(model_dir=str(model_dir), fp16=False)
parts = list(model.inference_instruct2(text, instruction, str(reference), stream=False, speed=.96, text_frontend=False))
audio = torch.cat([p['tts_speech'].cpu() for p in parts], dim=1).squeeze().numpy()
if not np.isfinite(audio).all() or not 5 < len(audio)/model.sample_rate < 28 or np.max(np.abs(audio)) < .005:
    raise ValueError('Reference failed duration or signal check.')
meter = pyln.Meter(model.sample_rate)
audio = pyln.normalize.loudness(audio, meter.integrated_loudness(audio), -16)
audio *= min(1, .98/np.max(np.abs(audio)))
sf.write(str(target), audio, model.sample_rate, subtype='PCM_16')
target.with_suffix('.txt').write_text(text,'utf-8')
target.with_suffix('.json').write_text(json.dumps({'text':text,'instruction':instruction,'seed':2093,'speed':.96,'source':reference.name,'sourceSha256':hashlib.sha256(reference.read_bytes()).hexdigest(),'sha256':hashlib.sha256(target.read_bytes()).hexdigest(),'model':json.loads((model_dir/'revision.json').read_text()),'status':'Synthetic reference derived from the existing synthetic voice; unapproved audition.'},ensure_ascii=False,indent=2),'utf-8')
print(f'Reference ready: {len(audio)/model.sample_rate:.2f}s',flush=True)
