"""Local auditions only. Never changes the app's voice manifest."""
import os
os.environ['HF_HUB_OFFLINE'] = '1'
os.environ['TOKENIZERS_PARALLELISM'] = 'false'
import hashlib
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

out = root/'output/voice-compare'
roster = json.loads((root/'content/voices/roster.json').read_text('utf-8'))
sentences = json.loads((out/'sentences.json').read_text('utf-8'))
model_dir = root/'.models/Fun-CosyVoice3-0.5B-2512'
if not torch.cuda.is_available():
    raise RuntimeError('CUDA is not available; refusing to silently use a slow CPU run.')
torch.set_num_threads(4)
model = AutoModel(model_dir=str(model_dir), fp16=False)
clips = out / roster['revision']
clips.mkdir(exist_ok=True)
files = []
for mood in roster['moods']:
    for i, text in enumerate(sentences):
        target = clips/f'{mood["id"]}-{i}.wav'
        seed = 1986 + i
        if not target.exists():
            torch.manual_seed(seed)
            torch.cuda.manual_seed_all(seed)
            parts = list(model.inference_instruct2(text, mood['instruct'], str(root/mood['reference']), stream=False, speed=mood['speed'], text_frontend=False))
            audio = torch.cat([p['tts_speech'].cpu() for p in parts], dim=1).squeeze().numpy()
            if not np.isfinite(audio).all() or np.max(np.abs(audio)) < .005:
                raise ValueError(f'Empty or invalid clip: {target.name}')
            nz = np.flatnonzero(np.abs(audio) > .005)
            pad = int(.08 * model.sample_rate)
            audio = audio[max(0,nz[0]-pad):min(len(audio),nz[-1]+pad)]
            duration = len(audio)/model.sample_rate
            if not .25 < duration < max(8,len(text)*.9):
                raise ValueError(f'Suspicious duration {duration:.2f}: {target.name}')
            meter = pyln.Meter(model.sample_rate, block_size=min(.4, duration/2))
            audio = pyln.normalize.loudness(audio, meter.integrated_loudness(audio), -16)
            peak = np.max(np.abs(audio))
            if peak > .98:
                audio *= .98/peak
            sf.write(str(target), audio, model.sample_rate, subtype='PCM_16')
        info = sf.info(str(target))
        files.append({'file':target.name, 'text':text, 'mood':mood['id'], 'seed':seed, 'seconds':info.duration, 'sampleRate':info.samplerate, 'sha256':hashlib.sha256(target.read_bytes()).hexdigest()})
        print(f'READY {target.name} {info.duration:.2f}s',flush=True)

provenance = {'generatedAt':datetime.now(timezone.utc).isoformat(), 'model':json.loads((model_dir/'revision.json').read_text()), 'referenceSha256':hashlib.sha256((root/roster['reference']).read_bytes()).hexdigest(), 'roster':roster, 'files':files, 'status':'Unapproved auditions; linguistic and timbre review pending.'}
(clips/'provenance.json').write_text(json.dumps(provenance,ensure_ascii=False,indent=2),'utf-8')
print(f'All {len(files)} audition clips ready. App voices unchanged.',flush=True)
