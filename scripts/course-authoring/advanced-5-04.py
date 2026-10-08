"""Follow knowledge and timing across an original missed-meeting drama."""
import sys
from advanced_core import write,rows,words,q,card,practice
V=words('''
真相|what actually happened; truth|sự thật|真相和我开始想的完全不同。|What actually happened was completely different from my first idea.|故事没有立刻把真相告诉观众。|The story does not immediately tell the audience what happened.
线索|clue|manh mối|门上的纸是我们找到新地方的线索。|The paper on the door is a clue to finding the new venue.|我把前面的线索重新看了一遍。|I looked back over the earlier clues.
关键|key; crucial|then chốt|关键是他当时还没有看到消息。|The key is that he had not seen the message then.|这句话是理解后面反应的关键。|This sentence is key to understanding the later reaction.
分析|analyse; analysis|phân tích|先说发生了什么，再分析为什么。|First say what happened, then analyse why.|我们分析了两个人知道的内容。|We analysed what the two people knew.
逻辑|logic|logic|按这个逻辑，发过消息就等于对方看过，可这不对。|By that logic, sending a message means the other person read it, but that is wrong.|故事的逻辑要和前面的事实接上。|The story’s logic needs to connect with the earlier facts.
误解|misunderstand; misunderstanding|hiểu lầm|这个误解来自两个人知道的事情不同。|The misunderstanding comes from the two people knowing different things.|她误解了那句没说完的话。|She misunderstood the unfinished remark.
暂时|temporarily; for now|tạm thời|我们暂时在小厅等。|We are waiting in the small hall for now.|这段暂时没有告诉我们结果。|This section has not told us the result yet.
总算|finally; at last|cuối cùng|我总算找到你们了。|I finally found you all.|最后一次电话总算接通了。|The final call finally connected.
居然|unexpectedly; to one’s surprise|không ngờ|我居然在门口等了这么久。|I cannot believe I waited at the door so long.|他居然还记得两年前说过的话。|Surprisingly he still remembered something said two years earlier.
干脆|simply; decisively|dứt khoát|手机没电，干脆借一个打电话吧。|The phone is dead; let’s simply borrow one to make a call.|她干脆把问题当面问清楚。|She decided to ask directly and settle the question.
毕竟|after all|dù sao|毕竟他没有看到消息，不能说他故意不来。|After all, he did not see the message; we cannot say he deliberately stayed away.|毕竟第一次见面，我们先把地方说清楚。|After all, it is the first meeting; let’s make the location clear.
偶然|by chance; accidental|tình cờ|我偶然在门口看见那个通知。|I happened to notice the sign at the entrance.|这次偶然的相遇让他们重新联系。|This chance meeting brought them back in touch.
怀疑|suspect; doubt|nghi ngờ|我怀疑自己是不是记错了地方。|I wondered whether I had remembered the wrong place.|她怀疑那个解释，但愿意先听完。|She doubted the explanation but was willing to hear it out.
事实|fact|sự thật|事实是两个人都到了，只是不在同一个地方。|The fact is that both arrived, but at different places.|我想把事实和自己的判断分开。|I want to separate the facts from my judgment.
解释|explain; explanation|giải thích|你先解释一下为什么换了地方。|First explain why the venue changed.|这个解释还没有回答时间的问题。|This explanation has not answered the timing question.
确认|confirm|xác nhận|下次换地方，我们要确认对方收到。|Next time we change venues, let’s confirm the other person received the update.|他打电话确认门口是哪一扇门。|He called to confirm which entrance was meant.
表情|facial expression|biểu cảm|他这个表情不一定是在生气。|His expression does not necessarily mean he is angry.|我只看见表情，没听见他说什么。|I saw the expression but did not hear his words.
细节|detail|chi tiết|这个细节前面已经出现过。|This detail appeared earlier.|她补了一个我们没注意的细节。|She added a detail we had missed.
期间|during; period|trong thời gian|活动期间，你可以来小厅找我。|During the event, you can find me in the small hall.|放假期间，他们见了两次面。|They met twice during the holiday.
之前|before|trước khi|出门之前，我看过原来的地址。|Before leaving, I checked the original address.|你之前有没有告诉他换地方了？|Had you told him about the venue change before that?
之后|after|sau khi|接通电话之后，他才知道我们在小厅。|Only after the call connected did he know we were in the small hall.|比赛之后，她才解释那个动作。|Only after the competition did she explain that gesture.
判断|judge; judgment|phán đoán|只凭一个表情，很难判断他在想什么。|It is hard to judge his thoughts from one expression.|先听完，再做判断。|Listen to the end before making a judgment.
观察|observe|quan sát|我们再观察一下他后面的动作。|Let’s observe what he does afterwards.|她观察到门口的纸被风吹起来了。|She noticed the paper at the entrance blowing in the wind.
通知|notify; notice|thông báo|门口有一个换地方的通知。|There is a notice at the entrance about the venue change.|他通知了群里的人，却没有等回复。|He notified the group but did not wait for replies.
''')
D=rows('''
你总算来了，我还以为你不来了。|You finally made it. I thought you weren’t coming.
我在大门口等了半个小时。你们怎么全在这儿？|I waited at the main entrance for half an hour. Why are you all here?
大房间的灯坏了，十点零五分才决定换到小厅。|The large room’s light broke. We only decided to move to the small hall at 10:05.
你为什么没告诉我？|Why didn’t you tell me?
我发了消息，就在决定以后。你没看到？|I sent a message just after the decision. Didn’t you see it?
没看到。我十点上车，手机就没电了。|No. My phone died when I boarded at ten.
我以为你收到，也以为你会从另一边进来。|I thought you’d received it and would enter from the other side.
你以为，我还以为你忘了今天的活动呢。|You thought that, and I thought you’d forgotten today’s event.
门口不是也贴了通知吗？|Wasn’t there a notice at the entrance too?
我看见一张纸，风把它吹起来了，没看清。|I saw a sheet of paper, but the wind blew it up and I couldn’t read it.
我应该再等你回一句，不能发完就算了。|I should have waited for a reply rather than treating sending as enough.
我也应该早一点借电话，别一直在门外猜。|I should have borrowed a phone sooner rather than guessing outside.
刚才是谁的电话？我没认出号码。|Whose phone was that just now? I didn’t recognise the number.
门口那家店的老板。他说可以打一个电话。|The owner of the shop at the entrance. He said I could make a call.
幸好接了，不然你可能还在外面。|Good thing I answered. Otherwise you might still be outside.
是啊。从门口走过来才五分钟，我倒等了三十分钟。|Yes. The walk here took only five minutes, yet I waited thirty.
进来喝点水吧。我们刚摆好椅子，还没开始。|Come in and have some water. We’ve just set up the chairs and haven’t started.
下次先告诉我是哪一扇门，我今天已经把大门看够了。|Next time tell me which entrance. I’ve seen quite enough of the main one today.
''')
R=rows('''
这段短剧从林安走进小厅开始。陈宇说“你总算来了”，林安没有回答问候，先问为什么大家全在这里。只看开头，我以为林安迟到，陈宇已经等得不耐烦。可第二句提到大门口等了半个小时，刚才的判断就不够了：林安并不是没有来，他到的地方和大家不同。|The short drama begins with Lin An entering the small hall. Chen Yu says she has finally arrived; she asks why everyone is there. I first assumed lateness and impatience. Her next line about waiting half an hour at the main entrance changes that: she came, but to a different place.
陈宇解释，大房间的灯坏了，大家十点零五分才决定换到小厅。他在决定以后发了消息，以为林安会从另一边进来。镜头没有让我们看见林安的手机，所以到这里，我们只能知道陈宇发过，不能直接知道她收到了。他说“你没看到”，也是在问，并不是已经知道答案。|Chen explains that a broken light prompted the move at 10:05. He sent a message and expected Lin to use the other entrance. We have not seen her phone, so know only that he sent it, not that she received it. His question about seeing it is a question, not prior knowledge of the answer.
林安说，自己十点上车的时候，手机已经没电。这个时间比换地方早了五分钟，也比消息发出早。她出门之前看的是原来的地址，到门口时自然还在找大房间。她没有看见大家，就怀疑陈宇忘了活动。这里可以理解她为什么这样想，却不能把她的怀疑当成陈宇真的忘了。|Lin’s phone died on boarding at ten, five minutes before the venue change and message. She had checked the original address before leaving, so still looked for the large room. Seeing nobody, she suspected Chen had forgotten. We can understand the suspicion without treating it as fact.
门口的通知是第三个线索。陈宇以为贴了纸，后来到的人就能找到小厅。林安确实看见了纸，可风把纸吹起来，她没看清内容。如果我们只听“看见一张纸”，就会漏掉后半句。看见纸和读到通知不是同一件事，就像发过消息和对方看过消息也不是同一件事。|The entrance notice is a third clue. Chen expected later arrivals to find the small hall from it. Lin saw the paper, but the wind lifted it and she could not read the contents. Seeing paper differs from reading a notice, just as sending a message differs from the other person reading it.
等到十点四十分，林安向门口一家店的老板借了电话。陈宇不认识这个号码，但还是接了，这才听见她在大门口。电话接通以后，两个人知道的内容才接上。他告诉她从哪里走，她走了五分钟到了小厅。前面的等待很长，并不是因为路很远，而是因为她没有新地址。|At 10:40 Lin borrowed a shopkeeper’s phone. Chen answered an unfamiliar number and learned she was at the main entrance. Only then did their information connect. His directions brought her to the small hall in five minutes. The long wait resulted from lacking the new location, not a long walk.
后面的两句没有把责任全推给一个人。陈宇说，应该等她回复；林安说，应该早点借电话。两个人都说出了下一次能做的具体事情，没有只争谁比较粗心。这里也没有证据说明谁故意不让对方参加。把误会解释清楚，不需要再替人物加一个更复杂的坏打算。|Neither assigns all responsibility to one person. Chen says he should have waited for a reply; Lin says she should have borrowed a phone sooner. Both name concrete future actions. There is no evidence of deliberate exclusion, and no need to invent a more complicated malicious plan.
最后林安说，她今天已经把大门看够了。陈宇邀请她进来喝水，活动还没有开始。我觉得这句话有一点抱怨，也有一点开玩笑：她不想再等，可也没有直接离开。如果换一种语气读，它可能更生气。我们讨论时先保留这两种可能，再听前后的声音，而不是凭一个词替整段关系下结论。|Finally Lin jokes that she has seen enough of the main entrance. Chen invites her for water; the event has not started. Her line could combine complaint and humour: she does not want more waiting but does not leave. Different delivery could sound angrier. We retain possibilities and hear the context rather than judging the whole relationship from one word.
''')
P=rows('''
看这段短剧时，我把纸分成三栏：观众知道什么，陈宇知道什么，林安知道什么。不是每一栏都要写满。有些信息后来才出现，有些一直没有说明。这样记下来，我发现开头最容易犯的错误，是把后来听到的解释放回前面，以为人物从一开始就应该知道。|I divided my notes into what the audience, Chen and Lin knew. Not every column needed filling: some facts appeared later and others remained unspecified. The common mistake was putting a later explanation back into the beginning and assuming the characters should always have known it.
在陈宇说发了消息的时候，他知道灯坏了，也知道活动换地方。他不知道林安的手机十点已经没电，更不知道她正站在大门口。林安知道原来的地址，知道自己等了很久，却不知道小厅里的人刚摆好椅子。两个人都不是毫无原因地生气，只是各自看到的事情不完整。|When Chen mentions his message, he knows about the light and move, but not Lin’s dead phone or waiting position. Lin knows the old address and her long wait, but not that the others are just setting up chairs. Their reactions have reasons, but each has incomplete information.
观众也不是从开头就比所有人知道得多。我们先看见林安走进来，听见陈宇说“总算”，容易跟着他觉得她来晚了。等她说在门口等，又容易立刻站到她那边。我暂停了一次，问自己前一个判断有没有被后面的事实改变。陈宇忘了活动这个说法，并没有在后面得到证明。|The audience does not know everything from the start. Seeing Lin enter and hearing finally can lead us to side with Chen; hearing about her wait can reverse that. I paused to ask whether later facts changed my earlier judgment. The claim that Chen forgot the event was never confirmed.
把时间写清楚以后，事情更容易理解。十点手机没电，十点零五分换地方并发消息，十点四十分借电话，五分钟后到小厅。林安说等了半个小时，所以她到大门口是在十点十分左右，不是十点半。这个时间来自电话和等待一起计算，不是她在对话里直接报了到达时间。|A timeline helps: phone dead at ten, move and message at 10:05, borrowed call at 10:40, arrival five minutes later. A half-hour wait puts Lin at the main entrance around 10:10, not 10:30. That is an inference from the call and waiting duration, not an explicitly announced arrival time.
不过我也注意到，人物口中的“半个小时”可能是大概的时间。我们能确定她等待很久，不能因此说她一定在十点十分零秒到达。讨论故事时，计算能帮我们发现顺序，但不应该把日常说话的大概数字变成不存在的准确记录。朋友说，他以前看字幕也常把“等了一百年”当成实际很久，其实那是在夸张。|Half an hour may be approximate. We know she waited a long time, not that she arrived at precisely 10:10:00. Calculations can clarify sequence without turning conversational estimates into exact records. My friend recalled exaggerations such as waiting a hundred years, not literal durations.
再读最后几句，我发现解释已经从过去转向下一次。等回复、说清是哪扇门、发现不对就借电话，都比简单说“下次别迟到”更符合这段经历。因为迟到这个词没有说明为什么找错地方，也没有说明消息没有读到。我们给这一段取了个自己的名字：两个人都来了，信息却没见面。|The ending turns from the past to next time: wait for a reply, specify the entrance, borrow a phone if things seem wrong. These fit the incident better than don’t be late, which misses the venue and unread message. We gave it our own title: both people arrived, but their information never met.
朋友让我再讲一遍，不要照着每句字幕翻译。我先讲换地方的原因，再讲手机没电，最后讲那通电话怎样解决了问题。他提醒我，按事情发生的顺序讲和按短剧告诉观众的顺序讲不一样。我试了两个版本，听起来确实不同，但手机没电在消息之前这一点，在两个版本里都没有变。|My friend asked for a retelling without translating each subtitle. I described the venue change, dead phone and resolving call. He noted the difference between chronological events and the order the drama reveals them. I tried both; they sounded different, but the phone dying before the message remained true in each.
''')
M=rows('''
我以为你已经收到。|I thought you had received it.
你发的时候，我手机已经没电了。|My phone was already dead when you sent it.
我只看见消息发出去了。|I only saw that the message had been sent.
那就不是看见我读过了。|That is not seeing that I had read it.
对，我把这两件事当成一件了。|Right. I treated those two things as one.
我也把没看见你，当成你没有来。|I also treated not seeing you as you not having come.
其实我在这边摆椅子。|Actually I was setting up chairs here.
我在那边看大门。|I was looking at the main entrance over there.
下次别看了，直接打电话。|Next time don’t keep looking; just call.
用什么打？你忘了我手机没电。|With what? You’ve forgotten my phone was dead.
也是。那我先确认你收到。|True. Then I’ll first confirm you received it.
现在收到：下次先找能充电的地方。|Message received now: next time first find somewhere to charge.
''')
G=[
card('直到…才…','Identify the first point when something becomes possible','直到 sets the boundary; 才 marks that the event did not happen earlier. Keep the actual sequence distinct from the order information is revealed.','直到电话接通，他才知道我在门口。|Only when the call connected did he know I was at the entrance.\n直到她解释，我才发现自己想错了。|Only after she explained did I realise I had been mistaken.','直到电话接通，他已经一直知道我在门口。','直到电话接通，他才知道我在门口。','The original says the information became known then, not that it was known all along.'),
card('原来…','Mark a newly understood situation','原来 can introduce a discovery that changes an earlier belief. It differs from 原来的, which modifies something previously used or existing.','原来你们换地方了。|So you changed venues.\n原来他没看到，不是故意不回。|So he had not seen it, rather than deliberately not replying.','原来的你们换地方了。','原来你们换地方了。','Use 原来 as the discovery marker; 原来的 needs a modified noun.'),
card('再…也不 / 没…','Describe an extreme that does not change a limit','再 can set an imagined degree; 也不 or 也没 gives the unchanged limitation. Do not treat it as a report of something actually attempted.','我再等，也看不到小厅里的人。|However long I wait, I cannot see the people in the small hall.\n声音再大，也没办法让没电的手机响起来。|However loud the sound, it cannot make a dead phone ring.','我再等，也看不到小厅里的人，所以我已经等了一整天。','我再等，也看不到小厅里的人。','An imagined extreme does not establish that a whole day of waiting occurred.'),
card('不然…','State a consequence if the preceding condition fails','In conversation, 不然 often means otherwise. The consequence can be a possibility rather than an asserted fact.','幸好接了，不然你可能还在外面。|Good thing I answered; otherwise you might still be outside.\n先确认一下，不然又要找错地方。|Confirm first; otherwise we may go to the wrong place again.','幸好接了，不然你可能还在外面，所以现在你仍在外面。','幸好接了，不然你可能还在外面。','The otherwise clause describes the avoided possibility, not the present location.'),
card('把A当成B','Explain a mistaken equation','把 introduces what is being treated as something else; 当成 names that category or assumption. A following correction can separate the two.','我把发过消息当成对方看过。|I treated sending the message as the other person having read it.\n她把沉默当成同意。|She took silence for agreement.','我把发过消息当成看过对方。','我把发过消息当成对方看过。','The subject of having read is the other person, not someone looking at that person.'),
]
spec=dict(title=('Who knows what, and when?','消息发了，不等于看了'),goals=['Track changing knowledge across an original drama scene','Retell a misunderstanding while preserving the order of events','Separate a sent update, a received update and a read notice'],vocabulary=V,grammar=G,
dialogue=(D,[q('gist','What explains the missed meeting?','Different locations and unread information','A deliberate permanent cancellation','A refusal to let Lin participate'),q('detail','What happened before the venue changed?','Lin’s phone died on the bus','Chen recognised the borrowed number','The chairs were packed away after the event'),q('inference','What does Chen realise he should have checked?','That Lin received and understood the update','That Lin disliked every activity','That the large room was in another city')]),
reading=(R,[q('gist','What brings the two accounts together?','A borrowed-phone call followed by directions','Proof that Chen forgot the event','An unexplained refusal at the door'),q('detail','When does Lin borrow a phone?','At 10:40','At 10:05','At nine the previous evening'),q('inference','Why is the wait not explained by the walking distance?','The walk is only five minutes once she has directions','The small hall is a whole day away','The text says there was no waiting')]),
pairedTitle='The viewer’s timeline',pairedReading=(P,[q('gist','What is the value of separate knowledge columns?','Avoiding the assumption that later information was known earlier','Making every character equally informed from the start','Replacing the dialogue with an invented biography'),q('detail','What is inferred rather than directly stated in the dialogue?','An approximate arrival at the main entrance around 10:10','The phone dying at ten','The decision to move at 10:05'),q('inference','What remains true in either retelling order?','The phone died before the message was sent','Every event happened at precisely the same second','Lin never reached the small hall')]),
mediaTitle='Two things treated as one',media=(M,[q('detail','What was Chen doing in the small hall?','Setting up chairs','Replacing Lin’s phone battery','Selling all the tickets'),q('inference','Why does Lin ask with what?','Calling is not possible with her dead phone','She cannot understand the word phone','She has declined all future contact')]),
glosses=[('小厅','small hall'),('接通','connect a call'),('摆','arrange; set out'),('粗心','careless'),('号码','telephone number'),('充电','charge a battery'),('镜头','camera shot'),('不耐烦','impatient'),('推给','shift responsibility onto'),('零秒','zero seconds'),('三栏','three columns'),('夸张','exaggerate'),('反应','reaction'),('故意','deliberately'),('门外','outside the entrance'),('贴','attach a notice'),('沉默','silence'),('字幕','subtitles'),('关系','relationship'),('准确','accurate'),('风','wind'),('坏','broken; bad'),('前后','before and after; surrounding context')],
place='A small community hall',context='A light failure changes the venue after a friend’s phone dies; each mistakes an incomplete clue for the whole story.',
turns=[('我发过消息，你没看吗？','I sent a message; didn’t you see it?','Explain the missing information',['我十点手机就没电了，没看到后来换地方的消息。']),('我还以为你没来呢。','I thought you had not come.','Correct a belief with a concrete detail',['我已经到了，只是在大门口等，不知道你们在小厅。']),('下次怎么确认？','How can we confirm next time?','Ask for acknowledgement',['换地方以后先等一句回复，没收到就再想办法联系。'])],
usage=[('Separate sending from reading','我发了，但还没确认你看到。','I sent it, but have not confirmed you saw it.','A sent message is not evidence of another person’s attention.'),('Ask before judging','你刚才是没看到，还是没办法回复？','Did you not see it, or were you unable to reply?','Offer plausible alternatives without assigning intent.'),('Retell with perspective','他当时还不知道我的手机没电。','He did not yet know my phone was dead.','Anchor a person’s knowledge to a time rather than later information.')],
tasks=practice(
[(D[2][0],D[2][1],'The move was decided at 10:05 after the light broke.',True,'Both cause and decision time are stated.'),(D[5][0],D[5][1],'Lin saw the new message before boarding at ten.',False,'Her phone died at ten and she says she did not see it.'),(R[3][0],R[3][1],'Seeing the paper proves Lin read its contents.',False,'The wind prevented her from reading it.'),(P[4][0],P[4][1],'Half an hour establishes an exact arrival at 10:10:00.',False,'The account explicitly treats the duration as approximate.')],
[('你十点手机就没电，十点零五分发的消息为什么没回？','Your phone died at ten. Why was there no reply to the message sent at 10:05?',['手机没电，我没看到；不是故意不回。','我十点零五分已经看完，只是没回。','我十点半手机才没电，之前还看过。'],0,'The reply gives a concrete reason without treating sending as reading.'),('这次发完消息没有等回复。下次怎样确认对方收到？','We did not wait for a reply this time. How can we confirm receipt next time?',['等对方回一句，再确认是哪扇门。','看到自己发出，就算对方已经读过。','等对方到了，再把新地址发出去。'],0,'Acknowledgement and an entrance description address the actual failure.'),('你只说没看见她，还没确认。怎么知道她没来？','You only said you did not see her, without checking. How do you know she did not come?',['我只是没看见她，还得确认。','我还没确认，但已经确定她没到。','我看到她在门口，所以她根本没来。'],0,'Not seeing someone alone does not prove absence.')],
[('直到电话接通，他才知道我在门口。','Only when the call connected did he know I was at the entrance.','才'),('我把发过消息当成对方看过。','I treated sending the message as the other person having read it.','当成'),('我总算找到你们了。','I finally found you all.','总算')],
[[(V[i][3],V[i][4]) for i in [0,1,4]],[(V[i][5],V[i][6]) for i in [12,15,17]],[(V[i][3],V[i][4]) for i in [6,18,20]]]),
review='Native review: 你今天已经把大门看够了 teasing, 总算/居然 force and the figurative 信息却没见面. Phone dead at 10:00 precedes the 10:05 move and message; call at 10:40 precedes a five-minute walk. Half-hour waiting implies approximately 10:10 arrival, not an exact timestamp. Missing acknowledgement never establishes deliberate exclusion. The scene does not claim read-receipt functionality or a device feature.')
spec['glosses'].extend([('犯','commit, e.g. make a mistake'),('毫无','not at all; completely without')])
write(5,4,spec,publish='--publish' in sys.argv)
