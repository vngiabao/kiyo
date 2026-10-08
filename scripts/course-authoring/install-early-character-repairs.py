"""Repair contextual readings while retaining every saved curriculum ID."""
import hashlib,json
from common import ROOT,py

repairs={
    's1-u21':('觉','perceive; feel (jué); jiào in 睡觉',
              'Read jué in 觉得, to feel or think. 睡觉 uses the different jiào reading, to sleep. This is a usage contrast, not an etymological claim.'),
    's1-u24':('兴','rise; flourish (xīng); xìng in 高兴',
              'The source character reading xīng means rise or flourish. 高兴, glad or happy, uses xìng instead. These word-dependent readings are not interchangeable.'),
    's1-u19':('识','knowledge; recognize',
              'The standalone reading is shí. In 知识, knowledge, shi is normally neutral. This connected-speech change does not change the word meaning.'),
    's1-u20':('候','time in 时候',
              'The standalone reading is hòu. In 时候 and 有时候, hou is normally neutral. Listen to the whole word; this is a usage note, not an etymological claim.'),
}
for uid,(glyph,meaning,note) in repairs.items():
    path=ROOT/'content/packs'/f'{uid}.json'
    pack=json.loads(path.read_text('utf-8'))
    character=next(c for c in pack['characters'] if c['hanzi']==glyph)
    character.update(meaning=meaning,note=note)
    character['parts'][0]['gloss']=meaning
    if glyph=='觉':
        character['words']=[dict(w='觉得',p=py('觉得'),m='feel; think'),
                            *[w for w in character['words'] if w['w']!='觉得']]
    path.write_text(json.dumps(pack,ensure_ascii=False,indent=2)+'\n','utf-8')
    print(uid,glyph,'source reading and contextual contrast repaired; IDs retained.')

path=ROOT/'src/hanzi.ts'
source=path.read_text('utf-8')
source=source.replace('觉: "睡觉"','觉: "觉得"').replace('兴: "高兴",','')
assert '觉: "觉得"' in source and '兴: "高兴"' not in source
path.write_text(source,'utf-8')

# The low-level source reading must not inherit xìng from 高兴. Use the existing
# carrier/crop mechanism; provenance retains the carrier and exact crop boundary.
path=ROOT/'content/voices/approved-b-half/pronunciation-contexts.json'
contexts=json.loads(path.read_text('utf-8'))
token=hashlib.sha256('兴'.encode()).hexdigest()[:16]
for mood in ['clear','playful','cool']:
    contexts.setdefault(token+'-'+mood,dict(synthesisText='兴起。兴。',extract='last-clause',
        reason='Disambiguate source xīng, rise, from xìng in 高兴; retain only the final target syllable. Native tone review remains pending.'))
path.write_text(json.dumps(contexts,ensure_ascii=False,indent=2)+'\n','utf-8')
