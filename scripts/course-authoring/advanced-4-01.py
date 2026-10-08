"""Authored social bridge: meeting a new group without forced small talk."""
import sys
from advanced_core import write
from editorial_repair import tf,reply,fill,match
from common import dictionary
dictionary.update({'我得先':'wǒ děi xiān','明天得早点':'míng tiān děi zǎo diǎn','得先':'děi xiān'})

V=[
('聚会','get-together','buổi tụ họp','周末的聚会在我家。','The get-together this weekend is at my place.','聚会结束后，我和新朋友交换了号码。','After the get-together I exchanged numbers with a new friend.'),
('称赞','praise; compliment','khen ngợi','她称赞我做的蛋糕，说还想再吃一块。','She complimented my cake and said she wanted another slice.','老师称赞了我们的表演。','The teacher praised our performance.'),
('沉默','remain silent; silence','im lặng','他沉默了一会儿，才说起昨天的事。','He was silent for a moment before talking about yesterday.','大家忽然都沉默了，我不知道该说什么。','Everyone suddenly fell silent and I didn’t know what to say.'),
('表情','facial expression','biểu cảm','看你的表情，你是不是不喜欢这道菜？','Judging by your expression, don’t you like this dish?','他的表情很认真，可他说的其实是玩笑话。','He looked serious, but what he said was actually a joke.'),
('误会','misunderstand; misunderstanding','hiểu lầm','我误会你的意思了，对不起。','I misunderstood you. Sorry.','这次误会说开以后，我们反而更了解彼此了。','Once we cleared up this misunderstanding, we understood each other better.'),
('解释','explain','giải thích','你能解释一下为什么要换地方吗？','Could you explain why we need to change the venue?','她解释了半天，我才发现是自己看错了日期。','After she explained for ages, I realised I’d read the date wrong.'),
('反而','instead; contrary to expectation','ngược lại','我原来怕冷场，见面以后反而聊个不停。','I’d worried the conversation would dry up, but once we met we couldn’t stop talking.','他没有生气，反而笑了。','He didn’t get angry; he laughed instead.'),
('按时','on time','đúng giờ','请按时到，大家一起做饭。','Please arrive on time; we’re cooking together.','我今天按时到了，主人却还没回来。','I arrived on time today, but the host wasn’t back yet.'),
('性格','personality','tính cách','我们性格不太一样，但都喜欢看电影。','Our personalities are quite different, but we both like films.','她的性格和她姐姐很不一样。','Her personality is very different from her sister’s.'),
('主动','take the initiative','chủ động','我主动问她要不要一起去买菜。','I took the initiative and asked whether she wanted to buy groceries together.','下课后，他主动过来跟我打招呼。','After class he came over to say hello first.'),
('话题','topic of conversation','chủ đề','刚才那个话题我不太了解。','I don’t know much about the topic you were just discussing.','我们从天气聊到了音乐，话题越来越多。','We went from weather to music and found more and more to talk about.'),
('共同','shared; common','chung','我们有一个共同的朋友。','We have a friend in common.','这个决定是大家共同作出的。','Everyone made this decision together.'),
('印象','impression','ấn tượng','这座城市给我的第一印象是很安静。','My first impression of this city was how quiet it was.','我对他的印象变了：他比我想的热情。','My impression of him changed: he’s friendlier than I thought.'),
('互相','each other; mutually','lẫn nhau','我们互相介绍了自己的家乡。','We told each other about our hometowns.','搬家那天，邻居们互相帮忙。','On moving day, the neighbours helped each other.'),
('适应','adapt to','thích nghi','刚搬到这里，我还在适应新的生活。','I’ve just moved here and I’m still adjusting to my new life.','我花了两个月才适应这里的天气。','It took me two months to get used to the weather here.'),
('热情','friendly; enthusiastic','nhiệt tình','她很热情，一进门就问我要不要喝茶。','She was very welcoming and offered me tea as soon as I came in.','大家对这个计划很热情，马上开始讨论。','Everyone was enthusiastic about the plan and immediately started discussing it.'),
]
D=[
('你今晚也去林安家的聚会吗？','Are you going to the get-together at Lin An’s tonight too?'),
('去，不过除了你，我谁都不认识。','Yes, but I don’t know anyone except you.'),
('别担心，我先介绍你们认识。你几点能到？','Don’t worry, I’ll introduce you first. What time can you get there?'),
('六点吧。我得先回家拿蛋糕。','Around six. I have to go home and pick up the cake first.'),
('你还做了蛋糕？人家肯定很高兴。','You made a cake too? They’ll be delighted.'),
('别先称赞我，可能没有上次那么好吃。','Don’t compliment me yet. It might not be as good as last time.'),
('好，那我吃完再说。对了，有个朋友也喜欢你说的那个乐队。','Fine, I’ll say something after I try it. By the way, one of the friends likes that band you mentioned too.'),
('真的？那我们至少有个共同话题了。','Really? Then we’ve got at least one topic in common.'),
('你不想说话的时候，安静听着也行，不用一直找话题。','When you don’t feel like talking, it’s fine to just listen. You don’t have to keep finding topics.'),
('你越这么说，我反而越紧张。','The more you say that, the more nervous I get.'),
('行，我不说了。你按时来就好，我在门口等你。','Okay, I’ll stop. Just come on time; I’ll wait at the door.'),
('好。蛋糕要是不好吃，你可别当着大家的面说。','Okay. If the cake tastes bad, don’t say so in front of everyone.'),
]
R=[
('搬到新城市以后，我最不适应的是下班后的安静。以前想吃饭，随时都能找到朋友。现在手机里有很多名字，却不知道该联系谁。','After moving to a new city, I struggled most with the quiet evenings after work. I used to be able to find friends for dinner whenever I wanted. Now there were lots of names in my phone, but I didn’t know whom to contact.'),
('星期五，邻居问我要不要去她家的聚会。我答应了，到了门口却有点紧张：如果大家没有共同话题，怎么办？','On Friday my neighbour invited me to a get-together at her place. I accepted, but at the door I felt nervous: what if we had nothing in common to talk about?'),
('她先介绍我认识另一个新搬来的朋友。我们都带了一盒自己做的点心，看见对方手里的盒子，反而一起笑了。','She introduced me to another friend who’d recently moved here. We’d both brought a box of homemade snacks. When we saw each other’s boxes, we laughed.'),
('一开始，我们聊家乡的天气和吃的东西。后来，他说自己周末常去听音乐，我才发现我们喜欢同一个乐队。','At first we talked about the weather and food in our hometowns. Then he said he often went to hear music at weekends, and I discovered we liked the same band.'),
('那天我没有和每个人都聊很久。有一段时间，我只是坐着听。主人没催我说话，也没有问我为什么沉默。','I didn’t talk at length with everyone that day. For a while I simply sat and listened. The host didn’t push me to speak or ask why I was quiet.'),
('走的时候，我们互相留了号码，约好下周去听音乐。回家的路上，我突然觉得这座城市没那么陌生了。','Before leaving, we exchanged numbers and arranged to hear music together the following week. On the way home, the city suddenly felt less unfamiliar.'),
('后来我主动请邻居来吃饭。她称赞我的菜，我解释说是照着妈妈教的做的。我们又多了一个能聊的话题。','Later I invited my neighbour to dinner. She complimented my food, and I explained that I’d made it the way my mum taught me. We had another topic to talk about.'),
('现在我知道，交朋友未必需要很多漂亮的话。按时赴约，记住对方说过的小事，有时候比不停地说更重要。','Now I know that making friends doesn’t necessarily require lots of impressive words. Showing up on time and remembering little things someone told you can matter more than talking nonstop.'),
]
M=[
('这盒也是蛋糕？','Is that box a cake too?'),('对。你不会也带了吧？','Yes. Don’t tell me you brought one too?'),
('带了。我做了两个小时，路上还怕没人喜欢。','I did. I spent two hours making it and worried on the way that nobody would like it.'),('那正好，我们互相称赞一下。','Perfect. We can compliment each other’s.'),
('还没吃呢，你这称赞也太早了。','We haven’t eaten yet. That’s a bit early for compliments.'),('我先称赞你的盒子。挺漂亮的。','I’ll compliment your box first. It’s pretty.'),
('谢谢。这是昨天买的。蛋糕才是今天做的。','Thanks. I bought it yesterday. The cake’s the part I made today.'),('那我们先找把刀。再不切，大家只能看盒子了。','Then let’s find a knife. If we don’t cut them, people can only admire the boxes.'),
]
G=[
('得 + verb','State a practical obligation','Read 得 as děi here: the speaker needs to do something. The complement marker 得 is de and occupies a different position.', [('我得先回家拿蛋糕。','I have to go home and pick up the cake first.'),('明天得早点走，不然会迟到。','We need to leave early tomorrow or we’ll be late.')],('我先回家得拿蛋糕。','我得先回家拿蛋糕。','Modal 得 goes before the action; 得 after a verb has another function.')),
('人家','Refer informally to someone else','人家 can refer to another person or household already understood in the conversation. It is informal; use a name when the referent could be unclear.', [('人家请我们吃饭，我们别迟到。','They invited us to dinner; let’s not be late.'),('你先问问人家愿不愿意。','Ask whether they’re willing first.')],('人家请我们，所以所有人都愿意。','人家请我们，我们按时到吧。','An invitation refers to this host; it does not state everyone’s preference.')),
('未必 + predicate','Challenge an assumption without asserting its opposite','未必 means not necessarily. It leaves the result open; it does not mean definitely not.', [('安静的人未必不喜欢聚会。','Quiet people don’t necessarily dislike get-togethers.'),('带礼物未必需要花很多钱。','Bringing a gift doesn’t necessarily require spending a lot.')],('她未必不来，所以她一定来。','她未必不来，我们再问问。','Not necessarily absent does not guarantee attendance.')),
('原来…反而…','Describe a result that reverses expectation','Give the expectation first and use 反而 for the surprising opposite tendency. It is more specific than a general 而且 addition.', [('我原来怕冷场，见面以后反而聊个不停。','I feared the conversation would dry up, but we couldn’t stop talking once we met.'),('我以为他会生气，他反而笑了。','I thought he’d be angry; instead he laughed.')],('他喜欢这道菜，反而又吃了一碗。','他喜欢这道菜，所以又吃了一碗。','Eating more is an expected consequence here, so 所以 fits better.')),
]
qD=[('gist','What is the friend offering?',['An introduction and someone to meet at the door','A paid cooking course','A change to the gathering date'],0),('detail','Why must the guest go home first?',['To pick up the cake','To buy a ticket','To find the neighbour’s number'],0),('inference','What does the guest’s final request suggest?',['They’re joking but feel self-conscious about the cake','They plan to buy a different cake instead','They have already tried everyone else’s cake'],0)]
qR=[('gist','What changes for the narrator?',['A new city starts feeling less unfamiliar','They decide to stop meeting people','They immediately know everyone in the city'],0),('detail','What shared interest do the two newcomers discover?',['The same band','The same employer','The same cooking teacher'],0),('inference','What helped the narrator feel comfortable?',['The host allowed them to listen quietly','The host required them to give a speech','The host criticised the snacks'],0)]
qM=[('detail','Which part was bought yesterday?',['The box','The cake','The knife'],0),('inference','Why is the early compliment funny?',['Neither person has tasted the cake yet','They already dislike the cake','The cakes have disappeared'],0)]
spec=dict(title=('A new group, a real connection','第一次见面，不用一直找话题'),goals=['Join a gathering and find a shared interest','Recognise an obligation and a tentative assumption','Follow friendly teasing without treating it as criticism'],vocabulary=V,grammar=G,dialogue=(D,qD),reading=(R,qR),mediaTitle='Two cakes at the door',media=(M,qM),glosses=[('乐队','band'),('冷场','an awkward lull in conversation'),('点心','snack; small treat'),('陌生','unfamiliar'),('赴约','keep an appointment'),('邻居','neighbour'),('盒子','box'),('催','urge; press someone'),('不停','without stopping'),('蛋糕','cake')],place='At a friend’s doorway',context='You are arriving at a gathering where you know only one person.',turns=[('你带了什么？','What did you bring?','Introduce what you brought',['我带了自己做的蛋糕。']),('你们有共同的爱好吗？','Do you have an interest in common?','Name a shared interest',['我们都喜欢同一个乐队。']),('你现在想说话还是听一会儿？','Would you like to talk now or listen for a while?','Ask for a little time without apologising excessively',['我想先听一会儿。'])],usage=[('Offer an introduction','我介绍你们认识吧。','Let me introduce you.','A concrete offer helps a newcomer more than repeatedly telling them not to feel nervous.'),('Clarify a misunderstanding','我不是那个意思。我说清楚一点。','That’s not what I meant. Let me explain more clearly.','Explain your intended meaning before arguing about the listener’s reaction.')],tasks=[tf(D[3][0],D[3][1],'The guest must pick up a cake before coming.',True,'The guest says 我得先回家拿蛋糕.'),tf(R[4][0],R[4][1],'The host insisted that the narrator speak continually.',False,'The host did not push the narrator to talk.'),reply('我有点紧张，不知道说什么。','I’m a little nervous and don’t know what to say.',['先听一会儿也行，不用一直说。','你必须马上跟每个人说话。','你肯定不喜欢这里。'],0,'Listening quietly is offered as an acceptable choice.'),reply('你还没吃蛋糕就说好吃？','You are saying the cake tastes good before trying it?',['那我吃完再称赞。','对，我已经吃了十块。','因为没吃就一定知道味道。'],0,'The friendly reply acknowledges the premature compliment.'),fill('我得先回家拿蛋糕。','I have to go home and pick up the cake first.','得'),fill('他没有生气，反而笑了。','He didn’t get angry; he laughed instead.','反而'),match(V[0][3:5] and [(V[0][3],V[0][4]),(V[7][3],V[7][4]),(V[9][3],V[9][4])]),match([(V[4][3],V[4][4]),(V[5][3],V[5][4]),(V[12][3],V[12][4])])],review='Check informal 人家, the joking cake exchange and the intended warmth of the English translations with a native speaker. All factual keys trace to explicit details; no unqualified social universal is claimed.')
spec['tasks'][4]['blankPy']='děi'
spec['glosses'].extend([('号码','number; contact number here'),('彼此','each other')])
write(4,1,spec,publish='--publish' in sys.argv)
