"""Apply independently authored paragraph edits without replacing assessment IDs."""
import json,re,sys
from common import ROOT,line,py

def apply(level,edits,review,glosses=(),publish=False):
    for number,sections in edits.items():
        uid=f's{level}-u{number:02}'
        current=ROOT/f'content/packs/{uid}.json'
        source=current if current.exists() else ROOT/f'output/advanced-course-drafts/{uid}.json'
        if not publish and '--shadow' in sys.argv:
            source=ROOT/f'.cache/advanced-preflight/content/packs/{uid}.json'
        pack=json.loads(source.read_text('utf-8'))
        for suffix,replacements in sections.items():
            text=next(t for t in [pack['dialogue'],pack['reading'],*pack['extraReadings']] if t['id']==uid+suffix)
            for index,(zh,en) in replacements.items():
                before=text['lines'][index]
                after=line(zh,en,before.get('speaker'))
                text['lines'][index]=after
                def update_reference(value):
                    if isinstance(value,dict):
                        if value.get('zh')==before['zh']:
                            value.update(zh=after['zh'],py=after['py'],en=after['en'])
                        for child in value.values():update_reference(child)
                    elif isinstance(value,list):
                        for child in value:update_reference(child)
                update_reference(pack['tasks'])
            # Rebuild gaps from the revised passage; never retain an old paragraph.
            selected=[]
            for item in text['lines']:
                word=next((v['hanzi'] for v in pack['vocabulary'] if v['hanzi'] in item['zh'] and v['hanzi'] not in [w for _,w in selected]),None)
                if word:selected.append((item,word))
                if len(selected)==3:break
            if selected:
                text['cloze']=dict(lines=[{**item,'zh':item['zh'].replace(w,f'【{w}】',1)} for item,w in selected],bank=[w for _,w in selected]+['明天' if all(w!='明天' for _,w in selected) else '昨天'])
            else:text.pop('cloze',None)
            for word,meaning in glosses:
                if any(word in item['zh'] for item in text['lines']) and not any(g['hanzi']==word for g in text.get('glosses',[])):
                    text.setdefault('glosses',[]).append(dict(hanzi=word,pinyin=py(word),meaning=meaning))
            if suffix!='-d':
                assert sum(len(re.findall(r'[\u3400-\u9fff]',item['zh'])) for item in text['lines'])>={5:600,6:900}[level],(uid,suffix,'reading length')
        note='2026-10-08 advanced reading self-review: '+review+' Native review pending.'
        for text in [pack['dialogue'],pack['reading'],*pack['extraReadings']]:
            for word,meaning in glosses:
                if any(word in item['zh'] for item in text['lines']) and not any(g['hanzi']==word for g in text.get('glosses',[])):
                    text.setdefault('glosses',[]).append(dict(hanzi=word,pinyin=py(word),meaning=meaning))
        pack['notes']='\n'.join(dict.fromkeys([*pack.get('notes','').splitlines(),note]))
        dest=ROOT/('content/packs' if publish else 'output/parity-editorial-drafts')/f'{uid}.json'
        dest.parent.mkdir(parents=True,exist_ok=True)
        dest.write_text(json.dumps(pack,ensure_ascii=False,indent=2)+'\n','utf-8')
        print(uid,'published' if publish else 'drafted',flush=True)

def dependencies(definitions,publish=False):
    for uid,terms in definitions.items():
        source=ROOT/f'content/packs/{uid}.json'
        # A definition dependency must not publish an entire future unit early.
        # Its own authored editorial layer carries the definition on publication.
        if publish and not source.exists():continue
        if not publish and '--shadow' in sys.argv:source=ROOT/f'.cache/advanced-preflight/content/packs/{uid}.json'
        elif not source.exists():source=ROOT/f'output/advanced-course-drafts/{uid}.json'
        pack=json.loads(source.read_text('utf-8'))
        for text in [pack['dialogue'],pack['reading'],*pack['extraReadings']]:
            for term in terms:
                word,meaning=term[:2]
                pinyin=term[2] if len(term)>2 else py(word)
                if any(word in item['zh'] for item in text['lines']) and not any(g['hanzi']==word for g in text.get('glosses',[])):
                    text.setdefault('glosses',[]).append(dict(hanzi=word,pinyin=pinyin,meaning=meaning))
        target=ROOT/('content/packs' if publish else 'output/parity-editorial-drafts')/f'{uid}.json'
        target.write_text(json.dumps(pack,ensure_ascii=False,indent=2)+'\n','utf-8')
