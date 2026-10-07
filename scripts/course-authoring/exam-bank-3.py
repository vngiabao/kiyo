"""Ninety original level-three practice items, not an official mock examination."""
import sys
from exam_authoring import R,L,O,C,mix,write_bank
from common import dictionary
dictionary.update({'好像':'hǎo xiàng','比起':'bǐ qǐ','一会儿':'yī huìr','一点儿':'yī diǎnr','点儿':'diǎnr','开玩笑':'kāi wán xiào','看起来':'kàn qǐ lai','看上去':'kàn shàng qu','没完没了':'méi wán méi liǎo','想法':'xiǎng fǎ','不到':'bù dào','一共':'yī gòng','有空儿':'yǒu kòngr','并没有':'bìng méi yǒu','作为':'zuò wéi','同意':'tóng yì','暖和':'nuǎn huo','有点儿':'yǒu diǎnr','空儿':'kòngr','衣服':'yī fu','清楚':'qīng chu','答应':'dā ying','得':'de'})
scope_r=[
R('只有她同意，我们才把她的照片放上去。她还没回答。','Only if she agrees will we post her photo; she has not replied.','现在能放照片吗？',[('还不能','Not yet'),('已经放了','Already posted'),('一定同意','Certainly agrees'),('不用回答','No answer needed')],'The prerequisite is actual consent; no reply is not consent.'),
R('她不但会唱，还会写；这次只报名写作。','She can sing and write; this time she signs up only for writing.','这次报名什么？',[('写作','Writing'),('唱歌','Singing'),('两种活动都报名','Both'),('两种活动都没报名','Neither')],'Ability in two activities is distinct from this time’s registration.'),
R('除了周三，其他几天都可以。周三她要上课。','Every other day works except Wednesday, when she has class.','哪天不可以？',[('周三','Wednesday'),('周一','Monday'),('周五','Friday'),('周日','Sunday')],'周三 is explicitly excluded.'),
R('他听得清楚，可是最后一句没听懂。','He hears clearly but does not understand the final sentence.','他的困难是什么？',[('最后一句的意思','Meaning of the final sentence'),('所有声音都听不见','Cannot hear any sound'),('不知道谁说话','Does not know the speaker'),('不想听任何话','Does not want to hear anything')],'Signal clarity and comprehension differ; the problem is meaning.'),
R('比起快，她更重视准确。现在读得慢一点。','She values accuracy above speed; she reads a little slowly now.','她更重视什么？',[('准确','Accuracy'),('速度','Speed'),('名次','Ranking'),('声音大','Loudness')],'The priority is explicitly accuracy.'),
R('她看起来很累，自己说只是有点儿冷。','She looks tired but says she is only a little cold.','她本人说什么？',[('有点儿冷','A little cold'),('特别累','Very tired'),('非常生气','Extremely angry'),('已经睡了','Already asleep')],'The question asks her own report rather than appearance.'),
R('这家店不大，东西也不贵，但今天还没开业。','The shop is small and inexpensive but has not opened for business today.','今天能直接买东西吗？',[('还没开业','Not open yet'),('已经买到了','Already bought'),('一定开了','Certainly open'),('价格都改了','All prices changed')],'Today’s opening is explicitly uncompleted.'),
R('他一会儿看书，一会儿听录音，不是同时做。','He alternates reading and recordings, rather than doing both simultaneously.','他怎么练？',[('有时读书，有时听录音','Sometimes reads, sometimes listens to recordings'),('一直只听','Only listening throughout'),('一直只读','Only reading throughout'),('同时做两种练习','Both simultaneously')],'The text explicitly identifies alternation.'),
R('她说好是好，不过地点太远，所以还要再想一想。','She says it is good, but too far away, so she must consider it.','她已经决定参加了吗？',[('还没决定','Not decided'),('已经参加了','Already attended'),('一定不参加','Certainly rejected'),('地点已改','Place already changed')],'A qualified positive evaluation is not a completed decision.'),
R('朋友只是建议读这本书，没有说所有人都喜欢。','The friend recommends this book, not claiming universal liking.','建议说明什么？',[('朋友的建议','The friend’s suggestion'),('人人都喜欢','Everyone likes it'),('已经买了','Already bought'),('没有其他书','No other books exist')],'Recommendation remains the friend’s suggestion, not universal preference.'),
]
scope_l=[
L('活动并没有取消，只是换到二楼。别在一楼等。','The activity is not cancelled; it moves to floor two. Do not wait on floor one.','在哪里等？',[('二楼','Floor two'),('一楼','Floor one'),('门外','Outside the door'),('已经取消','It is cancelled')],'The denial concerns cancellation; the new location is floor two.'),
L('新通知已经发出，但还没收到她的回答。','The new notice is sent, but her reply has not arrived.','什么已经完成？',[('发出通知','Sending the notice'),('收到回答','Receiving the reply'),('她已同意','Her consent'),('活动已结束','The event finished')],'Only sending is completed.'),
L('我问了她两次，第二次才听清楚时间。','I asked twice and heard the time clearly only on the second try.','问了几次？',[('两次','Twice'),('一次','Once'),('三次','Three times'),('没问','Did not ask')],'The count concerns asking twice, not two different people.'),
L('她是来取自己的包的，不是来拿别人的。','She came to collect her own bag, not someone else’s.','她来做什么？',[('取自己的包','Collect her own bag'),('拿别人的包','Take another bag'),('卖衣架','Sell a rack'),('改路线','Change the route')],'The purpose and ownership are explicit.'),
L('十个人左右想参加，具体名单还没确定。','About ten people want to join; the exact list is unconfirmed.','能确定正好是十人吗？',[('不能确定','Cannot establish the exact count'),('正好十人','Exactly ten'),('正好二十人','Exactly twenty'),('没有人想来','Nobody wants to come')],'左右 marks an approximate estimate; it does not exclude an actual count of ten.'),
L('她汉语说得很流利，写作还需要练。','She speaks Chinese fluently; her writing still needs practice.','哪一部分还要练？',[('写作','Writing'),('已经没有要练的','Nothing needs practice'),('只要走路','Only walking'),('只要唱歌','Only singing')],'The stated remaining need is writing.'),
L('图上北在上，东在右；我现在面对南。','North is up and east right on the map; I face south.','图上的东在哪里？',[('右边','Right'),('左边','Left'),('上边','Up'),('下边','Down')],'The question concerns the map, not the speaker’s viewpoint.'),
L('你不用急，我和你一起慢慢说。准确更重要。','Do not rush; I will help you speak at your pace. Accuracy matters more.','她希望怎么说？',[('慢慢说，把话说准确','Speak accurately at one’s pace'),('马上说得很快','Speak very fast at once'),('不可以提问','No questions'),('只看名次','Only check ranking')],'The stated invitation is patient, accurate speech.'),
L('我们又高兴又紧张，明天第一次上台。','We are happy and nervous; tomorrow is our first stage appearance.','现在有什么感受？',[('高兴和紧张都有','Both happy and nervous'),('只有生气','Only angry'),('完全不紧张','Not nervous at all'),('已经表演完','Already performed')],'Both feelings occur; tomorrow’s performance is not complete.'),
L('她一点儿也不生气，不过想把意思说清楚。','She is not angry at all, but wants to clarify her meaning.','她想做什么？',[('说清楚意思','Clarify the meaning'),('继续吵架','Keep quarrelling'),('不问就说','Speak without asking'),('马上取消','Cancel at once')],'The goal is clarification; anger is emphatically denied.'),
]
scope_o=[
O(['只有','她同意','我们才','参加'],'We participate only if she agrees.','在什么条件下参加？',['只有她我们同意才参加','我们只有参加她才同意','她只有同意才我们参加'],'Keep the condition 只有她同意 and response 我们才参加.'),
O(['她','汉语','说得','很流利'],'She speaks Chinese fluently.','谁说得很流利？',['她汉语得说很流利','她说很流利得汉语','很她流利汉语说得'],'The predicate 说得很流利 follows the larger topic 她汉语.'),
O(['我','一点儿也','不','生气'],'I am not angry at all.','说话的人生气吗？',['我一点儿也生不气','一点儿我不生气也','我也不气生一点儿'],'Keep emphatic 一点儿也不 before 生气.'),
O(['我','问了','她','两次'],'I asked her twice.','问了几次？',['我了问她两次','我问两她了次','我次问了她两'],'Put the pronoun object before the event count in this ordinary construction.'),
O(['她','看起来','很','累'],'She looks tired.','谁看起来累？',['她起来看很累','她看很累起来','很她看累起来'],'Keep the visual inference marker 看起来 intact.'),
]
scope_c=[
C('她一点儿也不生气。','She is not angry at all.','她一点儿也___生气。',[('不','Not'),('书','Book'),('水','Water'),('门','Door')],'不 creates the specified emphatic negation.'),
C('只有她同意，我们才参加。','We join only if she agrees.','只有她同意，我们___参加。',[('才','Only then'),('门','Door'),('桌子','Table'),('纸','Paper')],'才 pairs with the stated necessary condition.'),
C('她又高兴又紧张。','She is both happy and nervous.','她又高兴___紧张。',[('又','Also; and'),('书','Book'),('杯子','Cup'),('包','Bag')],'The repeated 又 coordinates the two states.'),
C('活动并没有取消。','The activity has not been cancelled.','活动并___取消。',[('没有','Has not'),('桌子上','On the table'),('门外','Outside'),('很甜','Very sweet')],'并没有 is the stated emphatic denial.'),
C('十个人左右参加。','About ten people attend.','十个人___参加。',[('左右','Approximately'),('桌子','Table'),('房间','Room'),('杯子','Cup')],'左右 follows the quantity to mark approximation.'),
]

plans_r=[
R('她离开这里四天了，昨天才给我打电话。','She left four days ago and called me only yesterday.','她什么时候离开？',[('四天前','Four days ago'),('昨天','Yesterday'),('今天','Today'),('还没离开','Has not left')],'Elapsed time since leaving differs from the later call.'),
R('首先确定场地，然后报名；现在场地还没确定。','First confirm the venue, then register; the venue remains unconfirmed.','下一步先做什么？',[('确定场地','Confirm the venue'),('假装已报名','Pretend registered'),('直接宣布完成','Declare completion'),('忘掉以前的记录','Delete all records')],'The first prerequisite is venue confirmation.'),
R('不是周六，就是周日，主人还没选好。','Either Saturday or Sunday; the host has not chosen.','哪一天已确定？',[('都还没确定','Neither fixed'),('周六','Saturday'),('周日','Sunday'),('周五','Friday')],'The alternative pattern does not choose a date.'),
R('他是负责人，记录结果，但不能代别人同意。','As leader he records results but cannot consent for others.','他做什么工作？',[('记录结果','Record results'),('代所有人同意','Consent for everyone'),('改自己的名字','Change one’s name'),('不看全部问题','Not read all the questions')],'Recording is stated; proxy consent is explicitly excluded.'),
R('包被放到衣架旁边了，没有说是谁放的。','The bag was put beside the rack; the agent is unnamed.','什么是明确的？',[('包在哪里','Bag location'),('是谁放的','Who put it'),('放的原因','Why it was put'),('所有人已同意','Everyone agreed')],'The passive specifies location, not agent or purpose.'),
R('一方面想参加，另一方面今天太累，所以先休息。','I want to attend on one hand, but am tired today, so I will rest first.','现在先做什么？',[('休息','Rest'),('已经上台','Already on stage'),('立刻报名','Register immediately'),('代朋友参加','Attend for a friend')],'The explicit next step is rest.'),
R('不但问了课程安排，而且问了学费；住旅馆的费用还不知道。','She asked about the course schedule and tuition; accommodation costs remain unknown.','什么还不知道？',[('住旅馆的费用','Accommodation cost'),('问没问过学费','Whether tuition was asked'),('问没问过课程','Whether courses were asked'),('她从没提问','She never asked')],'Two inquiries are affirmed; accommodation remains unknown.'),
R('价格从二十块变成二十五块，增加五块。','The price changes from twenty to twenty-five yuan, five yuan more.','增加了多少？',[('五块','Five yuan'),('二十块','Twenty yuan'),('二十五块','Twenty-five yuan'),('五个人','Five people')],'The absolute difference is twenty-five minus twenty.'),
R('路线约两千米，图上是一个环，不说明走了几步。','The route is about two kilometres; its loop drawing does not give steps.','明确的是什么？',[('大概多远','Approximate distance'),('走了几步','How many steps were walked'),('两升水','Two litres of water'),('所有路都开放','All roads open')],'The distance is approximate; steps and accessibility are not given.'),
R('活动还在谈判，只是有初步想法，没有最后结果。','The activity is being negotiated; only a preliminary idea exists, with no final result.','现在是什么状态？',[('仍在谈判','Still negotiating'),('已经全部同意','Everything agreed'),('没有讨论过','Never discussed'),('所有条件取消','Every condition cancelled')],'The preliminary plan does not establish a final agreement.'),
]
plans_l=[
L('从下周起，我每天先读一段，然后听一遍。','Starting next week I first read a passage daily, then hear it once.','什么时候开始这个安排？',[('下周','Next week'),('昨天','Yesterday'),('已经一年','Already a year'),('永远不开始','Never')],'The starting point is next week.'),
L('都九点了，慢就慢一点儿吧，先告诉等你的人。','It is already nine; a little delay is fine, but tell the person waiting first.','先做什么？',[('联系等的人','Contact the person waiting'),('不用告诉任何人','Tell nobody'),('改成昨天','Change to yesterday'),('假装准时','Pretend punctuality')],'The concession does not erase the stated need to notify.'),
L('我看了两遍说明，还没问负责人。','I read the instructions twice and have not asked the leader.','什么还没做？',[('问负责人','Ask the leader'),('第一次读','First reading'),('第二次读','Second reading'),('看到说明','See the instructions')],'Two readings are completed; asking is not.'),
L('为了带书方便，我选书包，不选那只小包。','For convenient book carrying I choose the schoolbag, not the small bag.','目的是什么？',[('带书方便','Carry books conveniently'),('代人报名','Register for someone'),('改时间','Change time'),('买车','Buy a vehicle')],'The purpose is explicitly convenient carrying.'),
L('去村里学习农业是目的，坐车去是方式。','Learning agriculture in the village is the purpose; going by vehicle is the method.','坐车说明什么？',[('方式','Method'),('已经学会','Already learned'),('保证结果','Guaranteed outcome'),('谁是主人','Who is host')],'The text explicitly distinguishes method from purpose.'),
L('除了今天，明天和后天都行。今天没有空儿。','Tomorrow and the following day work, except today when I am busy.','哪天没空儿？',[('今天','Today'),('明天','Tomorrow'),('后天','Following day'),('两天都没空','Neither later day')],'Only today is excluded.'),
L('她被调到新部门，工作地点变了，时间还没变。','She transfers to a new department; the location changed but time stayed the same.','什么变了？',[('工作地点','Workplace'),('工作时间','Work time'),('本人姓名','Her name'),('所有安排','All arrangements')],'The change is restricted to location.'),
L('交通看上去方便，不过旅馆还没订。','Transport seems convenient, but the hotel is not booked.','什么还没完成？',[('订旅馆','Hotel booking'),('已经到旅馆','Already arriving at hotel'),('看交通介绍','Viewing transport information'),('改变所有时间','Changing every time')],'The uncompleted action is the hotel reservation.'),
L('这里两所学校，一所上午开课，一所下午。','There are two schools; one starts morning classes and the other afternoon.','共有几所学校？',[('两所','Two'),('一所','One'),('三个班','Three classes'),('四个房间','Four rooms')],'所 counts institutions, not classes or rooms.'),
L('她说现在处理不了所有邮件，只能先看最紧急的一封。','She cannot handle all mail now and can only read the most urgent one first.','先看什么？',[('最紧急的一封','The most urgent message'),('所有都已看完','All already read'),('任何邮件都不看','No mail at all'),('别人的包','Someone’s private bag')],'A stated capacity limit still allows one specific first action.'),
]
plans_o=[
O(['首先','确定时间','然后','报名'],'Confirm time first, then register.','报名以前先做什么？',['首先确定然后时间报名','首先报名时间然后确定','时间首先报名然后确定'],'Keep 确定时间 as the first action and 报名 as the subsequent one.'),
O(['她','把旧牌子','换成','新牌子'],'She replaces the old sign with a new one.','旧牌子怎么处理？',['她把旧牌子换新成牌子','她旧把牌子换成新牌子','她换成把新牌子旧牌子'],'Keep 把旧牌子 intact and 换成 before the new result.'),
O(['包','被放在','衣架','旁边'],'The bag is placed beside the rack.','包放在哪里？',['包被在放衣架旁边','包在被放衣架旁边','包被放旁边在衣架'],'Keep the passive location 被放在衣架旁边.'),
O(['从下周起','我','每天','读一段'],'Starting next week I read a passage daily.','什么时候开始？',['从下起周我每天读一段','从下周起我每读一段天','我从下周起每天一读段'],'Keep 从下周起 and 每天 intact.'),
O(['她','离开这里','四天','了'],'It has been four days since she left here.','离开多久了？',['她离开四这里天了','她这里四天离了开','四她离开这里了天'],'The elapsed duration 四天 follows the completed departure.'),
]
plans_c=[
C('首先确定，然后报名。','First confirm, then register.','首先确定，___报名。',[('然后','Then'),('衣架','Rack'),('面积','Area'),('金牌','Gold medal')],'然后 introduces the subsequent action.'),
C('我一会儿读，一会儿听。','I alternate reading and listening.','我一会儿读，___听。',[('一会儿','For a spell'),('桌子上','On the table'),('五块','Five yuan'),('屋子','Room')],'Repeating 一会儿 frames alternation.'),
C('不但要读书，而且要听录音。','One must read books and listen to recordings too.','不但要读书，___要听录音。',[('而且','Also; moreover'),('牌子','Sign'),('板','Board'),('地上','On the floor')],'而且 introduces the included addition.'),
C('这个包属于她。','This bag belongs to her.','这个包___她。',[('属于','Belongs to'),('杯子','Cup'),('金牌','Medal'),('面积','Area')],'属于 specifies the ownership relation.'),
C('从下周起每天读一段。','Read a passage daily starting next week.','___下周起每天读一段。',[('从','From'),('门','Door'),('茶','Tea'),('牌子','Sign')],'从 pairs with the stated startpoint and 起.'),
]

media_r=[
R('她在话剧里哭，跟记者说话时说自己很高兴。','She cries in the play but says in an interview she is happy.','跟记者说话时她说什么？',[('很高兴','Happy'),('一直在哭','Always crying'),('一定受伤','Certainly injured'),('没演过话剧','Never acted')],'The question concerns her reported interview state, not the acted character.'),
R('这是去年直播的录像，今天只是重新播放。','This records last year’s live broadcast and is replayed today.','原来什么时候直播？',[('去年','Last year'),('今天','Today'),('明天','Tomorrow'),('从来没播出','Never broadcast')],'Original broadcast time differs from today’s playback.'),
R('台词里的她还没说明是谁，不能只看衣服就说是谁。','The dialogue’s she is unidentified; do not guess from clothing.','现在知道指谁吗？',[('还不知道','Not yet'),('一定是老师','Certainly teacher'),('一定是导演','Certainly director'),('已经问过本人','Already asked the person')],'The reference remains explicitly unresolved.'),
R('她演得很认真，但故事不是真实发生的。','She acts seriously, but the story is fictional.','能确定什么？',[('表演认真','Serious acting'),('事情真实发生','The event truly happened'),('演员自己经历过','The actor experienced it'),('所有台词都是真话','Every line is true')],'Serious performance does not prove actual occurrence.'),
R('这句声音很清楚，字也看得清楚；意思还没理解。','Sound and text are clear but the meaning is not understood.','还有什么困难？',[('意思','Meaning'),('完全听不见','No sound audible'),('完全看不见字','No text visible'),('不知道有没有声音','Unknown whether sound exists')],'Clarity is affirmed; meaning remains unclear.'),
R('歌词里的船和烟是故事的一部分，不是今天的天气报告。','The boat and smoke in the lyrics are part of a story, not today’s weather report.','这段是什么？',[('歌词里的故事','Imagined lyrics'),('天气报告','Weather report'),('真实的出发记录','Real departure record'),('正式通知','Official notice')],'The text states its imaginative genre and excludes weather reporting.'),
R('她只是拿自己的错误开玩笑，不是在笑旁边的人。','She jokes about herself, not the person beside her.','在笑谁？',[('她自己','Herself'),('旁边的人','The person beside her'),('全部观众','All listeners'),('每个演员','Every actor')],'The target of humour is self-directed.'),
R('怕什么啊有时让人不舒服，有时是朋友的支持，要听前后说的话。','怕什么啊 can be uncomfortable or supportive from a friend; listen to what is said around it.','判断需要什么？',[('前后说的话和怎么说','Tone and context'),('只看字数','Only word count'),('只看服装','Only clothing'),('只看播放日期','Only playback date')],'The interpretation depends on delivery and context.'),
R('标题说重大，内容还没给具体情况。','The headline says significant; the body gives no details yet.','什么还缺少？',[('具体情况','Specific details'),('一个标题','A headline'),('重大两个字','The word significant'),('文字','Writing')],'The missing material is detailed information, not the headline.'),
R('原来的牌子写九点，新通知写十点；两条的时间不同。','The old sign says nine and the new notice ten; the two are not one time.','新通知是什么时间？',[('十点','Ten'),('九点','Nine'),('八点','Eight'),('十一点','Eleven')],'The latest specified notice gives ten.'),
]
media_l=[
L('你笑什么啊？我笑自己读错了字，不是笑你。','What are you laughing at? My own reading error, not you.','笑的是谁？',[('自己','Self'),('对方','Other person'),('所有老师','All teachers'),('所有朋友','All friends')],'The second utterance explicitly identifies self-directed humour.'),
L('老师张先生也来了，张先生就是老师，不是两个人。','Teacher Mr Zhang also arrived; teacher and Mr Zhang identify one person.','说的是几个人？',[('一个','One'),('两个','Two'),('三个','Three'),('没说有人来','Nobody is said to arrive')],'The apposition is explicitly one individual.'),
L('我想问这个东西是谁造的，不知道是谁。','I want to ask who made this thing; I do not know who.','说话的人知道是谁吗？',[('不知道','Does not know'),('知道是自己','Knows it is self'),('知道是老师','Knows it is teacher'),('知道是朋友','Knows it is friend')],'The indirect question does not supply an answer.'),
L('把声音调低一点，不用换说话的人。','Lower volume a little; no need to change the speaker.','要调整什么？',[('声音','Volume'),('说话人','Speaker'),('全部台词','All dialogue'),('演员的名字','Actor’s name')],'The requested adjustment is volume, not identity.'),
L('越听越累，就先停一下，不是必须一直听。','If listening makes one increasingly tired, pause; continuous listening is not compulsory.','累的时候怎么办？',[('先停一下','Pause first'),('必须一直听','Must keep listening'),('忘掉以前学习','Forget previous learning'),('立刻结束全部课程','Finish all courses immediately')],'The invitation is to pause; it does not say to forget prior learning.'),
L('十分钟的录像我看了两遍，不是两部录像。','I watched a ten-minute recording twice, not two recordings.','看了几遍？',[('两遍','Twice'),('一遍','Once'),('十遍','Ten times'),('两部不同录像','Two different recordings')],'The count concerns repeated views of one recording.'),
L('她已经把时间改了，但还没把旧牌子换掉。','She changed the time but has not replaced the old sign.','什么还没换？',[('旧牌子','Old sign'),('时间','Time'),('自己的名字','Own name'),('课程全部内容','All course content')],'The time change is complete; sign replacement is not.'),
L('比起自己练，我更喜欢一起读，但今天先自己试。','I prefer reading together to solo practice, but will try alone today.','今天先怎么练？',[('自己试','Try alone'),('已经一起读完','Already completed together'),('不再练','Never practise again'),('代别人回答','Answer for others')],'The question concerns today’s next action, not general preference.'),
L('都十点了，今天先到这里，下次再来。','It is already ten; stop here today and return next time.','今天的安排是什么？',[('先结束','Stop for now'),('必须继续一夜','Must continue all night'),('以后永远不来','Never return'),('过去记录消失','Past records vanish')],'Stopping today does not mean never returning.'),
L('谈过不等于答应，群里最后还要等她自己说。','Discussion is not agreement; the final group-chat line awaits her own answer.','最后要等什么？',[('她自己的回答','Her own answer'),('衣服颜色','Clothing colour'),('杯子的意见','Cup’s opinion'),('钟的回答','Clock’s answer')],'The remaining prerequisite is the actual person’s response.'),
]
media_o=[
O(['我','不知道','她','指谁'],'I do not know whom she refers to.','知道指谁吗？',['我不知道指她谁','我不她知道指谁','我知道不她指谁'],'Keep 不知道 and the embedded reference question 她指谁.'),
O(['她','读得','很','清楚'],'She reads clearly.','读得怎么样？',['她得读很清楚','她读很得清楚','她很得读清楚'],'Keep 得 immediately after 读 before the degree complement.'),
O(['老师','张先生','也','来了'],'Teacher Mr Zhang also arrived.','谁也来了？',['老师张先也生来了','老师张先生也了来','老师张先生来了也'],'Keep the name 张先生 and appositive title 老师 intact.'),
O(['把','声音','调低','一点'],'Lower the sound a little.','要调低什么？',['把声音低一点调','声音把低调一点','把声音调一点低'],'Keep 把声音 and result 调低 before its degree 一点.'),
O(['比起快','她','更重视','准确'],'She values accuracy above speed.','她更重视什么？',['比她起快更重视准确','比起快她更准确重视','她比起更重视快准确'],'Keep the comparison 比起快 and predicate 更重视准确.'),
]
media_c=[
C('我不知道她指谁。','I do not know whom she refers to.','我___她指谁。',[('不知道','Do not know'),('书包','Schoolbag'),('衣架','Rack'),('金牌','Medal')],'不知道 introduces the unanswered indirect question.'),
C('她读得很清楚。','She reads clearly.','她读___很清楚。',[('得','Complement marker'),('桌子','Table'),('杯子','Cup'),('纸','Paper')],'得 connects the verb and degree complement.'),
C('越听越累，就先停一下。','If increasingly tired from listening, pause first.','越听___累，就先停一下。',[('越','Increasingly'),('杯子','Cup'),('衣架','Rack'),('金牌','Medal')],'Repeated 越 pairs the linked changes.'),
C('我只是拿自己的错误开玩笑。','I only joke about myself.','我___拿自己的错误开玩笑。',[('只是','Only'),('桌子上','On the table'),('房间','Room'),('板','Board')],'只是 limits the activity in the stated self-directed joke.'),
C('群里还要等她自己的回答。','The group chat still awaits her own answer.','群里还要等她自己的___。',[('回答','Answer'),('高度','Height'),('石油','Petroleum'),('铁路','Railway')],'The required response is the person’s actual answer.'),
]

write_bank(3,[('identity',mix(scope_r,scope_l,scope_o,scope_c)),('numbers',mix(plans_r,plans_l,plans_o,plans_c)),('daily',mix(media_r,media_l,media_o,media_c))],draft='--install' not in sys.argv)
