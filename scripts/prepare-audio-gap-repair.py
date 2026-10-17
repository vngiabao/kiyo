"""Queue one genuine new clear take for each explicitly deferred exact text.

Keep the approved speaker/profile and every other mood recipe unchanged. Short
targets use a pronunciation-matched carrier; only its last clause can be installed.
"""
from datetime import datetime, timezone
from pathlib import Path
import hashlib
import json
import re
import shutil
import sys

from pypinyin import lazy_pinyin, Style
from pypinyin.contrib.tone_convert import to_tone3

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'output/audio-gap-repair'
read = lambda p: json.loads(p.read_text('utf-8'))
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
key = lambda text: re.sub(r'[\s，。！？,.!?、]', '', text)

def main():
    sys.stdout.reconfigure(encoding='utf-8')
    OUT.mkdir(parents=True, exist_ok=True)
    marker = OUT / 'baseline.json'
    if marker.exists():
        raise SystemExit('A repair baseline already exists; resume its queued recipes instead of incrementing again.')
    scripts = read(ROOT/'content/audio-scripts.json')
    entries = {key(e['text']): e for e in scripts}
    policy = read(ROOT/'content/voices/audio-deferred.json')
    retries_path = ROOT/'content/voices/approved-b-half/retries.json'
    contexts_path = ROOT/'content/voices/approved-b-half/pronunciation-contexts.json'
    retries, contexts = read(retries_path), read(contexts_path)
    backup = OUT/'before'
    backup.mkdir(exist_ok=True)
    protected = [ROOT/'src/audio-assets.json', ROOT/'public/audio-v2/assets.json',
        ROOT/'content/audio-provenance.json', ROOT/'content/voices/sayo-library-provenance.json',
        ROOT/'content/voices/audio-deferred.json', ROOT/'content/voices/released-audio-compatibility.json',
        retries_path, contexts_path]
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
        take = int(retries.get(token, 0))+1
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
        if len(clean) <= 3:
            carrier = carrier or '我说的是'+text.rstrip('。！？!?')
            cue.update(synthesisText=carrier.rstrip('。！？!?')+'。'+text.rstrip('。！？!?')+'。',
                       extract='last-clause',
                       reason='Pronunciation-matched natural carrier; retain and screen only the final exact target.')
        retries[token] = take
        contexts[token] = cue
        queued.append(dict(text=text, token=token, take=take, carrier=carrier,
                           authoredPinyin=entry.get('pinyin'), context=cue))
    report = dict(startedAt=datetime.now(timezone.utc).isoformat(), beforeHashes=hashes,
                  approvedProfileSha256=sha(ROOT/'content/voices/approved-b-half/profile.json'),
                  rosterSha256=sha(ROOT/'content/voices/sayo-roster-staged.json'), queued=queued,
                  directDeferred=len(policy['texts']), scripts=len(scripts))
    marker.write_text(json.dumps(report, ensure_ascii=False, indent=2)+'\n', 'utf-8')
    for path, data in [(retries_path, retries), (contexts_path, contexts)]:
        path.write_text(json.dumps(data, ensure_ascii=False, indent=2)+'\n', 'utf-8')
    print(f'Queued {len(queued)} genuine new clear takes; {sum(q["context"]["extract"]=="last-clause" for q in queued)} use cropped carriers.')

if __name__ == '__main__':
    main()
