"""B-dominant synthetic speaker blend, for listening review only."""
import os
os.environ['HF_HUB_OFFLINE'] = '1'
os.environ['TOKENIZERS_PARALLELISM'] = 'false'
import hashlib
import argparse
import importlib.util
import json
from dataclasses import replace
from datetime import datetime, timezone
from pathlib import Path
import sys

import torch
from qwen_tts import Qwen3TTSModel

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('base_audition', ROOT/'scripts/audition-sayo-qwen.py')
helpers = importlib.util.module_from_spec(spec)
spec.loader.exec_module(helpers)
OUT = ROOT/'output/voice-b-refinement'
SOURCE = ROOT/'output/voice-base-review'
LINES = [
    ('welcome', '来了？开始吧。', 'Lái le? Kāishǐ ba.', 'You’re here? Let’s begin.', 'playful', 16320),
    ('teacher', '认真一点。开始吧。', 'Rènzhēn yìdiǎn. Kāishǐ ba.', 'Focus a little. Let’s begin.', 'cool', 16321),
    ('tones', '声调呢？', 'Shēngdiào ne?', 'What about the tones?', 'deadpan', 16322),
    ('smug', '不错嘛。', 'Bú cuò ma.', 'Not bad at all.', 'deadpan', 16410),
    ('celebrate', '太棒了！', 'Tài bàng le!', 'Fantastic!', 'intense', 16411),
    ('hint', '下次不看提示。', 'Xià cì bú kàn tíshì.', 'Next time, no peeking.', 'deadpan', 16412),
    ('rest', '今天够了。', 'Jīntiān gòu le.', 'That’s enough for today.', 'soft', 16413),
    ('words', '什么？很好。我的书。你好吗？', 'Shénme? Hěn hǎo. Wǒ de shū. Nǐ hǎo ma?', 'What? Very good. My book. How are you?', 'clear', 16324),
]

def main():
    global OUT
    parser = argparse.ArgumentParser()
    parser.add_argument('--current-weight', type=float, default=.15)
    args = parser.parse_args()
    if args.current_weight not in [.15, .35]:
        raise ValueError('Use a reviewed experiment weight: 0.15 or 0.35')
    weight = args.current_weight
    if weight == .35:
        OUT = ROOT/'output/voice-b-refinement-35'
    sys.stdout.reconfigure(encoding='utf-8')
    sys.stderr.reconfigure(encoding='utf-8')
    OUT.mkdir(parents=True, exist_ok=True)
    manifest_path = ROOT/'src/audio-assets.json'
    manifest_hash = helpers.digest(manifest_path)
    manifest = json.loads(manifest_path.read_text('utf-8'))
    base_report = json.loads((SOURCE/'provenance.json').read_text('utf-8'))
    anchor = next(c for c in base_report['clips'] if c['file']=='b-anchor.wav')
    assert helpers.digest(SOURCE/anchor['file']) == anchor['sha256']
    key = lambda s: ''.join(c for c in s if '\u4e00' <= c <= '\u9fff')
    def current(text, mood):
        found = next((v for k,v in manifest.items() if key(k)==key(text)), None)
        return found.get(mood, next(iter(found.values()))) if found else None
    references = []
    for text, mood in [('来了？开始吧。', 'playful'), ('不错嘛。', 'deadpan'), ('今天够了。', 'soft')]:
        url = current(text, mood)
        assert url
        path = ROOT/'public'/url.lstrip('/')
        references.append(dict(text=text, mood=mood, file=str(path.relative_to(ROOT)).replace('\\','/'), sha256=helpers.digest(path)))
    report = dict(createdAt=datetime.now(timezone.utc).isoformat(),
        status='B selected as starting point. This refinement is audition-only, not approved for installation.',
        selection='Owner selected dry and playful B; wants some of the current voice retained.',
        model=json.loads((ROOT/'.models/Qwen3-TTS-12Hz-1.7B-Base/revision.json').read_text('utf-8')),
        installedManifestSha256=manifest_hash, syntheticAnchor=anchor,
        currentSyntheticReferences=references, clips=[],
        method=f'Experimental speaker-embedding interpolation: normalize each current synthetic clip embedding, average, normalize; {1-weight:.2f} B + {weight:.2f} current, then restore B embedding norm. B reference codes and text stay identical for every take. These are embedding weights, not perceived percentages. Both sources are synthetic. No real-person recordings or post pitch/formant/tempo effects.',
        weights=dict(b=1-weight,current=weight), runtime='qwen-tts 0.1.1; torch 2.6.0+cu124; bf16; sdpa',
    )
    def checkpoint():
        assert helpers.digest(manifest_path) == manifest_hash
        (OUT/'provenance.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n','utf-8')
    torch.set_num_threads(4)
    model = Qwen3TTSModel.from_pretrained(str(ROOT/'.models/Qwen3-TTS-12Hz-1.7B-Base'), device_map='cuda:0', dtype=torch.bfloat16, attn_implementation='sdpa')
    b_prompt = model.create_voice_clone_prompt(ref_audio=str(SOURCE/anchor['file']), ref_text=anchor['text'], x_vector_only_mode=False)
    current_embeddings = [model.create_voice_clone_prompt(ref_audio=str(ROOT/r['file']), x_vector_only_mode=True)[0].ref_spk_embedding.float() for r in references]
    unit = lambda value: value/value.norm().clamp_min(1e-8)
    old = unit(torch.stack([unit(v) for v in current_embeddings]).mean(0))
    b = b_prompt[0].ref_spk_embedding
    mixed = unit((1-weight)*unit(b.float())+weight*old)*b.float().norm()
    mix_prompt = [replace(b_prompt[0], ref_spk_embedding=mixed.to(b.dtype))]
    embedding_bytes = mixed.detach().cpu().numpy().tobytes()
    report['fixedBlendEmbeddingSha256'] = hashlib.sha256(embedding_bytes).hexdigest()
    for identity,text,pinyin,meaning,mood,seed in LINES:
        row = dict(id=identity,text=text,pinyin=pinyin,meaning=meaning,current=current(text,mood),takes=[])
        for label,prompt in [('b', b_prompt), ('refined', mix_prompt)]:
            if label=='b' and weight==.35:
                earlier_folder = ROOT/'output/voice-b-refinement'
                earlier_report = json.loads((earlier_folder/'provenance.json').read_text('utf-8'))
                earlier_row = next(c for c in earlier_report['clips'] if c['id']==identity and c['text']==text)
                earlier = next(c for c in earlier_row['takes'] if c['id']=='refined')
                assert helpers.digest(earlier_folder/earlier['file'])==earlier['sha256']
                row['takes'].append(dict(id='previous',file=f'../voice-b-refinement/{earlier["file"]}',sha256=earlier['sha256'],seed=earlier['seed'],seconds=earlier['seconds']))
                continue
            prior = next((c for c in base_report['clips'] if c['file']==f'b-{identity}.wav' and c['text']==text), None)
            if label=='b' and prior:
                row['takes'].append(dict(id=label,file=f'../voice-base-review/{prior["file"]}',sha256=prior['sha256'],seed=seed,seconds=prior['seconds']))
                continue
            helpers.seed(seed)
            wavs,rate = model.generate_voice_clone(text=text,language='Chinese',voice_clone_prompt=prompt,non_streaming_mode=True,max_new_tokens=240)
            take = helpers.save(OUT/f'{label}-{identity}.wav',wavs[0],rate)
            take.update(id=label,seed=seed)
            row['takes'].append(take)
            print('RENDERED',label,identity,take['seconds'],flush=True)
        report['clips'].append(row)
        checkpoint()
    checkpoint()
    print('DONE: one fixed B-led blend; current application audio unchanged.',flush=True)

if __name__=='__main__':
    main()
