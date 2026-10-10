"""Late HSK 2: reading friends, a short visit, painting and shared old photos."""
import json,sys
from common import ROOT,py
from advanced_core import rows
from editorial_repair import repair,tf,reply,fill,match
from parity_repair_09_contexts import VOCAB
from common import dictionary

dictionary['画儿']='huàr'

TEXTS={
29:(
'''我姓王，叫王宁，叫我小王就行。|My surname is Wang and my name is Wang Ning. Just call me Xiao Wang.
我姓李，叫李安。我们昨天晚会见过吧？|I'm Li An, surname Li. Didn't we meet at the evening party yesterday?
对！你坐在老王旁边。|Yes! You were beside Lao Wang.
我还帮他拿了报纸，他今天又带来了。|I helped him carry the newspaper. He's brought it again today.
他在哪里？我想问问春节的活动。|Where is he? I'd like to ask about the Spring Festival event.
他在里面午睡，晚点儿再问吧。|He's having a nap inside. Let's ask him later.
好。你带书、笔什么的了吗？|Okay. Did you bring books, pens and things like that?
带了。有空的话，先和我读一段吧。|Yes. If you're free, read a passage with me first.
''',
'''昨天在晚会上，我认识了李安。他姓李，坐在大家都叫老王的那位朋友旁边，帮老王拿着一份晚报。|I met Li An at yesterday's evening party. His surname was Li. He sat beside the friend everyone calls Lao Wang and helped him carry an evening newspaper.
今天到读书小组，我又见到了李安。他看见我就笑了，说原来是你啊，昨天说话的人太多，今天可以慢慢聊。|I saw Li An again at the reading group today. He smiled: oh, it's you! There had been too many people talking yesterday; today we could chat properly.
老王正在里面午睡，我就先和李安看报纸。第二页写着春节的活动，李安说自己过年要回家，活动结束后就出发。|Lao Wang was napping inside, so Li An and I read the newspaper first. The second page described a Spring Festival event. Li An would go home for the New Year, leaving after that event.
我今年想留在这里，和朋友一起过年。我们看见活动要带一道菜，就开始说自己会做什么；李安说他只会煮面。|I wanted to stay here and celebrate with friends this year. The event asked everyone to bring a dish, so we talked about what we could cook. Li An said he only knew how to cook noodles.
老王醒了，走过来问我们读到哪里了。我指给他看那条活动消息，他说晚上大家可以一起来，不用现在就想好带什么。|When Lao Wang woke he asked how far we'd read. I showed him the event notice. We could all come that evening, he said; we didn't need to decide on a dish yet.
回家以后，我给李安发了书店的地址。晚上睡前，他说晚安，还问我下次能不能带一本喜欢的书来。|Back home I sent Li An the bookshop address. Before bed he said goodnight and asked me to bring a favourite book next time.
''',
'''你说你只会煮面，是真的吗？|Is it true you can only cook noodles?
还会烧水，泡茶。|I can boil water and make tea too.
那我们过年喝你的茶？|Then shall we have your tea at New Year?
行，不过菜还是你们做。|Sure, but you can cook the food.
老王说不用现在想好。|Lao Wang said we don't have to decide now.
那先喝茶吧，面明天再想。|Let's have tea now and think about noodles tomorrow.
'''),
30:(
'''喂，你好，我是小王。现在方便说话吗？|Hello, it's Xiao Wang. Is now a good time to talk?
方便。我已经出院，在家休息了。|Yes. I've left hospital and am resting at home.
有空的话，我今天来坐一会儿？|If you're free, may I visit briefly today?
好，四点半来吧。我五点想睡一会儿。|Sure, come at four thirty. I'd like a nap at five.
行。你想看哪本书？我带过来。|Okay. Which book would you like? I'll bring it.
就上次那本小说吧，我一直没看完。|That novel from last time. I still haven't finished it.
好，我找一下，不一会儿就能找到。|Sure. I'll look for it; it shouldn't take long.
慢慢找。我还在等你发书的照片呢。|Take your time. I'm still waiting for your photo of it.
''',
'''朋友已经出院，今天在家休息。我打电话问现在方不方便说话，她说可以，声音也比上次轻松了。|My friend had left hospital and was resting at home. I called to ask if it was a good time to talk. It was, and she sounded more relaxed than last time.
我们约好四点半见，五点我就走。她想睡一会儿，我也还有事，所以坐半小时正好。|We arranged to meet at four thirty and for me to leave at five. She wanted a nap, and I had other plans too, so half an hour suited us.
她想继续看上次的小说，我就在书架上找。不一会儿找到了，可是夹在里面的纸掉了出来，上面还有她写的两句话。|She wanted to carry on reading the novel from last time. I found it on the bookshelf shortly afterwards, but a sheet slipped out with two sentences she'd written.
我把书和纸一起拍给她看，她说就是这本，纸也别忘了带。我把它放回书里，再把书放进包里。|I sent her a photo of the book and paper. It was the right one, and she asked me to bring the paper too. I put it back inside the book and put the book in my bag.
四点半到她家时，太阳已经照到窗边。她坐在椅子上，我们聊了小说里的朋友，也说了下次去哪家书店。|At four thirty the sun was shining by her window. We sat and chatted about the friends in the novel and which bookshop to visit next time.
快五点时，我先告别。走到楼下，她还发来消息，说我带对了书，却忘了把自己的围巾带走。|Just before five I said goodbye. When I got downstairs she messaged: I'd brought the right book but forgotten to take my own scarf.
''',
'''你今天带了书，却把围巾留下了。|You brought the book but left your scarf.
我下次来拿，行吗？|Can I get it next time?
行，我先放门边。|Sure. I'll put it by the door.
别放太远，我下次可能又忘。|Don't put it too far away. I might forget again.
那我也给围巾拍张照片。|I'll take a photo of the scarf too, then.
好，看到照片我就想起来了。|Good. The photo will remind me.
'''),
31:(
'''这张画比上周那张好看多了。|This drawing looks much nicer than last week's.
我越画越喜欢，就是还画不出那只猫的样子。|The more I draw, the more I enjoy it. I still can't get that cat right, though.
先画桌子也行。你上周不是画完一张了？|You can draw the table first. Didn't you finish one last week?
画完了。以前想成为画家，现在先把桌子画好。|I did. I used to dream of becoming a painter. Now I'll get the table right first.
上次那个展览，你还想去吗？|Do you still want to go to that exhibition?
想。我早就想去，就是周末一直没空。|Yes. I've wanted to go for ages but haven't been free at weekends.
网站上写周四晚上也开门。|The website says it's open on Thursday evenings too.
那周四去吧。不但能看画，还能听画家说怎么画的。|Let's go Thursday, then. We can see the paintings and hear how the painter made them.
''',
'''上周我只画了一张桌子，这周想把桌子旁边的猫也画进去。可是猫一直走来走去，我刚画出头，它已经坐到另一边了。|Last week I drew only a table. This week I wanted to add the cat beside it, but the cat kept moving. By the time I'd drawn its head, it was on the other side.
陈宇来看我的画，说桌子越来越像了。我说自己以前想成为画家，现在连一只猫都画不完。他笑了，让我先等猫睡着。|Chen Yu said the table was looking more convincing. I'd once dreamed of becoming a painter, I said, yet couldn't finish one cat. He laughed and suggested waiting until it slept.
我想起网上看到的展览，早就想去，可周末一直没空。陈宇在网站上查了时间，发现周四晚上也开门。|I remembered an exhibition I'd seen online. I'd wanted to go for a while but had no free weekends. Chen Yu checked the website and found it open on Thursday evenings.
周四我们下班后一起去。展览里有画家的作品，也有她年轻时用过的本子，里面画了许多很小的桌子和椅子。|We went after work on Thursday. The exhibition showed the painter's works and notebooks she'd used when younger, full of tiny tables and chairs.
画家出来和大家说话，我问她是不是一开始就画得好。她拿出一张旧画，说这张桌子的一条腿比别的长，自己现在还留着。|When the painter spoke with us I asked whether she'd been good from the start. She showed an old drawing of a table with one leg longer than the others; she'd still kept it.
回家以后，我把没画完的猫放在桌上，今后还想继续画。陈宇给我发了张照片，这回猫睡着了，我终于不用追着它看。|Back home I put the unfinished cat drawing on the table and wanted to keep going. Chen Yu sent a photo of the cat asleep. I finally didn't have to chase it to look at it.
''',
'''你这张画里，猫怎么比桌子大？|Why is the cat bigger than the table in this drawing?
我想把它的眼睛画清楚一点。|I wanted to draw its eyes clearly.
那桌子呢？|What about the table?
桌子已经画过一次了，让猫大一点吧。|I've drawn the table already. Let the cat be bigger this time.
行，反正猫看起来很满意。|Okay. The cat looks pleased, anyway.
它满意的是桌上的鱼。|It's pleased with the fish on the table.
'''),
32:(
'''这是我们以前三个人的照片，你还记得吗？|This is a photo from when there were three of us. Remember?
记得。现在小组变成五个人了。|Yes. Now our group has grown to five.
照片里你穿的外套，我姐姐也有一件。|My sister has a coat like the one you're wearing in the photo.
你姐姐现在做什么？|What does your sister do now?
她是商人，在市中心开了一家茶叶店。|She's a businesswoman with a tea shop in the city centre.
那我们下次去看看？我正好想买点茶。|Shall we visit next time? I'd like to buy some tea.
好。今天星期三，周六下午去吧。|Sure. It's Wednesday today; let's go on Saturday afternoon.
行，三点在活动中心门口见，再一起坐车过去。|Okay. Meet at the activity centre entrance at three, then take the bus together.
''',
'''我找旧照片时，想起以前的小组只有三个人。现在有五位朋友一起读书，见面的地方也从小房间变成了活动中心。|Looking through old photos reminded me that our group once had only three people. Five of us now read together, and we'd moved from a small room to the activity centre.
陈宇看照片，认出了自己以前的外套。我说姐姐也有一件，他就问姐姐现在做什么。我告诉他，她在市中心开了茶叶店。|Chen Yu recognised his old coat in a photo. I said my sister had one like it, and he asked what she did now. She had a tea shop in the city centre.
姐姐过去在南方长大，现在搬到这里。我去她店里看过，里面有许多小杯子，客人可以先坐下喝一点茶。|My sister had grown up in the south and moved here. I'd visited her shop. It had lots of little cups, and customers could sit and taste some tea first.
我们周三约好，周六三点在活动中心门口见。我把店的地址发给另外三位朋友，问她们要不要一起去。|On Wednesday we arranged to meet at the activity centre entrance at three on Saturday. I sent the shop address to the other three friends and asked if they'd like to join us.
周六有一位朋友要上班，四个人一起去了。姐姐先拿来茶，陈宇选了一小袋，付款时才想起信用卡忘在家里。|One friend had work on Saturday, so four of us went. My sister brought tea. Chen Yu chose a small bag and only remembered when paying that his credit card was at home.
他用手机付了钱，我们又坐了一会儿。走以前，姐姐帮我们拍了照片；这次四个人站在一起，下次想五个人都来。|He paid by phone, and we stayed a while. My sister took a photo before we left. There were four of us this time; next time we hoped all five could come.
''',
'''这次照片里，你又站最边上。|You're at the edge of the photo again.
我刚买完茶，来晚一步。|I'd just finished buying tea and arrived a moment late.
下次你先站中间。|Stand in the middle first next time.
行，茶让你去买。|Sure. You can buy the tea.
我还没答应呢。|I haven't agreed to that yet.
那我们一起买，别分开了。|Then let's buy it together instead of splitting up.
''')}

QUESTIONS={
29:([
('gist','What do the two acquaintances do?',['Introduce themselves again and begin reading','Miss a flight','Cancel Spring Festival'],0),
('detail','Where is Lao Wang?',['Napping inside','Buying a bus ticket','At the station'],0),
('inference','Why ask him later?',['He is currently asleep','He dislikes all books','He is leaving forever'],0)], [
('gist','What comes from the second meeting?',['Reading, talking about New Year and planning another visit','A quarrel over the newspaper','An immediate trip home'],0),
('detail','What does Li An say he can cook?',['Noodles','Every dish in the shop','Nothing at all'],0),
('inference','Why mention a favourite book before bed?',['He wants to read together next time','He wants to return a lost library card','He is cancelling the group'],0)]),
30:([
('gist','What do the friends arrange?',['A short visit with a novel','A hospital appointment for tomorrow','A whole-day outing'],0),
('detail','When should Xiao Wang arrive?',['Four thirty','Five thirty','Four in the morning'],0),
('inference','Why leave at five?',['The friend wants a nap','The hospital closes then','The novel must be returned then'],0)], [
('gist','How does the visit go?',['The right novel arrives but a scarf is left behind','The visitor cannot find the home','The friend rejects the book'],0),
('detail','What is inside the book?',['A paper with two sentences','A new credit card','A teacup'],0),
('inference','Why send a photo of the book?',['To check it is the one the friend wants','To publish a medical report','To ask for the time of discharge'],0)]),
31:([
('gist','What plan do they make?',['Visit an exhibition on Thursday evening','Buy a cat that night','Give up drawing'],0),
('detail','Why has the visit been delayed?',['Weekends have been busy','The painter has moved abroad','There is no website'],0),
('inference','Why does Thursday help?',['The exhibition also opens that evening','Thursday is their only competition date','The cat can paint on Thursday'],0)], [
('gist','What encourages the narrator?',['Seeing the painter’s imperfect old work and a sleeping-cat photo','Winning a prize immediately','Buying a longer table leg'],0),
('detail','What is unusual about the old table drawing?',['One leg is longer than the others','It contains five cats','It has no table at all'],0),
('inference','Why is the last photo helpful?',['The cat is still enough to study','The table has disappeared','The exhibition will be held in the house'],0)]),
32:([
('gist','What plan follows looking at the photo?',['Visiting the sister’s tea shop','Moving into a new province','Entering a points competition'],0),
('detail','When do they meet on Saturday?',['Three at the activity centre entrance','Two at a hospital','Five at the bookshop'],0),
('inference','Why suggest the tea shop?',['Chen Yu wants to buy tea','His sister owns it','The old coat must be returned there'],0)], [
('gist','What happens on the trip?',['Four friends visit the shop and take a photo','All five stay at home','The shop refuses payment'],0),
('detail','Why do only four go?',['One friend has work','The shop has only four cups','Someone loses the address'],0),
('inference','Why does Chen Yu pay by phone?',['His credit card is at home','He forgot to buy tea','The narrator pays for every friend'],0)])}

REPLIES={
29:[('我姓王，你呢？','My surname is Wang. What about you?',['我姓李，叫李安。','报纸在第二页。','老王今天睡了。']),('老王午睡呢，我们先做什么？','What shall we do while Lao Wang is napping?',['先读一段吧，晚点儿再问他。','马上叫醒所有人。','春节已经过完了。'])],
30:[('四点半来，五点我想睡一会儿，行吗？','Can you come at four thirty if I’d like a nap at five?',['行，我坐半小时就走。','好，我五点半才来。','那我一直坐到晚上。']),('带上次那本小说，别忘了里面的纸。','Bring the last novel, including the paper inside.',['好，书和纸一起带。','我只把纸留在家。','四点半已经过去一年了。'])],
31:[('周末没空，展览周四晚上也开门，去吗？','Shall we go Thursday evening if weekends are busy and it opens then too?',['去，周四下班后见吧。','不，它只在周末开门。','先把猫卖给画家。']),('猫一直动，我怎么画？','How can I draw the cat when it keeps moving?',['等它睡着，再慢慢看。','桌子必须比猫小。','我们已经看完小说。'])],
32:[('周六三点在哪里见？','Where do we meet at three on Saturday?',['活动中心门口吧。','星期三在省里。','信用卡在口袋里。']),('我想买点茶，你姐姐的店在哪里？','Where is your sister’s shop? I’d like some tea.',['在市中心，我们一起去。','我们有五张旧照片。','你这件外套很暖和。'])]}

GLOSSES=[('科学家','scientist'),('作家','writer'),('同事','colleague'),('王宁','Wang Ning, a name'),('李安','Li An, a name'),('转身','turn around'),('回头','turn one’s head'),('宁','used here in a given name'),('杂志','magazine'),('煮','cook by boiling'),('醒','wake up'),('烧水','boil water'),('泡茶','make tea'),('院长','head of an institution; hospital director or dean'),('重视','value; attach importance to'),('柜子','cupboard'),('汗','sweat'),('香味','pleasant smell'),('夹','place between; hold between'),('掉','drop; fall'),('小说','novel'),('轻松','relaxed; easy'),('告别','say goodbye'),('深','deep; late in the night'),('指出','point out'),('变化','change'),('窄','narrow'),('信心','confidence'),('展览','exhibition'),('画家','painter'),('出版','publish'),('贴','stick onto'),('墙','wall'),('街道','street'),('作品','a work or creation'),('发展','development'),('反正','anyway'),('追','chase'),('腿','leg'),('冰','ice'),('结论','conclusion'),('门口','entrance'),('茶叶','tea leaves'),('付款','pay'),('付钱','pay'),('区','district'),('出席','attend'),('开幕','opening of an event'),('生意','business; trade'),('围巾','scarf'),('香','fragrant'),('热闹','lively'),('一生','a lifetime'),('纸','paper'),('拍','photograph'),('猫','cat'),('认出','recognise'),('抬头','look up'),('睡着','fall asleep'),('过去','the past'),('结束','finish'),('活动中心','activity centre'),('中心','centre'),('笔','pen'),('地点','location')]

GLOSSES += [('饮料','drink; beverage'),('父亲','father'),('书架','bookshelf'),('历史','history'),('盒子','small box'),('窗户','window'),('圆','round'),('连','even'),('表演','performance'),('家乡','hometown'),('兴趣','interest'),('袋','bag; pouch'),('靠窗','by the window'),('突然','suddenly'),('除了','except; besides'),('谈','talk')]

for number,(d,r,m) in TEXTS.items():
    pack=json.loads((ROOT/f'content/packs/s2-u{number:02}.json').read_text('utf-8'))
    examples={};contexts=[]
    for raw in VOCAB[number].splitlines():
        word,z,e,z2,e2=raw.split('|');assert word in z and word in z2 and z!=z2
        examples[word]=(z,e);contexts.extend([(z,e),(z2,e2)])
    assert set(examples)=={v['hanzi'] for v in pack['vocabulary']}
    dqs,rqs=QUESTIONS[number]
    index={29:5,30:3,31:6,32:7}[number]
    yes={29:'Lao Wang is napping inside.',30:'The visit begins at four thirty.',31:'The exhibition also opens on Thursday evening.',32:'They meet at three at the activity centre entrance.'}[number]
    no={29:'Li An asks the narrator never to bring a book.',30:'The visitor remembered to take the scarf.',31:'The cat in Chen Yu’s photo keeps moving.',32:'All five friends appear in the new photo.'}[number]
    tasks=[tf(*rows(d)[index],yes,True,'This detail is stated in the heard line.'),tf(*rows(r)[-1],no,False,'The heard line explicitly states a different result.'),
        *[reply(z,e,c,0,'This reply responds directly to the immediate question.') for z,e,c in REPLIES[number]]]
    for word in {29:['姓名','春节'],30:['月份','空气'],31:['成为','广告'],32:['结果','信用卡']}[number]:tasks.append(fill(*examples[word],word))
    example_rows=list(examples.values());tasks.extend(match(example_rows[i:i+3]) for i in [0,3,6])
    inherited=[(g['hanzi'],g['meaning']) for t in [pack['dialogue'],pack['reading'],*pack['extraReadings']] for g in t.get('glosses',[])]
    repair(number,dict(dialogue=(rows(d),dqs),reading=(rows(r),rqs),media=(rows(m),[]),examples=examples,contexts=contexts,tasks=tasks,
        dialogueSpeakers={29:['王宁','李安'],30:['王宁','林安'],31:['陈宇','林安']}.get(number,['林安','陈宇']),
        mediaSpeakers={29:['王宁','李安'],30:['林安','王宁']}.get(number,['陈宇','林安']),
        glosses=list(dict.fromkeys(inherited+GLOSSES)),
        usage=[('Ask about a concrete detail',REPLIES[number][0][0],REPLIES[number][0][1],'Tie the next action to what the other person has just said.')],
        turns=[(z,e,'Answer the immediate practical question',[c[0]]) for z,e,c in REPLIES[number]],
        review='Late HSK 2 correction: acquaintances reading a newspaper and planning New Year; a half-hour visit with the right novel and a forgotten scarf; painting an uncooperative cat and visiting an exhibition; old group photos and a sister’s tea shop. Removed app-policy/identity/medical-disclaimer leakage from ordinary speech and replaced metalinguistic word examples with independent situations. All target records get two authored contexts. Preserved old unit/word/task IDs. Native flags: suffix 家, 老/小 address forms, 等 list suffix, aspiration 成为/实现, result 成, scope of 以上/以下, 得 dé and 长 zhǎng, concrete medicine nouns 药片/药水 and subject 科. 画儿 remains subject to the explicit unresolved-audio policy, never native-reviewed. Check exact question facts, inclusive age bounds and the teasing tone.'),publish='--publish' in sys.argv,level=2)

# Removing an incidental introduction cannot leave later uses unexplained.
DEPENDENCIES={
    's2-u34':[('乱','messy; in disorder')],
    's3-u05':[('判','judge; decide')],
    's3-u13':[('未','not yet; has not')],
    's3-u17':[('判','judge; decide'),('按','according to; follow')],
    's3-u18':[('景','scene; view'),('混','mix; muddle together')],
    's3-u19':[('并','and; also; with negation: actually'),('修','repair; revise'),('未','not yet; has not')],
}
for uid,terms in DEPENDENCIES.items():
    path=ROOT/f'content/packs/{uid}.json'
    source=path if path.exists() else ROOT/f'output/advanced-course-drafts/{uid}.json'
    pack=json.loads(source.read_text('utf-8'))
    for text in [pack['dialogue'],pack['reading'],*pack['extraReadings']]:
        for word,meaning in terms:
            if any(word in l['zh'] for l in text['lines']) and not any(g['hanzi']==word for g in text.get('glosses',[])):
                text.setdefault('glosses',[]).append(dict(hanzi=word,pinyin=py(word),meaning=meaning))
    destination=ROOT/('content/packs' if '--publish' in sys.argv else 'output/parity-editorial-drafts')/path.name
    destination.write_text(json.dumps(pack,ensure_ascii=False,indent=2)+'\n','utf-8')

# A photocopy needs a physical original; sending a file would imply printing.
# Apply this narrow follow-through only after the preceding batch has finished.
uid='s3-u04'
path=ROOT/f'content/packs/{uid}.json'
pack=json.loads(path.read_text('utf-8'))
def hand_over_paper(value):
    if isinstance(value,str):
        return value.replace('能，发给我吧。','能，拿给我吧。').replace('能，把这一页发给我吧','能，把这一页拿给我吧').replace('陈宇把自己的一页发给我','陈宇把自己的一页交给我').replace('Yes. Send it over.','Yes. Hand it to me.').replace('Chen Yu sent me a page','Chen Yu handed me a page')
    if isinstance(value,list):
        return [hand_over_paper(child) for child in value]
    if isinstance(value,dict):
        result={key:hand_over_paper(child) for key,child in value.items()}
        if 'zh' in result and result['zh']!=value['zh'] and 'py' in result:
            result['py']=py(result['zh'].replace('【','').replace('】',''))
        return result
    return value
pack=hand_over_paper(pack)
note='2026-10-09 photocopy follow-through: the original page is handed over physically with 拿给/交给, rather than sent as a digital file. Dialogue, reading, task answer and conversation acceptance remain aligned; saved IDs are preserved. Fresh audio and all gates required. Native review pending.'
pack['notes']='\n'.join(dict.fromkeys([*pack.get('notes','').splitlines(),note]))
destination=ROOT/('content/packs' if '--publish' in sys.argv else 'output/parity-editorial-drafts')/path.name
destination.write_text(json.dumps(pack,ensure_ascii=False,indent=2)+'\n','utf-8')
print(uid,'physical-paper follow-through published' if '--publish' in sys.argv else 'physical-paper follow-through drafted',flush=True)
