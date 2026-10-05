"""Lower the selected previous performance, without another identity regeneration."""
from datetime import datetime, timezone
import hashlib
import html
import json
from pathlib import Path
import subprocess
import sys

from fractions import Fraction
from scipy.signal import resample_poly
import librosa
import numpy as np
import pyloudnorm as pyln
import soundfile as sf

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT/'output/voice-b-refinement'
OUT = ROOT/'output/voice-lower-clean'
SHIFT = -1.75
FACTOR = 2**(SHIFT/12)
sys.stdout.reconfigure(encoding='utf-8')
OUT.mkdir(parents=True, exist_ok=True)
digest = lambda path: hashlib.sha256(path.read_bytes()).hexdigest()
manifest = ROOT/'src/audio-assets.json'
before = digest(manifest)
source_report = json.loads((SOURCE/'provenance.json').read_text('utf-8'))
report = dict(createdAt=datetime.now(timezone.utc).isoformat(), status='Audition only; current app voice unchanged.',
    source='The previous 85/15 B/current synthetic blend, not the rejected 65/35 regeneration.',
    goal='Lower again, simpler processing, moving toward the Current app register while remaining lighter than it.',
    method='Polyphase resampling of the original 85/15 synthetic take, without a phase vocoder, time stretching, formant correction or EQ. Pitch and resonance lower together; duration increases by 10.64 percent. Loudness matched with constant gain.',
    semitones=SHIFT, pitchFactor=FACTOR, installedManifestSha256=before, clips=[])
report['resamplingRatio'] = str(Fraction(1/FACTOR).limit_denominator(10000))

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
    ratio=Fraction(1/FACTOR).limit_denominator(10000)
    signal=resample_poly(original,ratio.numerator,ratio.denominator,window=('kaiser',8.6))
    assert rate==24000 and signal.ndim==1 and np.isfinite(signal).all()
    assert abs(len(signal)/len(original)-1/FACTOR)<.001
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
    # Compare the same spoken instant after the deliberate speed change.
    indices=np.minimum(np.rint(np.arange(len(old_f0))/FACTOR).astype(int),len(new_f0)-1)
    new_f0,new_good=new_f0[indices],new_good[indices]
    valid=old_good&new_good&np.isfinite(old_f0)&np.isfinite(new_f0)
    shifts=12*np.log2(new_f0[valid]/old_f0[valid])
    measured=float(np.median(shifts)) if len(shifts) else None
    assert measured is not None and -2.2<measured<-1.3, f'Pitch verification failed: {row["id"]}: {measured}'
    clip=dict(id=row['id'],text=row['text'],pinyin=row['pinyin'],meaning=row['meaning'],current=row['current'],
        previous=f'../voice-b-refinement/{take["file"]}',sourceSha256=take['sha256'],file=dest.name,sha256=digest(dest),
        seconds=len(decoded)/rate,sourceSeconds=len(original)/rate,sourceLufs=old_lufs,outputLufs=final_lufs,measuredPitchChangeSemitones=round(measured,2),pitchComparisonFrames=int(valid.sum()))
    report['clips'].append(clip)
    print(row['id'],'measured shift',round(measured,2),'semitones',flush=True)
assert digest(manifest)==before
report['pitchCheck']='Median paired pYIN voiced-frame pitch difference. Confident voiced frames aligned to the deliberate speed change. Confirms downward adjustment; does not certify naturalness or tones.'
(OUT/'provenance.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n','utf-8')
esc=html.escape
sections=[]
for c in report['clips']:
    controls=[('Last lower version',f'../voice-lower-register/lower-{c["id"]}.wav'),('Lower again · no time stretching',c['file'])]
    if c['current']:
        controls.append(('Current app · your reference',c['current']))
    sections.append('<section><h2 lang="zh-CN">'+esc(c['text'])+'</h2><p>'+esc(c['pinyin'])+'</p><p>'+esc(c['meaning'])+'</p><div class="takes">'+''.join('<div><h3>'+esc(label)+'</h3><audio controls preload="none" aria-label="'+esc(label+' '+c['text'])+'" src="'+esc(url)+'"></audio></div>' for label,url in controls)+'</div></section>')
page='''<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Sayo · Lower again, simpler processing</title><style>body{margin:0;background:#101c2b;color:#eef2f7;font:17px/1.55 system-ui}main{max-width:1120px;margin:auto;padding:32px 20px 70px}a{color:#b7d8fa}h1{font-size:clamp(30px,5vw,46px);line-height:1.15}h2{margin-bottom:8px}h3{font-size:17px}p{max-width:77ch;margin:8px 0}section{border-top:1px solid #526379;margin-top:28px;padding-top:14px}.takes{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:24px}audio{width:100%;margin:8px 0}summary{cursor:pointer;padding:12px 0}a:focus-visible,summary:focus-visible{outline:3px solid #b7d8fa;outline-offset:4px}@media(max-width:800px){.takes{grid-template-columns:1fr;gap:6px}}</style><main><a href="../voice-b-refinement/index.html">Back to the previous blend</a><h1>A little lower. A simpler adjustment.</h1><p>The middle recording is half a semitone lower than the last audition (1.75 below the original blend). It uses the original recording with simple resampling, avoiding the pitch-processing step that may have introduced metallic texture. Delivery is about 10% slower than the original blend. Compare it with <strong>Current app</strong> on the right—the lower reference you meant.</p><p>This is a direct pitch adjustment toward that register, not another identity blend. Resonance also becomes a little darker. Pay particular attention to 声调呢？; any texture already present in the source may remain. Each clip was checked to move downward. Listen for whether it keeps the friendly character and stays clean; processing can still introduce artifacts. The installed app voice is unchanged.</p>'''+''.join(sections)+'''<details><summary>Processing and checks</summary><p>SciPy polyphase resampling, with no time stretching, phase vocoder or formant correction. No new TTS generation or changed words. Loudness matched to the original blend. Duration increases by 10.64%. Pitch movement checked on time-aligned voiced frames. Automatic transcription screens wording, not tone accuracy or metallic artifacts. No claim that every line is higher than the current app throughout: Mandarin tones and different performances vary.</p><a href="provenance.json">File checks and measured downward shifts</a></details></main><script>document.querySelectorAll('audio').forEach(a=>a.addEventListener('play',()=>document.querySelectorAll('audio').forEach(b=>{if(a!==b)b.pause()})))</script></html>'''
(OUT/'index.html').write_text(page,'utf-8')
print('DONE: 8 lower-pitch files; previous blend and app unchanged.',flush=True)
