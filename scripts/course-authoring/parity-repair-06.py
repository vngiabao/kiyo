"""Authored earlier HSK 3 repairs; separate scenes from lexical coverage."""
import json,sys
from editorial_repair import repair,tf,reply,fill,match,ROOT
from advanced_core import rows
from common import py,dictionary

TEXTS={
21:(
'''你快递到了，我放在门边了。|Your delivery arrived. I put it by the door.
谢谢！你别拆，我订的被子有点大。|Thanks! Don't open it yet; the quilt I ordered is rather big.
这么大一个袋子，你一个人拿得动吗？|Can you carry a bag that big on your own?
能，你帮我把门打开就行。|Yes. Just help me open the door.
等一下，袋子下面湿了。|Wait, the bottom of the bag is wet.
刚才下雨了吧？先别放沙发上。|Was it raining earlier? Let's keep it off the sofa.
放哪里？椅子上也有你的裤子。|Where should it go? Your trousers are on the chair too.
我把裤子拿走，你把袋子放到椅子上。|I'll move the trousers. Put the bag on the chair.
这条绳子太紧了，解不开。|This cord is too tight. I can't undo it.
剪刀在书架上。剪开外面的袋子，别剪到被子。|The scissors are on the bookshelf. Cut the outer bag, not the quilt.
里面没湿。你今晚就盖这个？|It's dry inside. Are you using it tonight?
对，旧被子明天洗。谢谢你，差点把新被子留在门口过夜。|Yes. I'll wash the old one tomorrow. Thanks; I nearly left the new quilt outside overnight.
''',
'''我下班回家时，看见门边放着一个很大的袋子。房东帮我收了快递，还发消息说今天下雨，袋子下面湿了。|When I got home from work, I found a large bag beside the door. The landlord had taken my delivery and messaged that the rain had wet the bottom.
我想把袋子直接放在沙发上，朋友拦住我，说先看看里面。我把裤子挪到另一把椅子上，两个人才有地方放袋子。|I was going to put it straight on the sofa. My friend stopped me and suggested checking inside first. I moved my trousers to the other chair so we had somewhere to put the bag.
绳子太紧，朋友拉了几次也没有解开。我去书架上拿剪刀，慢慢剪开外面的袋子，里面的被子没有湿。|The cord was too tight to undo. I fetched scissors from the bookshelf and carefully cut the outer bag. The quilt inside was dry.
我高兴地把新被子抱进卧室，想今晚就用。朋友问旧的放哪里，我说先和裤子放在一起，明天再洗。|I happily took the new quilt into the bedroom to use that night. My friend asked about the old one. I'd put it with the trousers until I washed it tomorrow.
两把椅子都放满东西，我们只好坐在沙发上喝水。朋友笑着说，你现在最需要订的，可能不是被子，是一个更大的房间。|Both chairs were now full, so we sat on the sofa with water. My friend joked that my next order should perhaps be a bigger room, not another quilt.
我把裤子挂好，旧被子搬进卧室，终于空出一个座位。房间没变大，至少明天吃早饭不用站着了。|I hung up the trousers and moved the old quilt into the bedroom, finally freeing a seat. The room was no bigger, but at least I wouldn't have to eat breakfast standing up.
''',
'''你把剪刀放哪里了？|Where did you put the scissors?
书架上，最上面那一层。|On the top shelf of the bookshelf.
我够不到。|I can't reach.
那我来。你别把被子当椅子踩。|I'll get them. Don't stand on the quilt as if it were a chair.
我只是想试试软不软。|I was just testing how soft it is.
用脚试？今晚这被子归你了。|With your feet? This quilt is yours tonight, then.
'''),
22:(
'''除了我，你们都看过这个节目了？|Has everyone seen this show except me?
我也没看完，只看了开头。|I haven't finished either. I've only seen the beginning.
那你干吗说最后一集最好？|Then why did you say the last episode was the best?
我听姐姐说的。她一边看一边哭，纸都用完了。|My sister told me. She cried so much watching it that she used up the tissues.
这么动人？我还以为是那种一直让人笑的节目。|Is it that moving? I thought it was the kind that keeps you laughing.
开头是很好笑。后面怎么样，我真不知道。|The beginning is funny. I honestly don't know about the rest.
今晚电视台还播吗？|Is the TV station showing it again tonight?
八点重播第一集。你要来我家一起看吗？|The first episode is repeated at eight. Want to watch at my place?
来。除了看节目，我们还可以点个晚饭。|Yes. Besides watching, we can order dinner.
好，但你别看到一半就问最后谁回来了。|Fine, but don't ask who returns at the end halfway through.
你不是也不知道吗？|You don't know either, do you?
所以别问，我也想知道。|Exactly. Don't ask; I want to find out too.
''',
'''最近朋友们都在聊一个电视节目。我没看过，听他们说最后一集时，总觉得自己少认识了几个朋友。|My friends have been talking about a TV show. When they discussed its last episode, I felt as if there were a few friends I had yet to meet.
陈宇说除了看最后一集，还得从第一集开始。我问他是不是全看完了，他承认只看了开头，后面的情节都是姐姐告诉他的。|Chen Yu said I needed the first episode as well as the last. When I asked if he had finished it, he admitted he had only seen the beginning. His sister had told him the rest.
我们在互联网上查到电视台晚上八点重播第一集。我下班后带了晚饭去他家，两个人先吃，再打开电视。|Online we found that the station repeated episode one at eight. I took dinner to his place after work. We ate before turning on the TV.
节目开头很好笑，陈宇总看我有没有笑。我说你也看屏幕，别把我当观众里的唯一一个人。|The opening was funny. Chen Yu kept checking my reaction. I told him to watch the screen too, instead of treating me as the only person in the audience.
看到最后，门外响起一个人的声音，可画面没有拍到是谁。我们都想再看一集，明天却还要上班，只好先关掉。|At the end someone spoke outside the door, but the camera did not show who. We both wanted another episode, but work the next day meant switching off.
回家以后，我给他发消息说除了周五晚上，其他晚上都能再看。他马上回，周四吧，我也想知道门外是谁。|Back home I messaged that any evening except Friday worked for another episode. He immediately suggested Thursday: he wanted to know who was outside too.
''',
'''你姐姐说门外是谁了吗？|Did your sister tell you who was outside?
说了，但我忘了名字。|Yes, but I've forgotten the name.
这个时候忘得正好。|That's a good time to forget.
那你别帮我想起来。|Don't help me remember, then.
除了看下一集，我们还有别的办法吗？|Have we got another way besides watching the next episode?
有，问姐姐。不过我想自己看。|Yes, we could ask my sister. But I want to watch it myself.
'''),
23:(
'''周五一起做饭吧？我想叫上小周。|Shall we cook together on Friday? I'd like to invite Xiao Zhou.
周五不行，我要加班。周六能不能来？|I can't on Friday; I'm working late. Would Saturday work?
我问问她。你想吃什么？|I'll ask her. What would you like to eat?
面条吧，不光吃饭，还能一起看节目。|Noodles. We could watch a show as well as eat.
好主意。要是她来，我做三个人的。|Good idea. If she comes, I'll cook for three.
她上次说不能吃很辣的，别忘了。|She said she couldn't eat very spicy food last time. Don't forget.
那辣的放旁边，自己加。|We can put the chilli on the side and add it ourselves.
我同意。只有你自己吃的那碗，才可以全放进去。|Agreed. Only your own bowl gets the whole lot.
你反对我的做法？|You object to my cooking?
我反对把我的面条变成一碗辣椒。|I object to my noodles becoming a bowl of chilli.
行，我周六下午买菜，你带饮料。|Fine. I'll buy groceries on Saturday afternoon; you bring drinks.
好，并且我会带一个能吃饭的嘴。|Yes. And I'll bring a mouth ready to eat.
''',
'''我想周五请朋友来做饭，陈宇却要加班。他提议改到周六，我问过小周以后，三个人都同意了。|I wanted friends over to cook on Friday, but Chen Yu had to work late. He suggested Saturday. After I checked with Xiao Zhou, all three of us agreed.
小周说只要不太辣，她就很想吃面条。我平时爱吃辣，原来打算把辣椒直接放进锅里，这次先把它留在一只小碗里。|Xiao Zhou wanted noodles as long as they were not too spicy. I usually like chilli in the pot, but this time I kept it in a small bowl.
周六下午，我买了面条和蔬菜，并且提前洗好三个碗。陈宇带来饮料，还带了一个大碗，说小碗恐怕不够他吃。|On Saturday afternoon I bought noodles and vegetables and washed three bowls in advance. Chen Yu brought drinks and a large bowl, saying a small one might not be enough.
面条煮好以后，小周先尝了一口，说这样正好。我给自己的那碗加了辣椒，陈宇加了一点，又赶紧拿饮料。|Once the noodles were ready, Xiao Zhou tasted hers and said they were just right. I added chilli to my bowl. Chen Yu tried a little and quickly reached for his drink.
我们一边吃一边看节目。好笑的地方来了，陈宇差点把饮料放进我的碗里，说下次只有他自己吃的那碗，才可以离饮料这么近。|We ate while watching a show. At a funny moment Chen Yu nearly put his drink in my bowl. He said next time only his own bowl should be that close to his drink.
吃完以后，小周帮我洗碗，陈宇把剩下的饮料收好。三个人商量，下次去他家，他说可以，但先别期待他也能做饭。|After eating, Xiao Zhou helped wash up and Chen Yu put away the drinks. We agreed to meet at his place next time. He said yes, but asked us not to expect him to cook too.
''',
'''你带的这个大碗，能放多少面条？|How many noodles does that big bowl hold?
不知道，要是吃不完，我就带回家。|I don't know. If I can't finish, I'll take them home.
你不仅来吃饭，还想带走？|You want food to take away as well?
我还带了饮料，不是空手来的。|I brought drinks. I didn't arrive empty-handed.
那我认可这个理由。|I'll accept that reason.
谢谢，面条可以再加一点吗？|Thanks. Could I have a few more noodles?
'''),
24:(
'''哈哈，你怎么把周六看成周日了？|Ha! How did you read Saturday as Sunday?
我看错了。你干吗一直笑？|I misread it. Why are you still laughing?
不是笑你，我上次星期一才去，门都关了。|I'm not laughing at you. Last time I went on Monday; the place was closed.
那你比我还晚一天。|Then you were a day later than me.
所以我们这次一起去，谁也别一个人看通知。|So let's go together this time and check the notice together.
好，你念时间，我看地址。|You read the time aloud; I'll look at the address.
周六，下午两点。|Saturday, two in the afternoon.
你突然说这么大声干吗？我听见了。|Why did you suddenly get so loud? I heard you.
我怕你又听成周日。|I was worried you'd hear Sunday again.
好好说就行，我还没紧张到连两点都听不见。|Just speak normally. I'm not so nervous that I can't hear two o'clock.
行，周六一点半在车站见？|All right. Shall we meet at the station at one thirty on Saturday?
好。要是我星期一才来，你就别等了。|Yes. If I turn up on Monday, don't wait for me.
''',
'''我把活动时间看成周日下午两点，准备约陈宇一起去。他看了通知，问我为什么要晚一天。|I read the event time as two on Sunday afternoon and was about to invite Chen Yu. He looked at the notice and asked why I wanted to go a day late.
我有点不好意思。他却笑起来，说自己上次星期一才到，门口连一个人都没有。我也笑了，原来不是只有我会看错。|I felt embarrassed. He laughed and said he had gone on Monday last time, when no one was at the door. I laughed too: I was not the only one who misread it.
这次我们把通知再看一遍。他念时间，我读地址，读完还把两个信息写在一起。活动是周六下午两点，我们约一点半在车站见。|This time we checked the notice again. He read the time and I read the address; we wrote both down together. The event was at two on Saturday, so we arranged to meet at the station at one thirty.
周六我一点二十分就到了。陈宇来时问我是不是紧张，我说不是，刚才那班车来得早，我就上了。|I reached the station at one twenty on Saturday. When Chen Yu asked if I was nervous, I explained that an early bus had come along and I had taken it.
我们到门口时，里面已经有音乐声。今天真有人，陈宇说完自己先笑了。我让他进去再笑，后面还有人在等。|At the entrance we could already hear music. Chen Yu said there really were people there today and laughed. I told him to go in before laughing: others were waiting behind us.
表演结束后，我们在路边吃东西。陈宇问下周还来不来，我说先看看日期，今天总算没白跑。|After the performance we ate by the road. Chen Yu asked about coming next week. I suggested checking the date first. At least we had not made a wasted trip today.
''',
'''你今天看着很精神。|You look full of energy today.
我昨晚睡得早，今天状态不错。|I went to bed early. I'm feeling good today.
那你把下一次的通知也读一下。|Read the notice for the next event too, then.
我这么精神，就是为了替你看日期？|All this energy just to check dates for you?
你念得比我清楚嘛。|You read them more clearly than I do.
好，听着，这次你自己记下来。|All right, listen. This time write it down yourself.
''')}

VOCAB={
21:'''把|请把那杯水拿过来。|Please bring that glass of water.|她把钥匙放在桌上了。|She put the keys on the table.
被|我的鞋被雨弄湿了。|My shoes got wet in the rain.|门被风吹开了。|The wind blew the door open.
叫|我的外套叫他拿走了。|He took my coat away.|这张纸叫弟弟弄坏了。|My younger brother damaged this paper.
房东|房东明天来修门。|The landlord is coming to fix the door tomorrow.|我给房东打电话，问能不能养猫。|I called the landlord to ask about keeping a cat.
房屋|这张图画了街边的房屋。|This picture shows the houses along the street.|房屋里面很干净。|The inside of the house is clean.
房租|我今天交了房租。|I paid the rent today.|这间房的房租比那间高。|The rent for this room is higher than for that one.
订|我们订了两张票。|We booked two tickets.|她想订一个生日蛋糕。|She wants to order a birthday cake.
放到|把书放到我包里吧。|Put the book in my bag.|他把椅子放到窗边了。|He moved the chair beside the window.
挂|外套挂在门后。|The coat hangs behind the door.|我想把这张画挂在墙上。|I'd like to hang this picture on the wall.
解开|她帮我解开绳子。|She helped me undo the cord.|先解开袋子，再拿里面的东西。|Open the bag before taking anything out.
紧|这双鞋有点紧。|These shoes are a little tight.|瓶盖太紧，我打不开。|The bottle cap is too tight for me to open.
旧|我把旧手机给了弟弟。|I gave my old phone to my younger brother.|这张旧照片是在北京拍的。|This old photo was taken in Beijing.
书架|书架上还有几个空位。|There are a few empty spaces on the bookshelf.|我买了一个小书架放在床边。|I bought a small bookshelf to put by the bed.
沙发|猫睡在沙发上。|The cat is asleep on the sofa.|这个沙发坐着很舒服。|This sofa is comfortable to sit on.
被子|我把被子拿出去晒了。|I took the quilt outside to air.|晚上冷，记得盖好被子。|It's cold at night. Keep the quilt over you.
裤子|这条裤子太长了。|These trousers are too long.|他的裤子上有一点泥。|There is some mud on his trousers.
衬衫|他今天穿了一件白衬衫。|He is wearing a white shirt today.|这件衬衫洗完以后变小了。|This shirt shrank after washing.
衬衣|她把衬衣挂起来了。|She hung up the shirt.|我给爸爸买了一件新衬衣。|I bought my father a new shirt.
上衣|这件上衣和那条裤子很合适。|This top goes well with those trousers.|我的上衣留在朋友家了。|I left my top at a friend's home.
裙子|她试了一条蓝裙子。|She tried on a blue skirt.|这条裙子没有口袋。|This skirt has no pockets.
皮包|妈妈的皮包放在椅子上。|My mother's leather handbag is on the chair.|这个皮包是她自己买的。|She bought this leather handbag herself.
皮|这双鞋是皮的。|These shoes are leather.|这件衣服用了很软的皮。|This garment uses very soft leather.''',
22:'''除了|除了小周，其他人都到了。|Everyone except Xiao Zhou has arrived.|除了看电影，我还喜欢画画。|Besides watching films, I like drawing.
普遍|手机支付已经很普遍了。|Paying by phone is widespread now.|这类问题在刚开始的时候很普遍。|This kind of problem is common at the beginning.
类|你喜欢哪一类电影？|What kind of films do you like?|这两类书放在不同的书架上。|These two types of books go on different shelves.
类似|我昨天也遇到过类似的问题。|I had a similar problem yesterday.|这道菜和我妈妈做的很类似。|This dish is similar to my mother's version.
区别|这两个词有什么区别？|What's the difference between these words?|我尝不出两种茶的区别。|I can't taste the difference between these teas.
具有|这座房屋具有古代建筑的特色。|This house has features of ancient architecture.|这种材料具有一定的保温作用。|This material has some insulating properties.
人生|她把人生中的重要时刻写成了一本书。|She wrote a book about important moments in her life.|他在朋友的帮助下开始了新的人生。|With friends' help, he began a new life.
全场|音乐响起，全场都安静了。|When the music began, the whole room fell quiet.|他一上台，全场就笑了。|The whole audience laughed as soon as he came on stage.
观众|观众在门外排队。|The audience is queuing outside.|表演结束后，观众站起来鼓掌。|After the performance the audience stood and applauded.
观看|我们准备一起观看决赛。|We're going to watch the final together.|这段视频可以反复观看。|This video can be watched repeatedly.
收看|她每天晚上收看新闻。|She watches the news every evening.|欢迎收看今天的节目。|Welcome to today's programme.
收听|我爸爸开车时收听广播。|My father listens to the radio while driving.|感谢大家收听，下周再见。|Thanks for listening. See you next week.
听众|有位听众打电话来点歌。|A listener called to request a song.|主持人读了听众寄来的信。|The host read a listener's letter.
广播|我在广播里听到了这首歌。|I heard this song on the radio.|车站广播通知旅客换站台。|The station announcement told passengers to change platforms.
电台|这家电台每天早上七点播新闻。|This station broadcasts news at seven each morning.|她想去电台工作。|She wants to work at a radio station.
电视台|电视台今天来学校拍节目。|The TV station is filming at the school today.|我姐姐在电视台工作。|My sister works at a TV station.
国内|这个节目在国内很受欢迎。|This show is popular within the country.|他先在国内旅行，后来去了国外。|He travelled domestically before going abroad.
全球|比赛吸引了全球的观众。|The match attracted viewers around the world.|这家公司的产品销往全球。|This company's products are sold worldwide.
广大|这封信感谢了广大读者。|The letter thanked the many readers.|活动欢迎广大市民参加。|The event welcomes the public to take part.
媒体|几家媒体报道了这场比赛。|Several media outlets covered the match.|她在媒体上看到这条消息。|She saw this news in the media.
互联网|我通过互联网和家人联系。|I keep in touch with family over the internet.|这家小店也在互联网上卖东西。|This little shop also sells online.
联合|两所学校联合举办了比赛。|Two schools jointly held the competition.|他们联合起来解决了这个问题。|They joined forces to solve the problem.''',
23:'''并且|他买了菜，并且洗好了碗。|He bought groceries and washed the bowls.|她会唱歌，并且会弹琴。|She can sing and play an instrument.
不光|不光我喜欢，弟弟也喜欢。|My younger brother likes it as well as me.|这家店不光卖书，还卖咖啡。|This shop sells coffee as well as books.
不仅|她不仅来了，还带了朋友。|She came and brought a friend too.|他不仅会做饭，还会做蛋糕。|He can make cakes as well as cook.
要是|要是下雨，我们就坐车。|If it rains, we'll take a bus.|要是你有空，就来喝茶吧。|If you're free, come over for tea.
只有|只有把门关好，屋里才暖和。|The room only stays warm if the door is properly shut.|只有周六我才有空。|I'm only free on Saturday.
同意|爸爸同意我周末出去玩。|My father agreed to let me go out at the weekend.|我们都同意先吃饭。|We all agreed to eat first.
反对|我反对把旧树砍掉。|I object to cutting down the old tree.|她没有反对，只是问了一下费用。|She did not object; she just asked about the cost.
坚决|他坚决不肯换座位。|He firmly refused to change seats.|妈妈坚决反对我晚上一个人去。|My mother strongly opposed my going alone at night.
主张|她主张先修好屋顶。|She advocated repairing the roof first.|我主张把时间留给大家提问。|I suggest leaving time for everyone's questions.
主意|你有什么好主意？|Have you got a good idea?|这个主意是小周提的。|Xiao Zhou suggested this idea.
制定|学校制定了新的时间表。|The school drew up a new timetable.|我们先制定旅行计划。|Let's draw up a travel plan first.
制度|公司改了休假制度。|The company changed its leave system.|这项制度已经用了十年。|This system has been used for ten years.
规范|老师说我的书写越来越规范。|The teacher says my handwriting is becoming more standard.|这家公司有完整的服务规范。|This company has a complete set of service standards.
合法|这家公司的经营是合法的。|This company operates legally.|他问这份合同是否合法。|He asked whether this contract was legal.
批准|学校批准了我们的申请。|The school approved our application.|这个项目还没有得到批准。|This project has not yet been approved.
认可|她的设计得到了大家的认可。|Everyone approved of her design.|老师认可了我的修改。|The teacher accepted my revisions.
确保|出门前，他确保窗户都关好了。|Before leaving, he made sure all the windows were shut.|我想确保每个人都有座位。|I'd like to make sure everyone has a seat.
防止|把杯子放远一点，防止被碰倒。|Move the cup further away so it won't be knocked over.|她写了张纸条，防止自己忘记。|She wrote herself a note to avoid forgetting.
预防|医生告诉我们怎样预防感冒。|The doctor told us how to prevent colds.|这次检查是为了预防机器故障。|This inspection is to prevent machine faults.
情况|你先说说今天的情况。|Tell me how things went today.|我打电话问了他的情况。|I called to ask how he was doing.
如何|她教我如何使用这个工具。|She taught me how to use this tool.|我还不知道如何回答他。|I still don't know how to answer him.
能不能|你能不能帮我拿一下？|Could you help me carry this?|我们能不能晚一点走？|Could we leave a little later?''',
24:'''哈哈|她在消息里写了哈哈。|She wrote “haha” in her message.|哈哈，原来你也忘了。|Ha! So you forgot too.
干吗|你干吗穿这么多？|Why are you wearing so many layers?|你站在门口干吗？|What are you doing at the door?
话题|他们换了一个话题。|They changed the subject.|这个话题我们昨天谈过。|We discussed this subject yesterday.
念|她给奶奶念了一封信。|She read a letter aloud to her grandmother.|你念慢一点，我想记下来。|Read more slowly; I'd like to write it down.
突然|突然下雨了。|It suddenly started raining.|门突然开了，我吓了一跳。|The door suddenly opened and startled me.
快速|他快速收好东西就出门了。|He quickly packed his things and left.|这个方法可以快速找到文件。|This method finds files quickly.
速度|车的速度慢下来了。|The car slowed down.|他跑步的速度比我快。|He runs faster than I do.
静|夜里，这条街很静。|This street is quiet at night.|屋里很静，只听得见钟的声音。|The room is quiet; only the clock can be heard.
紧张|她第一次上台，有点紧张。|She is nervous about going on stage for the first time.|别紧张，我陪你进去。|Don't be nervous; I'll go in with you.
乐|听到这句话，他乐了。|He laughed at those words.|他们一边看照片一边乐。|They laughed while looking at the photos.
乐观|她对明年的生活很乐观。|She is optimistic about life next year.|他总能找到办法，很乐观。|He always finds a way and is optimistic.
欢乐|大家一起度过了一个欢乐的晚上。|Everyone enjoyed a happy evening together.|屋里充满了欢乐的笑声。|The room was full of happy laughter.
活|他把这个人物演活了。|He brought this character to life.|她把故事讲得很活。|She tells the story vividly.
生动|老师讲的故事很生动。|The teacher's story is vivid.|这张照片生动地表现了当时的生活。|This photo vividly captures life at that time.
动人|她的歌声很动人。|Her singing is moving.|这是一个很动人的故事。|This is a very moving story.
表现|他今天的表现比上次好。|He did better today than last time.|她在比赛中表现得很好。|She performed well in the competition.
表演|我们晚上去看表演。|We're going to see a performance tonight.|孩子们准备了一个小表演。|The children prepared a short performance.
明显|他的进步很明显。|His progress is clear.|两张图的区别很明显。|The difference between the two pictures is obvious.
精神|睡了一觉，我精神多了。|After some sleep, I feel much more energetic.|她今天看着很精神。|She looks full of energy today.
状态|今天状态不错，我想再跑一圈。|I'm feeling good today; I'd like another lap.|他工作时的状态比昨天好。|He is doing better at work than yesterday.
自觉|孩子们自觉把玩具收好了。|The children put their toys away without being asked.|大家都很自觉，没有人插队。|Everyone behaved considerately; no one cut the queue.
好好|回去好好休息吧。|Go home and get a good rest.|我想好好学做饭。|I'd like to learn to cook properly.'''}

QUESTIONS={
21:([
('gist','What are they doing?',['Opening a delivery and finding a dry place for it','Buying a sofa','Moving to a bigger flat'],0),
('detail','Where do they put the wet outer bag?',['On the chair after moving the trousers','On the sofa','On the bed'],0),
('inference','Why mention scissors?',['The tight cord will not come undone','They want to cut the quilt','They are making clothes'],0)], [
('gist','What changes by the end?',['A chair is free after the trousers are hung up','The room becomes bigger','The quilt is washed'],0),
('detail','Is the quilt wet inside?',['No','Yes','They never open it'],0),
('inference','What is the bigger-room remark?',['A joke about how full the room is','A confirmed rental offer','A request to throw away the quilt'],0)]),
22:([
('gist','What do they decide?',['Watch episode one together and order dinner','Ask the sister to tell every detail','Watch only the last episode'],0),
('detail','How much has the friend watched?',['Only the beginning','The whole series','None at all'],0),
('inference','Why not ask about the ending?',['Both want to find out by watching','The friend refuses all television','The sister has never watched'],0)], [
('gist','What brings them together?',['Catching up on a show friends discuss','Preparing a radio broadcast','Performing on television'],0),
('detail','Which evening do they arrange next?',['Thursday','Friday','They do not choose an evening'],0),
('inference','Why stop after one episode?',['They have work the next day','They already know the ending','The TV is broken'],0)]),
23:([
('gist','What are they planning?',['Noodles and a show on Saturday','A Friday work meeting','A cooking competition'],0),
('detail','Where should the chilli go?',['On the side for people to add','Into every bowl','Into the drinks'],0),
('inference','What does the bowl-of-chilli complaint mean?',['The friend wants less chilli in his noodles','He refuses to eat anything','He wants to replace all noodles with chilli'],0)], [
('gist','How does the meal go?',['They share noodles, watch a show and clean up','Xiao Zhou cancels','Nobody brings drinks'],0),
('detail','Who brings the large bowl?',['Chen Yu','Xiao Zhou','The landlord'],0),
('inference','What does Chen Yu say about next time?',['They may visit him but should not expect him to cook','He has already made next week’s meal','He refuses to meet again'],0)]),
24:([
('gist','What are they sorting out?',['A mistaken date and where to meet','A missed Monday class','How to perform on stage'],0),
('detail','When do they meet at the station?',['Saturday at one thirty','Sunday at two','Monday at one thirty'],0),
('inference','Why does the friend laugh at the date mistake?',['He once made a worse mistake himself','He wants to exclude the narrator','He thinks the event is cancelled'],0)], [
('gist','What is different this time?',['They check the notice and reach the right event','They go a day late again','They never enter'],0),
('detail','Why does the narrator reach the station early?',['An early bus came along','The performance began at one twenty','Chen Yu demanded it'],0),
('inference','Why say there really are people today?',['Chen Yu remembers his earlier trip to a closed venue','They expect the venue to be empty','They are counting attendance for an exam'],0)])}

REPLIES={
21:[('袋子下面湿了，放哪里？','The bag is wet underneath. Where should it go?',['先放椅子上，别放沙发上。','直接放新被子上。','明天再买一把剪刀。']),('绳子解不开，剪刀在哪里？','Where are the scissors for this tight cord?',['在书架上，我拿给你。','今天下雨了。','我还没洗旧被子。'])],
22:[('你只看了开头，知道最后是谁吗？','Do you know who appears at the end if you only watched the beginning?',['不知道，我也想接着看。','知道，我看完每一集了。','观众在门外排队。']),('周五不行，周四一起看吗？','Friday does not work. Watch together on Thursday?',['好，周四晚上见。','那就周五见。','第一集晚上八点播。'])],
23:[('小周不能吃太辣的，辣椒怎么办？','What should we do with the chilli if Xiao Zhou cannot eat very spicy food?',['放旁边，想吃的人自己加。','每一碗都多放一点。','周五你要加班。']),('你周六带饮料，我买菜，行吗？','Will you bring drinks on Saturday while I buy groceries?',['行，我带饮料。','你周五不能来。','只有我吃的才是面条。'])],
24:[('活动周六两点，几点在车站见？','The event is at two on Saturday. When should we meet at the station?',['周六一点半吧。','周日两点吧。','星期一门口见。']),('你怎么今天这么早？','Why are you so early today?',['刚才那班车来得早，我就上了。','我以为今天是星期一。','活动昨天已经结束了。'])]}

for number,(d,r,m) in TEXTS.items():
    if number==24:dictionary['精神']='jīng shen'  # Energetic, not the noun spirit.
    pack=json.loads((ROOT/f'content/packs/s3-u{number:02}.json').read_text('utf-8'))
    examples={};contexts=[]
    for raw in VOCAB[number].splitlines():
        word,z,e,z2,e2=raw.split('|');assert word in z and word in z2 and z!=z2
        examples[word]=(z,e);contexts.extend([(z,e),(z2,e2)])
    assert set(examples)=={v['hanzi'] for v in pack['vocabulary']}
    dqs,rqs=QUESTIONS[number]
    true_index={21:9,22:7,23:10,24:10}[number]
    true_statement={21:'The scissors are on the bookshelf.',22:'Episode one is repeated at eight.',23:'Groceries will be bought on Saturday afternoon.',24:'They arrange to meet at the station on Saturday at one thirty.'}[number]
    false_statement={21:'The room has become bigger.',22:'The next meeting is on Friday.',23:'Chen Yu promises to cook next time.',24:'They left without seeing the performance.'}[number]
    tasks=[tf(*rows(d)[true_index],true_statement,True,'The line explicitly states this detail.'),tf(*rows(r)[-1],false_statement,False,'The passage gives a different outcome.'),
           *[reply(z,e,c,0,'Only this reply answers the immediate question with the stated facts.') for z,e,c in REPLIES[number]]]
    targets={21:['解开','订'],22:['除了','全场'],23:['只有','同意'],24:['突然','紧张']}[number]
    tasks.extend(fill(*examples[word],word) for word in targets)
    example_rows=list(examples.values());tasks.extend(match(example_rows[i:i+3]) for i in [0,3,6])
    if len(pack['tasks'])==10:tasks.append(match(example_rows[9:12]))
    glosses=[(g['hanzi'],g['meaning']) for t in [pack['dialogue'],pack['reading'],*pack['extraReadings']] for g in t.get('glosses',[])]
    glosses += [('剪刀','scissors'),('瓶盖','bottle cap'),('淋','get wet in rain'),('泥','mud'),('晒','air or dry in the sun'),('口袋','pocket'),('衣架','clothes hanger'),('拦','stop; block'),('抱','carry in one’s arms'),('盖','cover'),('支付','make a payment'),('保温','keep warm; insulate'),('材料','material'),('特色','distinctive feature'),('点歌','request a song'),('站台','platform'),('播','broadcast'),('市民','city residents'),('吸引','attract'),('销往','sell to a destination'),('鼓掌','applaud'),('纸巾','tissues'),('重播','rebroadcast'),('辣椒','chilli'),('砍','cut down'),('屋顶','roof'),('休假','take leave'),('经营','operate a business'),('合同','contract'),('碰倒','knock over'),('故障','fault'),('插队','jump a queue'),('钟','clock'),('演','perform; portray'),('充满','be full of'),('笑意','a hint of a smile'),('嗓子','throat; voice'),('袖子','sleeve'),('窗口','window opening'),('缴','pay'),('嘴','mouth'),('装','fill; pack'),('拍','film or photograph'),('陌生','unfamiliar'),('顿','meal classifier'),('排队','queue'),('围','surround'),('预订','reserve'),('毛巾','towel'),('圈','lap; round'),('收拾','tidy up'),('砸','smash'),('挤','squeeze; crowded'),('盖好','cover properly'),('锅','cooking pot'),('空手','empty-handed')]
    glosses += [('拆','open; take apart'),('卧室','bedroom'),('挪','move something a short distance'),('踩','step on'),('软','soft'),('钥匙','key'),('唯一','only; sole'),('遇到','encounter'),('建筑','architecture; building'),('视频','video'),('产品','product'),('蔬菜','vegetables'),('弹琴','play an instrument'),('肯','be willing'),('申请','application'),('窗户','window'),('嘛','conversational explanatory particle'),('吓了一跳','be startled')]
    spec=dict(dialogue=(rows(d),dqs),reading=(rows(r),rqs),media=(rows(m),[]),examples=examples,contexts=contexts,tasks=tasks,glosses=list(dict.fromkeys(glosses)),
        usage=[('Ask for a concrete check',REPLIES[number][0][0],REPLIES[number][0][1],'Keep the request tied to what the other person can do now.')],
        turns=[(z,e,'Respond to the immediate practical question',[c[0]]) for z,e,c in REPLIES[number]],
        review='Earlier HSK 3 naturalness correction: delivery and a wet bag; two friends catching up on a show; noodles with chilli served separately; friends admitting date mistakes. Corrected quilt/chair continuity: trousers move to the other chair, the old quilt joins them, and both are removed before the seat is free. Formal vocabulary uses independent contexts rather than speech that sounds like a report. Replaced abstract caution and assessment-policy dialogue. All target words get two independently authored contexts, and old word/task/unit IDs remain intact. Native flags: colloquial passive 叫, 具有 with formal collocations, 广大 in public notices, the playful eating invitation, 活 as vivid portrayal and 乐 lè as laughter. All distractors and true/false keys were checked against the rewritten facts.')
    repair(number,spec,publish='--publish' in sys.argv)

# These two later readings used a glyph met only incidentally in the old scene.
# Give its actual meaning at that use; leave all their lines and IDs untouched.
for number in [25,27]:
    path=ROOT/f'content/packs/s3-u{number:02}.json'
    pack=json.loads(path.read_text('utf-8'))
    text=pack['reading']
    if any('与' in l['zh'] for l in text['lines']) and not any(g['hanzi']=='与' for g in text.get('glosses',[])):
        text.setdefault('glosses',[]).append(dict(hanzi='与',pinyin=py('与'),meaning='with; and, in a written register'))
    destination=ROOT/('content/packs' if '--publish' in sys.argv else 'output/parity-editorial-drafts')/path.name
    destination.write_text(json.dumps(pack,ensure_ascii=False,indent=2)+'\n','utf-8')

path=ROOT/'content/packs/s4-u05.json'
pack=json.loads(path.read_text('utf-8'))
text=pack['reading']
if any('单独' in l['zh'] for l in text['lines']) and not any(g['hanzi']=='单独' for g in text.get('glosses',[])):
    text.setdefault('glosses',[]).append(dict(hanzi='单独',pinyin=py('单独'),meaning='on its own; individually'))
destination=ROOT/('content/packs' if '--publish' in sys.argv else 'output/parity-editorial-drafts')/path.name
destination.write_text(json.dumps(pack,ensure_ascii=False,indent=2)+'\n','utf-8')

for uid,terms in [('s5-u02', [('平稳','steady; stable'),('疑问','question; doubt')]),
                  ('s5-u04', [('符合','fit; accord with')]),
                  ('s5-u08', [('区域','area; zone'),('扫','scan')]),
                  ('s6-u01', [('拥有','have; possess')]),
                  ('s6-u02', [('采纳','adopt a suggestion'),('依赖','rely on')]),
                  ('s6-u03', [('款','model; style')])]:
    published=ROOT/f'content/packs/{uid}.json'
    source=published if published.exists() else ROOT/f'output/advanced-course-drafts/{uid}.json'
    pack=json.loads(source.read_text('utf-8'))
    for text in [pack['dialogue'],pack['reading'],*pack['extraReadings']]:
        for word,meaning in terms:
            if any(word in l['zh'] for l in text['lines']) and not any(g['hanzi']==word for g in text.get('glosses',[])):
                text.setdefault('glosses',[]).append(dict(hanzi=word,pinyin=py(word),meaning=meaning))
    destination=ROOT/('content/packs' if '--publish' in sys.argv else 'output/parity-editorial-drafts')/published.name
    destination.write_text(json.dumps(pack,ensure_ascii=False,indent=2)+'\n','utf-8')
