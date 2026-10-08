"""Explain a time-budget trade-off without treating friendship as lost time."""
import sys
from advanced_core import write,rows,words,q,card,practice
V=words('''
不利|unfavourable; disadvantageous|bất lợi|每天睡得太晚，对第二天的学习不利。|Sleeping too late every day is bad for the following day’s study.|只看一个人的意见，对讨论不利。|Considering only one person’s view is unhelpful for the discussion.
犹豫|hesitate|do dự|我犹豫要不要每次都参加。|I’m unsure whether to join every time.|他犹豫了一会儿，还是问了时间。|He hesitated briefly but still asked about the time.
预期|expectation|kỳ vọng|计划太满，结果常和预期不同。|When the plan is too full, the result often differs from expectations.|我们没有达到预期，但知道了问题在哪。|We didn’t meet expectations but learned where the problem was.
充足|sufficient; ample|đầy đủ|我需要留出充足的休息时间。|I need to leave enough time to rest.|活动前，大家准备了充足的水。|Everyone prepared plenty of water before the event.
不足|insufficient; shortcoming|không đủ; thiếu sót|睡眠不足的时候，我很难听进去。|When I haven’t slept enough, I struggle to take things in.|这个方案的不足是回家太晚。|This plan’s drawback is getting home too late.
减轻|reduce; ease|giảm bớt|少安排一个晚上，能减轻一点压力。|Scheduling one fewer evening can ease the pressure a little.|她帮我分担任务，减轻了我的负担。|She shared the tasks and lightened my load.
效率|efficiency|hiệu suất|不是坐得越久，效率就越高。|Spending longer seated doesn’t necessarily make you more efficient.|我们把重复的步骤合在一起，提高了效率。|We combined repeated steps and improved efficiency.
精力|energy|sức lực|我晚上没有那么多精力。|I don’t have that much energy in the evening.|这件事花了她很多精力。|This took a lot of her energy.
节省|save; economise|tiết kiệm|早点把地点说清楚，能节省找路的时间。|Clarifying the location early can save time finding the way.|我想节省路上的时间，不是省掉见朋友。|I want to save travel time, not cut out seeing friends.
投入|put in; invest time or effort|đầu tư|这段练习已经投入不少时间。|I’ve already put quite a lot of time into practising this section.|她做事很投入，没听见我进来。|She was so absorbed in the task she didn’t hear me come in.
有限|limited|có hạn|时间有限，我得先选最想做的。|With limited time, I need to choose what I most want to do first.|座位有限，晚来的人只能站一会儿。|Seats were limited, so late arrivals had to stand for a while.
长期|long term|dài hạn|我想找一个能长期继续的办法。|I want a method I can sustain long term.|长期不见面，不等于没有联系。|Not meeting for a long time doesn’t mean losing contact.
短期|short term|ngắn hạn|这是短期调整，不是以后都不去了。|This is a short-term adjustment, not never going again.|短期看不出变化，我还想再试两周。|I can’t see a change in the short term and want two more weeks.
范围|range; scope|phạm vi|今天先把练习范围缩小到两段。|Let’s limit today’s practice to two sections.|这次活动的范围比上次大。|This event covers a wider scope than the previous one.
收获|gain; what one gets from an experience|thu hoạch|我今天的收获是终于和新朋友聊起来了。|My gain today was finally chatting with a new friend.|看完以后，你最大的收获是什么？|What did you get most from watching it?
调整|adjust|điều chỉnh|试两周以后，我们再调整时间。|After trying it for two weeks, we’ll adjust the schedule.|我把练习顺序调整了一下。|I changed the order of the practice a little.
规律|regular pattern; regularity|quy luật; đều đặn|我想把作息变得规律一点。|I want a slightly more regular routine.|我还没找到他说话的规律。|I haven’t found the pattern in his speech yet.
自觉|self-aware; act of one’s own accord|tự giác|没人提醒，我也会自觉记下没听懂的地方。|Without a reminder, I note down the parts I don’t understand.|大家自觉把椅子放回去。|Everyone put the chairs back without being asked.
坚持|persist; keep doing|kiên trì|我想坚持练，不是每次都练到没力气。|I want to keep practising, not exhaust myself each time.|她坚持先听完，再给意见。|She insisted on listening to the end before giving feedback.
方案|plan; proposed approach|phương án|这个方案保留了周六见面的时间。|This plan keeps Saturday available for meeting.|我们比较了两个方案，选了路上更近的。|We compared two plans and chose the nearer route.
压力|pressure|áp lực|把每个晚上都安排满，我反而有压力。|Filling every evening actually puts pressure on me.|你不用为了减轻我的压力，假装事情很容易。|You don’t need to pretend it’s easy to take pressure off me.
独立|independent; independently|độc lập|有些内容我能独立练，有些需要一起聊。|Some things I can practise independently; others need conversation.|她已经能独立完成这个任务。|She can now complete the task independently.
目标|goal|mục tiêu|我的目标是能参加聊天，不只是做完题。|My goal is joining conversations, not just finishing questions.|这个月的目标先定小一点。|Let’s set a smaller goal for this month.
合理|reasonable|hợp lý|这个安排听起来合理，但得试了才知道。|This schedule sounds reasonable, but we’ll need to try it.|你可以不同意，也可以问这个决定是否合理。|You can disagree and ask whether the decision is reasonable.
''')
D=rows('''
这周三次活动你都来吗？|Are you coming to all three activities this week?
我想来，不过周一和周三已经有课，三个晚上再出门有点多。|I’d like to, but I already have classes Monday and Wednesday. Three more evenings out is a lot.
周二看电影，周四唱歌，周六吃饭，你最想留哪个？|Film Tuesday, singing Thursday, dinner Saturday. Which do you most want to keep?
周六吧。我上次一直听，想这次跟大家聊起来。|Saturday. Last time I mostly listened; I’d like to chat with everyone this time.
那电影和唱歌都先不来了？|So are you skipping both the film and singing for now?
电影这周先不去，唱歌我隔周来一次，行不行？|I’ll skip the film this week and come to singing every other week. Would that work?
当然。你不用每次都到。|Of course. You don’t have to be there every time.
我就是怕不常来，大家很快就不认识我了。|I’m worried that if I don’t come often, everyone will quickly forget me.
上次那个来得最少的人，你还记得吧？|You remember the person who came least often last time, don’t you?
记得，那个会给每道菜起名字的。|Yes, the one who gave every dish a name.
对，我们也记得你把辣椒当青菜的那次。|Right. And we remember the time you mistook the chilli for a green vegetable.
这个记忆能不能删掉？|Could you delete that memory?
不能。不过下次我先提醒你。|No. But next time I’ll warn you first.
谢谢，终于有一点实际帮助。周六我六点到，八点半回去。|Thanks, finally some practical help. I’ll arrive at six Saturday and head home at half eight.
太早了吗？我们一般聊到九点。|Is that too early? We usually talk until nine.
我第二天想早点练，路上还要半小时。先试两周吧。|I’d like to practise early the next day, and the journey takes half an hour. Let’s try it for two weeks.
好，要走就说一声，不用等大家一起。|Okay. Let us know when you leave; no need to wait for everyone.
那我先这样安排，不把下个月也一次定死。|I’ll schedule it like that for now without fixing all of next month at once.
''')
R=rows('''
朋友发来三次活动的时间，我看了一眼就想全部答应。周二有电影，周四唱歌，周六吃饭，都不是我讨厌的事情。而且我学中文本来就想和人聊，不想只在家做题。可是打开日历，周一和周三已经有课，如果另外三个晚上都出去，这周只剩一个工作日晚上没有安排。|My friend sent three activities and I wanted to accept all of them: a Tuesday film, Thursday singing and Saturday dinner. I liked them all and was learning Chinese to talk with people, not just do exercises. But Monday and Wednesday already had classes; adding three evenings out would leave only one weekday evening free.
上个月我试过把时间安排满。课前赶着吃饭，活动结束又在车上补练习，回家以后还觉得当天没做够。最晚的一次，我快十二点才睡，第二天看见熟悉的字也读得很慢。我不能只算每个活动有多有用，却不算路上和休息需要的时间。坐在那里很久，也不等于一直在认真听。|Last month I had tried a packed schedule: rushing meals, finishing exercises in transit and still feeling I hadn’t done enough. One night I slept near midnight and read familiar characters slowly the next day. I needed to count travel and rest, not just the apparent value of each activity. Sitting a long time did not mean listening attentively throughout.
我跟朋友说，想先留下周六吃饭。上次我只跟熟悉的人说话，这次想问新朋友平时看什么、怎么选活动，再讲讲自己最近看的短剧。电影当然也有意思，但这一周我更想把见面以后不敢开口的问题放在前面。这是我现在的目标，不是说看电影没有收获，也不是要大家都按我的目标选。|I kept Saturday dinner first. Last time I talked only to familiar people; this time I wanted to ask newcomers about what they watched and how they chose activities, then discuss a drama. This week I prioritised speaking at gatherings. That didn’t make films worthless or require everyone to share my goal.
唱歌活动我想隔周参加。自己在家能把两句慢慢读清楚，到了现场再问别人哪里没听懂。我不准备把所有独立练习都搬到活动里，也不把活动当作没人说话的教室。朋友说，可以练，也可以聊天，大家来这里并不是为了给我上一整节课。我觉得这个提醒很有用。|I planned singing every other week: practise two lines as speech at home, then ask what others couldn’t understand at the event. I wouldn’t move all solo practice into the gathering or make it a silent classroom. My friend reminded me people came to chat too, not give me a full lesson. That was helpful.
周六我决定六点到，八点半离开。朋友说一般聊到九点，我知道会少听最后半小时，但也想留出回家的路程。坐车半小时，九点左右到家，我还有时间收好东西，再睡觉。我们没有把这个安排说成最好的办法，只约好先试两周，看看我是不是仍然太累，也看看见面有没有真的聊起来。|I would arrive Saturday at six and leave at 8:30, knowing I’d miss the final half hour of their usual conversation. With a half-hour journey I’d be home around nine and have time to settle before bed. We didn’t call it the best method; we’d try two weeks and see whether I was still tired and actually joining conversations.
第一次照着这个安排去，我真的和一个新朋友说了几句。她问我为什么最近看短剧，我说长的先听不住，短的能再看一遍。她推荐了自己的方法，我没有当场答应全部照做，先记了最想试的一点。八点半时我说要走，她没有觉得我不喜欢大家，还问下周是不是也来。|The first time, I talked to a new friend. Asked why I watched short dramas, I explained I couldn’t sustain attention on longer ones and could replay short ones. I noted one of her suggestions rather than promising to adopt all of them. At 8:30 I left; she didn’t interpret it as dislike and asked about next week.
第二周有一天加班，我在群里说那周唱歌不去，周六仍然想来。以前我会觉得计划改了就是没坚持，这次我把坚持理解成继续找能做到的安排。两周以后，电影、唱歌和吃饭都还在朋友的计划里，我没有失去选择，只是没有在同一周把所有选择都做完。|Overtime in week two led me to skip singing while still planning Saturday. I used to treat any schedule change as failed persistence; now it meant continuing to find workable arrangements. After two weeks the activities remained available. I had not lost my choices; I simply hadn’t tried every choice in one week.
''')
P=rows('''
我邀请朋友来活动，是想和他见面，不是想替他的日历做决定。他一开始说三个都想来，我很高兴，后来又说晚上已经有课。我差点回一句“反正出来也是练中文”，可想了一下，练中文并不能让路程变短，也不能让一个晚上多出几个小时。喜欢一件事，不代表什么时候做都合适。|I invited my friend to see him, not to decide his calendar. I was pleased he wanted all three events, then learned he had evening classes. I nearly said going out was Chinese practice anyway, but practice didn’t shorten travel or add hours to an evening. Enjoying an activity didn’t make every time suitable.
我们把活动一个一个说清楚。电影那天结束比较晚，唱歌可以只来一段，吃饭一般从六点聊到九点。他选吃饭，不是因为其他两个没有意思，而是想多和新朋友说话。我原来以为他最喜欢唱歌，听他说完才知道，喜欢和这周最想解决的问题不一定是同一个答案。|We discussed each event: a late film finish, an optional shorter singing visit and dinner from six to nine. He chose dinner to speak to new people, not because the others were uninteresting. I’d assumed singing was his favourite. Hearing him out showed a favourite and the most pressing goal could differ.
他说八点半走，我先问会不会太早。后来听见路上还要半小时，我就没有继续劝他留下。大家聊到九点，是我们常见的安排，不是每个人都必须遵守的结束时间。下次有人晚到，也不代表要让全桌的人跟着晚走。先把自己的时间说出来，比到了门口才突然着急更容易一起安排。|I initially asked whether 8:30 was too early, then heard about the half-hour trip and stopped urging him to stay. Nine was our usual finish, not a compulsory one. A late arrival didn’t require everyone to leave later. Stating availability early helped coordination more than suddenly rushing at the door.
那晚他坐在新朋友旁边，刚开始还是我先介绍。后来他们聊到看短剧，他就自己问了两个问题。我没有一直替他补句子，也没有在每次停下来时马上换成另一种语言。有一处他找不到词，我问是不是想说听得累，他点头，又用自己的方式说完。别人回答时，我也留在旁边听。|That evening I introduced him to someone new. When short dramas came up, he asked two questions himself. I didn’t finish all his sentences or immediately change languages at every pause. When he searched for a word, I checked whether he meant listening fatigue; he agreed and finished in his own way. I stayed to hear the reply too.
八点半，他站起来说先回去，感谢大家推荐。我只提醒他别忘了外套，没有再说“再坐十分钟”。这不是我突然不想见他，而是我们前面已经说好。他走后，还有人聊到九点，也有人九点以前走。一个朋友说，他下次也想早点来，原来只来前半段并不会错过所有聊天。|At 8:30 he thanked everyone and left. I reminded him about his coat rather than urging ten more minutes. We had already agreed; it didn’t mean I no longer wanted to see him. Others left at various times. Someone said they’d try coming early, having seen that a shorter visit didn’t mean missing all conversation.
第二周他发消息说加班，唱歌那次不来。我没有把这句话理解成以后再也不来，只回他工作结束早点休息，周六的地点还一样。他周六问能不能带自己做的一点吃的，我们一起问了人数。这些联系也发生在活动外面，并不只有人坐在椅子上的时间才算我们认识。|In week two he messaged that overtime meant missing singing. I didn’t take it as a permanent departure; I wished him rest and confirmed Saturday’s venue. He later offered food, and we checked numbers. Contact happened outside gatherings too, not only while people were seated there.
两周以后，我问这个安排要不要改。他说周六想继续，唱歌隔周来，电影以后有合适的再约。我把这些记在邀请消息里，没有替他答应下个月的每一场。我们仍然想一起玩，也仍然有自己的时间。能把这些说清楚，反而让我发邀请时更轻松，不用猜他没来是不是因为不想见我们。|After two weeks he kept Saturday and alternate-week singing, leaving films for suitable occasions. I noted that without accepting next month’s every event on his behalf. We wanted time together and time of our own. Clarity made invitations easier; I no longer had to guess whether absence meant not wanting to see us.
''')
M=rows('''
你又做时间表了？|You’ve made another timetable?
这次没有把每一分钟都填满。|This time I haven’t filled every minute.
上次连吃饭都写十五分钟。|Last time you allowed fifteen minutes even for dinner.
我现在知道十五分钟不够听你给菜起名字。|Now I know fifteen minutes isn’t enough to hear your names for the dishes.
那你给聊天留了多久？|How long did you leave for chatting?
两小时半，六点到八点半。|Two and a half hours, six to half eight.
要是讲到一半呢？|What if you’re halfway through a story?
那我就说，下周再讲。|Then I’ll say I’ll finish next week.
你这样比短剧还会让人等。|You’re better than a short drama at making people wait.
谢谢，这是我今天的收获。|Thanks. That’s what I got out of today.
不算表扬。|That wasn’t praise.
我知道，我也没放进成绩表。|I know. I didn’t put it in my marks sheet either.
''')
G=[
card('既然…，就…','Connect a known condition to a proposed decision','既然 treats the first point as accepted information; 就 introduces a response to it. It can propose a decision without making that decision universal.','既然周一有课，就先不加活动了。|Since there is class on Monday, let us not add an activity then.\n既然路上要半小时，就给回家留点时间。|Since the trip takes half an hour, leave some time to get home.','既然周一有课，但是就先不加活动了。','既然周一有课，就先不加活动了。','For this reason-to-decision pair, use 就; do not insert a contrasting 但是.'),
card('除非…，否则…','Set an exception to a default intention','除非 names the exception; 否则 introduces what will hold if it does not arise. Distinguish this from 除非…才…, where a condition is necessary for an action.','除非临时加班，否则我周六会来。|Unless overtime comes up, I will come Saturday.\n除非时间改了，否则我还是六点到。|Unless the time changes, I will still arrive at six.','除非临时加班，否则我一定永远不用上班。','除非临时加班，否则我周六会来。','The stated exception concerns this Saturday, not all future work.'),
card('V下去','Describe continuation rather than direction','With an ongoing activity, 下去 can mean continue. It need not describe moving physically downward.','我想用这个办法练下去。|I want to keep practising this way.\n这样忙下去，我怕坚持不了。|If I keep being this busy, I fear I cannot sustain it.','我想练下去，所以必须到楼下。','我想用这个办法练下去。','The complement indicates continued practice, not a required location downstairs.'),
card('…为的是…','Make a purpose explicit','为的是 introduces the intention behind an action. Achieving that intended result is a separate question.','我留出周六，为的是和大家聊起来。|I keep Saturday available in order to start talking with everyone.\n先读两句，为的是到现场能问清楚问题。|I read two lines first so I can ask clearly about them at the event.','我留出周六，为的是和大家聊起来，所以已经聊得很好。','我留出周六，为的是和大家聊起来。','A purpose does not by itself establish that the desired result has happened.'),
card('不是…就…','Describe an exhaustive pair in a particular context','不是A就是B can present two alternatives covering the relevant possibilities. Use it only when the situation really supports that restriction.','这两周的周四，我不是上课就是唱歌。|On Thursdays these two weeks I am either at class or singing.\n今晚不是在家练，就是去活动。|Tonight it is either practice at home or the event.','我不是参加就是不参加，所以每天都只能有两种生活。','今晚不是在家练，就是去活动。','Restrict the alternatives to this evening; two stated options do not cover all of life.'),
]
spec=dict(title=('A plan with room for friends','不是每一次，都要到'),goals=['Explain a realistic trade-off between study, rest and social plans','Offer a limited commitment without implying permanent withdrawal','Compare personal gains and the costs of a packed schedule'],vocabulary=V,grammar=G,
dialogue=(D,[q('gist','What does the learner settle on?','Saturday dinner and alternate-week singing','All three activities every week indefinitely','No contact with friends again'),q('detail','What time will the learner leave Saturday dinner?','8:30','Six when it begins','Midnight'),q('inference','Why try two weeks rather than fix next month?','To see whether the plan actually fits energy and conversation goals','To prove all activities are useless','To prevent any later adjustment')]),
reading=(R,[q('gist','How does the narrator rethink persistence?','Continuing workable arrangements rather than filling every evening','Never changing any plan once written','Finishing all choices in the same week'),q('detail','How long is the journey home?','Half an hour','Three hours','Five minutes'),q('inference','Why prioritise dinner this week?','To practise joining conversations with new people','Because films can never help language learning','Because friends have banned singing')]),
pairedTitle='The friend sending the invitations',pairedReading=(P,[q('gist','What makes invitations easier for the friend?','Clear preferences and availability without guessing absence means dislike','Deciding every evening for the learner','Requiring every participant to leave together'),q('detail','What does the host do at 8:30?','Reminds the learner about the coat without pressing them to stay','Cancels all future dinners','Rewrites the learner’s timetable without asking'),q('inference','What does the host learn about a favourite activity?','It need not match the goal someone prioritises this week','It must be attended every time','It guarantees a particular examination result')]),
mediaTitle='An unfinished dinner story',media=(M,[q('detail','How long is set aside for chatting?','Two and a half hours','Fifteen minutes','Half an hour'),q('inference','What does the short-drama comparison tease?','Leaving a story unfinished until next week','An actual examination award','The end of the friendship')]),
glosses=[('作息','daily routine of work and rest'),('省掉','omit; save by removing'),('负担','burden'),('睡眠','sleep'),('补练习','catch up on exercises'),('课前','before class'),('疲劳','fatigue'),('隔周','every other week'),('路程','journey; travel distance'),('加班','work overtime'),('缩小','reduce in scope'),('定死','fix rigidly'),('日历','calendar'),('辣椒','chilli pepper'),('青菜','green leafy vegetables'),('成绩表','marks sheet'),('遵守','observe a rule or agreement'),('熟悉','familiar'),('前半段','first half'),('推迟','postpone')],
place='Planning the week with a friend',context='Three social activities compete with two class evenings and a need for rest. The learner proposes a two-week trial.',
turns=[('三个活动你都来吗？','Are you coming to all three?','Choose and explain',['这周先来周六吃饭，唱歌隔周来，电影先不去。']),('不多留半小时吗？','Won’t you stay another half hour?','State a friendly departure boundary',['我八点半先走，路上还要半小时，下次再接着聊。']),('那以后都这样？','Is that how it will always be?','Limit the commitment',['先试两周，再看要不要调整。'])],
usage=[('Limit without rejecting','这次先不去，下次有合适的再约。','I’ll skip this one; let’s arrange another suitable occasion.','A bounded refusal need not mean ending contact.'),('Say what you want to preserve','我想留出周六，和大家好好聊。','I want to keep Saturday free to have a proper chat.','Give a positive priority rather than only listing constraints.'),('Leave at the agreed time','我先回去了，下次接着听你讲。','I’ll head home now; I’ll hear the rest next time.','State the departure and keep the social thread open.')],
tasks=practice(
[(D[5][0],D[5][1],'The learner proposes singing every other week.',True,'隔周来一次 states the frequency.'),(R[4][0],R[4][1],'The learner expects to be home around nine.',True,'Departure at 8:30 plus a half-hour journey.'),(P[4][0],P[4][1],'The friend pressures the learner to stay ten more minutes.',False,'The host explicitly does not do that.'),(R[6][0],R[6][1],'An overtime day leads the learner to abandon every future activity.',False,'They skip singing that week while keeping Saturday.')],
[('你说先试两周，周六还来。是以后都不来了？','You proposed a two-week trial and still coming Saturday. Does that mean never coming again?',['不是，先试两周，周六还是想来。','对，我刚才答应以后每场都不来。','对，先试两周就是永久停止见面。'],0,'The reply corrects a permanent interpretation of a temporary adjustment.'),('现在八点半，你想九点到家，路上半小时。还坐十分钟吗？','It is 8:30. You want to be home at nine, and the trip takes half an hour. Stay ten more minutes?',['今天先回去吧，下次再听你讲。','再坐十分钟，九点正好到家。','等九点出发，还是九点到家。'],0,'A personal departure leaves others free to continue.'),('我们还没试这个安排，已经知道一定最好了吗？','We have not tried this schedule. Do we already know it is definitely the best?',['还不知道，先试两周再调整。','已经试过两周，结果完全证明了。','没试也能确定，实际情况不用看。'],0,'Trial and observation are distinct from guaranteeing success.')],
[('除非临时加班，否则我周六会来。','Unless overtime comes up, I will come Saturday.','否则'),('我想用这个办法练下去。','I want to keep practising this way.','下去'),('我需要留出充足的休息时间。','I need to leave enough time to rest.','充足')],
[[(V[i][3],V[i][4]) for i in [0,2,5]],[(V[i][5],V[i][6]) for i in [7,12,16]],[(V[i][3],V[i][4]) for i in [14,20,22]]]),
review='Native review: teasing about dish names and short-drama suspense, limited invitations and departure register, 不是A就是B context and 为的是 purpose. Classes Monday/Wednesday, film Tuesday, singing Thursday, dinner Saturday; dinner six to nine, learner leaves 8:30 and travels half an hour. The two-week trial is an individual fictional arrangement, not a sleep prescription or guaranteed learning method. The host’s participation is friendship, not unpaid full-time tutoring.')
spec['glosses'].extend([('步骤','step in a process'),('劝','urge; persuade'),('讨厌','dislike; find annoying')])
write(5,5,spec,publish='--publish' in sys.argv)
