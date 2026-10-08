"""Set a clear conversational limit while keeping a friendship open."""
import sys
from advanced_core import write,rows,words,q,card,practice
V=words('''
尊重|respect|tôn trọng|你不想说的部分，我会尊重。|I’ll respect the parts you don’t want to discuss.|尊重他的决定，不等于必须同意他的所有想法。|Respecting his decision doesn’t mean agreeing with all his ideas.
抱怨|complain|phàn nàn|你可以抱怨，不过我今天只能听一会儿。|You can complain, but I can only listen briefly today.|她抱怨排队太久，但没有责怪店员。|She complained about the long queue without blaming the staff.
无奈|helpless; without a good alternative|bất lực|我有点无奈，不知道怎么把话接下去。|I feel rather stuck and don’t know how to continue.|他无奈地看着没接通的电话。|He looked helplessly at the call that hadn’t connected.
心态|mindset|tâm thế|我想换个心态，不把每次没接电话都当成拒绝。|I want to stop treating every unanswered call as rejection.|心态变了，不代表问题马上解决。|A changed mindset doesn’t mean the problem is solved immediately.
打扰|disturb; interrupt|làm phiền|这么晚打电话，是不是打扰你了？|Am I disturbing you by calling so late?|你先忙，我晚一点再来，不打扰了。|Carry on; I’ll come back later and leave you to it.
私人|private; personal|riêng tư|这部分是私人的，我现在不想聊。|That part is personal; I don’t want to discuss it now.|这是私人信件，先问本人再看。|It’s a private letter; ask its owner before reading it.
坚定|firm; resolute|kiên định|她说得很平静，态度却很坚定。|She spoke calmly, but her position was firm.|我想坚定一点说清楚，不是提高声音。|I want to state it firmly, not raise my voice.
委托|entrust; commission|ủy thác|他委托我把资料带给同事。|He entrusted me to bring the materials to a colleague.|这项工作不能没有问过就委托给别人。|You can’t assign this work to someone without asking.
沟通|communicate|giao tiếp|我们需要沟通时间，不只是沟通内容。|We need to discuss timing as well as content.|沟通以后，我才知道他没有听清。|Only after talking did I learn he hadn’t heard clearly.
拒绝|refuse; reject|từ chối|我拒绝的是这个时间，不是以后都不见面。|I’m declining this time, not all future meetings.|她拒绝了邀请，也谢谢对方想到她。|She declined the invitation and thanked them for thinking of her.
敏感|sensitive|nhạy cảm|他对这个话题很敏感，我们先不追问。|He's sensitive about this topic; let's not press him for now.|她对声音很敏感，一点动静就能听见。|She is sensitive to sounds and can hear even a small noise.
真诚|sincere|chân thành|我想真诚地说明，不想随便找个理由。|I want to explain sincerely rather than invent an excuse.|她真诚地谢谢我听完，却没有要求我一定同意。|She sincerely thanked me for listening without requiring agreement.
直接|direct; directly|trực tiếp|我直接说今天只能聊二十分钟。|I said directly that I could talk for only twenty minutes today.|你可以直接问我，不用让别人转告。|You can ask me directly without having someone pass it on.
理解|understand|hiểu|我理解你想说，但今天不方便。|I understand you want to talk, but today isn’t convenient.|我还没理解，你再举一个例子好吗？|I haven’t understood yet; could you give another example?
失望|disappointed|thất vọng|听见不能继续聊，他有点失望。|He was a little disappointed we couldn’t keep talking.|她失望了一会儿，后来又问有没有别的时间。|After feeling disappointed briefly, she asked about another time.
个人|individual; personal|cá nhân|这是我的个人安排，不要求你一样。|This is my own arrangement; I don’t expect yours to be identical.|个人意见可以说，但别当成所有人的意见。|You can share a personal opinion, but don’t treat it as everyone’s view.
坚决|firmly; resolutely|kiên quyết|这次我坚决不把睡前的时间再排满。|This time I won’t fill the time before bed again.|她坚决反对把没确认的消息发出去。|She firmly opposed sending out unconfirmed information.
请求|request|yêu cầu|我想提一个请求，先问你有没有时间。|I’d like to ask something, but first whether you have time.|这个请求太突然，他需要想一下。|The request came so suddenly he needed time to think.
承担|take on; bear|đảm nhận|我愿意帮一部分，不能全部承担。|I’m willing to help with part, but can’t take on all of it.|她承担了安排场地的工作。|She took on arranging the venue.
负担|burden|gánh nặng|每天都等电话，对我成了负担。|Waiting for calls every day became a burden for me.|把时间说清楚，减轻了双方的负担。|Being clear about timing eased the burden for both.
责任|responsibility|trách nhiệm|朋友的每一个决定，不都是我的责任。|Not every decision a friend makes is my responsibility.|整理共享的桌子，是我们一起的责任。|Tidying the shared table is our joint responsibility.
体会|understand through experience; feel|cảm nhận|我能体会他一个人在外面的感觉。|I can understand how he feels alone away from home.|这次以后，我才体会到等回复有多难。|Only after this experience did I feel how hard waiting for a reply can be.
适应|adapt; get used to|thích nghi|他还在适应新的工作时间。|He’s still adapting to his new work schedule.|我慢慢适应先约时间再聊天。|I’m getting used to arranging a time before chatting.
改善|improve|cải thiện|我们想改善联系的方式，不是结束联系。|We want to improve how we keep in touch, not end contact.|换个说法，可能改善气氛，却不能代替实际安排。|Changing the phrasing may improve the atmosphere but can’t replace practical arrangements.
''')
D=rows('''
你昨晚没接，我是不是说太多了？|You didn’t answer last night. Had I been talking too much?
不是只说昨晚。最近好几次都是十一点以后，我已经准备睡了。|It’s not just last night. Several recent calls were after eleven, when I was getting ready for bed.
我下班才有时间，白天又不方便。|I only have time after work, and daytime isn’t convenient.
我知道你工作时间晚，但我第二天要早起。|I know you work late, but I have to get up early the next day.
那你以后都不想听了？|So you don’t want to listen anymore?
我没这样说。我是想把时间先约好，十一点以后就不聊了。|That’s not what I said. I want to arrange a time first and not chat after eleven.
可有时候到了晚上，我才知道自己想说什么。|But sometimes I only know what I want to say once evening comes.
可以先写给我，不用等我马上回。第二天我有空再看。|You can write it to me without waiting for an immediate reply. I’ll read it when free the next day.
要是我就想打电话呢？|What if I want a call?
那先问有没有时间。明晚九点，我可以聊二十分钟。|Then ask if I have time first. Tomorrow at nine I can talk for twenty minutes.
二十分钟会不会太短？|Won’t twenty minutes be too short?
对你可能短，对我已经要留出时间了。我不能每次都一直聊。|It may feel short to you, but I still need to make time for it. I can’t keep talking indefinitely every time.
好，我有点失望，不过听懂了。|Okay. I’m a little disappointed, but I understand.
我知道你会失望。我还是想和你联系，只是这个安排得改。|I know you're disappointed. I still want to keep in touch; this arrangement needs changing.
那明晚先讲一件，别从整个月第一天开始。|Then tomorrow I’ll start with one thing, not the first day of the whole month.
这个主意不错，你上次讲到周二我就忘了周一。|Good idea. Last time you reached Tuesday, I’d already forgotten Monday.
行，我准备一个短版。到了时间你直接提醒我吧。|Okay. I’ll prepare a short version. Remind me directly when time is up.
好。没讲完的我们再找时间，不保证每天都有空。|Okay. We’ll find another time for what remains, but I can’t promise to be free every day.
''')
R=rows('''
朋友换了新的工作，常常很晚才下班。我们原来每周见一次，现在见面少了，他就晚上打电话。最开始我很高兴，觉得他还愿意把生活里的事情告诉我。我也听他说新的同事、回家的路和白天没来得及吃的饭，没有把每一次电话都当成问题。|My friend changed jobs and often finished late. We used to meet weekly; now he called at night. At first I was pleased he still shared his life: colleagues, the journey home and missed meals. I didn’t treat every call as a problem.
后来电话越来越晚，有几次过了十一点。第一次我想，只听一会儿就睡，可讲完已经过了十二点。第二天我早上有课，坐在那里总想闭眼睛。我没有把这些告诉他，只说最近忙，偶尔不接。他听见我说忙，就以为过几天会和以前一样，不知道我想改的是联系的时间。|The calls grew later, several after eleven. One supposed short chat lasted past midnight; I was sleepy in an early class next day. I only said I was busy and sometimes didn’t answer, without explaining the timing problem. He expected things to return to normal once I was less busy.
一次我没接，第二天他问是不是自己说太多。我本来想再找一个理由，后来觉得这样会让他继续猜。我告诉他，十一点以后我不再接着聊，因为第二天要早起。这个时间是我的个人安排，不是规定朋友都必须一样，也不是说他的工作问题不重要。|After an unanswered call he asked whether he’d talked too much. Rather than invent another excuse, I explained I wouldn’t keep chatting after eleven because I needed an early start. It was my own availability, not a rule for everyone or a claim his work problems didn’t matter.
他有点失望，说下班以后才知道自己想讲什么。我听完，没有马上把安排收回，也没有说他不应该失望。我提出可以先发文字，不用等我马上回；想打电话就先问时间。明晚九点，我可以留出二十分钟。文字和电话都还可以，只是不能每次都由一个突然响起来的铃声决定。|He was disappointed, saying he often knew what to discuss only after work. I didn’t withdraw the limit or forbid the feeling. He could send writing without expecting an immediate reply, or ask about call availability. I offered twenty minutes at nine the next evening. Both methods remained possible, without an unexpected ring deciding every time.
第二天他真的先发了一句，问九点还方便吗。我说方便，先问他最想讲哪件事。他选了和同事约时间的误会，没有从上个月第一天开始说。我们聊的时候，我仍然认真听，也问了自己不清楚的地方。二十分钟快到时，我提醒还有两分钟，他把最后的问题说完，我们就结束了。|The next day he checked whether nine still suited me. I asked which event mattered most; he chose a scheduling misunderstanding with a colleague rather than starting from the beginning of the previous month. I listened and asked questions. Two minutes before the limit I reminded him; he finished his question and we ended.
挂电话以后，我发现自己没有像前几次那样一边听一边看钟。他也发来消息，说短一点反而容易说清楚。不过一次顺利不代表以后永远不会有变化。后来有一天我九点要外出，就提前告诉他，改到第二天。他说可以，没有把改一次时间当成我不想再做朋友。|Afterwards I hadn’t spent the call watching the clock as before. He said a shorter account was easier to explain. One success didn’t guarantee every future call would fit. When I later needed to go out at nine, I proposed the next day beforehand. He accepted without treating a change as ending the friendship.
我仍然关心他的生活，也愿意在自己能做到的时候帮忙。他也开始问我最近怎么样，不是每次只有一个人讲。我们没有把谁更好的问题分出胜负，只把原来没说清楚的时间说出来。这个安排以后可能还会调整，但我不再需要先累到不想接，再希望他自己明白。|I still cared and helped when I could. He began asking about my life too. We weren’t deciding who was better; we clarified previously unstated availability. It might change again, but I no longer had to become too tired to answer and hope he’d work out why.
''')
P=rows('''
我开始新工作以后，下班时间变晚，认识的人也少。坐车回去时想起白天的事，总觉得终于有时间讲了。朋友前几次都接电话，我就慢慢把这个时间当成我们共同方便的时间。其实我没有问过他第二天几点起，也没有看见电话另一边他是在坐着休息，还是已经准备睡觉。|After starting a new job I finished late and knew few people. On the journey home I finally wanted to discuss the day. Because my friend answered the first calls, I gradually assumed that time suited us both. I hadn’t asked when he got up or whether he was relaxing or preparing for bed.
后来有一次他没接，我有点难受，先想到是不是嫌我总抱怨。第二天问他，他没有说是，也没有只说忙，而是解释最近好几次过了十一点。我回想了一下，的确有一次一直讲到十二点以后。我当时觉得自己终于把话说完，没注意对方已经几次说第二天还要早起。|After an unanswered call I wondered whether he disliked my complaints. The next day he explained several calls had been after eleven. One had lasted past midnight. I’d been glad to finish my account and missed his repeated references to an early start.
他说十一点以后不聊，我第一反应是以后都不想听了。现在看，那是我把一个时间的限制变成了整段关系的判断。他当时回答，还是想联系，只是要先约好。我不能因为自己想说，就把他的准备睡觉看成没有兴趣；也不能因为他说得平静，就以为这个安排可以一直再问到他答应。|I first heard his limit as no longer wanting to listen at all. I had turned a time restriction into a judgment of our relationship. He wanted contact but with an arranged time. My wish to speak didn’t make his bedtime lack of interest, and his calmness didn’t mean I could keep asking until he agreed.
我还是觉得二十分钟短，却决定试一次。准备短版时，我发现自己平时常把前面每个细节都讲一遍，真正想问的问题到最后才出现。这次我先选了和同事约时间的事，写下自己最不理解的一点。不是为了把心情全部藏起来，而是让朋友知道我为什么把这件事拿出来说。|Twenty minutes still seemed short, but I tried. Preparing, I noticed I usually repeated every detail before reaching the question. I chose the scheduling issue and wrote down what puzzled me most—not to hide feelings, but to explain why I wanted to discuss it.
九点前我先问他方便不方便，收到回复才打。我们聊的时候，他问了两个问题，我也更清楚自己想做什么。到了二十分钟，他说今天先到这里，我没有再加一句“还有最后一件”。以前这句常常又变成十分钟，这次我说好，谢谢你听，下次再讲。挂掉以后，事情不全解决，但我没有觉得自己被赶走。|I checked before nine and called after a reply. His questions helped clarify my next step. At twenty minutes I didn’t add one more thing, which used to become ten extra minutes. I thanked him and left the rest for another time. The problem wasn’t wholly solved, but I didn’t feel expelled.
后来有一天他说要外出，不能按原来的时间聊，我有一点失望，但没有追问一定去哪里。我们改到第二天。我也开始把不急的事情写下来，有时写完自己就知道问题是什么，不需要每一件都打电话。有时还是想听他的声音，就先问什么时候方便，而不是只发一个电话过来。|When he later had plans, I felt disappointed but didn’t demand his destination. We moved the call to the next day. I began writing non-urgent issues down; sometimes writing clarified them without a call. When I wanted his voice, I asked about availability rather than starting with a ringing phone.
这次沟通没有让我马上喜欢所有限制，却让我知道哪里可以继续，哪里需要换办法。朋友也讲了他的课和活动，我才发现自己最近问得很少。现在我们仍然会聊长一点，只是那要双方都有时间。我不再把每一次没接都当作拒绝，也不把一回愿意多听当作以后每晚都一样。|The discussion didn’t make me immediately enjoy every limit, but showed where contact could continue differently. Hearing about his classes and activities, I realised I’d asked little lately. We still sometimes talk longer when both are free. An unanswered call isn’t necessarily rejection, and one longer call isn’t an agreement to every night.
''')
M=rows('''
短版准备好了？|Is your short version ready?
好了，从今天下午开始。|Yes. It starts this afternoon.
不错，不是从上个月开始。|Good. Not from the previous month.
但你得先知道昨天发生了什么。|But first you need to know what happened yesterday.
昨天需要讲多久？|How long will yesterday take?
一分钟。我写了三句话。|One minute. I wrote three sentences.
那可以。先说你最想问的。|That works. Start with what you most want to ask.
我想问，别人说再看看，是还没决定吗？|When someone says we’ll see, does that mean they haven’t decided?
要听前后。你同事当时怎么说？|It depends on context. What did your colleague say then?
他说周五时间还没定，让我明天再问。|He said Friday’s time wasn’t settled and asked me to check tomorrow.
那先按这句理解，不用猜已经答应了。|Then use that statement for now; don’t assume he agreed already.
好。短版里终于有一个问题了。|Okay. My short version finally has a question in it.
''')
G=[
card('怎么…也 / 都不…','Describe a persistent negative result','怎么 combined with 也不 or 都不 can describe a negative result despite repeated or varied attempts. It is stronger than a simple one-time negative.','昨晚怎么打也接不通。|However I tried calling last night, it would not connect.\n这句话我怎么想都不明白。|However I think about this sentence, I cannot understand it.','昨晚怎么打也接不通，所以他一定讨厌我。','昨晚怎么打也接不通。','Failed attempts establish a connection problem, not another person’s motive.'),
card('X归X，…','Allow a feeling without cancelling a decision','Acknowledge X and then distinguish the practical point. Do not use the pattern as a dismissive substitute for listening.','失望归失望，我们还是得先约时间。|Disappointed or not, we still need to arrange a time first.\n想帮归想帮，我今天不能聊太久。|I do want to help, but cannot talk too long today.','失望归失望，所以不许你失望。','失望归失望，我们还是得先约时间。','The first clause acknowledges disappointment rather than banning it.'),
card('A的A，B的B','Describe different people doing different things','Repeated verbs can distribute parallel actions across a group. This is a compact description, not a universal claim about everyone.','吃饭的吃饭，聊天的聊天，大家各做各的。|Some eat, some chat; everyone does their own thing.\n准备的准备，休息的休息，没有一起开始。|Some prepare and some rest; they do not all start together.','吃饭的聊天，聊天的吃饭，所以是各做各的。','吃饭的吃饭，聊天的聊天，大家各做各的。','Repeat each activity in its own pair to describe separate ongoing groups.'),
card('为的是…，不是…','Clarify the aim of a limit','The purpose clause names the intended aim; 不是 distinguishes it from a mistaken aim. The surrounding conduct should support the explanation.','先约时间，为的是能认真听，不是以后都不联系。|Arranging a time is so I can listen properly, not stop contact altogether.\n写短一点，为的是说清问题，不是把心情藏起来。|Writing a shorter version is to make the issue clear, not hide feelings.','先约时间，为的是不再联系，后面却说不是不再联系。','先约时间，为的是能认真听，不是以后都不联系。','Keep the stated purpose and the corrected assumption distinct rather than contradicting them.'),
card('…得…','Express a necessary action in speech','得 pronounced děi means need to or must before a verb. Compare de after an adjective in a result or degree complement.','这个安排得改。|This arrangement needs changing.\n你得先问有没有时间。|You need to ask first whether there is time.','这个安排改得。','这个安排得改。','For necessity, děi precedes the action 改; it is not a degree complement after it.'),
]
spec=dict(title=('Still friends, with a clearer limit','想听，也得先约时间'),goals=['State when and how much conversation is possible','Acknowledge disappointment without silently withdrawing a limit','Distinguish a declined time from the end of contact'],vocabulary=V,grammar=G,
dialogue=(D,[q('gist','What is the proposed change?','Arrange calls and stop chatting after eleven','Never discuss anything again','Require daily unlimited calls'),q('detail','What is offered for tomorrow evening?','Twenty minutes at nine','An entire night after eleven','No alternative at all'),q('inference','Why clarify a time limit rather than merely say busy?','It makes the actual availability understandable','It proves one person never cares','It means the other person may not feel disappointed')]),
reading=(R,[q('gist','What improves after the discussion?','Contact continues with clearer timing and more mutual conversation','All difficult feelings vanish permanently','Every call becomes longer'),q('detail','When is the agreed call checked?','Before nine the next evening','Only after midnight','After the friend stops all work forever'),q('inference','Why does one smooth call not settle everything?','Future availability can change and require another arrangement','The conversation never happened','The twenty-minute limit was secretly a test score')]),
pairedTitle='The friend who calls after work',pairedReading=(P,[q('gist','What assumption does the caller revise?','Answering early calls did not mean every late time suited both people','A single answered call means unlimited availability forever','A calm limit can be ignored until it changes'),q('detail','What does the caller do when twenty minutes end?','Thanks the friend without adding another last thing','Keeps talking for another hour without asking','Demands an account of all future evenings'),q('inference','What remains possible after the limit?','Longer chats when both have time','No more contact of any kind','Immediate solutions to every work problem')]),
mediaTitle='The short version needs a question',media=(M,[q('detail','What did the colleague say about Friday?','The time was not set and the caller should check tomorrow','Friday was confirmed permanently','The friend must answer after eleven'),q('inference','What does the friend advise against assuming?','That an unsettled arrangement is already agreed','That the colleague mentioned Friday','That the caller can ask a question')]),
glosses=[('铃声','ringing sound'),('收回','take back; withdraw'),('挂电话','hang up a call'),('双方','both parties'),('责怪','blame'),('气氛','atmosphere'),('光线','light; lighting'),('准备睡觉','prepare for bed'),('转告','pass on a message'),('睡前','before bed'),('藏起来','hide away'),('限制','limit; restriction'),('赶走','drive away'),('推问','press with questions'),('嫌','dislike; find something objectionable'),('日历','calendar'),('接通','connect a call'),('一分钟','one minute'),('不急','not urgent')],
place='A planned call between friends',context='Several calls after eleven have become tiring; the friends clarify a twenty-minute call and later contact.',
turns=[('你以后都不想听了？','Do you never want to listen again?','Correct a global interpretation',['不是，我想先约时间，十一点以后就不聊了。']),('今晚再聊一会儿不行吗？','Can’t we talk a little longer tonight?','State a limit and a concrete alternative',['今晚不行，明晚九点可以聊二十分钟。']),('我还是有点失望。','I’m still a little disappointed.','Acknowledge without changing the limit',['我理解，也想继续联系，只是时间要先约好。'])],
usage=[('Check availability','现在方便聊十分钟吗？','Is now a good time for a ten-minute chat?','A question is not already permission; follow the answer.'),('Be clear at the end','今天先到这里，没说完的再找时间。','Let’s stop here today and find another time for the rest.','A calm limit can be clear without being harsh.'),('Keep a refusal specific','我今天没有时间，不是以后都不想聊。','I don’t have time today; it doesn’t mean never wanting to chat again.','Specify the actual constraint instead of leaving the other person to infer a permanent decision.')],
tasks=practice(
[(D[5][0],D[5][1],'The speaker wants no contact ever again.',False,'The stated change concerns arranging time and calls after eleven.'),(D[9][0],D[9][1],'Tomorrow’s offer is twenty minutes at nine.',True,'The time and duration are explicit.'),(R[4][0],R[4][1],'The friend adds another last item when time is up.',False,'The question is finished and the call ends.'),(P[5][0],P[5][1],'A changed evening is treated as proof of rejection.',False,'They move the call to the next day instead.')],
[('你今天没空，明晚九点能聊二十分钟。现在方便聊吗？','You are busy today but offered twenty minutes tomorrow at nine. Is now convenient?',['今天不行，明晚九点可以聊二十分钟。','今天可以，你刚才说今天有空。','明晚十点聊一个小时，和刚才说的一样。'],0,'The reply gives an actual answer and alternative.'),('你说今天先结束，明晚再聊。我有点失望。','You said to end today and chat tomorrow. I am a little disappointed.',['我理解，不过今天还是先到这里。','那我收回刚才的安排，今晚继续到十二点。','我说的明晚，是以后都不再联系。'],0,'Acknowledge the feeling while retaining the stated limit.'),('他昨晚一次没接，还不知道原因。是不是不想做朋友了？','He missed one call last night, and we do not know why. Does he not want to be friends?',['先问问原因，没接一次还不能确定。','已经问过了，他明确说以后不做朋友。','既然不知道原因，就已经确定是拒绝。'],0,'One missed call does not establish a relationship decision.')],
[('这个安排得改。','This arrangement needs changing.','得'),('先约时间，为的是能认真听。','We arrange a time so I can listen properly.','为的是'),('这么晚打电话，是不是打扰你了？','Am I disturbing you by calling so late?','打扰')],
[[(V[i][3],V[i][4]) for i in [0,4,5]],[(V[i][5],V[i][6]) for i in [8,9,18]],[(V[i][3],V[i][4]) for i in [19,21,23]]]),
review='Native review: calm firmness, acknowledgement of disappointment, 委托 workplace register, distribution pattern A的A B的B, and děi necessity versus de complement. The stated times are the fictional friends’ availability, not universal rules. A twenty-minute offer is not automatic permission for daily calls; the second account preserves continuing contact and adjustment. Chinese and English retellings avoid turning refusal of a time into refusal of the person.')
from common import dictionary
dictionary.update({'得改':'děi gǎi','得先':'děi xiān'})
spec['glosses'].extend([('动静','sound or movement; signs of activity')])
write(5,6,spec,publish='--publish' in sys.argv)
