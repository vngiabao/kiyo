"""Design original synthetic anchors; reuse each unchanged for local auditions only."""
import argparse
import gc
import hashlib
import json
import os
from pathlib import Path
import random
import sys
from datetime import datetime, timezone

os.environ['HF_HUB_OFFLINE'] = '1'
os.environ['TOKENIZERS_PARALLELISM'] = 'false'
import numpy as np
import soundfile as sf
import torch
from qwen_tts import Qwen3TTSModel

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'output/voice-base-review'
ANCHOR_TEXT = '来了？开始吧。别紧张，我陪你慢慢来。这个字读什么？先想一想。声调呢？嗯，这次读对了。哎呀，全对啦！不错嘛，你还挺厉害的。好，我们再来一次。'
DESIGNS = [
    ('a', 'Full and smiling', '年轻成年女性，音色自然偏低，胸腔共鸣饱满扎实，带非常轻的沙感。用准确的标准普通话说话。像熟悉的朋友，放松、带笑、机灵又有一点懒洋洋的幽默。开头低而从容，开心时自然升高音调，仍然是同一个人的声音。语速中等稍慢，吐字完整，句尾轻轻舒展。'),
    ('b', 'Dry and playful', '二十多岁的年轻女性，自然中低音，清晰厚实、有质感的女声，略带鼻腔共鸣。准确的标准普通话。亲近的朋友之间打趣，懒洋洋、带笑，假装一本正经但藏不住开心，偶尔短促地明亮起来。温暖而有精神，不凶也不气声。语速中等稍慢，声调清楚自然。'),
    ('c', 'Warm with more range', '年轻女性自然低中音，圆润饱满的胸声，轻微沙感，清楚的标准普通话。笑着说话，亲切、俏皮、有一点害羞的坏笑。平静时声音低而稳，惊喜时音高自然上扬，随后又放松下来，情绪变化中音色保持一致。语速稍慢，轻松口语节奏，句尾有很轻的拖音，发音准确。'),
]
LINES = [
    ('welcome', '来了？开始吧。', 'Lái le? Kāishǐ ba.', 'You’re here? Let’s begin.'),
    ('teacher', '认真一点。开始吧。', 'Rènzhēn yìdiǎn. Kāishǐ ba.', 'Focus a little. Let’s begin.'),
    ('tones', '声调呢？', 'Shēngdiào ne?', 'What about the tones?'),
    ('praise', '哎呀，全对啦！不错嘛！', 'Āiyā, quán duì la! Bú cuò ma!', 'Oh! All correct! Not bad!'),
    ('words', '什么？很好。我的书。你好吗？', 'Shénme? Hěn hǎo. Wǒ de shū. Nǐ hǎo ma?', 'What? Very good. My book. How are you?'),
]

def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def seed(value):
    random.seed(value)
    np.random.seed(value)
    torch.manual_seed(value)
    torch.cuda.manual_seed_all(value)

def save(path, signal, rate):
    signal = np.asarray(signal, dtype=np.float32).squeeze()
    if signal.ndim != 1 or not np.isfinite(signal).all():
        raise ValueError(f'Invalid waveform: {path}')
    active = np.flatnonzero(np.abs(signal) > .003)
    if not len(active):
        raise ValueError(f'Empty waveform: {path}')
    pad = int(rate * .12)
    signal = signal[max(0, active[0]-pad):min(len(signal), active[-1]+pad)]
    if not .3 < len(signal)/rate < 40:
        raise ValueError(f'Suspicious duration: {path}')
    # Lossless PCM, peak headroom only: no pitch, formant, tempo or EQ effects.
    peak = float(np.max(np.abs(signal)))
    if peak > .89:
        signal *= .89/peak
    sf.write(path, signal, rate, subtype='PCM_16')
    return dict(file=path.name, sha256=digest(path), seconds=round(len(signal)/rate,3), sampleRate=rate, peak=float(np.max(np.abs(signal))))

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('stage', choices=['design', 'reuse'])
    parser.add_argument('--candidate', choices=['a', 'b', 'c'])
    args = parser.parse_args()
    sys.stdout.reconfigure(encoding='utf-8')
    sys.stderr.reconfigure(encoding='utf-8')
    OUT.mkdir(parents=True, exist_ok=True)
    manifest = ROOT/'src/audio-assets.json'
    before = digest(manifest)
    report_path = OUT/'provenance.json'
    report = json.loads(report_path.read_text('utf-8')) if report_path.exists() else dict(
        createdAt=datetime.now(timezone.utc).isoformat(), installedManifestSha256=before,
        status='Local audition only; no application audio replaced.',
        method='Qwen text-designed synthetic anchors reused unchanged with the Base model. No real-person audio conditioning. No pitch/formant/tempo processing.',
        clips=[], models={},
    )
    def checkpoint():
        assert digest(manifest) == before, 'Application manifest changed during audition'
        report_path.write_text(json.dumps(report, ensure_ascii=False, indent=2)+'\n', 'utf-8')
    model_name = 'Qwen3-TTS-12Hz-1.7B-'+('VoiceDesign' if args.stage=='design' else 'Base')
    folder = ROOT/'.models'/model_name
    report['models'][args.stage] = json.loads((folder/'revision.json').read_text('utf-8'))
    assert torch.cuda.is_available(), 'CUDA is required for this audition'
    torch.set_num_threads(4)
    model = Qwen3TTSModel.from_pretrained(str(folder), device_map='cuda:0', dtype=torch.bfloat16, attn_implementation='sdpa')
    for index, (identity, title, instruction) in enumerate(DESIGNS):
        if args.candidate and identity != args.candidate:
            continue
        anchor_path = OUT/f'{identity}-anchor.wav'
        if args.stage == 'design':
            if any(c['file']==anchor_path.name for c in report['clips']):
                continue
            seed_value = 16200+index
            seed(seed_value)
            wavs, rate = model.generate_voice_design(text=ANCHOR_TEXT, language='Chinese', instruct=instruction, max_new_tokens=650)
            record = save(anchor_path, wavs[0], rate)
            record.update(candidate=identity, title=title, kind='anchor', text=ANCHOR_TEXT, instruction=instruction, seed=seed_value)
            report['clips'].append(record)
            checkpoint()
            print('DESIGNED', identity, record['seconds'], flush=True)
        else:
            anchor_record = next(c for c in report['clips'] if c['file']==anchor_path.name)
            assert digest(anchor_path) == anchor_record['sha256']
            prompt = model.create_voice_clone_prompt(ref_audio=str(anchor_path), ref_text=ANCHOR_TEXT, x_vector_only_mode=False)
            for line_index, (label, text, pinyin, meaning) in enumerate(LINES):
                path = OUT/f'{identity}-{label}.wav'
                if any(c['file']==path.name for c in report['clips']):
                    continue
                seed_value = 16300+index*20+line_index
                seed(seed_value)
                wavs, rate = model.generate_voice_clone(text=text, language='Chinese', voice_clone_prompt=prompt, non_streaming_mode=True, max_new_tokens=240)
                record = save(path, wavs[0], rate)
                record.update(candidate=identity, title=title, kind=label, text=text, pinyin=pinyin, meaning=meaning, seed=seed_value, syntheticReferenceSha256=anchor_record['sha256'])
                report['clips'].append(record)
                checkpoint()
                print('REUSED', identity, label, record['seconds'], flush=True)
    del model
    gc.collect()
    torch.cuda.empty_cache()
    checkpoint()

if __name__ == '__main__':
    main()
