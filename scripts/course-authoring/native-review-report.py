"""Expose exact native-review candidates; never grant linguistic approval."""
import json,re
from common import ROOT,read

rows=[]
for path in sorted((ROOT/'content/packs').glob('s*-u*.json')):
    pack=read(path)
    note=pack.get('notes','Native review pending.')
    terms=re.findall(r'[\u4e00-\u9fff]{2,}',note)
    candidates=[]
    def walk(value):
        if isinstance(value,dict):
            if all(k in value for k in ['zh','py','en']):candidates.append(value)
            for child in value.values():walk(child)
        elif isinstance(value,list):
            for child in value:walk(child)
    for field in ['grammar','dialogue','reading','extraReadings']:walk(pack.get(field))
    flagged=[line for line in candidates if any(term in line['zh'] for term in terms)
             or any(term in line['zh'] for term in ['还书','还笔','还回来','还的书','还给','还你'])]
    if not flagged:flagged=candidates[:2]
    seen=set()
    for line in flagged:
        if line['zh'] in seen:continue
        seen.add(line['zh'])
        return_note = (' Contextual 还 should be huán for returning an object; verify the actual recorded tone, not just the displayed pinyin.'
                       if any(term in line['zh'] for term in ['还书','还笔','还回来','还的书','还给','还你']) else '')
        rows.append(dict(unit=pack['unit']['id'],text=line['zh'],py=line['py'],en=line['en'],reason=note+return_note,status='native review pending'))
for path in sorted((ROOT/'content/packs').glob('hsk-*-bank.hsk.json')):
    bank=read(path)
    for item in bank['items']:
        # Exact connected prompts make the unresolved native-review scope clear.
        rows.append(dict(unit=item['id'],text=item['sentence'],py=item['py'],en=item['en'],
                         prompt=item['prompt'],choices=item['choices'],answer=item['answer'],
                         reason='Original exam draft: check naturalness, tone delivery and whether the distractors admit another valid interpretation.',
                         status='native review pending'))
for exception in read(ROOT/'content/voices/audio-deferred.json')['entries']:
    rows.append(dict(unit='audio exception',text=exception['text'],reason=exception.get('reason','Automatic screening failed after repair; device speech fallback.'),status='native review pending'))
destination=ROOT/'prompts/research/native-review-lines.json'
destination.write_text(json.dumps(dict(status='All course drafts remain AI-assisted; this is a prioritised exact-line list, not a declaration that unlisted lines have native approval.',lines=rows),ensure_ascii=False,indent=2)+'\n','utf-8')
print(f'{len(rows)} exact-line native-review candidates recorded. None marked reviewed.')
