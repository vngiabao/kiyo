"""Repair a fast informal exchange through context, ellipsis and speaker intent."""
import sys
import common
from advanced_core import write,rows,words,q,card,practice
common.dictionary.update({'待会儿':'dāi huìr'})
V=words('''
待会儿|in a little while|lát nữa|我待会儿到，你们先进去。|I'll arrive shortly;go in first.|待会儿再回你消息。|I'll reply in a little while.
很难说|hard to say|khó nói|这场什么时候散，很难说。|It's hard to say when this show will finish.|他今晚能不能来，很难说。|It's hard to say whether he can come tonight.
说实话|to be honest|thật lòng|说实话，我刚才没听清。|Honestly,I didn't catch that.|说实话，结尾有一点难。|Honestly,the ending is a little difficult.
算了|never mind; let it go|thôi|买不到就算了，我们先进去。|If we can't get it,never mind;let's go in.|这件事先算了，下次再问。|Let this go for now;ask next time.
只管|just go ahead and|cứ|你只管先坐下，我去拿水。|Go ahead and sit;I'll get water.|有问题你只管问。|Just ask if you have questions.
只顾|be preoccupied with|chỉ lo|我只顾看路，没听见后半句。|I was concentrating on the route and missed the second half.|她只顾找卡，忘了拿包。|She was so busy finding her card she forgot her bag.
只得|have no choice but|đành|那班车已经走了，我只得等下一班。|That bus has left,so I have to wait for the next.|雨太大，只得先留下。|The heavy rain leaves us no choice but to stay for now.
再说|discuss later; besides|để sau; hơn nữa|先看完，结尾出去再说。|Finish watching;discuss the ending outside.|再说，你也还没吃饭。|Besides,you haven't eaten yet.
就是说|that is to say|tức là|就是说，你会来，只是晚一点。|So you'll come,just a little later.|就是说，先别替我点？|So don't order for me yet?
不再|no longer|không còn|他不再等上一班车了。|He's no longer waiting for the previous bus.|她不再用那张旧节目单。|She no longer uses that old programme.
前来|come to a place|đến|她前来取票，没留下看演出。|She came to collect tickets without staying for the show.|他前来问活动时间。|He came to ask the event time.
路过|pass by|đi ngang|我路过门口，听到你说算了。|I passed the entrance and heard you say never mind.|她路过车站时给我发消息。|She messaged while passing the station.
挨着|next to|sát bên|我坐在挨着门的位置。|I sit beside the door.|那张椅子挨着窗。|That chair is next to the window.
沿着|along|dọc|沿着小路走到红门。|Follow the path to the red door.|他们沿着河边走。|They walk along the riverbank.
前方|ahead|phía trước|前方那辆不是我们等的车。|The bus ahead isn't the one we're waiting for.|前方有一家还开着的店。|There's a shop still open ahead.
通道|passage|lối đi|别站在通道里等消息。|Don't wait for messages in the passage.|这条通道通向小厅。|This passage leads to the small room.
响声|sound; noise|âm thanh|响声把后半句盖住了。|The noise drowned out the second half.|楼上传来搬桌子的响声。|The noise of moving a table came from upstairs.
笑声|laughter|tiếng cười|笑声过后她又补了一句。|After the laughter,she added another sentence.|门外有一阵笑声。|Laughter came from outside.
音量|volume|âm lượng|音量太大，我没听清。|The volume was too loud for me to catch it.|把音量调小一点。|Turn the volume down a little.
通话|have a phone call|gọi điện|这里太吵，不便通话。|It's too noisy here for a call.|她通话结束后才进来。|She came in after finishing her call.
留言|leave a message|nhắn|先留言，我出去再听。|Leave a message;I'll listen outside.|他留言说改到门口见。|He left a message changing the meeting to the entrance.
回应|respond|đáp|她回应说不是不去。|She replied that it wasn't a refusal to go.|他回应了关于票的问题。|He answered the ticket question.
打断|interrupt|ngắt|我打断一下，你刚才说先别等？|Let me interrupt—did you say don't wait for now?|电话打断了那句话。|The call interrupted the sentence.
区分|distinguish|phân biệt|把先别等和不会来区分开。|Distinguish don't wait for now from won't come.|这两种语气要区分。|Distinguish these two tones.
此处|here|tại đây|此处不能停留，请到门外等。|No waiting here;please wait outside.|此处是活动入口。|This is the event entrance.
当天|on that day|hôm đó|当天我们在红门见，不在车站。|That day we met at the red door,not the station.|当天的节目临时调整了。|That day's programme changed at short notice.
此前|before this|trước đó|此前我以为她不来了。|Before this,I thought she wasn't coming.|此前一直在小厅见面。|Before this,we always met in the small room.
事后|afterwards|sau đó|事后重听，才听出不是不去。|Listening again afterwards,I caught wasn't refusing to go.|她事后才知道时间改了。|Only afterwards did she learn the time changed.
传出|come from; spread|truyền ra|小厅里传出音乐声。|Music came from the small room.|消息从群里传出去了。|The news spread beyond the group.
忽略|overlook|bỏ qua|我忽略了那个先字。|I overlooked the word for now.|别忽略最后一句。|Don't overlook the final sentence.
很|very; strongly|rất|这次我很想去，只是要晚到。|I really want to go this time;I'll just arrive late.|我很喜欢这个结尾。|I like this ending very much.
能否|whether possible|liệu có thể|我想问能否晚一点进场。|I'd like to ask whether I can enter later.|能否留座位，先问工作人员。|Ask staff whether saving a seat is possible.
''')
D=rows('''
你在哪？我这边散了。|Where are you?Mine has finished.
车还没到。先别等我，你们进去。|The bus hasn't come.Don't wait for me now;go in.
不去了？|Not coming?
不是不去，晚点到。|Not refusing to go—I'll get there later.
我刚才只听见别等。|I only caught don't wait.
门口太吵了吧。|It's noisy by the door,isn't it?
对。那先给你点？|Yes.Shall we order for you first?
先别点，我可能路上吃一点。|Don't order yet;I might eat on the way.
这回听清了，先别点。|Got it this time—don't order yet.
你别连水也不给我啊。|Don't deny me water too.
水可以。你到红门发消息。|Water's fine.Message at the red door.
哪个红门？上次那家？|Which red door?Last time's place?
不是，挨着电影院的小店。|No,the small shop next to the cinema.
哦，我上次走错过。|Oh,I went the wrong way last time.
沿着小路，不用过桥。|Follow the path.No need to cross the bridge.
知道了，等会儿到。|Got it.I'll get there shortly.
等会儿到底多久？|How soon is shortly?
车刚到，十分钟左右。|Bus just arrived.Around ten minutes.
行，我进去坐，不站通道里了。|Okay.I'll sit inside,not stand in the passage.
只管进去，我不是让你守红门。|Go in.I wasn't asking you to guard the red door.
你一会儿一个不是，我得听全。|You keep correcting things.I need to hear the whole sentence.
慢点说给你听，别替我把后半句删了。|I'll say it slower.Don't delete the second half for me.
好，来得及的话，结尾也给你讲。|Okay.If there's time,I'll tell you the ending too.
结尾先别讲！这句你可听清。|Don't tell the ending yet!Make sure you catch that one.
''')
M=rows('''
这结尾不是不好，是我没听懂。|It's not that the ending's bad—I didn't understand it.
我还以为你说不好。|I thought you said it was bad.
后半句呢？|What about the second half?
被门外的声音盖住了。|Noise outside drowned it out.
那先问我，不用替我写影评。|Then ask me first;don't write my review for me.
你再说一遍？|Could you say it again?
不是不好，是我没听懂。|Not bad—I didn't understand it.
现在听全了。|Now I've heard it all.
想听我哪里没懂吗？|Want to hear what I didn't understand?
想，但先去安静一点的地方。|Yes,but somewhere quieter first.
这句你倒听得挺快。|You caught that one quickly.
因为我也想听清。|Because I want to hear properly too.
''')
R=rows('''
演出散场，我站在门边给林安打电话。她那边像有车经过，后面几个人又一边走一边笑。我问她在哪，她说车还没到，先别等我，你们进去。我只抓住别等两个字，马上问不去了。她回答不是不去，晚点到，这回我听清，才知道自己把临时安排听成最后决定。门外的声音没有变小，可我开始知道需要补听的是哪一段，不是随便猜一个跟前两个字接得上的结局。|After the show,I called Lin An near the door.Noise on both sides masked her.She said the bus hadn't arrived and not to wait for now.I caught don't wait and asked whether she wasn't coming.Her full correction—coming later—showed I'd turned a temporary arrangement into a final decision.The noise stayed,but I knew which part to ask for rather than invent a continuation.
我们约的地方换过一次，上回在桥那边，这次是挨着电影院的红门小店。我习惯说到红门见，以为颜色已经够明确；她问哪一个，我才想到附近还有另一家红门。刚才的消息里没写店名，不能怪她记得上次。于是我补了一句沿着小路走，不用过桥，还拍了一张门口照片。照片只给她认位置，我没有让她边走边低头找每个字，她可以到电影院旁停下来再看。|The meeting place had changed from beyond the bridge to a red-door shop next to the cinema.I thought the colour was enough,but another red door existed.My message lacked the shop name,so her old memory was reasonable.I added path directions,no bridge,and a photo for recognition.She could stop beside the cinema to inspect it rather than read while walking.
进店以后我又问要不要替她点吃的。她说先别点，路上可能吃一点。我这次把先字也重复了一遍，问那到了以后再点，她说对，水可以先拿。不是要把每句话都检查成一个题目，而是刚才已经听错，确认一下具体要做什么，能省掉后来一份她吃不下的饭。陈宇在旁边笑我终于知道不是不去不等于不吃，我说我今天先学会别替别人决定就行。|Inside,I asked about ordering.She said not yet,as she might eat en route.I repeated for now and confirmed ordering after arrival;water could come first.I wasn't turning every sentence into a quiz.A concrete check after a mistake avoided unwanted food.Chen Yu teased me about my pile of negatives.I said learning not to decide for others was enough for today.
她上车后发语音，说十分钟左右到，后面还有一句别站通道里等。我当时正在找座位，耳机里只听到十分钟，就把手机放下了。过一会儿想到外面有人进出，重听一次才听见后半句。她到时我已经坐好，给她指旁边的位置。她问你没真守着门吧，我说没有，现在也不需要让大家绕过我走。她笑得很大声，服务员看过来，我们就把声音放低，先让她喝水。|On the bus,she said around ten minutes and not to wait in the passage.While finding a seat,I initially caught only the time.A replay supplied the rest.I was seated when she arrived,and pointed to a place.She joked whether I'd guarded the door.I said people no longer needed to go round me.We lowered our laughter when a server looked over and let her drink.
聊演出时，她说另一场结尾不是不好，是她没听懂。我差点又只接不好，说那就别推荐了，想到刚才的电话，先问她后面说什么。原来她想知道主角为什么把信留下，不是在给整部作品一个坏评价。我们把节目单拿出来看人物名字，又分清信是谁写、谁最后拿到。我没有装成每一处都看懂，自己也不知道的一段就跟她一起留着，下次见那个朋友时再问。|About another show,she said the ending wasn't bad;she hadn't understood it.I nearly responded only to bad,but asked for the continuation.She wanted to know why the lead left the letter,not condemn the whole work.We checked names and who wrote and received it.I didn't pretend complete understanding;we saved our shared question for another friend next time.
还有一处我们把人物说串了。她一直说她把信留下，我以为是坐在窗边的姐姐，可她指的是刚回家的妹妹。两个人在不同场景里都穿同一件外套，借来借去，节目单上的名字又小。我问是哪一位，她用妹妹回家那场来说明，比只重复一个她字清楚。后来再讲剧情，我们先说一次妹妹，再接她，不必每一句都念全名，也不让同一件衣服替我们认人。|We had also mixed up the characters. Her repeated she meant the returning younger sister,not the sister by the window. They shared a coat across scenes. Asking which scene clarified the referent better than another she. We named the younger sister once before using pronouns,without making every sentence a full name or using clothing as identity.
回家路上，我把几条语音重新听了一遍。平时听得慢，能认出的词不少，可朋友说得快时，先、只是、不是这些很短的部分常在笑声里过去。今天没有突然变成什么都听得懂，只是更愿意说刚才后半句没听清，也会把听到的安排复述一下。她最后一条说下次先把店名写上，我回好。这次连红门都没有替我们决定去哪里，得由我们把地点说完整。|On the way home,I replayed the messages.Words I recognised slowly still passed in laughter during fast speech,especially small terms marking scope.I hadn't suddenly understood everything;I was more willing to ask for a missed second half and repeat the plan.Her final message asked for the shop name next time.I agreed.The red door couldn't decide our destination—we needed to say it fully.
''')
P=rows('''
我今天的演出比陈宇他们那场晚结束一点，赶到车站，等的那班车还没来。群里问要不要继续等，我先发一句你们进去，别站门口，以为把大家放开就够了。电话接通以后，他问是不是不来了，我才发现没有说清我自己还会去。于是我补一句不是不去，只是车还没到。我不想他们为了我吹风，也不想自己被提前从见面名单里划掉，这两件事原本可以一起说明。|My show ended later,and the bus hadn't come.I told the group to go in without clearly saying I'd still arrive.When asked whether I wasn't coming,I corrected it.I wanted them out of the wind without removing myself from the gathering;both points could have been stated together.
车站有人说话，电话那头又有散场的响声，我们两边都不太听得清。我发文字，把晚点到写出来，等上车才补大约十分钟。刚才说待会儿的时候，我还没知道车什么时候来，不能因为朋友问多久就装作自己能确定。看见车到了，才有新的依据说大约时间。这个大约也不是车一定一路不停车的承诺，只是让他们知道我已经在往那边走，不用一直站门口等。|Both ends were noisy.I texted coming later,then estimated ten minutes once on the bus.Before arrival I couldn't specify shortly merely because asked.The bus gave a new basis for an estimate,not a promise of an uninterrupted journey.It let them know I was on my way and they needn't stand at the door.
关于吃饭，我说先别替我点，怕自己路上吃过，到了又留下一大份。我没有说这辈子不吃他们推荐的东西，也没有让大家都陪我不吃。可是这种省掉主语的短句，听起来很容易只留下别点两个字。朋友问是不是到了再看，我说对，顺便要他给我拿水。我能听出他这回在认真确认，虽然重复了一点，也比到了以后对着两份饭互相问谁让你点的舒服。|I asked them not to order for me yet,to avoid another meal if I ate en route.I wasn't rejecting their food forever or asking everyone to wait without eating.Short subjectless requests can sound like bare don't order.His check about deciding on arrival was welcome;water was fine.A little repetition beat two unwanted meals and blame later.
下车后我沿着小路走，差点又往桥上去。上次的路太熟，看到红门这两个字就想当然。朋友的照片让我停下来，看清电影院旁边的小店。店门口有几个人等座位，我没有站进通道里，发了到了再进去。进去时大家已经坐好，旁边空着一把椅子，没有人端着手机守门。我想这就是刚才那几条消息想要的结果：他们可以先舒服地坐，我也能找到地方，不必把等我变成一种特别隆重的仪式。|The familiar old route nearly led me over the bridge.The photo identified the cinema-side shop.I messaged arrival outside the passage before entering.They were seated with an empty chair,no one guarding the door on a phone.That was the messages' purpose:let them settle and let me find them without making waiting a grand ceremony.
喝过水我们才谈演出。我先说结尾不是不好，是我没听懂，陈宇问没听清哪句，我又笑起来，这次不是声音问题，是人物的意思没懂。两个没听懂在当时说的是不同的事，一个缺了电话里的半句话，一个听到完整句子还是不明白角色为什么这样做。我们把信的情节从头讲了一遍，发现他也漏了一场短戏。知道自己漏在哪里，问起来就比一个人说我全不懂、另一个人说你再看一遍有用。|After water we discussed the show.My not understanding the ending meant motive,not masked sound.The same expression had meant different gaps:missing half a phone sentence versus hearing words but not interpreting an action.We reconstructed the letter plot and found he'd missed a brief scene.A specific gap was more useful than total incomprehension met with watch again.
谈完以后我才知道，他以前看过前半场，没有看完后半场，我却是漏了开头。我们原来一直以为对方比自己懂得多，轮流把问题推给另一个人。现在把各自看过哪一段说出来，缺的地方就比较清楚。陈宇提议下次有时间一起看完整，再聊今天留下的信和外套。我说好，但不是约定今晚又回去看一遍，明天都还要早起。我们把下次留成待定，吃完饭就各自回家。|We then learned he had seen only the first half and I had missed the opening. Each had assumed the other knew more. Naming the scenes we had seen revealed the gaps. He proposed a full viewing together sometime. I agreed without making it a return tonight;we both needed an early start. We left the next date open and went home after eating.
我回去以后给他发消息，下一次店名和时间都写全，不只发一个红门。他回了一段故意说得很慢的语音，连店名都说了三遍。我说我听见了，你这样说，等你说完我又饿了。他发来一个笑脸，问那要不要现在再出来吃。我说明天吧，今天真的回家了。我们约好重要的变化先写一句，路上说笑还是照常。睡觉前他把明天的店名和时间发来，我回了个好，这次连地址也看完才放下手机。|After getting home I asked him to write out the shop name and time next time, instead of just sending “red door.” He replied with a deliberately slow voice message and repeated the name three times. I said I had heard him: at that speed I would be hungry again before he finished. He sent a smiling face and asked if I wanted to go back out for food. Tomorrow, I said; I really was home now. We agreed to text important changes but keep joking on the phone as usual. Before bed he sent tomorrow's shop name and time. I replied yes, this time reading the address too before putting my phone down.
''')
G=[
card('不是不…，只是…','Distinguish a limited obstacle from refusal','Double negation can reject a refusal interpretation. 只是 limits the following reason;keep the whole sentence.','不是不去，只是晚一点到。|I am coming,just arriving later.\n不是不喜欢，只是还没看懂。|I do like it;I have not understood it yet.','不是不去，表示绝对不去。','不是不去，只是晚一点到。','The phrase explicitly rejects not going.'),
card('先别…','Read temporary timing in a negative instruction','先 limits the instruction to the current step;it is not necessarily permanent.','先别替我点，到了再看。|Do not order for me yet;decide on arrival.\n结尾先别讲，我还没看。|Do not tell the ending yet;I have not watched.','先别点，表示以后永远不能点。','先别替我点，到了再看。','Retain the temporary scope.'),
card('你只管…','Invite an action without requiring a second duty','只管 can give permission or reassurance to go ahead. Interpret any added task separately.','你只管进去，我晚点到。|Go in;I will arrive later.\n有问题只管问。|Go ahead and ask questions.','只管进去，表示必须一直站在门口。','你只管进去，我晚点到。','The action invited is entering,not guarding the door.'),
card('我可没说…','Recognise an emphatic correction','可 adds emphasis in this conversational correction. Tone may be playful or serious according to context.','我可没说不去啊。|I did not say I would not go.\n我可没说每个人都得等。|I did not say everyone must wait.','我可没说不去，等于我说不去。','我可没说不去啊。','The speaker denies having made that claim.'),
card('省略主语','Recover the missing participant from context','In a shared plan,the subject or object may be omitted. Ask when the referent is unclear instead of adding an unsupported person.','先别点，我路上可能吃一点。|Do not order for me yet;I may eat en route.\n到了再发消息。|Message when you arrive.','先别点，表示全店都不许点餐。','先别点，我路上可能吃一点。','Context points to the speaker’s order,not every order.'),
card('不是…，是…','Correct evaluation versus comprehension','A contrast can distinguish a judgement of quality from a missing understanding.','不是不好，是我没听懂。|It is not bad;I did not understand.\n不是换地方，是我记错了。|The venue did not change;I remembered wrong.','不是不好，是没听懂，已经给出坏的评价。','不是不好，是我没听懂。','A comprehension gap is not a negative quality judgement.'),
]
spec=dict(title=('Hear the second half','后半句也要听见'),goals=['Recover intent from fast casual speech and ellipsis','Ask for a missing clause without pretending understanding','Separate temporary instructions,refusal and comprehension gaps'],vocabulary=V,grammar=G,
dialogue=(D,[q('gist','What does Lin An mean?','Coming later;friends should enter without waiting outside','She will never come','Everyone must refuse food'),q('detail','Which shop is intended?','The red-door shop next to the cinema,without crossing the bridge','Last time’s place beyond the bridge','The bus station'),q('inference','Why say do not tell the ending yet?','She has not watched it,not a permanent ban on discussing endings','She dislikes every film','She never wants to hear a friend')]),
reading=(R,[q('gist','What improves through the misunderstanding?','Specific requests for missed clauses and concrete plan checks','Perfect understanding of all fast speech','A decision never to call again'),q('detail','When is the ten-minute estimate given?','After the bus arrives','Before knowing any bus timing','After reaching the shop'),q('inference','Why not respond to only bad in the ending comment?','The second clause explains a comprehension gap','The friend has given a complete bad review','The friend never watched anything')]),
pairedTitle='The friend on the bus',pairedReading=(P,[q('gist','How does the second account complement the first?','It explains short requests and changing timing from the traveller’s side','It says no messages were sent','It insists all friends must stop eating'),q('detail','What is agreed for important changes next time?','Write the important change clearly while keeping ordinary banter','Stop all friendly speech','Only use a colour for venue'),q('inference','Are the two not-understanding moments identical?','No:one misses sound,the other lacks plot interpretation','Yes:both mean the film is bad','Yes:both prove a pronunciation score')]),
mediaTitle='Not bad—just not understood',media=(M,[q('detail','What has been misunderstood?','A comprehension gap as a negative review','The cinema address','The meal cost'),q('inference','What repair is suggested?','Repeat the full line somewhere quieter','Guess another ending','Pretend to understand every word')]),
glosses=[('串', 'mix up'),('辈', 'generation; a lifetime'),('末班车','last scheduled bus or train'),('主语','subject'),('省略','omit'),('后半句','second half of the sentence'),('语音','voice message'),('影评','film review'),('耳机','earphones'),('散场','a performance ends'),('隆重','grand; ceremonious'),('覆盖','cover; mask'),('盖住','drown out; cover'),('拒绝','refuse'),('误听','mishear'),('语境','context'),('补听','listen for the missed part'),('吹风','be exposed to the wind'),('端','hold; carry'),('承诺','promise'),('仪式','ceremony'),('桥','bridge'),('店名','shop name'),('剧透','spoil a plot'),('身份','identity'),('闹','noisy'),('礼','courtesy'),('熟','familiar'),('漏','miss; overlook'),('删','delete'),('推荐','recommend')],
place='A noisy cinema exit,bus stop and nearby café',context='Traveller still coming,late;friends enter first,no order for her yet,water fine. New shop next tocinema red door,path no bridge,not old bridge shop. Around10minutes only afterbusarrives. Ending not bad but not understood:plot interpretation differs from masked sound.',
turns=[('先别等我，你们进去。我是不来了吗？','Don’t wait for me now;go in.Does that mean not coming?','Recover scope',['不是，还会来，只是晚一点到。']),('不是不好，是没听懂。你听成不好了？','Not bad—didn’t understand.Did you hear bad?','Retain contrast',['后半句说明没理解，不是给坏评价。']),('红门就是上次过桥那家吧？','Red door means the old place beyond the bridge?','Confirm referent',['不是，这次挨着电影院，不用过桥。']),('待会儿就一定是十分钟？','Shortly must mean ten minutes?','Avoid an exact unsupported timing',['不一定，要看车到没到，再确认大约多久。'])],
usage=[('Ask for the missed part','刚才后半句没听清，你再说一遍？','I missed the second half;could you repeat it?','Name the gap without inventing a meaning.'),('Repeat the actionable plan','你会来，我们先进去，不替你点，对吗？','You are coming;we enter first and do not order for you yet,right?','Brief concrete readback checks the actual arrangement.'),('Keep humour while clarifying','不用慢成这样，后半句别丢就好。','Not that slowly—just keep the second half.','A clearer pace need not change Sayo’s identity or claim pronunciation grading.')],
tasks=practice([(R[0][0],R[0][1],'The traveller has permanently refused to come.',False,'She is coming later.'),(R[3][0],R[3][1],'A replay supplies the instruction about the passage.',True,'The later half was initially missed.'),(P[4][0],P[4][1],'Both comprehension gaps involve missing sound.',False,'The plot gap remains despite hearing words.'),(P[5][0],P[5][1],'The friends decide to stop ordinary banter.',False,'They keep banter and text important changes.')],
[('不是不去，只是晚到。应该怎么理解？','Not refusing to go,just late.Meaning?',['还会来，晚一些。','永远不来。','已经在店里。'],0,'Double negation rejects refusal.'),('先别点，我路上可能吃一点。能替她立刻点饭吗？','Do not order yet;may eat en route.Order immediately?',['不能，到了再确认。','能，先别等于马上。','能，已经明确要两份。'],0,'Temporary negative instruction remains in force.'),('不是不好，是我没听懂。这是明确的坏评价吗？','Not bad—I did not understand.Clear bad review?',['不是，是理解还有缺口。','是，只听不好就够。','是，没懂就说明作品一定差。'],0,'Retain the correcting clause.'),('新店挨着电影院，不用过桥。哪条路符合？','New shop beside cinema,no bridge.Whichroute?',['沿小路到电影院旁红门。','过桥去上次红门。','留在车站永远等。'],0,'Both location and no-bridge detail fit.')],
[('她回应说不是不去。','She replied that she was not refusing to go.','回应'),('别忽略最后一句。','Do not overlook the last sentence.','忽略'),('我只顾看路，没听见后半句。','I was preoccupied with the route and missed the second half.','只顾'),('有问题你只管问。','Go ahead and ask questions.','只管')],
[[(V[i][3],V[i][4]) for i in [0,1,2]],[(V[i][5],V[i][6]) for i in [4,6,8]],[(V[i][3],V[i][4]) for i in [11,14,17]],[(V[i][5],V[i][6]) for i in [20,23,26]],[(V[i][3],V[i][4]) for i in [28,29,31]]]),
review='Native review: fast-chat ellipsis,可没说 correction,delayed-order/water banter,待会儿 pronunciation and voice-paced joke. Self-review distinguishes firsttemporaryinstruction/fullcorrection,old/newred-door venues,estimateonlyafterbusarrives,and sound-vs-plot comprehension. No algorithm claims pace or pronunciation mastery. One Sayo identity retains mood variants; unverified takes follow the owner’s dated audio exception after genuine repair.')
write(6,11,spec,publish='--publish' in sys.argv)
