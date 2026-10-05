"""Isolated delivery/processing comparison; never installs application audio."""
import os
os.environ['HF_HUB_OFFLINE'] = '1'
os.environ['TOKENIZERS_PARALLELISM'] = 'false'
import hashlib
import html
import json
import random
import sys
from datetime import datetime, timezone
from pathlib import Path

import librosa
import numpy as np
import soundfile as sf
import torch
import whisper

root = Path(__file__).resolve().parent.parent
sys.stdout.reconfigure(encoding='utf-8')
sys.stderr.reconfigure(encoding='utf-8')
sys.path[:0] = [str(root/'.tts'), str(root/'.tts/third_party/Matcha-TTS')]
from cosyvoice.cli.cosyvoice import AutoModel
from audio_postprocess import normalize_clip

out = root/'output/voice-delivery-audition'
out.mkdir(exist_ok=True)
cache = out/'work'
cache.mkdir(exist_ok=True)
manifest_path = root/'src/audio-assets.json'
manifest_hash = hashlib.sha256(manifest_path.read_bytes()).hexdigest()
manifest = json.loads(manifest_path.read_text('utf-8'))
reference = root/'content/voices/sayo-source.wav'
reference_hash = hashlib.sha256(reference.read_bytes()).hexdigest()
instruction = 'You are a helpful assistant. 年轻成年女声，笑着和熟悉的朋友说标准普通话，轻松俏皮，有一点逗趣。起声从容，后半句自然明亮起来。每个字清楚完整。<|endofprompt|>'
lines = [
    ('来了？开始吧。', 'Lái le? Kāishǐ ba.', 'You’re here? Let’s begin.', 'playful'),
    ('声调呢？', 'Shēngdiào ne?', 'What about the tones?', 'deadpan'),
    ('认真一点。开始吧。', 'Rènzhēn yìdiǎn. Kāishǐ ba.', 'Focus a little. Let’s begin.', 'cool'),
    ('不错嘛。', 'Bú cuò ma.', 'Not bad at all.', 'deadpan'),
    ('什么', 'shénme', 'what', 'clear'),
    ('我们吃米饭。', 'Wǒmen chī mǐfàn.', 'We eat rice.', 'clear'),
]
torch.set_num_threads(4)
model_dir = root/'.models/Fun-CosyVoice3-0.5B-2512'
model = AutoModel(model_dir=str(model_dir), fp16=False)
records = []
for index, (text, pinyin, meaning, mood) in enumerate(lines):
    # Use punctuation-insensitive lookup only to find the already-installed baseline.
    key = lambda s: ''.join(c for c in s if '\u4e00' <= c <= '\u9fff')
    matching = next(k for k in manifest if key(k) == key(text))
    baseline = manifest[matching].get(mood, manifest[matching]['clear'] if 'clear' in manifest[matching] else next(iter(manifest[matching].values())))
    row = dict(text=text, pinyin=pinyin, meaning=meaning, baseline=baseline, takes=[])
    seed = 9400+index
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    torch.cuda.manual_seed_all(seed)
    chunks = list(model.inference_instruct2(text, instruction, str(reference), stream=False, speed=.98, text_frontend=False))
    raw = torch.cat([c['tts_speech'].cpu() for c in chunks], dim=1).squeeze().numpy()
    assert np.isfinite(raw).all() and np.max(np.abs(raw)) > .005
    active = np.flatnonzero(np.abs(raw) > .005)
    raw = raw[max(0,active[0]-1920):min(len(raw),active[-1]+1920)]
    assert .23 <= len(raw)/24000 <= 15, text
    for label, shift in [('same-depth', -2), ('natural-pitch', 0)]:
        signal = librosa.resample(raw, orig_sr=24000*2**(shift/12), target_sr=24000, res_type='soxr_hq') if shift else raw.copy()
        path = out/f'{index+1:02d}-{label}.wav'
        sf.write(path, signal, 24000, subtype='PCM_16')
        details = normalize_clip(path, cache)
        decoded, rate = sf.read(path)
        # The shared library normalizer writes MP3. Auditions are real PCM WAVs.
        sf.write(path, decoded, rate, subtype='PCM_16')
        assert rate == 24000 and decoded.ndim == 1 and np.isfinite(decoded).all()
        assert .005 < np.max(np.abs(decoded)) < 1
        assert abs(details['lufs']+16) <= 1
        row['takes'].append(dict(id=label, file=path.name, seed=seed, pitchShift=shift, speed=.98, seconds=len(decoded)/rate, sha256=hashlib.sha256(path.read_bytes()).hexdigest(), **details))
    records.append(row)
    print('GENERATED '+text, flush=True)

del model
torch.cuda.empty_cache()
recognizer = whisper.load_model('small', device='cuda', download_root=str(root/'.models/whisper'))
for row in records:
    for take in row['takes']:
        signal, _ = librosa.load(out/take['file'], sr=16000)
        take['screeningTranscript'] = recognizer.transcribe(signal, language='zh', temperature=0, beam_size=5, condition_on_previous_text=False)['text']
        print(row['text'], take['id'], take['screeningTranscript'], flush=True)
receipt = dict(generatedAt=datetime.now(timezone.utc).isoformat(), status='Audition only. Not installed; human listening required.', reference=str(reference.relative_to(root)), referenceSha256=reference_hash, instruction=instruction, model=json.loads((model_dir/'revision.json').read_text()), sourceVideo='https://www.youtube.com/watch?v=y-JLOQOAay0', sourceEvidence='Automatic transcript read; video audio extraction timed out. Delivery targets come from the owner’s descriptions. No direct acoustic analysis or real-person reference audio used.', screening='Whisper small without expected-text prompting; not pronunciation certification.', installedManifestSha256=manifest_hash, clips=records)
(out/'provenance.json').write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n','utf-8')
esc = html.escape
blocks = []
for row in records:
    controls = [('Current app', row['baseline'])] + [(('Smiling · same depth' if t['id']=='same-depth' else 'Same take · natural pitch'), t['file']) for t in row['takes']]
    warning = '<p>Pronunciation concern: automatic screening flagged this line in one or both new takes. Keep it out of lessons pending repair and listening review.</p>' if row['text'] in ['认真一点。开始吧。', '不错嘛。'] else ''
    blocks.append('<section><h2 lang="zh-CN">'+esc(row['text'])+'</h2><p>'+esc(row['pinyin'])+'</p><p>'+esc(row['meaning'])+'</p>'+warning+'<div class="takes">'+''.join('<div><h3>'+esc(label)+'</h3><audio controls preload="none" aria-label="'+esc(label+' '+row['text'])+'" src="'+esc(url)+'"></audio></div>' for label,url in controls)+'</div></section>')
page = '<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>Sayo · Delivery audition</title><style>body{background:#0f1b2a;color:#eef2f5;font:17px/1.6 system-ui;margin:0}main{max-width:1120px;margin:auto;padding:32px 20px}a{color:#b8d4f4}section{border-top:1px solid #43536a;padding:24px 0}h2,p{margin:8px 0}.takes{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:24px}h3{font-size:16px}audio{width:100%}@media(max-width:760px){.takes{grid-template-columns:1fr;gap:8px}}</style><main><a href="/#companion">Back to Sayo</a><h1>Smile first. Compare the depth.</h1><p>Six short comparisons. The two new options share exactly the same generated performance: one is lowered two semitones, one is untouched. Both use Sayo’s existing synthetic reference and simpler acting directions.</p><p>Audition only: the app voice is unchanged. The interview transcript was accessible, but its audio was not extracted; this is not a measured match to the video. Judge friendliness, clean consonants and correct tones by ear.</p>'+''.join(blocks)+'</main><script>document.querySelectorAll("audio").forEach(a=>a.addEventListener("play",()=>document.querySelectorAll("audio").forEach(b=>{if(a!==b)b.pause()})))</script></html>'
(out/'index.html').write_text(page,'utf-8')
assert hashlib.sha256(manifest_path.read_bytes()).hexdigest() == manifest_hash, 'Installed voice changed during audition'
print('DONE: 12 new clips; installed manifest unchanged.', flush=True)
