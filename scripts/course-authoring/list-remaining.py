"""Print unallocated official source entries without changing course assets."""
import argparse
import re
import common

parser=argparse.ArgumentParser()
parser.add_argument('--through',type=int,default=17)
args=parser.parse_args()
used=set()
chars=set()
def capture(uid,*values):
    p=next(u for u in common.plan['units'] if u['id']==uid)
    for word in common.vocab(values[2],uid,p['gfLevel']):
        m=re.search(r'\[GF2021:L(\d+):(\d+)\]',word['usageNote'])
        used.add((int(m[1]),m[2]))
    chars.update(c for c,_ in common.character_groups[uid])
common.write=capture
for batch in range(15,args.through+1):
    path=common.ROOT/f'scripts/course-authoring/batch-{batch:02}.py'
    source=path.read_text('utf-8').split('from retrievals import')[0]
    source=source.replace('from common import *','from common import *\nwrite=capture',1)
    exec(compile(source,str(path),'exec'),{'capture':capture,'__file__':str(path)})
for e in common.baseline['levels'][2]['words']['remainingEntries']:
    if (3,e['sourceNo']) not in used:
        print(e['sourceNo'],e['entry'],e['pinyin'],e['partOfSpeech'])
print('CHARACTERS',''.join(c for c in common.baseline['levels'][2]['characters']['remaining'] if c not in chars))
