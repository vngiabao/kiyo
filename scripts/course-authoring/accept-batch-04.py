"""Record completed gate receipts and conservative grammar introduction evidence."""
import json
from pathlib import Path
ROOT = Path(__file__).resolve().parents[2]
p = ROOT / 'prompts/research/grammar-crosswalk.json'
d = json.loads(p.read_text('utf-8'))
for n in range(25, 29):
    pack = json.loads((ROOT / f'content/packs/s1-u{n:02}.json').read_text('utf-8'))
    for card in pack['grammar']:
        code = card['id'].split('-g')[-1]
        row = next((x for x in d['evidence'] if x['code'] == code), None)
        if row is None:
            row = dict(code=code, cards=[])
            d['evidence'].append(row)
        if card['id'] not in row['cards']:
            row['cards'].append(card['id'])
        row['status'] = 'introduced'
        row['note'] = 'Explicit instruction and contrasting examples in the accepted owner card; AI-assisted draft, native review pending. Introduction is not mastery.'
p.write_text(json.dumps(d, ensure_ascii=False, indent=2)+'\n', 'utf-8')
log = ROOT / 'prompts/research/course-log.md'
with log.open('a', encoding='utf-8') as f:
    f.write('''
### Batch 04 acceptance — 6 October

- Accepted s1-u25–s1-u28: 68 vocabulary records, 56 explicit characters, ten grammar families. Owners: 一09 degree, 一30 adjective predicates, 一35 exclamations, 一18 比, 一38 comparisons, 一10 collective adverbs, 一39 parallel clauses, 一22 particles, 一33 question forms, 一45 吗. Each unit includes an original scene/verse and concrete retrieval of earlier instruction.
- Self-review fixes: ordinary meanings for 普通/练/但/另/湿/让/选/发; added an actual 看见 context; corrected 先不知道 to 还不知道 and a misleading Mandarin-study adjective example. Compared localizers, comparison reference sets and dialogue details; no invented grades or readiness claims.
- All required gates passed: packs and pinyin with no fixes, word readability at least 95%, types, content/audio, 130 unit tests, 34 browser tests, production build and the three separately required production browser checks. Receipts: output/gates/batch-04-final-*.log. The three conditional production tests in the dev run were run against the final preview, not omitted.
- Installed 6,839 screened/mastered files, 125,917,300 bytes. After a real repair round, nine additional exact texts remain documented device-speech exceptions (19 direct exceptions total; 27 texts including dependent assemblies). Failed takes are not installed and exceptions remain reviewed:false. These are explicit owner-approved audio exceptions; other gates remain strict. Automatic ASR is not native tone certification.
- Native flags: reference sets for 最好/最好看; 饭店 restaurant versus hotel; formal 小姐; clipped original poetry; 一块儿/一下儿 pronunciation; directional/polyphonic verbs. Exact unresolved speech is in content/voices/audio-deferred.json, with dated reasons and repair receipts. Earlier flags remain open.
- All five protected A/B files match their C2-start hashes. No learner data or database name changed, no dependency or paid service added. New-course acceptance is 16/96; 80 remain. Level 1 deployment follows its final two units.
''')
