"""Concrete later retrieval tasks, using existing screened course sentences."""
import json
from pathlib import Path
from common import py
ROOT = Path(__file__).resolve().parents[2]

RETRIEVALS = {
13:('一02',[('我会说英语。','I can speak English.'),('今天我不能去上课。','I cannot attend class today.'),('我能教你汉字。','I can teach you Chinese characters.')]),
14:('一15',[('从这儿到机场远吗？','Is the airport far from here?'),('从机场到我家，你坐地铁吧。','Take the subway from the airport to my home.'),('从大学站到我家不远，走路五分钟。','My home is not far from University Station: five minutes on foot.')]),
15:('一21',[('我昨天看了两个电影。','I watched two films yesterday.'),('我昨天没出去。','I did not go out yesterday.'),('昨天下雨了。','It rained yesterday.')]),
16:('一34',[('请坐！','Please sit down.'),('请进！请坐！','Please come in and sit down.'),('请坐，喝点儿茶吧。','Please sit down and have some tea.')]),
17:('一40',[('我病了。','I have become ill.'),('我好点儿了。','I am a little better now.'),('我感冒了。','I have caught a cold.')]),
18:('一02 / 一41',[('我会说英语。','I can speak English.'),('我在家看了两个电影。','I watched two films at home.'),('我昨天没出去。','I did not go out yesterday.')]),
19:('一15 / 一43',[('从这儿到机场远吗？','Is the airport far from here?'),('这件衣服一百二十块。','This item of clothing costs one hundred and twenty yuan.'),('水三块。','Water costs three yuan.')]),
20:('一21 / 一47',[('我昨天看了两个电影。','I watched two films yesterday.'),('中文字幕还是英语字幕？','Chinese subtitles or English subtitles?'),('周末你做了什么？','What did you do at the weekend?')]),
21:('一34 / 二26 / 一20 / 一26',[('请坐，喝点儿茶吧。','Please sit down and have some tea.'),('给我你的微信吧。','Give me your WeChat contact.'),('我找钱包，你帮我。','I will look for my wallet; please help me.')]),
22:('一40 / 二72 / 一07 / 一23',[('我好点儿了。','I am a little better now.'),('这是我第一次来中国。','This is my first visit to China.'),('两杯水和半杯奶。','Two glasses of water and half a cup of milk.')]),
23:('一41 / 一08 / 一37 / 一12 / 一28',[('我在家看了两个电影。','I watched two films at home.'),('一家商店，两间房，三口人。','One shop, two rooms, three family members.'),('我常在家读书，她常常上午学习。','I often read at home; she often studies in the morning.')]),
24:('一43 / 一20 / 一26 / 一14 / 一48',[('这件衣服一百二十块。','This item of clothing costs one hundred and twenty yuan.'),('这是我的课本，那是别人的。','This is my textbook; that one belongs to someone else.'),('星期日有没有课？','Is there class on Sunday?')]),
25:('一47 / 一16 / 一29 / 一44',[('中文字幕还是英语字幕？','Chinese subtitles or English subtitles?'),('我在车站旁边等你。','I will wait beside the station.'),('我们八点零五分见面。','Let us meet at eight oh five.')]),
26:('二26 / 一12 / 一28 / 一17 / 一19',[('给我你的微信吧。','Give me your WeChat contact.'),('先吃晚饭，再去上课。','Eat dinner first, then go to class.'),('爷爷和奶奶都来。','Grandfather and grandmother are both coming.')]),
27:('二72 / 一14 / 一48 / 一09 / 一30 / 一35',[('这是我第一次来中国。','This is my first visit to China.'),('星期日没有课，别去学校。','There is no class on Sunday; do not go to school.'),('真好看！','That really looks good!')]),
28:('一16 / 一29 / 一44 / 一18 / 一38',[('我买车票，你等朋友。','I buy tickets; you wait for our friend.'),('星期日两点半上车。','Board on Sunday at half past two.'),('商场没有图书馆安静。','The shopping centre is not as quiet as the library.')]),
29:('一12 / 一28 / 一17 / 一19 / 一10 / 一39',[('我常在家读书，她常常上午学习。','I often read at home; she often studies in the morning.'),('爷爷和奶奶都来。','Grandfather and grandmother are both coming.'),('我们一边走路，一边聊天。','We walk and chat at the same time.')]),
30:('一14 / 一48 / 一09 / 一30 / 一35 / 一22 / 一33 / 一45',[('星期日有没有课？','Is there class on Sunday?'),('真好看！','That really looks good!'),('我可以进去吗？','May I go in?')]),
's2-u01':('一18 / 一38 / 一01 / 一31',[
('图书馆比商场安静。','The library is quieter than the shopping centre.'),
('商场没有图书馆安静。','The shopping centre is not as quiet as the library.'),
('北门。学校前边，路的东边。','The north gate: in front of the school, on the east side of the road.')]),
's2-u02':('一10 / 一39 / 一25 / 一32 / 一36',[
('我们一边走，一边聊天。','We walk and chat at the same time.'),
('我们都想走，有些朋友想跑。','We all want to walk; some friends want to run.'),
('这是学校，是我们学习的地方。','This is a school, the place where we study.'),
('今天星期六，我二十岁。','Today is Saturday; I am twenty.'),
('桌上是书，不是饭。','What is on the table is a book, not food.'),
('我有书，也喜欢读书。','I have books and also enjoy reading.')]),
's2-u03':('一22 / 一33 / 一45 / 二06 / 二37 / 二01',[
('明天考不考？上午还是下午？','Is there a test tomorrow or not? In the morning or afternoon?'),
('咱们自己先看，小组的书读懂了吗？','Let us check for ourselves first; have we understood the group’s book?'),
('你可以去，他可能会来。大家来了？开始吧。','You may go; he might come. Is everyone here? Let us begin.'),
('你在网上买的吗？','Did you buy it online?'),
('书和本子，新的书，读书，读懂，大家来了。','Book and notebook; a new book; read a book; understand by reading; everyone has arrived.'),
('我在家，你呢？','I am at home; what about you?')]),
's2-u04':('一01 / 一31 / 二02 / 二75',[
('北门。学校前边，路的东边。','The north gate: in front of the school, on the east side of the road.'),
('我该带什么？你应该先问主人。','What should I bring? You should ask the host first.'),
('六点半来，好吗？带书怎么样？','Come at half past six, okay? How about bringing a book?'),
('我带两瓶水，可以吗？行吗？','May I bring two bottles of water? Is that okay?')]),
's2-u05':('一25 / 一32 / 一36 / 二03 / 二45',[
('今天星期六，我二十岁。','Today is Saturday; I am twenty.'),
('这是学校，是我们学习的地方。','This is a school, the place where we study.'),
('我愿意帮忙，但今晚不方便。','I am willing to help, but tonight is inconvenient.'),
('还是星期六去吧，你想喝茶还是喝咖啡？','Let us go on Saturday instead; would you like tea or coffee?')]),
's2-u06':('二06 / 二37 / 二01 / 二05 / 二76',[
('咱们自己先看，小组的书读懂了吗？','Let us check for ourselves first; have we understood the group’s book?'),
('你可以去，他可能会来。','You may go; he might come.'),
('为什么选这里？你想去什么样的饭馆？','Why choose here? What kind of restaurant would you like?'),
('怎样去，要多久？','How do we get there, and how long does it take?'),
('谁来，哪里见，什么时候走？','Who is coming, where do we meet, and when do we leave?'),
('什么菜，几个人，多少钱，怎么付？','Which dish, how many people, how much money, and how do we pay?')]),
's2-u07':('二02 / 二75 / 二04 / 二11 / 二52',[
('我该带什么？你应该先问主人。','What should I bring? You should ask the host first.'),
('六点半来，好吗？我带两瓶水，可以吗？','Come at half past six, okay? May I bring two bottles of water?'),
('我看了看题目，我们练习练习。','I briefly looked at the questions; let us practise a little.'),
('这段录音听了两遍，答案检查了三次。','This recording was heard twice through; the answers were checked three times.'),
('看一场电影，去一回活动，老师拍三下手。','Watch a film showing, attend an activity once, and the teacher claps three times.'),
('看看，说一说，再练习练习。','Take a look, say a little, then practise a little.')]),
's2-u08':('二03 / 二45 / 二07 / 二38',[
('我愿意帮忙，但今晚不方便。','I am willing to help, but tonight is inconvenient.'),
('还是星期六去吧，你想喝茶还是喝咖啡？','Let us go on Saturday instead; would you like tea or coffee?'),
('图片这么小，别那样猜时间。','The image is so small; do not guess the time that way.'),
('新的通知还没有，我去问主办方。','The new notice is not here yet; I will ask the organizer.')]),
's2-u09':('二05 / 二76 / 二08 / 二41 / 二46',[
('为什么选这里？你想去什么样的饭馆？','Why choose here? What kind of restaurant would you like?'),
('怎样去，要多久？谁来，哪里见，什么时候走？','How do we get there, how long does it take, who comes, where do we meet, and when do we leave?'),
('绿的又轻又短，黄的还没干。','The green one is light and short; the yellow one is not dry.'),
('衣服干干净净，鞋也干干净净。','The clothes are clean, and the shoes are clean too.')]),
's2-u10':('二04 / 二11 / 二52 / 二09 / 二73',[
('我看了看题目，我们练习练习。','I briefly looked at the questions; let us practise a little.'),
('这段录音听了两遍，答案检查了三次。','This recording was heard twice through; the answers were checked three times.'),
('看一场电影，去一回活动，老师拍三下手。','Watch a film showing, attend an activity once, and the teacher claps three times.'),
('一万不是一千，一亿不是一百万。','Ten thousand is not one thousand; one hundred million is not one million.'),
('十多个人，一个多小时。','More than ten people, a little over an hour.')]),
's2-u11':('二07 / 二38 / 二10 / 二61',[
('图片这么小，别那样猜时间。','The image is so small; do not guess the time that way.'),
('新的通知还没有，我去问主办方。','The new notice is not here yet; I will ask the organizer.'),
('一封信，一件衣服，一条围巾。','A letter, an item of clothing, a scarf.'),
('我送你一本书。','I give you a book as a gift.'),
('我送给你一本书。','I give you a book as a gift.')]),
's2-u12':('二08 / 二41 / 二46 / 二12 / 二47 / 二81',[
('绿的又轻又短，黄的还没干。','The green one is light and short; the yellow one is not dry.'),
('衣服干干净净，鞋也干干净净。','The clothes are clean, and the shoes are clean too.'),
('我们等十分钟，七点开始。','We wait ten minutes; it starts at seven.'),
('开场以前先坐好，散场以后再出去。','Take your seat before the start; leave after the end.'),
('快要七点了，节目就要开始了。','It is nearly seven; the programme is about to begin.')]),
}

RETRIEVALS.update({
's2-u13':('二09 / 二73 / 二10 / 二61',[
('一万不是一千，一亿不是一百万。','Ten thousand is not one thousand; one hundred million is not one million.'),
('十多个人，一个多小时。','More than ten people, a little over an hour.'),
('一封信，一件衣服，一条围巾。','A letter, an item of clothing, a scarf.'),
('我送你一本书，我送给你一本书。','I give you a book; I give a book to you.')]),
's2-u14':('二12 / 二47 / 二81',[
('开场以前先坐好，散场以后再出去。','Take your seat before the start; leave after the end.'),
('快要七点了，节目就要开始了。','It is nearly seven; the programme is about to begin.'),
('我们等十分钟，七点开始。','We wait ten minutes; it starts at seven.')]),
's2-u15':('二13 / 二58',[
('这里挺亮，也很凉快。','It is quite bright and pleasantly cool here.'),
('里面比外面响，外面不如里面暖和。','Inside is louder than outside; outside is not as warm as inside.'),
('这里又亮又响，我想换个地方。','It is bright and loud here; I would like to change places.')]),
's2-u16':('二14 / 二39',[
('四个人，其中一个只要水。','Four people, one of whom wants only water.'),
('大多数同意，不等于所有人都同意。','The majority agreeing does not mean everyone agrees.'),
('其他人还没选，先别下单。','The others have not chosen yet; do not order first.')]),
's2-u17':('二15 / 二20 / 二80',[
('朋友已经到了，我还在路上。','My friend has already arrived; I am still on the way.'),
('才六点四十，不用急。','It is only six forty; no need to hurry.'),
('都七点了，他七点才到。','It is already seven; he did not arrive until seven.'),
('集合时间到了，我们该出发了。','The meeting time has come; it is time for us to set off.')]),
's2-u18':('二16 / 二62 / 二69',[
('先看通知，然后报名。','Check the notice first, then sign up.'),
('从学校走到活动地点，先走进东门。','Walk from the school to the event venue; first enter through the east gate.'),
('从教室拿出书，再把书交给老师。','Take a book out of the classroom, then hand it to the teacher.')]),
's2-u19':('二17 / 二74',[
('重点是日期，不是地址。','The main point is the date, not the address.'),
('我想讨论这个问题，你可以直接问。','I want to discuss this question; you may ask directly.'),
('同样的问题，不一定有相同的答案。','The same question does not necessarily have an identical answer.')]),
's2-u20':('二18 / 二79 / 二78',[
('我以为你同意了，但还没有问清楚。','I thought you had agreed, but had not clarified it.'),
('点头不一定就是同意。','Nodding does not necessarily mean agreement.'),
('不是故意拿的，我现在还给你。','I did not take it deliberately; I will return it now.'),
('好吧，我们先别开这个玩笑。','Okay, let us not make this joke for now.')]),
})

RETRIEVALS.update({
's2-u21':('二19 / 二66 / 二67',[
('只要有空，就可以来。','As long as you are free, you may come.'),
('如果下雨，就换地方，时间不变。','If it rains, change the venue; the time stays unchanged.'),
('多云不等于一定下雨。','Cloudy does not mean rain is certain.')]),
's2-u22':('二21 / 二40',[
('今天我当组长，明天换人。','I act as group leader today; someone else takes a turn tomorrow.'),
('我们想办活动，还没有举行。','We want to organize an event; it has not yet been held.'),
('目的是让大家练习说汉语。','The purpose is to let everyone practise speaking Mandarin.')]),
's2-u23':('二22 / 二23',[
('往东走，路口再向左转。','Walk east, then turn left at the intersection.'),
('看着北边，不是已经往北走。','Looking north is not already walking north.'),
('出口在右边，别去左边。','The exit is on the right; do not go left.')]),
's2-u24':('二24 / 二60',[
('我们是去年在门口认识的。','We met at the entrance last year.'),
('从这个消息看，时间还没定。','Judging from this message, the time is not settled yet.'),
('从小在南方长大。','Grew up in the south from childhood.')]),
})

RETRIEVALS.update({
's2-u25':('二25 / 二59',[
('我对这个活动有兴趣。','I am interested in this activity.'),
('她跟我一样喜欢看书。','She likes reading just as I do.'),
('生活不同，不等于态度不好。','Different lives do not imply a bad attitude.')]),
's2-u26':('二27 / 二53',[
('湖离海很远，我们先去河边。','The lake is far from the sea; we will go to the river first.'),
('这条路比那条路长一公里。','This route is one kilometre longer than that one.'),
('她背两句话，不是背着一个包。','She recites two sentences, rather than carrying a bag on her back.')]),
's2-u27':('二28 / 二55',[
('我为朋友打印两页。','I print two pages for a friend.'),
('她为这个问题想了很久。','She thought about this question for a long time.'),
('这个活动很有意义。','This activity is meaningful.')]),
's2-u28':('二29 / 二64',[
('明天读书或者看影片，还没定。','Read or watch a film tomorrow; it is not settled.'),
('你想读书还是听音乐？','Would you like to read or listen to music?'),
('或者我先讲，或者你先讲。','Either I speak first or you do.')]),
's2-u29':('二32 / 二71',[
('她去过这个地方，但今天不在那里。','She has been to this place but is not there today.'),
('以前坐过船，不等于今天已经上船。','Having taken a boat before does not mean having boarded one today.'),
('没有去过，还想试一次。','Has not been before and still wants to try once.')]),
's2-u30':('二30 / 二65 / 二33 / 二56 / 二70',[
('虽然下雨，但是时间没变。','Although it rains, the time has not changed.'),
('门开着，不等于可以直接进去。','An open door does not mean you may enter directly.'),
('桌上放着书，她还没有读。','A book lies on the table; she has not read it yet.')]),
's2-u31':('二31 / 二51 / 二34 / 二43 / 二77',[
('她说得很清楚。','She speaks clearly.'),
('带书、笔什么的就行。','Things like books and pens are enough.'),
('我想看书，你呢？','I want to read; what about you?')]),
's2-u32':('二35 / 二42 / 二36 / 二32 / 二71',[
('喂，你好，现在方便吗？','Hello, is now convenient?'),
('有空的话，我来坐一会儿。','If free, I will visit briefly.'),
('不一会儿，她回了消息。','A short while later, she replied.'),
('这部影片我看过，但小说还没读。','I have seen this film but not read the novel.')]),
's2-u33':('二44 / 二63 / 二33 / 二56 / 二70',[
('她不但能读，而且能说。','She can not only read but also speak.'),
('越来越清楚，还不是完美。','It is becoming clearer, but is not perfect yet.'),
('桌上放着杯子，门还开着。','Cups lie on the table and the door is still open.')]),
's2-u34':('二48 / 二54 / 二34 / 二43 / 二77',[
('今天星期三，这本书三十五块。','Today is Wednesday; this book costs thirty-five yuan.'),
('姐姐是商人，我是学生。','My elder sister is a businessperson; I am a student.'),
('我想读报纸，你呢？','I want to read a newspaper; what about you?')]),
})

RETRIEVALS.update({
's3-u01':('二35 / 二42 / 二36 / 二49 / 二50 / 二57',[
('喂，你好，有空的话来坐一会儿。','Hello; if free, come visit briefly.'),
('不一会儿，她回了消息。','A short while later, she replied.'),
('先把面粉取出来，再称一百克。','Take the flour out first, then weigh a hundred grams.'),
('请她把杯子端出来。','Ask her to bring the cups out.')]),
's3-u02':('二44 / 二63 / 二68',[
('她不但能读，而且能说。','She can not only read but also speak.'),
('越练越清楚，还不是完美。','Practice makes it clearer, but it is not yet perfect.'),
('因为分工清楚，所以没有重复做。','Because responsibilities were clear, the work was not duplicated.')]),
's3-u03':('二48 / 二54 / 三01 / 三02',[
('姐姐是商人，我是学生。','My elder sister is a businessperson; I am a student.'),
('今天星期三，这本书三十五块。','Today is Wednesday; this book costs thirty-five yuan.'),
('老李是称呼，不能直接猜他的年龄。','Old Li is an address form; do not directly infer his age.'),
('朋友们看包里头的书，桌子上的笔先别动。','The friends look at the books inside the bag; leave the pens on the table for now.')]),
's3-u04':('二49 / 二50 / 二57 / 三03 / 三07',[
('请她把杯子端出来。','Ask her to bring the cups out.'),
('先取出面粉，再称一百克。','Take out the flour first, then weigh a hundred grams.'),
('谁都可以只听，不一定参加比赛。','Anyone may just listen; entering the competition is not required.'),
('不敢参加，不等于没有能力。','Not daring to join does not imply lacking ability.')]),
's3-u05':('二68 / 三04 / 三08',[
('因为分工清楚，所以没有重复做。','Because responsibilities were clear, the work was not duplicated.'),
('每个人都先看自己的任务。','Everyone first checks their own task.'),
('需要帮忙，先问对方有没有空。','When help is needed, first ask whether the other person is free.'),
('任何人都可以问，不必已经有答案。','Anyone may ask; already having the answer is unnecessary.')]),
's3-u06':('三01 / 三02 / 三05 / 三57',[
('老李是称呼，不能直接猜他的年龄。','Old Li is an address form; do not directly infer his age.'),
('朋友们看包里头的书。','The friends look at the books inside the bag.'),
('下午理个发，再跟朋友谈一谈话。','Have a haircut in the afternoon, then have a chat with a friend.'),
('请她问一下朋友，不能替朋友答应。','Ask her to ask her friend; she cannot agree on the friend’s behalf.')]),
's3-u07':('三03 / 三07 / 三06 / 三46',[
('谁都可以只听，不一定参加比赛。','Anyone may just listen; competition entry is not required.'),
('不敢参加，不等于没有能力。','Not daring to join does not imply lacking ability.'),
('文件打得开，日期还没核对。','The file can open; its date has not been checked.'),
('找了十分钟，终于找到了。','Searched for ten minutes and finally found it.')]),
's3-u08':('三04 / 三08 / 三09 / 三10',[
('每个人都先看自己的任务。','Everyone first checks their own task.'),
('需要帮忙，先问对方有没有空。','When help is needed, ask whether the other person is free first.'),
('两双筷子，通常是四根。','Two pairs of chopsticks normally contain four individual sticks.'),
('看了一眼，还要仔细读。','After a glance, one still needs to read carefully.')]),
's3-u09':('三05 / 三57 / 三11 / 三33',[
('下午理个发，再跟朋友谈一谈话。','Have a haircut in the afternoon, then have a chat with a friend.'),
('请她问一下朋友，不能替朋友答应。','Ask her to ask her friend; she cannot agree on the friend’s behalf.'),
('张张纸都有标题，一张一张地看。','Every sheet has a heading; read them one at a time.'),
('六个人四张纸，还缺两张。','Six people and four sheets: two more sheets are needed.')]),
's3-u10':('三06 / 三46 / 三12 / 三58',[
('文件打得开，日期还没核对。','The file can open; its date has not been checked.'),
('找了十分钟，终于找到了。','Searched for ten minutes and finally found it.'),
('今天更加清楚，不等于一定更快。','Clearer today does not mean necessarily faster.'),
('不比她快，可能一样快。','Not faster than her; possibly equally fast.')]),
's3-u11':('三09 / 三10 / 三13 / 三37',[
('两双筷子，通常是四根。','Two pairs of chopsticks normally contain four individual sticks.'),
('看了一眼，还要仔细读。','After a glance, one still needs to read carefully.'),
('至少提前一天，提前两天也可以。','At least one day ahead; two days ahead is also acceptable.'),
('材料有的是，名额还要确认。','Materials are plentiful; places still need confirmation.')]),
's3-u12':('三11 / 三33 / 三14 / 三21',[
('张张纸都有标题，一张一张地看。','Every sheet has a heading; read them one at a time.'),
('六个人四张纸，还缺两张。','Six people and four sheets: two more sheets are needed.'),
('她曾经住这里，旧店早已搬走。','She once lived here; the old shop moved away long ago.'),
('自从毕业，我们很少见面。','Since graduation we have rarely met.')]),
})

RETRIEVALS.update({
's3-u13':('三12 / 三58 / 三15 / 三51',[
('今天更加清楚，不等于一定更快。','Clearer today does not necessarily mean faster.'),
('不比她快，可能一样快。','Not faster than her; possibly equally fast.'),
('通常周末散步，今天只走了二十分钟。','Usually walk on weekends; today walked only twenty minutes.'),
('连续两天不等于坚持了一年。','Two consecutive days do not mean a year of perseverance.')]),
's3-u14':('三13 / 三37 / 三16 / 三17',[
('至少提前一天，提前两天也可以。','At least one day ahead; two days ahead is fine too.'),
('材料有的是，名额还要确认。','Materials are plentiful; places still need confirmation.'),
('等听清楚了再加快。','Increase speed after hearing clearly.'),
('我亲自读，你帮我听。','I read personally; you help listen.')]),
's3-u15':('三14 / 三21 / 三18 / 三69',[
('她曾经住这里，旧店早已搬走。','She once lived here; the old shop moved long ago.'),
('自从毕业，我们很少见面。','Since graduation we have rarely met.'),
('她大概六点到，还没确认。','She will probably arrive at six; it is unconfirmed.'),
('要是下雨，就在室内见。','If it rains, meet indoors.')]),
's3-u16':('三15 / 三51 / 三19 / 三76',[
('通常周末散步，今天只走了二十分钟。','Usually walk on weekends; today walked only twenty minutes.'),
('连续两天不等于坚持了一年。','Two consecutive days do not mean a year of perseverance.'),
('活动并没有取消，只是换了房间。','The event is not cancelled; only the room changed.'),
('难道旧图片就能证明今天取消了吗？','Can an old picture really prove today’s cancellation?')]),
})

RETRIEVALS.update({
's3-u17':('三16 / 三17 / 三20 / 三29',[
('等听清楚了再加快。','Increase speed after hearing clearly.'),
('我亲自读，你帮我听。','I read personally; you help listen.'),
('活动由学生举办。','Students organize the event.'),
('按名单分组，不按到达时间。','Group according to the list, not arrival time.')]),
's3-u18':('三18 / 三69 / 三22 / 三47',[
('她大概六点到，还没确认。','She will probably arrive at six; it is unconfirmed.'),
('要是下雨，就在室内见。','If it rains, meet indoors.'),
('朝门口走，还没说是否到达。','Walk toward the doorway; arrival has not been established.'),
('我在二楼，你上来。','I am on the second floor; come up.')]),
's3-u19':('三19 / 三76 / 三23 / 三40',[
('活动并没有取消，只是换了房间。','The event is not cancelled; only the room changed.'),
('难道旧图片就能证明今天取消了吗？','Can an old picture really prove today’s cancellation?'),
('我为她担心，也尊重她的选择。','I worry about her and also respect her choice.'),
('对我来说，安静很重要。','For me, quiet matters.')]),
's3-u20':('三20 / 三29 / 三24 / 三41',[
('活动由学生举办。','Students organize the event.'),
('按名单分组，不按到达时间。','Group according to the list, not arrival time.'),
('向主人问清楚时间。','Ask the host to clarify the time.'),
('像平时一样，先问时间。','As usual, ask the time first.')]),
})

RETRIEVALS.update({
's3-u21':('三22 / 三47 / 三25 / 三71',[
('朝门口走，还没说是否到达。','Walk toward the doorway; arrival has not been established.'),
('我在二楼，你上来。','I am on the second floor; come up.'),
('因为我没核对，我发了旧地址。','Because I did not check, I sent the old address.'),
('由于通知有错，所以先停止传播旧通知。','Because the notice is wrong, stop circulating the old notice first.')]),
's3-u22':('三23 / 三40 / 三26 / 三72',[
('我为她担心，也尊重她的选择。','I worry about her and also respect her choice.'),
('对我来说，安静很重要。','For me, quiet matters.'),
('为了带书方便，我选这个布袋。','For carrying books conveniently, I choose this cloth bag.'),
('为了纪念见面，我们做一张贺卡。','To commemorate meeting, we make a greeting card.')]),
's3-u23':('三24 / 三41 / 三27 / 三54',[
('向主人问清楚时间。','Ask the host to clarify the time.'),
('像平时一样，先问时间。','As usual, ask the time first.'),
('衣服被雨弄湿了。','The clothes were made wet by rain.'),
('把这本书交给她。','Hand this book to her.')]),
's3-u24':('三25 / 三71 / 三28 / 三38',[
('因为没核对，我发了旧通知。','Because I did not check, I sent an old notice.'),
('由于通知有错，所以先停止传播旧通知。','Because the notice is wrong, stop circulating the old notice first.'),
('除了看节目，我还听广播。','Besides watching programmes, I also listen to the radio.'),
('除了周五，其他几天都可以。','Any of the other days works, except Friday.')]),
})

RETRIEVALS.update({
's3-u25':('三26 / 三72 / 三30 / 三70',[
('为了带书方便，我选这个布袋。','For carrying books conveniently, I choose this cloth bag.'),
('为了纪念见面，我们做一张贺卡。','To commemorate meeting, we make a greeting card.'),
('要是时间合适，就再问她。','If the time suits, ask her again.'),
('只有她同意，才写她的职业。','Only if she agrees do we write her occupation.')]),
's3-u26':('三27 / 三54 / 三31 / 三78',[
('衣服被雨弄湿了。','The clothes were made wet by rain.'),
('把这本书交给她。','Hand this book to her.'),
('哈哈，笑的是我自己。','Ha ha, I am laughing at myself.'),
('你今天也来参加活动？','Are you joining the event today too?')]),
's3-u27':('三28 / 三38 / 三32 / 三53',[
('除了看节目，我还听广播。','Besides watching programmes, I also listen to the radio.'),
('除了周五，其他几天都可以。','Any of the other days works, except Friday.'),
('老师张先生也来了。','Teacher Mr Zhang also came.'),
('她汉语说得很流利。','She speaks Chinese fluently.')]),
's3-u28':('三30 / 三70 / 三34 / 三68',[
('要是时间合适，就再问她。','If the time suits, ask her again.'),
('只有她同意，才写她的职业。','Only if she agrees do we write her occupation.'),
('她不慌不忙地核对地址。','She checks the address unhurriedly.'),
('好是好，不过地点还没确认。','It is good, but the location is still unconfirmed.')]),
})

RETRIEVALS.update({
's3-u29':('三31 / 三78 / 三35 / 三36',[
('哈哈，笑的是我自己。','Ha ha, I am laughing at myself.'),
('你今天也来参加活动？','Are you joining the event today too?'),
('她看起来很累，先问本人。','She looks tired; ask her first.'),
('照片看上去很亮，不说明现场温度。','The photo looks bright; it does not establish the temperature there.')]),
's3-u30':('三32 / 三53 / 三39 / 三52',[
('老师张先生也来了。','Teacher Mr Zhang also came.'),
('她汉语说得很流利。','She speaks Chinese fluently.'),
('从下周起，每天先读一段。','Starting next week, read a passage first each day.'),
('她离开这里三天了。','It has been three days since she left here.')]),
's3-u31':('三34 / 三68 / 三42 / 三59',[
('她不慌不忙地核对地址。','She checks the address unhurriedly.'),
('好是好，不过地点还没确认。','It is good, but the location is still unconfirmed.'),
('越听越累，就先停一下。','If listening makes you increasingly tired, stop briefly.'),
('她听汉语听得很认真。','She listens to Chinese carefully.')]),
's3-u32':('三35 / 三36 / 三43 / 三44',[
('她看起来很累，先问本人。','She looks tired; ask her first.'),
('照片看上去很亮，不说明现场温度。','The photo looks bright; it does not establish the temperature there.'),
('学习汉语需要时间。','Learning Chinese takes time.'),
('我希望大家都看懂说明。','I hope everyone understands the instructions.')]),
})

RETRIEVALS.update({
's3-u33':('三39 / 三52 / 三45 / 三56',[
('从下周起，每天先读一段。','Starting next week, read a passage first each day.'),
('她离开这里三天了。','It has been three days since she left here.'),
('朋友推荐的旅馆还没订。','The hotel recommended by the friend is not booked.'),
('我们去村里了解农业。','We go to the village to learn about agriculture.')]),
's3-u34':('三42 / 三59 / 三48 / 三50',[
('越听越累，就先停一下。','If listening makes you increasingly tired, stop briefly.'),
('她听汉语听得很认真。','She listens to Chinese carefully.'),
('这些邮件今天处理不了。','These emails cannot be dealt with today.'),
('我问了她三次。','I asked her three times.')]),
's3-u35':('三43 / 三44 / 三49 / 三75',[
('学习汉语需要时间。','Learning Chinese takes time.'),
('我希望大家都看懂说明。','I hope everyone understands the instructions.'),
('她笑得很开心。','She laughs happily.'),
('她一点儿也不生气。','She is not angry at all.')]),
's3-u36':('三45 / 三56 / 三55 / 三77',[
('朋友推荐的旅馆还没订。','The hotel recommended by the friend is not booked.'),
('我们去村里了解农业。','We go to the village to learn about agriculture.'),
('行李被同学移到门后了。','A classmate moved the luggage behind the door.'),
('我是来领行李的。','I came to collect the luggage.')]),
})

def apply(first, last):
    apply_ids(list(range(first,last+1)))

def apply_ids(ids):
    scripts=json.loads((ROOT/'content/audio-scripts.json').read_text('utf-8'))
    by_text={e['text']:e for e in scripts}
    for n in ids:
        if n not in RETRIEVALS:continue
        code, pairs=RETRIEVALS[n]
        uid=f's1-u{n:02}' if isinstance(n,int) else n
        path=ROOT/'content/packs'/f'{uid}.json'
        p=json.loads(path.read_text('utf-8'))
        task_pairs=[]
        for zh,en in pairs:
            source=by_text.get(zh,{})
            task_pairs.append(dict(left=en,right=dict(zh=zh,py=source.get('pinyin') or py(zh),en=en)))
        task=dict(type='match',id=f'{uid}-t9',phrase=p['vocabulary'][0]['id'],
                  title='Bring back earlier language',pairs=task_pairs)
        p['tasks']=[t for t in p['tasks'] if t['id']!=task['id']]+[task]
        p['notes']=p['notes'].split(' Planned retrieval ')[0]+f' Planned retrieval {code}: '+', '.join(zh for zh,_ in pairs)+'.'
        path.write_text(json.dumps(p,ensure_ascii=False,indent=2)+'\n','utf-8')

if __name__=='__main__':apply(13,16)
