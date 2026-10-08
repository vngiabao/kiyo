"""Four authored everyday scenes; default to drafts until preceding gates pass."""
import sys
from editorial_repair import repair, tf, reply, fill, match

SPECS={
37:dict(title=('A small business, a real plan','一起开一家小店'),
goals=['Explain the order of a shared plan','Add related reasons with 并且','Distinguish a completed opening from a future plan'],
dialogue=([
('你不是一直想创业吗？现在有想法了？',"Haven't you always wanted to start a business? Do you have an idea now?"),
('有。我想开一家小书店，周末开展读书活动。',"Yes. I'd like to open a small bookshop and hold reading events at weekends."),
('光卖书，生意会不会不太好？',"Would business be slow if you only sold books?"),
('所以我也想卖咖啡，并且留几张桌子给大家聊天。',"That's why I'd also sell coffee and leave a few tables for people to chat."),
('那首先得找地方吧？',"Then finding a space comes first, right?"),
('对，其次才是买书。我还没找到合适的店。',"Right, and buying books comes next. I haven't found a suitable place yet."),
('学校旁边有一家店关了。要不明天一起去看看？',"A shop near the school has closed. Shall we go and look tomorrow?"),
('好。你有朋友从事这种工作吗？我想听听他们的意见。',"Sure. Do you know anyone who works in this field? I'd like their advice."),
('有，我姐姐经营一家小店。我今晚问问她。',"Yes, my sister runs a small shop. I'll ask her tonight."),
('太好了！先请她喝杯咖啡，我的问题可能有点多。',"Great! I'll buy her a coffee first. I may have quite a few questions."),
], [('gist','What is the proposed business?',['A bookshop with coffee and reading events','A large factory','A bus company'],0),('detail','What does the speaker want to do first?',['Find a suitable space','Buy every book','Hire all the staff'],0),('inference','Why ask the sister?',['She has experience running a shop','She owns the school','She has already bought the bookshop'],0)]),
reading=([
('去年，我和朋友在学校附近开了一家书店。我们都没有经营经验，最初只想到书和咖啡。',"Last year a friend and I opened a bookshop near the school. Neither of us had experience running a business; initially we only thought about books and coffee."),
('看了几个地方以后，我们发现每个月的钱比想象的多。首先要交房租，其次要买材料，还得给职工发工资。',"After looking at a few spaces, we found the monthly costs were higher than expected: rent first, then supplies, and wages for staff."),
('朋友的姐姐从事餐饮工作。她把我们的计划展开在桌上，一项一项地问。我们回答不上来，就一起去了解。',"My friend's sister works in catering. She spread our plan on the table and went through it item by item. When we couldn't answer, we went to find out together."),
('小店开门后，生意并不是每天都好。有时一下午只卖出两本书，但读书活动慢慢有了固定的朋友。',"After we opened, business wasn't good every day. Sometimes we sold only two books all afternoon, but our reading events slowly attracted a regular group."),
('我们没有急着扩大店面，而是先建立自己的读书小组，每周开展一次活动，并且听大家想读什么。',"Instead of rushing to expand, we set up our own reading group, met weekly and listened to what people wanted to read."),
('现在我仍然喜欢这份事业。不过，喜欢书和经营书店是两回事，后者每天都有很多小事要做。',"I still love this work. But loving books and running a bookshop are different things: the latter comes with lots of small daily tasks."),
], [('gist','What has the narrator learned?',['Running a bookshop involves more than liking books','A bookshop never needs supplies','Reading groups always bring immediate profit'],0),('detail','What did the sister do?',['Discussed the plan item by item','Bought the school','Paid every wage herself'],0),('inference','Why did they avoid immediate expansion?',['They chose to develop a regular reading group first','They had sold all their books','The sister prohibited coffee'],0)]),
media=([
('这张桌子也算我们的事业吗？',"Does this table count as part of our business too?"),
('算啊。先别笑，帮我把它搬过去。',"Of course. Stop laughing and help me move it."),
('你不是说今天只看地方，不干活吗？',"Didn't you say we were only looking at spaces today, not working?"),
('是，可老板明天要清空这里。我怕来晚了桌子就没了。',"Yes, but the owner is clearing this place tomorrow. I'm worried the table will be gone if we come late."),
('好吧。首先搬桌子，其次请我吃饭。',"Fine. First we move the table, then you buy me dinner."),
('没问题。并且我会记住你今天帮了我。',"Deal. And I'll remember that you helped me today."),
], [('detail','Why move the table today?',['The owner will clear the space tomorrow','The bookshop has closed permanently','The table is already at home'],0),('inference','What does the friend ask for in return?',['Dinner','A salary for a year','Ownership of the shop'],0)]),
glosses=[('房租','rent'),('餐饮','food and catering'),('店面','shop premises'),('清空','clear out; empty')],
examples={
'建':('这座桥是十年前建的。','This bridge was built ten years ago.'),
'建成':('学校的新楼去年建成了。',"The school's new building was completed last year."),
'建设':('新车站的建设要花两年。','Construction of the new station will take two years.'),
'设立':('学校在北门设立了一个报名点。','The school set up a registration point at the north gate.'),
'厂':('我爸爸以前在汽车厂工作。','My dad used to work in a car factory.'),
'职工':('这家店只有五位职工。','This shop has only five employees.'),
'事业':('她喜欢自己的事业，也喜欢和家人在一起。','She loves her career and spending time with her family.'),
'推动':('新的活动推动了两所学校的交流。','The new activity promoted exchange between the two schools.'),
'推进':('他们每周开一次会，讨论怎样推进项目。','They meet weekly to discuss how to move the project forward.'),
'工资':('这个月的工资已经发了。',"This month's wages have been paid."),
'人才':('公司想找懂设计的人才。','The company is looking for talented people who know design.'),
},
contexts=[
('首先买票，然后找座位。','First buy a ticket, then find a seat.'),('我喜欢这家店，首先是因为近，其次是因为安静。','I like this place first because it is nearby, and secondly because it is quiet.'),
('我们准备开展一次旧书交换活动。',"We're planning a second-hand book exchange."),('她展开地图，指了指北边的小路。','She spread out the map and pointed at a small road to the north.'),
('他们在河上建了一座桥。','They built a bridge over the river.'),('新图书馆建成以后，我几乎每天都去。','After the new library was completed, I went almost every day.'),
('我们在第一次活动后建立了一个群。','We set up a group chat after the first event.'),('附近正在建设新的地铁站。','A new underground station is being built nearby.'),
('这个读书小组成立三年了。','This reading group was founded three years ago.'),('图书馆设立了儿童阅读区。','The library set up a reading area for children.'),
('那家厂现在不生产汽车了。','That factory no longer makes cars.'),('她毕业后和朋友一起创业。','After graduating she started a business with a friend.'),
('我姐姐从事翻译工作。','My sister works as a translator.'),('他们一家经营这家店十多年了。','Their family has run this shop for over ten years.'),
('周末生意很好，老板忙得没时间吃饭。','Business is good at weekends; the owner is too busy to eat.'),('她用第一份工资给妈妈买了礼物。','She bought her mum a gift with her first pay.'),
('所有职工都可以参加周五的活动。','All employees can join the Friday event.'),('学校周六有就业介绍会。','The school has a careers event on Saturday.'),
('她把大部分时间都用在自己的事业上。','She spends most of her time on her career.'),('这家公司需要会两种语言的人才。','This company needs talented people who speak two languages.'),
('朋友的鼓励推动我完成了这个计划。',"My friend's encouragement helped me complete the plan."),('我们先解决最急的问题，再推进其他工作。',"We'll solve the most urgent problem first, then move the other work forward."),
],
usage=[('Offer help without taking over','要不我陪你去看看？','Shall I come and have a look with you?','要不 offers a tentative suggestion, leaving room to decline.'),('Ask an experienced friend','我有几个问题想请教你。',"I'd like to ask you about a few things.",'请教 recognizes the listener’s experience; it need not sound formal or grand.')],
turns=[('你想先做什么？','What do you want to do first?','State the first step',['我想先找一个合适的地方。']),('买书的钱准备好了吗？','Have you put aside money for books?','Explain what comes next',['还没有。我先找地方，其次才是买书。']),('要不要问问我姐姐？','Would you like to ask my sister?','Accept the offer',['好啊，我想听听她的意见。'])],
review='Bookshop plan: believable shared decision, natural 首先/其次/并且, plans separated from completed actions, every comprehension key checked against the text. Check 餐饮 and 请教 register with a native speaker.'),
38:dict(title=('Which course fits my week?','选一门能坚持的课'),
goals=['Compare two courses using 不仅…还…','State a repeated either-or pattern with 不是…就是…','Explain a choice using time, tuition and learning goals'],
dialogue=([
('你留学的材料准备好了吗？',"Have you prepared your study-abroad documents?"),
('差不多了。现在最难的是选专业。',"Almost. The hardest part now is choosing a subject."),
('你不是想学中文吗？',"Didn't you want to study Chinese?"),
('对，但我也想学设计。中文系的课不仅多，还要写很多作业。',"Yes, but I also want to study design. The Chinese department has lots of classes and a lot of written work."),
('能把两个专业结合起来吗？',"Could you combine the two subjects?"),
('我问过老师，可以先学中文，再选几门设计课。',"I asked a teacher. I can start with Chinese and take a few design classes later."),
('那学费会增加吗？',"Would the tuition go up?"),
('不会。但是我刚过去，可能需要时间适应。',"No, but I'll probably need time to settle in when I first arrive."),
('你现在不是上班就是上课，确实够忙的。',"You're always either working or in class now. You really are busy."),
('所以我想先少选一点。有空再和同学交流，别每天只赶作业。',"That's why I want to take fewer classes at first, and have time to talk with classmates rather than just rush through assignments."),
], [('gist','What is the main decision?',['How to combine language and design study','Which factory to buy','How to become the institute director'],0),('detail','Will tuition increase under the proposed arrangement?',['No','Yes, it doubles','The teacher refuses to say'],0),('inference','Why choose fewer classes at first?',['To have time to adapt and meet classmates','To avoid learning Chinese entirely','To finish two degrees in one week'],0)]),
reading=([
('到新的学校以后，我本来想把每个晚上都安排成学习时间。周一和周三上中文课，周二和周四去设计室，周五参加交流活动。',"When I arrived at my new school, I initially planned to study every evening: Chinese on Mondays and Wednesdays, the design studio on Tuesdays and Thursdays, and an exchange event on Fridays."),
('第一周，我不是在教室就是在路上。回到住处已经很晚，连朋友发来的消息都没有时间看。',"In the first week I was either in a classroom or on the road. I got home so late I didn't even have time to read friends' messages."),
('后来，老师让我写下自己真正想做的事。我想不仅看懂外文材料，还能和同学讨论自己的作品。',"Later my teacher asked me to write down what I really wanted to do. I wanted to read material in another language and discuss my work with classmates."),
('我发现一门课同时包括这两部分，而且教室离住处只有几百米。教室面积较小，但每个人都能说话。',"I found a class covering both parts, with a classroom just a few hundred metres from home. The room was relatively small, but everyone got a chance to speak."),
('我于是减少了晚上的课程。两周内，我认识了几位新朋友，也渐渐适应了课堂的节奏。',"So I reduced my evening classes. Within two weeks I had met some new friends and gradually adjusted to the pace of class."),
('现在我仍然学得很认真，不过周五晚上有时只和朋友散步。能坚持下去的安排，比满满一张表更适合我。',"I still study seriously, but sometimes on Friday evenings I just walk with friends. A schedule I can maintain suits me better than a completely full timetable."),
], [('gist','What changes in the narrator’s schedule?',['Fewer classes, with more time to adapt and socialize','Every evening becomes longer','All learning is abandoned'],0),('detail','How far is the new class from home?',['A few hundred metres','Hundreds of kilometres','Exactly two metres'],0),('inference','What does the narrator value most by the end?',['A sustainable routine','The largest possible classroom','Having the fullest timetable'],0)]),
media=([
('今晚又上课？',"Class again tonight?"),('不上。我终于有空一起吃饭了。',"No. I finally have time to have dinner with you."),
('真难得。你上个月不是上课就是写作业。',"What a rare occasion! Last month you were always either in class or doing homework."),
('我少选了一门。学习不是把日历填满就行。',"I dropped one class. Filling my calendar isn't all there is to learning."),
('那太好了。你选饭馆，我请客。',"Great. You choose the restaurant; dinner's on me."),
('等等，选课我想了两周，选饭馆你给我几分钟？',"Wait. I spent two weeks choosing a class. How many minutes do I get to choose a restaurant?"),
], [('detail','Why is the friend free tonight?',['They reduced their courses','The school has permanently closed','They finished all homework for the year'],0),('inference','What makes the last line playful?',['It compares a small choice with a major decision','It announces a new tuition charge','It refuses dinner permanently'],0)]),
glosses=[('设计室','design studio'),('住处','place to live'),('节奏','pace; rhythm'),('填满','fill completely')],
examples={'交流':('吃饭时，我们交流了学中文的方法。','Over dinner we shared our ways of learning Chinese.'),'外文':('这本外文书有中文译本。','This foreign-language book has a Chinese translation.'),'室':('会议室在二楼。','The meeting room is on the second floor.'),'所':('这是一所新学校。','This is a new school.'),'较':('这间房较小，适合两个人住。','This room is comparatively small and suits two people.'),'比例':('班里留学生的比例大约是三分之一。','International students make up about a third of the class.'),'面积':('这间教室的面积有六十平方米。','This classroom has an area of sixty square metres.'),'米':('我住的地方离学校五百米。','I live five hundred metres from school.'),'公民':('她是中国公民。','She is a Chinese citizen.'),'老百姓':('这部电影讲老百姓的生活。','This film is about ordinary people’s lives.')},
contexts=[('她把语言学习和设计结合起来。','She combines language study and design.'),('我想和不同专业的同学交流。',"I'd like to talk with students in different subjects."),('我姐姐去年去北京留学了。','My sister went to study in Beijing last year.'),('学费可以分两次交。','Tuition can be paid in two instalments.'),('他每天读半小时外文报纸。','He reads a foreign-language newspaper for half an hour every day.'),('中文系的办公室在三楼。',"The Chinese department's office is on the third floor."),('你的专业是设计还是中文？','Is your subject design or Chinese?'),('请到会议室等我。','Please wait for me in the meeting room.'),('这所学校有五百名学生。','This school has five hundred students.'),('所长今天不在办公室。','The institute director is not in the office today.'),('她很快适应了这里的生活。','She quickly adjusted to life here.'),('这个房间的光线较好。','This room has comparatively good light.'),('选这门课的学生中，女生的比例较高。','A relatively high proportion of the students choosing this class are women.'),('房间面积不大，但住起来很舒服。','The room has a small area but is comfortable to live in.'),('先向北走两百米，再向右转。','Go north two hundred metres, then turn right.'),('请在三天内给我回复。','Please reply within three days.'),('这些人当中，有几个是我的老朋友。','Several people among this group are old friends of mine.'),('你周五有空儿吗？','Are you free on Friday?'),('那位老太太经常坐在这里看书。','That elderly woman often sits here reading.'),('我爷爷笑着说，他就是一个爱唱歌的老头儿。',"My grandpa laughs and says he's just an old man who loves singing."),('这条路方便了附近的老百姓。','This road made life easier for ordinary people nearby.'),('每个公民都有自己的权利和义务。','Every citizen has rights and responsibilities.')],
usage=[('Choose a manageable schedule','我想先少选一门。',"I'd like to take one fewer class at first.",'少选一门 means one fewer course; 少选一点 leaves the amount open.'),('Refer to an older stranger','那位老人需要帮忙吗？','Does that older person need help?','老人 is a safer neutral reference to a stranger. 老头儿 can be familiar, self-deprecating or dismissive depending on the relationship.')],
turns=[('你想学什么？','What would you like to study?','Describe two interests',['我想学中文，也想学设计。']),('为什么不把每天都安排满？','Why not fill every day?','Explain your preference',['我想留一点时间和同学交流。']),('选好了以后告诉我。','Tell me when you’ve chosen.','Reply with a time frame',['好，我三天内给你回复。'])],
review='Course-choice scene: 不仅/还 and 不是/就是 used conversationally; tuition, area and distance facts checked. Elders’ labels kept contextual rather than generic address. Native check: 所长 context and 老头儿 self-reference.'),
39:dict(title=('What did our weekend cost?','周末的钱怎么算'),
goals=['Use 做完了就… to order completed actions','Compare an estimate with the final amount','Explain a travel choice and split actual costs'],
dialogue=([
('昨天的车费你算好了吗？',"Have you worked out yesterday's fares?"),('算了。四个人一共一百二十，每人三十。',"Yes. A hundred and twenty for four people, so thirty each."),
('那饭钱呢？我记得大约两百。',"What about dinner? I remember it being about two hundred."),('实际是一百八十。你们把钱转给我，我收到了就发收据。',"It was actually a hundred and eighty. Transfer me the money and I'll send the receipt when I get it."),
('所以每人一共七十五？',"So seventy-five each in total?"),('对。比上次增加了十块，主要是车费涨了。',"Right. Ten more than last time, mainly because fares went up."),
('不过那个市场挺值得去的，小吃很有特色。',"Still, that market was worth visiting. The snacks were distinctive."),('我也觉得值。下次早一点去，坐公交车能省一点。',"I think it was worth it too. Next time let's go earlier; taking the bus would save a bit."),
('行，我转完钱就把照片发群里。',"Okay. I'll send the photos to the group after transferring the money."),('先把我闭着眼的那张删了，求你了。',"Please delete the one where my eyes are shut first. I'm begging you."),
], [('detail','What is each person’s total share?',['75 yuan','30 yuan','120 yuan'],0),('detail','What mainly increased?',['The fare','The number of travellers','The price of every snack'],0),('inference','Why go earlier next time?',['To use a cheaper transport option','To avoid the market entirely','To stop eating together'],0)]),
reading=([
('周六，我们四个人去了城南的市场。出发前，大家预计每人花七十块左右，车费和饭钱都算在里面。',"On Saturday four of us went to the market in the south of town. Before leaving we estimated around seventy yuan each, including transport and dinner."),
('那天起床晚了，到了车站才发现公交车刚走。我们等了一会儿，就决定一起打车。',"We got up late and discovered at the station that the bus had just left. After waiting a while, we decided to share a taxi."),
('市场比照片上热闹。当地的小吃很有特色，同一种商品在不同店里的价格也不一样。',"The market was livelier than in the photographs. The local snacks were distinctive, and the same goods had different prices in different shops."),
('朋友买完东西就去问路，我们在旁边等她。老板介绍了一家饭馆，四个人吃饭一共花了一百八十。',"Once my friend had finished shopping she asked for directions while we waited nearby. A shopkeeper recommended a restaurant, where dinner for four cost a hundred and eighty."),
('回家以后，我们把每一笔钱加起来。车费一百二十，饭钱一百八十，购物的钱各自付。最后每人七十五，比预计多了五块。',"Back home we added up the shared expenses: a hundred and twenty for fares and a hundred and eighty for dinner, with shopping paid separately. Each person owed seventy-five, five more than estimated."),
('虽然多花了一点，我仍然觉得这次出门值得。下次早点出发，不仅能少等一会儿，也能坐公交车省钱。',"Although we spent a little more, I still thought the trip was worthwhile. Leaving earlier next time would mean less waiting and saving money by taking the bus."),
], [('gist','What does the reading describe?',['A trip and the final division of shared costs','A plan to invest in a market','A cancelled dinner'],0),('detail','How was shopping paid for?',['Each person paid for their own purchases','It was included in the shared 75 yuan','The shopkeeper paid'],0),('inference','What caused the estimate to differ from the final cost?',['The group took a taxi after missing the bus','One person paid everyone’s shopping','The group had eight members'],0)]),
media=([
('你不是说大约七十吗？',"Didn't you say about seventy?"),('最后七十五，差五块。',"It came to seventy-five. Five more."),
('那照片里的我怎么比平时胖了五倍？',"Then why do I look five times bigger than usual in that photo?"),('你穿了两件外套，不是五倍。',"You're wearing two coats. Not five times bigger."),
('照片不好看，我要再拍一次。',"That photo isn't good. I want to take another one."),('行。你把外套放下，我准备好了就拍。',"Okay. Put the coats down. I'll take it when I'm ready."),
], [('detail','What is the additional expense per person?',['Five yuan','Seventy-five yuan','Five times the total'],0),('inference','Why is 五倍 an exaggeration here?',['The speaker dislikes how they look in a photograph','The fare literally multiplied by five','They measured the coats’ area'],0)]),
glosses=[('收据','receipt'),('预计','estimate; expect'),('各自','each separately')],
examples={'任':('任你怎么劝，他都不肯离开。',"No matter how you try to persuade him, he won't leave."),'为':('她被选为组长。','She was chosen as group leader.'),'某':('某一天，我们还会再见面。',"We'll meet again someday."),'商品':('这家店的商品都有价格。','All the goods in this shop have prices.'),'商业':('这条街是一个热闹的商业区。','This street is a lively commercial area.'),'经济':('旅游给当地的经济带来了变化。','Tourism brought changes to the local economy.'),'增长':('去年游客的人数增长了。','Visitor numbers increased last year.'),'石油':('新闻说石油价格又涨了。','The news says oil prices have risen again.'),'环境':('我喜欢这里安静的环境。','I like the quiet surroundings here.'),'环保':('我们带自己的杯子，更环保。','Bringing our own cups is better for the environment.'),'值':('这张票值五十块。','This ticket is worth fifty yuan.'),'升':('请给车加二十升汽油。','Please put twenty litres of petrol in the car.')},
contexts=[('任他说什么，我都想自己试试。','Whatever he says, I want to try it myself.'),('这位老师被大家称为老朋友。','Everyone calls this teacher an old friend.'),('某个周末，我们可以一起去海边。','We could go to the beach together one weekend.'),('排队买票太费时间了。','Queuing for tickets takes too much time.'),('这件商品可以退吗？','Can I return this item?'),('学校旁边有一个商业中心。','There is a shopping and business centre near the school.'),('这个市场周一不开放。','This market is closed on Mondays.'),('她在大学学经济。','She studies economics at university.'),('春天到了，气温逐渐上升。','As spring arrives, the temperature gradually rises.'),('我们又增加了两个座位。','We added two more seats.'),('小店的收入每年都在增长。',"The small shop's income increases every year."),('房间的温度升了两度。','The room temperature went up two degrees.'),('这么好的书，值这个价。','A book this good is worth the price.'),('为了这场演出跑这么远，值得吗？','Is travelling this far for the performance worthwhile?'),('她的声音在合唱里特别突出。','Her voice really stands out in the choir.'),('这里的特色是手工做的面条。',"The speciality here is handmade noodles."),('手机支付已经很普及了。','Mobile payment is now widespread.'),('这座城市的公共交通很发达。',"This city's public transport is well developed."),('这种原料来自石油。','This raw material comes from petroleum.'),('这条路线绕湖一环。','This route makes one loop around the lake.'),('学校举办了一次环保活动。','The school held an environmental protection event.'),('窗外的环境很安静。','The surroundings outside the window are very quiet.')],
usage=[('Check the total','我算得对不对？','Have I worked it out correctly?','An open check is friendlier than assuming the other person has made a mistake.'),('Thank a friend for paying first','谢谢你先帮我们付了。','Thanks for paying for us first.','先 acknowledges that the payment will be settled later.')],
turns=[('一共三百，四个人分，怎么算？','Three hundred in total, split between four. What is each share?','State the share',['每人七十五块。']),('你什么时候发照片？','When will you send the photos?','Sequence two actions',['我转完钱就发照片。']),('下次还去吗？','Will you go again next time?','Explain your choice',['还去，我觉得很值得。'])],
review='Trip budget: arithmetic 120+180=300, four shares of 75; forecast 70 versus actual 75, each person’s shopping excluded. Completed-action 就 in new contexts; no commercial advice in dialogue. Native check: 绕湖一环 and comic 五倍 delivery.'),
40:dict(title=('The last guests go home','都这么晚了'),
goals=['Express surprise at an already late time with 都…了','Accept a modest compromise with X就X点吧','End a friendly visit without sounding abrupt'],
dialogue=([
('都十一点了，我们是不是该走了？',"It's already eleven. Shouldn't we get going?"),('再坐一会儿吧。我爸退休以后，就喜欢家里热闹。',"Stay a little longer. Since my dad retired, he loves having people around."),
('我也想多聊，可明天还要早起。',"I'd like to keep talking too, but I have to get up early tomorrow."),('那我送你到楼下。路上慢一点。',"Then I'll walk you downstairs. Take your time on the way."),
('刚才空调开得太冷了，我手指都凉了。',"The air conditioning was so cold earlier that even my fingers feel cold."),('怪不得你一直抱着杯子。我还以为你特别喜欢那杯水。',"That explains why you kept holding your cup. I thought you really liked that water."),
('凉水我怎么会一直想喝啊？',"Why would I keep wanting cold water?"),('是我忘了关。下次你直接告诉我。',"I forgot to turn it off. Tell me directly next time."),
('好。对了，周六的聚会我可能晚一点到。',"Okay. By the way, I might arrive a little late on Saturday."),('晚就晚点吧，你来了就好。到时候再聊。',"A little late is fine. I'm happy as long as you come. We'll talk then."),
], [('gist','What are the friends doing?',['Ending a visit','Opening a hospital','Taking a written test'],0),('detail','Why does one friend need to leave?',['They must get up early','They dislike the father','The police called them'],0),('inference','What does 晚就晚点吧 convey?',['A little lateness is acceptable','The invitation is cancelled','Everyone must arrive at eleven'],0)]),
reading=([
('星期五晚上，我们去朋友家给她爸爸庆祝退休。他以前是大夫，工作忙的时候常常很晚才回家。',"On Friday evening we visited a friend to celebrate her dad's retirement. He used to be a doctor and often got home very late when work was busy."),
('那天他给大家讲以前的事：一次紧急电话、一个多年后又见到的病人，还有一个怕打针的孩子。大家听着听着都笑了。',"That evening he told us stories: an urgent phone call, a patient he met again years later, and a child afraid of injections. As we listened, we all started laughing."),
('饭后，他拿出照片。最旧的一张已经看不清了，他却还记得照片上每个人的名字。',"After dinner he brought out photographs. The oldest one had faded, but he still remembered everyone in it."),
('十一点多，我看了一眼墙上的钟。朋友说明天可以晚起，我却还有早上的课，只好先告别。',"After eleven I glanced at the wall clock. My friend said we could get up late the next day, but I had a morning class and had to say goodbye first."),
('他送我们到门口，说慢就慢点吧，别急，下次再来。我答应周六带自己做的点心来。',"He walked us to the door and said to take our time and visit again. I promised to bring homemade snacks on Saturday."),
('走到楼下，我才发现外套还在椅子上。都告别两次了，我又得回去一次。朋友打开门，笑着问我是不是又饿了。',"Downstairs I realised my coat was still on a chair. I'd already said goodbye twice, and now I had to go back again. My friend opened the door and laughed, asking if I was hungry again."),
], [('gist','What is being celebrated?',['The father’s retirement','A new hospital opening','The narrator’s graduation'],0),('detail','Why does the narrator return upstairs?',['A coat was left behind','Dinner had not started','The clock was broken'],0),('inference','What suggests the host is welcoming?',['He invites them back and jokes when the narrator returns','He refuses to open the door','He asks them never to visit again'],0)]),
media=([
('你怎么又回来了？',"Why are you back again?"),('外套忘了。',"I forgot my coat."),
('都说了三次再见了，这回真的走？',"We've said goodbye three times now. Are you really leaving this time?"),('真的。慢就慢点吧，我总会到家的。',"Yes. I'll get home eventually, even if I take my time."),
('等等，你的手机呢？',"Wait. Where's your phone?"),('别吓我！在口袋里。',"Don't scare me! It's in my pocket."),
], [('detail','What was left behind?',['A coat','The phone','A bag of books'],0),('inference','What is the host teasing the guest about?',['The repeated goodbyes','Their medical knowledge','Their unwillingness to visit'],0)]),
glosses=[('打针','have an injection'),('点心','snack; pastry'),('告别','say goodbye')],
examples={'大夫':('我明天去看大夫。',"I'm seeing the doctor tomorrow."),'公务员':('我姐姐是公务员，在市里工作。','My sister is a civil servant and works for the city.'),'否定':('他没有否定我的想法，只是提出了两个问题。',"He didn't reject my idea; he just asked two questions."),'紧急':('这是一条紧急通知，请尽快回复。','This is an urgent notice; please reply as soon as possible.'),'交警':('交警站在路口指挥车辆。','A traffic officer is directing vehicles at the junction.'),'警察':('我在车站找到了警察。','I found a police officer at the station.'),'救':('邻居救了那只小猫。','A neighbour rescued the kitten.'),'危害':('这种做法会危害环境。','This practice harms the environment.'),'卫生':('厨房打扫以后，卫生好多了。','The kitchen is much cleaner after it was tidied.'),'血':('他的手指流了一点血。','His finger bled a little.'),'离婚':('他们离婚以后仍然一起照顾孩子。','They still look after their child together after divorcing.'),'凉水':('天太热了，我想喝一杯凉水。',"It's so hot. I'd like a glass of cool water."),'压':('别把书压在花上。',"Don't put the book on top of the flowers."),'手指':('她的手指很灵活，钢琴弹得很好。','Her fingers are nimble, and she plays the piano well.')},
contexts=[('那位大夫对每个人都很耐心。','That doctor is patient with everyone.'),('她考上了公务员，准备回老家工作。','She passed the civil service exam and is preparing to work in her hometown.'),('他去年调到北京工作了。','He transferred to Beijing for work last year.'),('学校在调查学生想选哪些课。','The school is surveying which classes students want to take.'),('这次失败不等于否定以前的努力。',"This failure doesn't negate the earlier effort."),('她否认拿过那本书。','She denies having taken that book.'),('他接到紧急电话，马上离开了。','He received an urgent call and left immediately.'),('交警让我从另一个路口走。','The traffic officer told me to use another junction.'),('警察帮孩子找到了妈妈。','The police helped the child find their mum.'),('他从河里救了一只狗。','He rescued a dog from the river.'),('污染会危害人和动物。','Pollution harms people and animals.'),('这家饭馆很注意卫生。','This restaurant pays close attention to hygiene.'),('卫生间在走廊尽头。','The bathroom is at the end of the corridor.'),('她看到血就有点害怕。','She gets a little scared when she sees blood.'),('阳台上的花死了，我又种了一棵。','The plant on the balcony died, so I planted another.'),('我爸爸退休以后开始学画画。','My dad started learning to paint after retiring.'),('电影里那对夫妻最后离婚了。','The couple in the film divorced at the end.'),('房间太冷，先把空调关了吧。',"It's too cold in here. Let's turn the air conditioning off."),('杯子里的凉水已经喝完了。','The cool water in the cup has all been drunk.'),('她用手指在地图上画了一条路。','She traced a route on the map with her finger.'),('书太重，把盒子压坏了。','The books were so heavy that they crushed the box.'),('墙上的钟比手机快五分钟。','The wall clock is five minutes ahead of the phone.')],
usage=[('Leave warmly','今天很开心，我得先走了。',"I've had a lovely time. I need to get going.",'Give a warm closing before the reason; 得 signals your need to leave.'),('Accept a small delay','晚就晚点吧，你来了就好。',"A little late is fine. I'm happy as long as you come.",'X就X点吧 accepts a modest compromise; tone and context determine whether it sounds relaxed or resigned.')],
turns=[('还想再坐一会儿吗？','Would you like to stay a little longer?','Decline with a reason',['我明天还要早起，得先走了。']),('周六能准时到吗？','Can you arrive on time on Saturday?','State a possible delay',['我可能晚一点到。']),('怎么又回来了？','Why are you back?','Explain a forgotten item',['我的外套忘在椅子上了。'])],
review='Friendly departure: late-time 都…了, compromise X就X点吧, coat/phone continuity, no fabricated clinical advice. Check colloquial 血 reading and the doctor’s remembered family stories with a native speaker.'),
}

SECOND_CONTEXTS={
37:[
('新体育馆已经建成，下个月就能用了。','The new sports hall is complete and will be usable next month.'),
('这条路还在建设，公交车得绕一下。','This road is still under construction, so buses have to take a detour.'),
('我们三年前成立了这个乐队。','We formed this band three years ago.'),
('医院在门口设立了临时咨询点。','The hospital set up a temporary information point at the entrance.'),
('这家厂以前生产自行车。','This factory used to make bicycles.'),
('毕业前，老师给我们介绍了几种就业机会。','Before graduation, our teacher told us about several job opportunities.'),
('我们公司正在找设计方面的人才。','Our company is looking for talented designers.'),
('这次合作推动了两个小组的交流。','This collaboration encouraged exchange between the two groups.'),
('材料到了，我们终于能推进下一步工作了。','The materials have arrived, so we can finally move the next stage forward.'),
],
38:[
('所长今天不在，明天才回来。','The institute director is away today and returns tomorrow.'),
('这张地图的比例不对，学校看起来比城市还大。','The scale of this map is wrong; the school looks bigger than the city.'),
('我们当中有三个人会开车。','Three of us can drive.'),
('周五有空儿的话，一起吃饭吧。','If you have some free time on Friday, let’s have dinner.'),
('门口那位老太太是我邻居。','The elderly lady at the door is my neighbour.'),
('那个老头儿每天都来这里喝茶。','That old man comes here for tea every day.'),
('老百姓买菜比以前方便多了。','Buying groceries is much more convenient for ordinary people now.'),
('每个公民都有自己的权利，也有义务。','Every citizen has rights as well as responsibilities.'),
],
39:[
('任他怎么叫，小猫都不肯出来。','However much he calls, the kitten refuses to come out.'),
('他不想说某个人的名字，只告诉我那是以前的同学。','He didn’t want to name a certain person, only saying it was a former classmate.'),
('这条街以前是商业街，现在大部分店都搬走了。','This used to be a shopping street; most shops have moved away now.'),
('这篇文章讲的是当地的经济。','This article is about the local economy.'),
('河里的水位上升了，大家别靠近岸边。','The river level has risen; keep away from the bank.'),
('这个月，来图书馆的人数增长了不少。','The number of library visitors has grown considerably this month.'),
('海报上最突出的字是活动日期。','The most prominent words on the poster are the event date.'),
('手机已经很普及，买票也越来越方便。','Mobile phones are widespread now, and buying tickets is becoming easier.'),
('这里公共交通很发达，不开车也能到很多地方。','Public transport is well developed here; you can get to many places without a car.'),
('这家公司以前主要做石油生意。','This company used to deal mainly in oil.'),
('我买了一个环保袋，以后不用每次都拿新袋子。','I bought a reusable bag so I won’t need a new bag every time.'),
('这家店环境安静，很适合看书。','This shop has a quiet atmosphere and is a good place to read.'),
],
40:[
('她考上了公务员，明年开始上班。','She passed the civil-service recruitment exam and starts work next year.'),
('调查结果出来以后，学校决定延长图书馆的开放时间。','After the survey results came out, the school decided to extend library opening hours.'),
('老师没有否定我的想法，只让我再改一改。','The teacher didn’t reject my idea, just asked me to revise it.'),
('他否认拿过这本书，但我还没找到它。','He denies taking this book, but I haven’t found it yet.'),
('交警站在路口，让车先停下来。','A traffic officer stood at the junction and stopped the cars first.'),
('我在车站找不到包，就去找警察帮忙。','I couldn’t find my bag at the station, so I asked the police for help.'),
('路人把掉进水里的小狗救了上来。','A passer-by rescued the puppy that had fallen into the water.'),
('乱扔垃圾会危害河里的动物。','Littering can harm animals in the river.'),
('卫生间在走廊尽头，左边那扇门。','The toilet is at the end of the corridor, through the door on the left.'),
('他手指破了，流了一点血。','He cut his finger and it bled a little.'),
('院子里的树死了，我们准备种一棵新的。','The tree in the courtyard died; we plan to plant a new one.'),
('他们离婚以后，还是一起照顾孩子。','After their divorce, they still look after their child together.'),
('别把书压在眼镜上，会压坏的。','Don’t put books on the glasses; they’ll get crushed.'),
]}
for number,s in SPECS.items():
    s['contexts'].extend(SECOND_CONTEXTS[number])
    s['examples'].update({
      37:{'生意':('最近生意不太好，老板准备少进一点货。','Business has been slow recently, so the owner plans to order less stock.')},
      38:{'内':('请在三天内回复这封邮件。','Please reply to this email within three days.'),'当中':('我们当中有两个人是第一次来。','Two of us are visiting for the first time.'),'老头儿':('那个老头儿坐在树下听收音机。','That old man is sitting under the tree listening to the radio.')},
      39:{'任':('任你怎么劝，他都不肯离开。','No matter how you try to persuade him, he won’t leave.'),'升':('太阳慢慢升起来了。','The sun is slowly rising.'),'环':('她用线把两个环连在一起。','She joined two rings together with string.'),'市场':('早上的市场很热闹，我买了些新鲜的水果。','The morning market was lively; I bought some fresh fruit.'),'值得':('这部电影值得再看一遍。','This film is worth watching again.'),'特色':('这家店的特色是手工做的面。','This shop specialises in handmade noodles.'),'发达':('这里交通很发达，去机场也不用开车。','Transport here is well developed; you don’t need a car to reach the airport.')},
      40:{'死':('这棵树去年冬天死了。','This tree died last winter.')},
    }[number])
    if number==39:
        # The source row is 升 (verb), not the litre measure. 任 is the
        # conjunction reading/sense, not the unrelated hold-office verb.
        s['vocabularyFields']={'升':dict(meaning='rise; go up',meaningVi='tăng; lên',pos='verb')}
        s['contexts']=[('气温升到三十度，大家都躲到树下。','The temperature rose to thirty degrees, and everyone took shelter under the trees.') if z=='温度上升了两度。' else ('这个环可以挂钥匙。','This ring can hold keys.') if z=='这条路线绕湖一环。' else (z,e) for z,e in s['contexts']]
        s['contexts'].extend([('太阳从山后升起来了。','The sun rose from behind the mountains.'),('她用线把两个环连在一起。','She joined two rings together with string.')])
        s['glosses'].extend([('钥匙','key'),('躲','take shelter; hide')])
    # Assessment sentences are new contexts, with old IDs retained for review.
    d=s['dialogue'][0]; r=s['reading'][0]
    s['tasks']=[
      tf(d[1][0],d[1][1],s['dialogue'][1][0][2][0],False,'This statement is not the information in the spoken line.'),
      tf(r[0][0],r[0][1],s['reading'][1][0][2][0],True,'The line introduces this situation.'),
      reply(*d[0],[d[1][0],d[3][0],d[-1][0]],0,'This directly answers the preceding question.'),
      reply(*d[-2],[d[-1][0],d[1][0],d[3][0]],0,'This response fits the question and situation.'),
      fill(*s['contexts'][0], next(iter({37:['首先'],38:['结合'],39:['任'],40:['大夫']}[number]))),
      fill(*s['contexts'][1],{37:'其次',38:'交流',39:'为',40:'公务员'}[number]),
      match(s['contexts'][2:5]),match(s['contexts'][5:8]),match(s['contexts'][-3:]),
    ]
    # The two true/false statements are authored facts rather than loose passage labels.
    facts={37:('The speaker wants to open a car factory.','Two friends opened a bookshop last year.'),38:('The speaker’s hardest task is finding a restaurant.','The narrator planned classes or activities every evening.'),39:('Each person’s fare is 120 yuan.','Four people planned to visit a market on Saturday.'),40:('The father retired from the police.','The visitors are celebrating a doctor’s retirement.')}
    s['tasks'][0]['statement'],s['tasks'][1]['statement']=facts[number]
    followups={
      37:[('你为什么也想卖咖啡？','Why do you also want to sell coffee?',['这样大家可以坐下来聊天。','因为我不想开店了。','因为这家店不卖书。'],0,'Coffee and seating support the social purpose.'),('你想先买书吗？','Do you want to buy books first?',['不，我想先找地方。','对，我已经买好了。','我根本不想开店。'],0,'Finding the premises comes first in this plan.')],
      38:[('你想先少选一点课吗？','Do you want to take fewer classes at first?',['对，我想留时间适应。','不，我要把每天都排满。','学费已经增加了一倍。'],0,'The speaker explicitly wants time to adapt.'),('学费会增加吗？','Will tuition increase?',['不会，老师说不用多交。','会，要多交一倍。','我已经不学设计了。'],0,'The proposed arrangement does not increase tuition.')],
      39:[('每人一共七十五，对吗？','Seventy-five each in total, right?',['对，车费三十，饭钱四十五。','对，车费一百二十。','不，饭钱每人一百八十。'],0,'120/4=30 and 180/4=45; total 75.'),('为什么下次早点出发？','Why leave earlier next time?',['可以坐公交车，省一点钱。','因为市场永远关了。','因为这次不用付车费。'],0,'Earlier departure permits the cheaper bus option.')],
      40:[('为什么现在要走？','Why do you need to leave now?',['明天还要早起。','因为我不认识主人。','因为空调已经坏了。'],0,'The guest has an early start tomorrow.'),('你怎么又回来了？','Why are you back again?',['我的外套忘在椅子上了。','我从来没来过这里。','我已经回到家了。'],0,'The guest returns for the forgotten coat.')],
    }
    for i,row in enumerate(followups[number],2):
        s['tasks'][i]=reply(*row)
    s['tasks'][0]['why']={37:'The speaker describes a bookshop, not a factory.',38:'The speaker says choosing a subject is hardest.',39:'120 yuan is the total fare; divided by four it is 30 each.',40:'The father is retired, but no police career is stated.'}[number]
    s['glosses'].extend({37:[('房租','rent'),('餐饮','catering'),('项目','project')],38:[('译本','translated edition'),('光线','light; lighting'),('权利','rights'),('义务','responsibilities; duties')],39:[('收据','receipt'),('预计','expect; estimate'),('各自','each separately'),('合唱','choir; group singing')],40:[('污染','pollution'),('走廊','corridor'),('尽头','the end')]}[number])
    # Explain unfamiliar words in the passage where they occur; the checker
    # still calculates readability independently of these definitions.
    s['glosses'].extend({
      37:[('附近','nearby'),('固定','fixed; regular'),('扩大','expand'),('几乎','almost'),('儿童','children'),('翻译','translate; translation'),('鼓励','encourage; encouragement'),('绕','go around; take a detour'),('临时','temporary'),('咨询','ask for information; consultation')],
      38:[('增加','increase'),('渐渐','gradually'),('附近','nearby')],
      39:[('涨','rise, of prices or water'),('购物','shopping'),('倍','times, a multiplier'),('逐渐','gradually'),('岸边','riverbank')],
      40:[('抱','hold in the arms; hug'),('吓','scare'),('耐心','patient; patience'),('夫妻','husband and wife; married couple'),('延长','extend'),('扔','throw'),('垃圾','rubbish'),('扇','measure word for doors and windows')],
    }[number])
    repair(number,s,publish='--publish' in sys.argv)
