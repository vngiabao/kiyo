"""A narrow corpus correction; Chinese, IDs, keys and non-得 syllables stay intact."""
import argparse,json
from pathlib import Path
from contextual_de import ROOT,correct,reading

parser=argparse.ArgumentParser()
parser.add_argument('--root',type=Path,default=ROOT/'content/packs')
parser.add_argument('--write',action='store_true')
parser.add_argument('--report',type=Path,default=ROOT/'output/contextual-de-corrections.json')
args=parser.parse_args()
changes=[]
unresolved=set()
def walk(value,unit,location=''):
    if isinstance(value,dict):
        zh=next((value[k] for k in ['zh','text','sentence','hanzi'] if isinstance(value.get(k),str)),None)
        key=next((k for k in ['py','pinyin'] if isinstance(value.get(k),str)),None)
        if zh and key and '得' in zh:
            plain=zh.replace('【','').replace('】','')
            if plain!='得':
                for i,c in enumerate(plain):
                    if c=='得' and reading(plain,i) is None:unresolved.add((unit,plain[max(0,i-6):i+7]))
            before=value[key]
            after=correct(zh,before)
            if zh in ['舍不得','怪不得']:
                after={'舍不得':'shě bu de','怪不得':'guài bu de'}[zh]
            if before!=after:
                changes.append(dict(unit=unit,location=location,text=zh,before=before,after=after))
                value[key]=after
        for key,child in value.items():walk(child,unit,location+'/'+key)
    elif isinstance(value,list):
        for i,child in enumerate(value):walk(child,unit,location+'/'+str(i))

prepared=[]
for path in sorted(args.root.glob('*.json')):
    if path.name.startswith('_'):continue
    pack=json.loads(path.read_text('utf-8-sig'))
    before=len(changes)
    walk(pack,path.stem)
    if len(changes)>before:prepared.append((path,pack))
if unresolved:raise ValueError(('Unreviewed 得 contexts; do not write',sorted(unresolved)))
# Prepare everything successfully before replacing a single source file.
if args.write:
    for path,pack in prepared:path.write_text(json.dumps(pack,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
report=args.report
report.write_text(json.dumps(dict(applied=args.write,root=str(args.root),changes=changes),ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(f'{len(changes)} pinyin fields in {len(prepared)} packs; applied={args.write}. Chinese and assessment IDs unchanged. Evidence: {report}')
