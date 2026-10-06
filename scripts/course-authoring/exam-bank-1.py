"""Original GF2021 level-1 practice; not official exam questions or a full mock."""
from common import ROOT, py
import json, sys

def choice(zh, en):
    return dict(zh=zh, py=py(zh), en=en)

def comprehension(fmt, sentence, en, prompt, answers, why):
    return dict(format=fmt, sentence=sentence, py=py(sentence), en=en,
        prompt=prompt, promptPy=py(prompt), choices=[choice(*a) for a in answers],
        answer=answers[0][0], explanation=why)

def ordering(segments, en, prompt, wrong, why):
    segments=[s.replace('。','') for s in segments]
    wrong=[s.replace('。','') for s in wrong]
    sentence=''.join(segments)
    return dict(format='ordering', sentence=sentence, py=py(sentence), en=en,
        prompt=prompt, promptPy=py(prompt), segments=[choice(s,'Sentence part') for s in segments],
        choices=[choice(sentence,en),*[choice(s,'Alternative word order') for s in wrong]],
        answer=sentence, explanation=why)

R=lambda *args:comprehension('reading',*args)
L=lambda *args:comprehension('listening',*args)
O=ordering

identity=[
R('我的姐姐是医生，妹妹是学生。','My elder sister is a doctor; my younger sister is a student.','谁是医生？',[('姐姐','Elder sister'),('妹妹','Younger sister'),('老师','Teacher'),('哥哥','Elder brother')],'姐姐 is explicitly identified as the doctor; 妹妹 is the student.'),
R('他是我的同学，不是我的弟弟。','He is my classmate, not my younger brother.','他是谁？',[('同学','Classmate'),('弟弟','Younger brother'),('医生','Doctor'),('工人','Worker')],'The positive identity is 同学; 弟弟 is explicitly denied.'),
R('那个孩子的妈妈是老师。','That child’s mother is a teacher.','谁是老师？',[('孩子的妈妈','The child’s mother'),('我的妈妈','My mother'),('朋友的姐姐','My friend’s elder sister'),('那个孩子','That child')],'The stated teacher is the child’s mother; the child is not identified as a teacher.'),
R('妈妈在家，爸爸在学校。','Mother is at home; father is at school.','谁在学校？',[('爸爸','Father'),('妈妈','Mother'),('哥哥','Elder brother'),('妹妹','Younger sister')],'爸爸 is located at school; 妈妈 is located at home.'),
R('我朋友会说汉语，也会读汉字。','My friend can speak Mandarin and read Chinese characters.','朋友会做什么？',[('说汉语和读汉字','Speak Mandarin and read characters'),('不说汉语','Not speak Mandarin'),('不读汉字','Not read characters'),('不说话','Not speak')],'Both speaking Mandarin and reading characters are affirmed; the negative alternatives contradict the statement.'),
R('我有两个妹妹，没有哥哥。','I have two younger sisters and no elder brother.','我没有谁？',[('哥哥','Elder brother'),('妹妹','Younger sister'),('妈妈','Mother'),('爸爸','Father')],'没有哥哥 is an explicit negative; there are two 妹妹.'),
L('我的哥哥是工人，他今天不上班。','My elder brother is a worker; he is not working today.','哥哥是做什么的？',[('工人','Worker'),('学生','Student'),('医生','Doctor'),('老师','Teacher')],'His occupation is 工人 even though he is not at work today.'),
L('新来的老师教我们汉字。','The new teacher teaches us Chinese characters.','谁教汉字？',[('新来的老师','The new teacher'),('我的妹妹','My younger sister'),('那个孩子','That child'),('他的爸爸','His father')],'The subject of 教我们汉字 is 新来的老师.'),
L('今天是奶奶的生日，爷爷也来。','Today is grandmother’s birthday; grandfather is also coming.','今天是谁的生日？',[('奶奶的','Grandmother’s'),('爷爷的','Grandfather’s'),('妈妈的','Mother’s'),('姐姐的','Elder sister’s')],'爷爷 also attends, but the birthday belongs to 奶奶.'),
L('朋友的儿子在家，他的女儿在学校。','My friend’s son is at home; his daughter is at school.','谁在家？',[('儿子','Son'),('女儿','Daughter'),('老师','Teacher'),('工人','Worker')],'The locations distinguish 儿子 at home from 女儿 at school.'),
L('这是我的书，那是别人的书。','This is my book; that is someone else’s book.','那是谁的书？',[('别人的','Someone else’s'),('我的','Mine'),('老师的','The teacher’s'),('妹妹的','My younger sister’s')],'The second book is only identified as someone else’s; the person is not specified.'),
L('我不是老师，我是大学生。','I am not a teacher; I am a university student.','我是谁？',[('大学生','University student'),('老师','Teacher'),('医生','Doctor'),('中学生','Secondary-school student')],'大学生 is explicitly affirmed; 老师 is negated.'),
O(['妹妹','是','学生。'],'My younger sister is a student.','谁是学生？',['学生妹妹是。','妹妹学生是。','是学生妹妹。'],'Use the stated ordinary subject–是–identity order; 妹妹 is the subject.'),
O(['哥哥','不是','老师。'],'My elder brother is not a teacher.','谁不是老师？',['哥哥不老师是。','不是哥哥老师。','老师哥哥不是。'],'Place 不是 before the identity complement 老师.'),
O(['老师','教','汉语。'],'The teacher teaches Mandarin.','谁教汉语？',['汉语教老师。','老师汉语教。','教汉语老师。'],'老师 performs 教; 汉语 is what is taught. The alternatives reverse the relation or break ordinary word order.'),
O(['爸爸','在','学校。'],'Father is at school.','谁在学校？',['在爸爸学校。','爸爸学校在。','学校在爸爸。'],'在 introduces the location after the subject 爸爸.'),
O(['姐姐','有','两个孩子。'],'My elder sister has two children.','谁有两个孩子？',['两个孩子有姐姐。','姐姐两个有孩子。','有姐姐两个孩子。'],'姐姐 is the possessor; 两个孩子 is the object with a complete numeral-classifier phrase.'),
O(['朋友','会说','汉语。'],'My friend can speak Mandarin.','谁会说汉语？',['汉语会说朋友。','朋友汉语会说。','会说朋友汉语。'],'Keep 会说 together after the subject; 汉语 is the language spoken.'),
]

numbers=[
R('一本书十块，三本书三十块。','One book costs ten yuan; three cost thirty.','三本书多少钱？',[('三十块','Thirty yuan'),('十块','Ten yuan'),('二十块','Twenty yuan'),('四十块','Forty yuan')],'The price for three books is stated as 三十块, consistent with three times ten.'),
R('我们星期六上午九点见面。','We meet at nine on Saturday morning.','几点见面？',[('上午九点','Nine in the morning'),('下午九点','Nine in the afternoon'),('上午六点','Six in the morning'),('下午六点','Six in the afternoon')],'The message specifies 上午九点; 星期六 is the day, not the time.'),
R('哥哥二十岁，妹妹十五岁。','My elder brother is twenty; my younger sister is fifteen.','妹妹多大？',[('十五岁','Fifteen years old'),('二十岁','Twenty years old'),('五岁','Five years old'),('十岁','Ten years old')],'十五岁 is the younger sister’s age; twenty belongs to her brother.'),
R('桌子上有两杯水和一杯茶。','There are two glasses of water and one cup of tea on the table.','有几杯水？',[('两杯','Two cups'),('一杯','One cup'),('三杯','Three cups'),('四杯','Four cups')],'Count only water: 两杯水. The extra cup contains tea.'),
R('今天十月六日，明天十月七日。','Today is October sixth; tomorrow is October seventh.','明天几月几日？',[('十月七日','October seventh'),('十月六日','October sixth'),('七月十日','July tenth'),('六月十日','June tenth')],'明天 is explicitly 十月七日; do not reverse month and day.'),
R('我买五个包子，朋友买两个。','I buy five steamed buns; my friend buys two.','朋友买几个包子？',[('两个','Two'),('五个','Five'),('七个','Seven'),('三个','Three')],'The question asks only about the friend, who buys two, not the group’s total.'),
L('水三块，茶五块。我买茶。','Water costs three yuan; tea costs five. I buy tea.','我买的东西多少钱？',[('五块','Five yuan'),('三块','Three yuan'),('八块','Eight yuan'),('两块','Two yuan')],'Only tea is bought, so its price 五块 applies; eight would combine unpurchased water and tea.'),
L('我们下午两点半上车，三点到。','We board at half past two and arrive at three in the afternoon.','几点上车？',[('两点半','Half past two'),('三点','Three'),('三点半','Half past three'),('两点','Two')],'上车 is at 两点半; 到 is at 三点.'),
L('学校里有四个人，老师还没来。','There are four people inside the school; the teacher has not arrived.','现在有几个人？',[('四个人','Four people'),('五个人','Five people'),('三个人','Three people'),('一个人','One person')],'Count the four people currently present; the absent teacher is not a fifth person inside the school.'),
L('我拿两本书和三个本子。','I take two books and three notebooks.','我拿几本书？',[('两本','Two books'),('三本','Three books'),('五本','Five books'),('一本','One book')],'Only the books are counted in the question. There are two books and three separate notebooks.'),
L('我们八点看电影，我七点半到。','We watch the film at eight; I arrive at half past seven.','几点看电影？',[('八点','Eight'),('七点半','Half past seven'),('八点半','Half past eight'),('七点','Seven')],'Watching the film is planned for 八点; 七点半 is the visitor’s arrival.'),
L('一杯奶和半杯水，我都喝了。','I drank one glass of milk and half a glass of water.','我喝了多少水？',[('半杯','Half a cup'),('一杯','One cup'),('两杯','Two cups'),('三杯','Three cups')],'Water is 半杯; the full cup contains milk.'),
O(['我','买了','三本书。'],'I bought three books.','谁买了三本书？',['三本书买了我。','我三本买了书。','我买三了本书。'],'The subject 我 precedes 买了; keep 三本书 intact as the object.'),
O(['妹妹','今年','十五岁。'],'My younger sister is fifteen this year.','谁今年十五岁？',['今年妹妹岁十五。','妹妹十五今年岁。','十五岁今年妹妹。'],'Place the time 今年 before the age predicate 十五岁.'),
O(['我们','八点','见面。'],'We meet at eight.','谁八点见面？',['我们见面八点。','见面我们八点。','见面八点我们。'],'Keep 见面 together and put the clock time before it in ordinary subject–time–verb order.'),
O(['桌子上','有','两杯水。'],'There are two glasses of water on the table.','哪里有两杯水？',['两杯水有桌子上。','桌子上两杯水有。','有两杯水桌子上。'],'Use the stated place–有–object order. Inversion or a postponed location does not answer the requested ordinary order.'),
O(['哥哥','喝了','半杯奶。'],'My elder brother drank half a glass of milk.','谁喝了半杯奶？',['半杯奶喝了哥哥。','哥哥半喝了杯奶。','哥哥喝半了杯奶。'],'The subject is 哥哥; 半杯奶 stays together after 喝了.'),
O(['这本书','是','一百块。'],'This book costs one hundred yuan.','什么是一百块？',['一百块这本书是。','是这本书一百块。','这本书一百块是。'],'Keep the book phrase and 一百块 whole. 是 introduces the stated price in this exchange.'),
]

daily=[
R('我先吃晚饭，再去学校。','I eat dinner first, then go to school.','先做什么？',[('吃晚饭','Eat dinner'),('去学校','Go to school'),('看电影','Watch a film'),('买衣服','Buy clothes')],'先 marks eating dinner as the first action; school comes after 再.'),
R('书店在学校西边，商店在南边。','The bookshop is west of the school; the shop is south.','书店在哪里？',[('西边','West side'),('南边','South side'),('东边','East side'),('北边','North side')],'The bookshop is 西边; 南边 identifies the other shop.'),
R('昨天我没去学校，在家看书。','I did not go to school yesterday; I read at home.','昨天我在哪里？',[('在家','At home'),('在学校','At school'),('在商店','At the shop'),('在车站','At the station')],'The speaker says 在家 and explicitly denies going to school.'),
R('弟弟想吃米饭，不想吃包子。','My younger brother wants rice, not steamed buns.','弟弟想吃什么？',[('米饭','Rice'),('包子','Steamed buns'),('水果','Fruit'),('面包','Bread')],'米饭 is wanted; 包子 is explicitly declined.'),
R('下雨了，我们今天不出去。','It is raining; we are not going out today.','今天出去吗？',[('不出去','Not going out'),('现在出去','Go out now'),('先出去','Go out first'),('一起出去','Go out together')],'今天不出去 directly states the plan for today.'),
R('门开着，朋友在门外等我。','The door is open; my friend is waiting outside it.','朋友在哪里？',[('门外','Outside the door'),('门里','Inside the door'),('楼上','Upstairs'),('楼下','Downstairs')],'The friend is 门外; an open door does not establish that they entered.'),
L('我坐车去上课，回来走路。','I go to class by vehicle and walk back.','去上课怎么走？',[('坐车','Go by vehicle'),('走路','Walk'),('坐飞机','Fly'),('不去','Not go')],'The outward journey is by vehicle; walking belongs to the return journey. The specific vehicle is not stated.'),
L('妈妈在楼上看书，爸爸在楼下做饭。','Mother reads upstairs; father cooks downstairs.','谁在楼下？',[('爸爸','Father'),('妈妈','Mother'),('妹妹','Younger sister'),('老师','Teacher')],'Father’s cooking is located downstairs; mother’s reading is upstairs.'),
L('我不喝牛奶，给我一杯茶吧。','I do not drink milk; give me a cup of tea, please.','我想喝什么？',[('茶','Tea'),('牛奶','Milk'),('奶','Milk, short form'),('水','Water')],'The request is for 茶, while milk is explicitly declined.'),
L('这本书是新的，那本不是新的。','This book is new; that book is not new.','哪本书是新的？',[('这本','This one'),('那本','That one'),('两本','Both books'),('三本','Three books')],'这本 is identified as new; the second book is explicitly not new.'),
L('我们在学校前边等你，不在后边。','We wait for you in front of the school, not behind it.','我们在哪里等？',[('学校前边','In front of school'),('学校后边','Behind school'),('学校里边','Inside school'),('学校上边','Above school')],'前边 is explicitly affirmed and 后边 denied.'),
L('今天我不买衣服，我买书。','Today I do not buy clothes; I buy books.','今天我买什么？',[('书','Books'),('衣服','Clothes'),('杯子','Cups'),('米饭','Rice')],'Books are the stated purchase; clothes are explicitly excluded.'),
O(['我','在家','看书。'],'I read at home.','谁在家看书？',['看书在我家。','我书在家看。','在我看家书。'],'Put the location 在家 before the action 看书 in ordinary subject–location–verb order.'),
O(['朋友','不想吃','包子。'],'My friend does not want steamed buns.','谁不想吃包子？',['包子不想吃朋友。','朋友包子不想吃。','不朋友想吃包子。'],'不 negates 想吃 before the object 包子; it does not negate the person.'),
O(['妈妈','在楼上','读书。'],'Mother reads upstairs.','谁在楼上读书？',['妈妈书在楼上读。','读书妈妈在楼上。','楼上读在妈妈书。'],'Keep 在楼上 as the location phrase and 读书 as the action after 妈妈.'),
O(['他','昨天','没上课。'],'He did not attend class yesterday.','谁昨天没上课？',['他昨天没课上。','没他昨天上课。','昨天上他没课。'],'The time precedes 没上课; 没 negates the past action.'),
O(['我们','一起','去学校。'],'We go to school together.','谁一起去学校？',['学校一起去我们。','我们去一起学校。','一起我们学校去。'],'一起 modifies the action 去学校 after the subject in the ordinary order requested.'),
O(['爸爸','做了','晚饭。'],'Father made dinner.','谁做了晚饭？',['晚饭做了爸爸。','爸爸晚了做饭。','爸爸了晚饭做。'],'爸爸 is the cook and 晚饭 the thing made; 了 follows 做.'),
]

items=[]
for group, rows in [('identity',identity),('numbers',numbers),('daily',daily)]:
    assert len(rows)==18
    # Mix reading/listening/ordering within each selection pool, not just the sample.
    mixed=[rows[i+6*j] for i in range(6) for j in range(3)]
    for i,q in enumerate(mixed):
        unit=group if i<12 else 'sample'
        q.update(id=f'hsk1-bank-{group}-{i+1:02}',unit=unit)
        shift=len(items)%4
        q['choices']=q['choices'][shift:]+q['choices'][:shift]
        items.append(q)
assert len(items)==54 and sum(q['unit']=='sample' for q in items)==18
pack=dict(kind='hsk-practice',version=2,id='hsk1-original-rotating',standard='GF2021 practice',level=1,
    provenance=dict(author='Kiyo original exercises',status='AI-assisted draft; native review pending; original mixed practice, not an official paper',
        sources=['https://www.chinesetest.cn/syllabus','https://hsk-sample-1409982902.cos.ap-beijing.myqcloud.com/HSK3.0.zip']),items=items)
destination = ROOT / ('.cache/course-authoring/hsk-1-bank.hsk.json' if '--draft' in sys.argv else 'content/packs/hsk-1-bank.hsk.json')
destination.parent.mkdir(parents=True, exist_ok=True)
destination.write_text(json.dumps(pack,ensure_ascii=False,indent=2)+'\n','utf-8')
print('Authored 54 new level-1 questions; the legacy 36 remain intact. Publication requires the pack and audio gates.')
