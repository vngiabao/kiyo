"""List actual contextual 得 uses for editorial review; grant no approval."""
import json
from pathlib import Path
from common import ROOT

shadow = ROOT / '.cache/advanced-finalisation-20261008-123747/content/packs'
contexts = {}
def walk(value, unit, location=''):
    if isinstance(value, dict):
        zh = value.get('zh', value.get('sentence', ''))
        if isinstance(zh, str) and '得' in zh:
            for i, char in enumerate(zh):
                if char == '得':
                    context = zh[max(0, i-5):i+6]
                    contexts.setdefault(context, []).append({'unit': unit, 'location': location, 'text': zh, 'py': value.get('py', '')})
        for key, child in value.items():
            walk(child, unit, location + '/' + key)
    elif isinstance(value, list):
        for i, child in enumerate(value):
            walk(child, unit, location + '/' + str(i))

for path in sorted(shadow.glob('*.json')):
    walk(json.loads(path.read_text('utf-8-sig')), path.stem)
destination = ROOT / 'output/contextual-de-audit.json'
destination.write_text(json.dumps(contexts, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
for context, entries in sorted(contexts.items()):
    print(f"{context}\t{entries[0]['unit']}\t{len(entries)}")
print('Exact line evidence:', destination)
