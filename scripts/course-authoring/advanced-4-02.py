"""Authored misunderstanding and playful-intent lesson; no policy dialogue."""
import sys
from advanced_core import write,rows,words,q,card,practice

V=words('''
暗示|hint; imply|ám chỉ|她暗示自己想早点回家。|She hinted that she wanted to go home early.|他没直接说价格，只暗示可能很贵。|He didn’t name a price, only hinted that it might be expensive.
含义|meaning; implication|ý nghĩa|这句话的含义要看前面说了什么。|What this sentence means depends on what came before it.|这个名字有什么特别的含义吗？|Does this name have a special meaning?
究竟|exactly; after all|rốt cuộc|你究竟想周五去，还是周六去？|Do you actually want to go on Friday or Saturday?|我想知道他们究竟为什么吵架。|I want to know exactly why they argued.
未必|not necessarily|chưa chắc|贵的东西未必更好。|Expensive things aren’t necessarily better.|不说话未必是生气。|Being quiet doesn’t necessarily mean being angry.
的确|indeed; really|quả thật|这家店的面的确很好吃。|The noodles here really are good.|你的办法的确省时间。|Your method really does save time.
竟然|unexpectedly|vậy mà|他竟然记得我去年说过的话。|He actually remembered what I’d said last year.|我竟然把钥匙放进冰箱了。|Somehow I put my keys in the fridge.
却|but; yet|nhưng lại|我想帮忙，却越帮越忙。|I wanted to help but ended up making more work.|天气很好，她却不想出门。|The weather was lovely, yet she didn’t want to go out.
对于|as for; regarding|đối với|对于这个安排，你有什么意见？|What do you think of this arrangement?|对于第一次来的朋友，地图很有用。|A map is useful for friends visiting for the first time.
似乎|seem; apparently|dường như|他似乎没听懂我的问题。|He seems not to have understood my question.|雨似乎停了，我们出去看看吧。|It seems to have stopped raining. Let’s check outside.
承认|admit; acknowledge|thừa nhận|我承认，刚才是我看错了。|I admit I read it wrong just now.|他终于承认自己忘了报名。|He finally admitted he’d forgotten to register.
诚实|honest|thành thật|请诚实地告诉我，菜是不是太咸了？|Tell me honestly: is the food too salty?|她很诚实，捡到钱马上交给了老师。|She was honest and immediately gave the money she found to the teacher.
称赞|compliment; praise|khen ngợi|他称赞我的外套，我却听成了别的话。|He complimented my coat, but I misheard it as something else.|妈妈称赞我这次做饭有进步。|Mum said my cooking had improved this time.
解释|explain|giải thích|你先解释一下，我再回答。|Explain first, then I’ll answer.|她用两张照片解释了路线。|She explained the route using two photos.
表扬|commend; praise|biểu dương|老师当着全班表扬了她。|The teacher praised her in front of the whole class.|他不习惯被表扬，脸一下就红了。|He wasn’t used to being praised and immediately blushed.
不在乎|not mind; not care|không bận tâm|我不在乎坐哪里，只要能听清楚。|I don’t mind where I sit as long as I can hear.|她不在乎输赢，只想跟朋友一起玩。|She doesn’t care about winning or losing; she just wants to play with friends.
不要紧|no problem; it’s all right|không sao|迟到几分钟不要紧，到了给我发消息。|A few minutes late is fine; message me when you arrive.|杯子打破了？不要紧，你没受伤吧？|You broke the cup? It’s all right. Are you hurt?
''')
D=rows('''
你刚才说我的外套很特别，究竟是什么意思？|When you said my coat was unusual, what exactly did you mean?
就是颜色很好看。怎么了？|Just that the colour is lovely. What’s wrong?
你的表情太认真了，我以为你在说不好看。|You looked so serious that I thought you meant it looked bad.
我真是在称赞你。我这个人一紧张就不太会笑。|I really was complimenting you. I find it hard to smile when I’m nervous.
你也紧张？我还以为只有我这样。|You get nervous too? I thought it was just me.
当然。刚才我差点叫错你的名字。|Of course. I almost called you by the wrong name just now.
好吧，那是我误会了。谢谢你的称赞。|Okay, I misunderstood. Thanks for the compliment.
不要紧。说实话，你不喜欢别人评论你的衣服吗？|No problem. Honestly, do you dislike people commenting on your clothes?
不在乎，只是我今天自己也觉得这个颜色太亮了。|I don’t mind. It’s just that I already thought the colour was too bright today.
是挺亮的。我刚到门口，一下就找到你了。|It is bright. I spotted you as soon as I arrived at the door.
你这次是在开玩笑，对吧？|This time you’re joking, right?
对。不过你的确很好找。我们先进去吧。|Yes. But you really are easy to spot. Let’s go in.
''')
R=rows('''
以前，朋友说“你可真行”，我总以为是在表扬我。后来有一天，我把大家的车票忘在家里，他又说了这句话。|When friends used to say “You’re really something,” I always thought it was praise. Then one day I left everyone’s tickets at home, and a friend said it again.
我先笑了，看到他手里的空袋子才发现不对。原来，同样几个字，在不同的情况下，含义可能完全不同。|I smiled at first, then noticed the empty bag in his hand and realised something was wrong. The same few words can mean quite different things in different situations.
他没有发火，只问我究竟把票放在哪里。我承认自己出门前没检查，马上打车回去拿。|He didn’t lose his temper, just asked where exactly I’d put the tickets. I admitted I hadn’t checked before leaving and immediately took a taxi home to collect them.
回来以后，我想解释自己为什么会忘，朋友却先递给我一瓶水，说：“先喝口水，我们还有时间。”|When I got back, I wanted to explain why I’d forgotten, but my friend handed me some water first and said, “Have a drink first. We still have time.”
这次我没有急着猜他是不是生气。我先道歉，再问他刚才那句话是不是在开玩笑。他笑着说，一半是玩笑，一半是真的着急。|This time I didn’t rush to guess whether he was angry. I apologised first, then asked whether his earlier remark was a joke. He laughed and said it was half a joke and half genuine worry.
对于不太了解的表达，我现在会看前后的事情，也会直接问。不明白未必是自己的中文太差，有时连熟悉的人也会听错。|When I don’t understand an expression well, I now look at the surrounding events and ask directly. Not understanding doesn’t necessarily mean my Chinese is poor; even people who know each other can mishear things.
''')
M=rows('''
你可真行，票呢？|You’re really something. Where are the tickets?
在……等一下，我包里怎么没有？|In… hang on, why aren’t they in my bag?
你别告诉我，它们还在桌上。|Don’t tell me they’re still on the table.
我承认，应该还在桌上。你等我一下。|I admit they’re probably still on the table. Wait a moment.
先别跑，车还有半小时才开。我们一起想想办法。|Don’t run off yet. The train doesn’t leave for another half hour. Let’s work out what to do.
你不生气？|You’re not angry?
生气也不能把票变出来啊。你先打电话问问家里有人没有。|Getting angry won’t make the tickets appear. Call and see whether anyone’s home first.
好。今天我请你吃饭，先补偿一下。|Okay. Dinner’s on me today, to make it up to you.
''')
G=[
card('却','Express an unexpected contrast','Place 却 before the second predicate. It usually connects a result that conflicts with the first expectation. It does not automatically mean the result is negative.','我想帮忙，却越帮越忙。|I wanted to help but ended up making more work.\n天气很好，她却不想出门。|The weather is lovely, yet she doesn’t want to go out.','却天气很好，她不想出门。','天气很好，她却不想出门。','却 belongs with the contrasted predicate, not before the topic of the first clause.'),
card('究竟','Ask for the exact unresolved point','究竟 strengthens a genuine question with 谁、什么、哪里、为什么 or a choice. Context and delivery determine whether it sounds curious or impatient.','票究竟放在哪里了？|Where exactly did you put the tickets?\n你究竟想坐哪一班车？|Which train do you actually want to take?','你究竟坐哪一班车吗？','你究竟想坐哪一班车？','A specific-choice question does not add 吗.'),
card('对于 + topic','Set the topic of an attitude or assessment','对于 introduces what an attitude, opinion or evaluation concerns. In casual conversation, 关于、对 and a plain topic can overlap; do not force 对于 into every sentence.','对于这个安排，你有什么意见？|What do you think of this arrangement?\n对于第一次来的朋友，这张图很有用。|This map is useful for friends visiting for the first time.','我对于车站走过去了。','我向车站走过去了。','对于 introduces a topic or target of an attitude, not direction of movement.'),
card('的确 / 似乎','Separate confirmation from appearance','的确 endorses a claim; 似乎 presents an impression rather than certainty. A speaker can revise either after learning more.','这家的面的确很好吃。|The noodles here really are good.\n他似乎没听懂，我再说一次吧。|He seems not to have understood; I’ll say it again.','他似乎没听懂，所以我已经确定他不懂。','他似乎没听懂，我再问问。','似乎 does not itself establish certainty.'),
]
spec=dict(title=('A compliment or a joke?','你刚才究竟是什么意思'),goals=['Check the intended meaning of an ambiguous remark','Distinguish an impression from a confirmed fact','Repair a misunderstanding without turning it into an argument'],vocabulary=V,grammar=G,dialogue=(D,[q('gist','Why does the guest ask about the coat comment?','They aren’t sure whether it was a compliment','They want to borrow the coat','They cannot find their coat'),q('detail','Why does the speaker look serious?','They find it hard to smile when nervous','They are deliberately criticising the guest','They have already left'),q('inference','What supports the second remark being teasing?','The listener checks and the speaker confirms it is a joke','Every serious expression means a joke','The speaker refuses to explain')]),reading=(R,[q('gist','What has the narrator learned?','The meaning of a remark depends on its situation','Every remark containing 真 is praise','Questions should never be asked'),q('detail','What did the narrator forget?','Everyone’s tickets','A bottle of water','The taxi address'),q('inference','Why offer water before hearing the explanation?','The friend is helping them calm down while time remains','The friend has cancelled the journey','The friend has forgotten the tickets too')]),mediaTitle='The tickets are still at home',media=(M,[q('detail','How long remains before departure?','Half an hour','Five minutes','Two hours'),q('inference','What is the friend’s priority?','Find a practical way to get the tickets','Argue until the train leaves','Pretend the tickets are unnecessary')]),glosses=[('外套','coat'),('发火','lose one’s temper'),('熟悉','familiar'),('空袋子','empty bag'),('评论','comment on'),('补偿','make up for; compensate')],place='Outside a friend’s gathering',context='You are unsure whether a comment about your coat was friendly.',turns=[('你刚才是什么意思？','What did you mean just now?','Clarify your intended compliment',['我是真心称赞你，颜色很好看。']),('你是不是不喜欢这个话题？','Do you dislike this topic?','Say that the topic is fine but you misheard',['不是，我只是误会你的意思了。']),('那我们进去吧？','Shall we go in then?','Accept and move on',['好，进去吧。'])],usage=[('Check a possible joke','你是在开玩笑，对吧？','You’re joking, right?','Use a light delivery when checking friendly teasing; the same words can sound challenging if stressed.'),('Own a misunderstanding','是我误会了，谢谢你解释。','I misunderstood. Thanks for explaining.','This addresses your reading of the remark without claiming everyone must share it.')],tasks=practice([(D[3][0],D[3][1],'The speaker says nervousness makes smiling difficult.',True,'They explicitly describe what happens when nervous.'),(R[2][0],R[2][1],'The narrator immediately blamed the friend for losing the tickets.',False,'They admitted not checking before leaving.')],[('你说我的外套挺好看，究竟是什么意思？','You said my coat looks good. What exactly do you mean?',['我是在称赞你的外套。','我是说这件外套不好看。','我只说不好看，没有说好看。'],0,'This clarifies the remark under discussion.'),('票还在家里，我们现在在车站，家里可能有人。怎么办？','The tickets are at home and we are at the station. Someone may be home. What can we do?',['先问问家里有没有人。','我们已经拿到票，可以直接上车。','票不在家里，你刚才说带来了。'],0,'The reply offers a practical next step.')],[('天气很好，她却不想出门。','The weather is lovely, yet she doesn’t want to go out.','却'),('这家店的面的确很好吃。','The noodles here really are good.','的确')],[[(V[i][3],V[i][4]) for i in [0,2,9]],[(V[i][5],V[i][6]) for i in [3,7,14]]]),review='Native review: teasing force of 你可真行, whether the coat exchange sounds friendly in performance, 得/的/地 and neutral-syllable delivery. Keys distinguish uncertainty and direct statements without placing app-policy commentary in the dialogue.')
spec['glosses'].extend([('钥匙','key'),('冰箱','refrigerator'),('咸','salty')])
write(4,2,spec,publish='--publish' in sys.argv)
