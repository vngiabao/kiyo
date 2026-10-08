"""Preflight unpublished replacements with the unchanged pack/pinyin scripts.

Only an ignored shadow tree is written. This is not full batch acceptance.
"""
import argparse,os,shutil,subprocess,sys,json
from pathlib import Path
from common import ROOT
parser=argparse.ArgumentParser()
parser.add_argument('units',nargs='+')
parser.add_argument('--source-dir',choices=['parity-editorial-drafts','advanced-course-drafts'],default='parity-editorial-drafts')
args=parser.parse_args()
shadow=ROOT/'.cache'/('advanced-preflight' if args.source_dir=='advanced-course-drafts' else 'parity-preflight')
def connected(value):
    if isinstance(value,dict):
        return ([value['zh']] if 'zh' in value else [])+[s for k,v in value.items() if k!='zh' for s in connected(v)]
    if isinstance(value,list):return [s for v in value for s in connected(v)]
    return []
for relative in ['content/packs','content/hsk','public/dict']:
    shutil.copytree(ROOT/relative,shadow/relative,dirs_exist_ok=True)
for name in args.units:
    source=ROOT/'output'/args.source_dir/f'{name}.json'
    shutil.copy2(source,shadow/'content/packs'/source.name)
    pack=json.loads(source.read_text('utf-8'))
    assert len(pack['dialogue']['questions'])==len(pack['reading']['questions'])==3
    lines=[s for key in ['dialogue','reading','extraReadings','grammar','tasks'] for s in connected(pack.get(key))]
    for word in pack['vocabulary']:
        assert len({s for s in lines if word['hanzi'] in s})>=2,(name,word['hanzi'],'needs two authored contexts')
# Junction avoids copying the toolchain; source modules resolve from the real repo.
modules=shadow/'node_modules'
if not modules.exists():
    subprocess.run(['cmd','/c','mklink','/J',str(modules),str(ROOT/'node_modules')],check=True,capture_output=True)
for script in ['build-packs.ts','check-pinyin.ts']:
    subprocess.run(['node',str(ROOT/'node_modules/tsx/dist/cli.mjs'),str(ROOT/'scripts'/script)],cwd=shadow,check=True)
print('Editorial preflight passed. No published course or audio changed.')
