"""Original verse: interpret images, then rehearse words without losing meaning."""
import sys
from advanced_core import write,rows,words,q,card,practice
V=words('''
优美|beautiful; graceful|đẹp; thanh nhã|她的声音很优美。|Her voice is beautiful.|这篇文章的语言优美，但不难懂。|This article uses beautiful language without being hard to understand.
影子|shadow|bóng|灯下有两个人的影子。|There are two people’s shadows under the light.|太阳快落山了，树的影子越来越长。|The sun is setting and the tree’s shadow is growing longer.
浅|shallow; light in colour|nông; nhạt|这条河很浅，可以看见河底。|This river is shallow; you can see the bottom.|我想买一件颜色浅一点的外套。|I’d like a coat in a lighter colour.
演唱|sing; perform a song|biểu diễn bài hát|今晚由她演唱最后一首歌。|She’ll sing the final song tonight.|这首歌第一次公开演唱时，他还很年轻。|He was very young when he first sang this song in public.
录音|record sound; sound recording|thu âm; bản thu|我想录音，听听哪里唱得不清楚。|I’d like to record myself and hear which parts aren’t clear.|这段录音只有一分钟。|This recording is only a minute long.
重复|repeat|lặp lại|这句话请再重复一次。|Please repeat this sentence once more.|我不想每天重复同样的错误。|I don’t want to repeat the same mistakes every day.
效果|effect; result|hiệu quả|换了位置以后，录音效果好多了。|The recording sounds much better after we moved.|这个方法的效果要过几天才能看出来。|It’ll take a few days to see how well this method works.
轻|light; gentle|nhẹ|这个包很轻，你拿吧。|This bag is light; you can carry it.|关门轻一点，孩子在睡觉。|Close the door gently; the child is asleep.
深|deep; dark in colour|sâu; đậm|这条河中间很深。|The middle of this river is deep.|深蓝色那件更适合你。|The dark blue one suits you better.
温暖|warm|ấm áp|冬天的阳光照在身上很温暖。|The winter sunlight feels warm on my skin.|这封信让我感到温暖。|This letter made me feel cared for.
静|quiet; still|yên tĩnh|屋里很静，只听见钟的声音。|The room is quiet; only the clock can be heard.|请让孩子静一会儿。|Please let the child have a quiet moment.
感情|feelings; emotional attachment|tình cảm|他们认识很久了，感情很好。|They’ve known each other a long time and are very close.|唱得很准，却没什么感情。|The singing is accurate but has little feeling.
声音|sound; voice|âm thanh; giọng|我听见楼下有人说话的声音。|I heard people talking downstairs.|你的声音太小，我听不清。|Your voice is too quiet for me to hear clearly.
动作|movement; action|động tác|这个动作先慢慢练。|Practise this movement slowly first.|她的动作很快，转眼就收好了。|She moved quickly and had everything packed in a moment.
暗|dark; dim|tối|这边太暗，看不清字。|It’s too dark here to read the words.|天还没完全暗，我们出去走走吧。|It isn’t completely dark yet; let’s take a walk.
纯|pure; unmixed|thuần; nguyên chất|这件衣服是纯棉的。|This garment is pure cotton.|我想点一杯纯果汁，不加水。|I’d like pure fruit juice with no water added.
''')
D=rows('''
这两句你已经重复好多遍了，还没唱顺？|You’ve repeated those two lines so many times. Still not smooth?
字我都认识，可是一跟音乐就来不及。|I know all the words, but I can’t keep up with the music.
先别放音乐。把它当成一句话，读给我听。|Leave the music off for now. Treat it as a sentence and read it to me.
“把歌声留在窗边，把明天带回来。”明天怎么带回来？|“Leave the song by the window; bring tomorrow back.” How can you bring tomorrow back?
我觉得是在说想再见到那个人。不是有人真的拿着一个明天。|I think it means wanting to see someone again. Nobody’s literally carrying a tomorrow.
所以这句不是在讲一个动作？|So it isn’t describing an actual action?
有动作的样子，但意思得连着前面的“等你”看。|It looks like an action, but you need to read it with the earlier “waiting for you.”
懂了。那我先读清楚，再试着唱，行吗？|Got it. I’ll read it clearly first, then try singing. Okay?
行。录一小段就好，别一开始就从头唱到尾。|Sure. Just record a short part. Don’t try the whole thing from the start.
你听的时候不许笑。|You’re not allowed to laugh when you listen.
那要看你唱什么了。我只能保证认真听。|That depends on what you sing. I can only promise to listen properly.
好吧，认真听也行。先帮我看看这两个字。|Fine, listening properly will do. Help me check these two characters first.
''')
R=rows('''
第一次练这段歌时，我以为只要每个字都认识，就能跟着唱。结果音乐一响，我连第一句都没唱完，后面的字已经来了。|When I first practised this verse, I thought knowing every character would let me sing along. Once the music started, I hadn’t finished the first line before the next words arrived.
我关掉音乐，先读歌词。里面有窗边的灯、雨后的影子，还有一个人在等朋友回来。那些东西不难理解，可是最后两句不能只按字面看。|I switched off the music and read the words. There was a light by a window, a shadow after rain and someone waiting for a friend. Those details were clear, but the last two lines needed more than a literal reading.
朋友问我：“前面谁在等谁？”我才发现自己一直注意快不快，没有想过这段到底在说什么。|My friend asked, “Who is waiting for whom earlier?” I realised I’d only been thinking about speed, not what the verse was saying.
我们把八句分成四小段。我先读一句，讲清意思，再跟着音乐试一次。遇到连在一起的几个字，就单独重复，而不是每次都从头开始。|We divided the eight lines into four short sections. I read a line, explained its meaning and then tried it with the music. I practised difficult clusters separately instead of restarting each time.
后来我录了两次。第一次声音太小，第二次字清楚了，速度却还是有点慢。朋友没有说我已经唱好了，只指出我这次没有漏掉“等你”。|Later I made two recordings. The first was too quiet; in the second the words were clear but still a little slow. My friend didn’t say I’d mastered it, just that I hadn’t missed “waiting for you” this time.
现在我仍然会错，不过知道下一次要练哪一小段了。先懂意思再练速度，比把不懂的声音唱得很快更有用。|I still make mistakes, but I know which short section to practise next. Understanding first and then practising speed is more useful than singing unclear sounds quickly.
''')
M=rows('''
雨停以后，路还没干。|After the rain stops, the road is still wet.
你的影子，留在门前。|Your shadow stays in front of the door.
窗边的灯，亮了一晚。|The light by the window shines all night.
我等你说，明天再见。|I wait for you to say, “See you tomorrow.”
别让一句话，走得太远。|Don’t let a sentence wander too far.
有些想念，没说也听见。|Some longing can be heard even without words.
把歌声留在窗边。|Leave the song by the window.
把明天带回来。|Bring tomorrow back.
''')
G=[
card('一…就…','Describe an immediate trigger','The event after 一 triggers the result after 就. Subjects may differ. This pattern is about the relationship between events, not a promise that practice succeeds.','音乐一响，我就跟不上了。|As soon as the music starts, I can’t keep up.\n她一到家就给我打电话。|She calls me as soon as she gets home.','一音乐响，我就跟不上了。','音乐一响，我就跟不上了。','Put 一 immediately before the triggering verb.'),
card('把 + object + result/location','Track what happens to a known object','把 introduces a specific affected object before a verb with a result, location or other completion. In a verse the object or result can be figurative; the grammar alone does not make the image literal.','把录音发给我。|Send me the recording.\n把这句话读清楚。|Read this sentence clearly.','把录音发。','把录音发给我。','In this request, give the destination rather than leaving the action incomplete.'),
card('不是…而是…','Correct a misunderstanding of meaning','Reject one interpretation and supply the more fitting one. Keep the two clauses comparable.','这不是说明天是一件东西，而是在说还想再见。|It doesn’t mean tomorrow is an object; it means wanting to meet again.\n我不是不练，而是想先弄懂。|It isn’t that I won’t practise; I want to understand first.','我不是想先弄懂，而是想先弄懂。','我不是不练，而是想先弄懂。','Identical alternatives do not clarify the misunderstanding.'),
card('先…再… / 每次都…','Sequence a repeatable practice routine','先 and 再 order actions. 每次都 says an action happens on every occasion; it does not itself mean the action is useful.','先读清楚，再跟音乐。|Read clearly first, then try with the music.\n别每次都从头开始。|Don’t start from the beginning every time.','先跟音乐，再读清楚，所以第一步是读。','先读清楚，再跟音乐。','The stated first step must match the order of the clauses.'),
]
spec=dict(title=('Understand the verse before rushing it','先听懂，再跟着唱'),goals=['Explain a short original verse using clues from nearby lines','Distinguish a poetic image from a literal event','Choose a small practice segment and describe what improved'],vocabulary=V,grammar=G,dialogue=(D,[q('gist','What does the friend suggest first?','Read the words as speech without music','Perform the whole song immediately','Memorise sounds without checking meaning'),q('detail','What does the listener promise?','To listen carefully','Never to laugh under any circumstances','To make the recording professionally'),q('inference','Why refer to the earlier “waiting for you”?','It gives context for the figurative final line','It proves tomorrow can be carried','It supplies the price of the song')]),reading=(R,[q('gist','What changes in the narrator’s practice?','Meaning and short sections come before speed','Only full performances are used','Recordings are permanently avoided'),q('detail','Which phrase is no longer missed in the second recording?','等你','别笑','快一点'),q('inference','What remains difficult?','Matching the pace','Recognising any character at all','Finding someone willing to hear a recording')]),mediaTitle='Original verse: the window light',media=(M,[q('detail','Who is waiting for a farewell about tomorrow?','The narrator','A person buying a lamp','An unnamed train driver'),q('inference','Which reading best fits “把明天带回来”?','Hope for another meeting','A literal instruction to carry a date','A claim that the rain will never stop')]),glosses=[('歌词','song lyrics'),('字面','literal wording'),('漏掉','miss out; omit'),('从头','from the beginning'),('想念','miss; long for'),('保证','promise; guarantee'),('纯棉','pure cotton'),('果汁','fruit juice'),('河底','river bottom')],place='Practising an original verse with a friend',context='One friend can read the words but loses the line when music begins.',turns=[('为什么先不放音乐？','Why leave the music off first?','Explain the first step',['我想先读清楚，弄懂意思。']),('你要录整首吗？','Are you recording the whole song?','Choose a manageable section',['不用，我先录这两句。']),('最后一句是什么意思？','What does the last line mean?','Give an interpretation with a clue',['前面说在等朋友，所以我觉得是希望再见。'])],usage=[('Offer a specific listening request','帮我听听这两个字清不清楚。','Help me hear whether these two characters are clear.','The request asks about a defined segment rather than an invented overall pronunciation score.'),('Mark an interpretation','我觉得这里是在说想再见。','I think this means wanting to meet again.','我觉得 marks your interpretation; nearby lines provide the evidence.')],tasks=practice([(D[8][0],D[8][1],'The friend recommends recording a short section.',True,'录一小段 explicitly recommends a short section.'),(R[4][0],R[4][1],'The second recording was already perfectly at the musical pace.',False,'It was clearer but still a little slow.')],[('字能读清楚，一跟音乐就来不及。怎么办？','I can read the words clearly, but fall behind with the music. What should I do?',['先读这两句，再试着跟。','既然能读清楚，就已经完全跟上音乐了。','不用看意思，把整首加快唱完就行。'],0,'The reply offers the manageable practice described.'),('前面说在等朋友，最后说把明天带回来。是什么意思？','Earlier the narrator waits for a friend, then says bring tomorrow back. What does that mean?',['连着前面的等你看，可能是在说想再见。','是在要求朋友把一个日期拿在手里。','是在确定朋友已经回来，再也不用等。'],0,'The reply uses a contextual interpretation rather than literal objects.')],[('我想先读清楚，再跟音乐。','I want to read clearly first, then try with the music.','再'),('这段录音只有一分钟。','This recording is only a minute long.','录音')],[[(V[i][3],V[i][4]) for i in [0,1,2]],[(V[i][5],V[i][6]) for i in [6,8,10]]]),review='Native review: original lyric images, clause rhythm and playful promise to listen. The final-image answer is an evidence-based interpretation, not the sole possible artistic meaning. Recordings are learner-owned; Sayo assets read these lines as speech, not a musical performance. Speed practice never substitutes for lexical tones in ordinary conversation.')
spec['glosses'].extend([('从头唱到尾','sing from beginning to end'),('遇到','encounter; come across')])
write(4,5,spec,publish='--publish' in sys.argv)
