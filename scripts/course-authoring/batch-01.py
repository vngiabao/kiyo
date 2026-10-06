"""Serialize authored C2 batch 1. Uses the existing local pinyin runtime only.

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
remaining = {f: e for e in baseline['levels'][0]['words']['remainingEntries'] for f in e['forms']}
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
 '晚上':'wǎn shang','那里':'nà lǐ','这里':'zhè lǐ','哪':'nǎ',
 '男孩儿':'nán háir','女孩儿':'nǚ háir','面条儿':'miàn tiáor',
 '吗':'ma','个':'gè','要':'yào','还':'hái','都':'dōu','那':'nà','读':'dú',
 '上':'shàng','下':'xià','班':'bān','国':'guó','三':'sān','也':'yě',
 '书':'shū','新':'xīn','白':'bái','水':'shuǐ','爱好':'ài hào','地':'de',
 '看到':'kàn dào','完':'wán','怎么':'zěn me','门口':'mén kǒu','谁':'shéi'}
dictionary = {w: ' '.join(lazy_pinyin(w,style=Style.TONE)) for w,v in levels.items() if v.get('pinyin')}
dictionary.update(overrides)
def py(text):
    text = text.replace('【','').replace('】','')
    out, i = [], 0
    while i < len(text):
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

def vocab(rows, uid):
    result=[]
    for i,(w,en,vi,pos,example,translation) in enumerate(rows,1):
        assert w in remaining, f'{w}: not an untaught level-1 source entry'
        result.append(dict(id=f'{uid}-w{i:02}',hanzi=w,pinyin=py(w),meaning=en,meaningVi=vi,pos=pos,
            register='neutral',hskLevel=levels[w]['hsk3'],example=line(example,translation)))
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
    p=next(x for x in plan['units'] if x['id']==f's1-u{n:02}')
    uid=p['id']; vs=vocab(wordrows,uid)
    assert len(vs)==p['wordBudget']
    support={13:{'学习':'to study','所':'classifier for schools'},14:{'旁边':'next to','张':'classifier for tickets','行':'okay; acceptable'},
        15:{'一共':'altogether','刚才':'just now','现在':'now','问题':'question'},
        16:{'用完':'finish using','读':'to read'}}[n]
    for t in [dialogue,reading,media]:
        body=''.join(l['zh'] for l in t['lines'])
        t['glosses']=[dict(hanzi=w,pinyin=py(w),meaning=m) for w,m in support.items() if w in body]
    for v in vs:
        if v['hanzi']=='孩子':
            v['usageNote']='Northern casual speech also says 小孩儿 (xiǎoháir), meaning a young child. This is a recognition note; the spoken course practice uses 孩子 (háizi).'
    chars=[]
    for ch, meaning in character_groups[n]:
        assert ch in baseline['levels'][0]['characters']['remaining']
        stroke=read(ROOT/'node_modules/hanzi-writer-data'/f'{ch}.json')
        examples=[v for v in vs if ch in v['hanzi']][:2]
        assert examples
        chars.append(dict(hanzi=ch,pinyin=py(ch),meaning=meaning,strokes=len(stroke['strokes']),
            parts=[dict(form=ch,role='whole',gloss=meaning)],noteKind='usage',
            note=f"Recognize {ch} in {' / '.join(v['hanzi'] for v in examples)}. This usage note is not an origin or decomposition claim." + (' In 小孩儿, 儿 is an -r ending, not a separate ér syllable.' if ch=='儿' else ''),
            words=[dict(w=v['hanzi'],p=v['pinyin'],m=v['meaning']) for v in examples]))
    result=dict(packVersion=1,unit=dict(id=uid,stage=p['packStage'],order=p['order'],title=p['title'],titleZh=titleZh,
        canDo=canDo,hskTarget=dict(standard='HSK3.0',level=1),prerequisites=[p['prerequisite']],estimatedMinutes=45),
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

u='s1-u13'
write(13,'朋友的朋友',['Introduce a friend and explain how people know each other','Distinguish school stages without assuming ages','Use personal pronouns with clear references'],[
 ('她们','they (female group)','họ (nhóm nữ)','pronoun','她们是我的朋友。','They are my friends.'),
 ('班','class; group of students','lớp học','noun','我们在一个班。','We are in the same class.'),
 ('学生','student','học sinh; sinh viên','noun','你是学生吗？','Are you a student?'),
 ('中学','secondary school','trường trung học','noun','我妹妹在中学学习。','My younger sister studies at secondary school.'),
 ('中学生','secondary-school student','học sinh trung học','noun','他是中学生。','He is a secondary-school student.'),
 ('小学','primary school','trường tiểu học','noun','我弟弟在小学学习。','My younger brother studies at primary school.'),
 ('小学生','primary-school student','học sinh tiểu học','noun','她是小学生。','She is a primary-school student.'),
 ('学院','college; institute','học viện; trường cao đẳng','noun','我姐姐在这个学院学习。','My older sister studies at this college.'),
 ('姐姐','older sister','chị gái','noun','这是我姐姐。','This is my older sister.'),
 ('妹妹','younger sister','em gái','noun','我妹妹今年十五岁。','My younger sister is fifteen this year.'),
 ('弟弟','younger brother','em trai','noun','我弟弟今年八岁。','My younger brother is eight this year.'),
 ('男','male','nam','adjective','我们班有十个男学生。','Our class has ten male students.'),
 ('女生','female student','nữ sinh','noun','这两个女生是朋友。','These two female students are friends.'),
 ('男生','male student','nam sinh','noun','那个男生是我弟弟。','That male student is my younger brother.'),
 ('孩子','child','trẻ em; con','noun','这两个孩子都喜欢中文。','Both children like Chinese.'),
 ('儿子','son','con trai','noun','她的儿子是小学生。','Her son is a primary-school student.'),
 ('外国','foreign country; abroad','nước ngoài','noun','我姐姐在外国学习。','My older sister studies abroad.'),
 ('国家','country','quốc gia','noun','你喜欢哪个国家？','Which country do you like?')],
 [grammar(u,'一05','我 / 你 / 您 / 他 / 她 · 我们 / 你们 / 他们 / 她们','Keep track of who is speaking',
 'Use 我 for the speaker, 你 for the listener and 您 for respectful singular address. 他 and 她 sound identical: tā. 我们 includes the speaker; 你们 addresses a group. 他们 can refer to men or a mixed group; 她们 is written for a female group. Do not add 们 to 您 in beginner usage.',[
 ('我是学生，你呢？','I am a student. What about you?'),('您是我们的老师吗？','Are you our teacher?'),
 ('他是中学生，她是小学生。','He is a secondary-school student; she is a primary-school student.'),
 ('我们在一个班，你们呢？','We are in the same class. What about you?'),
 ('他们是男生，她们是女生。','They are male students; the others are female students.')],
 ('我们是一个学生。','我们都是学生。','我们 refers to a group; 一个学生 describes just one student in this ordinary introduction.')),
 grammar(u,'一24','person / pronoun / noun phrase + predicate','Introduce someone with a clear subject',
 'A subject can be a noun, a pronoun or a noun phrase. State who the sentence is about before 是 or the main verb. 我的朋友 is one noun phrase: 我的 modifies 朋友. Chinese does not need an extra pronoun after that subject. Use 是 with a noun description; ordinary adjective descriptions do not require it.',[
 ('学生在这里学习。','Students study here.'),('她在外国学习。','She studies abroad.'),('我的两个朋友在一个班。','My two friends are in the same class.')],
 ('是学生我的朋友。','我的朋友是学生。','Put the subject 我的朋友 before the predicate 是学生 in an ordinary statement. Topic-comment constructions are a different valid pattern, not an error.'))],
 text(u,'d','Meeting two sisters','Find out how the two new friends are related.',[
 ('这两个人是你的朋友吗？','Are these two people your friends?'),('是，她们是我的朋友。','Yes, they are my friends.'),
 ('她们在一个班吗？','Are they in the same class?'),('不在。她们是姐姐和妹妹。','No. They are older and younger sisters.'),
 ('她们都是学生吗？','Are they both students?'),('是。姐姐在学院学习，妹妹是中学生。','Yes. The older sister studies at a college; the younger sister is a secondary-school student.'),
 ('她们的弟弟呢？','What about their younger brother?'),('他是小学生，在小学学习。','He is a primary-school student and studies at primary school.'),
 ('你也是学生吗？','Are you a student too?'),('是。我和她们都学中文。','Yes. The sisters and I all study Chinese.'),
 ('你们的老师是哪国人？','What country is your teacher from?'),('我们的老师是中国人。','Our teacher is Chinese.')],[
 ('gist','How do the two new friends know each other?',['They are sisters','They are in the same class','They are colleagues'],0),
 ('detail','Where does the older sister study?',['At primary school','At a college','At secondary school'],1),
 ('inference','Why is 不在 followed by an explanation?',['To refuse a drink','To end the conversation','To correct the assumption that they share a class'],2)],drama=True),
 text(u,'r','A family introduction','Find which children are in which school.',[
 ('我们家有三个孩子。','There are three children in our family.'),('姐姐是中学生，在中学学习。','The older sister is a secondary-school student and studies at secondary school.'),
 ('妹妹和弟弟是小学生。','The younger sister and brother are primary-school students.'),('他们在一个小学，不在一个班。','They attend the same primary school but are not in the same class.'),
 ('妹妹是女生，弟弟是男生。','The younger sister is a female student; the younger brother is a male student.'),
 ('弟弟的班有十个男学生。','The younger brother’s class has ten male students.'),
 ('这三个孩子都喜欢学中文。','All three children enjoy learning Chinese.'),
 ('老师的儿子也在这所小学学习。','The teacher’s son also studies at this primary school.'),
 ('我们有一个朋友在外国的学院学习。','A friend of ours studies at a college abroad.'),
 ('她很喜欢那个国家。','She really likes that country.')],[
 ('gist','What does the note introduce?',['A restaurant','Children and their schools','A new teacher'],1),
 ('detail','Do the younger sister and brother share a class?',['Yes','The note does not say','No'],2),
 ('inference','Why can 他们 refer to the younger sister and brother?',['It can refer to a mixed group','It means only sisters','It refers to a single adult'],0)],[(1,'中学生'),(2,'小学生')]),
 text(u,'media','The small visitor','Read an original scene: who is the visitor?',[
 ('这个孩子是你的学生吗？','Is this young child your student?'),('不是，他是我弟弟。','No, he is my younger brother.'),
 ('你弟弟在哪儿学习？','Where does your younger brother study?'),('在小学。他是小学生。','At primary school. He is a primary-school student.'),
 ('他喜欢哪个国家？','Which country does he like?'),('他喜欢中国，想在外国学中文。','He likes China and wants to study Chinese abroad.')],[
 ('detail','Who is the visitor?',['A younger brother','A teacher','An older sister'],0)],drama=True),
 dict(tf=[('她们','她们在一个班学习。','They study in the same class.','The group studies in different classes.',False,'一个班 means the same class.'),
 ('外国','我妹妹在外国的中学学习。','My younger sister studies at secondary school abroad.','The younger sister studies abroad.',True,'外国 locates her study abroad.')],
 reply=[('班','你们在一个班吗？','Are you in the same class?',['我喝水。','是，我们在一个班。','这本书很好看。'],1,'The reply directly answers the class question.'),
 ('学生','您是学生吗？','Are you a student?',['不，我是老师。','我们看电影吧。','这是我的书。'],0,'The respectful question asks about student status.')],
 fill=[('姐姐','我的姐姐在学院学中文。','My older sister studies Chinese at a college.'),('国家','她很喜欢这个国家。','She really likes this country.')],
 match=[('女生',[('她们是中学生。','They are female secondary-school students.'),('我是女生。','I am a female student.'),('他是男生。','He is a male student.')]),
 ('孩子',[('她的儿子是小学生。','Her son is a primary-school student.'),('那个孩子今年八岁。','That young child is eight this year.'),('这是我的妹妹。','This is my younger sister.')])]),
 [('Introduce without listing private details','这是我的朋友。','This is my friend.','A brief introduction does not require someone’s age, income or full history.'),
 ('Show respect when meeting the teacher','您好，您是我们的老师吗？','Hello. Are you our teacher?','您好 / 您 is respectful singular address; use 你好 / 你 with peers.')],
 [('她们是你的朋友吗？','Are they your friends?','Identify the relationship',['是，她们是我的朋友','不是，她们是我的姐姐和妹妹']),
 ('你们在一个班吗？','Are you in the same class?','Confirm or correct the class assumption',['我们在一个班','我们不在一个班'])],
 'Native review: country-reference clarity in the original visitor scene; 学院 gloss includes college/institute without asserting an exact foreign qualification.')

u='s1-u14'
write(14,'一起去吧',['Invite a friend with a clear time and activity','Decline an invitation while keeping the conversation friendly','Use 想 and 要 without confusing wishes with firm plans'],[
 ('想','to want; to feel like','muốn','modal verb','你想看电影吗？','Do you feel like watching a film?'),
 ('也','also; too','cũng','adverb','我也喜欢看电影。','I also like watching films.'),
 ('还有','also have; in addition there is','còn có','phrase','我们还有两张票。','We also have two tickets.'),
 ('电影','film; movie','phim','noun','这个电影很好看。','This film is good.'),
 ('电影院','cinema','rạp chiếu phim','noun','电影院在学校旁边。','The cinema is next to the school.'),
 ('门票','admission ticket','vé vào cửa','noun','门票多少钱？','How much is an admission ticket?'),
 ('票','ticket','vé','noun','我有两张票。','I have two tickets.'),
 ('球','ball','bóng','noun','这是我的球。','This is my ball.'),
 ('打球','to play a ball sport','chơi bóng','verb','我们下午去打球。','We are going to play ball this afternoon.'),
 ('爱','to love; to be fond of','yêu; thích','verb','她爱看电影。','She loves watching films.'),
 ('爱好','hobby; interest','sở thích','noun','我的爱好是打球。','My hobby is playing ball.'),
 ('饿','hungry','đói','adjective','我有点儿饿。','I am a little hungry.'),
 ('菜','dish; vegetables','món ăn; rau','noun','这个菜很好吃。','This dish is delicious.'),
 ('饭','cooked rice; meal','cơm; bữa ăn','noun','我们先吃饭。','Let us eat first.'),
 ('米饭','cooked rice','cơm','noun','我要一碗米饭。','I would like a bowl of rice.'),
 ('面包','bread','bánh mì','noun','她想吃面包。','She wants some bread.'),
 ('包子','steamed bun with filling','bánh bao','noun','我想吃两个包子。','I would like two steamed buns.'),
 ('牛奶','milk','sữa bò','noun','你想喝牛奶吗？','Would you like some milk?')],
 [grammar(u,'一03','想 + verb · 要 + verb / noun','Distinguish a wish from a decision',
 '想 + verb expresses a wish or inclination: 想去. 要 + verb often expresses a decision, intention or need. 要 + noun orders or requests something: 我要米饭. Context matters; 要 does not always mean an obligation. Negate a wish with 不想. 不要 can sound like a refusal or prohibition. Soften invitations with 吗 or 吧.',[
 ('我想去看电影。','I feel like going to see a film.'),('我下午要去打球。','I am going to play ball this afternoon.'),
 ('我要一碗米饭，不要面包。','I would like a bowl of rice, not bread.'),('我今天不想去。','I do not feel like going today.')],
 ('我想两张票。','我想买两张票。','For wanting to buy something, put the verb 买 after 想; 要两张票 directly requests tickets.')),
 grammar(u,'一13','subject + 也 / 还 + predicate','Add a shared interest or another activity',
 '也 adds a matching fact about another person or activity: 我也想去. 还 adds something further or indicates continuation: 还要吃饭 / 还在看. Both come before the predicate, after the subject. 还有 introduces another item that is available. Do not put 也 at the end as if it were English “too”.',[
 ('她想打球，我也想打球。','She wants to play ball; I do too.'),('我们看电影，还想吃饭。','We are watching a film and also want to eat.'),
 ('他还在看电影。','He is still watching the film.'),('我有面包，还有牛奶。','I have bread and also milk.')],
 ('我想去也。','我也想去。','Place 也 before 想, not at the end.'))],
 text(u,'d','Tickets for tonight','Listen for the plan and the reason for changing it.',[
 ('你晚上想看电影吗？','Do you feel like seeing a film tonight?'),('想。我爱看电影。','Yes. I love watching films.'),
 ('我也想去，电影院就在学校旁边。','I want to go too. The cinema is right next to the school.'),('门票多少钱？','How much is an admission ticket?'),
 ('三十块。我还有两张票。','Thirty yuan. I also have two tickets.'),('好。可是我有点儿饿。','Good. But I am a little hungry.'),
 ('那我们先吃饭，再看电影。','Then let us eat first and see the film afterwards.'),('行。我想吃米饭和菜。','Okay. I would like rice and a dish.'),
 ('我想吃包子，还想喝牛奶。','I would like steamed buns and some milk too.'),('你不要面包了吗？','Do you not want bread now?'),
 ('今天不要。明天下午一起打球吧？','Not today. Shall we play ball together tomorrow afternoon?'),('好，我的爱好就是打球！','Yes. Playing ball is just my hobby!')],[
 ('gist','What do they decide to do tonight?',['Play ball only','Eat and then see a film','Study all evening'],1),
 ('detail','How much is an admission ticket?',['Twenty yuan','Forty yuan','Thirty yuan'],2),
 ('inference','Why do they eat before the film?',['One friend is hungry','The cinema is closed','The tickets are for tomorrow'],0)],drama=True),
 text(u,'r','An invitation with room to say no','Find which invitation is accepted and which is declined.',[
 ('我的爱好是看电影和打球。','My hobbies are watching films and playing ball.'),
 ('朋友今天想去电影院，我也想看那个电影。','My friend wants to go to the cinema today, and I want to see that film too.'),
 ('她有两张票，不用再买门票。','She has two tickets, so there is no need to buy admission tickets again.'),
 ('我们都饿了，先在学校吃饭。','We are both hungry, so we eat at school first.'),
 ('她吃米饭和菜，我吃包子，喝牛奶。','She eats rice and a dish; I eat steamed buns and drink milk.'),
 ('桌上还有面包，可是我们不想吃。','There is also bread on the table, but we do not feel like eating it.'),
 ('她明天还想打球，可是我要学中文。','She also wants to play ball tomorrow, but I am going to study Chinese.'),
 ('我说：今天去看电影，明天不去打球。','I say: we can see a film today, but I will not play ball tomorrow.'),
 ('她说：好，球在我家，下次一起玩。','She says: okay, the ball is at my place; we can play together next time.')],[
 ('gist','Which invitation does the writer accept?',['Seeing a film today','Playing ball tomorrow','Both invitations'],0),
 ('detail','Why does the writer decline tomorrow?',['There are no tickets','The ball is missing','The writer plans to study Chinese'],2),
 ('inference','What does 下次一起玩 show?',['Anger','The invitation can be repeated another time','A demand to buy bread'],1)],[(4,'米饭'),(6,'中文')]),
 text(u,'media','A small plan','Read this original verse rhythmically; identify the two shared activities.',[
 ('你爱电影，我爱球。','You love films; I love ball games.'),('你想看，我也想去。','You want to watch; I want to go too.'),
 ('先吃饭，喝牛奶。','Eat first; drink some milk.'),('米饭和菜都好吃。','Rice and a dish both taste good.'),
 ('还有面包和包子。','There are bread and steamed buns too.'),('今天看电影，明天再打球。','Watch a film today; play ball tomorrow.')],[
 ('detail','Which activities are proposed?',['Shopping and swimming','Watching a film and playing ball','Reading and writing'],1)]),
 dict(tf=[('票','我有两张票，我们一起去吧。','I have two tickets. Let us go together.','The speaker invites the listener to go together.',True,'一起去吧 is an invitation.'),
 ('爱好','她的爱好是打球，不是看电影。','Her hobby is playing ball, not watching films.','Her stated hobby is watching films.',False,'不是看电影 explicitly denies that.')],
 reply=[('想','明天想一起去打球吗？','Would you like to play ball together tomorrow?',['这个菜三十块。','我叫小夜。','不好意思，明天我要学习。'],2,'It declines with a reason rather than answering a different question.'),
 ('饿','你饿了吗？','Are you hungry?',['我想先吃饭。','电影在七点开始。','我不认识他。'],0,'The reply answers hunger and proposes food.')],
 fill=[('还有','我有米饭，还有菜。','I have rice and also a dish.'),('面包','她不想吃面包，想吃包子。','She does not want bread; she wants steamed buns.')],
 match=[('电影',[('我们晚上去电影院。','We are going to the cinema tonight.'),('我想买一张门票。','I want to buy one admission ticket.'),('我爱看这个电影。','I love watching this film.')]),
 ('球',[('我的球在学校。','My ball is at school.'),('她也想喝牛奶。','She also wants some milk.'),('我们明天再打球。','Let us play ball tomorrow instead.')])]),
 [('Invite with an easy answer','晚上一起看电影吗？','Shall we see a film together tonight?','An invitation asks about willingness; it does not presume agreement.'),
 ('Decline while leaving the door open','不好意思，明天我要学习。下次吧。','Sorry, I need to study tomorrow. Another time.','A brief reason and 下次吧 can soften a refusal without making a false promise.')],
 [('晚上想看电影吗？','Would you like to see a film tonight?','Accept or decline the invitation',['我也想去','不好意思，今天不想去']),
 ('先吃米饭还是包子？','Would you like rice or steamed buns first?','Choose a food',['我想吃米饭','我想吃包子'])],
 'Native review: lyrical rhythm is original text, not a claim that it is a singable song; 爱看 is fondness, not a literal love declaration.')

u='s1-u15'
write(15,'你说的是哪一个',['Ask which event, people and place a message means','Use a question word without adding 吗','Clarify a mistaken date before making plans'],[
 ('多','how (in degree questions); many','bao nhiêu; nhiều','question word','你弟弟多大？','How old is your younger brother?'),
 ('多少','how many; how much','bao nhiêu','question word','一共有多少人？','How many people are there altogether?'),
 ('几','how many (small expected number)','mấy; bao nhiêu','question word','你们有几个人？','How many people are in your group?'),
 ('哪','which','nào','question word','你去哪个电影院？','Which cinema are you going to?'),
 ('哪里','where','ở đâu','question word','你在哪里？','Where are you?'),
 ('哪儿','where','ở đâu','question word','我们在哪儿见？','Where shall we meet?'),
 ('哪些','which ones','những cái nào; những ai','question word','哪些朋友想去？','Which friends want to go?'),
 ('什么','what','gì','question word','你们想看什么？','What do you want to see?'),
 ('谁','who','ai','question word','谁买票？','Who is buying the tickets?'),
 ('日期','date','ngày tháng','noun','请问，日期对吗？','Excuse me, is the date correct?'),
 ('星期天','Sunday','Chủ nhật','noun','星期天我们去看电影。','We are going to see a film on Sunday.'),
 ('后天','the day after tomorrow','ngày kia','noun','后天是星期天。','The day after tomorrow is Sunday.'),
 ('门口','entrance; doorway','cửa ra vào','noun','我们在门口见。','Let us meet at the entrance.'),
 ('地图','map','bản đồ','noun','你看地图了吗？','Have you looked at the map?'),
 ('地点','location; venue','địa điểm','noun','地点在学校旁边。','The venue is next to the school.'),
 ('记住','to remember; to keep in mind','ghi nhớ','verb','请记住这个地点。','Please remember this location.'),
 ('错','wrong; mistake','sai; lỗi','adjective','这个日期错了。','This date is wrong.'),
 ('回答','to answer; answer','trả lời; câu trả lời','verb','请回答这个问题。','Please answer this question.')],
 [grammar(u,'一04','多大 / 多少 / 几 / 哪 / 哪里 / 哪儿 / 哪些 / 什么 / 谁 / 怎么','Choose the information you need',
 '多 + adjective asks degree: 多大 asks age or size. 多少 asks amount; 几 asks a number expected to be small and takes a classifier before a noun. 哪 chooses one; 哪些 chooses several. 哪里 and 哪儿 ask place. 什么 asks a thing, 谁 a person, 怎么 a method. Put the question word in the answer’s position.',[
 ('你妹妹多大？','How old is your younger sister?'),('门票多少钱？','How much is an admission ticket?'),('你们有几个人？','How many people are in your group?'),
 ('你想看哪个电影？','Which film do you want to see?'),('地点在哪里？我们在哪儿见？','Where is the venue? Where shall we meet?'),
 ('哪些人要去？','Which people are going?'),('谁买票？你想吃什么？','Who is buying the tickets? What would you like to eat?'),
 ('我们怎么去？','How shall we get there?')],
 ('你们有几人？','你们有几个人？','Use a classifier after 几 before 人 in the ordinary beginner pattern.')),
 grammar(u,'一46','statement slot → question word (no 吗)','Ask a follow-up question without an extra question particle',
 'Keep ordinary Chinese word order when using a question word: 你去学校 becomes 你去哪里. The question word itself asks for information, so do not add 吗. 谁 can be the subject or object. Several short follow-ups are easier to answer than one long interrogation. Use 请问 with an unfamiliar person.',[
 ('谁在电影院门口？','Who is at the cinema entrance?'),('你在等谁？','Who are you waiting for?'),('请问，这个地点怎么去？','Excuse me, how do I get to this location?')],
 ('你在哪里吗？','你在哪里？','A where-question does not take the yes/no particle 吗.'))],
 text(u,'d','Which cinema was that?','Find the corrected date, place and ticket buyer.',[
 ('后天一起看电影吧。','Let us see a film together the day after tomorrow.'),('后天是星期天吗？','Is the day after tomorrow Sunday?'),
 ('是，星期天。','Yes, Sunday.'),('看什么电影？地点在哪里？','What film? Where is the venue?'),
 ('看一个中国电影，在学校旁边的电影院。','A Chinese film, at the cinema next to the school.'),('哪些人想去？一共几个人？','Which people want to go? How many people altogether?'),
 ('我和两个朋友，一共三个人。','Me and two friends: three people altogether.'),('门票多少钱？谁买票？','How much are tickets? Who will buy them?'),
 ('一张三十块，我买。','Thirty yuan each. I will buy them.'),('我们在哪儿见？怎么去？','Where shall we meet? How do we get there?'),
 ('看地图，我们在电影院门口见。记住，日期是星期天。','Check the map. We will meet at the cinema entrance. Remember, the date is Sunday.'),
 ('知道了。我刚才的日期错了，谢谢你回答。','Got it. The date I had just now was wrong. Thanks for answering.')],[
 ('gist','What are the speakers doing?',['Cancelling a class','Clarifying a film outing','Reviewing an exam result'],1),
 ('detail','Who will buy the tickets?',['The first speaker','A teacher','The second speaker'],0),
 ('inference','Why does the last speaker thank the friend?',['The friend bought lunch','The friend changed the cinema','The friend corrected the date and clarified the plan'],2)],drama=True),
 text(u,'r','The corrected plan','Use the final message, not the writer’s earlier mistake.',[
 ('今天我问朋友：后天去哪儿？','Today I ask a friend: where are we going the day after tomorrow?'),
 ('他回答：星期天去学校旁边的电影院。','He answers: on Sunday we are going to the cinema next to the school.'),
 ('我看地图，记住了地点。','I look at the map and remember the location.'),
 ('我们在电影院门口见，一共三个人。','We will meet at the cinema entrance; there are three people altogether.'),
 ('我问哪些朋友去，他说是我认识的两个学生。','I ask which friends are going; he says two students I know.'),
 ('门票一张三十块，他买票。','Admission tickets are thirty yuan each; he is buying them.'),
 ('我还问看什么电影，他说是中国电影。','I also ask what film we are seeing; he says it is a Chinese film.'),
 ('我刚才的日期错了，现在知道是星期天。','The date I had just now was wrong; now I know it is Sunday.')],[
 ('gist','What is the corrected plan?',['Go to a film on Sunday','Meet a teacher on Monday','Buy a map tomorrow'],0),
 ('detail','Where will the group meet?',['Inside the school','At the cinema entrance','At the writer’s home'],1),
 ('inference','Which fact should override the earlier remembered date?',['Ticket price','Number of students','The friend’s explicit Sunday confirmation'],2)],[(2,'地点'),(3,'门口')]),
 text(u,'media','Too many questions?','Read an original scene: distinguish the two people asking questions.',[
 ('你弟弟多大？','How old is your younger brother?'),('八岁。你有多少个问题？','Eight. How many questions do you have?'),
 ('我还想问，他在哪里上学？','I also want to ask: where does he go to school?'),('在小学。还有什么？','At primary school. Anything else?'),
 ('他怎么去学校？','How does he get to school?'),('他走路去。现在我问你！','He walks there. Now it is my turn to ask you!')],[
 ('inference','What does 现在我问你 imply?',['The conversation is over','The second person wants a turn to ask','The brother has no school'],1)],drama=True),
 dict(tf=[('多少','门票一张三十块，一共三张。','Tickets are thirty yuan each; there are three tickets in total.','The three tickets cost thirty yuan altogether.',False,'Thirty is the price of one ticket, not all three.'),
 ('日期','我记住了，日期是星期天。','I remember: the date is Sunday.','The speaker now remembers the Sunday plan.',True,'记住了 confirms remembering.')],
 reply=[('谁','谁在门口等我们？','Who is waiting for us at the entrance?',['三十块。','我的两个朋友。','星期天。'],1,'谁 needs a person or group of people.'),
 ('哪儿','我们在哪儿见？','Where shall we meet?',['星期天。','三个人。','在电影院门口。'],2,'哪儿 asks for a place.')],
 fill=[('地图','我看了地图，知道怎么去。','I looked at the map and know how to get there.'),('错','这个日期错了，是后天。','This date is wrong; it is the day after tomorrow.')],
 match=[('回答',[('请回答：你在哪个班？','Please answer: which class are you in?'),('哪些学生想去？','Which students want to go?'),('你弟弟多大？','How old is your younger brother?')]),
 ('地点',[('请记住这个地点。','Please remember this location.'),('我们后天在哪儿见？','Where shall we meet the day after tomorrow?'),('一共有多少人？','How many people are there altogether?')])]),
 [('Ask one follow-up before piling on','看什么电影？','What film are we seeing?','Get the main missing detail first; then ask about time, place or cost.'),
 ('Ask an unfamiliar person politely','请问，电影院在哪里？','Excuse me, where is the cinema?','请问 can introduce a request for information without changing the question’s word order.')],
 [('我们在哪儿见？','Where shall we meet?','Name a meeting place',['在电影院门口见','在学校门口见']),
 ('一共几个人？','How many people altogether?','Give the group size',['一共三个人','一共两个人'])],
 'Native review: the deliberately rapid sequence of questions in the scene; 刚才 is glossed support vocabulary, not a new grammar claim here.')

u='s1-u16'
write(16,'这本还是那本',['Identify an object using demonstratives and a classifier','Describe whose object it is without ambiguous reference','Contrast some objects with other objects'],[
 ('这儿','here','ở đây','pronoun','请放在这儿。','Please put it here.'),
 ('这里','here; this place','ở đây; chỗ này','pronoun','这里有书和本子。','There are books and notebooks here.'),
 ('这些','these','những cái này','pronoun','这些书都是我的。','These books are all mine.'),
 ('那儿','there','ở đó','pronoun','你的书包在那儿。','Your schoolbag is there.'),
 ('那里','there; that place','ở đó; chỗ đó','pronoun','那里有两个杯子。','There are two cups there.'),
 ('那些','those','những cái đó','pronoun','那些本子不是我的。','Those notebooks are not mine.'),
 ('有的','some (members of a set)','một số','pronoun','这些书有的很新。','Some of these books are very new.'),
 ('新','new','mới','adjective','这是一本新书。','This is a new book.'),
 ('白','white','trắng','adjective','我要白的杯子。','I would like the white cup.'),
 ('书','book','sách','noun','这是我的书。','This is my book.'),
 ('本','classifier for books','lượng từ cho sách','classifier','我有两本书。','I have two books.'),
 ('本子','notebook','vở','noun','这个本子是新的。','This notebook is new.'),
 ('书包','schoolbag','cặp sách','noun','我的书包在桌上。','My schoolbag is on the table.'),
 ('杯','cupful; classifier for drinks','cốc; lượng từ cho đồ uống','classifier','请给我一杯水。','Please give me a glass of water.'),
 ('杯子','cup; glass','cốc; ly','noun','这是你的杯子吗？','Is this your cup?'),
 ('拿','to take; to hold','cầm; lấy','verb','请拿那本书。','Please take that book.'),
 ('放','to put; to place','đặt; để','verb','书放在桌上。','The book is placed on the table.'),
 ('用','to use','dùng; sử dụng','verb','你可以用我的本子。','You can use my notebook.')],
 [grammar(u,'一06','这 / 那 · 这儿 / 那儿 · 这里 / 那里 · 这些 / 那些 · 别的 / 有的','Point to a thing, place or subset',
 '这 and 那 distinguish this from that; add classifier + noun: 这本书. 这儿 / 这里 and 那儿 / 那里 name places. 这些 / 那些 refer to plural sets without an extra 们. 有的 picks some members of a known set; 别的 means other or different ones. Establish the set before saying 有的 so the reference is clear.',[
 ('这是我的书，那是你的本子。','This is my book; that is your notebook.'),('这儿有书，那儿有杯子。','There are books here and cups there.'),
 ('这里的书是新的，那里的书不是新的。','The books here are new; the books there are not.'),
 ('这些书有的很新，那些本子有的很小。','Some of these books are very new; some of those notebooks are very small.'),
 ('你想用别的本子吗？','Would you like to use a different notebook?')],
 ('这些们书是我的。','这些书是我的。','这些 already refers to a plural set; do not add 们.')),
 grammar(u,'一27','noun / pronoun + 的 · adjective · number + classifier + noun','Describe which object you mean',
 'Place descriptions before the noun: 我的书, 新书, 两本书. A possessor or longer adjective phrase often uses 的: 我的书, 很新的书. A simple adjective may attach directly, as in 新书. A quantity needs a classifier: 一本书, 一个杯子. Do not confuse 本 (classifier) with 本子 (notebook) or 杯 (cupful) with 杯子 (container).',[
 ('老师的书在这里。','The teacher’s book is here.'),('我的白杯子在那儿。','My white cup is there.'),('那两本新书是你的。','Those two new books are yours.'),
 ('我要一杯水，不是一个杯子。','I would like a glass of water, not an empty cup.')],
 ('我有两书。','我有两本书。','Put the classifier 本 between the number and 书.'))],
 text(u,'d','Before you take that book','Listen for the owner of each object.',[
 ('这些书都是你的吗？','Are all these books yours?'),('不是，有的是我的，有的是老师的。','No. Some are mine, and some are the teacher’s.'),
 ('我可以拿这本新书吗？','May I take this new book?'),('那本是我的，这本是老师的。','That one is mine; this one is the teacher’s.'),
 ('那我用你的书吧。我的本子在哪里？','Then I will use your book. Where is my notebook?'),('在那儿，你的书包旁边。','Over there, next to your schoolbag.'),
 ('那些白杯子也是老师的吗？','Are those white cups also the teacher’s?'),('是。我的杯子在这里。','Yes. My cup is here.'),
 ('请给我一杯水。','Please give me a glass of water.'),('好。你先拿杯子，我来放书。','Okay. You take a cup first; I will put the books away.'),
 ('这些本子放这儿吗？','Do these notebooks go here?'),('对。那些书放那里。','Yes. Those books go there.')],[
 ('gist','What are they sorting out?',['People’s books and study things','A cinema timetable','The school’s meal prices'],0),
 ('detail','Who owns the new book pointed to as 这本?',['The second speaker','The teacher','The first speaker'],1),
 ('inference','Why does the first speaker switch to 那本?',['It is white','It is not a book','They can borrow the friend’s book rather than the teacher’s'],2)],drama=True),
 text(u,'r','Leave the right things on the table','Find which objects belong here and which belong there.',[
 ('这里有两本新书和三个本子。','Here there are two new books and three notebooks.'),
 ('这两本书是老师的，那些本子是我的。','These two books are the teacher’s, and those notebooks are mine.'),
 ('本子有的大，有的小。','Some notebooks are big; some are small.'),
 ('老师的白杯子在那儿，我的杯子在这儿。','The teacher’s white cup is there; my cup is here.'),
 ('请拿我的杯子，给我一杯水。','Please take my cup and give me a glass of water.'),
 ('你可以用我的本子，不要拿老师的书。','You may use my notebook; do not take the teacher’s books.'),
 ('我的书包在桌子旁边。','My schoolbag is next to the table.'),
 ('用完的本子放这里，老师的书放那里。','Put notebooks you have finished using here, and the teacher’s books there.')],[
 ('gist','What is this note for?',['Introducing students','Explaining where objects belong','Buying film tickets'],1),
 ('detail','Which object may the reader use?',['The teacher’s book','The teacher’s cup','The writer’s notebook'],2),
 ('inference','Why should the reader check ownership before taking a book?',['The teacher’s books are not offered for borrowing','All books are broken','There are no books'],0)],[(1,'老师'),(3,'白')]),
 text(u,'media','This side, that side','Read this original verse: follow the objects across the two places.',[
 ('这本新书放这里。','Put this new book here.'),('那本书放在那儿。','Put that book there.'),
 ('这些本子有的大。','Some of these notebooks are big.'),('那些杯子有的白。','Some of those cups are white.'),
 ('拿一本，读一下。','Take one book and read a little.'),('用完再放回书包。','Put it back in the schoolbag after using it.')],[
 ('detail','What is taken for reading?',['A cup','A notebook','A book'],2)]),
 dict(tf=[('本','这里有两本书，不是两个本子。','There are two books here, not two notebooks.','There are two notebooks here.',False,'书 and 本子 are different objects.'),
 ('杯','那儿有一个杯子，里面有一杯水。','There is a cup there, with a glassful of water inside.','杯子 names the container and 杯 measures its contents.',True,'一个杯子 is the container; 一杯水 is the drink amount.')],
 reply=[('拿','我可以拿老师的书吗？','May I take the teacher’s book?',['三十块。','请先问老师。','我想看电影。'],1,'Ask the owner before taking the book.'),
 ('这里','这些本子放哪里？','Where do these notebooks go?',['放这里。','我不饿。','她是学生。'],0,'The question asks for placement.')],
 fill=[('书包','我的书包里有三本书。','There are three books in my schoolbag.'),('白','那个白杯子不是我的。','That white cup is not mine.')],
 match=[('放',[('请放在这儿。','Please put it here.'),('你可以用那个本子。','You may use that notebook.'),('这些书是新的。','These books are new.')]),
 ('那些',[('那些杯子在老师的桌上。','Those cups are on the teacher’s table.'),('那里有我的书包。','My schoolbag is there.'),('这两本书不是我的。','These two books are not mine.')])]),
 [('Ask before borrowing','我可以用你的本子吗？','May I use your notebook?','Ownership and permission are different. Pointing at an object is not permission to take it.'),
 ('Resolve a reference by pointing clearly','这本是老师的，那本是我的。','This one is the teacher’s; that one is mine.','The listener needs shared visual context for 这 / 那. Repeat 书 if the objects are not visible.')],
 [('你想用哪个本子？','Which notebook would you like to use?','Identify a notebook',['我想用这个本子','我想用那个本子']),
 ('这些书放哪里？','Where do these books go?','Give a placement instruction',['放在这里','放在那儿'])],
 'Native review: literary omissions of 是 / 很 in the short original verse are intentional; use full ordinary forms in conversation. Borrowing choices depend on visible referents.')

from retrievals import apply
apply(13,16)
