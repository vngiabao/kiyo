"""Screen and present the selected-B refinement without installing it."""
import hashlib
import argparse
import html
import json
from pathlib import Path
import sys

import librosa
import numpy as np
import soundfile as sf
import torch
import whisper

ROOT = Path(__file__).resolve().parents[1]
parser = argparse.ArgumentParser()
parser.add_argument('--current-weight', type=float, choices=[.15,.35], default=.15)
args = parser.parse_args()
OUT = ROOT/('output/voice-b-refinement-35' if args.current_weight==.35 else 'output/voice-b-refinement')
sys.stdout.reconfigure(encoding='utf-8')
report = json.loads((OUT/'provenance.json').read_text('utf-8'))
torch.set_num_threads(4)
recognizer = whisper.load_model('medium', device='cuda', download_root=str(ROOT/'.models/whisper'))
# Orthographic equivalents only; never merge homophones such as 吗 and 嘛.
glyphs = str.maketrans({'認':'认', '點':'点', '開':'开', '錯':'错', '嗎':'吗', '夠':'够', '麼':'么', '書':'书'})
hanzi = lambda s: ''.join(c for c in s.translate(glyphs) if '\u4e00' <= c <= '\u9fff')
for row in report['clips']:
    for take in row['takes']:
        path = OUT/take['file']
        assert hashlib.sha256(path.read_bytes()).hexdigest() == take['sha256']
        signal,rate = sf.read(path)
        assert rate==24000 and sf.info(path).format=='WAV' and signal.ndim==1
        assert np.isfinite(signal).all() and .001 < np.max(np.abs(signal)) < 1
        if 'screeningTranscript' not in take:
            audio = librosa.resample(signal.astype(np.float32),orig_sr=rate,target_sr=16000)
            result = recognizer.transcribe(audio,language='zh',temperature=0,beam_size=5,condition_on_previous_text=False)
            take['screeningTranscript'] = result['text']
        take['screeningExactText'] = hanzi(take['screeningTranscript'])==hanzi(row['text'])
        print(row['id'],take['id'],take['screeningTranscript'],flush=True)
report['screening'] = 'Whisper medium, Chinese, no expected-text prompt. Punctuation ignored; 認/认, 點/点, 開/开, 錯/错, 嗎/吗, 夠/够, 麼/么 and 書/书 normalized as orthographic equivalents. Homophones such as 吗/嘛 remain mismatches. Raw transcripts retained. Not tone, naturalness or speaker-identity certification.'
assert hashlib.sha256((ROOT/'src/audio-assets.json').read_bytes()).hexdigest()==report['installedManifestSha256']
(OUT/'provenance.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n','utf-8')
esc = html.escape
sections = []
for row in report['clips']:
    cells=[]
    for take in row['takes']:
        title = {'b':'B · the starting point','previous':'Previous blend','refined':'More of the original' if args.current_weight==.35 else 'B + a touch of current'}[take['id']]
        status = 'Text check matched; listen for tones.' if take['screeningExactText'] else 'Text check differs; listen carefully.'
        cells.append('<div><h3>'+esc(title)+'</h3><audio controls preload="none" aria-label="'+esc(title+' '+row['text'])+'" src="'+esc(take['file'])+'"></audio><details><summary>'+status+'</summary><p>'+esc(take['screeningTranscript'])+'</p></details></div>')
    if row['current']:
        cells.append('<div><h3>Current app</h3><audio controls preload="none" aria-label="'+esc('Current app '+row['text'])+'" src="'+esc(row['current'])+'"></audio></div>')
    sections.append('<section id="'+row['id']+'"><h2 lang="zh-CN">'+esc(row['text'])+'</h2><p>'+esc(row['pinyin'])+'</p><p>'+esc(row['meaning'])+'</p><div class="takes">'+''.join(cells)+'</div></section>')
page='''<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Sayo · Refining B</title><style>
body{margin:0;background:#101c2b;color:#eef2f7;font:17px/1.55 system-ui}main{max-width:1120px;margin:auto;padding:32px 22px 80px}a{color:#b7d8fa}h1{font-size:clamp(30px,6vw,48px);line-height:1.1}h2{font-size:26px;margin-bottom:8px}h3{font-size:17px}p{max-width:78ch;margin:8px 0}.takes{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:26px}section{border-top:1px solid #526379;margin-top:30px;padding-top:16px}audio{width:100%;margin:8px 0}details{font-size:14px;color:#cad5e3}summary{cursor:pointer;padding:8px 0}a:focus-visible,summary:focus-visible{outline:3px solid #b7d8fa;outline-offset:4px}nav{display:flex;gap:24px;flex-wrap:wrap;margin:24px 0}@media(max-width:800px){.takes{grid-template-columns:1fr;gap:8px}main{padding:24px 16px}}
</style><main><a href="../voice-base-review/index.html#b">Back to the original B audition</a><h1>B, with a little familiar Sayo.</h1><p>B is the starting point you chose. This experiment keeps B dominant and adds a small amount of the current synthetic voice’s character. One fixed blend is reused throughout, with no pitch lowering or time stretching.</p><p>Compare the middle clip with B on the left, then the current app on the right. Start with the greeting, praise and tone reminder. The app voice is unchanged.</p><nav><a href="#welcome">Greeting</a><a href="#smug">Dry praise</a><a href="#celebrate">Bright praise</a><a href="#tones">Tone reminder</a><a href="#words">Pronunciation</a></nav>'''+''.join(sections)+'''<section><h2>Listening notes</h2><p>Does the blend retain B’s identity? Is the familiar depth there without losing her smile? Automatic text discrepancies are shown, but a matched transcript cannot prove correct tones or natural delivery.</p><details><summary>How this experiment was made</summary><p>The model’s speaker representation uses 85% B and 15% the average representation of three installed synthetic Sayo clips. These are internal weights, not percentages of what you will hear. B’s reference performance stays unchanged. The same text and random seed are used on each paired take. This is an experimental blend, not a proven emotion-control method.</p><p>Processing only trims outer silence and keeps peak headroom. No real-person recordings were used. Human listening approval is still needed before any library replacement.</p><a href="provenance.json">Generation settings and checks</a></details></section></main><script>document.querySelectorAll('audio').forEach(a=>a.addEventListener('play',()=>document.querySelectorAll('audio').forEach(b=>{if(a!==b)b.pause()})))</script></html>'''
if args.current_weight==.35:
    page = page.replace('Sayo · Refining B','Sayo · B with more original')
    page = page.replace('B, with a little familiar Sayo.','B, a little deeper.')
    page = page.replace('B is the starting point you chose. This experiment keeps B dominant and adds a small amount of the current synthetic voice’s character. One fixed blend is reused throughout, with no pitch lowering or time stretching.', 'B stays the starting point. This version brings in more of the original voice, aiming for a pitch between the previous blend and the original. One fixed blend is reused throughout, without pitch lowering or time stretching. Listen to judge whether it lands in that middle ground.')
    page = page.replace('Compare the middle clip with B on the left, then the current app on the right.', 'Compare the new middle clip with the previous blend on the left, then the original app voice on the right.')
    page = page.replace('85% B and 15%', '65% B and 35%')
    page = page.replace('Back to the original B audition','Back to the previous blend').replace('../voice-base-review/index.html#b','../voice-b-refinement/index.html')
(OUT/'index.html').write_text(page,'utf-8')
print('DONE: 8 paired comparisons; app manifest unchanged.',flush=True)
