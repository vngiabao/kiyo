"""Targeted HSK 2 naturalness repairs; every line and answer is authored here."""
import json,sys
from common import ROOT,py
from advanced_core import rows
from editorial_repair import repair,tf,reply,fill,match

TEXTS={
4:(
'''晚上出去吃吧？我想找个安静的地方。|Want to eat out tonight? I'd like somewhere quiet.
好啊。你想吃什么？|Sure. What would you like?
今天不想吃快餐，也不想叫外卖。|I don't want fast food or delivery today.
那去我家附近那家饭馆吧，菜的味道不错。|Then let's go to the restaurant near my home. The food's good.
你去过？|Have you been?
去过，上周和小周一起去的。|Yes, with Xiao Zhou last week.
要等很久吗？|Is the wait long?
大概二十分钟。你饿了吗？|About twenty minutes. Are you hungry?
还好。我们六点出发，怎么样？|Not too hungry. Shall we leave at six?
行。坐车十分钟，再走五分钟。|Okay. Ten minutes by bus, then a five-minute walk.
到了以后，你帮我点菜吧。不要太辣。|Help me order when we get there. Nothing too spicy.
好。我们先点两个菜，不够再加。|Okay. We'll start with two dishes and order more if we need them.
''',
'''下班以后，我约陈宇出去吃饭。中午已经吃过快餐，晚上想找一家安静的饭馆，坐下来慢慢聊。|After work I asked Chen Yu to eat out. I'd already had fast food at lunch and wanted a quiet restaurant where we could sit and chat.
陈宇说他家附近有一家，菜的味道不错。他上周和小周去过，不过那天等了二十分钟才有座位。|He knew one near his home with good food. He and Xiao Zhou had gone the previous week, though they'd waited twenty minutes for seats.
我们六点出发，坐车十分钟，再走五分钟。进门时前面还有两位顾客，服务员请我们在门边等一会儿。|We left at six, rode the bus for ten minutes and walked another five. Two customers were ahead of us; a server asked us to wait by the entrance.
这次只等了十分钟。坐下以后，陈宇先问我想吃什么。我不太能吃辣，就选了一个鸡蛋菜和一个青菜。|This time the wait was only ten minutes. Once seated, Chen Yu asked what I'd like. I can't eat very spicy food, so I chose an egg dish and a vegetable dish.
菜来得很快，我对味道很满意。陈宇说上周也好吃，就是那次等得久，他有点不满。|The food came quickly and I liked it very much. Chen Yu said last week's food was good too; he'd just been a little unhappy about the long wait.
吃完我们走回车站，他问下次还来不来。我说来啊，不过午餐别再叫我吃快餐了，今天想换换。|After dinner we walked back to the stop. Would I come again? Yes, I said, but please don't invite me for fast food at lunch again. I wanted a change today.
''',
'''两个菜够吗？|Are two dishes enough?
先吃吧，不够再点。|Let's eat first. We can order more.
你说不辣，这个真的不辣？|You said it wasn't spicy. Really?
真的。你先尝一口。|Really. Try a bite.
那我信你一次。|I'll trust you this once.
一口就知道了，不用想这么久。|One bite will tell you. No need to think so long.
'''),
7:(
'''晚上见面，你穿什么？|What are you wearing for tonight's meet-up?
还没想好。蓝色的还是绿色的？|I haven't decided. Blue or green?
晚上有点凉，蓝色那件长一点吧？|It'll be cool tonight. Isn't the blue one longer?
对。绿色的又轻又短，我带蓝色的。|Yes. The green one's light and short. I'll bring the blue one.
那里面穿什么？|What will you wear underneath?
白色的。黄色那件还没干。|White. The yellow one hasn't dried yet.
鞋呢？我们还要走一会儿。|What about shoes? We'll be walking for a while.
黑色的，走路舒服。还有朋友送的红色围巾。|Black ones. They're comfortable. And the red scarf my friend gave me.
好啊。到时候我也戴红色的。|Nice. I'll wear my red one too.
你也有？那照片里可能认错我们。|You have one too? People might mix us up in photos.
认鞋就行，我的是白色的。|Just look at the shoes. Mine are white.
行，晚上见。|Okay. See you tonight.
''',
'''晚上我和陈宇约好见朋友。出门前他问我穿什么，说晚上有点凉，让我带一件长一点的衣服。|Chen Yu and I planned to meet friends tonight. Before leaving he asked what I planned to wear, said it would be cool and suggested a longer layer.
绿色那件又轻又短，蓝色的长一点。我把蓝色的放进包里，里面穿白色的。黄色那件还没干，只好留在家里。|The green one was light and short; the blue one was longer. I packed the blue one and wore white underneath. The yellow one hadn't dried, so it stayed home.
我穿黑色的鞋，也戴上朋友送的红色围巾。这双鞋虽然普通，走远路却很舒服，今天正好用得上。|I wore black shoes and the red scarf a friend had given me. The shoes were ordinary but comfortable for long walks, just right for today.
到车站时，我先看到一条红色围巾，走近才发现是陈宇。他的鞋是白色的，还真的和我们说好的一样。|At the stop I first saw a red scarf; closer up, I realised it was Chen Yu. His shoes were white, just as we'd said.
朋友给我们拍照片，笑着说两条围巾的样子很可爱。陈宇问我是不是故意和他穿一样，我说是他先说也戴红色的。|A friend took a photo and laughed that the two scarves looked cute. Chen Yu asked if I'd deliberately matched him. I said he'd been the one to choose red too.
回家时风有点大，我从包里拿出蓝色的衣服。陈宇说幸好带了，我说对，还好它不重。|It was windy on the way home, so I took out the blue layer. Chen Yu said it was lucky I'd brought it. Yes, I said, and luckily it wasn't heavy.
''',
'''照片里两条红围巾，哪条是你的？|Two red scarves in the photo. Which is yours?
看鞋，黑的是我的。|Look at the shoes. The black ones are mine.
你站我旁边，鞋看不到。|You're standing next to me. We can't see the shoes.
那看包，我的包在右边。|Then look at the bags. Mine's on the right.
看到了。这张拍得挺好。|Found it. This photo came out nicely.
发给我吧，我也想留着。|Send it to me. I'd like to keep it too.
'''),
23:(
'''下午能帮我打印两页材料吗？|Could you print two pages for me this afternoon?
可以，哪两页？|Sure. Which pages?
第二页和第三页。我发给你。|Pages two and three. I'll send them.
好。我两点去办公室，那时候开门。|Okay. I'll go to the office at two, when it opens.
里面的计算机能用吗？|Can we use the computer inside?
能，打印机也能用。拿到以后我给你送过来。|Yes, and the printer. I'll bring the pages to you afterwards.
谢谢！我在教室，三点才下课。|Thanks! I'm in class until three.
那三点教室门口见。|Then let's meet outside the classroom at three.
还有星期六那个活动，你去吗？|Are you going to that event on Saturday too?
我想去，不过上午有事。活动几点开始？|I'd like to, but I'm busy in the morning. What time does it start?
下午两点。先别报名，我问问还有没有位子。|Two in the afternoon. Don't sign up yet; I'll ask if there are places left.
好，你问到了再告诉我。|Okay. Let me know when you hear back.
''',
'''今天陈宇请我帮忙打印材料，他只要第二页和第三页。我先把文件存好，下午两点去办公室。|Chen Yu asked me to print some material today, just pages two and three. I saved the file and went to the office at two.
办公室刚开门，教师正在里面整理东西。我问能不能用计算机，她指给我看，还告诉我纸放在哪里。|The office had just opened. A teacher was tidying up inside. I asked to use the computer; she showed me it and where the paper was.
我打印完检查了一下，页数对了，字也很清楚。陈宇还在上课，我没有进去打断他，先在校园里走了一会儿。|After printing I checked: the pages were right and the text clear. Chen Yu was still in class, so I walked around campus rather than interrupt him.
三点我们在教室门口见面。他拿到材料，打开看了看，说正好可以用，谢谢我跑一趟。|We met outside the classroom at three. He looked through the pages and said they were just what he needed. He thanked me for the trip.
他还问了星期六的活动，工作人员说还有位子。活动下午两点开始，我上午的事情来得及做完，就说一起去吧。|He'd asked about Saturday's event too; the staff said there were places left. It started at two, leaving me time to finish my morning plans, so I said let's go together.
回家路上，他把报名的消息发来。我看见两个人的名字都在，回复他说周六见，材料也别忘了带。|On my way home he sent the registration message. Both our names were there. I replied: see you Saturday, and don't forget the materials.
''',
'''拿到两页了吗？|Did you get the two pages?
拿到了，第二页和第三页。|Yes, pages two and three.
很好，今天没打印错。|Great. No wrong pages today.
你上次发的是整本书。|Last time you sent me the whole book.
这次进步了吧？|I'm improving, right?
是，文件小多了。|Yes. The file's much smaller.
'''),
25:(
'''我刚才讲得太大声了吗？|Was I speaking too loudly just now?
有一点，旁边还在上课。|A little. There's still a class next door.
那我把门关上，小声一点。|Then I'll close the door and speak more quietly.
谢谢。这个包是谁的？小周想坐这儿。|Thanks. Whose bag is this? Xiao Zhou would like to sit here.
我的。我拿开，你让她进来吧。|Mine. I'll move it. Ask her in.
好。你刚才讲到哪儿了？|Okay. Where were you up to?
说周六去河边。先让我说完，行吗？|The Saturday trip to the river. Can I finish first?
行，你说，我听着。|Sure. Go on, I'm listening.
我们先在车站见，再一起走过去。|Let's meet at the stop and walk over together.
挺好。几点见？|Sounds good. What time?
三点吧。到时候我发消息。|Three. I'll message you then.
好，三点见。|Okay. See you at three.
''',
'''今天我们在活动室商量周六去哪儿。我一高兴，说话就大声了。陈宇轻轻提醒我，旁边还在上课。|Today we were deciding where to go on Saturday in the activity room. I got excited and spoke loudly. Chen Yu quietly reminded me there was a class next door.
我把门关上，也小声了一点。小周刚来，想坐在我们旁边，可是我的包占了座位。我赶紧拿开，让她坐下。|I closed the door and lowered my voice. Xiao Zhou had just arrived and wanted to sit with us, but my bag was on the seat. I quickly moved it for her.
我提议去河边，陈宇还没听完就问几点出发。我笑着让他等一下，先把要走的路讲完，再一起定时间。|I suggested the riverside. Before I'd finished, Chen Yu asked when we'd leave. Laughing, I asked him to wait while I explained the route, then we'd decide the time together.
我们最后约了三点在车站见。小周说这个时间不错，她上午还有事情，下午正好能够出来。|We agreed to meet at the stop at three. That suited Xiao Zhou: she was busy in the morning but could come out that afternoon.
活动室的钟响了，我以为设备出了问题。陈宇说那是正常的报时声音，已经四点，该回家了。|The activity-room clock chimed. I thought something was wrong with the equipment. Chen Yu said it was the normal chime: four o'clock, time to go home.
出门前我又看了一眼椅子，包已经拿走了。陈宇说周六别把包忘在车站，我说不会，到时里面还要装水呢。|Before leaving I checked the chair; I'd taken the bag. Chen Yu told me not to leave it at the stop on Saturday. I wouldn't, I said; I'd need it for the water.
''',
'''你又说大声了。|You're getting loud again.
知道了。这个消息太好了。|I know. It's such good news.
好消息小声说也一样好。|It's still good news said quietly.
那你靠近一点，我小声告诉你。|Come closer, then. I'll tell you quietly.
我就在旁边，你说吧。|I'm right here. Go ahead.
周六小周也能来。|Xiao Zhou can come on Saturday too.
''')}

# Each word keeps its existing first example unless it needed a specific fix.
# The second examples below are independent situations, not dialogue padding.
SECOND={
4:'''为什么|你为什么笑？我说错了吗？|Why are you laughing? Did I say something wrong?
安静|孩子睡着了，屋里很安静。|The child is asleep. The room is quiet.
怎样|这张表怎样填？|How do I fill in this form?
多久|你在北京住了多久？|How long have you lived in Beijing?
什么样|她喜欢什么样的电影？|What kind of films does she like?
认为|我认为这本书值得再读一次。|I think this book is worth reading again.
看法|看完电影，我们聊了聊各自的看法。|After the film we talked about what each of us thought.
原因|他迟到的原因是坐错了车。|He was late because he took the wrong bus.
好处|住得近的好处是可以走路上班。|The advantage of living nearby is being able to walk to work.
坏处|睡得太晚有什么坏处？|What are the drawbacks of going to bed too late?
味道|这杯茶的味道和昨天的不一样。|This tea tastes different from yesterday's.
饭馆|车站对面新开了一家饭馆。|A new restaurant has opened opposite the station.
快餐|楼下的快餐店十二点人最多。|The fast-food place downstairs is busiest at noon.
外卖|雨太大了，我们叫外卖吧。|It's raining hard. Let's order delivery.
方便面|家里还有两包方便面。|There are still two packets of instant noodles at home.
服务|这家旅馆的服务很好。|The service at this hotel is very good.
顾客|店里只有一位顾客。|There's only one customer in the shop.
满意|照片拍得很好，我很满意。|The photo came out well. I'm very happy with it.
不满|她对这个安排不满，想换个时间。|She's unhappy with this arrangement and wants a different time.
比如|周末可以做很多事，比如看书、散步。|There's plenty to do at weekends, like reading or walking.
不同|我们住在不同的城市。|We live in different cities.
座位|窗边还有一个座位。|There's another seat by the window.
''',
7:'''黑|天已经黑了，我们回去吧。|It's dark now. Let's go back.
黑色|黑色的包是我的。|The black bag is mine.
红|她的脸一下子红了。|Her face suddenly went red.
红色|我用红色的笔写了日期。|I wrote the date with a red pen.
蓝|今天的天很蓝，一朵云也没有。|The sky is blue today, without a single cloud.
蓝色|请把蓝色的杯子给我。|Please pass me the blue cup.
绿|春天一到，树就绿了。|The trees turn green when spring comes.
绿色|绿色的门旁边有一家小店。|There's a little shop beside the green door.
黄|这片叶子已经黄了。|This leaf has already turned yellow.
黄色|那辆黄色的车停在路边。|That yellow car is parked by the road.
可爱|她家的小猫真可爱。|Her kitten is so cute.
普通|我只要一个普通杯子，不用大的。|I just want an ordinary cup, not a big one.
特别|今天是他的生日，想做一点特别的菜。|It's his birthday today. I'd like to cook something special.
轻|这个包很轻，里面只有一本书。|This bag is light; there's only one book inside.
短|这支笔太短了，不好拿。|This pen is too short to hold easily.
低|桌子太低，我坐着不舒服。|The table is too low. It's uncomfortable to sit here.
鞋|进门先把鞋换了吧。|Change your shoes before coming in.
样子|你小时候是什么样子？|What did you look like as a child?
白色|白色的碗里是米饭。|The white bowl contains rice.
开心|收到你的消息，我很开心。|I was happy to hear from you.
颜色|这两个包的颜色不一样。|These bags are different colours.
凉|茶已经凉了，我再给你倒一杯。|The tea's gone cold. I'll pour you another cup.
''',
23:'''为|谢谢你为我们准备晚饭。|Thank you for making dinner for us.
加油|她跑过来的时候，我们一起喊加油。|We cheered her on as she ran towards us.
求|求你了，别再逗我笑了。|Please, stop making me laugh.
取|我去车站取票，你在门口等我。|I'll collect the tickets at the station. Wait at the entrance.
取得|这次比赛，他取得了第一名。|He came first in this competition.
拿到|我拿到新书就给你看。|I'll show you the new book as soon as I get it.
借|你的笔能借我一下吗？|Can I borrow your pen for a moment?
打印|这张照片可以打印出来吗？|Can this photo be printed?
计算机|这台计算机用了五年了。|This computer has been used for five years.
办公室|她的办公室在二楼。|Her office is on the second floor.
教师|她是一位音乐教师。|She's a music teacher.
教室|教室里有三十张桌子。|There are thirty desks in the classroom.
教学|这位老师有十年的教学经验。|This teacher has ten years of teaching experience.
教育|他们在讨论音乐教育。|They're discussing music education.
讲|再讲一次吧，我刚才没听清。|Say it again, please. I didn't hear clearly just now.
讲话|他讲话的时候有点紧张。|He's a little nervous when speaking.
家长|家长会下午三点开始。|The parent meeting starts at three in the afternoon.
高中|高中毕业以后，她去了上海。|After finishing high school she went to Shanghai.
中小学|附近的中小学今天都放假。|The nearby primary and secondary schools are all on holiday today.
校园|春天的校园里有很多花。|There are lots of flowers on campus in spring.
校长|校长在门口迎接新学生。|The principal is greeting new students at the entrance.
级|我妹妹今年上三年级。|My younger sister is in third grade this year.
''',
25:'''虽然|虽然下雨了，我们还是出门了。|We went out despite the rain.
所以|今天很冷，所以我多带了一件衣服。|It's cold today, so I brought another layer.
那|那就明天再见吧。|Then let's meet tomorrow instead.
让|让我看看你拍的照片。|Let me see the photo you took.
占|这张桌子太大，占了半个房间。|This table is so big it takes up half the room.
站|他站在车站旁边等我。|He's standing beside the stop, waiting for me.
站住|前面有车，先站住别走。|There's a car ahead. Stop; don't move yet.
影响|昨晚没睡好，影响了今天的工作。|A poor night's sleep affected today's work.
事情|等这件事情做完，我就回家。|I'll go home when I've finished this task.
受到|这本书受到很多读者的欢迎。|This book has been welcomed by many readers.
重视|她很重视这次比赛，每天都练习。|This competition matters to her; she practises every day.
行动|救人行动已经结束。|The rescue operation has ended.
行为|他的行为让大家很感动。|His actions moved everyone.
顺利|今天一路顺利，很快就到家了。|The trip went smoothly today. I got home quickly.
正常|手机现在能正常用了。|The phone works normally now.
安全|到了家给我发消息，我想知道你安全到家。|Message me when you get home. I'd like to know you've arrived safely.
习惯|我习惯早上先喝一杯水。|I'm used to having a glass of water first thing in the morning.
不要|不要忘了带钥匙。|Don't forget your keys.
不错|这家店的茶不错。|The tea at this shop is good.
挺好|你今天看起来挺好。|You look well today.
怎么办|钥匙不见了，怎么办？|My keys are missing. What should I do?
能够|六点以前我能够做完。|I can finish before six.
'''}

OVERRIDES={
7:{'蓝':('你看，海是蓝的。','Look, the sea is blue.'),'红':('红的这件是朋友送的。','The red one was a gift from a friend.')},
23:{'教育':('她在大学学教育。','She studies education at university.'),'家长':('家长正在校门口等孩子。','Parents are waiting for their children at the school gate.'),'校长':('我们在校园里遇到了校长。','We met the principal on campus.'),'级':('他比我高一级。','He is one grade above me.'),'求':('我求他再讲一个故事。','I begged him to tell another story.')},
25:{'事情':('今天事情太多，我忘了回消息。','I had so much to do today that I forgot to reply.'),'受到':('新同学受到大家的欢迎。','Everyone welcomed the new classmate.'),'行动':('他们已经开始行动了。','They have already started taking action.'),'行为':('这种行为很危险，别学。',"That behaviour is dangerous. Don't copy it."),'安全':('这条路很安全，我们走这里吧。',"This road is safe. Let's go this way."),'挺好':('这个办法挺好，我们试试。',"This is a good idea. Let's try it.")}
}

QUESTIONS={
4:([('gist','What do the friends decide?',['Have dinner at a restaurant near Chen Yu’s home','Order delivery at home','Cook instant noodles'],0),('detail','When will they leave?',['Six','Five','Seven'],0),('inference','Why order two dishes first?',['They can add more if needed','The restaurant sells only two dishes','One friend is leaving immediately'],0)], [('gist','How does dinner go?',['They enjoy the food after a short wait','They never get seats','They eat at home instead'],0),('detail','How long do they wait this time?',['Ten minutes','Twenty minutes','Fifteen minutes'],0),('inference','Why was Chen Yu unhappy last week?',['The wait was long','The food tasted bad','The restaurant was closed'],0)]),
7:([('gist','What are they discussing?',['Clothes for meeting friends','Buying school uniforms','Changing a bus ticket'],0),('detail','Which layer will Lin An bring?',['The blue one','The green one','The undried yellow one'],0),('inference','How could they tell each other apart?',['By their shoes','Both wear the same shoes','Neither wears a scarf'],0)],[('gist','What happens on the outing?',['They meet in matching red scarves and take a photo','They cancel because clothes are wet','They buy new shoes at the stop'],0),('detail','What does Lin An take out on the way home?',['The blue layer','A yellow shirt','A green cup'],0),('inference','Why was bringing it useful?',['The wind picked up','It was needed for a uniform inspection','They lost both scarves'],0)]),
23:([('gist','What help does Chen Yu request?',['Print pages two and three','Print a whole book','Cancel a class'],0),('detail','When do they meet outside the classroom?',['Three','Two','Six'],0),('inference','Why does Chen Yu check the event before registration?',['To find out whether places remain','He wants to borrow shoes','The office has no computer'],0)],[('gist','What happens after the printing?',['They meet at three and decide to attend Saturday’s event','They enter the class to interrupt','The printer fails and the pages are lost'],0),('detail','When does Saturday’s event begin?',['Two in the afternoon','Two in the morning','Three in the afternoon'],0),('inference','Why can the narrator attend?',['The morning plans can finish in time','The event changes to Sunday','There is no registration'],0)]),
25:([('gist','What are the friends planning?',['A Saturday riverside outing','A move to another school','A printer repair'],0),('detail','When will they meet at the stop?',['Three','Four','Six'],0),('inference','Why move the bag?',['To give Xiao Zhou the seat','The clock is broken','To cancel the outing'],0)],[('gist','What is the activity-room meeting about?',['Agreeing where and when to go on Saturday','Learning to fix a clock','Registering for a new class'],0),('detail','What makes the narrator think equipment has a problem?',['The clock chimes','The door falls off','The lights go out'],0),('inference','Why does three suit Xiao Zhou?',['She is busy in the morning and free later','She must attend a class at three','She has already left town'],0)])}

REPLIES={
4:[('不要太辣，好吗？','Nothing too spicy, okay?',['好，先点两个不辣的菜。','好，多放一点辣的。','我的鞋是白的。']),('二十分钟，你能等吗？','Can you wait twenty minutes?',['能，我还不太饿。','我是星期六来的。','这条围巾是红的。'])],
7:[('黄色那件还没干。',"The yellow one hasn't dried yet.",['那穿白色的吧。','那我喝黄色的。','办公室两点开。']),('把这张照片发给我吧。','Send me this photo, please.',['好，我现在发。','好，把照片穿上。','快餐很好吃。'])],
23:[('只打印第二页和第三页。','Print just pages two and three.',['好，一共两页。','好，我打印整本书。','那我去买鞋。']),('活动还有位子吗？','Are there places left at the event?',['我问到了再告诉你。','位子是黑色的。','我要喝一杯水。'])],
25:[('这个包是谁的？小周想坐这儿。','Whose bag is this? Xiao Zhou wants to sit here.',['我的，我马上拿开。','我的，让包继续坐吧。','明天办公室开门。']),('先让我说完，行吗？','Can I finish first?',['行，你说，我听着。','行，我再问一次打断你。','这条围巾很红。'])]}

GLOSSES=[('林安','Lin An, a name'),('陈宇','Chen Yu, a name'),('小周','Xiao Zhou, a name'),('辣','spicy'),('不辣','not spicy'),('点菜','order food'),('下班','finish work'),('青菜','green vegetables'),('换换','have a change'),('上周','last week'),('服务员','server'),('叶子','leaf'),('风','wind'),('层','layer'),('围巾','scarf'),('认错','mistake one person for another'),('故意','deliberately'),('用得上','come in useful'),('幸好','luckily'),('读者','reader'),('救人','rescue people'),('迎接','welcome; meet on arrival'),('经验','experience'),('整本','the whole volume'),('整理','tidy; organise'),('文件','file'),('存好','save securely'),('打印机','printer'),('报名','register'),('工作人员','staff'),('来得及','have time to'),('活动室','activity room'),('提议','suggest'),('路线','route'),('报时','tell the time; chime'),('商量','discuss plans'),('提醒','remind'),('轻轻','gently'),('赶紧','quickly'),('感动','moved emotionally'),('危险','dangerous'),('靠近','come closer'),('逗','amuse; tease'),('值得','worth'),('各自','each separately'),('优点','advantage'),('海','sea'),('假','holiday; leave'),('放假','have a holiday'),('高中毕业','finish high school')]

GLOSSES += [('附近','nearby'),('大概','approximately'),('约','arrange to meet'),('尝','taste; try a bite'),('比较','relatively; comparatively'),('屋','room; house'),('填','fill in'),('迟到','be late'),('旅馆','hotel'),('照片','photograph'),('拍','take a photograph'),('安排','arrange; arrangement'),('城市','city'),('窗边','by the window'),('戴','wear an accessory'),('双','pair; classifier for shoes'),('虽然','although'),('却','however; unexpectedly'),('脸','face'),('笔','pen'),('朵','classifier for flowers and clouds'),('云','cloud'),('春天','spring'),('猫','cat'),('支','classifier for pens'),('倒','pour'),('留','keep; leave'),('走近','walk closer'),('发现','discover; realise'),('挺好','quite good'),('信','trust; believe'),('这么','this much; so'),('聊','chat'),('周','week'),('久','long time'),('时','when; time'),('前面','in front'),('得很','very; complement marking degree'),('得','complement particle'),('戴上','put on an accessory')]

GLOSSES += [('打断','interrupt'),('趟','classifier for trips'),('比赛','competition'),('喊','shout; call'),('讨论','discuss'),('紧张','nervous'),('遇到','meet; encounter'),('河边','riverside'),('眼','eye; glance'),('椅子','chair'),('结束','end; finish'),('钥匙','key')]

for number,(d,r,m) in TEXTS.items():
    pack=json.loads((ROOT/f'content/packs/s2-u{number:02}.json').read_text('utf-8'))
    second={w:(z,e) for w,z,e in (row.split('|') for row in SECOND[number].splitlines())}
    assert set(second)=={v['hanzi'] for v in pack['vocabulary']}
    examples={v['hanzi']:OVERRIDES.get(number,{}).get(v['hanzi'],(v['example']['zh'],v['example']['en'])) for v in pack['vocabulary']}
    contexts=[]
    for w in examples:
        assert w in examples[w][0] and w in second[w][0] and examples[w][0]!=second[w][0]
        contexts.extend([examples[w],second[w]])
    dqs,rqs=QUESTIONS[number]
    true_index={4:9,7:5,23:8,25:10}[number]
    true_statement={4:'The bus ride is ten minutes, followed by five minutes on foot.',7:'The yellow garment has not dried.',23:'They are talking about an event on Saturday.',25:'The proposed meeting time is three.'}[number]
    false_index={4:4,7:1,23:3,25:4}[number]
    false_statement={4:'Chen Yu disliked last week’s food.',7:'Lin An packs the green layer.',23:'The two friends meet at two.',25:'The clock sound means the equipment is broken.'}[number]
    tasks=[tf(*rows(d)[true_index],true_statement,True,'The heard line explicitly states this fact.'),tf(*rows(r)[false_index],false_statement,False,'The heard line explicitly gives a different fact.'),*[reply(z,e,c,0,'This reply fits the immediate request.') for z,e,c in REPLIES[number]]]
    for word in {4:['满意','服务'],7:['白色','凉'],23:['打印','取得'],25:['习惯','虽然']}[number]: tasks.append(fill(*examples[word],word))
    tasks.extend(match(list(examples.values())[i:i+3]) for i in [0,3,6])
    inherited=[(g['hanzi'],g['meaning']) for t in [pack['dialogue'],pack['reading'],*pack['extraReadings']] for g in t.get('glosses',[])]
    repair(number,dict(dialogue=(rows(d),dqs),reading=(rows(r),rqs),media=(rows(m),[]),dialogueSpeakers=['陈宇','林安'] if number in [7,23] else ['林安','陈宇'],mediaSpeakers=['陈宇','林安'] if number==7 else ['林安','陈宇'],examples=examples,contexts=contexts,tasks=tasks,glosses=list(dict.fromkeys(inherited+GLOSSES)),
        usage=[('Respond to this request',REPLIES[number][0][0],REPLIES[number][0][1],'Give the next useful detail for the actual situation.')],turns=[(z,e,'Respond to the immediate request',[c[0]]) for z,e,c in REPLIES[number]],
        review='Targeted HSK 2 naturalness review: restaurant choice with a previous twenty-minute wait versus ten minutes today; two red scarves with different shoes, blue layer packed; printing only pages two/three at two and handing them over at three, Saturday event at two; activity-room discussion with a normal four-o’clock chime and Saturday three meeting. Removed assessment, identity and consent lectures inside friendly speech. All existing word/task IDs preserved. First examples retained where suitable, specific awkward examples fixed; every word also has an independently authored second context. Abstract education, behaviour and action vocabulary stays in separate examples rather than forced conversation. False statements checked against their own audio. Native flags: 为 beneficiary register, 取得成绩/同意 versus 拿到, educational 教师/教育/教学/中小学/年级 terms, 求 playful plea, 满意/不满 and 好处/坏处, adjective 色 forms, 站住 request strength, formal 受到/行动/行为 and colloquial 挺好. Native review pending.'),publish='--publish' in sys.argv,level=2)

# 得 here is a degree-complement gloss, not the vocabulary citation dé.
for number in TEXTS:
    target=ROOT/('content/packs' if '--publish' in sys.argv else 'output/parity-editorial-drafts')/f's2-u{number:02}.json'
    pack=json.loads(target.read_text('utf-8'))
    for text in [pack['dialogue'],pack['reading'],*pack['extraReadings']]:
        for gloss in text.get('glosses',[]):
            if gloss['hanzi']=='得' and gloss['meaning']=='complement particle':
                gloss['pinyin']='de'
    target.write_text(json.dumps(pack,ensure_ascii=False,indent=2)+'\n','utf-8')

DEPENDENCIES={
    's2-u12':[('决定','decide')],
    's2-u16':[('决定','decide')],
    's2-u17':[('像','be like; resemble')],
    's2-u18':[('负责','be responsible for')],
    's2-u19':[('距离','distance')],
    's2-u20':[('公园','park'),('报名','register')],
    's2-u21':[('选择','choose; choice'),('需要','need')],
    's2-u22':[('公园','park'),('公里','kilometre'),('百米','hundred metres'),('上方','above'),('下方','below'),('身边','by one’s side')],
    's5-u02':[('传统','tradition')],
    's5-u04':[('凭','on the basis of; rely on')],
}
for uid,terms in DEPENDENCIES.items():
    path=ROOT/f'content/packs/{uid}.json'
    source=path if path.exists() else ROOT/f'output/advanced-course-drafts/{uid}.json'
    pack=json.loads(source.read_text('utf-8'))
    for text in [pack['dialogue'],pack['reading'],*pack['extraReadings']]:
        for word,meaning in terms:
            if any(word in l['zh'] for l in text['lines']) and not any(g['hanzi']==word for g in text.get('glosses',[])):
                text.setdefault('glosses',[]).append(dict(hanzi=word,pinyin=py(word),meaning=meaning))
    destination=ROOT/('content/packs' if '--publish' in sys.argv else 'output/parity-editorial-drafts')/path.name
    destination.write_text(json.dumps(pack,ensure_ascii=False,indent=2)+'\n','utf-8')
