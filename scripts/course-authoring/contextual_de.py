"""Correct only 得 syllables, preserving every other authored reading and mark."""
import json,re,unicodedata
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
RULES=json.loads((ROOT/'content/hsk/contextual-de.json').read_text('utf-8'))
V='aeiouüvāáǎàēéěèīíǐìōóǒòūúǔùǖǘǚǜ'
SYLLABLE=re.compile(r'(?:zh|ch|sh|[bpmfdtnlgkhjqxrzcsyw])?['+V+r']+(?:ng(?!['+V+r'])|n(?!['+V+r']))?(?:r(?!['+V+r']))?',re.I)

def reading(text,index):
    if text=='得很' and index==0:return 'de'  # Degree-complement citation.
    for field in ['exactContexts','lexemes']:
        for word,tone in sorted(RULES[field].items(),key=lambda pair:-len(pair[0])):
            start=index-word.index('得')
            if start>=0 and text[start:start+len(word)]==word:return tone
    before,after=text[:index],text[index+1:]
    if any(before.endswith(stem) for stem in RULES['complementStems']):return 'de'
    if any(after.startswith(tail) for tail in RULES['modalTails']):return 'děi'
    if any(before.endswith(head) for head in RULES['modalHeads']):return 'děi'
    return None

def correct(text,pinyin):
    text=text.replace('【','').replace('】','')
    chars=[c for c in text if '\u3400'<=c<='\u9fff' or c=='〇']
    tokens=list(SYLLABLE.finditer(pinyin))
    positions=[]
    si=0
    for ci,c in enumerate(chars):
        if c=='儿' and si and tokens[si-1].group().lower().endswith('r') and not re.fullmatch('[eēéěè]r',tokens[si-1].group(),re.I):
            continue
        if si>=len(tokens):raise ValueError(('Cannot align authored pinyin',text,pinyin))
        if c=='得':positions.append((ci,si))
        si+=1
    if si!=len(tokens):raise ValueError(('Cannot align authored pinyin',text,pinyin))
    full_positions=[i for i,c in enumerate(text) if '\u3400'<=c<='\u9fff' or c=='〇']
    edits=[]
    for ci,si in positions:
        tone=reading(text,full_positions[ci])
        token=tokens[si]
        if tone is None:continue
        bare=''.join(c for c in unicodedata.normalize('NFD',token.group()) if not unicodedata.combining(c)).lower()
        if bare not in ['de','dei']:raise ValueError(('得 is not aligned to its syllable',text,pinyin,token.group()))
        if token.group()!=tone:edits.append((token.start(),token.end(),tone))
    for start,end,tone in reversed(edits):pinyin=pinyin[:start]+tone+pinyin[end:]
    return pinyin
