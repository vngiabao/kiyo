"""Record gate-backed introduction evidence, never native approval or mastery."""
import argparse, hashlib, json
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
read = lambda p: json.loads(p.read_text('utf-8-sig'))
parser = argparse.ArgumentParser()
parser.add_argument('batch')
parser.add_argument('units', nargs='+')
parser.add_argument('--fixes', required=True)
args = parser.parse_args()
receipt = read(ROOT / f'output/gates/batch-{args.batch}-final-receipt.json')
required = {'packs','types','content','unit','playback-review','browser','build','production-browser'}
assert {r['gate'] for r in receipt} == required
assert all(r['exitCode'] == 0 for r in receipt), 'Unpassed gate'
for protected in read(ROOT / 'prompts/research/c2-protected-files.json'):
    assert hashlib.sha256((ROOT / protected['path']).read_bytes()).hexdigest() == protected['sha256'], protected['path'] + ' changed'
packs = [read(ROOT / f'content/packs/{u}.json') for u in args.units]
crosswalk_path = ROOT / 'prompts/research/grammar-crosswalk.json'
crosswalk = read(crosswalk_path)
for pack in packs:
    for card in pack['grammar']:
        code = card['id'].split('-g')[-1]
        row = next((r for r in crosswalk['evidence'] if r['code'] == code), None)
        if row is None:
            row = dict(code=code, cards=[])
            crosswalk['evidence'].append(row)
        if card['id'] not in row['cards']:
            row['cards'].append(card['id'])
        row.update(status='introduced', note='Explicit owner instruction and contrasting examples; AI-assisted draft, native review pending. Introduction is not mastery.')
crosswalk_path.write_text(json.dumps(crosswalk, ensure_ascii=False, indent=2)+'\n','utf-8')
log = ROOT / 'prompts/research/course-log.md'
heading = f'### Batch {args.batch} acceptance'
assert heading not in log.read_text('utf-8'), 'Already logged'
words = sum(len(p['vocabulary']) for p in packs)
chars = sum(len(p['characters']) for p in packs)
codes = [g['id'].split('-g')[-1] for p in packs for g in p['grammar']]
policy = read(ROOT / 'content/voices/audio-deferred.json')
with log.open('a', encoding='utf-8') as f:
    f.write(f'\n{heading} — {datetime.now(timezone.utc).date().isoformat()}\n\n')
    f.write(f'- Accepted {", ".join(args.units)}: {words} vocabulary records, {chars} explicit characters. Grammar owners: {", ".join(codes)}. Each includes original media writing and retrieval.\n')
    f.write(f'- Self-review and applied fixes: {args.fixes}\n')
    f.write(f'- All eight required gates passed; exact receipts and test counts: output/gates/batch-{args.batch}-final-*.log. Packs/pinyin and word readability remain strict; production-only checks ran separately against the final preview.\n')
    f.write(f'- Audio: {len(policy["entries"])} direct dated exceptions after a real repair. Failed takes remain uninstalled, reviewed:false. Dependent assemblies use the same explicit policy. Automatic transcript screening is not native tone certification.\n')
    f.write('- Native-review flags remain open:\n')
    for pack in packs:
        f.write(f'  - {pack["unit"]["id"]}: {pack["notes"]}\n')
