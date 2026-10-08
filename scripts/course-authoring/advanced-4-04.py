"""Authored drama inference: a missed line and a visible letter."""
import sys
from advanced_core import write,rows,words,q,card,practice

V=words('''
镜头|shot; camera view|cảnh quay|这个镜头一直对着门口。|This shot keeps the doorway in view.|最后一个镜头里，桌上多了一封信。|In the final shot, there is an extra letter on the table.
角色|role; fictional character|vai; nhân vật|她在剧里演一个医生的角色。|She plays a doctor in the drama.|这个角色到最后才说出自己的名字。|This character reveals their name only at the end.
背景|background; setting|bối cảnh|故事的背景是一座小城市。|The story is set in a small city.|不了解当时的背景，很难懂这句话。|Without the background at that time, this remark is hard to understand.
描述|describe|miêu tả|你能描述一下她最后的表情吗？|Could you describe her final expression?|信里描述了他们第一次见面的地方。|The letter describes where they first met.
秘密|secret|bí mật|她把这个秘密告诉了姐姐。|She told her sister this secret.|他们准备给朋友过生日，暂时要保守秘密。|They’re preparing a birthday celebration for their friend and need to keep it secret for now.
甚至|even|thậm chí|他太忙了，甚至忘了今天是星期几。|He was so busy he even forgot what day it was.|这段话很难，我甚至听了五遍。|This passage is so difficult I listened to it five times.
保密|keep confidential|giữ bí mật|这件事先保密，周五再告诉她。|Keep this quiet for now; we’ll tell her on Friday.|请替我保密，我想给他一个惊喜。|Please keep this secret for me; I want to surprise him.
出色|excellent; outstanding|xuất sắc|她在这部电影里的表演很出色。|Her performance in this film is excellent.|他出色地完成了第一次演出。|He did an excellent job in his first performance.
沉重|heavy; serious in mood|nặng nề|这个故事的后半段很沉重。|The second half of this story is emotionally heavy.|他带着沉重的心情离开了医院。|He left the hospital feeling weighed down.
回|turn; instance|lần|这回我终于听懂她为什么笑了。|This time I finally understood why she laughed.|上回你说这家店关了，现在又开了吗？|Last time you said this shop had closed. Has it reopened?
段|section; passage|đoạn|这一段只有两个人说话。|Only two people speak in this section.|把最后一段再放一遍吧。|Please play the last section again.
反应|reaction|phản ứng|她听到名字以后，反应很奇怪。|Her reaction after hearing the name was strange.|我的反应慢了一点，没接上他的玩笑。|I reacted a little slowly and missed his joke.
表现|performance; show|thể hiện|他在比赛中的表现比上次好多了。|His performance in the competition was much better than last time.|她没有表现出不高兴。|She didn’t show that she was unhappy.
观众|audience|khán giả|演出结束，观众都站起来鼓掌。|At the end of the performance, the audience stood and applauded.|观众最想知道的是信里写了什么。|What the audience most wants to know is what the letter says.
内容|content|nội dung|这两封信的内容不一样。|The contents of these two letters differ.|标题很短，内容却有好几页。|The title is short, but the content runs to several pages.
误会|misunderstanding|hiểu lầm|她以为信是给自己的，结果闹了个误会。|She thought the letter was for her, which caused a misunderstanding.|这个误会到最后才解释清楚。|This misunderstanding is only cleared up at the end.
''')
D=rows('''
等一下，刚才她说什么？我只听到一个名字。|Wait, what did she say just now? I only caught a name.
她说那封信不是给她的，而是给她姐姐的。|She said the letter wasn’t for her; it was for her sister.
那她为什么还打开了？|Then why did she open it anyway?
她先打开才看见里面的名字。你看，信封上没写名字。|She opened it before seeing the name inside. Look, there’s no name on the envelope.
哦，难怪她的表情突然变了。我以为她生气了。|Oh, that explains why her expression suddenly changed. I thought she was angry.
未必。她可能只是发现自己弄错了。我们再看一段。|Not necessarily. She may just have realised she was mistaken. Let’s watch a little more.
这个镜头里，桌上好像还有另一封信。|In this shot there seems to be another letter on the table.
对，而且这封已经打开了。姐姐可能早就知道那件事。|Yes, and that one is already open. Her sister may have known about it for a while.
你连信封的颜色都记得，我刚才只顾着看她的脸。|You even remember the envelope’s colour. I was just watching her face.
我上回看过开头。你先别问最后怎么样，我不会说的。|I watched the opening last time. Don’t ask how it ends yet; I’m not telling.
行。与其听你解释，不如我自己看。就是得慢一点。|Fine. Rather than having you explain, I’d rather watch for myself. I just need to go a little slower.
那就一次看一段。等你看完，我们再谈这个角色。|Then let’s watch one section at a time. After you’ve finished, we can talk about the character.
''')
R=rows('''
第一次看这段戏时，我以为妹妹故意打开姐姐的信。她拿着信沉默了很久，最后只说了一句“原来你早就知道”。|The first time I watched this scene, I thought the younger sister deliberately opened her sister’s letter. She held it silently for a long time and finally said only, “So you knew all along.”
后来我重新看了前面的镜头。信封上没有名字，妹妹打开以后，才发现信里称呼的是姐姐。|Later I rewatched the earlier shots. There was no name on the envelope; only after opening it did the younger sister find it addressed to her older sister.
桌上另一封信已经打开，旁边还放着姐姐的照片。妹妹看到这些，才说出最后那句话。|Another letter on the table was already open, with a photo of the older sister beside it. The younger sister spoke her final line only after seeing these things.
这些细节让我改变了对这个角色的印象。她未必是在责怪姐姐，也可能是在难过：姐姐一直知道，却没告诉她。|These details changed my impression of the character. She wasn’t necessarily blaming her sister; she might also have been hurt that her sister had known all along without telling her.
不过，戏里没有直接解释姐姐为什么保密。直到下一段，我们才听见姐姐自己的回答。她说自己原来想等妹妹考试结束再谈。|But the scene didn’t directly explain why the older sister had kept it secret. Only in the next section did we hear her answer: she’d wanted to wait until her younger sister’s exams were over before discussing it.
现在跟朋友谈这段戏，我会先描述看见和听见的细节，再说自己的理解。大家可以有不同看法，回去看看同一个镜头，反而更有意思。|Now when discussing this scene with friends, I describe what I saw and heard before giving my interpretation. We can have different views; returning to the same shot makes it more interesting.
''')
M=rows('''
你都看过了，还跟着紧张？|You’ve already seen it. Why are you still getting nervous?
我看过开头，没看过最后。|I’ve seen the opening, not the ending.
那你刚才怎么知道她会打开信？|Then how did you know she’d open the letter?
她手都放在信封上了，我也是看出来的。|Her hand was already on the envelope. I worked it out from what I saw too.
我连她的手都没看见，光看那张照片了。|I didn’t even notice her hand. I was just looking at the photo.
难怪。你把这段倒回去，看右边。|That explains it. Go back through this section and look on the right.
好。你保密，别先告诉我。|Okay. Keep it secret—don’t tell me first.
知道了。今天我连一句多余的话都不说。|I know. Today I won’t say even one word more than necessary.
''')
G=[
card('不是…而是…','Correct the specific alternative','不是 rejects the first description and 而是 supplies the replacement. Both sides should answer the same implied question.','这封信不是给她的，而是给她姐姐的。|This letter is for her sister, not for her.\n我不是不想看，而是今天没时间。|It isn’t that I don’t want to watch; I don’t have time today.','这封信不是给她的，而且给她姐姐。','这封信不是给她的，而是给她姐姐的。','而是 introduces the corrected alternative; 而且 adds another item.'),
card('连…都…','Highlight an extreme or unexpected included case','Put the especially surprising case after 连. 都 or 也 follows it. The emphasis comes from context, not from an automatic negative meaning.','你连信封的颜色都记得。|You even remember the colour of the envelope.\n我连她的手都没看见。|I didn’t even notice her hand.','你连都信封的颜色记得。','你连信封的颜色都记得。','The highlighted phrase belongs between 连 and 都.'),
card('与其…不如…','Prefer one approach over another','The first approach is the less preferred one; the second follows 不如. This compares choices rather than measuring one person’s ability against another’s.','与其听你解释，不如我自己看。|Rather than listening to your explanation, I’d prefer to watch for myself.\n与其一次看完，不如一段一段看。|Rather than watching it all at once, it’s better to watch section by section.','与其我自己看，不如听你解释，所以我决定自己看。','与其听你解释，不如我自己看。','The chosen approach must follow 不如 in this comparison.'),
card('竟然 / 甚至','Distinguish surprise from escalation','竟然 marks something unexpected. 甚至 adds a case that goes further than what was already stated. Both need a meaningful context, not decoration.','她竟然记得十年前的那封信。|She surprisingly remembers that letter from ten years ago.\n他不只记得内容，甚至记得信封的颜色。|He remembers not just the contents, but even the envelope’s colour.','他甚至只记得内容，没有更多细节。','他记得内容，甚至记得信封的颜色。','The 甚至 case should extend the earlier claim, rather than merely restate a limited amount.'),
]
spec=dict(title=('Follow the letter, not just the face','那封信究竟给谁'),goals=['Recover a missed line from an original drama scene','Separate visible clues from interpretation','Discuss a character’s possible intention without revealing the ending'],vocabulary=V,grammar=G,dialogue=(D,[q('gist','What are the friends trying to clarify?','Whom the letter was for and why the expression changed','How much the letter cost','Who directed a different programme'),q('detail','What is missing from the envelope?','A name','An address already read aloud','Every piece of paper'),q('inference','Why does the experienced viewer refuse to explain the ending?','They want the other friend to watch it first','They have never seen any of the scene','They cannot remember the envelope colour')]),reading=(R,[q('gist','What changed the narrator’s interpretation?','Rewatching the letter and photo details','Learning a new actor’s name','Skipping every earlier shot'),q('detail','Why did the older sister say she had waited?','She wanted the younger sister’s exams to finish','She had lost both letters','She had never read any letter'),q('inference','Which point is presented as an interpretation rather than a direct statement?','The younger sister may feel hurt about not being told','The envelope has no name','The older sister says she waited for the exams')]),mediaTitle='Look at the right-hand side',media=(M,[q('detail','Which part has the friend already watched?','The opening','The whole ending','None of the scene'),q('inference','Why did the other friend miss the hand?','They were concentrating on the photo','The screen was turned off','There was no envelope in the shot')]),glosses=[('信封','envelope'),('妹妹','younger sister'),('姐姐','older sister'),('责怪','blame'),('故意','deliberately'),('多余','unnecessary; extra'),('称呼','address someone by a name or title'),('倒回去','go back in a recording here')],place='Watching an original drama together',context='You missed a line and need to work out whom the letter is addressed to.',turns=[('信是给谁的？','Whom is the letter for?','Correct the mistaken recipient',['不是给她的，而是给她姐姐的。']),('她为什么沉默？','Why is she silent?','Offer an interpretation as a possibility',['她可能是难过，不一定是生气。']),('要不要我告诉你最后怎么样？','Shall I tell you how it ends?','Decline the spoiler and ask to watch first',['先别告诉我，我自己看。'])],usage=[('Recover a line','刚才那句话我没听清，能倒回去吗？','I didn’t catch that line. Could we go back?','Ask for the missing span; hearing a sound and understanding its implication are different tasks.'),('Offer a reading of a character','我觉得她可能有点难过。','I think she might feel a little hurt.','我觉得 and 可能 keep the interpretation distinct from an explicit line in the scene.')],tasks=practice([(D[1][0],D[1][1],'The letter is addressed to the younger sister herself.',False,'It is for her older sister.'),(R[4][0],R[4][1],'The older sister says she wanted to wait until the exams finished.',True,'This is reported as her own explanation.')],[('我想自己看完再聊。你现在要直接告诉我结尾吗？','I want to watch it myself before discussing it. Are you going to tell me the ending now?',['先不说，你看完我们再聊。','不用看了，我现在把最后一幕讲完。','可以，你已经说想先听结尾。'],0,'The reply preserves the friend’s chance to watch first.'),('只看见她看信封后没说话，我以为她生气了。','I only saw her stop speaking after looking at the envelope, and assumed she was angry.',['未必，她也可能只是发现弄错了。','没说话就一定是生气，不用再看。','没听见她说原因，就已经知道全部了。'],0,'The reply gives a possible alternative without claiming certainty.')],[('这封信不是给她的，而是给她姐姐的。','This letter is for her sister, not for her.','而是'),('你连信封的颜色都记得。','You even remember the envelope’s colour.','连')],[[(V[i][3],V[i][4]) for i in [0,3,4]],[(V[i][5],V[i][6]) for i in [6,8,14]]]),review='Native review: natural force of 与其…不如… and 连…都… in friend chat, modal 得 in 得慢一点, and the letter scene’s emotional interpretation. Story chronology checked: opening precedes discovering the recipient; a later explicit explanation is distinguished from inference. Script is original.')
from common import dictionary
dictionary.update({'得慢一点':'děi màn yī diǎn'})
spec['glosses'].extend([('沉默','silence; remain silent'),('保守秘密','keep a secret'),('惊喜','pleasant surprise'),('鼓掌','applaud')])
write(4,4,spec,publish='--publish' in sys.argv)
