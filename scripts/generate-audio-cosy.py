"""Generate Sayo locally. Resume by content/settings hash; publish only a complete library.

.tts-env/Scripts/python scripts/generate-audio-cosy.py [--install] [--limit N]
No credentials, learner data or remote services are used.
"""
import os
os.environ['HF_HUB_OFFLINE'] = '1'
os.environ['TOKENIZERS_PARALLELISM'] = 'false'
import argparse
import hashlib
import json
import random
import re
import subprocess
import sys
sys.stdout.reconfigure(encoding='utf-8')
sys.stderr.reconfigure(encoding='utf-8')
from datetime import datetime, timezone
from pathlib import Path
import imageio_ffmpeg
import librosa
import numpy as np
import soundfile as sf
import torch

root = Path(__file__).resolve().parent.parent
sys.path[:0] = [str(root/'.tts'), str(root/'.tts/third_party/Matcha-TTS')]
from cosyvoice.cli.cosyvoice import AutoModel
from audio_postprocess import normalize_clip

parser = argparse.ArgumentParser()
parser.add_argument('--install', action='store_true')
parser.add_argument('--limit', type=int)
args = parser.parse_args()
roster = json.loads((root/'content/voices/roster.json').read_text('utf-8'))
scripts = json.loads((root/'content/audio-scripts.json').read_text('utf-8'))
moods = {m['id']: m for m in roster['moods']}
out = root/'public/audio-v2'
out.mkdir(exist_ok=True)
cache = root/'.cache/sayo-generation'
cache.mkdir(exist_ok=True)
reference = root/roster['synthesisReference']
ref_hash = hashlib.sha256(reference.read_bytes()).hexdigest()
model_dir = root/'.models/Fun-CosyVoice3-0.5B-2512'
model_meta = json.loads((model_dir/'revision.json').read_text())
ffmpeg = imageio_ffmpeg.get_ffmpeg_exe()
model = None
torch.set_num_threads(4)
key = lambda s: re.sub(r'[\s，。！？,.!?、]', '', s)
by_text = {key(s['text']): s for s in scripts}
records, manifest = [], {}
completed = 0

def atomic_json(path, data):
    tmp = path.with_suffix(path.suffix+'.tmp')
    tmp.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n','utf-8')
    tmp.replace(path)

def encode(audio, target):
    raw = cache/(target.stem+'.wav')
    sf.write(raw,audio,24000,subtype='FLOAT')
    # True-peak limiting and loudness normalization run at the final sample rate.
    proc = subprocess.run([ffmpeg,'-hide_banner','-loglevel','error','-y','-i',str(raw),
        '-af','loudnorm=I=-16:TP=-1.5:LRA=11','-ar','24000','-ac','1','-codec:a','libmp3lame','-b:a','64k',str(target)],capture_output=True)
    raw.unlink(missing_ok=True)
    if proc.returncode:
        raise RuntimeError(proc.stderr.decode(errors='replace'))
    decoded, sr = sf.read(target)
    if sr != 24000 or decoded.ndim != 1 or not np.isfinite(decoded).all() or max(abs(decoded)) < .005 or max(abs(decoded)) >= 1:
        raise ValueError(f'Broken or clipping encoded audio: {target}')
    return len(decoded)/sr

def generate(entry, mood):
    global model, completed
    setting = dict(moods[mood])
    is_hsk = any(kind.startswith('hsk-') for kind in entry['kinds'])
    if is_hsk:
        setting.update(roster.get('hskTeachingSettings', {}))
    if 'reaction' in entry['kinds']:
        setting.update(roster.get('reactionSettings', {}).get(mood, {}))
    instruction = roster.get('reactionInstructions', {}).get(mood, setting['instruct']) if 'reaction' in entry['kinds'] else setting['instruct']
    if is_hsk and 'reaction' not in entry['kinds']:
        instruction = roster.get('hskTeachingInstruction', instruction)
    take = roster.get('reactionTakes' if 'reaction' in entry['kinds'] else 'pronunciationTakes', {}).get(entry['text'], {})
    instruction = take.get('instruct', instruction)
    recipe = dict(text=entry['text'],mood=mood,instruct=instruction,speed=setting['speed'],pitchShift=setting['pitchShift'],referenceSha256=ref_hash,model=model_meta,pipeline=1)
    if 'seed' in take:
        recipe['generationSeed'] = take['seed']
    if 'synthesisText' in take:
        # CosyVoice 3's documented pinyin tokens can repair specific pronunciations.
        # Keep the app's displayed text and catalog keys unchanged.
        recipe['pronunciationText'] = take['synthesisText']
    if setting.get('pitchMethod'):
        recipe['pitchMethod'] = setting['pitchMethod']
    digest = hashlib.sha256(json.dumps(recipe,sort_keys=True,ensure_ascii=False).encode()).hexdigest()
    target = out/f'{entry["id"]}-{mood}-{digest[:10]}.mp3'
    receipt = cache/(target.stem+'.json')
    if target.exists() and receipt.exists():
        record = json.loads(receipt.read_text('utf-8'))
        if hashlib.sha256(target.read_bytes()).hexdigest() != record['sha256']:
            raise ValueError(f'Checksum mismatch: {target}; preserve and investigate before regeneration.')
    else:
        if args.limit and completed >= args.limit:
            raise RuntimeError('Requested generation limit reached. Existing clips kept; manifest not installed.')
        if model is None:
            if not torch.cuda.is_available():
                raise RuntimeError('CUDA is required for local Sayo generation.')
            model = AutoModel(model_dir=str(model_dir),fp16=False)
        # Cache the unchanged reference features AND this exact instruction.
        # CosyVoice's speaker cache stores prompt text, so each mood needs its own id.
        speaker_id = hashlib.sha256(instruction.encode()).hexdigest()
        if speaker_id not in model.frontend.spk2info:
            model.add_zero_shot_spk(instruction,str(reference),speaker_id)
        n = len(re.findall(r'[\u4e00-\u9fff]',entry['text']))
        last_error = None
        for attempt in range(4):
            seed = (recipe.get('generationSeed', int(digest[:8],16))+attempt) % (2**31)
            random.seed(seed); np.random.seed(seed); torch.manual_seed(seed); torch.cuda.manual_seed_all(seed)
            try:
                # A terminal boundary helps the model finish very short fragments.
                synthesis_text = take.get('synthesisText', entry['text'])
                if attempt and not re.search(r'[。！？.!?]$',synthesis_text):
                    synthesis_text += '。'
                chunks = list(model.inference_instruct2(synthesis_text,instruction,str(reference),zero_shot_spk_id=speaker_id,stream=False,speed=setting['speed'],text_frontend=False))
                audio = torch.cat([c['tts_speech'].cpu() for c in chunks],dim=1).squeeze().numpy()
                if not np.isfinite(audio).all() or np.max(np.abs(audio)) < .005:
                    raise ValueError('Empty/nonfinite synthesis')
                nz = np.flatnonzero(np.abs(audio) > .005)
                audio = audio[max(0,nz[0]-1920):min(len(audio),nz[-1]+1920)]
                seconds = len(audio)/24000
                upper = 2.5 if n == 1 else 3+n*(1.0 if 'reaction' in entry['kinds'] else .65)
                if not max(.23,n/9) <= seconds <= upper:
                    raise ValueError(f'Suspicious duration {seconds:.2f}s for {n} syllables')
                if setting['pitchShift']:
                    if setting.get('pitchMethod') == 'resample':
                        # Reactions allow slower delivery without phase-vocoder artifacts.
                        audio = librosa.resample(audio,orig_sr=24000*2**(setting['pitchShift']/12),target_sr=24000,res_type='soxr_hq')
                    else:
                        audio = librosa.effects.pitch_shift(audio,sr=24000,n_steps=setting['pitchShift'])
                seconds = encode(audio,target)
                record = dict(**recipe,synthesisText=synthesis_text,file=str(target.relative_to(root)).replace('\\','/'),seed=seed,attempts=attempt+1,seconds=seconds,sampleRate=24000,channels=1,bytes=target.stat().st_size,sha256=hashlib.sha256(target.read_bytes()).hexdigest(),generatedAt=datetime.now(timezone.utc).isoformat())
                atomic_json(receipt,record)
                break
            except (ValueError, RuntimeError) as error:
                last_error = error
                print(f'RETRY {entry["text"]} {mood}: {error}',flush=True)
        else:
            raise RuntimeError(f'Failed {entry["text"]} / {mood}: {last_error}')
        completed += 1
    records.append(record)
    manifest.setdefault(entry['text'],{})[mood] = '/audio-v2/'+target.name
    print(f'READY {len(records)} {entry["text"]} [{mood}] {record["seconds"]:.2f}s',flush=True)

def finalize(record):
    target = root/record['file']
    record.update(normalize_clip(target,cache))
    record['sha256'] = hashlib.sha256(target.read_bytes()).hexdigest()
    record['bytes'] = target.stat().st_size
    receipt = cache/(target.stem+'.json')
    if receipt.exists():
        atomic_json(receipt,record)

# Dependent dialogue/reading assemblies use the finalized, equally loud line clips.
for entry in scripts:
    if not entry.get('parts'):
        for mood in entry['moods']:
            generate(entry,mood)
for record in records:
    finalize(record)
for entry in scripts:
    if not entry.get('parts'):
        continue
    for reading_mood in ['dialogue'] if entry.get('dialogue') else entry['moods']:
        parts, hashes, selections = [], [], []
        for part in entry['parts']:
            source = by_text[key(part['text'])]
            mood = part['mood'] if reading_mood == 'dialogue' else reading_mood
            url = manifest[source['text']][mood]
            file = root/'public'/url.lstrip('/')
            audio, sr = sf.read(file)
            parts.extend([audio,np.zeros(int(sr*.22))])
            hashes.append(hashlib.sha256(file.read_bytes()).hexdigest())
            selections.append(dict(text=part['text'],mood=mood))
        digest = hashlib.sha256(''.join(hashes).encode()).hexdigest()[:10]
        target = out/f'{entry["id"]}-{reading_mood}-{digest}.mp3'
        seconds = encode(np.concatenate(parts[:-1]),target)
        for mood in entry['moods'] if reading_mood == 'dialogue' else [reading_mood]:
            manifest.setdefault(entry['text'],{})[mood] = '/audio-v2/'+target.name
        records.append(dict(text=entry['text'],mood=reading_mood,parts=selections,sourceHashes=hashes,file=str(target.relative_to(root)).replace('\\','/'),seconds=seconds,sampleRate=24000,channels=1,bytes=target.stat().st_size,sha256=hashlib.sha256(target.read_bytes()).hexdigest(),generatedAt=datetime.now(timezone.utc).isoformat()))

for record in records:
    finalize(record)
atomic_json(out/'assets.json',manifest)
provenance = dict(model=model_meta,codeRevision='074ca6dc9e80a2f424f1f74b48bdd7d3fea531cc',roster='content/voices/roster.json',referenceSha256=ref_hash,generatedAt=datetime.now(timezone.utc).isoformat(),status='Direction approved for local integration. Tone/naturalness review remains human.',format='mono 24 kHz MP3, 64 kbps',loudness='FFmpeg loudnorm and measured correction to -16 +/-1 LUFS; short syllables use a reduced meter window; peak limiter at 0.84',clips=records,totalBytes=sum(r['bytes'] for r in records))
atomic_json(root/'content/voices/sayo-library-provenance.json',provenance)
if args.install:
    atomic_json(root/'src/audio-assets.json',manifest)
    atomic_json(root/'content/audio-provenance.json',dict(provenance,
        scripts='content/audio-scripts.json',
        voiceIdentity='Sayo: one original synthetic adult female identity',
        settings=roster,modelLicense='Apache-2.0',
        legacyBackup='output/audio-backup-kokoro/audio-provenance.json'))
print(f'COMPLETE: {len(records)} files, {provenance["totalBytes"]:,} bytes. Installed: {args.install}',flush=True)
