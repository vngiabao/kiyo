"""Serialize explicitly authored repairs, preserving unit and assessment IDs.

No coverage-driven sentence synthesis. Authors provide every new Chinese line,
translation and answer. Draft mode never changes the published curriculum.
"""
import json
import re
from pathlib import Path
from common import line, py

ROOT = Path(__file__).resolve().parents[2]

def repair(number, spec, publish=False, level=3):
    uid = f's{level}-u{number:02}'
    p = json.loads((ROOT / f'content/packs/{uid}.json').read_text('utf-8'))
    def fix_negative_receive(value):
        if isinstance(value,dict):
            if '没收到' in value.get('zh','') and 'py' in value:
                value['py']=re.sub(r'mò\s+shōu\s+dào','méi shōu dào',value['py'])
            for child in value.values():fix_negative_receive(child)
        elif isinstance(value,list):
            for child in value:fix_negative_receive(child)
    fix_negative_receive(p)
    if 'title' in spec:
        p['unit']['title'], p['unit']['titleZh'] = spec['title']
    if 'goals' in spec: p['unit']['canDo'] = spec['goals']
    for key in ['dialogue', 'reading', 'media']:
        if key not in spec: continue
        rows, questions = spec[key]
        t = p[key] if key != 'media' else p['extraReadings'][0]
        t['lines'] = [line(zh, en, ('a' if i % 2 == 0 else 'b') if key in ['dialogue','media'] else None) for i,(zh,en) in enumerate(rows)]
        if key in ['dialogue','media']:
            names=spec.get(key+'Speakers',['林安','陈宇'])
            assert len(names)==2 and all(names)
            t['speakers'] = [dict(id='a',name=names[0]), dict(id='b',name=names[1])]
        t['questions'] = [dict(type=kind, q=q, choices=choices, answer=choices[answer]) for kind,q,choices,answer in questions]
        t['blurb'] = 'An original scene written for this course.'
        t['purpose'] = spec.get('purposes',{}).get(key, 'Follow the situation, the problem and what happens next.')
        t['glosses'] = [dict(hanzi=w,pinyin=py(w),meaning=en) for w,en in spec.get('glosses',[]) if any(w in zh for zh,_ in rows)]
        # A gap fill must retain the exact passage, including punctuation.
        selected=[]
        for l in t['lines']:
            w=next((v['hanzi'] for v in p['vocabulary'] if v['hanzi'] in l['zh'] and v['hanzi'] not in [w for _,w in selected]),None)
            if w: selected.append((l,w))
            if len(selected)==3: break
        if selected:
            t['cloze']=dict(lines=[{**l,'zh':l['zh'].replace(w,f'【{w}】',1)} for l,w in selected],bank=[w for _,w in selected]+['明天' if '明天' not in [w for _,w in selected] else '昨天'])
        else: t.pop('cloze',None)
    for v in p['vocabulary']:
        if v['hanzi'] in spec.get('examples',{}):
            v['example']=line(*spec['examples'][v['hanzi']])
        for field,value in spec.get('vocabularyFields',{}).get(v['hanzi'],{}).items():
            assert field in {'meaning','meaningVi','pos','register'}, 'Keep IDs, source evidence and checked levels intact'
            v[field]=value
    if 'contexts' in spec:
        t=next((t for t in p['extraReadings'] if t['id'].endswith('-word-notebook')),None)
        if t is None:
            t=dict(id=f'{uid}-word-notebook',titleZh=p['unit']['titleZh']+' · 词语练习',format='diary',register='neutral',lines=[],glosses=[],questions=[])
            p['extraReadings'].append(t)
        t['title']=p['unit']['title']+': words in context'
        t['blurb']='Independent everyday examples; these are separate situations.'
        t['purpose']='Understand each word in a different situation.'
        t['lines']=[line(zh,en) for zh,en in spec['contexts']]
        t['glosses']=[dict(hanzi=w,pinyin=py(w),meaning=en) for w,en in spec.get('glosses',[]) if any(w in zh for zh,_ in spec['contexts'])]
        t['questions']=[]
        t.pop('cloze',None)
    if 'tasks' in spec:
        result=[]
        for i,t in enumerate(spec['tasks']):
            old=p['tasks'][i]
            result.append(dict(id=old['id'],phrase=old['phrase'],**t))
        assert len(result)==len(p['tasks']), 'Every old task needs an authored replacement'
        p['tasks']=result
    if 'usage' in spec:
        p['pragmatics']=[dict(situation=s,natural=line(zh,en),note=note) for s,zh,en,note in spec['usage']]
    if 'turns' in spec:
        p['conversation'].update(place=spec.get('place','With friends'),context=spec.get('context',p['unit']['title']),goal=p['unit']['canDo'][0])
        p['conversation']['turns']=[dict(text=zh,pinyin=py(zh),meaning=en,intent=intent,examples=examples,accept=['^'+re.escape(e)+r'[。！？]?$' for e in examples]) for zh,en,intent,examples in spec['turns']]
    note='2026-10-07 parity editorial review: '+spec['review']+' Native review pending; no independent pronunciation or learner-mastery certification.'
    p['notes']='\n'.join(dict.fromkeys([*p.get('notes','').splitlines(),note]))
    target=ROOT/'content/packs' if publish else ROOT/'output/parity-editorial-drafts'
    target.mkdir(parents=True,exist_ok=True)
    (target/f'{uid}.json').write_text(json.dumps(p,ensure_ascii=False,indent=2)+'\n','utf-8')
    print(uid, 'published' if publish else 'drafted', flush=True)

def tf(zh,en,statement,answer,why):
    return dict(type='truefalse',audio=line(zh,en),statement=statement,answer=answer,why=why)
def reply(zh,en,choices,answer,why):
    return dict(type='reply',prompt=line(zh,en),choices=choices,answer=choices[answer],why=why)
def fill(zh,en,w):
    assert w in zh
    return dict(type='listenfill',line=line(zh.replace(w,f'【{w}】',1),en),blankPy=py(w))
def match(rows):
    return dict(type='match',title='Match the situation to the line',pairs=[dict(left=en,right=line(zh,en)) for zh,en in rows])
