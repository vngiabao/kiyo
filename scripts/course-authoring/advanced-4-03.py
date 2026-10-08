"""Authored group plan, fallback and fair division of practical work."""
import sys
from advanced_core import write,rows,words,q,card,practice

V=words('''
替|on someone’s behalf; instead of|thay cho|你能替我去拿一下票吗？|Could you collect the tickets for me?|她替同事上了一天班。|She covered a day of work for her colleague.
根据|according to; based on|dựa theo|根据天气情况，我们再决定去哪儿。|We’ll decide where to go based on the weather.|他根据大家的意见改了菜单。|He changed the menu based on everyone’s comments.
既然|since; given that|đã…thì|既然你也没吃饭，一起去吧。|Since you haven’t eaten either, let’s go together.|既然票都买好了，我们就早点出发。|Since the tickets are bought, let’s set off early.
以及|and; as well as|cũng như|桌上有茶、咖啡以及水果。|There are tea, coffee and fruit on the table.|这封邮件写了时间、地点以及需要带的东西。|This email gives the time, place and what to bring.
否则|otherwise|nếu không thì|我们早点走，否则会赶不上车。|Let’s leave early or we’ll miss the train.|先把名字写好，否则容易拿错。|Label the names first or people may take the wrong thing.
临时|temporary; at short notice|tạm thời; đột xuất|她临时有事，今天来不了。|Something came up, so she can’t come today.|我们找了一个临时放行李的地方。|We found a temporary place for our luggage.
尽快|as soon as possible|sớm nhất có thể|请尽快告诉我你几点能到。|Please let me know as soon as possible what time you can arrive.|我会尽快把照片发给你。|I’ll send you the photos as soon as I can.
再三|repeatedly; several times|nhiều lần|出门前，妈妈再三提醒我带伞。|Before I left, Mum reminded me several times to take an umbrella.|我再三确认了地址，还是走错了门。|I checked the address repeatedly and still went to the wrong door.
参与|participate in|tham gia|这次活动有十位邻居参与。|Ten neighbours are taking part in this event.|她也想参与讨论，但还没想好怎么说。|She wants to join the discussion too but hasn’t worked out what to say.
承担|take on; bear|đảm nhận|我来承担这次活动的车费。|I’ll cover the transport costs for this event.|他不想一个人承担所有工作。|He doesn’t want to take on all the work alone.
包括|include|bao gồm|这个价格包括一杯饮料。|This price includes a drink.|参加的人包括老师和学生。|Participants include teachers and students.
无论|regardless of; no matter|bất kể|无论下不下雨，我们都四点见。|Rain or no rain, we’ll meet at four.|无论你选哪一件，我都觉得好看。|Whichever one you choose, I think it looks good.
不管|no matter; regardless|dù; bất kể|不管有几个人来，我们都准备两壶茶。|However many people come, we’ll prepare two pots of tea.|不管谁先到，都在门口等一下。|Whoever arrives first should wait a moment at the door.
布置|arrange; decorate|sắp xếp; trang trí|我们一起布置房间，准备晚上的聚会。|We’re arranging the room together for tonight’s get-together.|桌子已经布置好了，就差花了。|The table is arranged; only the flowers are missing.
取消|cancel|hủy|因为大雨，今天的比赛取消了。|Today’s match was cancelled because of heavy rain.|我不想取消，只想换一个时间。|I don’t want to cancel, just change the time.
推迟|postpone|hoãn|我们把出发时间推迟了半小时。|We postponed departure by half an hour.|演出推迟到下周六了。|The performance has been postponed to next Saturday.
''')
D=rows('''
周六去公园的事，你问过大家了吗？|Have you asked everyone about going to the park on Saturday?
问了，现在四个人都能来。还是下午四点见？|Yes, all four can come. Shall we still meet at four in the afternoon?
可以，不过天气预报说可能下雨。|That works, but the forecast says it may rain.
既然这样，我再找个室内的地方。你的活动室能借吗？|In that case, I’ll look for an indoor place too. Could we borrow your activity room?
我问问。不管下不下雨，时间都不变，对吧？|I’ll ask. The time stays the same whether it rains or not, right?
对。今天晚上尽快告诉我，我好发消息给大家。|Right. Let me know as soon as you can tonight so I can message everyone.
吃的东西谁准备？上次你一个人做太多了。|Who’s getting the food ready? Last time you did too much on your own.
这次每个人带一道菜。我带面包，你替我买点水果行吗？|This time everyone brings a dish. I’ll bring bread. Could you buy some fruit for me?
行。买完把钱告诉你，我们四个人一起分。|Sure. I’ll tell you what it cost, and we’ll split it among the four of us.
好。费用包括水果和饮料，自己做的菜就别算了。|Good. We’ll split the cost of fruit and drinks, but not the dishes people make themselves.
那我买完再来帮你布置，别又一个人忙。|Then I’ll help you set up after shopping. Don’t do everything alone again.
知道了。这次我只负责带面包，以及提醒你别迟到。|I know. This time I’m only in charge of bringing bread—and reminding you not to be late.
''')
R=rows('''
星期六的天气比预报的还差。三点半，我看见窗外下着大雨，赶紧问群里是不是要取消。|Saturday’s weather was even worse than forecast. At half past three I saw heavy rain outside and quickly asked the group whether we should cancel.
林安回复说：“不用取消，我们改在活动室见，还是四点。门口有一把伞，谁先到谁先用。”|Lin An replied, “No need to cancel. We’re meeting in the activity room instead, still at four. There’s an umbrella at the door; whoever arrives first can use it.”
我到的时候，陈宇已经把桌子布置好了。桌上除了水果和饮料，还有每个人自己做的菜。|When I arrived, Chen Yu had already set the table. Besides fruit and drinks, it held dishes each person had made.
大家先吃东西，后来把桌子搬到一边，一起玩游戏。四个人当中，只有我不懂规则，他们就先玩了一轮给我看。|We ate first, then moved the table aside and played a game together. I was the only one of the four who didn’t know the rules, so they played a round to show me.
水果和饮料一共花了一百四十块。我们按四个人分，每人三十五块。陈宇说钱不用急着转，回家以后有空再转就行。|The fruit and drinks cost 140 yuan altogether. Divided among four people, that was 35 each. Chen Yu said there was no rush to transfer it; we could do it after getting home.
后来，一个朋友临时要回去照顾孩子，先走了。我们没把她留下，也没因为少了一个人就提前结束。|Later, something came up and one friend had to go home to look after her child. We didn’t make her stay or end early just because one person had left.
那天没有去成公园，但我没有失望。大家根据天气换了地方，也把准备工作分开承担了，谁都没忙得吃不上饭。|We didn’t get to the park that day, but I wasn’t disappointed. We changed venue because of the weather and shared the preparation, so nobody was too busy to eat.
''')
M=rows('''
你再三说别迟到，自己怎么还没到？|You kept telling us not to be late. How come you’re not here yet?
我到楼下了，面包太多，电梯还坏了。|I’m downstairs. There’s too much bread, and the lift is broken.
你不是说只带一点吗？|Didn’t you say you’d only bring a little?
买的时候饿了，越买越多。|I was hungry while shopping and kept buying more.
别爬楼了，我下来替你拿一半。|Don’t start climbing. I’ll come down and carry half for you.
那你带把伞，门外雨可大了。|Then bring an umbrella. It’s really raining outside the entrance.
好。今天谁都不许说“就一点”。|Okay. Today nobody’s allowed to say “just a little.”
等你看到面包再说吧，的确不少。|Wait until you see the bread. There really is quite a lot.
''')
G=[
card('既然…就…','Use an accepted fact as the basis for a decision','既然 presents a fact both sides can accept; 就 introduces the consequent decision. A merely hypothetical future condition is better introduced with 如果.','既然大家都能来，我们就定周六吧。|Since everyone can come, let’s choose Saturday.\n既然下雨了，我们就在室内见。|Since it’s raining, let’s meet indoors.','既然明天也许下雨，我们已经确定下雨了。','如果明天下雨，我们就在室内见。','A possible future condition is not an established fact.'),
card('无论 / 不管…都…','Keep a result constant across alternatives','The first clause supplies alternatives or a question-word range. 都 states the unchanged result. This pattern does not erase practical exceptions unless the speaker actually includes them.','无论下不下雨，我们都四点见。|Rain or no rain, we’ll meet at four.\n不管谁先到，都在门口等一下。|Whoever arrives first should wait a moment at the door.','无论下雨，我们都四点见。','无论下不下雨，我们都四点见。','下雨 alone is not a range or pair of alternatives here.'),
card('否则','State the unwelcome consequence of not doing something','The first clause gives the action or condition; 否则 introduces what happens if it is not met. It often fits a warning or reminder.','先告诉大家换了地方，否则有人会走错。|Tell everyone the venue changed or someone will go to the wrong place.\n早点出发，否则会迟到。|Leave early or you’ll be late.','先告诉大家换了地方，否则他们就知道了。','先告诉大家换了地方，否则有人会走错。','Knowing the new venue follows informing people; it is not the consequence of failing to tell them.'),
card('替 + person + action','Perform an action on someone’s behalf','替 identifies whose task you take over or whom you help. It does not by itself mean the person gave you permission to make unrelated decisions.','你替我买点水果，行吗？|Could you buy some fruit for me?\n她替同事上了一天班。|She covered a day of work for her colleague.','我买替你水果。','我替你买水果。','替 plus the person goes before the action.'),
]
spec=dict(title=('A plan that survives the rain','下雨也能聚在一起'),goals=['Coordinate a shared plan and backup venue','State what changes and what stays fixed','Share preparation and costs without assigning everything to one person'],vocabulary=V,grammar=G,dialogue=(D,[q('gist','What is the group planning?','A four-person gathering with shared food','A public cooking competition','A cancelled trip abroad'),q('detail','Which costs will be divided?','Fruit and drinks','Every homemade dish','Only bread'),q('inference','Why look for an indoor place too?','The weather forecast suggests rain','Nobody likes the park','The time has already been postponed')]),reading=(R,[q('gist','How did the gathering turn out?','It moved indoors and still worked well','It was cancelled before anyone arrived','Everyone stayed outside in the rain'),q('detail','How much does each person owe for fruit and drinks?','35 yuan','140 yuan','70 yuan'),q('inference','Why does the narrator see the preparation as successful?','The work was shared and everyone could eat','One host did all the work without eating','No food or drinks were purchased')]),mediaTitle='Just a little bread',media=(M,[q('detail','What practical problem holds up the friend?','Too much bread and a broken lift','They have lost all the food','They are at the wrong park'),q('inference','What does the other friend offer?','Carry half the bread upstairs','Cancel the meal immediately','Buy even more bread first')]),glosses=[('室内','indoors'),('活动室','activity room'),('天气预报','weather forecast'),('规则','rules'),('转','transfer money here'),('电梯','lift; elevator'),('爬楼','climb the stairs')],place='Planning with friends',context='Rain may change the venue, but the group wants to meet at the agreed time.',turns=[('如果下雨呢？','What if it rains?','Offer the backup venue',['如果下雨，我们就在活动室见。']),('费用怎么分？','How will we divide the costs?','Divide fruit and drink costs among four people',['水果和饮料的钱，我们四个人一起分。']),('要不要我来帮你？','Would you like me to help?','Ask for one concrete piece of help',['好啊，你替我买点水果吧。'])],usage=[('Give a concrete fallback','如果下雨，我们换到室内，时间不变。','If it rains, we’ll move indoors; the time stays the same.','A venue change and a cancellation are different actions.'),('Ask for manageable help','你能替我拿一半吗？','Could you carry half for me?','The bounded request makes the practical task clear.')],tasks=practice([(D[4][0],D[4][1],'The proposed meeting time changes if it rains.',False,'The speaker asks to keep the time unchanged.'),(R[4][0],R[4][1],'Each of four people owes 35 yuan.',True,'140 divided by 4 is 35.')],[('我一个人准备不过来，面包和水果还没买。','I cannot prepare everything alone; we have not bought bread or fruit yet.',['我们分一下，你负责面包，我买水果。','面包水果都买好了，不用分工。','我们还没准备，但大家已经吃完了。'],0,'The reply divides the actual preparation tasks.'),('我们说下雨就改活动室，时间还是四点。现在下雨，要取消吗？','We agreed to use the activity room if it rains, still at four. Now it is raining. Should we cancel?',['不用，改在活动室见，还是四点。','不用，按刚才安排改成明天六点。','对，原来的安排是下雨就取消。'],0,'The backup changes venue but preserves the agreed time.')],[('早点出发，否则会迟到。','Leave early or you’ll be late.','否则'),('她替同事上了一天班。','She covered a day of work for her colleague.','替')],[[(V[i][3],V[i][4]) for i in [1,7,8]],[(V[i][5],V[i][6]) for i in [9,13,15]]]),review='Native review: light exaggeration in the bread exchange, 以及 inside a joking list, money-transfer wording. Arithmetic checked: 140/4=35. Time remains four; only the venue changes. Independent formal vocabulary examples are not forced into the friends’ speech.')
spec['glosses'].extend([('伞','umbrella'),('壶','pot; kettle')])
write(4,3,spec,publish='--publish' in sys.argv)
