"""Test an authored repair in the existing unpublished combined shadow course."""
import argparse,json,runpy,shutil,subprocess,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
parser=argparse.ArgumentParser()
parser.add_argument('source')
parser.add_argument('units',nargs='+')
args=parser.parse_args()
source=ROOT/args.source
sys.path[:0]=[str(ROOT/'scripts/course-authoring'),str(source.parent)]
shadow=ROOT/'.cache/advanced-preflight'
sys.argv=[str(source),'--shadow']  # Draft only; never publish into the app.
ns=runpy.run_path(str(source),run_name='__main__')
def connected(v):
    if isinstance(v,dict):return ([v['zh']] if 'zh' in v else [])+[s for k,c in v.items() if k!='zh' for s in connected(c)]
    if isinstance(v,list):return [s for c in v for s in connected(c)]
    return []
for uid in args.units:
    path=ROOT/f'output/parity-editorial-drafts/{uid}.json'
    pack=json.loads(path.read_text('utf-8'))
    previous=ROOT/f'content/packs/{uid}.json'
    if not previous.exists():previous=ROOT/f'output/advanced-course-drafts/{uid}.json'
    old=json.loads(previous.read_text('utf-8'))
    assert [t['id'] for t in pack['tasks']]==[t['id'] for t in old['tasks']]
    assert [v['id'] for v in pack['vocabulary']]==[v['id'] for v in old['vocabulary']]
    context=[s for k in ['dialogue','reading','extraReadings','grammar','tasks'] for s in connected(pack[k])]
    for v in pack['vocabulary']:assert len({s for s in context if v['hanzi'] in s})>=2,(uid,v['hanzi'])
    shutil.copy2(path,shadow/'content/packs'/path.name)
# Merge authored definitions, not old whole packs that would undo other repairs.
for uid,terms in ns.get('DEPENDENCIES',{}).items():
    path=shadow/f'content/packs/{uid}.json'
    pack=json.loads(path.read_text('utf-8'))
    for text in [pack['dialogue'],pack['reading'],*pack['extraReadings']]:
        for word,meaning in terms:
            if any(word in l['zh'] for l in text['lines']) and not any(g['hanzi']==word for g in text.get('glosses',[])):
                text.setdefault('glosses',[]).append(dict(hanzi=word,pinyin=ns['py'](word),meaning=meaning))
    path.write_text(json.dumps(pack,ensure_ascii=False,indent=2)+'\n','utf-8')
for script in ['build-packs.ts','check-pinyin.ts']:
    result=subprocess.run(['node',str(ROOT/'node_modules/tsx/dist/cli.mjs'),str(ROOT/'scripts'/script)],cwd=shadow)
    if result.returncode:raise SystemExit(result.returncode)
print('Draft-only combined pack, readability and pinyin checks passed; audio and full batch gates remain.')
