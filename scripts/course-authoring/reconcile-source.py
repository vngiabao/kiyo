"""Apply narrowly sourced lookup corrections; never replace minimum levels by senses."""
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
inventory=json.loads((ROOT/'prompts/research/gf2021-inventory.json').read_text('utf-8'))
lookup=ROOT/'content/hsk/levels.json'
data=json.loads(lookup.read_text('utf-8'))
row=next(r for r in inventory['levels']['2']['words'] if r[0]=='446')
assert row[2:]==['表示','biǎoshì','动、名'], row
entry=data['words']['表示']
assert entry.get('hsk3') in [None,2]
entry['hsk3']=2
later=next(r for r in inventory['levels']['2']['words'] if r[2]=='一会儿')
assert later[3]=='yíhuìr'
readings=data['words']['一会儿']['pinyin']
if 'yí huì r' not in readings:
    readings.append('yí huì r')
correction=' GF0025-2021 official query corrections (2026-10-06): 表示 level 2, source row 446; 一会儿 alternate yíhuìr in the level-2 row. Evidence: prompts/research/gf2021-inventory.json; https://admin.chinesetest.cn/newhsk/standardsAction.do?means=standardInfo.'
if correction not in data['note']:
    data['note']+=correction
# Preserve the source's level-1 spelling and all prior alternative readings.
lookup.write_text(json.dumps(data,ensure_ascii=False,separators=(',',':'))+'\n','utf-8')
print('Reconciled 表示 L2 source 446; added the official L2 一会儿 reading.')
