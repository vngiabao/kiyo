"""Queue one genuine new clear take for each explicitly deferred exact text.

Keep the approved speaker/profile and every other mood recipe unchanged. Short
targets use a pronunciation-matched carrier; only its last clause can be installed.
"""
from datetime import datetime, timezone
import argparse
from pathlib import Path
import hashlib
import json
import re
import shutil
import sys

from pypinyin import lazy_pinyin, Style
from pypinyin.contrib.tone_convert import to_tone3

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT/'scripts/course-authoring'))
from contextual_de import SYLLABLE
read = lambda p: json.loads(p.read_text('utf-8'))
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
key = lambda text: re.sub(r'[\s，。！？,.!?、]', '', text)

def next_take(token,retries,highest):
    return max(int(retries.get(token,0)),int(highest.get(token,0)))+1

def checked_cue(text, cue, authored_pinyin=None):
    assert re.fullmatch(r'[\u4e00-\u9fff。，！？、；：\s]+', cue), 'Cue contains unverified spoken material: '+text
    clean = lambda value: re.sub(r'[^\u4e00-\u9fff]', '', value)
    tones = lambda value: lazy_pinyin(clean(value), style=Style.TONE3, neutral_tone_with_five=True)
    expected = tones(text)
    assert expected == tones(cue), 'Cue changes the target syllables or tones: '+text
    if authored_pinyin:
        authored = [to_tone3(m.group().lower(), neutral_tone_with_five=True) for m in SYLLABLE.finditer(authored_pinyin)]
        original, replacement = clean(text), clean(cue)
        assert len(original) == len(replacement) == len(expected) == len(authored), 'Cue needs aligned authored syllables: '+text
        # Unchanged syllables may carry authored sandhi (e.g. 一点 yìdiǎn).
        # Every replaced glyph must still match the authored target's tone.
        assert all(expected[i] == authored[i] for i in range(len(original)) if original[i] != replacement[i]), 'Cue needs an unambiguous authored reading: '+text
    return cue

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--run-id', default='audio-gap-repair')
    parser.add_argument('--reference-delivery', action='store_true')
    parser.add_argument('--whole-short', action='store_true')
    parser.add_argument('--temperature', type=float)
    parser.add_argument('--cue-file', type=Path)
    parser.add_argument('--cues-only', action='store_true')
    parser.add_argument('--cue-carriers', action='store_true')
    args = parser.parse_args()
    if args.temperature is not None and not .05 <= args.temperature <= 1:
        parser.error('Temperature must be between 0.05 and 1.')
    if not re.fullmatch(r'[a-z0-9][a-z0-9-]*', args.run_id):
        parser.error('Run id must be a simple lowercase folder name.')
    out = ROOT / 'output' / args.run_id
    sys.stdout.reconfigure(encoding='utf-8')
    out.mkdir(parents=True, exist_ok=True)
    marker = out / 'baseline.json'
    if marker.exists():
        raise SystemExit('A repair baseline already exists; resume its queued recipes instead of incrementing again.')
    scripts = read(ROOT/'content/audio-scripts.json')
    entries = {key(e['text']): e for e in scripts}
    policy = read(ROOT/'content/voices/audio-deferred.json')
    cues = read(args.cue_file) if args.cue_file else {}
    if args.cues_only:
        if not cues:parser.error('--cues-only requires a nonempty --cue-file.')
        policy = dict(policy, texts=[text for text in policy['texts'] if text in cues])
    for text in policy['texts']:
        if text in cues:
            checked_cue(text, cues[text], entries[key(text)].get('pinyin'))
    retries_path = ROOT/'content/voices/approved-b-half/retries.json'
    contexts_path = ROOT/'content/voices/approved-b-half/pronunciation-contexts.json'
    retries, contexts = read(retries_path), read(contexts_path)
    highest_path = ROOT/'content/voices/approved-b-half/highest-takes.json'
    highest = read(highest_path) if highest_path.exists() else {}
    backup = out/'before'
    backup.mkdir(exist_ok=True)
    protected = [ROOT/'src/audio-assets.json', ROOT/'public/audio-v2/assets.json',
        ROOT/'content/audio-provenance.json', ROOT/'content/voices/sayo-library-provenance.json',
        ROOT/'content/voices/audio-deferred.json', ROOT/'content/voices/released-audio-compatibility.json',
        retries_path, contexts_path]
    if highest_path.exists():protected.append(highest_path)
    hashes = {}
    for source in protected:
        rel = source.relative_to(ROOT)
        target = backup/rel
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, target)
        hashes[rel.as_posix()] = sha(source)
    dictionary = read(ROOT/'content/hsk/levels.json')['words']
    queued = []
    for text in policy['texts']:
        entry = entries[key(text)]
        assert not entry.get('parts'), 'Repair source lines, not assembled passages.'
        assert 'clear' in entry['moods'], text
        token = entry['id']+'-clear'
        take = next_take(token,retries,highest)
        highest[token] = take
        clean = re.sub(r'[^\u4e00-\u9fff]', '', text)
        cue = dict(synthesisText=text, extract='whole', promptMode='speaker-only',
                   sampling=dict(temperature=.55, subtalker_temperature=.55),
                   reason='Fresh accuracy-first local repair; approved fixed speaker and mastering preserved.')
        carrier = None
        if len(clean) == 1:
            authored = entry.get('pinyin', '').strip()
            wanted = to_tone3(authored).lower() if authored else lazy_pinyin(clean, style=Style.TONE3)[0]
            candidates = []
            for word, row in dictionary.items():
                if clean not in word or len(word) not in (2, 3) or '儿' in word:
                    continue
                for py in row['pinyin']:
                    syllables = py.lower().split()
                    at = word.index(clean)
                    if len(syllables) == len(word) and to_tone3(syllables[at]) == wanted:
                        candidates.append((row.get('hsk3', 99), len(word), at, word))
            if candidates:
                carrier = min(candidates)[-1]
        elif len(clean) <= 3:
            candidates = [e['text'] for e in scripts if clean in e['text']
                          and not e.get('parts') and 6 <= len(key(e['text'])) <= 16
                          and not re.search(r'[A-Za-z【】]', e['text'])]
            if candidates:
                carrier = min(candidates, key=lambda t: (len(key(t)), t))
        if len(clean) <= 3 and not args.whole_short:
            carrier = carrier or '我说的是'+text.rstrip('。！？!?')
            cue.update(synthesisText=carrier.rstrip('。！？!?')+'。'+text.rstrip('。！？!?')+'。',
                       extract='last-clause',
                       reason='Pronunciation-matched natural carrier; retain and screen only the final exact target.')
        if args.reference_delivery:
            # Keep the same checked speaker embedding and approved anchor codes.
            # Only the synthesis recipe changes; the screen and mastering do not.
            cue.update(promptMode='reference',
                       sampling=dict(temperature=.7, subtalker_temperature=.7),
                       reason='Fresh take using approved anchor delivery; screen the exact target before installation.')
        if args.temperature is not None:
            cue['sampling'] = dict(temperature=args.temperature, subtalker_temperature=args.temperature)
        if text in cues:
            cue.update(synthesisText=cues[text], extract='whole',
                       reason='Written pronunciation cue verified against the exact authored syllables and tones; same fixed speaker and screen.')
            if args.cue_carriers and len(clean) <= 3:
                spoken = re.sub(r'[^\u4e00-\u9fff]', '', cues[text])
                cue_carrier = carrier
                if len(spoken) == 1:
                    wanted = lazy_pinyin(spoken, style=Style.TONE3, neutral_tone_with_five=True)[0]
                    candidates = []
                    for word, row in dictionary.items():
                        if spoken not in word or len(word) not in (2, 3) or '儿' in word:continue
                        for py in row['pinyin']:
                            syllables = py.lower().split()
                            at = word.index(spoken)
                            if len(syllables) == len(word) and to_tone3(syllables[at], neutral_tone_with_five=True) == wanted:
                                candidates.append((row.get('hsk3', 99), len(word), at, word))
                    if candidates:cue_carrier = min(candidates)[-1]
                cue_carrier = cue_carrier or '我说的是'+spoken
                cue.update(synthesisText=cue_carrier.rstrip('。！？!?')+'。'+spoken+'。', extract='last-clause',
                           reason='Pronunciation-matched carrier followed by a tone-checked written cue; only the exact target sounds may be retained and screened.')
        retries[token] = take
        contexts[token] = cue
        queued.append(dict(text=text, token=token, take=take, carrier=carrier,
                           authoredPinyin=entry.get('pinyin'), context=cue))
    report = dict(startedAt=datetime.now(timezone.utc).isoformat(), beforeHashes=hashes,
                  approvedProfileSha256=sha(ROOT/'content/voices/approved-b-half/profile.json'),
                  rosterSha256=sha(ROOT/'content/voices/sayo-roster-staged.json'), queued=queued,
                  directDeferred=len(policy['texts']), scripts=len(scripts))
    marker.write_text(json.dumps(report, ensure_ascii=False, indent=2)+'\n', 'utf-8')
    for path, data in [(retries_path, retries), (contexts_path, contexts), (highest_path, highest)]:
        path.write_text(json.dumps(data, ensure_ascii=False, indent=2)+'\n', 'utf-8')
    print(f'Queued {len(queued)} genuine new clear takes; {sum(q["context"]["extract"]=="last-clause" for q in queued)} use cropped carriers.')

if __name__ == '__main__':
    main()
