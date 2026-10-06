"""Check unpublished editorial allocations without changing app content."""
import argparse
import re
import common

parser=argparse.ArgumentParser()
parser.add_argument('batches',nargs='+',type=int)
args=parser.parse_args()
used_chars=set()
used_words={}
used_sources={}

def drywrite(uid,*values):
    plan=next(u for u in common.plan['units'] if u['id']==uid)
    words=common.vocab(values[2],uid,plan['gfLevel'])
    assert len(words)==plan['wordBudget'],uid
    if plan['gfLevel']==2:
        unit_number=int(uid.split('u')[-1])
        assert len(common.character_groups[uid])==(9 if unit_number<=27 else 8),(uid,'character allocation budget')
    if plan['gfLevel']==3:
        unit_number=int(uid.split('u')[-1])
        assert len(common.character_groups[uid])==(7 if unit_number<=35 else 6),(uid,'character allocation budget')
    for word in words:
        source = re.search(r'\[GF2021:L(\d+):(\d+)\]',word['usageNote'])
        assert source, (uid,word['hanzi'],'missing official source citation')
        key=(source[1],source[2])
        assert key not in used_sources,(uid,word['hanzi'],'source entry already allocated',used_sources.get(key))
        used_sources[key]=uid
        # Polyphonic/grammatical source rows may intentionally reuse a form;
        # the final coverage audit must still verify the new reading and sense.
        old=used_words.setdefault(word['hanzi'],uid)
        if old!=uid: print('Repeated form; check cited sense:',uid,word['hanzi'],old)
    for ch,_ in common.character_groups[uid]:
        assert ch in common.baseline['levels'][plan['gfLevel']-1]['characters']['remaining'],(uid,ch,'not remaining at source level')
        assert ch not in used_chars,(uid,ch,'duplicate character introduction')
        used_chars.add(ch)
    print(uid,'allocation preflight:',len(words),'words')

common.write=drywrite
for batch in args.batches:
    path=common.ROOT/f'scripts/course-authoring/batch-{batch:02}.py'
    source=path.read_text('utf-8').split('from retrievals import')[0]
    source=source.replace('from common import *','from common import *\nwrite=drywrite',1)
    exec(compile(source,str(path),'exec'),{'drywrite':drywrite,'__file__':str(path)})
