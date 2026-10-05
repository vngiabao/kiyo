"""Lower the selected previous performance, without another identity regeneration."""
from datetime import datetime, timezone
import hashlib
import html
import json
from pathlib import Path
import subprocess
import sys

import imageio_ffmpeg
import librosa
import numpy as np
import pyloudnorm as pyln
import soundfile as sf

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT/'output/voice-b-refinement'
OUT = ROOT/'output/voice-lower-register'
SHIFT = -1.25
FACTOR = 2**(SHIFT/12)
sys.stdout.reconfigure(encoding='utf-8')
OUT.mkdir(parents=True, exist_ok=True)
digest = lambda path: hashlib.sha256(path.read_bytes()).hexdigest()
manifest = ROOT/'src/audio-assets.json'
before = digest(manifest)
source_report = json.loads((SOURCE/'provenance.json').read_text('utf-8'))
report = dict(createdAt=datetime.now(timezone.utc).isoformat(), status='Audition only; current app voice unchanged.',
    source='The previous 85/15 B/current synthetic blend, not the rejected 65/35 regeneration.',
    goal='Lower than the previous blend, moving toward the Current app register while remaining lighter than it.',
    method='FFmpeg Rubber Band pitch shift with formant preservation and tempo=1. No synthesis or further speaker-identity blending. Equalized to each source clip loudness with constant gain and peak headroom.',
    semitones=SHIFT, pitchFactor=FACTOR, installedManifestSha256=before, clips=[])
ffmpeg = imageio_ffmpeg.get_ffmpeg_exe()
report['ffmpeg'] = subprocess.check_output([ffmpeg,'-version'],text=True).splitlines()[0]
def f0(signal,rate):
    signal=librosa.resample(signal.astype(np.float32),orig_sr=rate,target_sr=16000)
    values,voiced,prob=librosa.pyin(signal,fmin=75,fmax=600,sr=16000,frame_length=1024,hop_length=160)
    return values,voiced&(prob>.15)
for row in source_report['clips']:
    take = next(t for t in row['takes'] if t['id']=='refined')
    path = SOURCE/take['file']
    assert digest(path)==take['sha256']
    original,rate = sf.read(path)
    dest = OUT/f'lower-{row["id"]}.wav'
    # Padding protects short words from the processor's start/end window effects.
    padding=rate//4
    filters=f'adelay=250:all=1,apad=pad_dur=0.25,rubberband=tempo=1:pitch={FACTOR:.12f}:formant=preserved:pitchq=quality,atrim=start_sample={padding}:end_sample={padding+len(original)}'
    args=[ffmpeg,'-hide_banner','-loglevel','error','-y','-i',str(path),'-af',filters,'-ar',str(rate),'-ac','1','-c:a','pcm_f32le',str(dest)]
    subprocess.run(args,check=True,capture_output=True)
    signal,new_rate = sf.read(dest)
    assert rate==new_rate==24000 and signal.ndim==1 and np.isfinite(signal).all()
    assert abs(len(signal)-len(original))<=rate*.03, 'Unexpected timing change'
    signal=np.pad(signal,(0,max(0,len(original)-len(signal))))[:len(original)]
    meter=pyln.Meter(rate,block_size=min(.4,len(signal)/rate/2))
    old_lufs=float(meter.integrated_loudness(original))
    new_lufs=float(meter.integrated_loudness(signal))
    gain=min(10**((old_lufs-new_lufs)/20),.94/np.max(np.abs(signal)))
    signal*=gain
    sf.write(dest,signal,rate,subtype='PCM_16')
    decoded,_=sf.read(dest)
    assert .005<np.max(np.abs(decoded))<1
    final_lufs=float(meter.integrated_loudness(decoded))
    assert abs(final_lufs-old_lufs)<.6
    old_f0,old_good=f0(original,rate)
    new_f0,new_good=f0(decoded,rate)
    valid=old_good&new_good&np.isfinite(old_f0)&np.isfinite(new_f0)
    shifts=12*np.log2(new_f0[valid]/old_f0[valid])
    measured=float(np.median(shifts)) if len(shifts) else None
    assert measured is not None and -1.8<measured<-.7, f'Pitch verification failed: {row["id"]}: {measured}'
    clip=dict(id=row['id'],text=row['text'],pinyin=row['pinyin'],meaning=row['meaning'],current=row['current'],
        previous=f'../voice-b-refinement/{take["file"]}',sourceSha256=take['sha256'],file=dest.name,sha256=digest(dest),
        seconds=len(decoded)/rate,sourceLufs=old_lufs,outputLufs=final_lufs,measuredPitchChangeSemitones=round(measured,2),pitchComparisonFrames=int(valid.sum()))
    report['clips'].append(clip)
    print(row['id'],'measured shift',round(measured,2),'semitones',flush=True)
assert digest(manifest)==before
report['pitchCheck']='Median paired pYIN voiced-frame pitch difference. Confident overlapping frames, same timings. Confirms downward adjustment; does not certify naturalness or tones.'
(OUT/'provenance.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n','utf-8')
esc=html.escape
sections=[]
for c in report['clips']:
    controls=[('Previous blend',c['previous']),('Lower pitch · same performance',c['file'])]
    if c['current']:
        controls.append(('Current app · your reference',c['current']))
    sections.append('<section><h2 lang="zh-CN">'+esc(c['text'])+'</h2><p>'+esc(c['pinyin'])+'</p><p>'+esc(c['meaning'])+'</p><div class="takes">'+''.join('<div><h3>'+esc(label)+'</h3><audio controls preload="none" aria-label="'+esc(label+' '+c['text'])+'" src="'+esc(url)+'"></audio></div>' for label,url in controls)+'</div></section>')
page='''<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Sayo · Lower than the previous blend</title><style>body{margin:0;background:#101c2b;color:#eef2f7;font:17px/1.55 system-ui}main{max-width:1120px;margin:auto;padding:32px 20px 70px}a{color:#b7d8fa}h1{font-size:clamp(30px,5vw,46px);line-height:1.15}h2{margin-bottom:8px}h3{font-size:17px}p{max-width:77ch;margin:8px 0}section{border-top:1px solid #526379;margin-top:28px;padding-top:14px}.takes{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:24px}audio{width:100%;margin:8px 0}summary{cursor:pointer;padding:12px 0}a:focus-visible,summary:focus-visible{outline:3px solid #b7d8fa;outline-offset:4px}@media(max-width:800px){.takes{grid-template-columns:1fr;gap:6px}}</style><main><a href="../voice-b-refinement/index.html">Back to the previous blend</a><h1>The previous blend, lower.</h1><p>The middle recording is the exact previous performance lowered by 1.25 semitones. Speed is unchanged and vocal resonance is preserved by the processing. Compare it with <strong>Current app</strong> on the right—the lower reference you meant.</p><p>This is a direct pitch adjustment toward that register, not another identity blend. Each clip was checked to move downward. Listen for whether it keeps the friendly character and stays clean; processing can still introduce artifacts. The installed app voice is unchanged.</p>'''+''.join(sections)+'''<details><summary>Processing and checks</summary><p>Rubber Band pitch processing through local FFmpeg. No new TTS generation or changed words. Duration preserved, loudness matched to the previous blend, formant preservation enabled. Pitch movement was checked on paired voiced frames. No claim that every line is higher than the current app throughout: Mandarin tones and different performances vary.</p><a href="provenance.json">File checks and measured downward shifts</a></details></main><script>document.querySelectorAll('audio').forEach(a=>a.addEventListener('play',()=>document.querySelectorAll('audio').forEach(b=>{if(a!==b)b.pause()})))</script></html>'''
(OUT/'index.html').write_text(page,'utf-8')
print('DONE: 8 lower-pitch files; previous blend and app unchanged.',flush=True)
