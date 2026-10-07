"""Original HSK2 practice: social meaning, times and quantities, everyday agreements."""
import sys
from exam_authoring import R,L,O,C,mix,write_bank
from common import dictionary
dictionary.update({'妈妈':'mā ma','衣服':'yī fu','不要':'bù yào','关上':'guān shàng','一直':'yī zhí','一定':'yī dìng','一起':'yī qǐ','玩儿':'wánr'})

identity_r=[
R('她愿意帮忙，但今天没有时间。','She is willing to help but has no time today.','她今天为什么不帮忙？',[('没有时间','No time'),('不愿意','Unwilling'),('不认识我','Does not know me'),('已经回家','Has already gone home')],'Willingness is affirmed; lack of time is the stated obstacle.'),
R('这是朋友的请求，不是老师的要求。','This is a friend’s request, not a teacher’s requirement.','是谁提出的？',[('朋友','Friend'),('老师','Teacher'),('家长','Parent'),('学生们','The students')],'The request belongs to the friend; the teacher attribution is denied.'),
R('她爱人是医生，她自己是教师。','Her spouse is a doctor; she herself is a teacher.','谁是教师？',[('她自己','She herself'),('她爱人','Her spouse'),('她家长','Her parent'),('她朋友','Her friend')],'The second clause identifies her own occupation.'),
R('我平常周末来，今天是第一次周一来。','I usually come on weekends; this is my first Monday visit.','平常什么时候来？',[('周末','Weekend'),('周一','Monday'),('天天','Every day'),('一号','First day of the month')],'平常 refers to the normal weekend habit, not today’s exception.'),
R('我认识那位中年朋友，不认识旁边的青年。','I know that middle-aged friend, not the young adult beside him.','我认识谁？',[('中年朋友','Middle-aged friend'),('旁边的青年','The young adult beside him'),('两个人都认识','Both people'),('两个人都不认识','Neither person')],'Recognition is explicitly limited to the middle-aged friend.'),
R('妈妈是家长，爸爸也是家长，两个人都来参加活动。','Both mother and father are parents, and both attend the event.','来了几个家长？',[('两个','Two'),('一个','One'),('三个','Three'),('四个','Four')],'Both named parents attend, so there are two.'),
R('朋友刚离开，还没有到家。','The friend has just left and has not arrived home.','朋友已经做了什么？',[('离开','Left'),('到家','Arrived home'),('洗澡','Showered'),('吃完饭','Finished eating')],'刚离开 is completed; arriving home is explicitly incomplete.'),
R('我收到她的礼物，感到很高兴。','I received her gift and feel happy.','我收到了什么？',[('礼物','Gift'),('作业','Homework'),('通知','Notice'),('考试成绩','Exam result')],'The received item is explicitly the gift.'),
R('她说我讲得有道理，可是还想问别人。','She says my explanation makes sense, but still wants to ask others.','她还想做什么？',[('问别人','Ask others'),('马上答应','Agree at once'),('不再问','Ask no more'),('换工作','Change jobs')],'The remaining intention is to consult others, not immediate agreement.'),
R('朋友想和我见面，不想参加活动。','The friend wants to meet me, not take part in an event.','朋友想做什么？',[('见面','Meet'),('活动','Join the event'),('上班','Work'),('旅游','Travel')],'见面 is affirmed and 活动 denied.'),
]
identity_l=[
L('他上完高中以后，到了南方。','After finishing high school, he went south.','先发生什么？',[('上完高中','Finishing high school'),('到南方','Going south'),('参加活动','Entering an event'),('考中级','Taking an intermediate exam')],'以后 places completion of high school before the move.'),
L('这是我太太的笔记本，不是我的。','This is my wife’s notebook, not mine.','笔记本是谁的？',[('太太的','The wife’s'),('我的','Mine'),('老师的','The teacher’s'),('经理的','The manager’s')],'Possession is assigned to 太太.'),
L('我在门口碰见朋友，然后一起进去。','I ran into a friend at the entrance and then we went in together.','在哪里碰见？',[('门口','Entrance'),('楼上','Upstairs'),('球场里','Inside the court'),('家里','At home')],'The meeting occurs at 门口.'),
L('院长今天不在，医生还在工作。','The hospital director is absent today; the doctors are still working.','谁今天不在？',[('院长','Hospital director'),('医生','Doctor'),('病人','Patient'),('家长','Parent')],'Only the director is stated absent.'),
L('她愿意听意见，但不一定答应别人的要求。','She welcomes opinions but may not agree to others’ requests.','她愿意做什么？',[('听意见','Hear opinions'),('答应所有要求','Accept all requests'),('不听别人','Listen to nobody'),('马上答应','Immediately agree')],'Willingness to listen does not promise acceptance.'),
L('我求朋友帮忙，她说先说明要什么。','I asked a friend for help; she said to explain what I need first.','先要说明什么？',[('要什么','What is needed'),('天气多热','How hot it is'),('谁参加了活动','Who took part in the activity'),('谁住国外','Who lives abroad')],'The requested clarification is the need.'),
L('大家都收到通知了，只有老师还没看。','Everyone received the notice, but the teacher has not read it yet.','老师还没做什么？',[('看通知','Read the notice'),('收到通知','Receive the notice'),('发礼物','Send a gift'),('买本子','Buy a notebook')],'Receipt and reading are separate; only reading is denied.'),
L('朋友问我嘴里在说什么，我说是在读课文。','The friend asks what I am saying; I say I am reading the lesson text.','我在做什么？',[('读课文','Read the lesson text'),('唱歌','Sing'),('问多少钱','Ask how much'),('打电话','Make a call')],'The speaker explicitly explains reading the lesson text.'),
L('我觉得她很健康，但她自己说今天不舒服。','I think she looks healthy, but she says she feels unwell today.','谁说不舒服？',[('她自己','She herself'),('我','Me'),('经理','Manager'),('考生','Candidate')],'The unwell feeling is her own report, not the observer’s guess.'),
L('这个机会她想试试，结果现在还不知道。','She wants to try this opportunity; the result is not yet known.','现在知道结果了吗？',[('还不知道','Not yet known'),('已经做完','Already finished'),('一定没做完','Certainly not finished'),('不用参加','No need to join')],'A willingness to try is not a result.'),
]
identity_o=[
O(['她','愿意','帮忙'],'She is willing to help.','谁愿意帮忙？',['帮忙愿意她','她帮忙愿意','愿意帮她忙'],'Use subject then willingness then the action; keep 帮忙 intact.'),
O(['我','刚刚','收到礼物'],'I just received the gift.','谁刚刚收到礼物？',['我刚收到刚礼物','礼物收到刚刚我','刚我刚收到礼物'],'Place 刚刚 before the verb phrase and keep its two syllables together.'),
O(['这本书','是','老师的'],'This book belongs to the teacher.','什么是老师的？',['这本书是的老师','老师的这本是书','这老师本书的是'],'Keep the subject 这本书 and possession 老师的 intact.'),
O(['他','上完高中以后','去了南方'],'He went south after finishing high school.','谁上完高中以后去了南方？',['他上完以后高中去了南方','高中他上完以后去了南方','他去了上完高中以后南方'],'Keep 上完高中 as the completed activity before 以后.'),
O(['我','不愿意','回答这个问题'],'I am unwilling to answer this question.','谁不愿意回答这个问题？',['我愿意不回答这个问题','回答这个我不愿意问题','我不回答愿意这个问题'],'The target meaning negates willingness, rather than expressing willingness not to answer.'),
]
identity_c=[
C('她愿意帮忙，但是今天没时间。','She is willing to help, but has no time today.','她愿意帮忙，___今天没时间。',[('但是','But'),('所以','Therefore'),('或者','Or'),('正在','In progress')],'但是 introduces the explicit contrast; no causal claim is given.'),
C('这是我的爱人，不是我的同学。','This is my spouse, not my classmate.','这是我的爱人，___我的同学。',[('不是','Is not'),('正在','In progress'),('以后','After'),('虽然','Although')],'不是 denies the alternative identity.'),
C('朋友已经离开，还没到家。','The friend has left but has not reached home.','朋友已经离开，___到家。',[('还没','Not yet'),('一定','Certainly'),('刚才','Just now'),('昨天','Yesterday')],'还没 preserves the stated distinction between departure and arrival.'),
C('她上完高中以后，去了南方。','After finishing high school, she went south.','她上完高中___，去了南方。',[('以后','After'),('里面','Inside'),('旁边','Beside'),('哪儿','Where')],'以后 links the completed completion of high school to a later action.'),
C('他不但听意见，而且认真记下来。','He not only hears opinions but also notes them carefully.','他不但听意见，___认真记下来。',[('而且','And also'),('昨天','Yesterday'),('什么','What'),('或者','Or')],'而且 continues the additive 不但 construction.'),
]
identity=mix(identity_r,identity_l,identity_o,identity_c)

numbers_r=[
R('活动九点上课，我八点半到。','The event starts at nine; I arrive at eight thirty.','我什么时候到？',[('八点半','Eight thirty'),('九点','Nine'),('九点半','Nine thirty'),('十点','Ten')],'Arrival is at eight thirty, before the event starts.'),
R('原来三个人，现在又来了两个。','There were three people; two more have arrived.','现在一共有几个人？',[('五个','Five'),('三个','Three'),('两个','Two'),('六个','Six')],'Three existing people plus two additional arrivals makes five.'),
R('一本书二十块，我买了两本。','One book costs twenty yuan; I bought two.','一共花了多少钱？',[('四十块','Forty yuan'),('二十块','Twenty yuan'),('两块','Two yuan'),('六十块','Sixty yuan')],'Two books at twenty yuan each cost forty yuan.'),
R('今天十号，朋友后天回来。','Today is the tenth; the friend returns the day after tomorrow.','朋友几号回来？',[('十二号','The twelfth'),('十号','The tenth'),('十一号','The eleventh'),('十三号','The thirteenth')],'The day after tomorrow is two days after the tenth.'),
R('他学了两年汉语，姐姐学了三年。','He has studied Chinese for two years; his elder sister for three.','谁学的时间更长？',[('姐姐','Elder sister'),('他','He'),('两人一样长','The same length'),('都没学过','Neither has studied')],'Three years is longer than two; both have studied.'),
R('我今天只工作四个小时，昨天工作八个小时。','I work only four hours today, compared with eight yesterday.','今天比昨天少工作几个小时？',[('四个小时','Four hours'),('两个小时','Two hours'),('八个小时','Eight hours'),('十二个小时','Twelve hours')],'The difference between eight and four is four hours.'),
R('四个人都拿两个杯子。','Each person takes two cups; four people take them together.','一共拿几个杯子？',[('八个','Eight'),('两个','Two'),('四个','Four'),('六个','Six')],'Four people with two cups each take eight cups.'),
R('车十点出发，路上要一个小时。','The vehicle departs at ten; the trip takes one hour.','路上不休息，几点到？',[('十一点','Eleven'),('九点','Nine'),('十点','Ten'),('十二点','Twelve')],'Adding one hour to the stated ten o’clock departure gives eleven.'),
R('先有十个包子，吃了三个，现在还有七个。','There were ten buns; three were eaten and seven remain.','现在还有几个？',[('七个','Seven'),('三个','Three'),('十个','Ten'),('十三个','Thirteen')],'The passage explicitly states seven remaining buns.'),
R('她星期二和星期四来，星期三不来。','She comes on Tuesday and Thursday, not Wednesday.','哪一天不来？',[('星期三','Wednesday'),('星期二','Tuesday'),('星期四','Thursday'),('两天都来','Comes on both days')],'Wednesday is the one explicitly excluded.'),
]
numbers_l=[
L('我们六点见面，先吃饭，七点去看电影。','We meet at six, eat first and go to the movie at seven.','几点见面？',[('六点','Six'),('七点','Seven'),('八点','Eight'),('九点','Nine')],'Meeting time is six; seven belongs to going to the movie.'),
L('你要一杯还是两杯？我只要一杯。','Do you want one cup or two? I only want one.','回答的人要几杯？',[('一杯','One'),('两杯','Two'),('三杯','Three'),('不要','None')],'The response selects one, not both alternatives.'),
L('这次买了三本书，送人一本，自己留两本。','I bought three books, gave one away and kept two.','自己留几本？',[('两本','Two'),('一本','One'),('三本','Three'),('四本','Four')],'Two are explicitly kept; one is given away.'),
L('饭要等十分钟，茶现在就可以喝。','The meal needs a ten-minute wait; the tea can be drunk now.','什么现在可以喝？',[('茶','Tea'),('饭','The meal'),('明天的饭','Tomorrow’s meal'),('还没买的水','Water not yet bought')],'Tea is available now; the meal still requires waiting.'),
L('她从九点工作到十二点，中间没有休息。','She worked from nine until twelve without a break.','她工作了多久？',[('三个小时','Three hours'),('一个小时','One hour'),('两个小时','Two hours'),('四个小时','Four hours')],'The uninterrupted interval from nine to twelve is three hours.'),
L('我要去二楼，朋友去三楼，我们不在一层。','I go to the second floor; my friend to the third; we are on different floors.','朋友去几楼？',[('三楼','Third floor'),('二楼','Second floor'),('一楼','First floor'),('四楼','Fourth floor')],'The friend’s destination is the third floor, not mine.'),
L('一共四十块，你给我五十块，我找你十块。','The total is forty; you give fifty and I return ten in change.','找回多少钱？',[('十块','Ten yuan'),('四十块','Forty yuan'),('五十块','Fifty yuan'),('九十块','Ninety yuan')],'Change is fifty minus forty, explicitly ten yuan.'),
L('昨天已经发了两封信，今天还没发。','Two letters were sent yesterday; none have been sent today.','今天发了几封？',[('还没发','None yet'),('两封','Two'),('三封','Three'),('四封','Four')],'The two belong to yesterday; today’s count is zero so far.'),
L('这条路近一些，那条路远一些；我走近的这条。','This route is somewhat nearer and that one farther; I take the nearer one.','我走哪条路？',[('近的这条','This nearer route'),('远的那条','That farther route'),('两条都走','Both routes'),('哪条都不走','Neither route')],'The speaker explicitly chooses this nearer route.'),
L('我只住两天，不是两个星期。','I am staying only two days, not two weeks.','我住多久？',[('两天','Two days'),('两个星期','Two weeks'),('两个月','Two months'),('两年','Two years')],'The duration is days; the week alternative is explicitly denied.'),
]
numbers_o=[
O(['我','八点半','到'],'I arrive at eight thirty.','谁八点半到？',['八我点半到','我半到八点','到半点八我'],'Keep the time 八点半 intact between subject and verb.'),
O(['她','学了','三年汉语'],'She studied Chinese for three years.','谁学了三年汉语？',['她了学三年汉语','三她年汉语了学','她学三年了汉语'],'Keep 学了 before the duration and its object 汉语.'),
O(['大家','都拿','两个杯子'],'Everyone takes two cups.','大家都拿几个杯子？',['大家拿都两个杯子','两个大家杯子都拿','大家都拿杯两个子'],'Keep 大家都 and the quantity phrase 两个杯子 intact.'),
O(['这条路','比那条','近'],'This route is nearer than that one.','哪条路更近？',['这条路近比那条','比这条路那条近','这条路比近那条'],'The target comparison places 比那条 before 近.'),
O(['她','从九点','工作到十二点'],'She works from nine to twelve.','谁从九点工作到十二点？',['她从工作九点到十二点','她九点从工作到十二点','工作她从九点到十二点'],'从 introduces the starting time; 到 introduces the end of the work interval.'),
]
numbers_c=[
C('一共四十块，我给了五十块。','The total is forty yuan; I gave fifty.','___四十块，我给了五十块。',[('一共','In total'),('什么时候','When'),('谁的','Whose'),('旁边','Beside')],'一共 labels the total amount, distinct from payment.'),
C('她从九点工作到十二点。','She works from nine to twelve.','她___九点工作到十二点。',[('从','From'),('给','Give'),('向','Toward'),('跟','With')],'从 marks the start of the interval ending with 到十二点.'),
C('这条路比那条近。','This route is nearer than that one.','这条路___那条近。',[('比','Compared with'),('给','Give'),('向','Toward'),('从','From')],'比 introduces the comparison standard before the adjective.'),
C('今天只买了一本书。','Today I bought only one book.','今天只买了一___书。',[('本','Classifier for books'),('块','Piece'),('杯','Cup'),('条','Classifier for long items')],'本 is the classifier for a book in this sentence.'),
C('我住两天，不是两个月。','I stay two days, not two months.','我住两___，不是两个月。',[('天','Days'),('本','Books'),('杯','Cups'),('条','Long items')],'The stated duration is two days; months are denied.'),
]
numbers=mix(numbers_r,numbers_l,numbers_o,numbers_c)

daily_r=[
R('我忘带课本，朋友借给我一本。','I forgot my textbook; a friend lent me one.','课本是谁借给我的？',[('朋友','Friend'),('司机','Driver'),('经理','Manager'),('医生','Doctor')],'The friend is explicitly the lender.'),
R('手机没有电了，先换个手机再给她打电话。','The phone is out of power; use another phone before calling her.','先做什么？',[('换个手机','Use another phone'),('打电话','Call'),('关门','Close the door'),('买菜','Buy groceries')],'The stated first action is to use another phone.'),
R('天气冷，房间里也很冷，我穿上外套。','It is cold and not warm indoors either, so I put on a coat.','我为什么穿外套？',[('因为冷','Because it is cold'),('因为热','Because it is hot'),('因为在唱歌','Because I am singing'),('因为买了书','Because I bought a book')],'Cold weather and a cold room explain the coat.'),
R('这件衣服太小，同学让我换一件大的。','This garment is too small; the classmate suggests exchanging it for a larger one.','原来的衣服怎么样？',[('太小','Too small'),('太大','Too big'),('太长','Too long'),('太贵','Too expensive')],'The original size problem is smallness, not the replacement’s size.'),
R('她没听懂，我又说了一遍。','She did not understand, so I said it once more.','我做了什么？',[('又说了一遍','Said it again'),('不再说','Stopped speaking'),('关上门','Closed the door'),('换了衣服','Changed clothes')],'The action after the understanding problem is repetition.'),
R('我以前去过这里，但今天第一次和她一起来。','I have been here before, but this is my first visit together with her.','以前来过吗？',[('来过','Have visited'),('没来过','Have not visited'),('只来过一次还没到','Only once but not yet arrived'),('不知道在哪里','Do not know where it is')],'Prior experience is affirmed; only accompanying her is new.'),
R('我不喝茶，只想要一杯水。','I do not drink tea; I only want a cup of water.','我想喝什么？',[('水','Water'),('茶','Tea'),('奶','Milk'),('牛奶','Milk')],'Water is requested and tea explicitly declined.'),
R('她说自己不舒服，想休息，不想出去。','She says she feels unwell and wants rest rather than going out.','她现在想做什么？',[('休息','Rest'),('出去玩儿','Go out for fun'),('走路','Walk'),('参加活动','Enter an event')],'Rest is her stated intention, not a medical inference.'),
R('我先想开门，后来发现外边下雨，就没开。','I meant to open the door, but found it raining outside and did not open it.','门打开了吗？',[('没打开','Not opened'),('已经打开','Already opened'),('天天都打开','Opened every day'),('刚买了门','Just bought a door')],'A prior intention does not imply completion; the text says no opening.'),
R('朋友叫我带课本，我出门前又看了一下包。','A friend told me to bring the textbook; I checked my bag before leaving.','朋友叫我带什么？',[('课本','Textbook'),('礼物','Gift'),('外套','Coat'),('水果','Fruit')],'The request explicitly concerns the textbook.'),
]
daily_l=[
L('书放在桌子上，别放地上。','Put the book on the table, not on the floor.','书应该放在哪里？',[('桌子上','On the table'),('地上','On the floor'),('门外','Outside the door'),('车里','Inside the car')],'The table is requested and the floor explicitly excluded.'),
L('你听懂了吗？没有，最后一句请再说一遍。','Did you understand? No; please repeat the final sentence.','回答的人要什么？',[('再听最后一句','Hear the final sentence again'),('离开活动','Leave the activity'),('买一本书','Buy a book'),('换一个房间','Change rooms')],'The listener asks for the final sentence again.'),
L('外边下雨，我们先在房间里等，不急着走。','It is raining outside; let us wait indoors without rushing to leave.','现在在哪里等？',[('房间里','Indoors'),('门外','Outside the door'),('车站外面','Outside the station'),('马路中间','In the road')],'The proposed waiting location is indoors.'),
L('这件不是我的，是姐姐留在这里的。','This item is not mine; my elder sister left it here.','这件是谁的？',[('姐姐的','Elder sister’s'),('我的','Mine'),('老师的','Teacher’s'),('同学的','Classmate’s')],'The speaker denies ownership and attributes the item to the elder sister.'),
L('我先洗手，再做饭。饭做好以后我们一起吃。','I wash my hands first, then cook; we eat together after the meal is ready.','做饭前先做什么？',[('洗手','Wash hands'),('吃饭','Eat'),('去睡觉','Go to sleep'),('买手机','Buy a phone')],'Handwashing is explicitly before cooking.'),
L('我已经试过一次，这次想换个办法。','I have tried once; this time I want another method.','这次想怎么样？',[('换个办法','Change method'),('不再试','Never try again'),('只问多少钱','Only ask price'),('马上回家','Go home at once')],'Trying another method is stated, not quitting.'),
L('茶放旁边，想喝的人自己拿，我不喝。','Put tea on the side; those who want it can take it; I will not drink it.','说话的人喝茶吗？',[('不喝','Does not drink it'),('喝很多','Drinks lots'),('一定喝','Certainly drinks'),('只喝两次','Drinks only twice')],'The speaker explicitly declines tea while allowing others a choice.'),
L('我只是在开玩笑，没有生气。','I am only joking; I am not angry.','说话的人在做什么？',[('开玩笑','Joking'),('生气','Being angry'),('问路','Asking directions'),('点菜','Ordering food')],'Joking is affirmed and anger denied; no inference from volume is needed.'),
L('朋友还没回答，我先做别的事，不一直等。','The friend has not replied; I will do something else rather than keep waiting.','我先做什么？',[('做别的事','Do something else'),('一直等回答','Keep waiting for an answer'),('马上出发','Depart immediately'),('再买手机','Buy another phone')],'The stated next action is another activity.'),
L('这次我只是问问，还没有答应报名。','This time I am only asking; I have not agreed to sign up.','已经答应报名了吗？',[('还没有','Not yet'),('已经答应','Already agreed'),('昨天已经报名','Signed up yesterday'),('不能问','Cannot ask')],'Asking is explicitly distinct from an agreement to register.'),
]
daily_o=[
O(['我','先洗手','再做饭'],'I wash my hands before cooking.','谁先洗手再做饭？',['我先做手再洗饭','我洗先手再做饭','我先洗饭再做手'],'先 attaches to washing and 再 to the later cooking action.'),
O(['书','放在','桌子上'],'The book is on the table.','书放在哪里？',['书放在上桌子','放书在桌子上','桌子书上放在'],'Keep the location 桌子上 after 放在.'),
O(['她','没听懂','最后一句'],'She did not understand the final sentence.','谁没听懂最后一句？',['她听没懂最后一句','最后她一句没听懂','她没听一句懂最后'],'Keep the negated result 没听懂 before its object 最后一句.'),
O(['我','以前','去过这里'],'I have been here before.','谁以前去过这里？',['我过以前去这里','这里我以前过去','我以前去这里过'],'Place experience 过 immediately after 去, not after its object.'),
O(['这次','我','还没答应报名'],'This time I have not agreed to sign up.','这次已经答应报名了吗？',['这次我答应还没报名','还这次我没答应报名','这我次还没答应报名'],'The target meaning negates agreement, rather than affirming an agreement not to sign up.'),
]
daily_c=[
C('我先洗手，再做饭。','I wash my hands first, then cook.','我先洗手，___做饭。',[('再','Then'),('正在','In progress'),('什么','What'),('哪儿','Where')],'再 sequences the second action after the stated first one.'),
C('我以前去过这里。','I have been here before.','我以前去___这里。',[('过','Experience marker'),('着','Ongoing state marker'),('呢','Topic particle'),('吗','Question particle')],'过 marks the stated previous experience.'),
C('我没听懂最后一句。','I did not understand the final sentence.','我没听___最后一句。',[('懂','Understand'),('水','Water'),('雨','Rain'),('书','Book')],'听懂 expresses successful understanding, here negated by 没.'),
C('这件衣服太小，我想换一件。','This garment is too small; I want to exchange it.','这件衣服太小，我___换一件。',[('想','Want'),('给','Give'),('向','Toward'),('从','From')],'想 expresses the stated desire to exchange the garment.'),
C('我还没有答应报名。','I have not agreed to sign up yet.','我___答应报名。',[('还没有','Have not yet'),('很漂亮','Very beautiful'),('在哪里','Where'),('是朋友','Am a friend')],'还没有 explicitly negates a completed agreement so far.'),
]
daily=mix(daily_r,daily_l,daily_o,daily_c)
write_bank(2,[('identity',identity),('numbers',numbers),('daily',daily)],draft='--install' not in sys.argv)
