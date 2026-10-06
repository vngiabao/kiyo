"""Explicitly authored additional contexts for under-recycled vocabulary.

The serializer reuses the introduction example for a later meaning check and
adds these distinct sentences where that still leaves fewer than two contexts.
It never repeats an identical sentence just to inflate the context count.
"""
CONTEXTS={
's2-u06':{'那么':('那张图片没有那么小，但日期也是旧的。','That image is not so small, but its date is old too.')},
's3-u13':{
'将来':('这次没时间，将来有空再约。','There is no time this occasion; arrange another meeting when free in the future.'),
'决定':('她还没决定，我们先别替她报名。','She has not decided; do not register on her behalf yet.'),
'适合':('这个房间适合四个人，不适合十个人。','This room suits four people, not ten.'),
'理由':('她改时间有自己的理由，先问清楚。','She has her own reason for changing the time; clarify it first.'),
'不得不':('门已经关了，我们不得不换地方。','The door is closed; we have no choice but to change places.'),
'不安':('她还没回消息，我有点不安。','She has not replied; I am a little uneasy.'),
'风险':('还没确认地址就出发，有走错的风险。','Setting off before confirming the address risks going the wrong way.'),
'保险':('先确认两个地点，安排起来更保险。','Confirming two venues first makes arranging things safer.'),
'意外':('她今天来了，我觉得很意外。','Her arrival today surprises me.'),
'预报':('先看今天的预报，别看昨天的。','Check today’s forecast, not yesterday’s.'),
'预习':('我预习了要问的话，还没开始活动。','I prepared what to ask; the event has not started.'),
'概念':('先弄清概念，再判断消息。','Clarify the concepts before judging the message.'),
'观念':('有不同观念，也可以好好交流。','People with different notions can still communicate well.')},
's3-u14':{
'白':('店没开，没问时间就白去了。','The shop is closed; visiting without asking the time was in vain.'),
'当然':('当然可以问，问清楚再告诉朋友。','Of course one can ask; clarify before telling the friend.'),
'到底':('时间前后不同，到底几点开始？','The stated times differ; when does it start, after all?'),
'反正':('反正还没发出去，先把日期改对。','It has not been sent anyway; correct the date first.'),
'根本':('这条消息根本没有说活动取消。','This message does not say the event is cancelled at all.'),
'果然':('我以为她没看新通知，问了以后果然是这样。','I thought she had not read the new notice; asking confirmed that expectation.'),
'简直':('字太小，这张图简直没法读。','The writing is too small; the image is practically impossible to read.'),
'其实':('其实她已经到了，只是在另一个门口。','Actually, she has arrived, just at another entrance.'),
'确实':('我核对了日期，确实是明天。','I checked the date; it really is tomorrow.'),
'只好':('电话没打通，只好先发短信。','The call did not connect; there is no choice but to text first.'),
'终于':('问了两次，终于知道新房间了。','After asking twice, finally learned the new room.'),
'事实上':('事实上，朋友只是换了时间，没有取消。','In fact, the friend only changed the time and did not cancel.'),
'判断':('先问来源，不急着做判断。','Ask the source first rather than rushing to a judgement.'),
'传播':('已经发现日期错了，就别继续传播。','The wrong date has been found; stop spreading it.'),
'真实':('真实的照片也要看拍摄时间。','Even a real photo needs its capture date checked.')},
's3-u15':{
'带领':('她带领新会员看名单，不替大家决定。','She guides new members through the list without deciding for everyone.'),
'会员':('会员先报到，新朋友也要看通知。','Members report on arrival; new friends also need to read the notice.'),
'过程':('这个过程有三步，先报到，再进场，最后交流。','This process has three steps: report on arrival, enter, then exchange ideas.'),
'宣传':('宣传写着六点，名单上的时间也要一致。','Publicity says six; the time on the list must agree.')},
's3-u16':{
'搬家':('朋友搬家了，做客前再确认地址。','The friend moved house; confirm the address before visiting.'),
'背后':('我背后有出口，箱子先别放这里。','There is an exit behind me; do not put the box here yet.'),
'底下':('桌子底下的工具先拿出来。','Take the tools beneath the desk out first.'),
'外面':('工具别留在外面，先拿进屋。','Do not leave the tools outside; bring them indoors first.'),
'上面':('箱子上面有字，先读清楚再搬。','There is writing on top of the box; read it clearly before moving it.'),
'下面':('把箱子放在下面，别放桌子上。','Put the box below, not on the table.'),
'前面':('前面的门已经开了，后面的还关着。','The door in front is open; the one behind remains shut.'),
'上来':('我在楼上等，你拿工具上来。','I am waiting upstairs; bring the tools up.'),
'下来':('我在一楼，你从二楼下来找我。','I am on the first floor; come down from the second to find me.'),
'下去':('我还在二楼，你先下去开门。','I am still upstairs; go down first and open the door.'),
'运输':('运输还没开始，箱子先装好。','Transport has not started; pack the boxes properly first.'),
'家具':('家具放好以后，再打开书箱。','Open the book box after the furniture is in place.'),
'木头':('这块木头先放屋里，别留在雨中。','Leave this piece of wood indoors, not in the rain.'),
'推开':('门能推开，但出口还要保持空着。','The door can be pushed open, but the exit still needs to stay clear.')},
's3-u17':{
'感情':('我们重视朋友之间的感情，也尊重不同选择。','We value friendship and also respect different choices.'),
'感受':('她的感受和我的不同，先听她说。','Her feelings differ from mine; listen to her first.'),
'情感':('情感可以表达清楚，不必猜对方的答案。','Emotions can be expressed clearly without guessing the other person’s answer.'),
'内心':('她内心喜欢热闹，今天却选择休息。','Inside she likes a lively atmosphere, but today chooses rest.'),
'心':('心里想来，不等于今天有时间。','Wanting to come does not mean having time today.'),
'思想':('我们交流思想，不把不同当错误。','We exchange ideas without treating difference as error.'),
'意义':('同一张照片，对两个人的意义可能不同。','The same photo can mean different things to two people.'),
'个人':('个人选择要由本人确认。','A personal choice needs confirmation by the person themself.'),
'自身':('她根据自身情况，决定先休息。','She decides to rest first based on her own situation.'),
'自主':('可以自主决定，也可以先向朋友请教。','One can decide independently and still first seek advice from a friend.'),
'对方':('对方还没说愿意，我们先不替她答应。','The other person has not said she is willing; do not agree on her behalf.'),
'对象':('这份通知的对象是会员，不是所有人。','This notice is intended for members, not everyone.'),
'合理':('把两个人的需要都问清楚，安排才合理。','Clarifying both people’s needs makes the arrangement reasonable.'),
'客观':('客观说明时间，不猜她一定喜欢。','State the time objectively without guessing she must like it.'),
'体会':('听她说今天很累，我能体会她想休息。','Hearing she is tired today, I can appreciate her wish to rest.'),
'体现':('给她自己选，体现对她的尊重。','Letting her choose reflects respect for her.'),
'相似':('两个安排相似，但时间不同。','The two arrangements are similar but have different times.'),
'显然':('她显然还在考虑，先等她回复。','She is evidently still considering; wait for her reply.')},
's3-u18':{
'文明':('文明地交流，也要让对方把话说完。','Communicating civilly also means letting the other person finish.'),
'民间':('这个民间故事是她从家人那里听来的。','She heard this folk story from her family.'),
'华人':('华人朋友也可能有不同的家庭习惯。','Friends of Chinese heritage may also have different family practices.'),
'中华民族':('这篇文章谈中华民族的文化，也说明各地不同。','This article discusses the culture of the Chinese nation and variation across places.'),
'社会':('社会变了，庆祝方式也可能变。','Society has changed; celebration practices may change too.'),
'人民':('了解人民的生活，不能只看表演。','To understand people’s lives, do not look only at performances.'),
'世界':('世界各地的朋友都可以介绍自己的习惯。','Friends around the world can introduce their own practices.'),
'世纪':('这张图来自上个世纪，日期写得很清楚。','This image is from the previous century; the date is clearly written.'),
'时代':('不同的时代，做客的安排也可能不同。','In different eras, arrangements for visiting may differ.'),
'国庆':('国庆那天有没有活动，先查当地通知。','Check local notices first for whether National Day events are scheduled.'),
'庆祝':('她想安静地庆祝，不一定办大活动。','She wants to celebrate quietly, not necessarily with a big event.'),
'文学':('文学可以讲故事，但不是报名通知。','Literature can tell stories, but it is not a registration notice.'),
'美术':('这次美术活动先介绍作品，再交流。','This fine-arts event introduces works before discussion.'),
'京剧':('看京剧前先了解这次演出的内容。','Learn the content of this performance before watching Peking opera.'),
'武术':('这场武术表演要看通知上的时间。','Check the notice for this martial-arts performance’s time.')},
's3-u19':{
'事件':('把事件经过写清楚，不把猜测写成事实。','Record the incident clearly without presenting guesses as facts.'),
'事故':('只是地址写错，没有发生事故。','Only the address was written incorrectly; no accident occurred.'),
'后果':('我承认错误，也认真处理它的后果。','I accept the error and deal seriously with its consequences.'),
'反应':('朋友的反应是先要求改地址。','The friend’s reaction is first to ask for the address to be corrected.'),
'表达':('我表达歉意，也说明下一步怎么改。','I express regret and explain how to correct it next.'),
'声明':('这份声明写清楚谁发错了地址。','This statement makes clear who sent the wrong address.'),
'宣布':('先确认新地点，再宣布，别反过来。','Confirm the new venue before announcing it, not the other way round.'),
'完善':('把日期和门牌号都补上，通知才完善。','Adding the date and building number makes the notice complete.'),
'注意':('要注意朋友的时间，不让她继续等错地方。','Pay attention to the friend’s time; do not leave her waiting at the wrong place.'),
'奇怪':('两个通知地址不同，她觉得很奇怪。','The notices have different addresses; she finds that strange.'),
'伤心':('她伤心的是被责怪，不只是多走路。','She is hurt by being blamed, not only by the extra travel.'),
'失去':('失去的时间不能直接补回来，但可以认真道歉。','Lost time cannot simply be restored, but one can apologize sincerely.'),
'消失':('旧消息消失了，新的地址还要发清楚。','The old message disappeared; the new address still needs sending clearly.'),
'信任':('她愿意再联系，不等于信任已经完全恢复。','Her willingness to contact again does not mean trust has fully recovered.'),
'对待':('对待这次错误，我先改，不先找借口。','In dealing with this error, I correct it first rather than look for excuses.'),
'相关':('和见面相关的地点、时间一起确认。','Confirm the venue and time relevant to the meeting together.')},
's3-u20':{
'设计':('设计看起来简单，带书却很方便。','The design looks simple but makes carrying books convenient.'),
'创造':('朋友一起创造回忆，不一定要花很多钱。','Friends create memories together without necessarily spending much.'),
'创新':('创新可以从自己的需要开始，不必冒充别人的作者。','Innovation can start from one’s own needs, without pretending to have created someone else’s work.'),
'浪费':('能用已有的纸，就别浪费新材料。','Use existing paper when possible rather than wasting new materials.'),
'利用':('利用剩下的布，做一个小袋子。','Use the remaining cloth to make a small bag.'),
'适用':('小布袋适用于小书，大书还要看尺寸。','The small bag suits small books; large ones require checking dimensions.'),
'应用':('把学过的汉语应用到祝福里。','Apply the Mandarin already learned to good wishes.'),
'消费':('消费多少是个人安排，不替别人决定。','Spending is a personal arrangement; do not decide for another.')},
}

CONTEXTS.update({
's3-u01':{
'姑娘':('那位姑娘是新来的会员，先问她怎么称呼。','That young woman is a new member; first ask how she wishes to be addressed.'),
'个性':('她的个性比较安静，也喜欢参加交流。','She has a quiet personality and also likes joining exchanges.'),
'称为':('大家把他称为老李，不是因为知道他的年龄。','People call him Old Li, not because they know his age.'),
'亲人':('亲人来访，也要先问时间。','Even when relatives visit, ask about the time first.'),
'父母':('她的父母不参加这次活动，别把他们算进去。','Her parents are not joining this event; do not count them in.'),
'故乡':('她说故乡在南方，没有说具体城市。','She says her hometown is in the south without naming a particular city.'),
'女子':('这位女子是组织者，不是刚到的客人。','This woman is the organizer, not a newly arrived guest.'),
'人员':('活动人员先看名单，再安排座位。','Event personnel check the list before arranging seats.')},
's3-u02':{
'群':('一群朋友来了，不等于他们都报名了。','A group of friends arrived; it does not mean all of them registered.'),
'好奇':('我对比赛很好奇，但还没决定参加。','I am curious about the competition but have not decided to enter.'),
'能力':('有能力的人也可以选择先听。','A capable person can also choose to listen first.'),
'才能':('她有语言才能，也需要练习。','She has a talent for languages and still needs practice.')},
's3-u03':{
'需求':('先问各组的需求，再分配任务。','Ask each group’s needs before allocating tasks.'),
'分组':('按名单分组，不按谁先说话。','Group according to the list, not who speaks first.'),
'团体':('这个团体今天需要四位志愿者。','This group needs four volunteers today.')},
's3-u04':{
'互相':('我们互相问清楚时间，不替别人答应。','We clarify the time with each other without agreeing for others.'),
'请教':('有不懂的地方，可以向老师请教。','One can ask a teacher for advice about what is unclear.'),
'打听':('我先打听开门时间，不直接猜。','I first inquire about opening time rather than guessing.'),
'访问':('访问以前先约时间，别突然到。','Arrange a time before visiting rather than arriving suddenly.'),
'及时':('她及时回了消息，我还没出发。','She replied promptly, before I had set off.'),
'提前':('要提前问，不等到门口才说。','Ask in advance, not only on reaching the doorway.'),
'约':('我们约了明天下午，不是今天。','We arranged tomorrow afternoon, not today.'),
'告别':('活动结束时，先向主人告别。','Say goodbye to the host when the event ends.'),
'结婚':('她朋友结婚了，具体安排还要看邀请。','Her friend got married; check the invitation for specific arrangements.'),
'谈话':('谈话没结束，我先不打断。','The conversation has not ended; I will not interrupt.'),
'领导':('领导不在，先问今天谁负责接待。','The leader is absent; ask who handles reception today.'),
'交往':('交往中有问题，可以先说明自己的需要。','When problems arise in interactions, first explain one’s needs.')},
's3-u05':{
'整理':('整理文件时，把旧日期和新日期分开。','When organizing files, separate old and new dates.'),
'证据':('图片没有日期，不能当今天活动的证据。','An image without a date cannot serve as evidence for today’s event.'),
'明确':('信息还不明确，先别发给所有人。','The information remains unclear; do not send it to everyone yet.'),
'解决':('解决开门问题以后，再核对日期。','After resolving the opening problem, check the date.'),
'达到':('只找到文件，还没达到核对完成的目标。','Finding the file alone has not achieved the goal of completed checking.')},
's3-u06':{
'红酒':('她不喝红酒，给她果汁就好。','She does not drink red wine; juice is fine for her.'),
'红茶':('红茶还很热，先放在桌上。','The black tea is still hot; leave it on the table first.'),
'食品':('买食品以前，先看人数和需要。','Check the number of people and their needs before buying food.'),
'美食':('分享美食，也要问别人能不能吃。','When sharing good food, also ask whether others can eat it.')},
's3-u07':{
'人群':('人群里有六个人，纸还缺两张。','There are six people in the group; two sheets of paper are still missing.')},
's3-u08':{
'强大':('声音强大，不等于每个字都清楚。','A powerful voice does not mean every word is clear.'),
'强烈':('她想参加的愿望很强烈，也先确认时间。','She strongly wants to join and still confirms the time first.'),
'演唱会':('演唱会还没开始，大家先看座位。','The concert has not started; everyone checks their seats first.'),
'歌声':('我听见歌声，歌词却还没听清。','I hear singing but have not yet understood the lyrics clearly.'),
'歌迷':('歌迷也可以安静地听，不必一直喊。','A fan can listen quietly without shouting all the time.')},
's3-u09':{
'仅仅':('仅仅确认日期，还没确认名额。','Only the date is confirmed; the place is not yet confirmed.'),
'近期':('近期活动的费用，要看新的通知。','Check the new notice for upcoming events’ costs.'),
'价钱':('价钱相同，也要分别看报名规定。','Even with the same price, check registration rules separately.'),
'必要':('确认费用很必要，不要只看标题。','Confirming the cost is necessary; do not read only the heading.'),
'公共':('公共场所还有空座，不代表活动还有名额。','A public venue having empty seats does not mean event places remain.')},
's3-u10':{
'赶快':('地址写错了，赶快联系还没出发的朋友。','The address is wrong; promptly contact the friend who has not set off.'),
'始终':('她始终没说一定参加，我们先别替她答应。','She has never said she will definitely join during this time; do not agree on her behalf.'),
'过去':('过去见面的地点变了，先看新地址。','The former meeting venue has changed; check the new address first.'),
'当初':('当初只定了日期，没有定具体时间。','Originally only the date was settled, not an exact time.'),
'年代':('照片上的年代不同，不是同一次活动。','The photos are from different eras, not the same event.'),
'变化':('地点有变化，见面的愿望没变。','The venue has changed; the wish to meet has not.'),
'成长':('朋友在不同城市成长，也能聊共同的经历。','Friends who grew up in different cities can discuss shared experiences.'),
'印象':('我有旧店的印象，还要确认现在的地点。','I remember the old shop but still need to confirm the current venue.')},
's3-u11':{
'日常':('日常习惯可以慢慢改，不必一天全改。','Everyday habits can change gradually, not all in one day.'),
'定期':('我们定期交流，不代表每天都见面。','We have regular exchanges; that does not mean meeting every day.'),
'营养':('午饭想吃有营养的东西，先问有什么。','For lunch, I want something nutritious; first ask what is available.')},
's3-u12':{
'继续':('休息以后继续，不把暂停当失败。','Continue after a rest without treating a pause as failure.'),
'训练':('这次训练只有两句，先把第一句听清。','This practice has only two sentences; understand the first clearly first.'),
'克服':('克服困难需要办法，不只是加快速度。','Overcoming difficulty needs a method, not merely faster speed.'),
'改造':('不必改造整个计划，先改不清楚的一步。','There is no need to remodel the whole plan; adjust the unclear step first.'),
'加强':('加强练习，也要留时间休息。','More practice still needs time set aside for rest.'),
'效果':('只听了一次，练习效果还要再看。','After only one listen, the practice’s effect still needs observing.'),
'力量':('有力量也不必一直大声说。','Having power does not require speaking loudly all the time.'),
'决心':('有决心继续，也可以承认第二句没懂。','Determination to continue can coexist with admitting the second sentence was not understood.'),
'成就':('把实际成就记下来，不把计划当完成。','Record actual achievements, not planned work as completed work.')},
})

CONTEXTS.update({
's2-u09':{'感到':('收到朋友的信，我感到很高兴。','Receiving my friend’s letter makes me feel happy.')},
's2-u10':{},
's3-u21':{},
's3-u22':{},
's3-u23':{},'s3-u24':{},
's2-u11':{'不行':('声音太大不行，先问能不能调小。','Excessive volume will not do; first ask whether it can be turned down.')},
's2-u12':{'大部分':('大部分朋友都到了，还有两个人没来。','Most friends have arrived; two have not come yet.')},
's2-u13':{},'s2-u14':{},
's2-u15':{'道理':('你说的有道理，不过我想先问清楚。','What you say makes sense, but I want to clarify first.')},
's2-u16':{'嘴':('她嘴上说不急，已经看了三次时间。','She says she is not in a hurry, but has checked the time three times.')},
's2-u17':{
'阴':('今天阴，出门前还是要看天气预报。','It is overcast today; still check the forecast before going out.'),
'阴天':('阴天也可以散步，不等于一定下雨。','One can walk on an overcast day; it does not mean rain is certain.'),
'下雪':('明天可能下雪，见面的时间先别定死。','It may snow tomorrow; leave the meeting time flexible for now.')},
's2-u18':{
'球队':('这支球队周末比赛，我们先问在哪儿。','This team plays at the weekend; first ask where.'),
'球场':('朋友在球场外等，还没进去。','The friend waits outside the court and has not entered yet.'),
'球鞋':('球鞋忘带了，我先回家拿。','I forgot my sports shoes; I will go home to get them first.')},
's2-u19':{
'道路':('这条道路还没走过，我们先看地图。','We have not taken this road before; check the map first.'),
'东南':('学校在这里的东南，不是西南。','The school is southeast of here, not southwest.'),
'西方':('地图上的西方在左边，不等于我们面前。','West on the map is to the left, not necessarily in front of us.')},
's2-u20':{
'碰见':('我在门口碰见朋友，就一起进去了。','I ran into my friend at the entrance, and we went in together.'),
'见到':('今天终于见到新同学了。','Today I finally met the new classmate.'),
'青年':('这次活动欢迎青年参加，先看报名要求。','This event welcomes young adults; read the registration requirements first.'),
'中年':('中年朋友也可以参加，不只有学生。','Middle-aged friends can also join; it is not only for students.')},
's2-u21':{
'爱情':('这部电影讲爱情，也讲朋友之间的支持。','This film discusses romantic love and support among friends.'),
'爱人':('她和爱人一起去看电影。','She goes to the cinema with her spouse.'),
'平常':('平常我们在这里见，今天换个地方。','Usually we meet here; today we will change venues.'),
'太太':('王先生和太太已经到了。','Mr Wang and his wife have arrived.')},
's2-u22':{
'靠':('先靠右走，别挡住入口。','Keep to the right first, without blocking the entrance.'),
'大自然':('想看看大自然，也要先确认天气。','To experience nature, still confirm the weather first.')},
's2-u23':{
'求':('求朋友帮忙以前，先说明需要什么。','Before asking a friend for help, explain what is needed.'),
'教育':('我们聊教育，不把自己的经历当所有人的经历。','We discuss education without treating our experiences as everyone’s experiences.'),
'讲话':('她正在讲话，我等她说完再问。','She is speaking; I wait until she finishes before asking.'),
'家长':('家长还没收到通知，我们先别替他答应。','The parent has not received the notice; do not agree on his behalf.'),
'高中':('她高中毕业以后换了城市。','She moved cities after graduating from high school.'),
'级':('这本书适合初级，不代表所有级别都适合。','This book suits beginners; it does not suit every level automatically.')},
's2-u24':{
'不但':('她不但会说，还会写。','She can not only speak but also write.'),
'但是':('我想参加，但是那天没有时间。','I want to join, but have no time that day.'),
'而且':('时间合适，而且地点离家不远。','The time works, and the venue is not far from home.'),
'比如说':('可以带一份小礼物，比如说一本书。','One could bring a small gift, for example a book.'),
'听讲':('听讲时先记问题，下课再问。','While listening to the explanation, note questions and ask after class.')},
's2-u25':{
'所以':('地址变了，所以出发前再确认。','The address has changed, so confirm again before setting off.'),
'站':('先站在门外，等朋友出来。','Stand outside the door first and wait for the friend to come out.'),
'站住':('请站住，前面还不能进去。','Please stop there; one cannot enter ahead yet.'),
'事情':('事情还没说清楚，先别下结论。','The matter is not yet clear; do not draw a conclusion.'),
'受到':('我受到朋友的帮助，也想帮别人。','I received help from friends and want to help others too.'),
'行为':('这种行为让别人等了很久，要解释原因。','This behaviour kept others waiting a long time; explain why.'),
'顺利':('今天报名很顺利，不到五分钟就好了。','Registration went smoothly today, taking less than five minutes.'),
'挺好':('这个办法挺好，不过还要问朋友愿不愿意。','This method is pretty good, but still ask whether the friend is willing.')},
's2-u26':{
'懂得':('懂得规则以后，再开始练习。','Start practising after understanding the rules.'),
'中级':('她在读中级课本，还是会问生词。','She is using an intermediate textbook and still asks about unfamiliar words.'),
'考生':('考生先看通知，不要只听别人说。','Candidates should read the notice first, not just rely on what others say.')},
's2-u27':{
'机会':('这次没机会见面，下次再约。','There is no chance to meet this time; arrange another occasion.'),
'旅游':('旅游以前先确认地址和时间。','Confirm addresses and times before travelling.'),
'骑车':('今天下雨，我不骑车过去。','It is raining today; I will not cycle there.')},
's2-u28':{'洗澡':('我洗澡以后再回消息。','I will reply after taking a shower.')},
's2-u29':{
'的话':('时间合适的话，我们一起去。','If the time works, we will go together.'),
'叫作':('这家店叫作夜书店，名字不代表一直开门。','This shop is called Night Bookshop; its name does not mean it stays open all night.'),
'人们':('人们有不同的安排，要分别问清楚。','People have different arrangements; clarify with each of them.'),
'人口':('这座城市人口很多，但不能据此判断活动人数。','This city has a large population; that does not establish the event attendance.'),
'过年':('过年时朋友回家，我们另选时间见。','The friend goes home for the New Year; we will choose another meeting time.'),
'节日':('节日可能关门，出发前先问。','It may close for the holiday; ask before leaving.')},
's2-u30':{
'院长':('院长今天不在，通知由办公室发。','The hospital director is absent today; the office issues the notice.'),
'健康':('关心朋友的健康，也要尊重她不想说的事。','Care about a friend’s health and respect things she does not want to discuss.'),
'西医':('她想找西医，先问能不能预约。','She wants to consult a practitioner of Western medicine; first ask whether an appointment is available.'),
'中医':('她问中医门诊几点开，不是在问药店。','She asks when the Chinese medicine clinic opens, not the pharmacy.'),
'药店':('药店地址变了，先看新通知。','The pharmacy has changed address; read the new notice first.'),
'闻':('我闻到饭香了，不过还没问吃什么。','I smell food cooking, but have not asked what we will eat.'),
'空气':('屋里空气不好，我们先出去。','The indoor air is unpleasant; let us go outside first.'),
'地球':('这段话讲地球，不是在讲某个城市。','This passage concerns Earth, not a particular city.'),
'星星':('今天云很多，看不到星星。','There are many clouds today; the stars are not visible.'),
'一生':('这篇故事写一个人的一生，不只写一天。','This story describes a person’s lifetime, not just one day.'),
'永远':('我不能答应永远不改时间，但改了会告诉你。','I cannot promise never to change the time, but will tell you if it changes.')},
's2-u31':{'影片':('影片还没开始，我们先找座位。','The film has not begun; find our seats first.')},
's2-u32':{
'到处':('我到处找笔，最后在包里找到了。','I looked everywhere for the pen and finally found it in my bag.'),
'想到':('想到朋友还没回消息，我先等等。','Thinking of my friend’s unanswered message, I wait a little.'),
'想起':('我想起地址改了，赶快联系她。','I remembered the address had changed and contacted her promptly.'),
'以下':('以下三条是新安排，旧消息不要再发。','The following three points are the new arrangements; stop forwarding the old message.'),
'以外':('名单以外的人，要先问能不能加入。','People not on the list should ask whether they can join first.'),
'市长':('这条新闻讲市长的讲话，不是学校通知。','This news item concerns the mayor’s speech, not a school notice.'),
'信用卡':('这里不能用信用卡，先问还能怎么付。','Credit cards cannot be used here; ask what other payment methods are accepted.')},
's2-u33':{
'等于':('三加二等于五，不是六。','Three plus two equals five, not six.'),
'过来':('我在厨房，你过来看看。','I am in the kitchen; come over and look.'),
'片':('先尝一片，再决定要多少。','Try one slice before deciding how much you want.'),
'做到':('还没做到，就别说已经完成。','Do not say it is complete before accomplishing it.'),
'做饭':('今天一起做饭，先问每个人吃什么。','We cook together today; ask what each person eats first.'),
'吹':('饭还烫，吹一吹再吃。','The food is still hot; blow on it before eating.')},
's2-u34':{
'出现':('新问题出现了，我们先停下来问。','A new problem has arisen; stop and ask first.'),
'大大':('先确认地址，可以大大减少走错的可能。','Confirming the address first can greatly reduce the chance of going the wrong way.'),
'大量':('群里有大量消息，先找最新的通知。','The group has many messages; find the latest notice first.'),
'干活儿':('干活儿以前，先把安排说清楚。','Clarify the arrangements before starting work.'),
'个子':('她个子高，还是要先问她愿不愿意帮忙。','She is tall, but still ask whether she is willing to help.'),
'经理':('经理还没回来，先问工作人员。','The manager has not returned; ask the staff first.'),
'开学':('开学以后时间变了，我们重新约。','Our schedules change after term starts; arrange a new meeting.'),
'流':('水一直流，先把水关了。','The water keeps running; turn it off first.'),
'省':('这次省了十块，下次还要看价格。','This time we saved ten yuan; still check the price next time.'),
'语言':('学习语言要练习，也要给自己时间。','Learning a language requires practice and time.')},
})

NOTE_GLOSSES={
's2-u16':{'碰':'to touch; bump into','一切':'everything'},
's2-u17':{'骑车':'to ride a bicycle','定死':'to fix inflexibly','习惯':'to be accustomed to'},
's2-u18':{'正式':'formal; official','支':'classifier for teams','比赛':'to compete; match'},
's2-u20':{'终于':'finally'},
's2-u21':{'支持':'support; to support','称呼':'to address; form of address'},
's2-u22':{'挡住':'to block'},
's2-u23':{'毕业':'to graduate','城市':'city','初级':'beginner level'},
's2-u25':{'结论':'conclusion','建议':'suggestion; to suggest','这种':'this kind of','解释':'to explain','报名':'to register'},
's2-u26':{'规则':'rule','材料':'materials','例句':'example sentence','敲':'to knock'},
's2-u27':{'重新':'again; anew','约':'to arrange to meet','继续':'to continue'},
's2-u28':{'暂时':'temporarily'},
's2-u29':{'城市':'city','据此':'on this basis','判断':'to judge; judgement','习惯':'habit; to be accustomed to'},
's2-u30':{'办公室':'office','尊重':'to respect','判断':'to judge','建议':'suggestion','门诊':'outpatient clinic','专业':'professional; specialized','猫':'cat','香':'fragrant; aroma','呼吸':'to breathe; breathing','屋里':'inside the room','报名':'to register','某个':'a certain','城市':'city','窗':'window','习惯':'habit','篇':'classifier for articles'},
's2-u31':{'需要':'to need'},
's2-u32':{'赶快':'promptly','联系':'to contact','城区':'urban district','职务':'position; job responsibilities','姓':'surname','形式':'form'},
's2-u33':{'擦':'to wipe','尝':'to taste'},
's2-u34':{'减少':'to reduce','任务':'task','预约':'to book an appointment','约':'to arrange to meet','来往':'to go back and forth; contacts'},
's3-u01':{'年龄':'age','来访':'to visit','想念':'to miss someone or somewhere','观念':'notion; outlook','组织':'to organize; organization'},
's3-u04':{'突然':'suddenly','邀请':'to invite'},
's3-u06':{'分享':'to share'},
's3-u07':{'内容':'content','标准':'standard'},
's3-u08':{'团队':'team','愿望':'wish; aspiration'},
's3-u09':{'标题':'title; heading','仍然':'still'},
's3-u10':{'愿望':'wish; aspiration','仍然':'still'},
's3-u11':{'目标':'goal','速度':'speed','饮食':'diet; food and drink','注意':'to pay attention','仍':'still'},
's3-u12':{'失败':'failure; to fail','承认':'to acknowledge'},
's3-u13':{'组织':'to organize; organization'},
's3-u14':{'被传播':'to be circulated (passive expression)'},
's3-u16':{'压住':'to press down on'},
's3-u17':{'根据':'on the basis of'},
's3-u18':{'版本':'version','作品':'work of art or literature','表演':'to perform; performance'},
's3-u19':{'错误':'error'},
's3-u20':{'幅':'classifier for pictures','尺寸':'dimensions; size'},
}

def enrich(pack,make_line,support=None):
    uid=pack['unit']['id']
    if uid not in CONTEXTS:return
    # Only genuine lesson contexts, not the vocabulary introduction itself.
    context=[]
    def gather(value):
        if isinstance(value,dict):
            if 'zh' in value:context.append(value['zh'].replace('【','').replace('】',''))
            for key,child in value.items():
                if key!='zh':gather(child)
        elif isinstance(value,list):
            for child in value:gather(child)
    for section in ['dialogue','reading','extraReadings','grammar','tasks']:
        gather(pack.get(section))
    pairs=[]
    for word in pack['vocabulary']:
        contexts={zh for zh in context if word['hanzi'] in zh}
        if len(contexts)>=2:continue
        candidates=[(word['example']['zh'],word['example']['en'])]
        if word['hanzi'] in CONTEXTS[uid]:candidates.append(CONTEXTS[uid][word['hanzi']])
        for zh,en in candidates:
            if len(contexts)>=2:break
            if zh in contexts:continue
            assert word['hanzi'] in zh,(uid,word['hanzi'],'authored recall must contain the word')
            pairs.append(dict(left=en,right=make_line(zh,en)))
            contexts.add(zh)
        assert len(contexts)>=2,(uid,word['hanzi'],'needs a second distinct authored context')
    if not pairs:return
    unique={p['right']['zh']:p for p in pairs}
    pairs=list(unique.values())
    # Matching tasks need at least three unique sentences. Pad only with
    # already authored introduction examples; do not invent filler content.
    if len(pairs)>4:
        # Keep the main lesson within its existing task budget. Additional
        # contexts belong in an optional sentence notebook, with translations
        # and actual glosses, rather than an oversized matching exercise.
        notebook_lines=[p['right'] for p in pairs]
        body=''.join(l['zh'] for l in notebook_lines)
        pack['extraReadings'].append(dict(id=f'{uid}-word-notebook',
            title='Words in use',format='note',
            blurb='Original AI-assisted examples; native review pending.',
            purpose='Compare these complete sentences with the lesson examples. Notice what changes around the same word.',
            lines=notebook_lines,questions=[],
            glosses=[dict(hanzi=w,pinyin=make_line(w,m)['py'],meaning=m)
                     for w,m in {**(support or {}),**NOTE_GLOSSES.get(uid,{})}.items() if w in body]))
        return
    for offset in range(0,len(pairs),4):
        group=pairs[offset:offset+4]
        for word in pack['vocabulary']:
            if len(group)>=3:break
            if word['example']['zh'] in {p['right']['zh'] for p in group}:continue
            group.append(dict(left=word['example']['en'],right=word['example']))
        pack['tasks'].append(dict(type='match',id=f'{uid}-tcontext-{offset//4+1:02}',
            phrase=pack['vocabulary'][0]['id'],title='Use the words in a full sentence',pairs=group))
