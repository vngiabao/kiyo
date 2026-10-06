"""Run the unchanged pack/pinyin validators on unpublished editorial sources.

This preflight writes only an ignored shadow tree, leaving the current audio and
browser gate inputs stable. It is not an acceptance receipt.
"""
import argparse
import shutil
import subprocess
import common

parser=argparse.ArgumentParser()
parser.add_argument('batches',nargs='+',type=int)
parser.add_argument('--exam',type=int,choices=[1,2,3])
args=parser.parse_args()
actual=common.ROOT
shadow=actual/'.cache'/('course-editorial-'+ '-'.join(f'{b:02}' for b in args.batches))
shadow.mkdir(parents=True,exist_ok=True)
for relative in ['content/packs','content/hsk','public/dict']:
    shutil.copytree(actual/relative,shadow/relative,dirs_exist_ok=True)
for relative in ['src/content.ts','content/audio-scripts.json']:
    dest=shadow/relative
    dest.parent.mkdir(parents=True,exist_ok=True)
    shutil.copy2(actual/relative,dest)
# Only stroke JSON is needed by the editorial serializer and pack validator.
shutil.copytree(actual/'node_modules/hanzi-writer-data',shadow/'node_modules/hanzi-writer-data',dirs_exist_ok=True)
common.ROOT=shadow
import retrievals
retrievals.ROOT=shadow
for batch in args.batches:
    path=actual/f'scripts/course-authoring/batch-{batch:02}.py'
    exec(compile(path.read_text('utf-8'),str(path),'exec'),{'__file__':str(path)})
if args.exam:
    name=f'hsk-{args.exam}-bank.hsk.json'
    shutil.copy2(actual/'.cache/course-authoring'/name,shadow/'content/packs'/name)
print('Unpublished shadow:',shadow,flush=True)

# Mirror the existing acceptance test before spending time generating audio.
# A vocabulary introduction alone is not a second context.
def connected(value):
    if isinstance(value,dict):
        return ([value['zh']] if 'zh' in value else []) + [s for k,v in value.items() if k!='zh' for s in connected(v)]
    if isinstance(value,list):return [s for v in value for s in connected(v)]
    return []
for path in sorted((shadow/'content/packs').glob('s*.json')):
    pack=common.read(path)
    if not any(u['id']==pack['unit']['id'] for u in common.plan['units']):continue
    assert 8<=len(pack['tasks'])<=10,(pack['unit']['id'],'task budget')
    context=[s for key in ['dialogue','reading','extraReadings','grammar','tasks'] for s in connected(pack.get(key))]
    for word in pack['vocabulary']:
        assert len({s for s in context if word['hanzi'] in s})>=2,(pack['unit']['id'],word['hanzi'],'distinct contexts')
tsx=actual/'node_modules/.bin/tsx.cmd'
for script in ['build-packs.ts','check-pinyin.ts']:
    result=subprocess.run([str(tsx),str(actual/'scripts'/script)],cwd=shadow)
    if result.returncode:
        raise SystemExit(result.returncode)
print('Editorial preflight passed; audio and all acceptance gates are still required.')
