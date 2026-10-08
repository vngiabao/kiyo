"""Offer believable reassurance and precise feedback after a difficult performance."""
import sys
from advanced_core import write,rows,words,q,card,practice
V=words('''
安慰|comfort; reassure|an ủi|谢谢你安慰我，不过我想先安静一会儿。|Thanks for comforting me, but I’d like a quiet moment first.|她没有急着安慰，只问我想不想说。|She didn’t rush to reassure me; she just asked if I wanted to talk.
耐心|patience; patient|kiên nhẫn|你能耐心听完，再说哪里要改吗？|Could you listen patiently to the end before saying what to change?|他很有耐心，同一句教了我三次。|He was patient and taught me the same sentence three times.
心态|mindset; attitude|tâm thế|我想换个心态，把这次当作练习。|I’d like to treat this as practice with a different mindset.|比赛前，她的心态比以前平稳。|Her mindset was steadier than before the competition.
心疼|feel for someone; feel distressed about|xót; thương|看你忙了这么久，我有点心疼。|I feel for you after seeing how long you’ve been busy.|她很心疼那只受伤的小猫。|She felt sorry for the injured kitten.
鼓励|encourage|khuyến khích|老师鼓励我再试一次。|The teacher encouraged me to try again.|你的鼓励让我愿意把话说完。|Your encouragement made me willing to finish what I was saying.
打击|blow; discourage; strike|đả kích; cú sốc|这次结果对他的打击很大。|This result was a major blow to him.|我不是想打击你，只是提醒时间不够。|I’m not trying to discourage you; I’m pointing out there isn’t enough time.
失误|error; mistake|sai sót|我在第二句有一个失误。|I made a mistake in the second line.|这次失误没有改变最后的结果。|This error didn’t change the final outcome.
失望|disappointed|thất vọng|没有达到自己的目标，我有点失望。|I’m a little disappointed I didn’t reach my own goal.|她失望地把没用上的票收起来。|She put away the unused ticket in disappointment.
自豪|proud|tự hào|我为她坚持完成这件事感到自豪。|I’m proud of her for seeing it through.|这座城市的居民为自己的传统自豪。|Residents of this city are proud of their traditions.
勇气|courage|can đảm|第一次上台，我用了很大勇气。|It took courage for me to go on stage the first time.|我终于有勇气问那个问题了。|I finally had the courage to ask that question.
吃力|strenuous; have difficulty|vất vả; khó khăn|这段太快，我跟得很吃力。|This part is so fast I struggle to keep up.|他一个人搬这个箱子很吃力。|He struggles to carry this box alone.
恢复|recover; restore|hồi phục; khôi phục|休息以后，我恢复了一点精神。|After resting, I got some energy back.|丢掉的文件能恢复吗？|Can the lost file be restored?
缺乏|lack|thiếu|我不是不想说，只是缺乏练习机会。|I do want to speak; I just lack chances to practise.|这个计划缺乏具体的时间安排。|This plan lacks a specific schedule.
难以|difficult to|khó mà|第一次听，难以判断他是什么意思。|On first hearing, it’s difficult to judge what he means.|我难以接受只凭一句话就下结论。|I find it hard to accept a conclusion based on one sentence.
渴望|long for; strongly desire|khao khát|她渴望有一次自己选择的机会。|She longs for a chance to choose for herself.|我很渴望和大家自然地聊起来。|I really want to start chatting naturally with everyone.
无奈|helpless; no good alternative|bất lực|他无奈地说，票已经卖完了。|He said helplessly that the tickets had sold out.|我有点无奈，只好等下一班。|I had no good option but to wait for the next service.
受不了|cannot bear|không chịu nổi|我受不了大家同时说话，听不清。|I can’t cope with everyone talking at once; I can’t hear clearly.|她受不了屋里这么热，打开了窗。|She couldn’t bear the heat in the room and opened the window.
担心|worry|lo lắng|我担心自己又会漏掉第二句。|I’m worried I’ll miss the second line again.|他担心朋友找不到地方，就发了地图。|He worried his friend wouldn’t find the place and sent a map.
适应|adapt; get used to|thích nghi|我还在适应台上的声音。|I’m still getting used to the sound on stage.|她花了一周才适应新的时间表。|It took her a week to adapt to the new schedule.
依然|still; remain|vẫn|练完以后，我依然有点紧张。|After practising I was still a little nervous.|天气变了，他的计划依然没有变。|The weather changed but his plan stayed the same.
主观|subjective|chủ quan|这只是我的主观感受，你可以不一样。|This is only my subjective impression; yours may differ.|只凭第一印象判断，容易太主观。|Judging only by a first impression can be too subjective.
预期|expectation; expected|dự kiến; kỳ vọng|这次效果比我的预期好。|The result was better than I expected.|预期太高，有时更容易失望。|Sometimes high expectations make disappointment more likely.
情形|situation; circumstances|tình hình|当时是什么情形，你再说详细一点。|Tell me more about what was happening at the time.|换一种情形，同一句话可能不同。|In a different situation the same sentence may mean something else.
鼓掌|applaud; clap|vỗ tay|演出结束以后，大家一起鼓掌。|Everyone applauded after the performance.|他还没说完，后面已经有人鼓掌了。|Someone at the back started clapping before he’d finished speaking.
''')
D=rows('''
你怎么一个人坐在这里？大家还在里面聊天。|Why are you sitting here alone? Everyone’s still chatting inside.
我想先出来一会儿。刚才第二句唱错了，后面差点接不上。|I wanted a moment outside. I got the second line wrong and nearly lost the next part.
我听见你停了一下，不过后来接上了。|I heard you pause, but you picked it up again.
你不用安慰我，我知道和练的时候不一样。|You don’t need to reassure me. I know it wasn’t like rehearsal.
我没说没有错。我是说你没停在那里，后面唱完了。|I’m not saying there was no mistake. I’m saying you didn’t stop there; you finished the rest.
这点倒是。可我准备了那么久，还是有点失望。|That’s true, but I prepared so long and I’m still a little disappointed.
紧张归紧张，你还是站上去了。你第一次来，只在后面听呢。|Nervous or not, you still went on stage. The first time you came you only listened at the back.
别从我第一次来开始讲了。我就想知道第二句怎么改。|Don’t start from the first time I came. I just want to know how to fix the second line.
好，现在听录音，还是吃完东西再听？|Okay. Listen to the recording now, or after some food?
吃完再听吧。我现在一听见自己的声音就想关掉。|After food. Right now hearing my own voice makes me want to switch it off.
行。等会儿只听那两句，不用把整段一直重复。|Sure. Later we’ll listen only to those two lines, not keep repeating the whole thing.
你觉得是字没读准，还是跟音乐太急？|Do you think the word was wrong, or I rushed with the music?
我得再听一次才敢说。刚才只是听见你漏了两个字。|I need another listen before saying. I only heard you miss two characters.
这样说我反而放心。你要是说全部都完美，我才不信。|That actually reassures me. If you said everything was perfect, I wouldn’t believe it.
放心，我没那么会夸人。|Don’t worry; I’m not that good at lavish praise.
这个不用练。你先帮我拿点水吧。|No need to practise that. Get me some water first.
好。要不要我跟大家说你等会儿回去？|Okay. Shall I tell the others you’ll be back later?
说一下吧，别让他们以为我直接走了。|Yes, so they don’t think I’ve left altogether.
''')
R=rows('''
去唱歌活动以前，我在家练了十几次。音乐放慢时，每一句都能接上，我就以为到了现场也会一样。那天轮到我，站到前面才发现，听见的声音和房间里不太一样，手里拿着话筒，也不知道该看哪里。|Before the singing event I rehearsed more than ten times at home. I could keep up with every line when the music was slowed, so I expected the same at the event. Standing at the front, I found the sound different from my room and didn’t know where to look while holding the microphone.
第二句里有两个字，我还没唱完，音乐已经往下走了。我停了一下，差点接不上下一句。幸好前面的朋友用手给我指了开始的位置，我又跟了上去，最后唱完了整段。坐下以后，我只记得那两秒，觉得前面准备的都没有用。|Two characters in the second line fell behind the music. I paused and nearly missed the next line. A friend pointed to where I should restart, and I picked it up and finished the section. Afterwards I remembered only those two seconds and felt all my preparation had been useless.
我到门外坐了一会儿，朋友跟出来问怎么了。他说我后来接上了，我却以为他只是安慰。我们说了几句，我才听清楚：他并没有说我唱得完美，只说出了一个我自己没注意的事实。我确实没有在失误的地方结束。|I sat outside briefly, and a friend came to ask what was wrong. When he said I’d picked it up again, I thought he was merely comforting me. After talking I understood: he hadn’t called it perfect, just named a fact I’d overlooked. I hadn’t ended at the mistake.
我们先去吃东西。我不想刚坐下就反复听自己的录音，他也没有催我。吃完以后，我们找了个安静的地方，只听第二句和后面接上的一句。听的时候，我发现那两个字没跟上，但后面并不像自己记得的那么乱。|We ate first. I didn’t want to keep hearing my recording immediately, and he didn’t rush me. Afterwards we found a quiet place and listened only to the second line and the next one. The two characters had fallen behind, but the following line wasn’t as chaotic as I remembered.
朋友让我先按普通说话的方式读那两句，再试着跟音乐。我把快的地方分开练，没有每次从头开始。录音里哪里少了字，我们就停在哪里；不是所有地方都用同一个办法重做。这样练十分钟以后，我至少知道下一次要注意哪个位置。|My friend suggested reading the lines as ordinary speech first, then trying with the music. I practised the fast part separately instead of restarting every time. We stopped where the recording had missing characters rather than redoing every part the same way. After ten minutes I knew which spot to focus on next.
回去时，活动还没结束。有个新朋友问我是不是下次也来。我没有马上说一定会唱得更好，只说想再试一次，也问他平时怎么练。他说自己第一次更紧张，拿着话筒还忘了音乐已经开始。听见这个，我终于笑了，不是因为他的失误好笑，而是觉得自己不那么孤单了。|The event was still going when we returned. A new friend asked whether I’d come next time. I said I’d like another try and asked how he practised. He said he’d been even more nervous his first time, forgetting the music had started while holding the microphone. I finally laughed—not at his mistake, but because I felt less alone.
那天回家，我依然觉得第二句要练，却没有再把整次经历都叫作失败。能完成、能接受别人帮一下、能把不知道的地方问清楚，和唱得流畅是不同的进步。它们不能代替下一次练习，但让我愿意继续去，也让我认识了愿意一起练的人。|Going home, I still knew the second line needed practice, but I no longer called the whole experience a failure. Finishing, accepting a little help and asking about uncertainty were different kinds of progress from fluent singing. They didn’t replace practice, but made me want to return and introduced me to people willing to practise together.
''')
P=rows('''
这次活动由我负责安排顺序，一共有十二个人准备上台。有些人认识很久，有些第一次来。开始以前，我问大家想完整唱一段，还是只试自己选的几句。两个人选了短的部分，其他人选了整段，我们照着他们的选择安排，没有要求每个人一样长。|I arranged the order for twelve people at this event. Some were familiar faces and others were new. Before starting, I asked whether they wanted a full section or a few selected lines. Two chose short parts, and the others chose full sections. We used their choices rather than requiring identical lengths.
一个第一次上台的朋友唱到第二句时停了一下，前排的人指了开始的位置。他后来接上了，但走下来时看着地面，没有和旁边的人说话。我过去问他要不要喝水。他说先出去一会儿，另一个熟悉他的朋友陪他走了。我就告诉大家，下一位准备，不把所有人的注意都留在他身上。|A first-time performer paused in the second line, then restarted after someone in front pointed to the entry. He looked down afterwards and didn’t talk. I asked if he’d like water. He wanted a moment outside, and a friend went with him. I moved to the next performer rather than keeping everyone’s attention on him.
后来有人问，刚才鼓掌是不是表示让他停下来。我说自己鼓掌是在他唱完以后，是谢谢他参加。现场每个人坐的位置不同，听见和看见的也可能不同，所以有疑问可以直接问，不用从一阵掌声里猜所有人的想法。那个提问的人说，他上次也把别人的反应理解错了。|Later someone asked whether the clapping had meant he should stop. I said I’d clapped after he finished to thank him for taking part. People sat in different places and might hear and see different things; they could ask rather than guess everyone’s intention from applause. The questioner said he’d misread a reaction at the previous event too.
吃东西的时候，几个朋友开始讲自己的第一次。有个人说，他本来想表现得很自然，一拿起话筒却把介绍自己的句子忘了。另一个说，她练得最多的地方没有错，平时觉得最容易的一句反而漏了。大家没有照着一种经历来安慰，而是把自己的具体情况说出来，话题就从一个人的失误变成了共同经历。|Over food, people shared their first attempts. One had wanted to seem natural but forgot his introduction on picking up the microphone. Another made no error in the most-practised section but missed an apparently easy line. Their specific accounts shifted the conversation from one person’s mistake to shared experiences.
我想起自己以前带活动，常说“别紧张，一定没问题”。有时这句话能让气氛轻松一点，有时对方还是会紧张，甚至不知道出了问题该怎么办。这次我试着多说一点实际安排：可以选短的部分；忘了可以重新找开始的位置；结束以后，可以自己决定什么时候听录音。|I remembered telling people, “Don’t be nervous; it’ll definitely be fine.” Sometimes that relaxed the atmosphere; sometimes they remained nervous and didn’t know what to do if something went wrong. This time I gave practical options: a shorter part, finding an entry again if they forgot, and choosing when to listen to the recording afterwards.
活动结束前，那位出去休息的朋友回来了。他问下次还能不能带同一段，又说自己已经找到了要练的位置。我把下一次的时间发给他，没有替他决定要唱多长。另一个人听见，也想和他一起练两句，于是他们交换了联系方式。|Before the event ended, the person who’d rested outside returned. He asked whether he could bring the same section next time and said he’d found what to practise. I sent the next date without choosing his performance length for him. Someone else offered to practise two lines together, and they exchanged contact details.
收好东西以后，我觉得这次最值得留下的，不只是舞台上的声音，还有这些短短的对话。有人愿意承认紧张，有人问清楚掌声的意思，有人找到下一次一起练的伙伴。下次活动的顺序还没有定，我会再问大家想做什么，而不是拿今天的选择直接替他们报名。|After packing up, I valued the short conversations as well as the sounds on stage: admitting nerves, clarifying applause and finding a practice partner. The next order wasn’t fixed yet. I’d ask what people wanted rather than automatically sign them up based on today’s choices.
''')
M=rows('''
你第一次真的忘了音乐已经开始？|Did you really forget the music had started your first time?
真的。我还在问大家能不能听见我。|Really. I was still asking if everyone could hear me.
大家怎么说？|What did they say?
有人说听见了，还说音乐也听见了。|Someone said yes—and that they could hear the music too.
这个提醒挺清楚的。|That was a pretty clear reminder.
我当时没听懂，还问是不是太大声。|I didn’t understand then and asked if it was too loud.
所以后来呢？|So what happened then?
后来有人把音乐停了，说重新来。我才明白。|Someone stopped the music and said we’d restart. Only then did I understand.
你还能笑着讲，看来已经不怕了。|You can laugh about it now. Looks like you’re not afraid anymore.
谁说不怕？讲以前的很容易，等会儿轮到我还是怕。|Who says I’m not afraid? Talking about the past is easy; I’m still scared when my turn comes.
那我等会儿提醒你音乐开始了。|Then I’ll remind you when the music starts.
好，这次我先唱，唱完再问听不听得见。|Okay. This time I’ll sing first and ask if they can hear me afterwards.
''')
G=[
card('X归X，Y…','Concede one fact while keeping another judgment separate','Repeating X around 归 acknowledges that issue before giving a different point. In speech, the following clause often uses 但/还是. It does not mean X is unimportant.','紧张归紧张，你还是唱完了。|Nervous or not, you still finished.\n贵归贵，这次我还是想买。|It is expensive, but this time I still want to buy it.','紧张归紧张，所以紧张不存在。','紧张归紧张，你还是唱完了。','The first clause acknowledges the feeling; it does not deny it.'),
card('再…也…','State a continuing intention despite an extreme degree','再 before an adjective or mental verb supplies the challenging degree; 也 introduces what still holds. The statement can be a personal intention rather than a guarantee of achievement.','再紧张，我也想把它唱完。|However nervous I am, I still want to finish it.\n这段再快，我也可以先练两句。|However fast this section is, I can start by practising two lines.','再紧张，我也想把它唱完，所以我已经唱完了。','再紧张，我也想把它唱完。','An intention to finish does not establish that finishing has already happened.'),
card('动词 / 形容词 + 得 + clause','Describe an effect on a person','After 得, a clause can name the effect of the manner or degree, including a different subject. Compare a degree adjective with a consequence rather than inserting 得 anywhere.','音乐快得我都跟不上了。|The music is so fast I cannot keep up.\n我紧张得手心都湿了。|I am so nervous my palms are damp.','音乐得快我都跟不上了。','音乐快得我都跟不上了。','Put 得 after the adjective 快 and before the consequence clause.'),
card('在…看来','Attribute an assessment to a perspective','在 plus a person and 看来 frames an opinion from that standpoint. It leaves room for others to notice different things; evidence still needs to be named.','在我看来，后面接上了也是进步。|In my view, picking it up afterwards is progress too.\n在她看来，先休息再听比较好。|She thinks resting before listening is better.','在我看来，所以所有人都一定同意。','在我看来，后面接上了也是进步。','A framed opinion does not prove agreement from everyone.'),
card('先…还是…再…?','Offer a choice about sequence','还是 presents alternatives in a question. Let the actual answer settle which sequence will be followed rather than assuming the first option was chosen.','现在听，还是吃完东西再听？|Listen now, or after eating?\n先说问题，还是先听录音？|Discuss the problem first, or listen to the recording first?','现在听或者吃完再听？所以我们已经选了现在。','现在听，还是吃完东西再听？','An alternatives question does not itself establish a choice; the scene’s reply does.'),
]
spec=dict(title=('Comfort that makes room for the truth','紧张归紧张，你唱完了'),goals=['Respond to disappointment without erasing the actual mistake','Ask whether a friend wants company, rest or specific feedback','Compare a performer’s memory with observed details and another account'],vocabulary=V,grammar=G,
dialogue=(D,[q('gist','How does the friend respond to disappointment?','Names finishing after the pause without calling the singing perfect','Claims no error occurred','Demands an immediate complete replay'),q('detail','When does the performer want to hear the recording?','After eating','Before leaving the stage','Only after a year'),q('inference','Why does the specific comment feel more trustworthy?','It admits a gap while identifying a real recovery','It promises every future attempt will be perfect','It replaces listening with an invented mark')]),
reading=(R,[q('gist','What changes in the narrator’s view?','The mistake remains, but the whole experience is no longer called a failure','All practice is declared unnecessary','The missed words are denied'),q('detail','What gets replayed in the quiet place?','The second line and the following line','Every participant’s entire performance','Only the introduction before the music'),q('inference','Why does the narrator laugh at the new friend’s account?','It makes the experience feel less lonely','It proves the new friend can never sing','It shows everyone deliberately mocked the performer')]),
pairedTitle='The organiser’s view',pairedReading=(P,[q('gist','What does the organiser value?','Practical options and the conversations that help people continue','Identical performance length for everyone','Keeping attention on one mistake all evening'),q('detail','How many choose only a short part?','Two','Twelve','None'),q('inference','What do both accounts suggest about support?','Specific observations and choices can help more than blanket reassurance','A pause means the performer should permanently leave','A recording must always be heard immediately')]),
mediaTitle='Can you hear me?',media=(M,[q('detail','What does the new friend initially fail to notice?','That the music has already started','That the microphone is a train ticket','That the event was cancelled'),q('inference','What does laughing about the past not establish?','That the friend is no longer nervous about the next turn','That the friend has a memory of the earlier event','That someone once stopped the music to restart')]),
glosses=[('话筒','microphone'),('手心','palm of the hand'),('湿','damp; wet'),('前排','front row'),('掌声','applause'),('气氛','atmosphere'),('伙伴','partner; companion'),('催','urge; rush someone'),('漏掉','omit; miss out'),('流畅','fluent; smooth'),('孤单','lonely'),('反应','reaction'),('上台','go on stage')],
place='Outside a community singing event',context='A first-time performer has paused in the second line, recovered, then felt disappointed.',turns=[('我准备了这么久，还是唱错了。','I prepared so long and still got it wrong.','Acknowledge the mistake and a specific recovery',['第二句有停顿，不过你后面接上了，唱完了。']),('你要我马上听录音吗？','Do you want me to hear the recording now?','Offer a real choice',['你想现在听，还是先吃点东西再听？']),('你觉得到底哪里错了？','What exactly do you think went wrong?','Limit feedback to what you heard',['我听见漏了两个字，其他的得再听一次。'])],
usage=[('Ask what help is wanted','你想说说，还是先安静一会儿？','Would you like to talk, or have a quiet moment first?','Offer alternatives and follow the reply rather than assuming reassurance is wanted.'),('Identify an observation','我听见第二句停了一下，后来又接上了。','I heard a pause in the second line, followed by a recovery.','A concrete observation is different from an unsupported overall quality score.'),('Leave a social return open','我告诉大家你等会儿回去，行吗？','May I tell the others you will be back later?','Check the person’s plan before sending that message.')],
tasks=practice(
[(D[4][0],D[4][1],'The friend says the performance contained no mistake.',False,'The friend explicitly says they are not claiming that.'),(D[12][0],D[12][1],'The friend wants another listen before judging why it happened.',True,'They say they need another listen.'),(R[3][0],R[3][1],'The following line sounded as chaotic as the narrator had remembered.',False,'The narrator says it was less chaotic.'),(P[0][0],P[0][1],'All twelve participants must choose the same length.',False,'Two choose short parts and the others full sections.')],
[('第二句漏了两字，后面接上了。你不用说全部都完美。','Two words were missed, then you picked it up. You do not need to call it all perfect.',['我没这样说，只是听见你后来接上了。','对，你刚才说从头到尾都没漏字。','你说后面一直没接上，我也听到了。'],0,'The reply distinguishes observation from blanket praise.'),('你说先吃东西再听。现在还没吃，想现在听吗？','You said to eat before listening. We have not eaten yet; would you like to listen now?',['吃完再听吧，先让我休息一下。','吃完了，我刚才已经把饭吃完。','我没说过先吃，刚才只说立即听。'],0,'The response chooses the later listening sequence.'),('我还在问大家听不听得见，音乐已经响了。开始了吗？','I am still asking whether people can hear me, but music is already playing. Has it started?',['已经开始了，我们停一下重新来。','还没响，我们还没放音乐。','已经结束了，不用重新开始。'],0,'The reply directly addresses the missed musical start.')],
[('紧张归紧张，你还是唱完了。','Nervous or not, you still finished.','归'),('音乐快得我都跟不上了。','The music is so fast I cannot keep up.','得'),('老师鼓励我再试一次。','The teacher encouraged me to try again.','鼓励')],
[[(V[i][3],V[i][4]) for i in [0,5,10]],[(V[i][5],V[i][6]) for i in [11,17,20]],[(V[i][3],V[i][4]) for i in [12,14,22]]]),
review='Native review: reassurance between familiar adults, self-deprecating 夸人 banter, X归X concession and performance vocabulary. Actual pause/recovery and two missed characters remain distinct from diagnosis of word accuracy or timing. Twelve participants, two shorter choices and the performer’s return are consistent across accounts. No voice recording or pronunciation grade is created by these fictional texts.')
spec['glosses'].extend([('秒','second, unit of time'),('详细','detailed'),('一阵','a burst or short spell')])
write(5,2,spec,publish='--publish' in sys.argv)
