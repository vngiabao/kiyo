"""Resume local generation of the approved synthetic Sayo identity; never installs."""
import os
os.environ['HF_HUB_OFFLINE'] = '1'
os.environ['TOKENIZERS_PARALLELISM'] = 'false'
import argparse
from dataclasses import replace
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import random
import re
import sys
import numpy as np
import soundfile as sf
import torch
from qwen_tts import Qwen3TTSModel

ROOT = Path(__file__).resolve().parents[1]
CACHE = ROOT / '.cache/sayo-qwen-approved'
PROFILE = ROOT / 'content/voices/approved-b-half/profile.json'
ROSTER = ROOT / 'content/voices/sayo-roster-staged.json'
key = lambda text: re.sub(r'[\s，。！？,.!?、]', '', text)
digest = lambda path: hashlib.sha256(path.read_bytes()).hexdigest()

def read(path):
    return json.loads(path.read_text('utf-8'))

def atomic(path, data):
    temp = path.with_suffix('.tmp')
    temp.write_text(json.dumps(data, ensure_ascii=False, indent=2)+'\n', 'utf-8')
    temp.replace(path)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--limit', type=int)
    parser.add_argument('--batch', type=int, default=4)
    parser.add_argument('--retry-list', type=Path, default=ROOT/'content/voices/approved-b-half/retries.json')
    args = parser.parse_args()
    sys.stdout.reconfigure(encoding='utf-8')
    sys.stderr.reconfigure(encoding='utf-8')
    CACHE.mkdir(parents=True, exist_ok=True)
    profile, roster = read(PROFILE), read(ROSTER)
    scripts = read(ROOT / 'content/audio-scripts.json')
    selected = {key(c['text']): c for c in profile['clips']}
    audition_moods = dict(welcome='playful', teacher='cool', tones='deadpan',
        smug='deadpan', celebrate='intense', hint='deadpan', rest='soft', words='clear')
    retries = read(args.retry_list) if args.retry_list.exists() else {}
    override_path = ROOT/'content/voices/approved-b-half/pronunciation-contexts.json'
    overrides = read(override_path) if override_path.exists() else {}
    jobs, pending = [], []
    for entry in scripts:
        if entry.get('parts'):
            continue
        for mood in entry['moods']:
            approved = selected.get(key(entry['text']))
            use_approved = approved and audition_moods[approved['id']] == mood
            recipe = dict(text=entry['text'], mood=mood, model=profile['model'],
                profileSha256=digest(PROFILE), rosterSha256=digest(ROSTER), pipeline=1,
                take=int(retries.get(entry['id']+'-'+mood, 0)))
            if entry.get('delivery'):
                recipe['delivery'] = entry['delivery']
            if entry['id']+'-'+mood in overrides:
                recipe['pronunciationContext'] = overrides[entry['id']+'-'+mood]
            token = hashlib.sha256(json.dumps(recipe, sort_keys=True, ensure_ascii=False).encode()).hexdigest()[:12]
            filename = f'{entry["id"]}-{mood}-{token}'
            receipt, wav = CACHE/(filename+'.json'), CACHE/(filename+'.wav')
            job = dict(entry=entry, mood=mood, recipe=recipe, receipt=receipt, wav=wav)
            jobs.append(job)
            if use_approved:
                source = ROOT / approved['approved']['file']
                assert digest(source) == approved['approved']['sha256']
                record = dict(**recipe, rawFile=str(source.relative_to(ROOT)),
                    rawSha256=digest(source), alreadyProcessed=True, approvedTake=True,
                    seconds=approved['settings']['seconds'], seed=None)
                atomic(receipt, record)
            elif receipt.exists():
                record = read(receipt)
                assert digest(ROOT / record['rawFile']) == record['rawSha256']
            else:
                pending.append(job)
    # Publish only a generation plan here; app assets are installed by the checked mastering step.
    atomic(CACHE/'plan.json', dict(profileSha256=digest(PROFILE), rosterSha256=digest(ROSTER),
        scriptsSha256=digest(ROOT/'content/audio-scripts.json'),
        jobs=[dict(text=j['entry']['text'], mood=j['mood'], receipt=str(j['receipt'].relative_to(ROOT))) for j in jobs]))
    print(f'PLAN {len(jobs)} clips, {len(pending)} pending', flush=True)
    if not pending:
        return
    torch.set_num_threads(4)
    assert torch.cuda.is_available(), 'CUDA is required'
    model = Qwen3TTSModel.from_pretrained(str(ROOT/'.models/Qwen3-TTS-12Hz-1.7B-Base'),
        device_map='cuda:0', dtype=torch.bfloat16, attn_implementation='sdpa')
    anchor = profile['anchor']
    assert digest(ROOT/anchor['file']) == anchor['sha256']
    base_prompt = model.create_voice_clone_prompt(ref_audio=str(ROOT/anchor['file']),
        ref_text=anchor['text'], x_vector_only_mode=False)[0]
    embeddings = []
    for reference in profile['currentSyntheticReferences']:
        assert digest(ROOT/reference['file']) == reference['sha256']
        embeddings.append(model.create_voice_clone_prompt(ref_audio=str(ROOT/reference['file']),
            x_vector_only_mode=True)[0].ref_spk_embedding.float())
    unit = lambda value: value/value.norm().clamp_min(1e-8)
    old = unit(torch.stack([unit(v) for v in embeddings]).mean(0))
    b = base_prompt.ref_spk_embedding
    mixed = unit(.85*unit(b.float())+.15*old)*b.float().norm()
    assert hashlib.sha256(mixed.detach().cpu().numpy().tobytes()).hexdigest() == profile['fixedBlendEmbeddingSha256']
    prompts = {}
    repair_prompt = replace(base_prompt, ref_spk_embedding=mixed.to(b.dtype))
    for mood in roster['moods']:
        assert digest(ROOT/mood['reference']) == mood['referenceSha256']
        delivery = model.create_voice_clone_prompt(ref_audio=str(ROOT/mood['reference']),
            ref_text=mood['referenceText'], x_vector_only_mode=False)[0]
        prompts[mood['id']] = replace(delivery, ref_spk_embedding=mixed.to(b.dtype))
    # Keep similar lengths together to avoid wasting batch decoding on padding.
    pending.sort(key=lambda j: (len(j['entry']['text']), j['entry']['id'], j['mood']))
    if args.limit:
        pending = pending[:args.limit]
    done = 0
    for start in range(0, len(pending), args.batch):
        batch = pending[start:start+args.batch]
        batch_seed = int(hashlib.sha256(''.join(str(j['wav']) for j in batch).encode()).hexdigest()[:8], 16) % (2**31)
        for attempt in range(4):
            seed = batch_seed + attempt
            random.seed(seed); np.random.seed(seed); torch.manual_seed(seed); torch.cuda.manual_seed_all(seed)
            texts = [j['recipe'].get('pronunciationContext',{}).get('synthesisText',j['entry']['text']) for j in batch]
            texts = [t if re.search(r'[。！？.!?]$', t) else t+'。' for t in texts]
            wavs, rate = model.generate_voice_clone(text=texts, language='Chinese',
                voice_clone_prompt=[repair_prompt if j['recipe']['take'] else prompts[j['mood']] for j in batch], non_streaming_mode=True,
                max_new_tokens=min(650, max(100, max(map(len, texts))*8+50)))
            failed = []
            for j, audio in zip(batch, wavs):
                audio = np.asarray(audio, dtype=np.float32).squeeze()
                n = len(re.findall(r'[\u4e00-\u9fff]', j['entry']['text']))
                nz = np.flatnonzero(np.abs(audio) > .003)
                if audio.ndim != 1 or rate != 24000 or not np.isfinite(audio).all() or not len(nz):
                    failed.append(j); continue
                pad = int(.12*rate)
                audio = audio[max(0,nz[0]-pad):min(len(audio),nz[-1]+pad)]
                context_record = {}
                if j['recipe'].get('pronunciationContext'):
                    # A natural carrier disambiguates pronunciation; only its final repeated word ships.
                    carrier = j['wav'].with_name(j['wav'].stem+'-carrier.wav')
                    sf.write(carrier,audio,rate,subtype='PCM_16')
                    frame = 240
                    rms = np.sqrt(np.mean(audio[:len(audio)//frame*frame].reshape(-1,frame)**2,axis=1))
                    voiced = np.flatnonzero(rms > max(.005,float(rms.max())*.07))
                    gaps = [(a,b) for a,b in zip(voiced,voiced[1:]) if b-a>=12 and (len(audio)-b*frame)/rate>=.23]
                    if not gaps:
                        print('RETRY missing carrier boundary',j['entry']['text'],flush=True)
                        failed.append(j);continue
                    boundary = max(0,gaps[-1][1]*frame-int(.06*rate))
                    context_record = dict(carrierFile=str(carrier.relative_to(ROOT)),carrierSha256=digest(carrier),cropStartSeconds=boundary/rate)
                    audio = audio[boundary:]
                seconds = len(audio)/rate
                if not max(.23,n/10) <= seconds <= max(2.8,2+n*.7):
                    print('RETRY duration', j['entry']['text'], j['mood'], seconds, flush=True)
                    failed.append(j); continue
                peak = float(np.max(np.abs(audio)))
                if peak > .89:
                    audio *= .89/peak
                sf.write(j['wav'], audio, rate, subtype='PCM_16')
                atomic(j['receipt'], dict(**j['recipe'], rawFile=str(j['wav'].relative_to(ROOT)),
                    rawSha256=digest(j['wav']), alreadyProcessed=False, approvedTake=False,
                    seconds=seconds, seed=seed, attempt=attempt+1,
                    synthesisText=texts[batch.index(j)],
                    reference=anchor['file'] if j['recipe']['take'] else roster['moods'][list(prompts).index(j['mood'])]['reference'],
                    batchTexts=texts,batchMoods=[item['mood'] for item in batch],batchPosition=batch.index(j),
                    **context_record,
                    generatedAt=datetime.now(timezone.utc).isoformat()))
                done += 1
                print(f'READY {done}/{len(pending)} {j["entry"]["text"]} [{j["mood"]}] {seconds:.2f}s', flush=True)
            if not failed:
                break
            batch = failed
        else:
            raise RuntimeError('Could not generate valid clips: '+str([(j['entry']['text'],j['mood']) for j in batch]))
    print('Generation pass complete. Master and verify before installation.', flush=True)

if __name__ == '__main__':
    main()
