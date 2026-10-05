"""Master a complete approved Sayo library; install only with --install after checks."""
import argparse
from datetime import datetime, timezone
from fractions import Fraction
import hashlib
import json
from pathlib import Path
import re
import shutil
import subprocess
import sys
import imageio_ffmpeg
import numpy as np
from scipy.signal import resample_poly
import soundfile as sf
from audio_postprocess import normalize_clip

ROOT = Path(__file__).resolve().parents[1]
CACHE = ROOT/'.cache/sayo-qwen-approved'
OUT = ROOT/'public/audio-v2'
key = lambda text: re.sub(r'[\s，。！？,.!?、]', '', text)
digest = lambda path: hashlib.sha256(path.read_bytes()).hexdigest()
read = lambda path: json.loads(path.read_text('utf-8'))

def atomic(path, data):
    temp = path.with_suffix('.tmp')
    temp.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n','utf-8')
    temp.replace(path)

def encode(signal, dest):
    raw = CACHE/(dest.stem+'-master.wav')
    sf.write(raw,signal,24000,subtype='FLOAT')
    subprocess.run([imageio_ffmpeg.get_ffmpeg_exe(),'-hide_banner','-loglevel','error','-y',
        '-i',str(raw),'-af','loudnorm=I=-16:TP=-1.5:LRA=11','-ar','24000','-ac','1',
        '-codec:a','libmp3lame','-b:a','64k',str(dest)],check=True,capture_output=True)
    raw.unlink()
    levels=normalize_clip(dest,CACHE)
    audio,rate=sf.read(dest)
    assert rate==24000 and audio.ndim==1 and np.isfinite(audio).all()
    return dict(file=dest.relative_to(ROOT).as_posix(),sha256=digest(dest),
        seconds=len(audio)/rate,sampleRate=rate,channels=1,bytes=dest.stat().st_size,**levels)

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--install',action='store_true')
    parser.add_argument('--partial',action='store_true')
    args=parser.parse_args()
    assert not(args.install and args.partial)
    sys.stdout.reconfigure(encoding='utf-8')
    plan=read(CACHE/'plan.json')
    profile_path=ROOT/'content/voices/approved-b-half/profile.json'
    roster_path=ROOT/'content/voices/sayo-roster-staged.json'
    assert plan['profileSha256']==digest(profile_path)
    assert plan['rosterSha256']==digest(roster_path)
    assert plan['scriptsSha256']==digest(ROOT/'content/audio-scripts.json')
    profile,roster=read(profile_path),read(roster_path)
    scripts=read(ROOT/'content/audio-scripts.json')
    missing=[j for j in plan['jobs'] if not (ROOT/j['receipt']).exists()]
    if missing and not args.partial:
        raise RuntimeError(f'{len(missing)} raw clips missing; refusing incomplete library')
    OUT.mkdir(exist_ok=True)
    records,manifest=[],{}
    screen=read(CACHE/'screening.json') if (CACHE/'screening.json').exists() else {'clips':{}}
    acceptable={'text-match','repeated-text-match','homophone-transcript','owner-approved-take','carrier-text-match','carrier-homophone-transcript'}
    raw_records=[read(ROOT/j['receipt']) for j in plan['jobs'] if (ROOT/j['receipt']).exists()]
    def screening(record):
        return screen['clips'].get(record['rawSha256']+':'+record['text'],{}).get('status','pending')
    substitutions=[]
    unresolved=[]
    ratio=Fraction(profile['processing']['resampleRatio'])
    for job in plan['jobs']:
        if not (ROOT/job['receipt']).exists():
            continue
        raw=read(ROOT/job['receipt'])
        original_mood=raw['mood']
        if screening(raw) not in acceptable:
            alternatives=[r for r in raw_records if r['text']==raw['text'] and screening(r) in acceptable]
            alternatives.sort(key=lambda r:r['mood']!='clear')
            if alternatives:
                raw=alternatives[0]
                substitutions.append(dict(text=raw['text'],requestedMood=original_mood,deliveryMood=raw['mood'],reason='Use the screened same-word take of the same Sayo identity; pronunciation before mood.'))
            else:
                unresolved.append(dict(text=raw['text'],mood=original_mood,status=screening(raw)))
        source=ROOT/raw['rawFile']
        assert digest(source)==raw['rawSha256']
        token=hashlib.sha256((raw['rawSha256']+original_mood+'qwen-master-v1').encode()).hexdigest()[:12]
        dest=OUT/f'sayo-b-half-{original_mood}-{token}.mp3'
        receipt=CACHE/(dest.stem+'-master.json')
        if receipt.exists() and dest.exists():
            record=read(receipt)
            assert digest(dest)==record['sha256']
        else:
            audio,rate=sf.read(source)
            assert rate==24000
            if not raw['alreadyProcessed']:
                audio=resample_poly(audio,ratio.numerator,ratio.denominator,window=('kaiser',8.6))
            record=dict(raw)
            record.update(**encode(audio,dest),pitchMethod='resample',pitchShift=-2.25,
                sourceApprovedProfile=profile_path.relative_to(ROOT).as_posix(),
                masteredAt=datetime.now(timezone.utc).isoformat())
            atomic(receipt,record)
        record.update(mood=original_mood,deliveryMood=raw['mood'],screeningStatus=screening(raw))
        records.append(record)
        manifest.setdefault(raw['text'],{})[original_mood]='/audio-v2/'+dest.name
    index={key(text):voices for text,voices in manifest.items()}
    if not args.partial:
        for entry in scripts:
            if not entry.get('parts'): continue
            for mood in ['dialogue'] if entry.get('dialogue') else entry['moods']:
                audios,hashes,selections=[],[],[]
                for part in entry['parts']:
                    part_mood=part['mood'] if mood=='dialogue' else mood
                    source=ROOT/'public'/index[key(part['text'])][part_mood].lstrip('/')
                    audio,rate=sf.read(source);assert rate==24000
                    audios.extend([audio,np.zeros(round(rate*.22))])
                    hashes.append(digest(source));selections.append(dict(text=part['text'],mood=part_mood))
                token=hashlib.sha256((''.join(hashes)+'qwen-assembly-v1').encode()).hexdigest()[:12]
                dest=OUT/f'{entry["id"]}-{mood}-{token}.mp3'
                record=dict(text=entry['text'],mood=mood,parts=selections,sourceHashes=hashes,
                    **encode(np.concatenate(audios[:-1]),dest))
                records.append(record)
                for alias in entry['moods'] if mood=='dialogue' else [mood]:
                    manifest.setdefault(entry['text'],{})[alias]='/audio-v2/'+dest.name
        index={key(text):voices for text,voices in manifest.items()}
        for entry in scripts:
            for mood in entry['moods']:
                assert index.get(key(entry['text']),{}).get(mood), (entry['text'],mood)
    provenance=dict(model=profile['model'],roster='content/voices/roster.json',
        approvedProfile='content/voices/approved-b-half/profile.json',
        generatedAt=datetime.now(timezone.utc).isoformat(),status='Owner-approved synthetic voice; automatic screening is not native pronunciation certification.',
        format='mono 24 kHz MP3, 64 kbps',loudness='-16 +/-1 LUFS, measured after encoding',
        pitchMethod='single-pass polyphase resampling; no phase vocoder',clips=records,
        totalBytes=sum(r['bytes'] for r in records),pronunciationFirstSubstitutions=substitutions,unresolved=unresolved)
    atomic(CACHE/'assets.json',manifest)
    atomic(CACHE/'provenance.json',provenance)
    if args.install:
        previous=ROOT/'output/audio-backup-before-approved-b/audio-assets.json'
        assert digest(ROOT/'src/audio-assets.json') in [digest(previous),
            hashlib.sha256((json.dumps(manifest,ensure_ascii=False,indent=2)+'\n').encode()).hexdigest()], 'Installed catalog changed in parallel; review before replacing it'
        screen=read(CACHE/'screening.json')
        assert screen['planSha256']==digest(CACHE/'plan.json')
        assert not unresolved, 'Resolve discrepancies without a screened same-word alternative before install'
        backup=ROOT/'output/audio-backup-before-approved-b'
        backup.mkdir(parents=True,exist_ok=True)
        # Keep all inactive audio recoverable outside public so the PWA only ships the new library.
        keep={Path(r['file']).name for r in records}
        archive=backup/'mp3';archive.mkdir(exist_ok=True)
        for file in OUT.glob('*.mp3'):
            if file.name in keep: continue
            assert file.resolve().parent==OUT.resolve()
            target=archive/file.name
            assert target.resolve().parent==archive.resolve()
            if target.exists():
                assert digest(target)==digest(file)
            else:
                shutil.copy2(file,target)
        atomic(ROOT/'src/audio-assets.json',manifest)
        atomic(ROOT/'content/voices/sayo-library-provenance.json',provenance)
        atomic(ROOT/'content/audio-provenance.json',dict(provenance,settings=roster,
            scripts='content/audio-scripts.json',modelLicense='Apache-2.0',voiceIdentity='Sayo: one approved original synthetic voice',legacyBackup='output/audio-backup-before-approved-b'))
        roster['status']='Installed approved B-half identity; individual pronunciation review remains ongoing.'
        atomic(ROOT/'content/voices/roster.json',roster)
        atomic(OUT/'assets.json',manifest)
        for file in OUT.glob('*.mp3'):
            if file.name not in keep:
                assert digest(archive/file.name)==digest(file)
                file.unlink()
    print(f'MASTERED {len(records)} files; {provenance["totalBytes"]:,} bytes; installed={args.install}; missing={len(missing)}',flush=True)

if __name__=='__main__':
    main()
