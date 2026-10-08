"""Explicit glyph meanings in connected, already authored advanced words.

Ownership is the first matching authored vocabulary context at the stated source
level. This is recognition instruction, not incidental-character coverage.
"""
import json
from common import ROOT, py

MEANINGS={
4:dict(s.split('|') for s in '''聚|gather
赞|praise
沉|sink; deep, in 沉默
默|silent
释|explain, in 解释
暗|dark; hidden
含|contain
究|investigate, in 究竟
竟|after all, in 究竟
未|not yet
却|yet; however
乎|bound component in 在乎, care about
承|undertake; accept
诚|sincere
扬|raise; praise, in 表扬
替|replace; on behalf of
既|already; since
则|rule; then
临|approach; be about to
与|with; and
担|undertake; carry a responsibility
括|include; sum up
无|without; not have
置|put; place
迟|late; slow
镜|mirror; lens
描|depict
述|state; recount
秘|secret
密|close; secret
甚|very; even, in 甚至
浅|shallow
纯|pure
择|choose, in 选择
申|state; apply
毕|finish; after all, in 毕竟
料|material; expect
趣|interest; interesting quality
序|order; sequence
操|operate, in 操作
测|measure; test
尺|ruler; measure of length
寸|unit of length; size
案|case; proposal
辩|argue; distinguish
避|avoid
免|spare; avoid
细|fine; detailed
映|reflect; show on a screen
航|navigate; voyage
途|way; route
堵|block
距|distance
即|immediately; namely
限|limit
延|extend; delay
虑|consider; worry
松|loose; relax'''.splitlines()),
5:dict(s.split('|') for s in '''沟|channel; communicate, in 沟通
尊|respect
矛|spear; bound component in 矛盾, contradiction
盾|shield; bound component in 矛盾, contradiction
怨|resent; complain
偶|occasional; by chance
奈|bound component in 无奈, having no alternative
谊|friendship
珍|valuable; treasure
惜|cherish; regret losing
犹|hesitate, in 犹豫
豫|bound component in 犹豫, hesitate
耐|endure; patient
敬|respect
慰|comfort
鼓|drum; encourage
励|encourage, in 鼓励
击|strike
豪|proud; outstanding
恢|restore, in 恢复
乏|lack; tired
掌|palm; grasp
曲|piece of music
辑|edit; bound component in 编辑
漫|spread; unrestrained
忆|remember
舍|give up; be willing to part with
仿|imitate
索|search; seek
键|key, on a keyboard
析|analyse, in 分析
逻|bound component in 逻辑, logic
暂|temporary
脆|brittle; crisp
扰|disturb
私|private; personal
委|entrust
托|entrust; support
拒|refuse
敏|sensitive; quick
执|hold; persist
估|estimate
尝|taste; try
览|view; browse
享|enjoy
返|return
触|touch
尔|bound component in 偶尔, occasionally
龄|age
启|open; begin
频|frequent
繁|numerous; complex
柜|cabinet; counter
幽|quiet; bound component in 幽默, humour
脾|bound component in 脾气, temper
骂|scold
傻|foolish
厉|strict; severe
怜|pity, in 可怜
忍|endure; restrain
厌|dislike
瞧|look
悄|quiet, in 悄悄
摄|take a photograph; record
朗|clear; bright
弹|play a stringed instrument
琴|a stringed musical instrument'''.splitlines()),
6:dict(s.split('|') for s in '''诺|promise
歉|apology; regret
谅|understand; forgive
赖|depend on
缘|connection; reason
纳|accept; take in
拨|move aside; dial
偏|lean to one side; contrary to expectation
恰|just; exactly
佛|bound component in 仿佛, as if
挨|be close to; next to
允|permit
额|amount; quota
若|if; like
凡|every; ordinary
罢|stop; bound component in 罢了, that is all
踩|step on
捡|pick up
裂|split; crack
侧|side
略|omit; brief
倾|lean; incline
壶|pot; kettle
抗|resist
稿|draft; manuscript
藏|hide; store
奏|play music
截|cut off; segment
隐|hidden
露|reveal; show
绪|thread; state of mind, in 情绪
憾|regret
孤|alone
衡|balance; weigh
番|an occurrence; a round
盼|hope; look forward to
屏|screen
洋|ocean; abundant
波|wave
渡|cross a body of water
幻|illusion; change
灵|spirit; quick-minded
融|melt; blend
素|element; plain
岗|post; position
策|plan; policy
监|supervise
异|different
仓|storehouse
储|store; accumulate
沿|along
涉|involve; wade
探|explore; investigate'''.splitlines())}

def authored_characters(level,number,vocabulary):
    inventory=json.loads((ROOT/'prompts/research/gf2021-advanced-inventory.json').read_text('utf-8'))['levels'][str(level)]['characters']
    source={r[2]:{row[3].lower() for row in inventory if row[2]==r[2]} for r in inventory}
    # Earlier-level explicit definitions retain their original IDs and senses.
    earlier={c['hanzi'] for f in (ROOT/'content/packs').glob('s*-u*.json')
             for p in [json.loads(f.read_text('utf-8'))]
             if p['unit']['hskTarget']['level']<level for c in p.get('characters',[])}
    owners={}
    for n in range(1,number):
        p=ROOT/'output/advanced-course-drafts'/f's{level}-u{n:02}.json'
        assert p.exists(), f'Missing authored earlier draft {p}'
        for character in json.loads(p.read_text('utf-8')).get('characters',[]):
            owners.setdefault(character['hanzi'],n)
    result=[]
    for ch,meaning in MEANINGS[level].items():
        words=[v for v in vocabulary if ch in v['hanzi']]
        if not words or ch in earlier or ch in owners:continue
        reading=py(ch)
        # These four have contextual readings different from the default lookup.
        reading={5:{'舍':'shě','曲':'qǔ','弹':'tán'},6:{'佛':'fú','挨':'āi','藏':'cáng','露':'lù'}}.get(level,{}).get(ch,reading)
        assert reading in source.get(ch,set()), (level,ch,reading,'not an exact official character reading')
        # A dictionary's isolated glyph reading must match the connected word.
        matching=[]
        for word in words:
            syllables=word['pinyin'].split()
            assert len(syllables)==len(word['hanzi']), (level,word['hanzi'],'unaligned character example')
            if all(syllables[position]==reading for position,glyph in enumerate(word['hanzi']) if glyph==ch):
                matching.append(word)
        # Do not claim the source reading through a differently pronounced word.
        if not matching:continue
        words=matching
        stroke=json.loads((ROOT/'node_modules/hanzi-writer-data'/f'{ch}.json').read_text('utf-8'))
        result.append(dict(hanzi=ch,pinyin=reading,meaning=meaning,strokes=len(stroke['strokes']),
            parts=[dict(form=ch,role='whole',gloss=meaning)],noteKind='usage',
            note=f"Recognize {ch} in {' / '.join(v['hanzi'] for v in words[:2])}. This is a usage aid, not an etymological decomposition. Other word-dependent readings are not interchangeable.",
            words=[dict(w=v['hanzi'],p=v['pinyin'],m=v['meaning']) for v in words[:2]]))
    return result
