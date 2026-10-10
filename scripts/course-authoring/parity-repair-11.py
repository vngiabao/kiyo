"""Editorial HSK 3 scenes: tickets, an old street, a walk, a rehearsal."""
import json,sys
from common import ROOT,py,dictionary
from advanced_core import rows
from editorial_repair import repair,tf,reply,fill,match
from parity_repair_11_contexts import VOCAB
dictionary['弹钢琴']='tán gāng qín'

TEXTS={
9:(
'''周六的演出，你想去吗？|Do you want to go to Saturday's performance?
想，票价是多少？|Yes. How much are tickets?
网上写二十元，至少提前一天订。|The website says twenty yuan. Book at least a day ahead.
那今天订吧，还有位子吗？|Let's book today. Are there still seats?
目前只剩两个，我们正好两个人。|There are only two left at present. Just right for us.
活动在哪儿？|Where's the event?
在学校旁边的公共活动室，不在上次那个地方。|It's in the shared activity room by the school, not where we went last time.
我差点走错。几点开始？|I almost went to the wrong place. When does it start?
七点。票上写仅限当天使用。|Seven. The ticket says it's valid only that day.
好，我先把地址存下来。|Okay. I'll save the address.
订好了。要是取消，明天下午以前告诉他们。|Booked. If we cancel, tell them by tomorrow afternoon.
不会吧，我连周六穿什么都想好了。|Surely not. I've already planned what to wear on Saturday.
''',
'''周四，陈宇问我要不要去看周六的演出。我想去，打开订票页面一看，只剩两个位子。我们一人一张，正好订完。|On Thursday Chen Yu asked if I'd like to see Saturday's performance. The booking page showed just two seats. We booked one each and took the last two.
票价是二十元，时间是晚上七点。地址在学校旁边的公共活动室，我把它存进手机，免得走到上次的地方。|Tickets were twenty yuan and the show started at seven. I saved the address of the shared activity room by the school so I wouldn't go to the previous venue.
周六六点半，我们在学校门口见面。陈宇穿了一件新衬衫，我问他是不是专门买的。他说不是，只是终于想起来穿。|We met at the school entrance at six thirty on Saturday. Chen Yu had a new shirt. Had he bought it for this? No, he said; he'd finally remembered to wear it.
走到活动室，门口的人看了票，让我们进去。前面两排已经坐满，我们的位子在第三排，离舞台也不远。|At the activity room someone checked our tickets and let us in. The first two rows were full. Our seats were in the third row, still near the stage.
演出开始以后，陈宇把手机放进包里。我也收起来，坐着听了一个多小时。最后一首歌，我们都听过，就轻轻跟着唱。|When the show began Chen Yu put his phone away. I did too, and we listened for over an hour. We both knew the last song and quietly sang along.
结束时我问他，下次还来吗。他说来，不过至少早一点订，省得每次都只剩两个位子。|Afterwards I asked if he'd come again. Yes, he said, but let's at least book earlier, rather than always finding just two seats left.
''',
'''衬衫新买的？|Is that a new shirt?
买了一个月，今天才穿。|I bought it a month ago and only wore it today.
你是在等一张二十元的票？|Were you waiting for a twenty-yuan ticket?
是在等你别再说我总穿同一件。|I was waiting for you to stop saying I always wear the same one.
好，今天不说。|Okay. I won't say it today.
明天也尽量别说。|Try not to tomorrow either.
'''),
10:(
'''你还记得从前那家书店吗？|Do you remember that old bookshop?
记得，我们放学以后常去。|Yes. We used to go after school.
今天想不想去看看？|Shall we have a look today?
想。不过它年初就搬走了。|Yes. But it moved at the beginning of the year.
啊，我还准备往老地方走。|Oh, I was about to go to the old place.
新地址在地铁站旁边，我发给你。|The new address is by the metro station. I'll send it.
收到了。那我立刻出门。|Got it. I'll leave right away.
别急，我还在找钥匙。|Don't rush. I'm still looking for my keys.
你每次放钥匙的地方都不一样。|You put your keys somewhere different every time.
找到了，在昨天那件外套里。|Found them, in yesterday's coat.
那三点在书店门口见？|At the bookshop entrance at three, then?
好。今天先看书，别又只聊一个下午。|Yes. Let's actually look at books today instead of just chatting all afternoon again.
''',
'''我曾经住在学校旁边，放学后常去街角的书店。后来搬家了，几年没回去，那家店的地址却一直留在手机里。|I once lived by the school and often visited the bookshop on the corner after class. I moved away and hadn't returned for years, but kept its address on my phone.
今天我和陈宇约好去看看。我本来想去老地方，他告诉我，书店年初已经搬到地铁站旁边。我赶紧改了地址。|Today Chen Yu and I arranged a visit. I'd planned to go to the old place, but he told me the shop had moved by the metro at the beginning of the year. I quickly changed the address.
三点，我们在新店门口见面。门口的字还是从前那几个，里面却大多了，窗边多了两张桌子，可以坐着读书。|We met outside the new shop at three. The sign still had the same words, but inside it was much bigger, with two new tables by the window for reading.
老板认出了陈宇，问他最近忙不忙。陈宇说，忙，不过经过这里就会进来。我站在旁边，突然觉得几年过去了，好像也没那么久。|The owner recognised Chen Yu and asked if he'd been busy. Yes, he said, but he always dropped in when passing. Standing beside him, I suddenly felt those years hadn't been so long.
我在书架上找到以前读过的一本小说。陈宇说封面早已换了，我打开一看，第一句话还是一样，连当初画的那条线都想起来了。|I found a novel I'd read before. Chen Yu said the cover had changed long ago. Inside, the first sentence was the same, and I even remembered the line I'd underlined.
回家时我们各买了一本书。陈宇说，这次总算不是光聊天。我说，聊也聊了，书也买了，下次还能继续。|We each bought a book before leaving. Chen Yu said we'd finally done more than chat. We'd chatted and bought books, I said; next time we could do both again.
''',
'''那本小说你以前看过。|You've read that novel before.
我知道，可是旧的找不到了。|I know, but I can't find my old copy.
说不定在你昨天的外套里。|Maybe it's in yesterday's coat.
外套能放钥匙，放不下一本书。|A coat holds keys, not a whole book.
那你下次买件大的。|Buy a bigger coat next time, then.
我还是整理书架吧。|I think I'll organise the bookshelf instead.
'''),
11:(
'''吃完饭出去散步吗？|Shall we walk after dinner?
想去，不过我有点困。|I'd like to, but I'm a little sleepy.
你今天整天都坐在电脑前吧？|You've sat at the computer all day, haven't you?
是啊，连续开了三个会。|Yes. Three meetings in a row.
那出去走二十分钟，换换空气。|Let's walk for twenty minutes and get some fresh air.
去哪儿？公园有点远。|Where? The park's a little far.
去河边，不到十分钟就到了。|The river. It takes less than ten minutes to get there.
外面冷不冷？|Is it cold outside?
今天挺暖和，带件薄外套就行。|It's quite warm today. Just bring a light jacket.
行。我拿钥匙，你等我一下。|Okay. I'll fetch my keys. Wait a moment.
我在门口等，今天不跑步。|I'll wait by the door. No jogging today.
太好了，跑的话，你得把我拉回来。|Great. If we ran, you'd have to drag me home.
''',
'''今天我连续开了三个会，午饭也是坐在电脑前吃的。晚上吃完饭，林安问我要不要去散步，我觉得困，差点说不去。|I had three meetings in a row today and ate lunch at the computer too. After dinner Lin An suggested a walk. I was sleepy and nearly said no.
她说不用跑，出去走二十分钟就回来。我拿了一件薄外套，跟她去河边。路上还有人推着自行车，慢慢往家走。|She said we wouldn't run; just twenty minutes out and back. I took a light jacket and followed her to the river. Other people were wheeling bicycles slowly home.
我们走到桥边停了一会儿。水面上有灯的光，风也不冷。我终于不想一直看手机了，就把它放进了口袋。|We stopped by the bridge. Lights shone on the water and the breeze wasn't cold. I finally stopped wanting to stare at my phone and put it in my pocket.
林安说她通常晚饭后出来走走，往往在这里碰见邻居。话刚说完，就有人叫她的名字，还问旁边的我是不是新来的朋友。|Lin An said she usually walked after dinner and often met neighbours here. Just then someone called her name and asked if I was a new friend.
我们聊了几句，就往回走。到家一看，出门整整二十分钟。林安问我还困不困，我说不困了，不过想喝点水。|We chatted briefly and headed back. We'd been out for exactly twenty minutes. Lin An asked if I was still sleepy. No, but I'd like some water.
她把水倒好，问明天还去吗。我说去，钥匙已经放在门边了。这次不用再找半天。|She poured water and asked if I'd go again tomorrow. Yes, I said; my keys were already by the door. No long search this time.
''',
'''现在还想睡吗？|Do you still want to sleep?
不想了，我想喝水。|No. I want water.
刚才是谁说走不动的？|Who said they couldn't manage a walk earlier?
是坐在电脑前的我。|Me at the computer.
现在呢？|And now?
现在的我已经坐回椅子上了。|Me now is back in my chair already.
'''),
12:(
'''明天上台那一段，你练得怎么样？|How's practice going for tomorrow's part onstage?
前面还行，最后两句总忘。|The beginning's fine. I keep forgetting the last two lines.
我们先慢慢说，不放音乐。|Let's say them slowly first, without music.
好，你帮我听听。|Okay. Listen for me.
这一遍你说全了。再配上音乐试试？|You got every line that time. Shall we try it with music?
等一下，先把最后一句再说两遍。|Wait. Let me say the last line twice more first.
行，不急。明天我站你旁边。|Sure. No rush. I'll stand beside you tomorrow.
你也上台？我以为只有我。|You'll be onstage too? I thought it was just me.
两个人一起，你唱第一句，我接第二句。|Together. You sing the first line; I'll take the second.
那我有把握多了。现在放音乐吧。|That makes me much more confident. Put the music on now.
好，准备。|Okay. Ready?
等一下，我刚把水拿起来。|Hang on, I've just picked up my water.
''',
'''明天社区有一场小演出，我和陈宇一起唱一首歌。今天他来帮我练习，我反复唱到最后两句，却每次都忘了一句。|Chen Yu and I are singing at a small community show tomorrow. Today he came to practise with me. I kept reaching the last two lines and forgetting one.
他关掉音乐，让我先慢慢说。我看着纸读了两遍，再把纸放下。这一次说全了，心里也没有刚才那么急。|He turned off the music and asked me to say it slowly. I read from the paper twice and put it down. This time I said every line and felt less rushed.
陈宇想放音乐，我说再练两遍。他就坐在旁边，等我把最后一句说清楚。说完我才发现，刚才一直把两个词的顺序弄反了。|Chen Yu wanted to put on the music, but I asked for two more tries. He waited beside me as I said the last line clearly. I realised I'd been reversing two words.
我们商量好明天一起上台。我唱第一句，他接第二句。音乐响起来，他向我点头，我这次就跟上了。|We agreed how we'd sing together onstage. I'd sing the first line and he'd take the second. When the music began he nodded to me, and this time I kept up.
练完以后，我说想先喝点水。他刚答应，就又放起音乐。我举着杯子看他，他也笑了，赶紧停下来。|After practice I asked for some water. He agreed, then started the music again. I looked at him over my cup; he laughed and quickly stopped it.
晚上我把要穿的衣服放好，又给陈宇发消息，说明天门口见。他回了一句，记得带水。我说水会带，最后两句也会带。|That evening I laid out my clothes and messaged Chen Yu about meeting at the entrance tomorrow. He reminded me to bring water. I'd bring water, I said, and the final two lines too.
''',
'''水会带，最后两句也会带。|I'll bring water and the final two lines too.
两句放在哪个包里？|Which bag are the lines in?
脑子里，不用包。|In my head. No bag needed.
那明天别忘了带脑子。|Don't forget your head tomorrow, then.
放心，这个我亲自带。|Don't worry. I'll bring it myself.
好，我负责带音乐。|Okay. I'll bring the music.
''')}

QUESTIONS={
9:([
('gist','What do the friends arrange?',['Two tickets for Saturday’s performance','A picnic on Sunday','A meeting with the school head'],0),
('detail','When does the performance begin?',['Seven','Six thirty','Eight thirty'],0),
('inference','Why do they book today?',['Only two seats remain','The event has already finished','The venue is closed permanently'],0)],[
('gist','What happens on Saturday?',['The friends enjoy a show together','The friends cancel their tickets','The friends sell shirts'],0),
('detail','Where are their seats?',['In the third row','In the first row','Outside the school'],0),
('inference','Why suggest earlier booking next time?',['To avoid leaving it until almost no seats remain','To make the show shorter','To get a different school uniform'],0)]),
10:([
('gist','What do they plan to visit?',['A bookshop that has moved','A cinema that has closed','An empty classroom'],0),
('detail','Where is the shop now?',['By the metro station','At its old corner','Inside the school'],0),
('inference','Why send a new address?',['The other friend was about to go to the old place','The keys belong to the shopkeeper','The shop has no books'],0)],[
('gist','What is the visit like?',['A familiar shop in a new place brings back memories','They cannot find the new shop','They visit without buying anything'],0),
('detail','When do they meet?',['Three','Noon','Six'],0),
('inference','What does the familiar first sentence bring back?',['A memory of underlining the old book','A request to move home','A new train timetable'],0)]),
11:([
('gist','What do they agree to do?',['Take a short walk by the river','Run to a distant park','Have another video meeting'],0),
('detail','How long is the proposed outing?',['Twenty minutes','Two hours','Five minutes'],0),
('inference','Why is the short walk appealing?',['It offers a change after sitting all day without requiring a run','It is a compulsory race','They must look for a lost bicycle'],0)],[
('gist','What happens after dinner?',['A sleepy friend enjoys a short walk and plans another','The friends sleep through a meeting','The friends run for an hour'],0),
('detail','Where do they pause during the walk?',['By the bridge','Inside the park café','At the school entrance'],0),
('inference','Why put the keys by the door?',['To be ready for the next walk','To give them to a stranger','To stop drinking water'],0)]),
12:([
('gist','How do they practise?',['Say the difficult lines slowly, then add music','Ignore the forgotten lines','Buy a larger stage'],0),
('detail','Who sings the second line?',['Chen Yu','The audience','The narrator alone'],0),
('inference','Why does the learner feel more confident?',['The friend will perform beside them','The performance has been cancelled','There are no lyrics'],0)],[
('gist','What improves during practice?',['The narrator gets the lines right and agrees how to sing with a friend','The narrator stops singing permanently','The paper is replaced by tickets'],0),
('detail','What mistake does the narrator notice?',['Two words were in the wrong order','The song was written on a shirt','The event was the previous week'],0),
('inference','Why stop the music again?',['The narrator is taking a drink','They have lost the venue address','The audience has left'],0)])}

REPLIES={
9:[('还有两个位子，今天订吗？','There are two seats left. Shall we book today?',['订吧，我们一人一张。','好，我已经看完演出了。','这把钥匙是我的。']),('明天下午以前能取消吗？','Can we cancel by tomorrow afternoon?',['能，票上有联系方式。','不能，第三排有两个座位。','我昨天买了衬衫。'])],
10:[('书店搬到地铁站旁边了。','The bookshop has moved beside the metro.',['把新地址发给我吧。','那我还去老地方等。','演出是七点开始。']),('三点在门口见，好吗？','At the entrance at three, okay?',['好，我带上想买的书单。','好，那我五点才到。','这张票二十元。'])],
11:[('不跑步，走二十分钟就回来。','No running. Just twenty minutes out and back.',['行，我拿件外套。','好，我们跑两个小时。','票只能今天用。']),('明天还去散步吗？','Shall we walk again tomorrow?',['去，我把钥匙放在门边。','书店已经搬走了。','那句话我说反了。'])],
12:[('我们先慢慢说，不放音乐。','Let’s say it slowly without music first.',['好，我先读最后两句。','那我把音乐开大一点。','新地址我收到了。']),('你唱第一句，我接第二句。','You sing the first line; I’ll take the second.',['好，你站我旁边吧。','好，两句都不唱。','明天车票涨价了。'])]}

GLOSSES=[('林安','Lin An, a name'),('陈宇','Chen Yu, a name'),('小周','Xiao Zhou, a name'),('优惠券','voucher'),('淋湿','get wet in the rain'),('平分','split equally'),('电池','battery'),('通道','passageway'),('畅通','unobstructed'),('订位','reserve a seat'),('野餐','picnic'),('衬衫','shirt'),('舞台','stage'),('前排','front row'),('省得','so as to avoid'),('一排','a row'),('排','row; arrange'),('活动室','activity room'),('放学','finish school for the day'),('街角','street corner'),('书架','bookshelf'),('封面','cover of a book'),('年代','era'),('阅览室','reading room'),('外套','coat'),('门铃','doorbell'),('订单','order'),('回复','reply'),('钥匙','key'),('画线','underline'),('地铁站','metro station'),('窗边','beside the window'),('窗户','window'),('书单','book list'),('邻居','neighbour'),('河边','riverside'),('口袋','pocket'),('薄','thin; light'),('薄外套','light jacket'),('推','push'),('放弃','give up'),('一集','one episode'),('集','episode'),('毕业','graduate'),('国外','abroad'),('山顶','summit'),('营养','nutrition'),('牛奶','milk'),('课程','course'),('日常','everyday'),('社区','community'),('脑子','brain; head'),('点头','nod'),('举','raise'),('音乐','music'),('球队','sports team'),('措施','measure; action'),('漏水','water leak'),('厨房','kitchen'),('改造','remodel; transform'),('训练','train; training'),('进展','progress'),('压力','pressure'),('鼓励','encourage'),('成果','results'),('成就感','sense of accomplishment'),('老板','boss; proprietor'),('用','use'),('接','take the next turn; receive'),('弄反','reverse by mistake'),('吹','blow'),('边','side'),('望','look into the distance')]

GLOSSES += [('订','book; reserve'),('仅限','restricted to; valid only for'),('限','limit'),('专门','specially; specifically'),('尽量','as far as possible'),('迟到','arrive late'),('儿童','children'),('弹钢琴','play the piano'),('桥','bridge'),('购物','shopping'),('着急','be anxious; in a hurry'),('紧张','nervous'),('盏','classifier for lamps'),('肯','be willing')]

for number,(d,r,m) in TEXTS.items():
    pack=json.loads((ROOT/f'content/packs/s3-u{number:02}.json').read_text('utf-8'))
    examples={};contexts=[]
    for raw in VOCAB[number].splitlines():
        word,z,e,z2,e2=raw.split('|');assert word in z and word in z2 and z!=z2
        examples[word]=(z,e);contexts.extend([(z,e),(z2,e2)])
    assert set(examples)=={v['hanzi'] for v in pack['vocabulary']}
    dqs,rqs=QUESTIONS[number]
    # Listening assertions are each supported or contradicted by their own clip.
    true_index={9:8,10:5,11:4,12:8}[number]
    true_statement={9:'The show starts at seven.',10:'The new address is by the metro.',11:'The outing is twenty minutes.',12:'The friend takes the second line.'}[number]
    false_statement={9:'The friends plan never to attend another show.',10:'The friends leave without buying any books.',11:'The narrator refuses to go out tomorrow.',12:'Chen Yu asks the narrator to leave the water at home.'}[number]
    tasks=[tf(*rows(d)[true_index],true_statement,True,'This fact is explicitly stated in the heard line.'),tf(*rows(r)[-1],false_statement,False,'The heard line explicitly describes a different action.'),
        *[reply(z,e,c,0,'This reply responds directly to the question or proposal.') for z,e,c in REPLIES[number]]]
    for word in {9:['票价','取消'],10:['本来','印象'],11:['散步','连续'],12:['继续','把握']}[number]:tasks.append(fill(*examples[word],word))
    example_rows=list(examples.values());tasks.extend(match(example_rows[i:i+3]) for i in [0,3,6])
    inherited=[(g['hanzi'],g['meaning']) for t in [pack['dialogue'],pack['reading'],*pack['extraReadings']] for g in t.get('glosses',[])]
    repair(number,dict(title={9:('Only a few places left','只剩两个位子'),10:('An old bookshop’s new address','老书店的新地址'),11:('The habits we keep','每天走一走'),12:('Let’s give it another go','再练一遍吧')}[number],dialogue=(rows(d),dqs),reading=(rows(r),rqs),media=(rows(m),[]),examples=examples,contexts=contexts,tasks=tasks,
        dialogueSpeakers={11:['林安','陈宇'],12:['陈宇','林安']}.get(number,['林安','陈宇']),
        mediaSpeakers={9:['林安','陈宇'],10:['陈宇','林安'],11:['林安','陈宇'],12:['林安','陈宇']}[number],
        glosses=list(dict.fromkeys(inherited+GLOSSES)),
        usage=[('Respond to the next concrete detail',REPLIES[number][0][0],REPLIES[number][0][1],'Tie your answer to the proposed action.')],
        turns=[(z,e,'Answer the immediate question or proposal',[c[0]]) for z,e,c in REPLIES[number]],
        review='Naturalness correction: last two tickets for a Saturday show, returning to a relocated bookshop, a twenty-minute riverside walk after three meetings, and shared rehearsal with water-break teasing. Removed assessment-rule monologues and inflated coverage recycling from dialogue and readings. All 88 word records retain IDs and receive two independent contexts. Self-review: Saturday show at seven, third row and twenty-yuan tickets; bookshop moved at beginning of year, meet at three; walk twenty minutes, no running; Lin An sings first and Chen Yu second, no solo performance. False statements contradict their own heard clip. Existing grammar ownership and assessment IDs retained. Native flags: written register 仅/已/变为/至今, 空 kōng versus kòng, informal 有的是, habitual 往往 versus 总是, 采取/采用, 成果/成就, and teasing about bringing one’s head. Native review pending.'),publish='--publish' in sys.argv)

DEPENDENCIES={
    's3-u40':[('聚','gather; get together'),('败','lose; fail')],
    's5-u07':[('额','amount; quota')],
    's6-u01':[('抢','rush to do; compete for')],
    's6-u04':[('诺','promise')],
    's6-u05':[('稿','draft; manuscript'),('绪','mood; thread')],
    's6-u06':[('凡','every; ordinary'),('若','if; as if'),('诺','promise'),('逼','press; force')],
    's6-u07':[('稿','draft; manuscript'),('若','if; as if'),('遗憾','regret; regrettable')],
    's6-u08':[('若','if; as if'),('诺','promise')],
    's6-u09':[('若','if; as if')],
    's6-u12':[('若','if; as if')],
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

