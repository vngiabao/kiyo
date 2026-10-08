"""Four original social situations; no lexical quotas inside character speech."""
import sys,json
from editorial_repair import repair,tf,reply,fill,match,ROOT
from advanced_core import rows

TEXTS={
33:(
'''你刚才笑什么？我说错了吗？|What were you laughing at? Did I say something wrong?
不是，你拿杯子的样子让我想到昨晚那部剧。|No. The way you held the cup reminded me of last night's drama.
哪部？我也想看。|Which one? I'd like to watch it too.
就是你推荐的那部。她说茶不甜，下一句却问能不能再放三次糖。|The one you recommended. She says the tea isn't sweet, then asks for sugar three more times.
她每次都这样，我看到那里也笑了。|She always does that. I laughed at that part too.
这杯奶茶真的很甜。你要不要换我的绿茶？|This milk tea really is sweet. Would you like my green tea instead?
不用，你自己喝。我下次记得少放糖就好了。|No, keep yours. I'll remember less sugar next time.
那下次看剧别让我选茶，你会怪我的。|Don't let me choose the tea for our next drama night then. You'll blame me.
我只会怪你提前把后面说出来。|I'll only blame you for telling me what happens next.
好，我不说了。你先看到第五集再来找我。|Fine, I won't. Come back when you've reached episode five.
''',
'''新朋友第一次来家里看剧，我给她倒了一杯奶茶。她喝了一口，说很香，又把杯子放在桌上。|A new friend came over for drama night. I poured milk tea; she took a sip, called it fragrant and put the cup down.
我以为她不喜欢，正想换一杯，她却指着电视笑起来。原来剧里的人也在喝茶，还把糖放个不停。|I was about to replace it, thinking she disliked it, when she laughed at the television. The character was drinking tea and adding sugar endlessly.
我问她是不是也觉得太甜。她说是有一点，不过让她笑的是那个人说不想吃糖，手却一直没停。|I asked whether she found it too sweet. A little, she said, but the joke was the character saying she didn't want sugar while continuing to add it.
后面两个人吵起来，声音很大。我想问她站在哪一边，她说先看完吧，现在还不知道谁把杯子换了。|Two characters later argued loudly. When I asked which side she took, she said to finish watching first: we still didn't know who'd switched the cups.
结束以后，她帮我把桌上的杯子收好。我们都忘了喝第二杯，凉了的茶倒是没刚才那么甜。|Afterward she helped clear the cups. We'd both forgotten our second cup; cold, it didn't seem as sweet as before.
她走到门口又回头说，下次还有茶吗？我说有，不过这次糖放多少，你自己来。|At the door she asked whether there'd be tea next time. Yes, I said, but she'd decide how much sugar to add.
''',
'''你说不提前告诉我，怎么又笑了？|You promised no spoilers. Why are you laughing again?
我看见你的表情了，跟剧里那个人一模一样。|Your expression's exactly like that character's.
别看我，看电视！|Watch the television, not me!
好好好。你刚才说看完要讨论，可别先睡着。|All right. You said we'd discuss it afterward; don't fall asleep first.
我才不会，茶太甜了，我现在一点儿都不困。|I won't. The tea's so sweet I'm wide awake.
那正好，你来洗杯子。|Perfect. You can wash the cups.
'''),
34:(
'''我的包怎么不在衣架旁边了？|Why isn't my bag beside the coat rack?
是这个蓝色的吗？工作人员刚拿到门后了。|The blue one? A staff member just moved it behind the door.
门后？我刚看过，没看见。|Behind the door? I just looked and didn't see it.
门开着的时候会挡住，你先把门关一点。|The open door hides it. Close the door a little.
看到了。我的行李怎么放在这里？|There it is. Why is my luggage here?
刚才来了很多人，你的包放在路中间。他们怕有人被它挡住。|A lot of people came in. Your bag was in the way, and they were worried it would block someone.
是我没放好。我来领行李，要跟谁说？|I didn't put it away properly. Who should I tell before collecting it?
桌子旁边那个人。你告诉她是你的包就行。|The person beside the table. Tell her it's yours.
包带有点儿破了，我得小心拿。|The strap's a little damaged. I need to carry it carefully.
我帮你拿一边。别急，车还有十分钟才来。|I'll take one side. No rush; the bus won't be here for ten minutes.
''',
'''演出结束，我回去找衣架旁边的包。那里多了几件外套，却没有我的蓝色行李。|After the performance I returned to the coat rack. There were more coats there, but my blue luggage was missing.
我问了工作人员，她说已经放到门后。我过去看，门开着，下面只有一双鞋。|A staff member said it had been moved behind the door. I looked, but with the door open all I could see was a pair of shoes.
朋友把门慢慢关上一点，我才看见包在墙边。它没有丢，只是刚才被门挡住了。|My friend partly closed the door. The bag was against the wall: it wasn't lost, just hidden by the door.
领行李的时候，我发现包带破了一小块。工作人员给我一根绳子，朋友帮我把它连起来。|On collecting it I found a small tear in the strap. The staff member gave me cord, and my friend helped secure it.
我们一起把包拿到车站。车还没来，朋友说幸好你没急着自己拿，不然可能走一半就断了。|We carried it to the stop. The bus hadn't arrived. My friend said it was lucky I hadn't rushed to carry it alone: the strap might have snapped halfway.
回家以后，我先把东西拿出来，再给旧包拍了一张照片。下次出门，我会换一个好一点的包。|At home I unpacked and photographed the old bag. I'd use a better bag for my next trip.
''',
'''你说包丢了，我怎么就在门后找到了？|You said the bag was lost. How did I find it behind the door?
那是你眼睛好，我刚才只看见鞋。|You've got better eyes. I only saw the shoes.
门那么大，你倒是看不见。|Yet you somehow missed that huge door.
好了，包找到了，别再笑我。|All right, we found the bag. Stop laughing at me.
行，你拿这边，我拿另一边。|Fine. You take this side; I'll take the other.
谢谢。下次我先找门，不找鞋。|Thanks. Next time I'll look for the door, not the shoes.
'''),
35:(
'''你今天要去看比赛吗？|Are you going to the match today?
去，我们班有人参加决赛。你一起去吗？|Yes. Someone from our class is in the final. Would you come too?
是什么比赛？足球？|What kind of match? Football?
篮球。她平时跳舞，最近也一直在练球。|Basketball. She normally dances, but she's been practising basketball lately too.
那我去。几点开始？|I'll come. What time does it start?
三点。我们两点半在门口见，早点找位置。|Three. Let's meet at the entrance at two thirty to get seats early.
她们现在排名第一吧？|Her team's ranked first now, right?
对，不过今天的对手也很强。上次只赢了两分。|Yes, but today's opponents are strong. They won by just two points last time.
那我们多带一点水，别光顾着喊。|Let's bring extra water and not just keep shouting.
还有你答应带的面包。我可记着呢。|And the bread you promised to bring. I haven't forgotten.
''',
'''下午两点半，我和朋友在门口见面。她抱着两瓶水，我带着一袋面包，一起进了体育馆。|At two thirty I met my friend at the entrance. She had two bottles of water; I brought bread. We entered the sports hall together.
比赛开始以后，我们班的队很快领先。朋友高兴得站起来，我拉她坐下，后面的人还要看。|Our class's team soon took the lead. My friend stood up excitedly; I pulled her down so those behind could see.
第二节，对手把分数追上来了。朋友说今天可能要输，我说还有时间，先把面包吃了。|In the second quarter the opponents caught up. My friend thought we might lose. I said there was time left, so let's eat first.
最后一分钟，两队只差一分。我们都不说话了，连水也忘了喝。结束的时候，我们班多得了三分，终于赢了。|With one minute left, the teams were a point apart. We fell silent and forgot our water. Our class scored three more points before the end and won.
同学出来以后，第一件事是问有没有吃的。我们把剩下的面包给她，她一边吃一边说今天比上次还紧张。|Our classmate came out asking for food. We gave her the remaining bread. She said today's game had been even more tense than last time.
回去路上，朋友说下次她也想试试。我说可以，但别只练站起来喊，那可不算上场。|On the way home my friend wanted to try playing next time. I told her not to practise only standing and shouting: that didn't count as playing.
''',
'''你嗓子怎么这样了？|What happened to your voice?
刚才喊太多了，水都没喝。|I shouted too much and didn't drink water.
我以为比赛的是她，你怎么比她还累？|I thought she was the player. How are you more tired than her?
我们球迷也很努力啊。|We fans work hard too.
那下次别忘了你的水。|Don't forget your water next time then.
行，你也别把面包全吃了。|Fine, but don't eat all the bread yourself either.
'''),
36:(
'''周六一起去种花吗？你上次说想去。|Want to plant flowers together Saturday? You said you were interested.
我还没决定。最近太累，一方面想出去，另一方面又想在家睡觉。|I haven't decided. I'm exhausted: I want to go out, but I also want to sleep at home.
活动十点开始，不用很早起来。|It starts at ten. You wouldn't need to get up very early.
那也要带很多东西吧？|But we'd need to bring a lot, wouldn't we?
不用，我带种子。土和工具那里都有。|No. I'll bring the seeds. Soil and tools are supplied there.
我手还没完全好，可能不能一直做。|My hand hasn't fully recovered, so I might not be able to work the whole time.
你可以先坐着看，想帮忙再来。累了就休息。|You can watch first and help when you want. Rest when you're tired.
这样可以。那我明天晚上再告诉你，好吗？|That sounds manageable. Can I let you know tomorrow evening?
好，别为了陪我就勉强自己。|Sure. Don't push yourself just to keep me company.
知道了。你倒是别太早睡，明天记得看消息。|I know. Don't go to bed too early yourself; check my message tomorrow.
''',
'''周五晚上，我告诉朋友周六想一起去种花。我没有答应做一整天，只想上午去看看。|Friday evening I told my friend I'd join Saturday's planting. I hadn't offered a full day's work, just a morning visit.
十点到那里时，已经有几个人在准备。朋友把种子放好，我坐在旁边听他们介绍。|At ten several people were preparing. My friend set out the seeds; I sat nearby and listened to the introduction.
我试着把一点土放进小盒子，手有些累，就停下来。朋友没有催我，只把椅子往树下挪了一点。|I tried putting some soil in a small box, but my hand tired, so I stopped. My friend didn't hurry me; she moved my chair into the shade.
休息了一会儿，我又过去帮她把名字写在纸上。做不了重的工作，也可以做一点别的。|After a rest I helped label the plants. Even without doing heavy work, there were other little things I could do.
中午有人问我们要不要留下吃饭。我下午还想休息，就和朋友先回去了。她说下周再来看看花有没有长出来。|At noon we were invited to stay for lunch. I wanted an afternoon rest, so we headed home. My friend suggested checking next week whether anything had sprouted.
回家以后，我给她发了今天拍的照片。小盒子里的土还没变化，照片里大家的笑倒是很清楚。|At home I sent her our photos. The soil in the little boxes hadn't changed yet, but everyone's smiles were clear.
''',
'''你说今天只是看看，怎么也种了一盒？|You said you were only watching. How did you plant a whole box?
看着看着就想试了嘛。|Watching made me want to try.
那下周来看看你种的花？|Want to check your flowers next week?
先别叫它花，现在还只有土。|Don't call it a flower yet. It's only soil for now.
行，看看你种的土。|Fine. Let's check the soil you planted.
你这个说法，我听着怎么更奇怪了。|Somehow that sounds even stranger.
''')}

# Two authored situations for each stated sense, separate from the main scene.
VOCAB={
33:'''吵|这里太吵，我们换个地方。|It's too noisy here; let's go elsewhere.|楼下的声音有点儿吵。|It's a little noisy downstairs.
吵架|他们为了这件事吵架了。|They argued about this.|我不想跟你吵架。|I don't want to argue with you.
充满|她的笑让房间充满了快乐。|Her laughter filled the room with joy.|这个故事充满了希望。|This story is full of hope.
传来|门外传来一阵笑声。|Laughter came from outside.|远处传来了汽车的声音。|The sound of a car came from a distance.
传说|这个村有一个古老的传说。|This village has an old legend.|奶奶给我们讲了一个传说。|Grandma told us a legend.
超级|这个箱子超级重。|This case is super heavy.|我今天超级开心。|I'm super happy today.
极了|这顿饭好吃极了。|This meal is delicious.|听到这个消息，她高兴极了。|She was delighted by the news.
乱|我的桌子太乱了。|My desk is a mess.|别把纸放乱了。|Don't mess up the papers.
迷|我弟弟最近迷上了足球。|My brother's got really into football lately.|她很迷这个演员。|She's really into this actor.
巧|真巧，我们坐的是同一班车。|What a coincidence: we're on the same bus.|你也住这里？太巧了。|You live here too? What a coincidence.
热烈|大家热烈欢迎新同学。|Everyone warmly welcomed the new classmate.|讨论进行得很热烈。|The discussion was lively.
香|这个面包闻起来很香。|This bread smells lovely.|刚做好的饭很香。|The freshly cooked meal smells lovely.
奶茶|我想要一杯热奶茶。|I'd like a hot milk tea.|这家的奶茶有点儿甜。|This place's milk tea is a little sweet.
绿茶|她喜欢喝绿茶。|She likes green tea.|我给你带了一包绿茶。|I've brought you a packet of green tea.
毛|猫的白毛掉在椅子上了。|The cat shed white fur on the chair.|这只狗的毛很长。|This dog's fur is long.
只是|我只是想问一下时间。|I just wanted to ask the time.|她只是来送东西，不留下吃饭。|She's only dropping things off, not staying for a meal.
就是|这件衣服很好，就是贵了一点。|This garment's good, just a little expensive.|路不远，就是现在下雨了。|It isn't far; it's just raining now.
据说|据说这个公园下周开门。|I hear this park opens next week.|据说她以前住在这里。|I hear she used to live here.
不断|手机不断响，我没法看书。|My phone keeps ringing, so I can't read.|这几天不断有人来问。|People have kept coming to ask over the last few days.
现象|这里下雪是很少见的现象。|Snow is a rare phenomenon here.|我们讨论了这个现象的原因。|We discussed the cause of this phenomenon.
性|这件事的重要性你已经知道了。|You already know this matter's importance.|我想提高练习的积极性。|I'd like to feel more enthusiastic about practising.
正|把照片放正一点。|Straighten the photo a little.|椅子没放正，我来移动一下。|The chair isn't straight; I'll move it.
''',
34:'''背|我的背有点儿疼。|My back hurts a little.|她的背上沾了一点土。|There's a little soil on her back.
板|这块板可以做桌面。|This board can make a tabletop.|门后有一块木板。|There's a wooden board behind the door.
保|我们先保住这个位置。|Let's hold on to this spot first.|这次至少要保住前两名。|We need to keep a top-two place this time at least.
保护|请保护好自己的书。|Please take care of your books.|这个袋子可以保护相机。|This bag can protect the camera.
步|往前走两步，就能看见门。|Take two steps forward to see the door.|她向后退了一步。|She stepped backward.
部|我昨天看了一部电影。|I watched a film yesterday.|他带了两部手机。|He brought two phones.
断|绳子突然断了。|The rope suddenly snapped.|这根线中间断了一段。|Part of this cable is broken in the middle.
刀|这把刀放在厨房里。|This knife belongs in the kitchen.|请把刀收好。|Please put the knife away.
防|带一件外套，防着晚上变冷。|Bring a coat in case it gets cold tonight.|出门记得防雨。|Remember rain protection when going out.
破|袋子破了一个洞。|There's a hole in the bag.|这双鞋太破了，得换了。|These shoes are worn out; I need new ones.
破坏|大雨破坏了这条小路。|The heavy rain damaged this path.|别破坏我们摆好的东西。|Don't damage the things we've set up.
行李|我的行李已经放在车上了。|My luggage is already in the vehicle.|她只带了一件行李。|She brought just one piece of luggage.
屋子|这间屋子比旁边的亮。|This room is brighter than the neighbouring one.|屋子里还有两把椅子。|There are two more chairs in the room.
衣架|请把外套放在衣架上。|Please put your coat on the hanger.|这个衣架已经坏了。|This hanger's broken.
服装|这家店卖儿童服装。|This shop sells children's clothing.|演出的服装放在箱子里。|The performance costumes are in the case.
短裤|我夏天喜欢穿短裤。|I like shorts in summer.|这条短裤有两个口袋。|These shorts have two pockets.
领|我明天去领新书。|I'll collect the new books tomorrow.|请到门口领自己的东西。|Please collect your belongings at the entrance.
抓|她抓着我的手，不想放开。|She held my hand and didn't want to let go.|先抓住绳子，再慢慢站起来。|Hold the rope before slowly standing.
抓住|我抓住了快掉下来的杯子。|I caught the cup as it was falling.|他想抓住这次机会。|He wants to seize this opportunity.
自动|门会自动关上。|The door closes automatically.|这个灯晚上会自动打开。|This light comes on automatically at night.
围|大家围着桌子坐下。|Everyone sat around the table.|几个人围在门口等消息。|Several people gathered at the door awaiting news.
周围|学校周围有很多小店。|There are many shops around the school.|我看了看周围，没有认识的人。|I looked around and didn't see anyone I knew.
''',
35:'''比赛|比赛明天下午开始。|The match begins tomorrow afternoon.|我们看完比赛再吃饭。|Let's eat after watching the match.
对手|今天的对手很强。|Today's opponent is strong.|她认识自己的对手。|She knows her opponent.
金牌|他得到了一块金牌。|He won a gold medal.|这块金牌是去年得到的。|This gold medal was won last year.
银牌|她把银牌拿给家人看。|She showed her family her silver medal.|他们队这次得了银牌。|Their team won silver this time.
决赛|决赛就在周日。|The final is on Sunday.|我们已经买到了决赛的票。|We've got tickets to the final.
球迷|我是一个足球球迷。|I'm a football fan.|很多球迷早早就到了。|Many fans arrived early.
领先|我们队现在领先两分。|Our team's two points ahead.|她一直领先到最后。|She held the lead until the end.
落后|他们暂时落后了。|They're behind for now.|我不想落后，明天再练一次。|I don't want to fall behind; I'll practise again tomorrow.
排名|我想看看最后的排名。|I'd like to see the final standings.|他的排名比上次高了。|His ranking has improved since last time.
胜|这次我们胜了。|We won this time.|他们连胜了三场。|They won three games in a row.
胜利|大家一起庆祝胜利。|Everyone celebrated the victory.|这次胜利来得不容易。|This victory was hard won.
输|我刚才输了两分。|I lost two points just now.|输了以后，她没有马上走。|She didn't leave immediately after losing.
赢|最后一分钟，我们终于赢了。|We finally won in the last minute.|你赢了，我请你喝茶。|You won; I'll buy you tea.
世界杯|我和朋友一起看世界杯。|I watch the World Cup with friends.|这是上次世界杯的录像。|This is a recording of the previous World Cup.
选手|几位选手已经准备好了。|Several competitors are ready.|那位选手来自我们学校。|That competitor is from our school.
足球|弟弟每周六练足球。|My younger brother practises football Saturdays.|这场足球比赛几点结束？|When does this football match finish?
跳|孩子从椅子上跳了下来。|The child jumped down from the chair.|你先别跳，鞋还没穿好。|Don't jump yet; your shoes aren't on properly.
跳高|他以前练过跳高。|He used to practise the high jump.|跳高比赛下午开始。|The high-jump competition begins this afternoon.
跳舞|她从小就喜欢跳舞。|She's loved dancing since childhood.|你愿意和我一起跳舞吗？|Would you like to dance with me?
跳远|这次跳远的成绩比上次好。|This long-jump result is better than last time.|跳远比赛结束以后，他去找教练。|He went to his coach after the long-jump competition.
游|我们从这里游到那边。|Let's swim from here to there.|她已经游了半小时。|She's been swimming for half an hour.
游泳|我不会游泳，你教我好吗？|I can't swim. Would you teach me?|我们明天去游泳。|Let's go swimming tomorrow.
''',
36:'''一方面|一方面我想参加，另一方面我怕没时间。|I want to join, but I'm afraid I won't have time.|一方面他想买，另一方面又觉得贵。|He wants to buy it but also finds it expensive.
另一方面|我喜欢这门课，另一方面，也想留时间工作。|I like this course, but I also want time for work.|她一方面高兴，另一方面又有点紧张。|She's happy but also a little nervous.
任|她现在任这所学校的校长。|She's now the principal of this school.|他曾经任我们队的队长。|He used to be our team captain.
受|这个办法受到了大家的欢迎。|This approach was welcomed by everyone.|她受了很大的影响。|She was greatly influenced.
受伤|他的手昨天受伤了。|He injured his hand yesterday.|我没受伤，只是有点累。|I'm not injured, just a little tired.
退|请往后退一点。|Please move back a little.|她看到车过来，退了两步。|She stepped back twice when the vehicle approached.
退出|我想退出这次活动。|I'd like to withdraw from this event.|他退出了比赛，但留下来看朋友。|He withdrew from the competition but stayed to watch his friend.
深|这里的水很深。|The water's deep here.|这个盒子比那个深。|This box is deeper than that one.
深刻|那次见面给我留下了深刻的印象。|That meeting left a deep impression.|她的话让我印象深刻。|Her words made a deep impression on me.
深入|我想深入了解这个地区。|I'd like to learn more deeply about this region.|他们深入讨论了这个问题。|They discussed this issue in depth.
温暖|屋子里很温暖。|It's warm in the room.|朋友的关心让我觉得温暖。|My friend's care made me feel warmth.
幸福|跟家人在一起，我觉得很幸福。|I feel happy with my family.|她说现在的生活很幸福。|She says her life is happy now.
幸运|我很幸运，遇到了愿意帮我的人。|I was lucky to meet someone willing to help.|今天真幸运，一出门就有车。|What luck: a vehicle arrived as soon as I went out.
福|门上贴着一个红色的福字。|A red character meaning good fortune is displayed on the door.|奶奶说，平安也是一种福。|Grandma says peace and safety are also a blessing.
生|这个土豆还是生的，没煮好。|This potato's still raw; it isn't cooked through.|生的东西和熟的分开放。|Keep raw and cooked foods separate.
生命|这本书讲植物的生命。|This book is about plant life.|他把时间都用来研究生命。|He devotes his time to studying life.
生存|这种植物在冷的地方也能生存。|This plant can survive in cold places.|没有水，植物很难生存。|Plants struggle to survive without water.
生长|这些花正在慢慢生长。|These flowers are growing slowly.|这种树生长得很快。|This kind of tree grows quickly.
土|盒子里还有一点土。|There's still some soil in the box.|他把种子放进土里。|He put the seeds in the soil.
种子|这些种子是朋友送的。|These seeds were a gift from a friend.|种子还没长出来，我们再等几天。|The seeds haven't sprouted; let's wait a few more days.
头脑|我现在头脑很清楚，可以继续工作。|My mind's clear now; I can keep working.|休息以后，他的头脑清楚多了。|His mind was much clearer after resting.
危险|这里太危险，我们换一条路。|It's too dangerous here; let's take another road.|这种动作有危险，先问教练。|This movement can be dangerous; ask the coach first.
'''}

QUESTIONS={
33:([
('gist','Why is the friend laughing?',['The cup reminds them of a drama','They want to insult the new friend','They have cancelled the viewing'],0),
('detail','What does the milk-tea drinker decide?',['Keep the drink and use less sugar next time','Swap for green tea immediately','Never drink tea again'],0),
('inference','Why stop describing the drama?',['Avoid telling what happens next','The TV has broken','Nobody knows its title'],0)],
[
('gist','What brings the new friends together?',['Watching and discussing a drama over tea','A fight about buying a factory','Preparing a train timetable'],0),
('detail','Why wait before choosing a side in the argument?',['They do not yet know who switched the cups','Every character has already apologised','The programme is over'],0),
('inference','What does asking for tea next time suggest?',['The friend wants another visit','The friend refuses to return','The cups have been stolen'],0)]),
34:([
('gist','What solves the missing-bag problem?',['Partly closing the door reveals the bag','Buying a different suitcase','Cancelling the performance'],0),
('detail','Why was the bag moved?',['It was blocking people’s path','The staff member wanted to sell it','It belonged on a train already'],0),
('inference','Why carry it together?',['Its strap is damaged','The bus has already left','The friend owns every bag'],0)],
[
('gist','What has actually happened to the luggage?',['It was moved and hidden by the open door','It was sold abroad','It was never brought to the performance'],0),
('detail','What does the staff member give the narrator?',['Cord','A new camera','A second phone'],0),
('inference','Why use a different bag next time?',['The old strap is damaged','The inn has closed','The performance has been cancelled'],0)]),
35:([
('gist','What will the friends watch?',['A basketball final with a classmate','A dance exam','A football training session'],0),
('detail','When will they meet?',['Two thirty','Three thirty','Two in the morning'],0),
('inference','Why is the result still uncertain?',['The opponents are strong and the last win was narrow','The match has ended','No opponents will attend'],0)],
[
('gist','How does the match end?',['Their class wins after a tense finish','The match is cancelled','Their class loses before it starts'],0),
('detail','What does their classmate first ask for afterward?',['Food','A new phone','A bus timetable'],0),
('inference','What is the joke on the way home?',['Cheering alone is not playing','Bread counts as a medal','Drinking water cancels the score'],0)]),
36:([
('gist','What makes joining feel manageable?',['A morning visit with breaks and optional help','A promise to work all day without rest','Cancelling every activity forever'],0),
('detail','When will the invitee confirm?',['Tomorrow evening','After the flowers bloom','Next month'],0),
('inference','Why mention the hand?',['It limits how long the person can work','The seeds are missing','The friend has already declined'],0)],
[
('gist','How does the narrator participate?',['Light work, breaks and labelling plants','Only watching without helping at all','Heavy work throughout the afternoon'],0),
('detail','Why leave at lunchtime?',['The narrator wants an afternoon rest','The friend refuses to speak','The flowers have already grown'],0),
('inference','What does the friend moving the chair show?',['Consideration for the narrator’s need to rest','A demand to work faster','An instruction never to return'],0)])}

REPLIES={
33:[('你笑的时候想到谁了？','Who came to mind when you laughed?',['剧里那个总喝奶茶的人。','这杯茶放了两勺糖。','我们下次还看这部剧。']),('怎么让这杯茶没那么甜？','How can we make this tea less sweet?',['加一点没放糖的茶。','再放一勺糖。','把杯子换个颜色。'])],
34:[('包带破了，怎么两个人一起拿？','How can two people carry it with the damaged strap?',['我们一人拿一边。','你一个人背着它跑。','我们先各自拿自己的衣服。']),('门开着，看不见门后，怎么办？','The open door hides what is behind it. What should we do?',['先把门关一点再看看。','把门开得更大一点。','看完再去车站。'])],
35:[('比赛还没结束，现在能确定谁赢吗？','Can we know the winner before the match is over?',['还不能，对手也很强。','能，先得分的就赢了。','知道开场时间就知道结果。']),('她刚比赛完，饿了，我们有面包，能给她什么？','She is hungry after the match and we have bread. What can we give her?',['把剩下的面包给她吧。','把比赛时间告诉她吧。','给她看看明天的安排。'])],
36:[('我手累了，想休息一会儿，坐哪里？','My hand is tired and I want a break. Where can I sit?',['坐树下那把椅子吧。','土和工具都在那里。','明天晚上再告诉我。']),('我明天晚上给你发消息，你什么时候看？','When will you check the message I send tomorrow evening?',['明天晚上我记得看。','我昨天晚上已经看过了。','你还没发，我现在就看到了。'])]}

for number,(d,r,m) in TEXTS.items():
    p=json.loads((ROOT/f'content/packs/s3-u{number:02}.json').read_text('utf-8'))
    examples={};contexts=[]
    for raw in VOCAB[number].strip().splitlines():
        word,z,e,z2,e2=raw.split('|')
        assert word in z and word in z2 and z!=z2
        examples[word]=(z,e);contexts.extend([(z,e),(z2,e2)])
    assert set(examples)=={v['hanzi'] for v in p['vocabulary']}
    dqs,rqs=QUESTIONS[number]
    evidence={33:(5,'The milk tea is sweet.'),34:(3,'Partly closing the door can reveal the bag.'),35:(5,'They will meet at two thirty.'),36:(4,'Soil and tools are available there.')}[number]
    wrong={33:'The visitor refuses all future tea.',34:'The narrator plans to use the same old bag next time.',35:'Standing and shouting alone counts as playing.',36:'Flowers have already sprouted in the boxes.'}[number]
    tasks=[tf(*rows(d)[evidence[0]],evidence[1],True,'This sentence explicitly gives the information.'),tf(*rows(r)[-1],wrong,False,'The passage states a different situation or outcome.'),
           *[reply(z,e,c,0,'The reply answers the specific question without changing its stated facts.') for z,e,c in REPLIES[number]]]
    target={33:['奶茶','只是'],34:['行李','领'],35:['比赛','赢'],36:['种子','任']}[number]
    tasks.extend(fill(*examples[word],word) for word in target)
    entries=list(examples.values())
    tasks.extend(match(entries[i:i+3]) for i in [0,3,6])
    if len(p['tasks'])==10:tasks.append(match(entries[9:12]))
    gloss=[(g['hanzi'],g['meaning']) for t in [p['dialogue'],p['reading'],*p['extraReadings']] for g in t.get('glosses',[])]
    gloss += [('猫','cat'),('倒','pour; tip'),('杯子','cup'),('表情','expression'),('糖','sugar'),('碗','bowl'),('争','argue; contend'),('逗','tease; amuse'),('拦','stop; block'),('罩','cover'),('带','strap; belt'),('沾','have something stick to a surface'),('破','torn; damaged'),(' cord','cord'),('绳子','rope; cord'),('挡','block'),('墙','wall'),('藏','hide'),('冠','champion; crown'),('篮球','basketball'),('体育馆','sports hall'),('追','chase; catch up'),('嗓子','throat; voice'),('戴','wear, of an accessory'),('移','move'),('挪','move; shift'),('重','heavy'),('勉强','force oneself; unwillingly'),('催','urge; hurry someone'),('苗','seedling'),('嘛','explanatory conversational particle'),('校长','school principal'),('队长','team captain'),('人物','character; person'),('拍','take a photo'),('得','obtain; score'),('庆祝','celebrate'),('名','place in a ranking'),('雨','rain'),('针','needle'),('孔','hole')]
    gloss=[(z,e) for z,e in gloss if not z.startswith(' ')]
    gloss += [('阵','short spell; classifier for a burst of sound'),('丢','lose; mislay'),('幸好','fortunately'),('土','soil'),('洞','hole'),('摆','arrange; set out'),('儿童','children'),('抱','hold in one’s arms'),('遇到','encounter'),('贴','stick; affix'),('土豆','potato'),('研究','study; research')]
    spec=dict(dialogue=(rows(d),dqs),reading=(rows(r),rqs),media=(rows(m),[]),examples=examples,contexts=contexts,tasks=tasks,glosses=list(dict.fromkeys(gloss)),
        turns=[(z,e,'Answer the immediate social situation',[c[0]]) for z,e,c in REPLIES[number]],
        review='Removed role lists, grammar definitions, safety/identity disclaimers and abstract cover-all assertions from the story. Each scene has a real social outcome; independent examples preserve unrelated target words. Keys are checked against the actual text, with one true and one false item and concrete reply intentions. Native flags: narrator’s tea taste, 杯子 sugar joke, partly closing a door, damaged strap repair, basketball final chronology, 任 as holding a named position, volunteering invitation and light teasing. Source senses and old task/word IDs are preserved; native language and audio review remain pending.')
    if number==34:spec['title']=('Where did my bag go?','我的包在哪里？')
    if number==35:spec['title']=('A final worth cheering for','一起去看决赛')
    repair(number,spec,publish='--publish' in sys.argv)

# Supply a later independent example's meaning previously inherited from an
# incidental old story line. Its wording, recording key and saved IDs stay valid.
pack=json.loads((ROOT/'content/packs/s3-u39.json').read_text('utf-8'))
text=next(t for t in pack['extraReadings'] if t['id'].endswith('-word-notebook'))
if not any(g['hanzi']=='肯' for g in text.get('glosses',[])):
    text.setdefault('glosses',[]).append(dict(hanzi='肯',pinyin='kěn',meaning='be willing to'))
dest=ROOT/('content/packs' if '--publish' in sys.argv else 'output/parity-editorial-drafts')/'s3-u39.json'
dest.write_text(json.dumps(pack,ensure_ascii=False,indent=2)+'\n','utf-8')

from advanced_reading_repair import dependencies
dependencies({'s4-u11':[('藏','hide; put out of sight','cáng')],
              's5-u01':[('挥','wave; swing'),('灰','dust; ash')],
              's5-u03':[('犹豫','hesitate; hesitation')],
              's5-u04':[('抱怨','complain')],
              's6-u02':[('珍惜','cherish; value'),('维持','maintain')],
              's6-u04':[('珍惜','cherish; value')],
              's6-u05':[('沿','along; follow'),('结局','ending; outcome')],
              's6-u07':[('线索','clue')],
              's6-u11':[('结局','ending; outcome')],
              's6-u12':[('挥','wave; swing')]},publish='--publish' in sys.argv)
