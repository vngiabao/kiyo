"""Replace four vocabulary-stuffed passages with authored everyday situations.

Default: drafts only. Old IDs survive publication and every gate still applies.
"""
import sys,json
from editorial_repair import repair,tf,reply,fill,match,ROOT
from advanced_core import rows

SCENES={
29:(
'''你今天怎么不放那段录音了？|Why aren't you playing that recording today?
我听了五遍，还是没听清最后那个时间。|I've listened five times and still can't make out the time at the end.
前面呢？你觉得他说了什么？|What about the beginning? What do you think he said?
他想周六见面。我读这段话读得很慢，看到最后才发现是下午三点。|He wants to meet on Saturday. Reading it slowly, I only noticed at the end that it was three in the afternoon.
我刚才也听成上午了。要不先听最后两句？|I heard morning too. Shall we start with the last two sentences?
好，你先别告诉我答案，让我再试一次。|Sure. Don't tell me the answer yet; let me try again.
这次怎么样？|How was it this time?
听出来了！不是越快越好，我刚才太急了。|I got it! Faster isn't always better. I was rushing.
那我们休息一下？你杯子里的茶都凉了。|Shall we take a break? Your tea's gone cold.
对，再听下去，今晚就没完没了了。|Yes. If we keep listening, we'll be here all night.
''',
'''上周朋友介绍了一门汉语课程。我试了第一节，老师让我们听两个朋友约时间。|A friend recommended a Chinese course last week. In the first class, we listened to two friends arranging a meeting.
我基本上听懂了，却把下午三点写成上午三点。朋友看见我的答案，笑着问谁会凌晨去喝茶。|I understood most of it but wrote three in the morning instead of the afternoon. My friend laughed and asked who would meet for tea before dawn.
晚上我又打开教材。我读那几句话读得很慢，把时间圈出来，再听同一段录音。|That evening I reopened the textbook, read the sentences slowly, circled the time and listened again.
头两次我还想看字。后来听见下午两个字，就知道这次不能写上午。|For the first two tries I still wanted to look at the text. Later, hearing 'afternoon', I knew not to write 'morning'.
朋友发消息问我明天几点见。我回下午三点，她说这次可别真的半夜来。|My friend asked when to meet tomorrow. I replied three in the afternoon. She told me not to turn up in the middle of the night this time.
我关了书去洗杯子。今天花的工夫不少，至少明天不会半夜跑去等她。|I closed the book and washed my cup. It had taken time, but at least I wouldn't go to meet her in the middle of the night tomorrow.
''',
'''你确定是下午三点？|Are you sure it's three in the afternoon?
确定。我现在连做梦都能听见下午两个字。|Yes. I can hear 'afternoon' even in my dreams now.
那你晚上早点睡，别三点就到店里。|Get to bed early then. Don't arrive at the cafe at three in the morning.
你再说，我真会把闹钟设错。|Keep saying that and I really will set my alarm wrong.
好了好了，明天下午见。|All right, all right. See you tomorrow afternoon.
记得带教材，这次我来问你。|Bring the textbook. This time I'll ask you the questions.
'''),
30:(
'''你手里这个小盒子是什么？|What's that little box in your hand?
我们课程上做的灯。打开以后，里面的纸会慢慢转。|A lamp we made in class. When it's switched on, the paper inside turns slowly.
你做的？我还以为是店里买的。|You made it? I thought you bought it in a shop.
盒子是我做的，里面的小机器是老师给的。|I made the box; the teacher gave us the little mechanism inside.
我可以打开看看吗？|Can I switch it on and have a look?
可以，先把它放在桌上。拿在手里会挡住下面。|Sure. Put it on the table first. Holding it blocks the bottom.
怎么只转了一下？|Why did it only turn once?
纸卡住了。我昨天也遇到这个问题，得把这边剪短一点。|The paper's stuck. That happened yesterday too. I need to trim this edge.
我帮你拿着剪刀，你慢慢来。|I'll hold the scissors for you. Take your time.
谢谢。制作这个比我想的难，但终于有点样子了。|Thanks. It was harder to make than I expected, but it's taking shape at last.
''',
'''姐姐是一位工程师，周末带我参加学校的科技活动。我想做一盏会转的小灯，她先问我有没有画图。|My sister, an engineer, took me to a school technology event at the weekend. I wanted to make a small turning lamp; she first asked whether I'd drawn it.
我说画图太慢，想直接开始。姐姐让我量一量纸盒，结果里面比我以为的小很多。|I said drawing was too slow and wanted to start. She asked me to measure the box. It was much smaller inside than I'd thought.
做完以后，小机器能转，纸却总卡住。姐姐没有帮我全部重做，只让我看看是哪一边碰到了盒子。|The mechanism turned, but the paper kept catching. Rather than rebuild everything, my sister asked me which edge was touching the box.
我把纸剪短一点，再试一次。这次它转了一圈，我高兴得想马上拿回家给朋友看。|I trimmed the paper and tried again. It made a full turn. I was so pleased I wanted to take it home and show my friends immediately.
姐姐说先把桌子上的东西收好。我一看，剪下来的纸比放进灯里的还多。|My sister reminded me to clear the table first. There was more scrap paper on it than paper inside the lamp.
回家以后，我把灯放在书架上。朋友问它能不能一直转，我说能，但最好别让我的猫发现。|At home I put the lamp on the bookshelf. A friend asked whether it could keep turning. I said yes, as long as my cat didn't discover it.
''',
'''你说这是自己做的，我差点就信了。|When you said you made it, I almost believed you.
真是我做的！只是机器不是我做的。|I did! Just not the mechanism.
那猫也能算帮忙吧？它刚才把纸从桌上推下来了。|Can we count the cat as a helper too? It pushed the paper off the table.
它负责检查我有没有收好东西。|Its job is checking whether I've put things away.
看来检查结果不太好。|That check doesn't seem to have gone very well.
你别笑了，帮我把纸捡起来。|Stop laughing and help me pick up the paper.
'''),
31:(
'''周六去你姐姐住的村里，还按昨天那条路线走吗？|For Saturday's trip to your sister's village, are we still following yesterday's route?
她刚打来电话，说西边那条路在修，要从东边过去。|She just called. The western road's being repaired, so we need to approach from the east.
我们先坐火车，再换汽车？|Train first, then a bus?
对。九点到车站，九点半有一班去村里的车。|Yes. We reach the station at nine; a bus to the village leaves at nine thirty.
朋友推荐的旅馆呢？我想住一晚。|What about the inn our friend recommended? I'd like to stay overnight.
就在村口，我姐姐说还有房间。我们今天打电话问问。|It's at the village entrance. My sister says there are rooms left. Let's call today.
好。第二天我想去看看河边，听说那里很安静。|Good. I'd like to visit the riverside the next day. I hear it's quiet.
早上去吧。姐姐说下午来的人多。|Let's go in the morning. My sister says more people come in the afternoon.
那别忘了叫我起床，我在旅馆容易睡过头。|Don't forget to wake me. I tend to oversleep at inns.
行，但你别把手机声音关了。|Sure, but don't silence your phone.
''',
'''周六早上，我们坐火车到城南的小站。朋友的姐姐住在附近的村里，要在那里等我们。|On Saturday morning we took the train to a small station south of the city. Our friend's sister was waiting at her nearby village.
我们昨天看过的路线图上有两条路。西边的路短一些，可是正在修，只能走东边。|Yesterday's map showed two roads. The western one was shorter but under repair, so we took the eastern one.
九点半的汽车还没来，朋友先去买水。我站在车站外，发现天上的云越来越厚。|The nine-thirty bus hadn't arrived yet. My friend went for water; outside the station I noticed the clouds thickening.
到了村口，姐姐拿着伞来接我们。她笑着说，幸好早上没有急着去河边，不然现在都湿了。|At the village entrance his sister met us with umbrellas. She said it was lucky we hadn't rushed to the river that morning, or we'd be soaked now.
我们先把包放进旅馆，再去她家吃饭。下午雨停了，三个人一起走到河边。|We put our bags in the inn, then ate at her house. After the rain stopped that afternoon, the three of us walked to the river.
第二天回来时，修路的地方还没开。我们又坐同一班车，手机里却多了几十张照片。|The road still hadn't reopened when we returned the next day. We took the same bus, with dozens more photos on our phones.
''',
'''你说村口的旅馆好找，我怎么走到河边了？|You said the inn was easy to find. How did I end up by the river?
你是不是只看见我发的照片，没看地址？|Did you look at the photo I sent and miss the address?
照片很好看嘛。|It was a lovely photo.
看照片去旅行，难怪你总找不到路。|Travelling by photos explains why you're always lost.
行，我现在看地址。你别再发猫的照片了。|Fine, I'm checking the address now. Stop sending cat photos.
那你赶快回来，猫已经占了你的位置。|Hurry back then. The cat's taken your seat.
'''),
32:(
'''旅行社发来的电子邮件，你看了吗？|Have you read the travel agency's email?
看了两遍，日期看懂了，最后那张表还没填。|Twice. I understand the dates, but I haven't filled in the form at the end.
你不是昨天就发出去了吗？|Didn't you send it yesterday?
我发的是问题，不是填好的表。我想问能不能周五出发。|I sent a question, not a completed form. I asked whether we could leave on Friday.
他们怎么说？|What did they say?
还没回。我早上又问了一次，怕邮件进了别的邮箱。|No reply yet. I asked again this morning in case the email went to another inbox.
要不下午打电话？网上的日期不一定还有地方。|Shall we call this afternoon? There might not still be places for the dates online.
好，你三点有空吗？我有些话不知道怎么问。|Sure. Are you free at three? I'm unsure how to ask a few things.
有。我坐你旁边，你先说，问不清楚我再帮你。|Yes. I'll sit beside you. You start; if anything's unclear, I'll help.
那我先把要问的写下来，别到时候又忘了。|I'll write my questions down first so I don't forget them again.
''',
'''我想和朋友周五出发，周日晚上回来。旅行社的网页上写着周四出发，我们就发邮件问有没有别的安排。|My friend and I wanted to leave Friday and return Sunday evening. The agency's website said Thursday, so we emailed about other options.
第二天还没收到回复，朋友问我是不是已经订好了。我把发出去的邮件给她看，最后一句明明是问句。|The next day there was still no reply. My friend asked whether I'd booked. I showed her the email: its final sentence was clearly a question.
下午三点，我们一起打电话。工作人员说周五也有位置，不过回来要到周一。|At three we called together. The staff member said there were Friday places, but the return would be Monday.
我周一有课，不能参加这次旅行。朋友说没关系，我们可以找近一点的地方，不一定跟团。|I had class Monday, so couldn't take that trip. My friend said we could find somewhere nearer and needn't join a group.
电话结束以后，我写下了新的安排。我们周六去附近的城市，晚上就回来，不用请假。|After the call I wrote down our new plan: visit a nearby city Saturday and return that evening, without taking time off.
那张没填的表留在邮箱里。朋友说下次再看它吧，这次先找一家好吃的店。|The unfinished form stayed in my inbox. My friend said we'd look at it another time; for now, we should find a good restaurant.
''',
'''你给旅行社写了多长的邮件？|How long was your email to the agency?
不长，就几个问题。|Not long. Just a few questions.
我看着怎么有两页？|Why does it look like two pages?
一页是问题，一页是我怕他们没看见，又写了一遍。|One page is the questions. I repeated them on another in case they missed them.
难怪你看了两遍。|No wonder you read it twice.
好了，我以后少写一点。你先帮我看最后一句。|All right, I'll keep it shorter next time. Help me check the last sentence first.
''')}

KEYS={
29:[('Why repeat the last two sentences?','To hear the meeting time','To cancel the course','To buy new tea'),('When will the friends meet?','Tomorrow afternoon at three','Tomorrow morning at three','Tonight at midnight'),('Why does the friend joke about an alarm?','The narrator confused morning and afternoon','The cafe sells alarm clocks','The textbook has no dates')],
30:[('What has the learner made?','A small lamp with turning paper','A whole industrial machine','A new phone'),('Why did the paper stop turning?','It caught inside the box','The cat took the lamp away','The teacher cancelled class'),('Why measure first?','The box is smaller than expected','The sister refuses to help','The lamp has already been sold')],
31:[('Why take the eastern road?','The western road is under repair','The inn has moved to Beijing','The train has no seats'),('When does the bus leave?','Nine thirty','Nine','Three'),('Why did they visit the river in the afternoon?','Rain stopped then','The sister had left forever','They cancelled their whole trip')],
32:[('What did the learner email?','A question about Friday departure','A completed booking form','A newspaper report'),('Why reject the agency trip?','Its Monday return conflicts with class','No Friday seats exist','The friend dislikes trains'),('What is their final plan?','A nearby city on Saturday, home that evening','The same trip until Monday','A two-week overseas trip')],
}

# Each tuple below is an independent vocabulary example, not a continued story.
EXAMPLES={
29:'''课程|这门课程每周上两次。|This course meets twice a week.
教材|我把教材忘在教室里了。|I left the textbook in the classroom.
基础|她有钢琴基础，学这首曲子比较快。|She has a piano background, so she's learning this piece fairly quickly.
基本|我们先学几个基本动作。|Let's learn a few basic movements first.
基本上|大家基本上都到了，还差两个人。|Nearly everyone is here; two people are still missing.
听力|我的听力比以前好一些了。|My listening is a little better than before.
试题|老师发给我们一份去年的试题。|The teacher gave us last year's test questions.
题目|这道题目问的是时间，不是地点。|This question asks for the time, not the place.
初|初来这里的时候，我谁也不认识。|When I first came here, I didn't know anyone.
工夫|我花了一个下午的工夫整理这些照片。|I spent an afternoon organising these photos.
功夫|她做菜的功夫是跟妈妈学的。|She learned her cooking skills from her mum.
功课|做完功课以后，我们去打球。|Let's play ball after finishing our homework.
力|你帮我推一下，我一个人的力不够。|Help me push; I'm not strong enough on my own.
实力|这支球队很有实力。|This team is very capable.
动力|有人一起练，我就更有动力。|I feel more motivated when someone practises with me.
理论|这个理论我还没完全理解。|I haven't fully understood this theory yet.
计算|请计算一下这次一共花了多少钱。|Please calculate our total spending this time.
得分|他的得分比上次高了十分。|His score is ten points higher than last time.
输入|请先输入你的名字。|Please enter your name first.
了|他们说起小时候的事，没完没了。|Once they start on their childhood, they go on endlessly.
连|把这两个点连起来，就是一条直线。|Join these two points to make a straight line.
头|头两天先休息，后面再去看朋友。|Rest for the first two days, then visit friends.
''',
30:'''产生|这个消息让大家产生了新的想法。|This news gave everyone new ideas.
发明|他发明了一种更轻的小工具。|He invented a lighter little tool.
发展|这座城市的发展很快。|This city's development is rapid.
开发|他们正在开发一个新的学习工具。|They're developing a new study tool.
科技|她对科技新闻很感兴趣。|She's interested in science and technology news.
先进|这家医院有先进的设备。|This hospital has advanced equipment.
化|这座城市正在进行现代化建设。|This city is undergoing modernisation.
工程师|我姐姐是一位工程师。|My sister is an engineer.
工厂|这家工厂离车站不远。|This factory isn't far from the station.
工业|这座城市过去主要发展工业。|This city previously developed industry as its main activity.
生产|这家工厂生产儿童玩具。|This factory produces children's toys.
制造|他们制造的机器卖到很多地方。|The machines they manufacture are sold in many places.
制作|我们一起制作了一本小相册。|We made a little photo album together.
加工|这些材料还需要加工。|These materials still need processing.
人工|机器做完以后，还有一次人工检查。|After the machine finishes, there's a manual check.
机器|这台机器下午就能修好。|This machine can be fixed this afternoon.
设备|新设备到了，旧的还留着。|The new equipment has arrived; we're keeping the old equipment too.
实验|我们明天做这个实验。|We'll carry out this experiment tomorrow.
实验室|老师在实验室等我们。|The teacher's waiting for us in the laboratory.
试验|新办法先进行一次试验。|The new approach will undergo a trial first.
实行|这个方案从下个月开始实行。|This plan will be implemented next month.
专家|几位专家一起讨论了这个问题。|Several specialists discussed this issue together.
''',
31:'''北部|这所学校在城市北部。|This school is in the northern part of the city.
东部|这个地区的东部经常下雨。|It often rains in the eastern part of this region.
南部|南部的天气比这里暖和。|The weather in the south is warmer than here.
西部|城市西部有一个很大的公园。|There's a large park in the western part of the city.
中部|地图中部那个地方就是车站。|That place in the centre of the map is the station.
地区|这个地区有很多小村。|This region has many small villages.
区|我们学校在这个区。|Our school is in this district.
城市|我想去别的城市住一段时间。|I'd like to live in another city for a while.
城|爷爷明天进城看医生。|Grandpa's going into town to see a doctor tomorrow.
村|这个村有两百多户人家。|This village has more than two hundred households.
农村|她小时候住在农村。|She lived in the countryside as a child.
农民|几位农民正在地里干活。|Several farmers are working in the fields.
农业|他学习农业，想回家种菜。|He's studying agriculture and wants to return home to grow vegetables.
首都|北京是中国的首都。|Beijing is China's capital.
长城|我还没去过长城。|I haven't been to the Great Wall yet.
路线|我们先看看哪条路线比较近。|Let's check which route is shorter.
前往|前往车站的汽车就在门外。|The bus heading to the station is right outside.
高速|这种列车可以高速行驶。|This kind of train can travel at high speed.
高速公路|这条高速公路经过三个城市。|This expressway passes through three cities.
铁路|这条铁路去年开始修。|Work on this railway began last year.
飞行|这次飞行用了两个小时。|This flight took two hours.
旅馆|这家旅馆就在河边。|This inn is beside the river.
''',
32:'''报|我爷爷早上喜欢看报。|Grandpa likes to read the newspaper in the morning.
报道|我在网上看到了这次活动的报道。|I saw a report about this event online.
报告|她的报告一共写了五页。|Her report is five pages long.
发出|我已经发出邀请了。|I've sent out the invitation.
发表|他在学校的报上发表了一篇文章。|He published an article in the school newspaper.
电子邮件|她用电子邮件联系了老师。|She contacted the teacher by email.
邮件|我还有三封邮件没看。|I have three unread emails.
邮箱|请把新的邮箱地址发给我。|Please send me your new email address.
邮票|我在信封上贴了一张邮票。|I put a stamp on the envelope.
信封|这个信封太小，放不下照片。|This envelope is too small for the photo.
证件|出发以前，先把证件收好。|Put your identification documents away safely before leaving.
身份证|我的身份证放在钱包里。|My identity card is in my wallet.
通信|我们毕业以后还一直通信。|We've kept corresponding since graduation.
交易|这次交易已经完成了。|This transaction is complete.
海关|通过海关以后，我们去拿行李。|After going through customs, we collected our luggage.
旅行社|我想问旅行社能不能改时间。|I'd like to ask the travel agency whether the time can be changed.
信|我信你的话，你不用再解释了。|I believe you; you don't need to explain again.
大使馆|大使馆的地址写在这张纸上。|The embassy's address is on this piece of paper.
美元|这本书要十美元。|This book costs ten US dollars.
资金|他们还在准备开店需要的资金。|They're still raising the funds needed to open the shop.
正式|我们还没有收到正式通知。|We haven't received an official notice yet.
证|他的学生证掉在教室里了。|He dropped his student card in the classroom.
'''}

FOLLOWUPS={
29:[('这次先听哪一部分？','Which part should we listen to first?',['最后两句。','明天下午三点。','这杯茶已经凉了。']),('我想自己听，不看答案，应该先关掉什么？','What should I hide to listen on my own without seeing the answer?',['先把文字关掉。','先把声音关掉。','先把录音删掉。'])],
30:[('纸碰到盒子卡住了，先检查哪里？','Where should we check first if the paper catches against the box?',['看看哪一边碰到了。','先看看灯是什么颜色。','只看看猫坐在哪里。']),('灯下面不能挡住，应该放在哪里？','Where should we put the lamp if its underside must remain clear?',['放在桌上，别拿手挡住下面。','拿在手里把下面盖住。','用纸把下面包起来。'])],
31:[('西边的路还在修，哪边可以过去？','Which side can we use while the western road is being repaired?',['从东边过去。','走正在修的西边那条路。','先从西边穿过修路的地方。']),('旅馆的地址是什么？','What is the inn’s address?',['我把地址发给你。','旅馆早上九点开门。','旅馆里有一只猫。'])],
32:[('你只是问有没有安排，还没有付款，订好了吗？','You only asked about arrangements and have not paid. Is it booked?',['没有，我还在等他们回复。','已经付款订好了。','我已经收到正式确认了。']),('周一有课，不能参加周一才回来的旅行，怎么改？','How can we change a trip that returns Monday when we have class then?',['换个周日以前能回来的安排。','继续订周一回来的那趟。','不改时间，还是周一回来。'])],
}

PASSAGE_QUESTIONS={
29:([
('gist','What are the friends trying to understand?',['The time in a recording','A train route','The price of a lamp'],0),
('detail','Which part will they repeat first?',['The last two sentences','Only the title','A different song'],0),
('inference','Why mention the cold tea?',['They have practised long enough for a break','The cafe has no hot water','The learner ordered ice'],0)],
[
('gist','What changes in the narrator’s practice?',['They slow down and attend to the time','They stop studying completely','They replace the course with a night job'],0),
('detail','What time do the friends arrange for tomorrow?',['Three in the afternoon','Three in the morning','Six in the morning'],0),
('inference','Why does the friend joke about a night visit?',['The narrator previously confused morning and afternoon','The cafe only opens overnight','The friend refuses to meet'],0)]),
30:([
('gist','What is the learner showing the friend?',['A small lamp they made','A factory they bought','A travel booking'],0),
('detail','Who supplied the small mechanism?',['The teacher','The cat','The travel agency'],0),
('inference','Why trim the paper?',['It is catching against the box','The lamp needs a new address','The friend dislikes all paper'],0)],
[
('gist','How does the narrator get the lamp working?',['Measure and trim the paper after a failed try','Buy an entirely finished lamp','Ask the cat to build it'],0),
('detail','What does the sister ask for before going home?',['Clear the table','Buy a factory','Cancel next week’s course'],0),
('inference','What does the final cat remark suggest?',['The cat might interfere with the lamp','The cat has designed the machine','The lamp is intended only for cats'],0)]),
31:([
('gist','What are the friends planning?',['An overnight village visit','Moving abroad forever','A trip to the Great Wall'],0),
('detail','When is the bus to the village?',['Nine thirty','Nine','Three'],0),
('inference','Why call the inn today?',['Check a room before staying overnight','Ask it to repair the western road','Cancel the train station'],0)],
[
('gist','What happens during their visit?',['They reach the village by the eastern road and visit the river after rain','They spend the entire weekend at the station','They return before arriving'],0),
('detail','When do they actually walk to the river?',['Saturday afternoon after rain stops','Saturday before boarding the train','Monday evening'],0),
('inference','Why was delaying the riverside walk fortunate?',['They avoided getting soaked in rain','The river had disappeared','They had no phone photos'],0)]),
32:([
('gist','What needs clarifying?',['Whether Friday departure is available','Whether a newspaper has been printed','Whether the learner owns the agency'],0),
('detail','When will they make the call together?',['Three in the afternoon','Before dawn','Next Monday night'],0),
('inference','Why ask the friend to sit beside them?',['Help asking unfamiliar questions','The friend has already booked everything','The form must be printed twice'],0)],
[
('gist','What is their final choice?',['A nearby city on Saturday and home that evening','The agency trip returning Monday','No further outings ever'],0),
('detail','Why does the agency’s Friday option fail?',['Its Monday return conflicts with class','Friday places are sold out','The friend cannot read emails'],0),
('inference','Why show the sent email?',['Its final question shows there was no booking','It proves Monday class was cancelled','Its length proves the agency agreed'],0)])}

SECOND={
29:'''课程|这门课程下周结束。|This course ends next week.
教材|新教材里有几篇短故事。|The new textbook has some short stories.
基础|先把基础练好，再学复杂一点的。|Practise the basics before learning something more complex.
基本|房间里有基本的生活用品。|The room has basic daily supplies.
基本上|这个房间基本上没变。|This room has hardly changed.
听力|我们周五有听力考试。|We have a listening test on Friday.
试题|这份试题有二十道题。|This test has twenty questions.
题目|你先读题目，再看下面的图。|Read the question before looking at the picture below.
初|初学的时候，我每天只练十分钟。|When I started learning, I practised just ten minutes daily.
工夫|做这道菜很费工夫。|This dish takes a lot of time and effort.
功夫|你切菜的功夫比我好多了。|Your knife skills are much better than mine.
功课|她每天晚上帮弟弟做功课。|She helps her younger brother with his homework every evening.
力|我用了很大的力，门还是推不开。|I pushed hard, but the door still wouldn't open.
实力|比赛结束以后，大家都看到了她的实力。|Everyone saw her ability after the competition.
动力|想到周末能见朋友，我就有动力了。|Thinking of seeing my friends at the weekend motivates me.
理论|他把这个理论讲得很清楚。|He explained this theory clearly.
计算|我用手机计算每个人要付的钱。|I used my phone to calculate what each person owed.
得分|我们队这场比赛的得分不高。|Our team's score in this game wasn't high.
输入|地址输入错了，我再改一下。|I entered the address incorrectly; I'll fix it.
了|别没完没了地说了，车都快走了。|Stop going on and on; the bus is about to leave.
连|这条线把两个小灯连在一起。|This wire connects the two little lamps.
头|头一回见面，她还有点不好意思。|She was a little shy when we first met.
''',
30:'''产生|他们讨论以后产生了一个新计划。|Their discussion produced a new plan.
发明|她发明的小机器能帮助人整理材料。|The little machine she invented helps people organise materials.
发展|我想了解这个地区的发展。|I'd like to learn about this region's development.
开发|公司开发的工具现在已经能用了。|The company's new tool is now ready to use.
科技|这个科技节目介绍了几种新的机器。|This science and technology programme introduced several new machines.
先进|这些先进的方法也需要人认真使用。|These advanced methods also need to be used carefully.
化|办公室的工作越来越信息化了。|The office's work is becoming increasingly computerised.
工程师|那位工程师给我们画了一张图。|That engineer drew a diagram for us.
工厂|他在这家工厂工作了十年。|He's worked at this factory for ten years.
工业|这本书介绍了当地工业的变化。|This book describes changes in local industry.
生产|他们从下个月开始生产这种材料。|They'll start producing this material next month.
制造|这家公司的工作是制造汽车。|This company manufactures cars.
制作|她制作了一段介绍家乡的视频。|She made a video introducing her hometown.
加工|加工以后，木头的表面很平。|After processing, the wood's surface is smooth.
人工|这里的检查主要靠人工完成。|Checks here are mostly carried out manually.
机器|先把机器关了，再清理桌子。|Switch off the machine before clearing the table.
设备|教室里的设备是去年买的。|The classroom equipment was bought last year.
实验|这次实验的结果跟上次不同。|This experiment's result differs from the last one.
实验室|实验室下午五点关门。|The laboratory closes at five in the afternoon.
试验|试验结束以后，我们换了一种材料。|After the trial, we switched materials.
实行|学校已经开始实行新的安排。|The school has begun implementing the new arrangements.
专家|我想请专家看看这份计划。|I'd like a specialist to look at this plan.
''',
31:'''北部|北部的冬天通常更冷。|Winters in the north are usually colder.
东部|我们明天去城市东部看朋友。|We'll visit a friend in the eastern part of the city tomorrow.
南部|地图上南部有一条河。|There's a river in the southern part of the map.
西部|她家住在这个地区的西部。|Her home is in the western part of this region.
中部|我们在公园中部见面。|We'll meet in the middle of the park.
地区|不同地区的生活习惯不完全一样。|Living habits differ between regions.
区|我想找离这个区近一点的房间。|I'd like a room a little nearer this district.
城市|这座城市的晚上很安静。|This city is quiet at night.
城|周末我们出城看朋友。|We're going out of town to see a friend this weekend.
村|村里的人都认识我姐姐。|Everyone in the village knows my sister.
农村|他们想回农村住一段时间。|They'd like to spend some time living in the countryside again.
农民|她的父母都是农民。|Both her parents are farmers.
农业|这个地区主要发展农业。|This region primarily develops agriculture.
首都|你去过他们国家的首都吗？|Have you been to their country's capital?
长城|朋友给我看了她在长城拍的照片。|My friend showed me photos she'd taken at the Great Wall.
路线|雨停以后，我们改了路线。|We changed our route after the rain stopped.
前往|请前往三楼的教室。|Please go to the classroom on the third floor.
高速|这种机器不能一直高速工作。|This machine can't keep running at high speed indefinitely.
高速公路|雨很大，高速公路暂时不能走。|It's raining heavily; the expressway is temporarily closed.
铁路|铁路经过我们村附近。|The railway passes near our village.
飞行|我第一次飞行的时候很紧张。|I was nervous on my first flight.
旅馆|我们已经订好了周六的旅馆。|We've booked our inn for Saturday.
''',
32:'''报|这张报上有一篇介绍我们学校的文章。|This newspaper has an article about our school.
报道|这篇报道介绍了当地的变化。|This report describes changes in the local area.
报告|老师让我们下周交报告。|The teacher asked us to hand in our reports next week.
发出|通知发出以后，几个人马上回复了。|Several people replied immediately after the notice went out.
发表|她刚发表了一篇短故事。|She's just published a short story.
电子邮件|我们还没收到他的电子邮件。|We haven't received his email yet.
邮件|这封邮件是昨天晚上来的。|This email arrived last night.
邮箱|你看看邮箱里有没有新的通知。|Check your inbox for a new notice.
邮票|她从小就喜欢收集邮票。|She's liked collecting stamps since childhood.
信封|请把地址写在信封上。|Please write the address on the envelope.
证件|这些证件都是我自己的。|These identification documents are all mine.
身份证|我找了半天，才找到身份证。|I spent ages looking before finding my identity card.
通信|我们以前用信通信，现在主要发邮件。|We used to correspond by letter; now we mostly email.
交易|这次交易的时间还没有确定。|The time of this transaction hasn't been fixed yet.
海关|她在海关工作了很多年。|She's worked at customs for many years.
旅行社|这家旅行社离学校很近。|This travel agency is near the school.
信|这件事听着奇怪，我有点不信。|This sounds strange; I don't quite believe it.
大使馆|我们约好在大使馆附近见面。|We've arranged to meet near the embassy.
美元|他还有二十美元没花。|He still has twenty US dollars left.
资金|资金准备好了，他们就开始找地方。|Once the funds were ready, they started looking for a space.
正式|我们下周正式开始上课。|Classes officially begin next week.
证|这张工作证是上个月办的。|This staff identification card was issued last month.
'''}

for number,(d,r,m) in SCENES.items():
    p=json.loads((ROOT/f'content/packs/s3-u{number:02}.json').read_text('utf-8'))
    examples={}
    for raw in EXAMPLES[number].strip().splitlines():
        word,z,e=raw.split('|');examples[word]=(z,e)
    contexts=[]
    for raw in SECOND[number].strip().splitlines():
        word,z,e=raw.split('|')
        assert word in z and word in examples
        contexts.extend([examples[word],(z,e)])
    keys=KEYS[number]
    dqs,rqs=PASSAGE_QUESTIONS[number]
    scenes=[*rows(d),*rows(r),*rows(m)]
    evidence={29:(3,'The meeting is at three in the afternoon.'),30:(7,'The paper is caught inside the box.'),31:(1,'The western road is under repair.'),32:(3,'The email asks a question; it is not a completed form.')}[number]
    taskrows=[tf(rows(d)[evidence[0]][0],rows(d)[evidence[0]][1],evidence[1],True,'The sentence explicitly supplies this information.'),
              tf(rows(r)[-1][0],rows(r)[-1][1],{29:'They decide to meet at three in the morning.',30:'The friend takes the lamp away.',31:'The western road has reopened on Sunday.',32:'They decide to stay away until Monday.'}[number],False,'The final passage explicitly describes a different outcome.'),
              *[reply(z,e,c,0,'This response follows the stated problem without contradicting the passage.') for z,e,c in FOLLOWUPS[number]],
              fill(*examples[{29:'教材',30:'制作',31:'路线',32:'电子邮件'}[number]],{29:'教材',30:'制作',31:'路线',32:'电子邮件'}[number]),
              fill(*examples[{29:'输入',30:'工程师',31:'旅馆',32:'信'}[number]],{29:'输入',30:'工程师',31:'旅馆',32:'信'}[number])]
    # Independent matching contexts retrieve vocabulary without inventing a story.
    items=list(examples.values())
    taskrows += [match(items[i:i+3]) for i in [0,3,6]]
    if len(p['tasks'])==10:taskrows.append(match(items[9:12]))
    gloss=[]
    for t in [p['dialogue'],p['reading'],*p['extraReadings']]:
        gloss.extend((g['hanzi'],g['meaning']) for g in t.get('glosses',[]))
    gloss += [('凌晨','the early hours before dawn'),('半夜','the middle of the night'),('圈','circle; mark with a circle'),('闹钟','alarm clock'),('卡','catch; jam (kǎ)'),('剪刀','scissors'),('剪','cut with scissors'),('裁','cut material'),('相册','photo album'),('贴','stick; affix'),('伞','umbrella'),('户','household; household classifier'),('团','group'),('跟团','travel with a tour group'),('河边','riverside'),('转','turn; rotate (zhuǎn)'),('行驶','travel, of a vehicle'),('盖','cover'),('捡','pick up'),('请假','request time off'),('空调','air conditioning'),('琴','a musical instrument'),('现代化','modernisation'),('信息化','computerisation; use of information systems'),('表面','surface'),('木头','wood'),('清理','clear away; tidy'),('种','type; kind')]
    gloss += [('梦','dream'),('曲','piece of music; tune'),('遇到','encounter'),('盏','classifier for lamps'),('兴趣','interest'),('儿童','children'),('视频','video'),('附近','nearby'),('厚','thick'),('幸好','fortunately'),('嘛','conversational explanatory particle'),('列车','train'),('填','fill in'),('填好','finish filling in'),('现代','modern')]
    spec=dict(dialogue=(rows(d),dqs),reading=(rows(r),rqs),media=(rows(m),[]),examples=examples,contexts=contexts,tasks=taskrows,glosses=list(dict.fromkeys(gloss)),
        turns=[(FOLLOWUPS[number][i][0],FOLLOWUPS[number][i][1],'Respond to the specific situation',[FOLLOWUPS[number][i][2][0]]) for i in range(2)],
        review='Removed grammar-analysis and permission disclaimers from character speech. The scene has one practical problem and a coherent timeline; unrelated vocabulary now has independent examples. Dates, times, causal questions and distractors were checked against their own passage. Every Chinese line still needs native review; particular flags: lamp mechanism 卡/转, 功夫/工夫 register, liǎo in 没完没了, casual travel teasing and the 信 trust sense. No scene claims that emailing constitutes a booking.')
    repair(number,spec,publish='--publish' in sys.argv)

# An older unit had relied on an incidental earlier use of 藏. Removing that
# artificial sentence must not leave its later learner-facing meaning missing.
# Preserve all its IDs and lines; supply the definition where it is now needed.
from common import py
pack=json.loads((ROOT/'content/packs/s3-u34.json').read_text('utf-8'))
text=pack['extraReadings'][0]
if not any(g['hanzi']=='藏' for g in text.get('glosses',[])):
    text.setdefault('glosses',[]).append(dict(hanzi='藏',pinyin='cáng',meaning='hide; put out of sight'))
dest=ROOT/('content/packs' if '--publish' in sys.argv else 'output/parity-editorial-drafts')/'s3-u34.json'
dest.write_text(json.dumps(pack,ensure_ascii=False,indent=2)+'\n','utf-8')

# These later texts used to borrow meanings from the removed artificial scene.
# Supply the actual local definitions rather than keeping that scene as padding.
from advanced_reading_repair import dependencies
dependencies({
 's5-u02':[('平稳','steady; stable')],
 's5-u08':[('小厅','small hall'),('摆','put; arrange'),('区域','area; region')],
 's5-u09':[('小厅','small hall')],
 's5-u10':[('小厅','small hall'),('缩','shrink; narrow')],
 's5-u11':[('摆','put; arrange'),('挑','choose; pick','tiāo')],
 's5-u12':[('缺乏','lack'),('接触','come into contact with'),('秒','second (time)')],
 's6-u01':[('小厅','small hall'),('估计','estimate'),('摆','put; arrange'),('挪','move; shift')],
 's6-u02':[('小厅','small hall'),('唯一','only; sole'),('栏','column; field on a form'),('柜子','cabinet'),('采纳','adopt; accept a suggestion'),('犯','make; commit (a mistake)'),('依赖','depend on; rely on')],
 's6-u03':[('挑','choose; pick','tiāo'),('嫌','dislike; find objectionable'),('阵','classifier for a burst of sound'),('小厅','small hall'),('圆','round'),('款','model; style of a product')],
 's6-u04':[('弹','play a musical instrument','tán'),('小厅','small hall'),('唯一','only; sole'),('挪','move; shift')],
 's6-u05':[('原稿','original manuscript'),('稿子','draft; manuscript'),('小厅','small hall'),('秒','second (time)'),('情绪','mood; emotion')],
 's6-u06':[('挑','choose; pick','tiāo'),('若','if'),('讨厌','dislike'),('引起','cause; give rise to'),('小厅','small hall'),('缩','shrink; narrow'),('凡是','all that; whenever')],
 's6-u07':[('伸','extend; stretch out'),('缩','shrink; narrow'),('挪','move; shift'),('大厅','main hall'),('小厅','small hall'),('若','if')],
 's6-u08':[('讨厌','dislike'),('引起','cause; give rise to'),('挑','choose; pick','tiāo'),('秒','second (time)'),('分析','analyse; analysis'),('唯一','only; sole'),('下降','fall; decrease'),('若','if')],
 's6-u09':[('区域','area; region'),('反馈','feedback'),('若','if'),('登记','register; registration'),('小厅','small hall')],
 's6-u10':[('小厅','small hall'),('缩','shrink; narrow'),('挑','choose; pick','tiāo'),('朗读','read aloud'),('阵','classifier for a burst of sound')],
 's6-u11':[('小厅','small hall'),('阵','classifier for a burst of sound')],
 's6-u12':[('触动','touch; move emotionally')],
},publish='--publish' in sys.argv)
pack=json.loads((ROOT/'content/packs/s4-u08.json').read_text('utf-8'))
text=pack['reading']
if not any(g['hanzi']=='依赖' for g in text.get('glosses',[])):
    text.setdefault('glosses',[]).append(dict(hanzi='依赖',pinyin='yī lài',meaning='depend on; rely on'))
dest=ROOT/('content/packs' if '--publish' in sys.argv else 'output/parity-editorial-drafts')/'s4-u08.json'
dest.write_text(json.dumps(pack,ensure_ascii=False,indent=2)+'\n','utf-8')
