"""Decode every installed Sayo clip and build the owner's listening checklist."""
import hashlib
import html
import json
import random
import re
from pathlib import Path
import numpy as np
import soundfile as sf
import pyloudnorm as pyln
from audio_postprocess import levels

root = Path(__file__).resolve().parent.parent
provenance = json.loads((root/'content/voices/sayo-library-provenance.json').read_text('utf-8'))
scripts = json.loads((root/'content/audio-scripts.json').read_text('utf-8'))
key = lambda s: re.sub(r'[\s，。！？,.!?、]', '', s)
catalog = {key(s['text']): s for s in scripts}
checks = []
for clip in provenance['clips']:
    path = root/clip['file']
    signal, rate = sf.read(path)
    assert hashlib.sha256(path.read_bytes()).hexdigest() == clip['sha256'], path
    assert rate == 24000 and signal.ndim == 1 and np.isfinite(signal).all(), path
    peak = float(max(abs(signal)))
    assert .005 < peak < 1 and len(signal)/rate >= .23, path
    _, _, loudness, block = levels(path)
    assert abs(loudness+16) <= 1, (path,loudness)
    checks.append(dict(file=clip['file'],seconds=len(signal)/rate,peak=peak,lufs=loudness,shortMeterWindow=block < .4))
report = dict(checked=len(checks),bytes=sum((root/c['file']).stat().st_size for c in checks),checks=checks,status='File integrity and signal checks passed. Linguistic quality is not machine-certified.')
(root/'content/voices/sayo-audio-check.json').write_text(json.dumps(report,indent=2)+'\n','utf-8')

mono = [c for c in provenance['clips'] if len(re.findall(r'[\u4e00-\u9fff]',c['text'])) == 1]
pool = [c for c in provenance['clips'] if c not in mono]
selected = random.Random(20261004).sample(pool,min(20,len(pool)))
esc = html.escape
def item(c):
    s = catalog[key(c['text'])]
    url = '/'+c['file'].removeprefix('public/')
    return '<article class="sample"><strong lang="zh-CN">'+esc(c['text'])+'</strong><span>'+esc(s.get('pinyin',''))+'</span><span>'+esc(s.get('meaning',''))+'</span><span>'+esc(c['mood'])+' · '+f'{c["seconds"]:.2f}s'+'</span><audio controls preload="none" aria-label="'+esc(c['text']+' '+c['mood'])+'" src="'+esc(url)+'"></audio><small>'+esc(Path(c['file']).name)+'</small></article>'
style = re.search(r'<style>(.*?)</style>',(root/'output/voice-compare/index.html').read_text('utf-8'),re.S).group(1)
page = '<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Sayo · Listening check</title><style>'+style+'.review-clips{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:22px}.sample{border-top:1px solid var(--rule);min-width:0}audio{width:100%;max-width:420px}.sample small{overflow-wrap:anywhere;color:var(--muted)}@media(max-width:640px){.review-clips{grid-template-columns:1fr}}</style><main><a href="/">Back to Kiyo</a><h1>Sayo, across the course.</h1><p>The deeper voice is installed locally. Listen for correct words and tones, a consistent identity, and clean endings. Report a filename and what sounds off; no need to approve the whole library again.</p><p>'+str(len(checks))+' files · '+f'{report["bytes"]/1024/1024:.2f} MiB'+' · all file checks passed. Pronunciation still needs human listening.</p><h2>20 sample clips</h2><div class="review-clips">'+''.join(map(item,selected))+'</div><h2>Every single-syllable clip</h2><p>'+str(len(mono))+' clips across Clear, Cool and Playful. Pay particular attention to 妈 / 麻 / 马 / 骂 and rising versus dipping tones.</p><div class="review-clips">'+''.join(map(item,mono))+'</div></main><script>document.querySelectorAll("audio").forEach(a=>a.addEventListener("play",()=>document.querySelectorAll("audio").forEach(b=>{if(a!==b)b.pause()})))</script></html>'
out = root/'output/voice-review'
out.mkdir(exist_ok=True)
(out/'index.html').write_text(page,'utf-8')
(out/'listening-list.json').write_text(json.dumps(dict(randomClips=selected,singleSyllables=mono),ensure_ascii=False,indent=2)+'\n','utf-8')
print(f'{len(checks)} checked; {report["bytes"]:,} bytes; 20 sample clips + {len(mono)} single-syllable clips.')
