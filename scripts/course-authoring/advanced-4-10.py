"""Decline a gathering while keeping a friendship and a concrete alternative."""
import sys
from advanced_core import write,rows,words,q,card,practice
V=words('''
原则|principle|nguyên tắc|先问本人，是我们做这件事的原则。|Asking the person first is our principle for this.|他的原则是不借别人的账号。|His principle is not to borrow someone else’s account.
不在乎|not care about; not mind|không để ý|我不在乎坐哪里，只要能听清。|I don’t mind where I sit as long as I can hear.|她不在乎礼物贵不贵，更喜欢自己做的。|She doesn’t care whether a gift is expensive; she prefers homemade ones.
在乎|care about|quan tâm|我在乎的是你愿不愿意来，不是礼物。|What matters to me is whether you want to come, not the gift.|他很在乎朋友的意见。|He cares a lot about his friends' opinions.
相处|get along; spend time together|hòa hợp; ở cùng|和她相处很轻松，不用一直找话题。|Spending time with her is easy; I don’t have to keep finding topics.|我们相处了一年，才发现喜欢同一种音乐。|We spent a year together before realising we liked the same music.
误会|misunderstand; misunderstanding|hiểu lầm|我可能误会了，你不是这个意思吧？|I may have misunderstood; that isn’t what you meant, is it?|这个误会解释清楚以后，我们都笑了。|We both laughed once the misunderstanding was cleared up.
难免|hard to avoid; inevitably sometimes|khó tránh|刚到新的地方，难免有点不习惯。|It’s natural to feel a little unfamiliar in a new place.|两个人一起做事，难免会有不同意见。|When two people work together, disagreements are hard to avoid.
约会|date; arranged meeting|hẹn hò; cuộc hẹn|他们第一次约会是在这家咖啡店。|Their first date was at this café.|我今晚有约会，不能参加聚会。|I have a date tonight, so I can’t join the gathering.
承认|admit; acknowledge|thừa nhận|我承认自己回复得太晚了。|I admit I replied too late.|他终于承认把地址看错了。|He finally admitted he’d misread the address.
担心|worry; be concerned|lo lắng|我担心你以为我不想见你。|I’m worried you’ll think I don’t want to see you.|别担心，我到家以后会给你消息。|Don’t worry; I’ll message you when I get home.
考虑|consider|cân nhắc|我想考虑一下，明天回复你。|I’d like to think about it and reply tomorrow.|你不用只考虑我的时间。|You don’t need to consider only my schedule.
回复|reply|trả lời|谢谢你这么快回复。|Thanks for replying so quickly.|我还没有收到他的回复。|I haven’t received his reply yet.
直接|directly; direct|trực tiếp|你可以直接告诉我，不用猜我想听什么。|You can tell me directly; no need to guess what I want to hear.|这班车可以直接到学校。|This service goes straight to the school.
态度|attitude|thái độ|她的态度很认真，但说话不重。|She takes it seriously without speaking harshly.|你刚才的态度让我以为你生气了。|Your manner just now made me think you were angry.
答应|agree to a request; promise|đồng ý; hứa|我答应周二陪你吃饭。|I agreed to have dinner with you on Tuesday.|他答应的事都会记下来。|He writes down the things he promises to do.
解释|explain|giải thích|我想解释一下为什么没去。|I’d like to explain why I didn’t go.|这段介绍解释了活动怎么报名。|This introduction explains how to sign up for the event.
坚持|persist; insist|kiên trì; giữ vững|她坚持每周给家里打电话。|She keeps calling home every week.|他坚持自己去，不想让我陪。|He insists on going himself and doesn’t want me to accompany him.
''')
D=rows('''
周六生日聚会你来吧？我还没算人数。|You’ll come to the birthday gathering on Saturday, right? I haven’t counted everyone yet.
谢谢你叫我，不过这次我就不去了。|Thanks for inviting me, but I think I’ll sit this one out.
那天有事？|Do you have something on that day?
也不是。最近每天都和人说话，我想在家安静一晚。|Not really. I’ve been talking to people every day recently and want a quiet evening at home.
你是不是不想见我？|Is it that you don’t want to see me?
不是不想见你。大聚会我现在有点累，单独吃饭我很愿意。|It isn’t that I don’t want to see you. A big gathering feels tiring right now; I’d be very happy to have dinner just with you.
那下周二呢？七点在以前那家店？|How about next Tuesday? Seven at that place we used to go to?
好，我答应你。不过你生日那天，我还是会给你电话。|Yes, I promise. I’ll still call you on your birthday too.
行。我刚才还真有点误会了。你以后直接说就好。|Okay. I really did misunderstand a little just now. Tell me directly next time.
我也是怕你不高兴，才拖到今天说。下次早点回复。|I was worried you’d be upset, which is why I put it off until today. I’ll reply earlier next time.
早点说我就不用一直问。礼物可别忘了。|If you say it sooner, I don’t have to keep asking. Don’t forget the present, though.
你不是说不在乎礼物吗？|Didn’t you say you didn’t care about presents?
''')
R=rows('''
周六聚会以后，陈宇给我发了一张照片。照片里有十几个人，大家围着桌子唱生日歌。我替他高兴，也知道自己那晚确实没有精力参加。|After Saturday’s gathering, Chen Yu sent me a photo. More than ten people were singing around the table. I was happy for him and knew I really hadn’t had the energy to join that night.
以前我遇到这种邀请，常常先答应，到当天才说去不了。朋友没时间重新安排，我也觉得不好意思。这次我在人数确定之前就回复了。|I used to accept this sort of invitation and then cancel on the day. That left friends no time to adjust and made me feel bad. This time I replied before the headcount was fixed.
一开始他以为我不想见他，我就把两件事分开解释：我不想参加大聚会，但想和他单独吃饭。我们约了下周二七点，他不用为了我改变周六的活动。|At first he thought I didn’t want to see him. I explained the two things separately: I didn’t want the big gathering but did want dinner with him. We arranged Tuesday at seven, without changing Saturday’s event for me.
生日当天，我给他打了电话。没说很多话，只问聚会准备得怎么样，祝他生日快乐。他说饭已经够了，让我下次别又带一大盒点心。|On his birthday I called, asked how preparations were going and wished him a happy birthday. He said there was enough food and told me not to bring another huge box of pastries next time.
周二见面时，我带了一小盒。他看了看，说“这回你真的听进去了”。我们吃完饭，又聊了周六的照片，没有再争论我为什么没去。|When we met Tuesday, I brought a small box. He looked and said, “You really listened this time.” After dinner we talked about the photos without returning to the argument about my absence.
我发现说清楚一个具体安排，比反复说“以后再约”有用。当然，有时别人还是会失望。解释并不能让所有人立刻高兴，但至少让这次决定少一点误会。|I found that a concrete plan was more useful than repeatedly saying, “Let’s meet sometime.” People can still feel disappointed. An explanation doesn’t instantly please everyone, but it can reduce misunderstanding about this decision.
''')
M=rows('''
这是一小盒？|This is a small box?
对，上次那个盒子有这么大。|Yes. Last time the box was this big.
你拿手比也没用，我记得上次的。|The hand gestures won’t help. I remember the last one.
今天这个真的小了。你不在乎礼物，还在乎盒子大小？|Today’s really smaller. You don’t care about the present, but you care about the box size?
我在乎冰箱能不能放下。|I care whether it fits in the fridge.
那我们现在吃掉一半，就放得下了。|Then we’ll eat half now, and it’ll fit.
这个方案我赞成。|I approve of that plan.
看吧，还是一起吃饭最容易说明白。|See? Things are easiest to clear up over dinner.
''')
G=[
card('不是不…，而是…','Clarify what is and is not being declined','不是不 rejects a negative interpretation, often followed by a specific reason after 而是. Avoid relying on double negatives alone when the other person needs a clear answer.','我不是不想见你，而是今天想早点回家。|It isn’t that I don’t want to see you; I want to go home early today.\n我不是不喜欢，只是现在吃不下。|It isn’t that I dislike it; I can’t eat any more now.','我不是不想见你，所以我不想见你。','我不是不想见你，而是今天想早点回家。','The second clause should clarify the actual limitation.'),
card('怕…才…','Explain a motivation that led to an action','怕 can introduce an anticipated unwelcome outcome; 才 highlights how it motivated the action. This explains the speaker’s decision, not the other person’s actual feelings.','我怕你不高兴，才一直没说。|I kept quiet because I was worried you’d be upset.\n怕赶不上车，我才提前出门。|I left early because I was worried I’d miss the train.','我怕你不高兴，所以你一定不高兴。','我怕你不高兴，才一直没说。','A feared reaction is not a verified reaction.'),
card('哪怕…也…','Keep a choice or result despite a difficult condition','哪怕 introduces an extreme condition, and 也 gives the result that still holds. It may be hypothetical; it does not force another person to accept your choice.','哪怕只坐十分钟，我也想见你一下。|Even if I can stay only ten minutes, I still want to see you.\n哪怕别人会失望，我也不能每次都答应。|Even if someone will be disappointed, I can’t agree every time.','哪怕只坐十分钟，所以我坐了一整天。','哪怕只坐十分钟，我也想见你一下。','The result should remain compatible with the stated condition.'),
card('比 + vague action + 更 / 有用','Compare concrete communication options','Use 比 to compare two actions, and state the dimension of comparison after the second action or in the predicate. This is a situated comparison, not a universal ranking of people.','约好具体时间，比只说以后再约更有用。|Agreeing a specific time is more useful than just saying we’ll meet sometime.\n早点回复，比当天才说更方便安排。|Replying early makes planning easier than saying it on the day.','比早点回复，我当天说更早点。','早点回复，比当天才说更方便安排。','Compare the same practical dimension with a coherent word order.'),
]
spec=dict(title=('A no that still leaves room for friendship','这次不去，周二见'),goals=['Decline an invitation with a truthful specific reason','Distinguish declining an event from rejecting a friendship','Offer and keep a concrete alternative plan'],vocabulary=V,grammar=G,dialogue=(D,[q('gist','What does the invited person decide?','Skip the large gathering and arrange dinner together','Attend every event without replying','Ask the host to cancel the birthday'),q('detail','When is the alternative dinner?','Next Tuesday at seven','Saturday at noon','Sunday at five'),q('inference','Why was the reply delayed?','The invited person feared upsetting the friend','The friend had never sent an invitation','The restaurant had already closed permanently')]),reading=(R,[q('gist','What helps reduce the misunderstanding?','A specific explanation and a kept alternative plan','Repeated vague promises with no date','Changing the whole birthday event'),q('detail','What does the narrator bring on Tuesday?','A small box of pastries','A large refrigerator','No gift after promising a large box'),q('inference','What does the narrator learn about explanations?','They may help without instantly removing all disappointment','They guarantee every person is happy','They make earlier replies unnecessary')]),mediaTitle='A small box, apparently',media=(M,[q('detail','Why does box size matter to the friend?','It needs to fit in the fridge','The box determines their age','It cannot be opened at dinner'),q('inference','What is the shared solution?','Eat half now','Cancel dinner','Buy a larger fridge immediately')]),glosses=[('精力','energy; mental effort'),('拖到','put off until'),('点心','pastry; snack'),('围着','gathered around'),('听进去','take in what someone said'),('冰箱','fridge'),('手比','gesture the size with one’s hands here'),('大小','size'),('立刻','immediately')],place='Responding to a close friend’s invitation',context='The learner wants a quiet Saturday but is happy to meet the friend separately.',turns=[('你是不是不想见我？','Is it that you do not want to see me?','Clarify the specific limit',['不是，我只是这次不想参加大聚会。']),('那什么时候有空？','When are you free then?','Offer a concrete alternative',['下周二七点一起吃饭，行吗？']),('你怎么今天才说？','Why did you only say so today?','Acknowledge the delayed reply',['我怕你不高兴，回复晚了，下次早点说。'])],usage=[('Give the answer before a vague future promise','这次我不去，周二想单独和你吃饭。','I will skip this one; I would like dinner with you on Tuesday.','The event decision is clear and the alternative is specific.'),('Acknowledge the practical impact','我回复晚了，让你不好算人数。','I replied late, which made the headcount difficult.','This recognises the effect on planning without inventing the other person’s emotions.')],tasks=practice([(D[3][0],D[3][1],'The speaker already has another event that night.',False,'The speaker says they want a quiet evening, not another event.'),(R[2][0],R[2][1],'The Saturday gathering is changed to suit the narrator.',False,'The Tuesday dinner is separate; Saturday does not change.')],[('你不来，是不想见我吗？','Does not coming mean you do not want to see me?',['不是，我想周二单独和你吃饭。','不是，所以你必须把周六改成周二。','对，我不想再有任何见面。'],0,'The reply distinguishes the event from the friendship.'),('这个盒子太大，想把一半留下。怎么才能放进冰箱？','This box is too large, and we want to keep half. How can it fit in the fridge?',['我们先吃一半吧。','把全部吃完，就还剩下一半。','一点不动，就已经只剩一半了。'],0,'The reply follows the box-size joke and shared solution.')],[('我承认自己回复得太晚了。','I admit I replied too late.','承认'),('哪怕只坐十分钟，我也想见你一下。','Even if I can stay only ten minutes, I still want to see you.','也')],[[(V[i][3],V[i][4]) for i in [0,4,10]],[(V[i][5],V[i][6]) for i in [3,7,12]]]),review='Native review: degree of directness between close friends, 才 explaining a delayed reply, and gift/fridge teasing. Timeline checked: Saturday party, birthday phone call, separate Tuesday dinner at seven. 约会 is taught as a date/arranged meeting; this friends’ dinner is not silently labelled romantic.')
spec.setdefault('glosses', []).append(('松', 'loose; relaxed (in 松一口气, breathe a sigh of relief)'))
write(4,10,spec,publish='--publish' in sys.argv)
