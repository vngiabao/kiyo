"""Two deeper auditions, rendered once from the unprocessed synthetic blend."""
from datetime import datetime, timezone
import argparse
from fractions import Fraction
import hashlib
import html
import json
from pathlib import Path
import sys

import librosa
import numpy as np
import pyloudnorm as pyln
from scipy.signal import resample_poly
import soundfile as sf

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / 'output/voice-b-refinement'
BASELINE = ROOT / 'output/voice-lower-clean'
OUT = ROOT / 'output/voice-lower-options'
OPTIONS = [('one', 'A · 1 semitone lower', -1.0),
           ('one-half', 'B · 1.5 semitones lower', -1.5)]
sys.stdout.reconfigure(encoding='utf-8')
OUT.mkdir(parents=True, exist_ok=True)

def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def pitch(signal, rate):
    signal = librosa.resample(signal.astype(np.float32), orig_sr=rate, target_sr=16000)
    values, voiced, probability = librosa.pyin(
        signal, fmin=60, fmax=600, sr=16000, frame_length=1024, hop_length=160)
    return values, voiced & (probability > .15)

def main():
    manifest = ROOT / 'src/audio-assets.json'
    before = digest(manifest)
    source = json.loads((SOURCE / 'provenance.json').read_text('utf-8'))
    baseline = json.loads((BASELINE / 'provenance.json').read_text('utf-8'))
    assert baseline['semitones'] == -1.75
    report = dict(createdAt=datetime.now(timezone.utc).isoformat(),
        status='Local audition only; neither option installed.',
        baseline='voice-lower-clean: -1.75 semitones from the original 85/15 synthetic blend.',
        method='Single-pass SciPy polyphase resampling from unprocessed 85/15 WAVs. No time stretching, formant correction, EQ or new synthesis. Pitch and resonance lower together. Loudness matched to baseline.',
        installedManifestSha256=before, clips=[])
    for row in source['clips']:
        take = next(t for t in row['takes'] if t['id'] == 'refined')
        path = SOURCE / take['file']
        assert digest(path) == take['sha256']
        original, rate = sf.read(path)
        base = next(c for c in baseline['clips'] if c['id'] == row['id'])
        base_path = BASELINE / base['file']
        assert digest(base_path) == base['sha256']
        base_audio, base_rate = sf.read(base_path)
        assert rate == base_rate == 24000
        meter = pyln.Meter(rate, block_size=min(.4, len(original) / rate / 2))
        target_lufs = float(meter.integrated_loudness(base_audio))
        original_f0, original_good = pitch(original, rate)
        result = dict(id=row['id'], text=row['text'], pinyin=row['pinyin'],
            meaning=row['meaning'], current=row['current'],
            baseline='../voice-lower-clean/' + base['file'],
            baselineSha256=base['sha256'], sourceFile='../voice-b-refinement/' + take['file'],
            sourceSha256=take['sha256'], takes=[])
        for key, label, relative in OPTIONS:
            shift = baseline['semitones'] + relative
            factor = 2 ** (shift / 12)
            ratio = Fraction(1 / factor).limit_denominator(10000)
            signal = resample_poly(original, ratio.numerator, ratio.denominator,
                                   window=('kaiser', 8.6))
            assert signal.ndim == 1 and np.isfinite(signal).all()
            assert abs(len(signal) / len(original) - 1 / factor) < .001
            gain = min(10 ** ((target_lufs - meter.integrated_loudness(signal)) / 20),
                       .94 / np.max(np.abs(signal)))
            dest = OUT / f'{row["id"]}-{key}.wav'
            sf.write(dest, signal * gain, rate, subtype='PCM_16')
            decoded, decoded_rate = sf.read(dest)
            assert decoded_rate == rate and .005 < np.max(np.abs(decoded)) < .95
            lufs = float(meter.integrated_loudness(decoded))
            assert abs(lufs - target_lufs) < .6
            new_f0, new_good = pitch(decoded, rate)
            indices = np.minimum(np.rint(np.arange(len(original_f0)) / factor).astype(int), len(new_f0)-1)
            valid = original_good & new_good[indices] & np.isfinite(original_f0) & np.isfinite(new_f0[indices])
            measured = float(np.median(12 * np.log2(new_f0[indices][valid] / original_f0[valid])))
            assert abs(measured - shift) < .45, (row['id'], measured, shift)
            result['takes'].append(dict(id=key, label=label, relativeSemitones=relative,
                totalSemitones=shift, relativeSpeed=2**(relative/12), ratio=str(ratio),
                file=dest.name, sha256=digest(dest), seconds=len(decoded)/rate,
                lufs=lufs, baselineLufs=target_lufs, measuredShiftFromOriginal=round(measured, 2)))
            print(row['id'], label, 'measured', round(measured, 2), flush=True)
        report['clips'].append(result)
    assert digest(manifest) == before
    (OUT / 'provenance.json').write_text(json.dumps(report, ensure_ascii=False, indent=2)+'\n', 'utf-8')
    render(report)

def render(report):
    esc = html.escape
    finalists = OPTIONS[0][2] == -.5
    sections = []
    for row in report['clips']:
        controls = [] if finalists else [('Previous audition', row['baseline'])]
        controls += [(t['label'], t['file']) for t in row['takes']]
        if row['current'] and not finalists:
            controls.append(('Current app reference', row['current']))
        players = ''.join(f'<div><h3>{esc(label)}</h3><audio controls preload="none" aria-label="{esc(label+" "+row["text"])}" src="{esc(url)}"></audio></div>' for label, url in controls)
        sections.append(f'<section id="{row["id"]}"><h2 lang="zh-CN">{esc(row["text"])}</h2><p>{esc(row["pinyin"])}</p><p>{esc(row["meaning"])}</p><div class="takes">{players}</div></section>')
    previous = (BASELINE / 'index.html').read_text('utf-8')
    style = previous.split('<style>')[1].split('</style>')[0]
    style = style.replace('max-width:1120px', 'max-width:1400px').replace('repeat(3,minmax(0,1fr))', 'repeat(4,minmax(0,1fr))')
    if finalists:
        style = style.replace('repeat(4,minmax(0,1fr))', 'repeat(2,minmax(0,1fr))').replace('max-width:1400px', 'max-width:1000px')
    title = 'The final two.' if finalists else 'Two deeper options.'
    introduction = ('<strong>0.5 semitone lower or 1 semitone lower.</strong> Both are measured from “Previous audition,” the same reference as the last page. The 1-semitone take is identical to the one you just heard. The new half-semitone option plays about 3% slower than that reference; the 1-semitone option about 6% slower.' if finalists else '<strong>A is 1 semitone lower. B is 1.5 semitones lower.</strong> Both changes are relative to the previous audition you just heard. A plays about 6% slower; B about 8% slower. The same performance and words stay in both.')
    totals = '−2.25 and −2.75' if finalists else '−2.75 and −3.25'
    page = f'''<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Sayo · {title}</title><style>{style}</style><main>
<a href="../voice-lower-clean/index.html">Back to the previous audition</a><h1>Two deeper options.</h1>
<p>{introduction}</p>
<p>Listen to <a href="#tones">声调呢？</a> for metallic texture. Both are made directly from the original blend with the simpler resampling approach, avoiding the earlier time-stretching process. Existing source artifacts may remain. The Current app reference stays alongside them; this adjusts pitch toward its register, without changing the identity blend.</p>
<p>Neither option is installed. Choose by sound, especially pronunciation and whether the deeper voice still feels friendly.</p>
{''.join(sections)}<details><summary>Processing and checks</summary><p>Total shifts from the original blend: {totals} semitones. Pitch and vocal resonance lower together. Single-pass resampling, no formant correction, matched loudness. Checks cover decoding, pitch direction, duration and hashes; they cannot certify naturalness or Mandarin tones.</p><a href="provenance.json">Audio provenance and checks</a></details></main><script>document.querySelectorAll('audio').forEach(a=>a.addEventListener('play',()=>document.querySelectorAll('audio').forEach(b=>{{if(a!==b)b.pause()}})))</script></html>'''
    page = page.replace('<h1>Two deeper options.</h1>', f'<h1>{title}</h1>')
    if finalists:
        page = page.replace('The Current app reference stays alongside them;', 'The previous audition is linked above;')
    (OUT / 'index.html').write_text(page, 'utf-8')

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--finalists', action='store_true')
    args = parser.parse_args()
    if args.finalists:
        OUT = ROOT / 'output/voice-final-showdown'
        OUT.mkdir(parents=True, exist_ok=True)
        OPTIONS = [('half', '0.5 semitone lower', -.5), ('one', '1 semitone lower', -1.0)]
    main()
