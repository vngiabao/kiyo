"""Serialize editorially authored C2 units. Uses the existing local pinyin runtime only.

This is editorial source, not a language generator. English/Vietnamese meanings,
Chinese contexts and assessment decisions below are written for each situation.
"""
import json
import re
from pathlib import Path
from pypinyin import lazy_pinyin, Style

ROOT = Path(__file__).resolve().parents[2]
read = lambda p: json.loads(p.read_text('utf-8-sig'))
levels = read(ROOT / 'content/hsk/levels.json')['words']
plan = read(ROOT / 'prompts/research/course-plan.json')
baseline = read(ROOT / 'prompts/research/c1-coverage-baseline.json')
unit_glosses={}
character_contexts={}
vocabulary_readings={}
character_readings={}
character_notes={}
remaining = {f: e for e in baseline['levels'][0]['words']['remainingEntries'] for f in e['forms']}
remaining_by_level = {level['level']: {f: e for e in level['words']['remainingEntries'] for f in e['forms']} for level in baseline['levels']}
source_aliases={'有（一）点儿':['有点儿','有一点儿'],'家（科学家）':['家'],
    '老（老王）':['老'],'小（小王）':['小'],'头（里头）':['头'],
    '面1':['面'],'面2':['面'],'称1':['称'],'们（朋友们）':['们'],'子（桌子）':['子'],
    '员（服务员）':['员'],'者（志愿者）':['者']}
for level, allocation in remaining_by_level.items():
    for entry in baseline['levels'][level-1]['words']['remainingEntries']:
        for alias in source_aliases.get(entry['entry'],[]):
            allocation.setdefault(alias,entry)
source_rows={e['sourceNo']:e for level in baseline['levels'] for e in level['words']['remainingEntries']}
selected_source_rows={}
for form, annotated in [('们','们（朋友们）'),('子','子（桌子）')]:
    remaining[form]=remaining[annotated]
character_groups = {
    13: [('儿','child; son'),('外','outside; foreign'),('妹','younger sister'),('姐','older sister'),('孩','child'),('弟','younger brother'),('班','class; group'),('男','male'),('院','institute; courtyard')],
    14: [('电','electricity'),('影','image; film'),('票','ticket'),('想','to think; to want'),('也','also'),('爱','to love'),('球','ball'),('米','rice'),('菜','dish; vegetables')],
    15: [('哪','which'),('什','part of 什么: what'),('么','part of 什么: what'),('几','how many (small number)'),('谁','who'),('期','period; scheduled time'),('图','picture; map'),('记','to remember; to record'),('答','to answer')],
    16: [('书','book'),('本','root; classifier for books'),('杯','cup'),('新','new'),('白','white'),('拿','to take; to hold'),('放','to put; to release'),('用','to use'),('那','that')],
}

# Citation forms; connected-speech sandhi is taught in notes rather than guessed.
overrides = {'她们':'tā men','学生':'xué sheng','中学生':'zhōng xué sheng',
 '小学生':'xiǎo xué sheng','姐姐':'jiě jie','妹妹':'mèi mei','弟弟':'dì di',
 '孩子':'hái zi','小孩儿':'xiǎo háir','朋友':'péng you','我们':'wǒ men',
 '你们':'nǐ men','他们':'tā men','什么':'shén me','多少':'duō shao',
 '哪里':'nǎ lǐ','哪儿':'nǎr','这儿':'zhèr','那儿':'nàr',
 '包子':'bāo zi','杯子':'bēi zi','本子':'běn zi','书包':'shū bāo',
 '还是':'hái shi','认识':'rèn shi','时候':'shí hou','意思':'yì si',
 '有意思':'yǒu yì si','同学':'tóng xué','名字':'míng zi','东西':'dōng xi',
 '晚上':'wǎn shang','这里':'zhè lǐ','有时候':'yǒu shí hou','干什么':'gàn shén me','干':'gàn','知识':'zhī shi','别人':'bié ren','家里':'jiā lǐ','里边':'lǐ bian','地上':'dì shang','楼上':'lóu shàng','楼下':'lóu xià','时候':'shí hou','奶奶':'nǎi nai','爷爷':'yé ye','打开':'dǎ kāi','关上':'guān shang','那里':'nà lǐ','这里':'zhè lǐ','哪':'nǎ',
 '男孩儿':'nán háir','女孩儿':'nǚ háir','面条儿':'miàn tiáor',
 '吗':'ma','们':'men','子':'zi','着':'zhe','个':'gè','要':'yào','还':'hái','都':'dōu','那':'nà','读':'dú',
 '上':'shàng','下':'xià','班':'bān','国':'guó','三':'sān','也':'yě',
 '书':'shū','新':'xīn','白':'bái','水':'shuǐ','爱好':'ài hào','地':'de',
 '看到':'kàn dào','完':'wán','怎么':'zěn me','门口':'mén kǒu','谁':'shéi','干干净净':'gān gān jìng jìng'}
dictionary = {w: ' '.join(lazy_pinyin(w,style=Style.TONE)) for w,v in levels.items() if v.get('pinyin')}
dictionary.update(overrides)
def py(text):
    text = text.replace('【','').replace('】','')
    out, i = [], 0
    while i < len(text):
        if text[i]=='〇':
            out.append('líng'); i+=1
            continue
        if not '\u4e00' <= text[i] <= '\u9fff':
            if text[i] in '，。！？；：、': out.append(dict(zip('，。！？；：、',',.!?;:, '))[text[i]])
            i += 1
            continue
        word = next((text[i:j] for j in range(min(len(text), i+8),i,-1) if text[i:j] in dictionary),None)
        if word:
            out.append(dictionary[word]); i += len(word)
        else:
            out.append(lazy_pinyin(text[i],style=Style.TONE,neutral_tone_with_five=False)[0]); i += 1
    return ' '.join(out)

def line(zh, en, speaker=None):
    result = dict(zh=zh, py=py(zh), en=en)
    if speaker: result['speaker']=speaker
    return result

def lines(rows, speakers=False):
    return [line(zh,en,('a' if i%2==0 else 'b') if speakers else None) for i,(zh,en) in enumerate(rows)]

def questions(rows):
    return [dict(type=kind,q=q,choices=choices,answer=choices[answer]) for kind,q,choices,answer in rows]

def vocab(rows, uid, gf_level=1):
    result=[]
    for i,(w,en,vi,pos,example,translation) in enumerate(rows,1):
        allocation = remaining if gf_level == 1 else remaining_by_level[gf_level]
        assert w in allocation, f'{w}: not an untaught level-{gf_level} source entry'
        result.append(dict(id=f'{uid}-w{i:02}',hanzi=w,pinyin=vocabulary_readings.get(uid+':'+w,py(w)),meaning=en,meaningVi=vi,pos=pos,
            register='neutral',hskLevel=levels[w]['hsk3'],example=line(example,translation)))
        source=source_rows[selected_source_rows[uid+':'+w]] if uid+':'+w in selected_source_rows else allocation[w]
        assert source['sourceNo'] in {entry['sourceNo'] for entry in baseline['levels'][gf_level-1]['words']['remainingEntries']}, f'{uid}: cited reading/sense of {w} is not in the allocated source level'
        assert w in source['forms'] or w in source_aliases.get(source['entry'],[]), f'{uid}: {w} does not match cited source {source["entry"]}'
        result[-1]['usageNote']=f"[GF2021:L{gf_level}:{source['sourceNo']}] Source entry: {source['entry']}; {source['pinyin']}; {source['partOfSpeech']}. This lesson teaches the stated reading and sense; the minimum-level lookup remains separate."
    return result

def grammar(uid, code, pattern, purpose, explanation, examples, mistake):
    wrong,right,why=mistake
    return dict(id=f'{uid}-g{code}',pattern=pattern,purpose=purpose,explanation=explanation,
        examples=lines(examples),commonMistakes=[dict(wrong=wrong,right=right,why=why)],register='neutral')

def text(uid, suffix, title, purpose, rows, qs, blanks=(), drama=False):
    ls=lines(rows,drama)
    result=dict(id=f'{uid}-{suffix}',title=title,format='story' if drama else 'note',
        blurb='Original AI-assisted course writing; not adapted from a show or song.',
        purpose=purpose,lines=ls,questions=questions(qs))
    if drama: result['speakers']=[dict(id='a',name='甲'),dict(id='b',name='乙')]
    if blanks:
        result['cloze']=dict(lines=[{**ls[i],'zh':ls[i]['zh'].replace(w,f'【{w}】',1)} for i,w in blanks],bank=[w for _,w in blanks]+['电影' if '电影' not in [w for _,w in blanks] else '学校'])
    return result

def tasks(uid, words, spec):
    def base(kind,i,word): return dict(type=kind,id=f'{uid}-t{i}',phrase=next(v['id'] for v in words if v['hanzi']==word))
    result=[]
    for i,(w,zh,en,statement,truth,why) in enumerate(spec['tf'],1):
        result.append(dict(**base('truefalse',i,w),audio=line(zh,en),statement=statement,answer=truth,why=why))
    for i,(w,zh,en,choices,answer,why) in enumerate(spec['reply'],3):
        result.append(dict(**base('reply',i,w),prompt=line(zh,en),choices=choices,answer=choices[answer],why=why))
    for i,(w,zh,en) in enumerate(spec['fill'],5):
        result.append(dict(**base('listenfill',i,w),line=line(zh.replace(w,f'【{w}】',1),en),blankPy=py(w)))
    for i,(w,pairs) in enumerate(spec['match'],7):
        result.append(dict(**base('match',i,w),title='Match the message to its meaning',pairs=[dict(left=en,right=line(zh,en)) for zh,en in pairs]))
    return result

def write(n, titleZh, canDo, wordrows, gs, dialogue, reading, media, practice, pragmatics, turns, flags):
    requested_id = f's1-u{n:02}' if isinstance(n,int) else n
    p=next(x for x in plan['units'] if x['id']==requested_id)
    uid=p['id']; vs=vocab(wordrows,uid,p['gfLevel'])
    assert len(vs)==p['wordBudget']
    support=unit_glosses.get(n,{})
    for t in [dialogue,reading,media]:
        body=''.join(l['zh'] for l in t['lines'])
        t['glosses']=[dict(hanzi=w,pinyin=py(w),meaning=m) for w,m in support.items() if w in body]
    for v in vs:
        if v['hanzi']=='孩子':
            v['usageNote']='Northern casual speech also says 小孩儿 (xiǎoháir), meaning a young child. This is a recognition note; the spoken course practice uses 孩子 (háizi).'
        if v['hanzi'] in ['们','子']:
            v['usageNote']=('Suffix, not a standalone spoken word. The official source entry is '+remaining[v['hanzi']]['entry']+'. '+('们 marks a group of people or pronouns, as in 朋友们; do not add it after a numeral and classifier.' if v['hanzi']=='们' else '子 is a neutral suffix in 桌子; this differs from full-tone zǐ in other words.'))
    chars=[]
    earlier_words=[]
    earlier_characters=set()
    for path in sorted((ROOT/'content/packs').glob('s*.json')):
        earlier=read(path)
        if (earlier['unit']['stage'],earlier['unit']['order'])<(p['packStage'],p['order']):
            earlier_words.extend(earlier['vocabulary'])
            for reading_text in [earlier.get('dialogue'),earlier.get('reading'),*earlier.get('extraReadings',[])]:
                if reading_text:
                    earlier_words.extend(reading_text.get('glosses',[]))
            earlier_characters.update(c['hanzi'] for c in earlier.get('characters',[]))
    # A displayed gloss in this unit is actual recognition instruction, not audited
    # vocabulary credit. Only words present in the connected text can support glyphs.
    for reading_text in [dialogue,reading,media]:
        earlier_words.extend(reading_text.get('glosses',[]))
    introduced={form for level in baseline['levels'] for entry in level['words']['introducedEntries'] for form in entry['forms']}
    base_source=(ROOT/'src/content.ts').read_text('utf-8')
    for w,meaning in character_contexts.values():
        assert w in introduced or ('"'+w+'"') in base_source, f'Character consolidation must use a taught base word: {w}'
        earlier_words.append(dict(hanzi=w,pinyin=py(w),meaning=meaning))
    for ch, meaning in character_groups[n]:
        assert ch in baseline['levels'][p['gfLevel']-1]['characters']['remaining'], f'{uid}: {ch} is not an unintroduced level-{p["gfLevel"]} character'
        assert ch not in earlier_characters, f'{uid}: {ch} already has an explicit earlier introduction'
        stroke=read(ROOT/'node_modules/hanzi-writer-data'/f'{ch}.json')
        examples=list({v['hanzi']:v for v in [*vs,*earlier_words] if ch in v['hanzi']}.values())[:2]
        assert examples
        chars.append(dict(hanzi=ch,pinyin=character_readings.get(uid+':'+ch,py(ch)),meaning=meaning,strokes=len(stroke['strokes']),
            parts=[dict(form=ch,role='whole',gloss=meaning)],noteKind='usage',
            note=f"Recognize {ch} in {' / '.join(v['hanzi'] for v in examples)}. This usage note is not an origin or decomposition claim." + (' In 小孩儿, 儿 is an -r ending, not a separate ér syllable.' if ch=='儿' else '') + character_notes.get(uid+':'+ch,''),
            words=[dict(w=v['hanzi'],p=v['pinyin'],m=v['meaning']) for v in examples]))
    result=dict(packVersion=1,unit=dict(id=uid,stage=p['packStage'],order=p['order'],title=p['title'],titleZh=titleZh,
        canDo=canDo,hskTarget=dict(standard='HSK3.0',level=p['gfLevel']),prerequisites=[p['prerequisite']],estimatedMinutes=45),
        vocabulary=vs,characters=chars,grammar=gs,dialogue=dialogue,reading=reading,extraReadings=[media],tasks=tasks(uid,vs,practice),
        pragmatics=[dict(situation=s,natural=line(zh,en),note=note) for s,zh,en,note in pragmatics],
        conversation=dict(id=f'{uid}-speak',title=p['title'],place='A language-exchange meeting',context=p['situation'],
            goal=canDo[0],partner=dict(name='Sayo',persona='Brief, patient and lightly teasing.'),
            turns=[dict(text=zh,pinyin=py(zh),meaning=en,intent=intent,examples=examples,
                accept=[f'^{re.escape(e)}[。！？]?$' for e in examples]) for zh,en,intent,examples in turns]),
        notes='AI-assisted draft; native review pending. GF2021 grammar families: '+', '.join(g['code'] for g in p['grammar'])+'. '+flags)
    dest=ROOT/'content/packs'/f'{uid}.json'
    dest.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n','utf-8')
    print(uid, len(vs), 'words; authored source saved')
