"""Serialize authored advanced course drafts, without inventing HSK levels.

The official inventory and the minimum-level lookup are deliberately separate.
Every example and question is supplied by the author. Missing contexts fail.
"""
import json
import re
from pathlib import Path
from common import ROOT, levels, line, py
from advanced_characters import authored_characters

INVENTORY = json.loads((ROOT / 'prompts/research/gf2021-advanced-inventory.json').read_text('utf-8'))

def rows(text):
    result=[tuple(p.strip() for p in l.split('|')) for l in text.strip().splitlines() if l.strip()]
    assert all(len(r)==2 for r in result)
    return result

def words(text):
    result=[tuple(p.strip() for p in l.split('|')) for l in text.strip().splitlines() if l.strip()]
    assert all(len(r)==7 for r in result)
    return result

def q(kind,prompt,correct,wrong1,wrong2):
    return kind,prompt,[correct,wrong1,wrong2],0

def card(pattern,purpose,explanation,examples,wrong,right,why):
    return pattern,purpose,explanation,rows(examples),(wrong,right,why)

def practice(facts,replies,fills,matches):
    from editorial_repair import tf,reply,fill,match
    # Keys and factual claims are authored, never inferred by this serializer.
    return [*[tf(*f) for f in facts],*[reply(*r) for r in replies],
            *[fill(*f) for f in fills],*[match(m) for m in matches]]

def passage(uid, suffix, title, rows, questions, glosses, dialogue=False):
    return dict(id=f'{uid}-{suffix}', title=title, titleZh=title,
                format='drama' if dialogue else 'story', register='casual' if dialogue else 'neutral',
                blurb='An original learning text, not a published script or lyric.',
                purpose='Follow the speakers’ intentions, supporting details and outcome.',
                speakers=[dict(id='a',name='林安'),dict(id='b',name='陈宇')] if dialogue else [],
                lines=[line(z,e,('a' if i%2==0 else 'b') if dialogue else None) for i,(z,e) in enumerate(rows)],
                glosses=[dict(hanzi=z,pinyin=py(z),meaning=e) for z,e in glosses if any(z in t for t,_ in rows)],
                questions=[dict(type=k,q=q,choices=c,answer=c[a]) for k,q,c,a in questions])

def write(level, number, spec, publish=False):
    uid=f's{level}-u{number:02}'
    previous=f's{level}-u{number-1:02}' if number>1 else ('s3-u44' if level==4 else f's{level-1}-u12')
    assert len(spec['vocabulary'])>={4:16,5:24,6:32}[level], 'An advanced unit needs substantive connected vocabulary.'
    if level>=5:
        minimum_chars={5:600,6:900}[level]
        count=lambda text:sum('\u4e00'<=c<='\u9fff' for z,_ in text for c in z)
        assert len(spec['dialogue'][0])>={5:18,6:24}[level], 'Author a substantial scene.'
        assert count(spec['reading'][0])>=minimum_chars, 'The main reading must develop its argument or story.'
        assert 'pairedReading' in spec and count(spec['pairedReading'][0])>=minimum_chars, 'Author the contrasting reading separately.'
    vocabulary=[]
    raw_context=[]
    pos_names={'名':'noun','动':'verb','形':'adjective','副':'adverb','代':'pronoun',
               '量':'classifier','助':'particle','介':'preposition','连':'conjunction'}
    for i,(word,en,vi,first,first_en,second,second_en) in enumerate(spec['vocabulary'],1):
        ref=levels.get(word)
        assert ref and isinstance(ref['hsk3'],int) and ref['hsk3']<=level,(uid,word,'unverified inventory level')
        assert word in first and word in second and first!=second,(uid,word,'two distinct authored contexts required')
        source=next((r for r in INVENTORY['levels'][str(level)]['words'] if r[2]==word),None)
        note=(f"[GF2021:L{level}:{source[0]}] Source entry: {source[2]}; {source[3]}; {source[4]}. The lesson teaches this stated sense; minimum-level lookup remains separate." if source else 'Retrieval of a word introduced at an earlier minimum level; no new advanced source-entry coverage is claimed.')
        # Preserve a stated source category rather than claiming coverage from spelling alone.
        category=next((pos_names[p] for p in source[4].split('、') if p in pos_names),'word') if source else 'word'
        category=spec.get('wordPos',{}).get(word,category)
        vocabulary.append(dict(id=f'{uid}-w{i:02}',hanzi=word,pinyin=py(word),meaning=en,meaningVi=vi,pos=category,register=spec.get('wordRegister',{}).get(word,'neutral'),hskLevel=ref['hsk3'],example=line(first,first_en),usageNote=note))
        # Two retrieval contexts remain separate from the initial word introduction.
        raw_context.extend([(first,first_en),(second,second_en)])
    grammar=[]
    for i,(pattern,purpose,explanation,examples,mistake) in enumerate(spec['grammar'],1):
        assert len(examples)>=2
        wrong,right,why=mistake
        grammar.append(dict(id=f'{uid}-g{i:02}',pattern=pattern,purpose=purpose,explanation=explanation,examples=[line(*r) for r in examples],commonMistakes=[dict(wrong=wrong,right=right,why=why)],register='neutral'))
    assert len(grammar)>={4:3,5:5,6:6}[level]
    glosses=spec.get('glosses',[])
    dialogue=passage(uid,'d',spec['title'][1],*spec['dialogue'],glosses,True)
    if 'dialogueSpeakerIds' in spec:
        ids=spec['dialogueSpeakerIds']
        dialogue['speakers']=spec['dialogueSpeakers']
        assert len(ids)==len(dialogue['lines'])
        assert set(ids)=={speaker['id'] for speaker in dialogue['speakers']}
        for spoken,speaker in zip(dialogue['lines'],ids):spoken['speaker']=speaker
    reading=passage(uid,'r',spec['title'][1],*spec['reading'],glosses)
    media=passage(uid,'media',spec['mediaTitle'],*spec['media'],glosses,True)
    notebook=passage(uid,'word-notebook',spec['title'][0]+': words in context',raw_context,[],glosses)
    notebook['titleZh']=spec['title'][1]+' · 词语练习'
    notebook.update(purpose='Retrieve these words in separate everyday situations.',format='diary')
    conversation=dict(id=f'{uid}-c',title=spec['title'][0],place=spec['place'],context=spec['context'],goal=spec['goals'][0],partner=dict(name='陈宇',persona='A familiar classmate; friendly, brief replies.'),turns=[dict(text=z,pinyin=py(z),meaning=e,intent=intent,examples=answers,accept=['^'+re.escape(a)+r'[。！？]?$' for a in answers]) for z,e,intent,answers in spec['turns']])
    extra=[media,notebook]
    if 'pairedReading' in spec:
        extra.append(passage(uid,'paired-reading',spec['pairedTitle'],*spec['pairedReading'],glosses))
    pack=dict(packVersion=1,unit=dict(id=uid,stage=3,order=108+(level-4)*12+number,title=spec['title'][0],titleZh=spec['title'][1],canDo=spec['goals'],hskTarget=dict(standard='HSK3.0',level=level),prerequisites=[previous,previous+'-usage'],estimatedMinutes={4:60,5:90,6:110}[level]),vocabulary=vocabulary,grammar=grammar,dialogue=dialogue,reading=reading,extraReadings=extra,conversation=conversation,pragmatics=[dict(situation=s,natural=line(z,e),note=n) for s,z,e,n in spec['usage']],tasks=[dict(id=f'{uid}-t{i:02}',phrase=vocabulary[(i-1)%len(vocabulary)]['id'],**t) for i,t in enumerate(spec['tasks'],1)],notes='2026-10-07 advanced media/social core. Original AI-assisted draft, checked against the stated inventory and comprehension keys. Native review pending. This is a selected competency route; it does not certify full HSK lexical coverage, exam readiness or learner mastery. '+spec['review'])
    assert len(dialogue['questions'])==len(reading['questions'])==3
    lo,hi={4:(8,10),5:(12,16),6:(16,20)}[level]
    assert lo<=len(pack['tasks'])<=hi
    pack['characters']=authored_characters(level,number,vocabulary)
    target=ROOT/('content/packs' if publish else 'output/advanced-course-drafts')
    target.mkdir(parents=True,exist_ok=True)
    (target/f'{uid}.json').write_text(json.dumps(pack,ensure_ascii=False,indent=2)+'\n','utf-8')
    print(uid,'published' if publish else 'drafted',flush=True)
    # Finalise the already reviewed four-unit editorial layer before the runner
    # collects audio. Avoid synthesising an older reading just to replace it.
    repair = {(5,8):16,(5,12):17,(6,4):18,(6,8):19,(6,12):20}.get((level,number))
    if publish and repair:
        import runpy
        runpy.run_path(str(ROOT/f'scripts/course-authoring/parity-repair-{repair:02}.py'),run_name='__main__')
