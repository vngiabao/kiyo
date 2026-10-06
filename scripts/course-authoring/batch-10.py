"""Editorial source: weather alternatives, hosting roles, routes and first meetings."""
from common import *
character_groups.update({
's2-u17':[('必','must; certainly'),('须','must; need'),('春','spring'),('夏','summer'),('秋','autumn'),('冬','winter'),('晴','clear weather'),('阴','overcast; shade'),('雪','snow')],
's2-u18':[('办','to handle; organize'),('报','to report; register'),('称','to call; name'),('单','single; list'),('举','to lift; raise'),('队','team'),('篮','basket'),('排','row; to arrange'),('运','to move; transport')],
's2-u19':[('往','towards'),('向','towards; direction'),('街','street'),('广','wide'),('园','garden; park'),('市','city; market'),('铁','iron'),('船','boat'),('骑','to ride')],
's2-u20':[('碰','to touch; meet by chance'),('庭','courtyard; family'),('青','young; blue-green'),('久','long in time'),('长','to grow; long'),('当','to act as; at the time'),('共','together; common'),('加','to add; join'),('己','self')],
})
unit_glosses.update({
's2-u17':{'备选':'alternative','天气预报':'weather forecast','预报':'forecast','取消':'to cancel','室内':'indoors','室外':'outdoors','集合':'to gather','更新':'to update','雨天':'rainy day','场地':'venue','北方':'the north','南方':'the south','公园':'park','以来':'since; up to now','雨衣':'raincoat'},
's2-u18':{'轮流':'to take turns','主持':'to host; preside','签到':'to sign in','组织':'to organize','规则':'rule','负责人':'person responsible','自愿':'voluntary','轮换':'rotation','通知':'notice','健康':'health','篮球':'basketball','由':'by; assigned to'},
's2-u19':{'导航':'navigation','地铁':'metro','站台':'platform','路口':'intersection','转弯':'to turn','过河':'to cross a river','路线':'route','步行':'to walk','临时':'temporary','出口':'exit','关闭':'to close','安全':'safe','地图':'map','市区':'urban area','船':'boat','骑车':'to ride a bicycle'},
's2-u20':{'共同':'common; together','同意':'to agree','聚会':'social gathering','回忆':'to recall','偶然':'by chance','第一次':'first time','本科':'undergraduate','经历':'experience','家庭':'family','年纪':'age','情况':'situation'},
})
dictionary.update({'气温':'qì wēn','凉快':'liáng kuai','什么':'shén me','碰见':'pèng jiàn','那会儿':'nà huìr','时候':'shí hou','当时':'dāng shí','长大':'zhǎng dà','称':'chēng'})

u='s2-u17'
write(u,'下雨就换个地方',['Make a conditional backup plan','Distinguish certainty from a weather forecast','State a sufficient condition without making it a requirement'],[
('必须','must; be required to','phải','adverb','下雪以后路不好走，必须先问场地的情况。','After snow the route is difficult; we must first ask about the venue.'),
('差不多','approximately; almost','gần như; xấp xỉ','adverb','两条路的时间差不多，但不是完全一样。','The two routes take approximately the same time, but not exactly.'),
('如果','if','nếu','conjunction','如果明天下雨，我们就在室内见。','If it rains tomorrow, we will meet indoors.'),
('只要','as long as; provided that','chỉ cần','conjunction','只要你有空，就可以参加。','As long as you are free, you can take part.'),
('条件','condition','điều kiện','noun','有空是这里说的条件，不是说必须下雨。','Being free is the condition here; it does not mean rain is required.'),
('气温','air temperature','nhiệt độ không khí','noun','气温只有三度，我多带一件衣服。','The air temperature is only three degrees; I will bring another layer.'),
('多云','cloudy','nhiều mây','adjective','预报说多云，还没有说会下雨。','The forecast says cloudy; it has not said it will rain.'),
('晴','clear; sunny','quang; nắng','adjective','天晴了，也要先看场地有没有开。','It has cleared up, but we still need to check whether the venue is open.'),
('晴天','sunny day; clear weather','ngày nắng','noun','晴天我们在公园见。','In clear weather we meet at the park.'),
('阴','overcast','âm u','adjective','今天阴，但不一定下雨。','Today is overcast, but it will not necessarily rain.'),
('阴天','overcast day','ngày âm u','noun','阴天也可以出门，先看预报。','You can go out on an overcast day too; check the forecast first.'),
('下雪','to snow','tuyết rơi','verb','如果下雪，就不骑车。','If it snows, we will not ride bicycles.'),
('雪','snow','tuyết','noun','路上有雪，走路要小心。','There is snow on the road; walk carefully.'),
('春天','spring','mùa xuân','noun','春天我们常在公园见。','We often meet in the park in spring.'),
('夏天','summer','mùa hè','noun','夏天气温高，带水来吧。','Temperatures are high in summer; bring water.'),
('秋天','autumn','mùa thu','noun','秋天凉快，我想出去走走。','Autumn is pleasantly cool; I would like to go for a walk.'),
('冬天','winter','mùa đông','noun','冬天也能见面，可以选室内。','We can meet in winter too; we can choose indoors.'),
('北方','the north; northern region','miền bắc','noun','朋友住在北方，冬天常下雪。','My friend lives in the north, where it often snows in winter.'),
('南方','the south; southern region','miền nam','noun','我在南方长大，不太习惯雪天出门。','I grew up in the south and am not used to going out in snow.'),
('凉快','pleasantly cool','mát mẻ','adjective','这里凉快，不是很冷。','It is pleasantly cool here, not very cold.'),
('零下','below zero','dưới không độ','noun','明天气温可能到零下三度。','Tomorrow the air temperature may reach minus three degrees.'),
('云','cloud','mây','noun','天上有云，不等于一定下雨。','There are clouds in the sky; that does not mean rain is certain.')],
[grammar(u,'二19','必须 / 一定 / 差不多 / 好像 / 也许','Keep obligation, certainty and approximation separate',
'必须 states a requirement; 一定 expresses a firm expectation or commitment. 差不多 marks approximation, 好像 an impression and 也许 a possibility. A cloudy forecast does not license 一定下雨. Say 也许会下雨 when uncertain. 差不多三度 is approximate, not an exact measurement. Different words change the strength of the claim, not the evidence available.',[
('必须先看通知，不一定要去室外。','We must check the notice first; we do not necessarily have to go outdoors.'),('两条路差不多远，好像都能走。','The two routes are about equally far; it looks as though both are usable.'),('也许下雨，时间一确认，我一定告诉你。','It may rain; once the time is confirmed, I will definitely tell you.')],
('多云，所以一定下雨。','多云，也许会下雨。','Clouds alone do not make the forecast certain.')),
grammar(u,'二66','条件：如果 … 就 / … 的话，就 / 不用连词','Give a condition and its consequence',
'如果下雨，我们就在室内见 and 下雨的话，我们就在室内见 make the condition explicit. In a known plan 下雨就换地方 can omit 如果. The consequence only follows when that condition holds; this is not a claim that rain will occur. Keep the subject of each clause clear. State what stays fixed and what changes.',[
('如果明天下雨，我们就在室内见。','If it rains tomorrow, we will meet indoors.'),('下雨的话，就换到饭馆。','If it rains, change to the restaurant.'),('天晴就在公园见，时间不变。','If it is clear, meet at the park; the time stays the same.')],
('如果下雨，所以我们在室内见。','如果下雨，我们就在室内见。','如果 sets a condition; 所以 is a causal link and is not the paired condition marker here.')),
grammar(u,'二67','只要 … 就','Express a sufficient condition',
'只要有空，就可以来 says having time is enough for this invitation. It does not require bad weather, a gift or a particular season. Contrast 如果下雨，就在室内见: the condition chooses the venue, not whether the person is allowed to come. Do not confuse 只要 with 只有…才, which states a necessary condition and is taught separately later.',[
('只要你有空，就可以来。','As long as you are free, you may come.'),('只要场地开着，我们就按计划见。','As long as the venue is open, we will meet according to plan.'),('只要先发消息，就不用一直等。','As long as we message first, we need not keep waiting.')],
('只要下雨，你才可以来。','只要你有空，就可以来。','The invitation makes free time sufficient; it does not require rain or use 只要…才.'))],
text(u,'d','The plan changes location','Find the condition, fixed time and backup venue.',[
('明天还是七点见吗？','Are we still meeting at seven tomorrow?'),('对，时间不变。如果天晴，我们就在公园见。','Yes, the time stays the same. If it is clear, we will meet in the park.'),
('预报说多云，一定下雨吗？','The forecast says cloudy. Is rain certain?'),('不一定。好像会下雨，但现在只能说也许。','Not necessarily. It looks like rain, but for now we can only say maybe.'),
('下雨的话，就不见了吗？','If it rains, will we not meet?'),('不是，下雨就换到饭馆，还是七点。','No, if it rains we change to the restaurant, still at seven.'),
('我住得远，必须去吗？','I live far away. Must I go?'),('不用。只要你有空，就可以来；不方便也可以改天。','No. As long as you are free, you can come; if inconvenient, another day is fine.'),
('气温可能到零下三度，路上有雪怎么办？','The temperature may reach minus three. What if there is snow on the road?'),('那就先问场地有没有开，别急着出门。','Then first ask whether the venue is open; do not rush out.'),
('我明天下午再看通知。','I will check the notice tomorrow afternoon.'),('好，地方一确认，我一定发消息。','Good. Once the place is confirmed, I will definitely message.')],
[('mainidea','What changes if it rains?',['The venue, not the agreed seven-o’clock time','The meeting must be cancelled','Everyone must attend'],0),('detail','Does cloudy mean certain rain here?',['No, rain is only a possibility','Yes, it is certain','No, rain is impossible'],0),('inference','What should happen before going out in snow?',['Check whether the venue is open','Guess that it is open','Ride faster'],0)],drama=True),
text(u,'r','An afternoon update','Read to choose the venue without guessing the weather.',[
('我们明天七点见，时间不变。','We meet at seven tomorrow; the time is unchanged.'),('晴天在公园，雨天在饭馆。','In clear weather, at the park; in rain, at the restaurant.'),('今天的预报说多云，没有说一定下雨。','Today’s forecast says cloudy, not certain rain.'),('北方的朋友说冬天要小心路上的雪。','Our friend from the north says to watch out for snow on the road in winter.'),('南方的朋友觉得秋天更凉快。','Our friend from the south finds autumn more pleasantly cool.'),('春天和夏天也能见，天气不是参加的条件。','We can meet in spring and summer too; the weather is not a condition of participation.'),('只要有空，就可以来，不方便可以改天。','As long as you are free, you can come; another day is fine if inconvenient.'),('明天下午看更新，地方确认以后再出门。','Check the update tomorrow afternoon; leave once the venue is confirmed.')],
[('mainidea','What does the note organize?',['A meeting with a weather-dependent venue','A compulsory winter trip','A confirmed sunny forecast'],0),('detail','When is the next update checked?',['Tomorrow afternoon','Yesterday evening','After arriving'],0),('inference','Does participation require rain?',['No, having free time is enough','Yes, only rain permits attendance','Yes, snow is required'],0)],[(1,'晴天'),(6,'只要')]),
text(u,'media','Clouds are not a promise','Read the original short verse for the fixed plan and uncertain weather.',[
('天上有云，心里别急。','Clouds in the sky; do not be anxious.'),('春天换衣，夏天带水。','Change layers in spring; bring water in summer.'),('秋天凉快，冬天看雪。','Autumn is cool; in winter watch the snow.'),('如果下雨，就换地方。','If it rains, change the place.'),('只要有空，就来坐坐。','As long as you are free, come and sit a while.'),('七点不变，先看消息。','Seven stays fixed; check the message first.')],
[('mainidea','What stays fixed?',['Seven o’clock','Sunny weather','Attendance by everyone'],0),('detail','What happens in rain?',['The place changes','The time becomes eight','The meeting is certainly cancelled'],0),('inference','Is a cloud treated as a certain forecast?',['No','Yes','Only in summer'],0)],drama=False),
dict(tf=[('多云','预报说多云，不一定下雨。','The forecast says cloudy, not certain rain.','The speaker says rain is certain.',False,'不一定 denies certainty.'),('只要','只要有空，就可以来。','If you are free, you may come.','Having time is sufficient here.',True,'只要…就 gives a sufficient condition.')],
reply=[('如果','如果明天下雨呢？','What if it rains tomorrow?',['就在饭馆见，时间不变。','我在春天长大。','一共三度。'],0,'Supply the consequence of the condition.'),('必须','我明天不方便，必须来吗？','Tomorrow is inconvenient; must I come?',['不用，我们可以改天。','一定是晴天。','雪在天上。'],0,'Do not invent an obligation.')],
fill=[('差不多','两条路的时间差不多。','The two routes take about the same time.'),('凉快','秋天这里很凉快。','It is pleasantly cool here in autumn.')],
match=[('零下',[('零下三度。','Minus three degrees.'),('也许下雨。','It may rain.'),('时间不变。','The time stays unchanged.')]),('条件',[('有空是条件。','Free time is the condition.'),('云不是雪。','Cloud is not snow.'),('先看通知。','Check the notice first.')])]),
[('Conditional update','下雨的话，就在饭馆见。','If it rains, meet at the restaurant.','Keep the fixed time explicit.'),('Declining without pressure','不方便可以改天。','Another day is fine if inconvenient.','An invitation is not an obligation.')],
[('如果下雨呢？','What if it rains?','Give a backup location',['就在饭馆见。']),('我不方便，必须来吗？','It is inconvenient; must I come?','Allow another day',['不用，我们可以改天。'])],
'Native check: conditional omissions, 只要 sufficient-condition scope, weather-register collocations and clipped original seasonal verse. Forecast statements are uncertainty examples, not live weather guidance.')

u='s2-u18'
write(u,'今天你来当组长',['Agree a voluntary hosting role','State who organizes an activity and what it is for','Distinguish an action phrase from a completed event'],[
('当','to act as; work as','làm; đảm nhận','verb','今天我当组长，明天换人。','Today I act as group leader; tomorrow someone else takes a turn.'),
('办','to organize; handle','tổ chức; xử lý','verb','我们想办一个小活动。','We want to organize a small activity.'),
('报名','to register; sign up','đăng ký','verb','想参加的人先报名。','People who want to take part should sign up first.'),
('名单','list of names','danh sách tên','noun','名单上有五个人，不是全班。','There are five people on the list, not the entire class.'),
('名称','name; designation','tên gọi','noun','活动的名称是朋友见面。','The name of the activity is Friends Meet.'),
('目的','purpose','mục đích','noun','目的就是让大家有机会说汉语。','The purpose is to give everyone a chance to speak Mandarin.'),
('进行','to carry out; proceed','tiến hành','verb','活动在室内进行。','The activity takes place indoors.'),
('举行','to hold an event','tổ chức sự kiện','verb','星期六举行活动，地点还要确认。','The event is held on Saturday; the venue still needs confirmation.'),
('队','team','đội','noun','每队三个人，先问谁愿意参加。','There are three people per team; first ask who wants to join.'),
('队长','team captain','đội trưởng','noun','队长负责说明规则。','The captain is responsible for explaining the rules.'),
('球队','sports team; ball-game team','đội bóng','noun','我们不是正式球队，只是一起玩。','We are not an official sports team; we are just playing together.'),
('体育','physical education; sport','thể dục; thể thao','noun','体育活动也可以先说明怎么参加。','A sports activity can also start with an explanation of how to take part.'),
('体育场','sports ground; stadium','sân vận động','noun','体育场在外面，下雨就换地方。','The sports ground is outdoors; in rain we change venue.'),
('体育馆','sports hall; gymnasium','nhà thi đấu','noun','体育馆在室内，但要先问有没有开。','The sports hall is indoors, but we must first ask whether it is open.'),
('球场','court; playing field','sân bóng','noun','球场上已经有人，我们先等。','There are already people on the court; we wait first.'),
('球鞋','sports shoes','giày thể thao','noun','我带球鞋，也带一瓶水。','I bring sports shoes and a bottle of water.'),
('篮球','basketball','bóng rổ','noun','朋友喜欢篮球，不太会打网球。','My friend likes basketball but is not very good at tennis.'),
('排球','volleyball','bóng chuyền','noun','今天不打排球，先学新的词。','Today we are not playing volleyball; we first learn new words.'),
('网球','tennis','quần vợt','noun','想打网球的人在这边报名。','People who want to play tennis sign up here.'),
('运动','to exercise; sport','vận động; thể thao','verb','今天想运动的人可以参加小队。','People who want to exercise today can join a small team.'),
('举','to raise; lift','giơ; nâng','verb','不懂规则就举手问。','Raise your hand and ask if you do not understand the rules.'),
('举手','to raise one’s hand','giơ tay','verb','我举手是想问，不是说我一定当队长。','I raise my hand to ask, not to say I will definitely be captain.')],
[grammar(u,'二21','当','Name an agreed role',
'当组长/当队长 uses 当 as act as or serve as. 今天我当组长 describes a role; 我当过组长 adds experience, and 当时 gives a time in another construction. Do not infer willingness from a name on a list. Ask 可以吗 before assigning a role. Hosting is a responsibility, not a claim of higher ability.',[
('今天我当组长，你当队长。','Today I act as group leader and you as captain.'),('你愿意当负责人吗？','Would you like to be the person responsible?'),('我可以当组长，但先说明规则。','I can act as leader, but first explain the rules.')],
('我举手了，所以你一定当队长。','你愿意当队长吗？','One person raising a hand does not assign another person a role.')),
grammar(u,'二40','动词性词组','Read an action together with its object or purpose',
'办活动、举行活动、进行练习、参加球队 and 举手问问题 are action phrases. A phrase identifies an action but does not by itself say it is finished: 想办活动 is an intention. Keep verbs with appropriate objects; 举行 is used for an event, not a ball as an object. In 举手问问题 the first action enables the second. Distinguish the role 当组长 from the activity 办活动.',[
('我们想办活动，还没有举行。','We want to organize an event; it has not been held yet.'),('大家举手问问题。','Everyone raises a hand to ask questions.'),('队长先说明规则，再进行练习。','The captain first explains the rules, then carries out practice.')],
('我们举行篮球。','我们举行篮球活动。','举行 takes an event; 篮球 alone names the sport or ball rather than the event.'))],
text(u,'d','Who is hosting?','Find the agreed role and what registration actually means.',[
('星期六想办活动，谁来当组长？','We want to organize an event on Saturday. Who will lead?'),('我可以当，但先说活动的目的吧。','I can, but first tell me the purpose.'),
('让大家说汉语，也一起运动。','To let everyone speak Mandarin and exercise together.'),('名称就叫朋友见面，行吗？','Can we call it Friends Meet?'),
('行。报名以后一定要打篮球吗？','Fine. Does signing up mean we must play basketball?'),('不用，想参加哪队就先问。网球、排球都还没有确认。','No. Ask about the team you want to join; tennis and volleyball are not confirmed yet.'),
('名单上五个人，能组成两队吗？','There are five on the list. Can we form two teams?'),('先别分。今天每队三个人，人数还不够。','Not yet. Today each team needs three; there are not enough people yet.'),
('体育场下雨就不能用了吧？','We cannot use the sports ground in rain, right?'),('那就问体育馆有没有开，别先说一定能用。','Then ask whether the sports hall is open; do not say it is definitely available first.'),
('我刚举手，是想问规则，不是报名当队长。','I raised my hand to ask the rules, not to volunteer as captain.'),('知道了。谁愿意当队长，我们再问。','Understood. We will ask who wants to be captain.')],
[('mainidea','What does the group agree?',['A volunteer leader and a purpose, with details still to confirm','Five people already form two teams of three','Everyone must play basketball'],0),('detail','Why did the speaker raise a hand?',['To ask about the rules','To become captain','To cancel the event'],0),('inference','Is the sports hall definitely available?',['No, its opening must be checked','Yes, rain guarantees it','Yes, the list confirms it'],0)],drama=True),
text(u,'r','A voluntary small event','Read to separate plans, roles and completed actions.',[
('星期六我们想办一个小活动，名称是朋友见面。','We want to organize a small event on Saturday called Friends Meet.'),('目的是让大家有机会说汉语，也一起运动。','The purpose is to let everyone speak Mandarin and exercise together.'),('今天我当组长，负责看名单和说明规则。','Today I act as leader, responsible for checking the list and explaining rules.'),('名单上五个人，每队三个人，还不能分成两队。','There are five on the list; with three per team, we cannot make two teams yet.'),('报名不是答应当队长，举手也可能只是问问题。','Signing up is not agreeing to be captain; raising a hand may just mean asking a question.'),('体育场和体育馆都要先问有没有开。','We must check whether both the sports ground and sports hall are open.'),('篮球、排球、网球由参加的人一起商量。','Participants discuss basketball, volleyball and tennis together.'),('现在是计划，活动还没有举行。','This is a plan; the event has not happened yet.')],
[('mainidea','What kind of document is this?',['A voluntary event plan','A completed-game score report','A compulsory team assignment'],0),('detail','How many people are on the list?',['Five','Six','Three'],0),('inference','Does registration appoint a captain?',['No, agreement is separate','Yes, everyone is a captain','Yes, the first name must be captain'],0)],[(2,'组长'),(7,'举行')]),
text(u,'media','A hand raised','Follow the original scene’s correction of an assumption.',[
('你举手了，来当队长吧。','You raised your hand; be captain.'),('等一下，我只是想问。','Wait, I only wanted to ask.'),('问什么？规则还是地点？','Ask what—the rules or venue?'),('先问规则，再问体育馆开不开。','First the rules, then whether the sports hall is open.'),('那先别分队，五个人还不够。','Then do not form teams yet; five is not enough.'),('对，愿意当的人，我们再问。','Right. We will ask who wants the role.')],
[('mainidea','Which assumption is corrected?',['A raised hand automatically means volunteering','The hall is closed','All five are captains'],0),('detail','What is asked first?',['The rules','The weather tomorrow','The final score'],0),('inference','What remains unresolved?',['Who voluntarily becomes captain','Whether five equals six','Whether the activity already ended'],0)],drama=True),
dict(tf=[('名单','名单上五个人，每队三个人。','Five names, three per team.','This already makes two teams of three.',False,'Five is less than six.'),('目的','目的是让大家有机会说汉语。','The purpose is to give everyone a chance to speak Mandarin.','Speaking Mandarin is a stated purpose.',True,'It is explicitly the purpose.')],
reply=[('当','你愿意当组长吗？','Would you like to lead?',['可以，但先说明规则吧。','我昨天吃米饭。','五点是三个人。'],0,'Accept with a relevant clarification.'),('举手','你举手是想当队长吗？','Did you raise your hand to be captain?',['不是，我只是想问。','已经两队三个人。','体育是一个名字。'],0,'Clarify the intention.')],
fill=[('报名','想参加的人先报名。','People who want to take part sign up first.'),('举行','活动还没有举行。','The event has not been held yet.')],
match=[('队长',[('队长说明规则。','The captain explains the rules.'),('我带一瓶水。','I bring a bottle of water.'),('名单上五个人。','Five people are on the list.')]),('进行',[('在室内进行。','It takes place indoors.'),('想办一个活动。','We want to organize an activity.'),('举手问问题。','Raise a hand to ask questions.')])]),
[('Asking before assigning','你愿意当队长吗？','Would you like to be captain?','Registration and willingness for responsibility are separate.'),('Correcting an assumption','我只是想问。','I only wanted to ask.','A brief clarification is enough.')],
[('谁当组长？','Who will lead?','Volunteer with a condition',['我可以当，但先说明规则。']),('你举手了，想当队长吗？','You raised a hand; want to be captain?','Clarify that you wanted to ask',['不是，我只是想问。'])],
'Native check: 举行/进行 collocations, role-assignment politeness, voluntary group register and marked action phrases. No sports skill or proficiency scores are invented.')

u='s2-u19'
write(u,'往东走，向左看',['Give a direction without confusing it with a location','Distinguish a route from a confirmed open entrance','Choose a route by destination and actual conditions'],[
('往','towards; in the direction of','về phía','preposition','从这里往东走。','Walk east from here.'),
('向','towards; facing','hướng về','preposition','到路口向左看，先别过街。','At the intersection look left; do not cross yet.'),
('方向','direction','phương hướng','noun','先看方向，再看距离。','Check the direction first, then the distance.'),
('问路','to ask directions','hỏi đường','verb','不清楚就问路，别跟着猜。','Ask directions if unsure; do not follow a guess.'),
('道路','road; route','đường','noun','这条道路今天不能走。','This road cannot be used today.'),
('公路','highway; road','đường ô tô','noun','公路不是步行的入口。','The highway is not the pedestrian entrance.'),
('街','street','phố','noun','这条街的名字在地图上。','The name of this street is on the map.'),
('广场','square; plaza','quảng trường','noun','我们在广场东边见。','We meet on the east side of the square.'),
('公园','park','công viên','noun','公园今天只开东门。','Only the east gate of the park is open today.'),
('花园','garden','vườn hoa','noun','花园在公园里，不是门外。','The garden is inside the park, not outside its gate.'),
('动物园','zoo','sở thú','noun','动物园在另一边，别走错。','The zoo is on the other side; do not go the wrong way.'),
('对面','opposite; across from','đối diện','noun','学校对面有一个公园。','There is a park opposite the school.'),
('边','side; edge','bên; phía','noun','先问是哪一边的入口。','First ask which side has the entrance.'),
('东方','the east','phía đông','noun','地图右边是东方。','The right side of the map is east.'),
('东北','northeast','đông bắc','noun','动物园在地图的东北。','The zoo is in the northeast on the map.'),
('东南','southeast','đông nam','noun','东南那边有一条公路。','There is a highway to the southeast.'),
('西方','the west','phía tây','noun','这张地图左边是西方。','On this map the left side is west.'),
('西北','northwest','tây bắc','noun','花园在公园的西北。','The garden is in the northwest of the park.'),
('西南','southwest','tây nam','noun','广场在学校西南。','The square is southwest of the school.'),
('公里','kilometre','ki-lô-mét','measure word','从这里到公园两公里。','It is two kilometres from here to the park.'),
('米','metre','mét','measure word','东门前五十米有一个路口。','There is an intersection fifty metres in front of the east gate.'),
('辆','vehicle classifier','lượng từ xe','measure word','那边有两辆公交车，不是两个人。','There are two buses there, not two people.')],
[grammar(u,'二22','往','Describe the direction of movement',
'往东走 places 往 plus direction before the motion verb. 往公园走 means move towards the park; it does not prove arrival. 在公园 says where a person is. A route can say 从学校往东走, keeping the start and direction separate. Distance and road availability are additional information, not supplied by 往.',[
('从学校往东走。','Walk east from the school.'),('我往公园走，还没有到。','I am walking towards the park and have not arrived yet.'),('往前走五十米，再问入口。','Walk forward fifty metres, then ask about the entrance.')],
('我往公园，所以我已经在公园里。','我往公园走，还没有到。','Moving towards a destination does not assert being inside it.')),
grammar(u,'二23','向','Orient an action or direct it towards a target',
'向左看 gives the direction of looking; 向老师问路 names the person addressed. 向 can introduce direction or an action’s target, so the following verb matters. 向东走 describes movement; 向东看 describes looking. Do not equate left with east without a known orientation. Here the map is explicitly north-up.',[
('在路口向左看。','Look left at the intersection.'),('向老师问路。','Ask the teacher for directions.'),('向东看，公园在学校对面。','Look east; the park is opposite the school.')],
('向东看，就是已经走到公园。','向东看，还没有走过去。','Looking east is not walking there.'))],
text(u,'d','The open gate matters','Find the available entrance rather than following a stale route.',[
('从学校怎样去公园？','How do I get to the park from school?'),('先看这张地图，上边是北，右边是东。','First look at this map: the top is north, the right is east.'),
('公园在学校对面，是往东走吗？','The park is opposite the school. Do I walk east?'),('对，往东走。但今天西门关了，要去东门。','Yes, walk east. But the west gate is closed today; use the east gate.'),
('导航让我走西门。','Navigation sends me to the west gate.'),('那是以前的路线，先看新的通知。','That is the earlier route; check the new notice first.'),
('从这里到东门多远？','How far is it from here to the east gate?'),('两公里。东门前五十米有路口，先看清楚再过街。','Two kilometres. There is an intersection fifty metres before the east gate; look carefully before crossing.'),
('花园和动物园都在里面吗？','Are the garden and zoo both inside?'),('不是。花园在公园西北，动物园在地图东北，是另一个地方。','No. The garden is in the northwest of the park; the zoo is northeast on the map, a different place.'),
('我骑车过去，可以从公路进吗？','I will cycle there. Can I enter from the highway?'),('先向工作人员问路，入口不能猜。','Ask staff for directions first; do not guess the entrance.')],
[('mainidea','Which source should guide the entrance choice?',['The updated notice, with the east gate open','The old west-gate navigation route','A guess from distance alone'],0),('detail','How far is the east gate from here?',['Two kilometres','Fifty metres','Two metres'],0),('inference','Does looking east mean arrival?',['No, looking is not travel','Yes, it proves arrival','Yes, the zoo is inside the park'],0)],drama=True),
text(u,'r','A north-up route note','Read for direction, distance and the changed entrance.',[
('这张市区地图上北下南，左西右东。','This urban-area map has north at top, south below, west left and east right.'),('公园在学校对面，广场在学校西南。','The park is opposite the school; the square is southwest of it.'),('花园在公园西北，动物园在地图东北。','The garden is northwest inside the park; the zoo is northeast on the map.'),('从学校往东走，可以去公园。','Walking east from the school takes you towards the park.'),('今天西门关闭，只能从东门进。','Today the west gate is closed; enter only from the east gate.'),('东门离这里两公里，不是五十米。','The east gate is two kilometres from here, not fifty metres.'),('五十米是东门前的路口到东门的距离。','Fifty metres is the distance from the intersection in front to the east gate.'),('坐地铁、坐船还是骑车，都先问新的入口。','Whether taking metro, boat or bicycle, first ask about the updated entrance.')],
[('mainidea','What is the key route update?',['Use the east gate because the west gate is closed','The garden is now the zoo','Every left turn is east'],0),('detail','Where is the zoo?',['Northeast on the map','Inside the garden','Southwest of the school'],0),('inference','Does fifty metres describe the whole trip?',['No, it describes the last intersection-to-gate distance','Yes, the whole two kilometres','Yes, it means two metres'],0)],[(4,'东门'),(5,'两公里')]),
text(u,'media','Where you look, where you walk','Follow this original scene’s correction of direction and action.',[
('往东走，向左看。','Walk east; look left.'),('左边就是东方吗？','Is the left side east?'),('不一定，要先看你向哪里。','Not necessarily; first check which way you are facing.'),('地图上北下南，我往右走。','The map is north-up and south-down; I go right.'),('那是在地图上往东，入口还要问。','That is east on the map; you must still ask about the entrance.'),('知道了，到了门口再确认。','Understood; confirm again at the gate.')],
[('mainidea','What must be distinguished?',['Map direction, bodily direction and entrance availability','East and west as the same direction','Looking and arrival as the same action'],0),('detail','How is the map oriented?',['North at top','South at top','No orientation given'],0),('inference','Is the entrance confirmed just by map direction?',['No','Yes','Only if looking left'],0)],drama=True),
dict(tf=[('公里','从这里到东门两公里。','Two kilometres from here to the east gate.','The whole trip is fifty metres.',False,'The stated trip is two kilometres.'),('向','我向东看，还没有走过去。','I look east and have not walked there.','Looking does not mean arrival.',True,'The speaker explicitly has not gone there.')],
reply=[('问路','导航说走西门，但西门关了。','Navigation says west gate, but it is closed.',['先看更新，向工作人员问路。','五十米就是两公里。','往东看已经到了。'],0,'Use current entrance information.'),('方向','这张地图的方向怎么看？','How is this map oriented?',['上北下南，左西右东。','左边一定是你身体的东。','两辆是两个人。'],0,'State the map orientation.')],
fill=[('对面','公园在学校对面。','The park is opposite the school.'),('东北','动物园在地图东北。','The zoo is northeast on the map.')],
match=[('往',[('往东走。','Walk east.'),('向左看。','Look left.'),('在公园里。','Inside the park.')]),('辆',[('两辆公交车。','Two buses.'),('两公里。','Two kilometres.'),('五十米。','Fifty metres.')])]),
[('Checking a route','今天从哪个门进？','Which gate do we use today?','Ask about current conditions rather than relying on a saved route.'),('Unknown entrance','我不清楚，先问路吧。','I am unsure; let us ask directions first.','Do not make up a route.')],
[('从学校往哪里走？','Which way from the school?','Give a direction',['往东走。']),('西门关了，怎么办？','The west gate is closed; what now?','Ask for current directions',['先向工作人员问路。'])],
'Native check: 往/向 targets, compass orientation, 对面 reference, metro/boat route plausibility and short dialogue ellipsis. Distances are fictional exercise facts, not real navigation instructions.')

u='s2-u20'
character_readings[u+':长']='zhǎng'
character_notes[u+':长']=' Here zhǎng means grow, as in 长大; cháng means long in other contexts.'
write(u,'我们是在活动上认识的',['Explain the time, place and way of a first meeting','Separate a starting point from evidence for a judgment','Ask about background without inferring it from appearance'],[
('当时','at that time','lúc đó','noun','当时我们还不认识，只在同一个活动。','At that time we did not know each other; we were just at the same event.'),
('那会儿','at that time; back then','hồi đó','noun','那会儿我还在上学。','Back then I was still studying.'),
('那时候','at that time','lúc ấy','noun','那时候我们住得很近。','At that time we lived near each other.'),
('碰','to touch; meet by chance','chạm; gặp','verb','我出门就碰到老朋友。','When I went out, I happened to meet an old friend.'),
('碰到','to run into; encounter','tình cờ gặp','verb','我们在门口碰到，不是先约好的。','We ran into each other at the entrance; it was not arranged first.'),
('碰见','to meet by chance','tình cờ gặp','verb','我昨天碰见一个同事。','Yesterday I ran into a colleague.'),
('见到','to see; meet successfully','gặp được','verb','今天终于见到你了。','Today I finally got to see you.'),
('见过','to have seen or met','đã từng gặp','verb','我见过她，但还不认识。','I have seen her before, but do not know her yet.'),
('从小','from childhood','từ nhỏ','adverb','我从小住在南方。','I have lived in the south since childhood.'),
('小时候','when young; childhood','khi còn nhỏ','noun','小时候我常去这个公园。','As a child I often went to this park.'),
('出生','to be born','sinh ra','verb','我在北方出生，在南方长大。','I was born in the north and grew up in the south.'),
('长大','to grow up','lớn lên','verb','我在南方长大，不是一直住在北方。','I grew up in the south; I did not always live in the north.'),
('同事','colleague','đồng nghiệp','noun','我们现在是同事，以前是同学。','We are colleagues now and used to be classmates.'),
('公司','company','công ty','noun','公司离学校不远。','The company is not far from the school.'),
('单位','work unit; organization','cơ quan; đơn vị','noun','她在这个单位工作。','She works in this organization.'),
('打工','to work for wages; do casual work','làm thuê','verb','那会儿我周末打工，平时上学。','Back then I worked on weekends and studied during the week.'),
('实习','to intern; practical training','thực tập','verb','我在公司实习的时候认识她。','I met her while interning at the company.'),
('老朋友','old friend; long-standing friend','bạn lâu năm','noun','老朋友是认识很久，不一定年纪大。','An old friend is someone known a long time, not necessarily an elderly person.'),
('青年','young adult; youth','thanh niên','noun','这个活动有青年，也有中年朋友。','The event has young adults and middle-aged friends.'),
('中年','middle age','trung niên','noun','中年朋友也可以来学汉语。','Middle-aged friends can also come to study Mandarin.'),
('老年','old age','tuổi già','noun','老年人参加以前，先问他们自己的想法。','Ask older people for their own views before participation.'),
('家庭','family; household','gia đình','noun','家庭情况是自己的事，不想说也可以。','Family circumstances are personal; it is okay not to discuss them.')],
[grammar(u,'二24','从：起点和依据','Distinguish a starting point from a basis for judgment',
'从学校出发 gives a spatial start; 从小 gives a temporal start. 从他说的话看 introduces a basis for a limited judgment. That evidence does not justify guesses about someone’s whole life or family. 从…看 is not a verb of physical travel. Ask instead of inferring background from voice, age or appearance.',[
('我从学校出发。','I set off from the school.'),('我从小住在南方。','I have lived in the south since childhood.'),('从他说的话看，他还没有确认时间。','Judging from what he says, he has not confirmed the time yet.')],
('从她的脸看，她一定住在北方。','她住在哪里？我们先问。','Appearance does not establish where someone lives.')),
grammar(u,'二60','是 … 的：时间、地点、方式、施事','Focus on circumstances of an already-established event',
'我们是在活动上认识的 focuses on where the known meeting occurred. 是去年认识的 focuses on time, 是朋友介绍的 on who introduced you, and 是坐车来的 on how you came. This construction does not make a planned future event completed. In casual speech 是 can be omitted: 我们去年认识的. Do not infer a closer relationship just from 见过.',[
('我们是去年认识的。','We met last year.'),('我们是在活动上认识的。','We met at an event.'),('是朋友介绍的，我是坐车来的。','A friend introduced us; I came by vehicle.')],
('我们是明天认识的。','我们明天去见面。','是…的 here focuses on an established past event, not tomorrow’s plan.'))],
text(u,'d','A first meeting remembered','Find the actual first meeting, later relationship and unknown background.',[
('我们以前见过吗？','Have we met before?'),('见过，去年在朋友见面的活动上。','Yes, at the Friends Meet event last year.'),
('是朋友介绍的吗？','Did a friend introduce us?'),('不是，是在门口碰到的。你先问我活动在哪里。','No, we ran into each other at the entrance. You first asked me where the event was.'),
('那时候我们还是同学吧？','We were classmates then, right?'),('不是。那会儿我还在上学，你在公司实习。现在我们是同事。','No. I was still studying then and you were interning at the company. Now we are colleagues.'),
('我从小在南方住，是坐车来的。','I have lived in the south since childhood and came by vehicle.'),('我在北方出生，后来在南方长大。','I was born in the north and later grew up in the south.'),
('那我们是老朋友了？','So we are long-standing friends?'),('认识一年了，可以这样说，不是说年纪大。','We have known each other a year; you can say that. It does not mean elderly.'),
('你的家庭情况呢？不想说也没关系。','What about your family circumstances? It is fine if you do not want to discuss them.'),('谢谢，我今天先不说，我们聊活动吧。','Thank you. I will not discuss that today; let us talk about the event.')],
[('mainidea','How did the first meeting happen?',['By chance at an event entrance last year','They were childhood classmates','A colleague formally introduced them yesterday'],0),('detail','What are they now?',['Colleagues','Definitely siblings','Definitely childhood classmates'],0),('inference','May the listener infer family details?',['No, the speaker declines to discuss them','Yes, from northern birthplace','Yes, from age'],0)],drama=True),
text(u,'r','A short memory','Read to distinguish birthplace, childhood home and first meeting.',[
('我在北方出生，在南方长大。','I was born in the north and grew up in the south.'),('小时候常去公园，不认识现在的同事。','As a child I often visited the park and did not know my present colleague.'),('去年我周末打工，平时还在上学。','Last year I worked on weekends and was still studying during the week.'),('我们是在朋友见面的活动上认识的。','We met at the Friends Meet event.'),('不是朋友介绍，是在门口碰到的。','It was not a friend’s introduction; we ran into each other at the entrance.'),('那时候她在公司实习，我是坐车来的。','She was interning at the company then; I came by vehicle.'),('现在同一个单位工作，我们是同事，也有共同的朋友。','Now we work in the same organization, are colleagues and have mutual friends.'),('见过一个人不等于很了解他的家庭。','Having met a person does not mean knowing their family well.')],
[('mainidea','What does the memory trace?',['Background and a chance first meeting followed by becoming colleagues','A lifelong family relationship','A planned meeting tomorrow'],0),('detail','Who introduced them?',['No one; they met by chance','A teacher','A family member'],0),('inference','Was northern birthplace the same as growing up there?',['No, the speaker grew up in the south','Yes, the speaker never moved','The text says southern birthplace'],0)],[(3,'活动'),(6,'同事')]),
text(u,'media','An old friend is not necessarily old','Follow the original scene’s correction of a double meaning.',[
('你说老朋友，他一定是老年人吧？','You said old friend; he must be elderly, right?'),('不是，老朋友是认识很久。','No, an old friend is someone known a long time.'),('那你们小时候就认识？','Then you knew each other as children?'),('也不是，我们是去年在活动上认识的。','Not that either; we met at an event last year.'),('我猜得太快了。','I guessed too quickly.'),('先问他自己，别从一个词猜家庭。','Ask him himself first; do not guess his family from one word.')],
[('mainidea','Which meaning is clarified?',['老朋友 refers to a long-standing relationship, not necessarily old age','老朋友 always means an elderly person','Every colleague is family'],0),('detail','When did they meet?',['Last year','In childhood','Tomorrow'],0),('inference','Does the label prove family background?',['No','Yes','Only if the person is young'],0)],drama=True),
dict(tf=[('出生','我在北方出生，在南方长大。','I was born in the north and grew up in the south.','The speaker grew up in the north.',False,'Birthplace and childhood home differ.'),('老朋友','老朋友不一定年纪大。','An old friend is not necessarily elderly.','The label need not describe age.',True,'It describes the relationship’s duration.')],
reply=[('碰到','是朋友介绍的吗？','Did a friend introduce you?',['不是，我们在门口碰到的。','我明天认识的。','从小就是公里。'],0,'Give the actual way of meeting.'),('家庭','家庭情况不想说，可以吗？','May I decline to discuss family circumstances?',['当然，我们聊别的吧。','从脸看就一定知道。','老朋友就是出生。'],0,'Respect the stated boundary.')],
fill=[('实习','那时候她在公司实习。','She was interning at a company then.'),('长大','我在南方长大。','I grew up in the south.')],
match=[('见过',[('见过，但不认识。','Seen before, but do not know each other.'),('是去年认识的。','Met last year.'),('我们是同事。','We are colleagues.')]),('当时',[('当时还在上学。','Still studying at that time.'),('现在同一个单位工作。','Now working in the same organization.'),('明天再见。','Meet again tomorrow.')])]),
[('A focused follow-up','你们是怎么认识的？','How did you meet?','Ask the specific circumstance, not a broad personal interrogation.'),('Respecting a refusal','可以，我们聊别的。','Of course; let us talk about something else.','A refusal to discuss family does not require justification.')],
[('你们是怎么认识的？','How did you meet?','Explain the chance meeting',['我们是在门口碰到的。']),('不想说家庭情况。','I do not want to discuss my family.','Respect the refusal',['可以，我们聊别的吧。'])],
'Native check: 是…的 circumstance focus, 从…看 evidence limits, 那会儿/那时候 register, 老朋友 duration and respectful personal questions. 字 长 is zhǎng in 长大, not cháng.')

from retrievals import apply_ids
apply_ids(['s2-u17','s2-u18','s2-u19','s2-u20'])
