"""Structure for explicitly authored original mixed practice, never exam copies."""
import json
from common import ROOT,py

def choice(zh,en):return dict(zh=zh,py=py(zh),en=en)
def question(fmt,sentence,en,prompt,answers,why):
    assert len(answers)==4 and len({z for z,e in answers})==4
    return dict(format=fmt,sentence=sentence,py=py(sentence),en=en,
        prompt=prompt,promptPy=py(prompt),choices=[choice(*a) for a in answers],
        answer=answers[0][0],explanation=why)
def R(*args):return question('reading',*args)
def L(*args):return question('listening',*args)
def C(sentence,en,prompt,answers,why):
    assert prompt.count('___')==1 and prompt.replace('___',answers[0][0])==sentence
    return question('cloze',sentence,en,prompt,answers,why)
def O(segments,en,prompt,wrong,why):
    segments=[s.replace('。','') for s in segments]
    wrong=[s.replace('。','') for s in wrong]
    sentence=''.join(segments)
    assert len(wrong)==3 and all(sorted(w)==sorted(sentence) for w in wrong)
    q=question('ordering',sentence,en,prompt,
        [(sentence,en),*[(w,'Alternative order') for w in wrong]],why)
    q['segments']=[choice(s,'Sentence part') for s in segments]
    return q
def write_bank(level,groups,draft=True):
    items=[]
    for group,rows in groups:
        assert len(rows)==30,(group,len(rows))
        for i,q in enumerate(rows):
            q.update(id=f'hsk{level}-bank-{group}-{i+1:02}',unit=group if i<20 else 'sample')
            shift=len(items)%4
            q['choices']=q['choices'][shift:]+q['choices'][:shift]
            items.append(q)
    assert len(items)==90 and sum(q['unit']=='sample' for q in items)==30
    pack=dict(kind='hsk-practice',version=2,id=f'hsk{level}-original-rotating',
        standard='GF2021 practice',level=level,
        provenance=dict(author='Kiyo original exercises',
            status='AI-assisted original mixed practice; native review pending. Ordering and choice cloze are adapted practice, not a full official mock or certified writing assessment.',
            sources=['https://www.chinesetest.cn/syllabus','https://hsk.cn-bj.ufileos.com/3.0/新版HSK考试大纲1219.pdf']),items=items)
    dest=ROOT/('.cache/course-authoring' if draft else 'content/packs')/f'hsk-{level}-bank.hsk.json'
    dest.parent.mkdir(parents=True,exist_ok=True)
    dest.write_text(json.dumps(pack,ensure_ascii=False,indent=2)+'\n','utf-8')
    print(f'Authored level {level}: 60 checkpoint and 30 sample items. Publication requires every gate.')

def mix(reading,listening,ordering,cloze):
    assert [len(reading),len(listening),len(ordering),len(cloze)]==[10,10,5,5]
    return [q for i in range(5) for q in [reading[i*2],listening[i*2],ordering[i],cloze[i],reading[i*2+1],listening[i*2+1]]]
