"""Exercise first-publication editorial layers in an isolated local draft copy."""
import json,runpy,shutil,subprocess,sys
from datetime import datetime,timezone
from pathlib import Path
import advanced_core,advanced_reading_repair
import common
from common import py

assert 'jiāo huán' in py('交还袋子以后，我还要看书。')
assert 'wǒ men hái yào' in py('线一起还回去，我们还要练。')
assert 'huán huí qù' in py('线一起还回去，我们还要练。')
assert 'dīng zhe' in py('她盯着表，说这回得改一下。')
assert 'zhè huí děi' in py('她盯着表，说这回得改一下。')

ROOT=Path(__file__).resolve().parents[2]
shadow=ROOT/'.cache'/('advanced-finalisation-'+datetime.now(timezone.utc).strftime('%Y%m%d-%H%M%S'))
for directory in ['content/packs','output/advanced-course-drafts']:
    def unpublished_groups(folder,names):
        if directory!='content/packs':return []
        return [name for name in names if name.startswith('s6-u') or name in [f's5-u{n:02}.json' for n in range(5,13)]]
    shutil.copytree(ROOT/directory,shadow/directory,ignore=unpublished_groups)
(shadow/'scripts/course-authoring').mkdir(parents=True)
for directory in ['content/hsk','public/dict','node_modules/hanzi-writer-data']:
    shutil.copytree(ROOT/directory,shadow/directory)
for n in range(16,21):
    shutil.copy2(ROOT/f'scripts/course-authoring/parity-repair-{n:02}.py',shadow/f'scripts/course-authoring/parity-repair-{n:02}.py')
result=subprocess.run([sys.executable,str(ROOT/'scripts/course-authoring/repair-de-pinyin.py'),'--root',str(shadow/'content/packs'),'--write'])
assert result.returncode==0,'Existing shadow corpus contextual pinyin correction failed'
common.ROOT=advanced_core.ROOT=advanced_reading_repair.ROOT=shadow
for level,start,end in [(5,5,12),(6,1,12)]:
    if level==5:
        source=ROOT/'scripts/course-authoring/parity-repair-15.py'
        import common
        original_common_root=common.ROOT
        common.ROOT=shadow
        sys.argv=[str(source),'--publish']
        try:runpy.run_path(str(source),run_name='__main__')
        finally:common.ROOT=original_common_root
        for name in ['build-packs.ts','check-pinyin.ts','check-contextual-pinyin.ts']:
            log=shadow/f'5-04-editorial-{name}.log'
            with log.open('w',encoding='utf-8') as output:
                result=subprocess.run(['node',str(ROOT/'node_modules/tsx/dist/cli.mjs'),str(ROOT/'scripts'/name)],cwd=shadow,stdout=output,stderr=subprocess.STDOUT)
            assert result.returncode==0,(5,'editorial15',name,str(log))
    for number in range(start,end+1):
        source=ROOT/f'scripts/course-authoring/advanced-{level}-{number:02}.py'
        sys.argv=[str(source),'--publish']
        runpy.run_path(str(source),run_name='__main__')
        if level==5:
            assert not list((shadow/'content/packs').glob('s6-u*.json')), 'A dependency published a future level early'
        if number%4==0:
            # A full-course shadow can hide a missing gloss behind a later unit.
            # Validate each published prefix before the next group exists.
            for name in ['build-packs.ts','check-pinyin.ts','check-contextual-pinyin.ts']:
                log=shadow/f'{level}-{number:02}-{name}.log'
                with log.open('w',encoding='utf-8') as output:
                    result=subprocess.run(['node',str(ROOT/'node_modules/tsx/dist/cli.mjs'),str(ROOT/'scripts'/name)],cwd=shadow,stdout=output,stderr=subprocess.STDOUT)
                assert result.returncode==0,(level,number,name,str(log))
    for number in range(start,end+1):
        uid=f's{level}-u{number:02}'
        pack=json.loads((shadow/f'content/packs/{uid}.json').read_text('utf-8'))
        original=json.loads((ROOT/f'output/advanced-course-drafts/{uid}.json').read_text('utf-8'))
        assert 'advanced reading self-review' in pack['notes'],uid
        for key in ['vocabulary','tasks','grammar']:
            assert [r['id'] for r in pack[key]]==[r['id'] for r in original[key]],(uid,key)
        for section in [pack['reading'],pack['extraReadings'][-1]]:
            assert sum('\u3400'<=c<='\u9fff' for l in section['lines'] for c in l['zh'])>={5:600,6:900}[level]
import common,editorial_repair
common.ROOT=editorial_repair.ROOT=shadow
for number in range(3,15):
    source=ROOT/f'scripts/course-authoring/parity-repair-{number:02}.py'
    sys.argv=[str(source),'--publish']
    runpy.run_path(str(source),run_name='__main__')
    for name in ['build-packs.ts','check-pinyin.ts','check-contextual-pinyin.ts']:
        log=shadow/f'editorial-{number:02}-{name}.log'
        with log.open('w',encoding='utf-8') as output:
            result=subprocess.run(['node',str(ROOT/'node_modules/tsx/dist/cli.mjs'),str(ROOT/'scripts'/name)],cwd=shadow,stdout=output,stderr=subprocess.STDOUT)
        assert result.returncode==0,('editorial',number,name,str(log))
print('Isolated first-publication and queued editorial checks passed; no app packs changed. Preserved:',shadow)
