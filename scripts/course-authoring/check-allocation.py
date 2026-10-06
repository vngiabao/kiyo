"""Check unpublished editorial allocations without changing app content."""
import argparse
import common

parser=argparse.ArgumentParser()
parser.add_argument('batches',nargs='+',type=int)
args=parser.parse_args()
used_chars=set()
used_words={}

def drywrite(uid,*values):
    plan=next(u for u in common.plan['units'] if u['id']==uid)
    words=common.vocab(values[2],uid,plan['gfLevel'])
    assert len(words)==plan['wordBudget'],uid
    for word in words:
        # Polyphonic/grammatical source rows may intentionally reuse a form;
        # the final coverage audit must still verify the new reading and sense.
        old=used_words.setdefault(word['hanzi'],uid)
        if old!=uid: print('Repeated form; check cited sense:',uid,word['hanzi'],old)
    for ch,_ in common.character_groups[uid]:
        assert ch in common.baseline['levels'][plan['gfLevel']-1]['characters']['remaining'],(uid,ch,'not remaining at source level')
        assert ch not in used_chars,(uid,ch,'duplicate character introduction')
        used_chars.add(ch)
    print(uid,'allocation preflight:',len(words),'words')

for batch in args.batches:
    path=common.ROOT/f'scripts/course-authoring/batch-{batch:02}.py'
    source=path.read_text('utf-8').split('from retrievals import')[0]
    source=source.replace('from common import *','from common import *\nwrite=drywrite',1)
    exec(compile(source,str(path),'exec'),{'drywrite':drywrite,'__file__':str(path)})
