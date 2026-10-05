"""Screen local Qwen auditions and build a listening page; never installs audio."""
import hashlib
import html
import json
from pathlib import Path
import sys
import argparse

import librosa
import numpy as np
import soundfile as sf
import torch
import whisper

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT/'output/voice-base-review'
sys.stdout.reconfigure(encoding='utf-8')
report = json.loads((OUT/'provenance.json').read_text('utf-8'))
parser = argparse.ArgumentParser()
parser.add_argument('--model', choices=['small', 'medium'], default='small')
args = parser.parse_args()
torch.set_num_threads(4)
model = whisper.load_model(args.model, device='cuda', download_root=str(ROOT/'.models/whisper'))
hanzi = lambda s: ''.join(c for c in s if '\u4e00' <= c <= '\u9fff')
for clip in report['clips']:
    path = OUT/clip['file']
    assert hashlib.sha256(path.read_bytes()).hexdigest() == clip['sha256']
    signal, rate = sf.read(path)
    assert sf.info(path).format == 'WAV' and signal.ndim == 1 and rate == 24000
    assert np.isfinite(signal).all() and .001 < np.max(np.abs(signal)) < 1
    clip.setdefault('screenings', {})
    if 'screeningTranscript' in clip and not clip['screenings']:
        clip['screenings']['small'] = clip['screeningTranscript']
    if args.model not in clip['screenings']:
        audio = librosa.resample(signal.astype(np.float32), orig_sr=rate, target_sr=16000)
        result = model.transcribe(audio, language='zh', temperature=0, beam_size=5, condition_on_previous_text=False)
        clip['screenings'][args.model] = result['text']
    clip['screeningTranscript'] = clip['screenings'][args.model]
    clip['screeningExactText'] = hanzi(clip['screeningTranscript']) == hanzi(clip['text'])
    print(clip['file'], clip['screeningTranscript'], flush=True)
report['screening'] = f'Whisper {args.model}, Chinese, no expected-text prompt. Text mismatch is flagged; neither matches nor mismatches prove tone accuracy. Human listening remains required. Earlier transcripts are retained under screenings.'
report['installedManifestUnchanged'] = hashlib.sha256((ROOT/'src/audio-assets.json').read_bytes()).hexdigest() == report['installedManifestSha256']
assert report['installedManifestUnchanged']
(OUT/'provenance.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n','utf-8')

esc = html.escape
def audio(clip):
    return '<audio controls preload="none" aria-label="'+esc(clip['title']+' '+clip['text'])+'" src="'+esc(clip['file'])+'"></audio>'
def note(clip):
    status = 'Text screen matched; tones still need listening.' if clip['screeningExactText'] else 'Text screen differs — listen carefully before choosing.'
    return '<details><summary>'+status+'</summary><p>Automatic transcript: '+esc(clip['screeningTranscript'])+'</p></details>'
anchors = [c for c in report['clips'] if c['kind']=='anchor']
sections = []
for anchor in anchors:
    clips = [c for c in report['clips'] if c['candidate']==anchor['candidate'] and c['kind']!='anchor']
    sections.append('<section id="'+anchor['candidate']+'"><h2>'+anchor['candidate'].upper()+'. '+esc(anchor['title'])+'</h2><p>One newly designed synthetic voice. Every short line below reuses this exact anchor.</p><h3>Full introduction</h3>'+audio(anchor)+'<details><summary>Chinese script</summary><p lang="zh-CN">'+esc(anchor['text'])+'</p></details>'+note(anchor)+'<div class="clips">'+''.join('<article><h3 lang="zh-CN">'+esc(c['text'])+'</h3><p>'+esc(c['pinyin'])+'</p><p>'+esc(c['meaning'])+'</p>'+audio(c)+note(c)+'</article>' for c in clips)+'</div></section>')
manifest = json.loads((ROOT/'src/audio-assets.json').read_text('utf-8'))
baseline = next(v for k,v in manifest.items() if hanzi(k)==hanzi('来了？开始吧。'))
baseline_url = baseline.get('playful',next(iter(baseline.values())))
page = '''<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Sayo · New base voices</title>
<style>body{margin:0;background:#101c2b;color:#eef2f7;font:17px/1.55 system-ui}main{max-width:1040px;margin:auto;padding:32px 22px 80px}a{color:#b7d8fa}h1{font-size:clamp(30px,6vw,48px);line-height:1.1}h2{font-size:27px}h3{font-size:19px}p{max-width:75ch}section{border-top:1px solid #526379;margin-top:36px;padding-top:18px}.clips{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:28px}article{padding:12px 0}article p{margin:5px 0;color:#cad5e3}audio{width:100%;max-width:480px;margin:10px 0}summary{cursor:pointer;padding:8px 0;color:#cbd9eb}details p{font-size:15px}nav{display:flex;gap:24px;flex-wrap:wrap}a:focus-visible,summary:focus-visible{outline:3px solid #b7d8fa;outline-offset:5px}@media(max-width:660px){.clips{grid-template-columns:1fr}main{padding:22px 16px}}</style>
<main><a href="/#settings">Back to Kiyo</a><h1>Fuller voice. Same person.</h1><p>Three new base voices, generated locally with Qwen3-TTS. No pitch lowering, formant shifting or time stretching. Each candidate is a separate option; within it, all five short lines reuse one unchanged synthetic anchor.</p><p>Start with the greeting and praise. Does the low voice still sound like the same person when it becomes brighter? Then check the teaching lines for clear Mandarin.</p><p>This is an audition, not an installed update. The app voice is unchanged. The reference recordings informed broad delivery goals only; they were not used to clone a speaker.</p><nav><a href="#a">A · Full and smiling</a><a href="#b">B · Dry and playful</a><a href="#c">C · Warm with more range</a></nav><section><h2>Current app · comparison</h2><p lang="zh-CN">来了？开始吧。</p><audio controls preload="none" aria-label="Current app greeting" src="'''+esc(baseline_url)+'''"></audio></section>'''+''.join(sections)+'''<section><h2>What this test can tell us</h2><p>The files passed signal checks. Automatic transcripts are shown beside every take, including discrepancies. They cannot certify tones, naturalness or character identity: those still need your listening judgment.</p><p>The Base model reuses the voice but has no direct emotion-instruction input. These short takes test how it responds to the reference performance, wording and punctuation. They do not yet establish a complete six-mood library.</p><a href="provenance.json">Generation settings and file checks</a></section></main><script>document.querySelectorAll('audio').forEach(a=>a.addEventListener('play',()=>document.querySelectorAll('audio').forEach(b=>{if(a!==b)b.pause()})))</script></html>'''
(OUT/'index.html').write_text(page,'utf-8')
print('REVIEW READY',len(report['clips']),'clips; application manifest unchanged.',flush=True)
