"""Explicit HSK 3 scenes with useful uncertainty and grounded directions."""
import json,sys
from common import ROOT,py,dictionary
from advanced_core import rows
from editorial_repair import repair,tf,reply,fill,match
from parity_repair_12_contexts import VOCAB
dictionary.update({'背着':'bēi zhe','背我':'bēi wǒ','朝南':'cháo nán'})

TEXTS={
13:(
'''周六去河边的事，还去吗？|Are we still going to the river on Saturday?
想去。不过天气预报说下午有雨。|I'd like to, but the forecast says rain in the afternoon.
那我们早上去？大概九点出门。|Shall we go in the morning? Leave around nine.
恐怕不行，我上午要上课。|I'm afraid I can't. I have class in the morning.
那下午在我家见吧，要是没下雨，再出去。|Come to mine in the afternoon, then. If it doesn't rain, we can go out.
好，几点到？|Okay. What time should I arrive?
两点左右。你不用带吃的，我来做。|Around two. No need to bring food; I'll cook.
我带点茶吧，家里还有一盒。|I'll bring some tea. I have a box at home.
行。路上大约要多久？|Sure. How long does the journey take?
二十分钟左右，下课以后我先回家拿茶。|About twenty minutes. I'll go home for the tea after class.
那我两点以前把饭做好。|I'll have lunch ready before two.
好。希望下午有太阳，吃完还想出去走走。|Great. I hope it's sunny in the afternoon. I'd still like a walk after eating.
''',
'''我和陈宇本来想周六去河边，天气预报却说下午有雨。我提议早上去，他上午要上课，不能早点出门。|Chen Yu and I had planned a riverside trip on Saturday, but the forecast said afternoon rain. I suggested the morning; he had class and couldn't leave early.
我们就改成下午在我家见。他两点左右到，带一盒茶，我来做饭。要是没下雨，吃完还可以去河边。|We switched to meeting at my home in the afternoon. He'd come around two with tea, and I'd cook. If it didn't rain, we could still walk to the river afterwards.
周六一点半，陈宇发消息，说已经回家拿了茶，预计二十分钟以后到。我把汤放在小火上，等他过来。|At one thirty on Saturday Chen Yu messaged that he'd fetched the tea and expected to arrive twenty minutes later. I left the soup over low heat and waited.
他进门时，外面刚下起雨。我们先吃饭，聊他今天的课。他说预习时没看懂的一段，老师用一张图讲清楚了。|It began raining just as he came in. Over lunch we talked about his class. He said the teacher used a diagram to explain a passage he hadn't understood while preparing.
三点多，雨停了，窗外亮起来。陈宇拿起外套，问我现在还想不想走。我说当然想，碗先放着，回来再洗。|After three the rain stopped and it brightened outside. Chen Yu picked up his coat and asked if I still wanted a walk. Of course; we'd leave the dishes and wash them when we returned.
走到河边，我们发现路上还有不少水。我庆幸今天穿了旧鞋，陈宇却一直低头看他的白鞋，说下次一定穿黑的。|The riverside path still had puddles. I was glad I'd worn old shoes. Chen Yu kept looking down at his white shoes, saying he'd definitely wear black ones next time.
''',
'''你的白鞋还好吗？|Are your white shoes okay?
刚才还是白的。|They were white a moment ago.
现在呢？|And now?
现在大概有三种颜色。|Now there are probably three colours.
回去洗洗吧。|Wash them when we get back.
下次我穿黑的，比较保险。|I'll wear black ones next time. A safer bet.
'''),
14:(
'''你怎么站在门外？活动还没开始吧？|Why are you outside? The event hasn't started yet, has it?
我收到一张图，说今天取消了。|Someone sent me an image saying it was cancelled today.
让我看看。这上面是上个月的日期。|Let me see. That's last month's date.
啊，我白跑一趟了？|Oh, have I come all this way for nothing?
不是，今天并没有取消，只是换到二楼。|No. It hasn't been cancelled today; it's moved upstairs.
你怎么知道？|How do you know?
我刚问了门口的工作人员，新通知也贴在这儿。|I just asked the staff member by the door. The new notice is here too.
果然，写着二楼。那赶紧上去吧。|You're right: it says the second floor. Let's go up quickly.
时间没变，七点开始，还早。|The time hasn't changed. It starts at seven. We've time.
千万别告诉大家我看错日期。|Please don't tell everyone I got the date wrong.
我不说，你下次先把图放大。|I won't. Zoom in on the image first next time.
好。我刚才根本没看下面那一行。|Okay. I didn't look at the bottom line at all.
''',
'''我六点半到活动室门口，看见陈宇站在外面。他拿着手机，说今天的活动取消了，我差点也跟着往回走。|I arrived at the activity room at six thirty and found Chen Yu outside with his phone. He said the event was cancelled. I almost headed home with him.
他把图片给我看，我注意到下面有日期，是上个月的。我把图放大，他终于看清楚，问今天是不是仍然在这里。|He showed me the image. The date at the bottom was from last month. I zoomed in, and he finally saw it and asked whether today's event was still here.
门口的工作人员告诉我们，今天换到二楼，时间没变，仍是七点开始。旁边贴着一张新通知，上面也写得清楚。|The staff member said today's event had moved to the second floor, still starting at seven. The new notice beside the door said the same.
陈宇把新通知拍下来，发给同来的两个朋友。一个朋友已经快到了，说幸好看到消息，刚才也准备回家。|Chen Yu photographed the new notice and sent it to two friends coming along. One was nearly there and was glad of the message: they'd been about to go home too.
我们先上楼，找了四个连在一起的位子。两位朋友过来坐下，一个笑着问陈宇，是不是上个月就来过。|We went upstairs and found four seats together. When the friends sat down, one jokingly asked Chen Yu whether he'd come last month already.
陈宇说没有，不过上个月的日期倒是认识了。我把手机收好，演出正好开始，这一趟总算没白来。|No, said Chen Yu, but he now knew last month's date well. I put away my phone as the show began. The trip hadn't been for nothing after all.
''',
'''是不是上个月就来过？|Did you come last month already?
没有，我今天才认识那个日期。|No. I only met that date today.
那今天的日期呢？|What about today's date?
认识了，不用再介绍。|We've met. No more introductions needed.
好，手机收起来吧。|Okay. Put your phone away.
这次绝对不看错。|I definitely won't misread it this time.
'''),
15:(
'''明天的交流活动，是你们学生会举办的？|Is tomorrow's exchange organised by your student union?
对，由文艺部负责，我帮忙报到。|Yes. The arts department is handling it. I'm helping with registration.
谁主持？文艺部部长吗？|Who's hosting? The head of the arts department?
不是，小周主持。主任今天来确认过房间。|No, Xiao Zhou. The director confirmed the room today.
我们几个几点到？|When should our group arrive?
九点在门口集中，先签名，再拿名字卡。|Gather at the entrance at nine, sign in, then collect name cards.
不用每个人都发言吧？|Not everyone has to speak, right?
不用，每组派一位代表，按照名单顺序说。|No. One representative per group, speaking in the order on the list.
一人说多久？|How long per person?
两分钟。你说吧，上次旅行的照片也可以放。|Two minutes. Why don't you speak? You can show your travel photos too.
那我今晚选三张，别一讲就停不下来。|I'll choose three tonight so I don't talk endlessly.
放心，小周会提醒你。|Don't worry. Xiao Zhou will remind you.
''',
'''学校明天举办一次交流活动，由学生会文艺部负责。陈宇帮忙报到，小周主持。我和三个同学一起去，大家让我代表小组发言。|The school has an exchange tomorrow, organised by the student union's arts department. Chen Yu is helping with registration and Xiao Zhou is hosting. Three classmates and I are going, and they've asked me to speak for our group.
我晚上选了三张旅行照片，每张准备说几句话。一张是车站，一张是山上的风景，还有一张是我们在雨里找路。|That evening I chose three travel photos and prepared a few sentences for each: a station, a mountain view, and us finding our way in the rain.
第二天九点，我们在门口集中。陈宇让大家按名单签名，再拿自己的名字卡。他看见我的照片，说那张雨里的应该放在最后。|At nine the next day we gathered at the entrance. Chen Yu asked us to sign in following the list and collect our name cards. Seeing my photos, he suggested putting the rainy one last.
进房间以后，小周先介绍今天的安排。每组代表发言两分钟，其他人可以提问，之后大家再自由聊天。|Inside, Xiao Zhou introduced the plan: a two-minute talk from each group's representative, questions from others, then time for everyone to chat freely.
轮到我时，我先讲车站和山，最后放出雨里的照片。有人问是不是迷路了，我说是，最后是一位路过的奶奶带我们找到车站。|When it was my turn I described the station and mountain, then showed the rainy photo. Someone asked if we'd got lost. We had; a passing grandmother finally led us to the station.
活动结束，小周来问那张照片还有没有。我发给她，她说下次出门一定带地图。我说地图我们带了，下次要记得打开。|Afterwards Xiao Zhou asked for that photo. I sent it to her. She said she'd be sure to bring a map next time. We had one, I said; next time we needed to remember to open it.
''',
'''地图你们带了？|You brought a map?
带了，在手机里。|Yes, on the phone.
那怎么还迷路？|How did you still get lost?
我们当时只顾着拍照。|We were too busy taking photos.
下次先看地图，再拍。|Look at the map first next time, then take photos.
好，地图也给它拍一张。|Okay. I'll take a photo of the map too.
'''),
16:(
'''你在哪儿？我把箱子搬到哪儿？|Where are you? Where should I bring the box?
我在一楼门口，朝这边走。|At the entrance on the ground floor. Come this way.
大的还是小的？|The big one or the small one?
先搬小的，里面是安装工具。|Bring the small one first. It has the assembly tools inside.
大的里面都是书，确实有点重。|The big one's full of books. It really is heavy.
放着吧，等我一起搬。先帮我推开门。|Leave it for now; we'll carry it together. Push the door open for me first.
好。工具拿进去以后，我上去吗？|Okay. After taking the tools inside, should I go upstairs?
先在一楼等，桌子装好再把书搬上去。|Wait on the ground floor first. We'll carry the books up when the desk is assembled.
那我把小箱子放在门边那张旧桌子底下。|I'll put the small box under the old table by the entrance, then.
行，别放在门后面，开门会碰到。|Okay. Don't put it behind the door; the door will hit it.
知道了。你背上那个包要放下来吗？|Got it. Do you want to put down the bag on your back?
当然，先帮我拿一下，我还没找到拉链。|Yes. Hold it for a moment; I haven't found the zip yet.
''',
'''今天林安搬家，我过去帮忙。到了楼下，她站在一楼门口，背着一个大包，朝我招手，让我先拿小箱子。|Lin An was moving today and I went to help. She stood by the ground-floor entrance with a big backpack, waving me over and asking me to take the small box first.
小箱子里面是安装工具，大箱子里面都是书。我把工具拿进去，放在门边的旧桌子底下。书太重，等她放下包，我们再一起搬。|The small box held assembly tools; the big one held books. I took the tools inside and put them under the old table by the entrance. The books were heavy, so we'd carry them together after she put down her bag.
林安把门推开，我看见里面还有两件新家具。一张木头桌子还没装好，旁边放着椅子。她说桌子是准备搬到二楼的。|Lin An pushed the door open. Inside were two new pieces of furniture: an unassembled wooden desk and a chair beside it. She said the desk was going upstairs.
我们先把桌子装好，再一起抬上去。到了二楼，她把桌子放在朝南的窗边，我问书是不是也放这里，她说放在旁边的书架上。|We assembled the desk and carried it up together. Upstairs she put it by the south-facing window. I asked about the books; they'd go on the bookshelf beside it.
我下去拿书，她在楼上等。我拿了几本上来，放进书架，大箱子剩下的书就分几次拿，不再整箱搬。|I went down for the books while she waited upstairs. I brought up a few and put them on the shelf. We made several trips for the rest rather than moving the whole box.
全部放好以后，林安请我坐下喝水。我说椅子终于能用了，她笑着说今天最有用的家具，果然还是椅子。|When everything was in place Lin An offered me a seat and water. Finally a use for the chair, I said. She laughed that it really was today's most useful piece of furniture.
''',
'''今天最有用的家具是什么？|What's today's most useful piece of furniture?
椅子，我已经走不动了。|The chair. I can't walk any more.
桌子也装好了。|The desk's assembled too.
桌子给书坐，我坐椅子。|The books can sit at the desk. I'll take the chair.
好，水放你前面。|Okay. Your water's in front of you.
谢谢，今天不想再把它搬来搬去了。|Thanks. I don't want to keep carrying it around today.
''')}

QUESTIONS={
13:([
('gist','What plan do they choose?',['Lunch at home, with a walk if it stays dry','A morning walk before class','Cancelling every meeting'],0),
('detail','When should Chen Yu arrive?',['Around two','Nine in the morning','Six in the evening'],0),
('inference','Why not go in the morning?',['Chen Yu has class','There is no tea','The river is closed'],0)],[
('gist','How does Saturday turn out?',['Lunch indoors, followed by a walk after the rain','A whole day at school','No meeting at all'],0),
('detail','What does Chen Yu bring?',['A box of tea','A map of the mountains','Three white coats'],0),
('inference','Why wish to wear black shoes next time?',['The wet path has marked the white ones','Black shoes make tea taste better','The class requires black shoes'],0)]),
14:([
('gist','What do they discover?',['The cancellation image is old and today’s event is upstairs','Today’s event has no staff','They need a train ticket'],0),
('detail','Where is today’s event?',['On the second floor','At another school','Outside the entrance'],0),
('inference','Why did Chen Yu think it was cancelled?',['He missed the old date on the image','The staff told him to go home','The new notice has no time'],0)],[
('gist','What happens after the misunderstanding?',['They send the correct notice and attend the show','They all leave immediately','They attend last month’s show'],0),
('detail','How many seats do they find together?',['Four','Two','Six'],0),
('inference','Why is one friend glad of the message?',['They had been about to head home too','They wanted to buy a coat','They were hosting the event'],0)]),
15:([
('gist','What are the friends discussing?',['Registration and a short talk at a school exchange','A furniture delivery','A solo concert abroad'],0),
('detail','Who hosts?',['Xiao Zhou','The arts department head','The director'],0),
('inference','Why choose just three photos?',['To keep the talk short','The others have no names','Only three guests can register'],0)],[
('gist','What does the narrator share?',['Travel photos and a story about getting lost','A new registration fee','An account of buying furniture'],0),
('detail','How long is each representative’s talk?',['Two minutes','Twenty minutes','Half an hour'],0),
('inference','Why did carrying a map not prevent getting lost?',['They did not open it','The grandmother took the map','The phone had no photographs'],0)]),
16:([
('gist','What are they doing?',['Moving boxes and arranging a desk','Buying concert tickets','Registering a delegation'],0),
('detail','What is in the small box?',['Assembly tools','All the books','Tea and cups'],0),
('inference','Why leave the heavy box for now?',['They will carry it together','It is empty','The door has disappeared'],0)],[
('gist','How do the friends get the room ready?',['Assemble a desk and carry books upstairs in smaller loads','Leave all the furniture outdoors','Carry every box upstairs unopened'],0),
('detail','Where does the desk go?',['By the south-facing window upstairs','Behind the entrance door','Outside beside the bicycle'],0),
('inference','Why is the chair appreciated at the end?',['They are tired and can sit down','It has become a map','They need to register on it'],0)])}

REPLIES={
13:[('恐怕不行，我上午要上课。','I’m afraid I can’t; I have class in the morning.',['那下午在我家见吧。','那你九点就出门。','这张桌子还没装好。']),('两点左右到，不用带吃的。','Come around two. No need to bring food.',['好，我带点茶。','好，我明天才订票。','日期是上个月的。'])],
14:[('这张图是上个月的日期。','The date on this image is from last month.',['啊，那我看看今天的通知。','所以今天绝对取消了。','先把工具拿进去。']),('今天换到二楼，时间没变。','Today it’s on the second floor, at the same time.',['好，我们上去吧。','好，我们去另一个学校。','我来洗白鞋。'])],
15:[('每组派一位代表，说两分钟。','One representative from each group, speaking for two minutes.',['那我选三张照片来讲。','那我们每个人讲半小时。','我把椅子搬下去。']),('九点在门口集中，先签名。','Gather at the entrance at nine and sign in first.',['好，我通知另外三个同学。','好，我十点再来。','天气预报有雨。'])],
16:[('先搬小箱子，里面是工具。','Bring the small box first; it has the tools.',['好，大的等你一起搬。','好，我先搬最大的。','小周明天主持。']),('别放在门后面，开门会碰到。','Don’t put it behind the door; the door will hit it.',['那我放在桌子底下。','那我就放在门后面。','这张图片是旧的。'])]}

GLOSSES=[('林安','Lin An, a name'),('陈宇','Chen Yu, a name'),('小周','Xiao Zhou, a name'),('室内','indoors'),('左右','approximately; left and right'),('预报','forecast'),('小火','low heat'),('火','fire; heat'),('庆幸','feel fortunate'),('低头','lower one’s head'),('白鞋','white shoes'),('水','water'),('鞋','shoes'),('投资','investment'),('风险','risk'),('保险','insurance; safer'),('许愿','make a wish'),('愿望','wish'),('太阳','sun'),('图','image; diagram'),('放大','enlarge; zoom in'),('工作人员','staff member'),('贴','stick up; paste'),('连在一起','connected; together'),('一排','a row'),('收','put away; collect'),('告诉','tell'),('真实','real'),('弄清楚','clarify; establish'),('一趟','one trip'),('学生会','student union'),('文艺部','arts department'),('文艺','literature and arts'),('签名','sign one’s name'),('名字卡','name card'),('名字','name'),('卡','card'),('顺序','order; sequence'),('迷路','get lost'),('路过','pass by'),('提醒','remind'),('交流','exchange; communicate'),('名单','list of names'),('书展','book fair'),('参观','visit; tour'),('办公室','office'),('宣传','publicise'),('复杂','complex'),('新生','new student'),('会','meeting; can'),('空调','air conditioner'),('外卖','food delivery'),('家具','furniture'),('招手','wave one’s hand'),('拉链','zip'),('背上','on one’s back'),('背','carry on the back'),('装','assemble; install'),('书架','bookshelf'),('重','heavy'),('一楼','ground floor; first floor'),('二楼','second floor'),('木头','wood'),('工具','tools'),('方向','direction'),('朝南','face south')]

GLOSSES += [('丢','lose; discard'),('短视频','short video'),('视频','video'),('风景','scenery'),('背景','background'),('退票','refund a ticket')]

for number,(d,r,m) in TEXTS.items():
    pack=json.loads((ROOT/f'content/packs/s3-u{number:02}.json').read_text('utf-8'))
    examples={};contexts=[]
    for raw in VOCAB[number].splitlines():
        word,z,e,z2,e2=raw.split('|');assert word in z and word in z2 and z!=z2
        examples[word]=(z,e);contexts.extend([(z,e),(z2,e2)])
    assert set(examples)=={v['hanzi'] for v in pack['vocabulary']}
    dqs,rqs=QUESTIONS[number]
    i={13:3,14:4,15:9,16:3}[number]
    yes={13:'Chen Yu has class in the morning.',14:'The event is on the second floor.',15:'Each talk is two minutes.',16:'The small box holds tools.'}[number]
    no={13:'Chen Yu plans to wear white shoes again next time.',14:'The narrator says the trip was for nothing.',15:'The group had brought no map.',16:'Lin An never offers the narrator a seat.'}[number]
    tasks=[tf(*rows(d)[i],yes,True,'This fact is explicitly stated in this clip.'),tf(*rows(r)[-1],no,False,'This clip explicitly states a different fact.'),*[reply(z,e,c,0,'This response fits the immediate proposal.') for z,e,c in REPLIES[number]]]
    for word in {13:['大概','预计'],14:['果然','消息'],15:['主持','会议'],16:['搬家','工具']}[number]:tasks.append(fill(*examples[word],word))
    example_rows=list(examples.values());tasks.extend(match(example_rows[i:i+3]) for i in [0,3,6])
    inherited=[(g['hanzi'],g['meaning']) for t in [pack['dialogue'],pack['reading'],*pack['extraReadings']] for g in t.get('glosses',[])]
    repair(number,dict(dialogue=(rows(d),dqs),reading=(rows(r),rqs),media=(rows(m),[]),examples=examples,contexts=contexts,tasks=tasks,
        dialogueSpeakers={16:['陈宇','林安']}.get(number,['林安','陈宇']),mediaSpeakers={15:['小周','林安'],16:['林安','陈宇']}.get(number,['林安','陈宇']),
        glosses=list(dict.fromkeys(inherited+GLOSSES)),usage=[('Agree on the next action',REPLIES[number][0][0],REPLIES[number][0][1],'Respond to the person’s specific constraint or instruction.')],
        turns=[(z,e,'Respond to the concrete situation',[c[0]]) for z,e,c in REPLIES[number]],
        review='Replaced policy-like lines with rainy-day lunch and muddy-shoe teasing, a wrong-date mix-up, student-union registration and travel photos, and a move with tools, a desk and books. All 88 existing vocabulary IDs get two independent contexts; tasks and grammar ownership preserved. Self-review: class rules out morning, lunch around two, walk after three; old cancellation image and current second-floor seven-o’clock show; four classmates, one representative, two-minute talk, host Xiao Zhou; small box tools, large box books, desk assembled below then carried up, narrator goes down and comes back up. False listening statements contradict their own clip. Native flags: 保险 safer versus insurance, written 仍, empathetic 恐怕, rhetorical 难道, student-union 部长/主任 titles, 代表 token sense, 朝 cháo and 背 bēi, directional 上来/上去/下来/下去 tied to speaker position, and teasing personification of dates/books. Native review pending.'),publish='--publish' in sys.argv)

DEPENDENCIES={'s3-u22':[('古','ancient; old')], 's3-u33':[('一模一样','exactly alike')], 's5-u08':[('组织','organise; organisation')]}
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
