"""Disagree about a film without treating a preference as a fact."""
import sys
from advanced_core import write,rows,words,q,card,practice
V=words('''
辩论|debate|tranh biện|这次辩论的题目是城市生活。|This debate is about city life.|我们在辩论中先说明自己的理由。|We explain our reasons first in the debate.
诚实|honest|trung thực|你诚实地告诉我，不喜欢也没关系。|Tell me honestly; it’s okay if you don’t like it.|他承认自己看错了，很诚实。|He honestly admitted he’d misread it.
避免|avoid|tránh|先问清楚，可以避免误会。|Asking first can avoid misunderstandings.|我想避免在大家忙的时候打电话。|I want to avoid calling when everyone’s busy.
片面|one-sided; incomplete|phiến diện|只看价格来评价，太片面了。|Judging only by price is too one-sided.|这篇介绍只说优点，比较片面。|This introduction is rather one-sided; it only mentions advantages.
结论|conclusion|kết luận|看完前面的部分，再下结论吧。|Watch the earlier parts before drawing a conclusion.|我们得到的结论不一样。|We reached different conclusions.
细节|detail|chi tiết|我想再看一遍这个细节。|I’d like to watch this detail again.|他记得见面时的很多细节。|He remembers many details of their meeting.
风格|style|phong cách|这个导演的风格比较安静。|This director has a fairly quiet style.|她不喜欢这家店的装修风格。|She doesn’t like this shop’s decorating style.
反映|reflect; report a problem|phản ánh|这部电影反映了小城里普通人的生活。|This film reflects ordinary life in a small town.|我已经向学校反映了这个问题。|I’ve reported this problem to the school.
争论|argue; disagreement|tranh luận|我们为最后那句话争论了半天。|We argued for ages about that final sentence.|先别争论，听听他怎么说。|Don’t argue yet; hear what he has to say.
期待|look forward to; expect|mong đợi|我很期待下周的演出。|I’m really looking forward to next week’s performance.|大家对新电影的期待不一样。|People have different expectations of the new film.
失望|disappointed|thất vọng|没买到票，我有点失望。|I’m a little disappointed I couldn’t get tickets.|我以为会再见到他，没想到又失望了。|I thought I’d see him again, but I was disappointed once more.
赞成|agree with; support an opinion|tán thành|我赞成先看完再讨论。|I agree we should finish watching before discussing it.|他不赞成把时间改到周一。|He doesn’t agree with moving it to Monday.
评价|evaluate; assessment|đánh giá|你怎么评价这个演员？|How would you assess this actor?|她的评价很具体，不只是说好看。|Her assessment is specific, not just “it’s good.”
演员|actor|diễn viên|这个演员以前演过老师。|This actor played a teacher before.|我记得演员的脸，却想不起名字。|I remember the actor’s face but can’t recall the name.
导演|director|đạo diễn|导演没有把最后的答案说出来。|The director didn’t give away the final answer.|我们看过同一个导演的两部电影。|We’ve seen two films by the same director.
观众|audience; viewer|khán giả|观众都安静下来，等演出开始。|The audience grew quiet, waiting for the performance.|有些观众喜欢最后那一段，有些不喜欢。|Some viewers like the final section; others don’t.
''')
D=rows('''
看完了？你怎么一句话都不说？|Finished? Why aren’t you saying anything?
我在想最后那个人到底回来没有。电影就这么结束了，有点失望。|I’m thinking about whether that person ever came back. The film just ends there. I’m a little disappointed.
我倒挺喜欢。她已经把该说的话说了，不一定非要再见面。|I actually liked it. She’d said what she needed to; they didn’t necessarily have to meet again.
可前面一直说等他，最后也没给个答案。|But she kept talking about waiting for him earlier, and we never got an answer.
答案不只是回没回来吧。她最后自己去了车站，没有再留在家里等。|The answer isn’t only whether he returned. At the end she went to the station herself instead of staying home waiting.
这点我没注意。我光看火车了，以为他会下来。|I missed that. I was only looking at the train, thinking he’d get off.
可以倒回去看看。她走到车站的时候，表情已经不一样了。|We can go back and watch. Her expression is already different when she reaches the station.
好。不过我还是觉得中间太慢。|Okay, but I still think the middle was too slow.
这个我同意。有两段我也差点没看下去。|I agree with that. I almost gave up during two sections too.
原来你也不是都喜欢。我还以为你要替导演解释每一分钟。|So you didn’t like everything either. I thought you were going to explain every minute on the director’s behalf.
哪有。我喜欢最后一段，又没说整部都好。|Of course not. I liked the last part; I didn’t say the whole thing was good.
那先看最后一段，再去吃饭。我现在只确定一件事：我饿了。|Then let’s rewatch the last part and get dinner. I am sure of just one thing right now: I am hungry.
''')
R=rows('''
我和朋友看完同一部电影，第一句话却完全不同。我说“终于结束了”，她说“最后那一段真好”。我们忍不住笑了，原来坐在一起也不代表期待一样。|My friend and I watched the same film but reacted differently. I said, “Finally over”; she said, “The last part was great.” We laughed: sitting together hadn’t made our expectations the same.
我想看的是两个人最后有没有再见。朋友注意的是女孩怎样从等别人回来，变成自己决定去哪里。我们看的不是两部电影，只是注意了不同的细节。|I wanted to know whether the two people met again. My friend noticed how the girl changed from waiting for someone to deciding where to go herself. We’d watched one film but focused on different details.
回看最后一段以后，我发现她说得有道理。女孩走进车站时没有拿那封一直留着的信。这个动作在前面出现过，所以不是随便加的一下。|After rewatching the last section, I saw her point. The girl entered the station without the letter she’d kept. That action had appeared earlier, so it wasn’t just an arbitrary extra gesture.
不过这没有让我突然喜欢整部电影。中间几段依然很慢，朋友也同意。我们把“有一个好细节”和“整部都好看”分开说，反而不用争论那么久。|That didn’t suddenly make me love the whole film. Some middle sections were still slow, and my friend agreed. Distinguishing one good detail from enjoying the whole film actually shortened the argument.
后来我写了几句话推荐给同学，没有只写“你一定喜欢”。我说它节奏慢，最后没有直接回答两个人是否再见，但人物的变化值得注意。喜欢明确结果的人，可能会和我一样失望。|Later I wrote a short recommendation for a classmate rather than simply saying, “You’ll definitely like it.” I said it was slow, didn’t directly answer whether they met again and had a character change worth noticing. People who want a definite outcome might be disappointed, as I was.
朋友说这个评价比我刚开始那句“没意思”诚实多了。我还是不想马上再看一遍，不过愿意听听其他观众看到了什么。|My friend said that assessment was much more honest than my initial “boring.” I still didn’t want an immediate rewatch, but I was willing to hear what other viewers had noticed.
''')
M=rows('''
你还是带着那封信？|Are you still carrying that letter?
今天没带。|Not today.
那你来车站做什么？|Then why have you come to the station?
买票，去我姐姐那儿。|To buy a ticket to visit my sister.
你不等他了？|You’re not waiting for him anymore?
他知道怎么找我。我不能一直坐在家里。|He knows how to find me. I can’t stay at home forever.
那我陪你买票。|Then I’ll come with you to buy the ticket.
好，顺便帮我看看几点还有车。|Okay. Help me check which trains are still available while we’re there.
''')
G=[
card('尽管…但是… / 即使…也…','Distinguish an actual concession from a hypothetical one','尽管 commonly accepts an actual fact and then gives a contrasting result. 即使 introduces an extreme or hypothetical condition; 也 keeps the result unchanged. Context, not translation alone, determines the reading.','尽管中间有点慢，但是最后一段很好。|Although the middle is slow, the final section is good.\n即使你不喜欢，也可以说说原因。|Even if you don’t like it, you can explain why.','即使我已经看完，所以我肯定没看。','尽管我已经看完，但是还没想好怎么评价。','The actual completion and the remaining uncertainty are compatible.'),
card('不一定 / 未必','Avoid claiming a result is guaranteed','These forms deny certainty, rather than directly asserting the opposite. 不一定会回来 leaves both return and non-return possible.','他不一定会回来。|He won’t necessarily return.\n大家未必有同样的期待。|People may not have the same expectations.','他不一定会回来，所以他一定不回来。','他不一定会回来，我还不知道。','Denying certainty does not establish the opposite as certain.'),
card('又没…','Reject an implied claim conversationally','又 before a negative often stresses that an accusation or assumption is unfounded. It can sound defensive, so the relationship and delivery matter.','我又没说整部都好。|I didn’t say the whole thing was good.\n我又没看过，怎么知道？|I haven’t even seen it; how would I know?','我又没说整部都好，所以我说了整部都好。','我喜欢最后一段，又没说整部都好。','The negative rejects the broader claim while preserving the limited preference.'),
card('反而','Mark a result opposite to an expectation','The context supplies an expected direction; 反而 presents a contrasting outcome. It does not simply mean “then”.','把不同意见说具体，反而少争论了。|Making our different views specific actually reduced the arguing.\n我想早点到，走错路反而迟到了。|I wanted to arrive early, but taking the wrong road made me late instead.','我早点出发，反而按时到了，因为这正是我预计的。','我想早点到，走错路反而迟到了。','The result must contrast with the relevant expectation.'),
]
spec=dict(title=('Same film, different expectations','你喜欢哪一段'),goals=['Give reasons for a film preference without dismissing another viewer','Separate an observed detail from an interpretation','Write a recommendation that names both strengths and limitations'],vocabulary=V,grammar=G,dialogue=(D,[q('gist','What do the viewers disagree about?','Whether the unresolved final section works','Whether they watched different films','How many tickets they bought'),q('detail','Which criticism do both accept?','Some middle sections are slow','No character reaches a station','Every minute is excellent'),q('inference','Why rewatch the final section?','One viewer missed a detail about the girl’s change','They want to erase their earlier discussion','The train timetable is an actual travel booking')]),reading=(R,[q('gist','What makes the later assessment more useful?','It distinguishes specific details from overall enjoyment','It promises everyone will enjoy the film','It copies the friend’s opinion without thought'),q('detail','What does the girl leave behind in the final section?','The letter','Her sister','Her train ticket already purchased'),q('inference','Who might find the film disappointing?','A viewer wanting a definite answer about the reunion','Every viewer who likes quiet films','Only the director')]),mediaTitle='The station decision',media=(M,[q('detail','Why does the girl come to the station?','To buy a ticket to visit her sister','To give the letter to a driver','To wait indefinitely at home'),q('inference','What does “我不能一直坐在家里” suggest?','She is choosing to act rather than only wait','She has already confirmed the man’s return','She has forgotten how to buy tickets')]),glosses=[('结尾','ending'),('节奏','pace; rhythm'),('明确','clear; definite'),('随便','arbitrarily; casually'),('忍不住','cannot help doing'),('反而','instead; contrary to expectation'),('替','on behalf of'),('未必','not necessarily')],place='Talking after an original film',context='Friends disagree about an unresolved ending but find one shared criticism.',turns=[('你觉得好看吗？','Did you like it?','Give a limited positive opinion',['我喜欢最后一段，不过中间有点慢。']),('你说他肯定回来了吗？','Did you say he definitely returned?','Distinguish inference from certainty',['没有，我觉得她不一定非要等他回来。']),('为什么推荐给我？','Why recommend it to me?','Name a relevant strength and limitation',['人物的变化很有意思，不过节奏比较慢。'])],usage=[('Disagree about the work, not the person','这一段我看法不一样。','I see this section differently.','Name the detail under discussion rather than assigning a trait to the other viewer.'),('Explain a bounded preference','我喜欢最后一段，没说整部都好。','I liked the last part; I did not say the whole film was good.','A specific positive evaluation can coexist with criticism of other parts.')],tasks=practice([(D[8][0],D[8][1],'The speaker also found two sections difficult to keep watching.',True,'The speaker agrees and identifies two sections.'),(R[3][0],R[3][1],'Rewatching made the narrator suddenly love the entire film.',False,'The narrator explicitly says it did not.')],[('你说中间慢、喜欢最后一段。是不是觉得整部都好？','You said the middle was slow but liked the last part. Do you think the whole film is good?',['不是，我只是喜欢最后一段。','对，我已经说中间每一段都很好。','不是，我已经说最后一段也完全不好。'],0,'The reply preserves the limited positive evaluation.'),('她到车站买票看姐姐，没有确定他回来。怎么回答你不等他了？','She buys a ticket to visit her sister without knowing whether he returns. How does she answer about no longer waiting?',['他知道怎么找我，我先去看看姐姐。','他已经回来了，所以不用等。','我来车站只是把信交给他。'],0,'The reply fits the station scene without inventing a confirmed reunion.')],[('大家未必有同样的期待。','People may not have the same expectations.','期待'),('我又没说整部都好。','I did not say the whole thing was good.','又')],[[(V[i][3],V[i][4]) for i in [3,6,11]],[(V[i][5],V[i][6]) for i in [4,8,12]]]),review='Native review: the closing hunger joke, defensive 又没 in a close friendship, and the film recommendation’s register. Letter continuity and station purpose checked. The woman’s change is supported by actions, while whether the man returns is deliberately left unknown.')
write(4,8,spec,publish='--publish' in sys.argv)
