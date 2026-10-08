"""Interpret friendly teasing from the scene, not a phrase-only label."""
import sys
from advanced_core import write,rows,words,q,card,practice
V=words('''
调皮|mischievous; playful|nghịch ngợm|这个孩子有点调皮，但不爱骗人。|This child is a little mischievous but doesn’t like lying.|她调皮地把最后一块点心藏起来了。|She playfully hid the last pastry.
过分|excessive; go too far|quá đáng|让一个人做完这些，太过分了。|Making one person do all this is too much.|你这次玩笑开得有点过分。|Your joke went a little too far this time.
天真|innocent; naive|ngây thơ|小时候我天真地以为月亮会跟着我走。|As a child I naively thought the moon followed me.|她说想一天学会，我觉得这个想法有点天真。|She said she wanted to learn it in a day; that idea seems a little naive.
得意|pleased with oneself; smug|đắc ý|他赢了以后，笑得很得意。|After winning he smiled smugly.|别太得意，还有最后一轮呢。|Don’t be too pleased with yourself; there’s still one round left.
大方|generous; at ease in manner|hào phóng; tự nhiên|她很大方，把自己的书借给大家。|She’s generous and lends everyone her books.|第一次上台，他说话就很大方。|He spoke confidently on his first appearance on stage.
看不起|look down on|coi thường|他从来不因为工作不同就看不起别人。|He never looks down on people for doing different work.|别看不起这个小店，做的东西很认真。|Don’t underestimate this small shop; it makes things carefully.
自信|self-confident; confidence|tự tin|准备以后，我比刚才自信多了。|After preparing I’m much more confident than before.|她有自信，也愿意听不同意见。|She’s confident and willing to hear different views.
亲密|close; intimate|thân thiết|他们从小一起长大，关系很亲密。|They grew up together and are very close.|只有亲密的朋友知道这个小名。|Only close friends know this childhood nickname.
语法|grammar|ngữ pháp|这句语法没错，但不适合这个场合。|The grammar is correct, but it doesn’t fit this situation.|我想问问这两个语法结构有什么不同。|I’d like to ask how these two grammatical structures differ.
语音|speech sounds; voice message|ngữ âm; tin nhắn thoại|这次课先练语音，再练对话。|This class practises speech sounds before dialogue.|她给我发了一条语音，让我听听语气。|She sent me a voice message so I could hear the delivery.
形容|describe|miêu tả|你会怎么形容这个人的表情？|How would you describe this person’s expression?|我找不到合适的词来形容那个声音。|I can’t find the right word to describe that sound.
误会|misunderstanding; misunderstand|hiểu lầm|我把他的玩笑当真，误会了。|I took his joke seriously and misunderstood.|别误会，我不是说你做得不好。|Don’t misunderstand; I’m not saying you did a bad job.
话题|topic|chủ đề|这个话题我们上次聊过。|We talked about this topic last time.|大家都安静了，我换了个话题。|Everyone went quiet, so I changed the topic.
关系|relationship; connection|quan hệ|他们关系很好，但意见不总一样。|They have a good relationship but don’t always agree.|这件事和钱没关系。|This has nothing to do with money.
表情|facial expression|biểu cảm|他说话时表情很认真。|His expression was serious as he spoke.|看到盒子里的东西，她的表情变了。|Her expression changed when she saw what was in the box.
放松|relax; loosen|thư giãn|先坐一会儿，放松一下。|Sit for a while and relax.|放松以后，我说话没那么快了。|After relaxing I didn’t speak so fast.
''')
D=rows('''
你今天可真早。|You’re really early today, aren’t you?
早？我不是晚了十分钟吗？|Early? Aren’t I ten minutes late?
对，我的咖啡都快喝完了。|Exactly. I’ve almost finished my coffee.
懂了，你在笑我。对不起，刚才走错出口了。|Got it. You’re teasing me. Sorry, I took the wrong exit.
先坐吧。怎么穿这么正式？你等会儿还要去开会？|Sit down first. Why so formal? Do you have a meeting later?
没有，今天第一次穿这件外套。不好看吗？|No, it’s my first time wearing this coat. Doesn’t it look good?
怪好看的。我刚才还以为你要去领奖。|It looks pretty good. I thought you were going to collect an award.
那你快给我颁一个，别只有咖啡。|Then hurry up and give me one instead of just coffee.
给你一个“终于找到出口”的奖，行不行？|An award for “finally finding the exit”—will that do?
才不要呢。你上次还让我去错了车站。|No thanks. You sent me to the wrong station last time.
好好好，这个话题跳过。想吃什么？|All right, all right, let’s skip that topic. What would you like to eat?
先来点甜的。听你说完，我现在需要点安慰。|Something sweet first. After hearing you out, I could use some comfort.
''')
R=rows('''
我第一次听到“你今天可真早”，是在迟到十分钟以后。按字面看，朋友像是在夸我；看他已经喝完半杯咖啡的样子，就知道不是这个意思。|The first time I heard “you’re really early today” was after arriving ten minutes late. Literally it sounded like praise, but seeing my friend with half his coffee gone made the intention clear.
那天我们笑了几句，很快开始点吃的。我认识他很久，知道他会拿我的迟到开玩笑，也知道说一句对不起就能把事情接过去。|We joked briefly and soon started ordering food. I’d known him a long time and knew he teased me about lateness; a quick apology let us move on.
后来我在活动里看到一个新同学迟到，差点也说同样的话。她进门时很紧张，一直解释公交车改了路线。我最后只说“没关系，先坐吧”，没有照搬朋友的说法。|Later, at an event, a new classmate arrived late and I almost used the same phrase. She was nervous and kept explaining that her bus route had changed. I just said, “It’s okay, sit down,” rather than copying my friend’s line.
活动结束后，她问我刚才是不是错过了重要内容。我把前面的安排说给她听，我们后来聊了喜欢的音乐。熟悉以后，也会开玩笑，但不是一开始就拿她着急的事来笑。|Afterwards she asked whether she’d missed anything important. I explained the plans, and we later talked about music we liked. Once we knew each other we joked too, but I didn’t start by teasing her about something that was worrying her.
我给自己记下的不是一句固定的“友好表达”，而是三个问题：刚才发生了什么？两个人熟不熟？对方现在什么表情？同样一句话，答案变了，听起来也会变。|I didn’t note a fixed “friendly phrase,” but three questions: what just happened, how well do the people know each other, and what expression does the other person have? When those answers change, the same sentence can sound different.
现在看剧时，我会留意说话前后发生的事。人物说“真不错”，可能是真心称赞，也可能是对刚发生的问题作出反应。我先找线索，不只找一个词的翻译。|Now when watching dramas I notice what happens before and after a line. “Really good” may be sincere praise or a reaction to a problem. I look for clues rather than just the translation of one word.
''')
M=rows('''
你做的？看着还真不错。|Did you make this? It really looks good.
当然。我试了三次才做好。|Of course. It took three attempts to get it right.
那我可以吃一个吗？|May I have one?
先等一下，你还没夸味道呢。|Wait a moment. You haven’t praised the taste yet.
还没吃怎么夸？|How can I praise it before eating?
也是。吃完再说，别只说“不难吃”。|True. Tell me after trying it, and don’t just say “not bad.”
要求还挺高。好，我认真吃。|Your standards are pretty high. Okay, I’ll eat attentively.
认真吃是什么样？慢一点还是多一点？|What does eating attentively look like—slower, or more?
''')
G=[
card('可真 + predicate','Add strong conversational emphasis','可真 strengthens the following evaluation. It does not encode teasing by itself: timing, known facts and the relationship may make a literal compliment ironic.','你今天可真早。|You’re really early today.\n这里可真安静。|It’s really quiet here.','只要说可真，就一定是在讽刺。','可真加强语气，意思还要看场景。','The same emphasis can be sincere or ironic; the scene supplies the interpretation.'),
card('怪…的','Give a conversational “quite” evaluation','怪 before an adjective with 的 often means quite or rather in casual speech. This use differs from 怪不得 and the adjective 奇怪.','这件外套怪好看的。|This coat is quite nice.\n今天怪冷的。|It’s quite cold today.','这件外套好看怪的。','这件外套怪好看的。','Place 怪 before the adjective and 的 after it.'),
card('才不 / 才不要 + 呢','Reject an idea emphatically in casual speech','才 before a negative can make a denial sound stronger and playful or defensive. It is not the time-marker meaning “only then”.','我才不要这个奖呢。|I don’t want this award.\n我才不会忘呢。|I won’t forget, you know.','我才不要这个奖呢，意思是我等到明天才要。','我才不要这个奖呢，意思是我不想要。','This 才 strengthens the refusal rather than scheduling it.'),
card('还没…怎么…','Point out a missing condition conversationally','A negative completed-state phrase sets up the rhetorical question: without the earlier event, how can the next action happen? A genuine request for a method can have the same words, so inspect the reply.','还没吃怎么夸味道？|How can I praise the taste before eating?\n还没看完，怎么知道最后发生什么？|How can I know the ending before finishing?','还没吃怎么夸味道，所以我已经吃了。','还没吃怎么夸味道？先让我尝一个。','The speaker is asking to try it before assessing its taste.'),
]
spec=dict(title=('Was that a compliment or a joke?','你今天可真早'),goals=['Interpret a teasing line using timing and shared facts','Recognise conversational emphasis without assigning it one fixed emotion','Change a reply to fit a new acquaintance rather than a close friend'],vocabulary=V,grammar=G,dialogue=(D,[q('gist','Why does “you are early” sound teasing here?','The listener is ten minutes late','The café has not opened yet','The listener arrived before the agreed time'),q('detail','What caused the delay?','Taking the wrong exit','Receiving an actual award','Finishing all the coffee first'),q('inference','Is the coat comment also simply a negative criticism?','No, the speaker says it looks quite good and jokes about an award','Yes, every joke must reject the coat','No comment about the coat is made')]),reading=(R,[q('gist','What does the narrator learn?','A familiar phrase needs situational and relationship context','可真 always expresses anger','Literal translation alone settles every intention'),q('detail','What reply is given to the new classmate?','没关系，先坐吧','你可真早','你一定在骗我'),q('inference','Why avoid the old teasing line with the new classmate?','She is anxious and they do not yet know each other well','The old line has no valid grammar','The classmate arrived a day early')]),mediaTitle='Eat attentively',media=(M,[q('detail','How many attempts did the maker need?','Three','One','Ten'),q('inference','Why can the friend not praise the taste yet?','They have not tried the food','The maker has never cooked','The food has already all been eaten')]),glosses=[('领奖','receive an award'),('颁','award; present a prize'),('安慰','comfort'),('照搬','copy unchanged'),('熟悉','familiar with'),('讽刺','irony; sarcasm'),('夸','praise'),('语气','delivery; pragmatic tone'),('小名','childhood nickname'),('出口','exit'),('线索','clue')],place='Close friends meeting at a café',context='One friend is ten minutes late; their shared history makes a dry joke intelligible.',turns=[('你今天可真早。','You are really early today.','Acknowledge lateness and explain briefly',['我晚了十分钟，对不起，走错出口了。']),('这件外套怪好看的。','This coat is quite nice.','Accept a casual compliment',['谢谢，今天第一次穿。']),('给你一个迟到奖？','An award for being late?','Decline playfully between close friends',['才不要呢，下次我早点来。'])],usage=[('Repair a joke that lands badly','我刚才开玩笑的，不过那句说得不合适。','I was joking, but that line was not well chosen.','Acknowledge your wording instead of claiming the other person must enjoy it.'),('Welcome an anxious newcomer','没关系，先坐吧，我告诉你刚才说到哪儿。','It is okay; sit down and I will tell you where we got to.','This responds to the actual missed information rather than copying close-friend banter.')],tasks=practice([(D[1][0],D[1][1],'The person arrived ten minutes before the meeting.',False,'They explicitly say they are ten minutes late.'),(R[2][0],R[2][1],'The narrator repeats the same teasing line to the new classmate.',False,'They choose 没关系，先坐吧 instead.')],[('还没吃怎么夸？','How can I praise it without trying it?',['也是，你先尝一个。','对，你已经吃了十个。','不用尝，没吃过也已经知道味道。'],0,'The reply accepts that tasting comes before judging.'),('这句一定是在生气吗？','Does this line definitely show anger?',['不一定，要看前后发生了什么。','对，只要有可真就生气。','只要有可真就一定在夸，从来不会生气。'],0,'The wording alone does not establish the emotion.')],[('这件外套怪好看的。','This coat is quite nice.','怪'),('我才不要这个奖呢。','I do not want this award.','才')],[[(V[i][3],V[i][4]) for i in [1,4,8]],[(V[i][5],V[i][6]) for i in [6,10,13]]]),review='Native review: playful force of 可真早/才不要呢, 怪好看的 regional familiarity and the award joke. The sincerity of the coat comment is supported by explicit wording; no inferred emotion score is claimed. 语音 includes a voice-message usage alongside speech sounds; check platform/register fit.')
spec['glosses'].append(('骗人','deceive; lie to someone'))
write(4,11,spec,publish='--publish' in sys.argv)
