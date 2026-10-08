"""Friendly irony, an uncertain newcomer, and a concrete conversational repair."""
import sys
from advanced_core import write,rows,words,q,card,practice
V=words('''
幽默|humour; humorous|hài hước|他想用幽默缓解尴尬，可是新朋友没听懂。|He tried humour to ease the awkwardness, but the newcomer didn’t understand.|这部电影的幽默很安静，不是每句都让人笑。|The film’s humour is understated; not every line gets a laugh.
神情|expression; look|vẻ mặt|她的神情变了，我才发现她没有跟着笑。|Her expression changed, and I realised she wasn’t laughing with us.|他听见名字，神情一下认真起来。|Hearing the name, he suddenly looked serious.
脸色|facial complexion; expression|sắc mặt|她脸色不好，我先问是不是累了。|She looked unwell, so I first asked whether she was tired.|听见这个消息，他的脸色变了。|His expression changed on hearing the news.
脾气|temper; temperament|tính khí|别把一次生气，就说成她脾气一直不好。|Don’t turn one angry moment into a claim she always has a bad temper.|他脾气有点急，但愿意听解释。|He is a little impatient but willing to hear an explanation.
客气|polite; formal; courteous|khách sáo|我们不用这么客气，不过也不能替对方决定。|We needn’t be so formal, but cannot decide for one another.|她客气地说谢谢，没有答应留下。|She politely thanked them without agreeing to stay.
面子|face; social dignity|thể diện|我想给他留点面子，就没有当众重复那件事。|To spare him embarrassment, I didn’t repeat it in front of everyone.|她不想为了面子答应自己做不到的事。|She didn’t want to promise something impossible just to save face.
骂|scold; curse|mắng|她是在解释，不是在骂我。|She is explaining, not scolding me.|他听到骂人的话，先停下了讨论。|He stopped the discussion on hearing insults.
傻|foolish; silly|ngốc|他觉得自己的做法有点傻，不是在说别人都傻。|He thought his own action a little silly, not that others were all foolish.|别直接叫不熟的人傻。|Don’t directly call someone you barely know silly.
居然|unexpectedly; to one’s surprise|không ngờ|我居然把盐放了两次。|I somehow put salt in twice.|他居然记得我两年前说过的话。|He unexpectedly remembered something I said two years ago.
明明|clearly; obviously, contrary to a claim|rõ ràng|明明尝着很咸，他还说你真会放盐。|It clearly tasted salty, yet he said I was good at adding salt.|明明已经到了，为什么说还在路上？|You have clearly arrived; why say you are still on the way?
可|emphatic adverb in context|phó từ nhấn mạnh|这句话可不一定是在夸。|This sentence certainly isn’t necessarily praise.|我可没答应每天都来。|I certainly didn’t promise to come every day.
厉害|impressive; severe; formidable|giỏi; dữ dội|你能一边做饭一边接电话，真厉害。|Cooking while taking calls is impressive.|雨下得厉害，我们先别走。|The rain is heavy; let’s not leave yet.
可怜|pitiful; unfortunate|tội nghiệp|他说这碗汤太可怜了，盐全进去了。|He joked the soup was unfortunate: all the salt went into it.|那只小猫湿了，看起来很可怜。|The wet kitten looked pitiful.
忍不住|cannot help doing|không nhịn được|听见那句，我忍不住笑了一下。|I couldn’t help a brief laugh at that line.|她忍不住又看了一眼照片。|She couldn’t help looking at the photo again.
忍受|endure; put up with|chịu đựng|不喜欢那样叫，就不用一直忍受。|You needn’t keep putting up with a name you dislike.|他难以忍受门外一直响的声音。|He finds the constant sound outside hard to endure.
强迫|force; compel|ép buộc|我不想强迫你跟着笑。|I don’t want to force you to laugh along.|她没有强迫大家留下吃饭。|She didn’t force everyone to stay for dinner.
讨厌|dislike; annoying|ghét; khó chịu|我讨厌一直拿同一件事来说。|I dislike having the same matter brought up repeatedly.|这个声音很讨厌，我先关掉。|This sound is annoying; I’ll switch it off first.
模仿|imitate|bắt chước|他模仿自己找盐的样子，大家才笑了。|He imitated himself searching for salt, and people laughed.|她模仿了一次门响的声音。|She imitated the sound of the door once.
模样|appearance; look|dáng vẻ|我没看见他当时的模样，只看了文字。|I didn’t see his expression at the time; I only read the text.|这把伞的模样很特别。|This umbrella has an unusual appearance.
目光|gaze; look|ánh mắt|她把目光移到汤上，没有看我。|She shifted her gaze to the soup instead of looking at me.|他的目光一直跟着门口的人。|His gaze kept following the person by the entrance.
瞧|look; see, conversational|nhìn|你瞧，我又拿起盐了。|Look, I’ve picked the salt up again.|瞧，那辆车已经来了。|Look, that vehicle has arrived.
悄悄|quietly; secretly|lặng lẽ|她悄悄问我，那句话是不是在生气。|She quietly asked whether the sentence showed anger.|我悄悄把湿伞移到门外。|I quietly moved the wet umbrella outside.
随意|casually; at will|tùy ý|不熟的人之间，称呼别太随意。|Don’t use overly casual forms of address with people you barely know.|这些座位可以随意选，前面没有预留。|You may choose these seats freely; none at the front are reserved.
失误|mistake; slip|sai sót|这次失误是放盐两次，不是他不会做任何菜。|The slip was adding salt twice, not inability to cook anything.|她说明了失误，也告诉我怎么改。|She explained the mistake and how to correct it.
''')
D=rows('''
你尝一口，今天这汤是不是有点咸？|Try some. Is today’s soup a little salty?
你可真会放盐。|You certainly know how to add salt.
是在夸我吗？我都放了两次了。|Is that praise? I added it twice.
就是在说放多了。我的嘴今天不用再吃别的盐了。|I mean you added too much. My mouth doesn’t need any other salt today.
你们很熟才这么说吧？|You say that because you know each other well, right?
对。你要觉得不舒服，告诉我，我换个说法。|Right. If it makes you uncomfortable, tell me and I’ll rephrase.
我刚才以为你在生气，没敢笑。|I thought you were angry, so I didn’t dare laugh.
我没生气，是汤太咸。不是说他所有菜都做得不好。|I’m not angry; the soup is salty. I don’t mean he cooks everything badly.
好，我明白了。不过别叫我傻，我不喜欢。|Okay, I understand. But please don’t call me silly; I dislike it.
好，不这样叫。刚才也不是在说你。|Okay, I won’t. I wasn’t referring to you earlier either.
真有你的，能把一道汤放两次盐。|Well, look at you—managing to salt one soup twice.
别再说了，我已经拿水来了。|Enough about it. I’ve brought water already.
行，不说了。你准备加多少？|Okay, I’ll stop. How much will you add?
先加一点，再尝，不把整瓶都倒进去。|A little first, then taste, not the whole bottle.
这次终于先尝了。|Finally tasting first this time.
我说别再说，你还来一句？|I asked you to stop, and you add another line?
对不起，这句也收回。我去拿碗。|Sorry, I take that one back too. I’ll get the bowls.
拿三个就行，你这次不用替盐拿一碗。|Three is enough. No need for a bowl for the salt this time.
''')
M=rows('''
外面雨这么大，我们挑的天气可真好。|With that heavy rain outside, we picked such lovely weather.
你是在说天气不好吧？|You mean the weather is bad, right?
对，本来想去公园，现在只能在家。|Yes. We wanted the park, but are staying home now.
那今天也不错，有汤喝。|Still not a bad day: there is soup.
你还没尝，别急着说不错。|You haven’t tasted it. Don’t say it’s good yet.
我只说有汤，没说味道。|I said there is soup, not how it tastes.
这话听起来真小心。|That sounds very cautious.
毕竟我看见你放了两次盐。|After all, I saw you add salt twice.
你居然一直看着。|You were watching the whole time?
我就在旁边洗菜，想不看也难。|I was washing vegetables beside you; hard not to notice.
好，先尝，再决定要不要加水。|Okay, taste first, then decide about water.
我只拿小勺，给自己留条路。|I’m taking a small spoon, leaving myself a way out.
''')
R=rows('''
周末我们本来想去公园，下午却下了很大的雨。三个朋友改到我家吃饭，其中两个人很熟，另一位是第一次来。我做了一道汤，一边接电话，一边找调料。电话结束以后，又照平时的习惯放了一次盐，等尝的时候才发现太咸。我说可能放了两次，朋友看着汤笑，说我可真会放盐。|Rain moved our planned park visit to my home. Two of the three friends knew each other well; one was visiting for the first time. While cooking soup I took a call and added salt, then added it again out of habit. When I noticed the saltiness, a friend smiled at the soup and said I certainly knew how to add salt.
如果只把这句话写下来，看起来像夸我有一种技能。可是前面已经说明汤很咸，后面他又说今天不用再吃别的盐，这些内容放在一起，才听得出他是在笑我放多了。他没有真的认为我这一次做得特别好，也没有因此说我什么菜都不会做。评价落在这道汤和这次失误，不必扩大成整个人的能力。|In writing alone it resembles praise for a skill. The stated saltiness and following line about needing no other salt identify the tease. He neither praised this cooking result nor claimed I could cook nothing. The comment concerns this soup and slip rather than my entire ability.
第一次来的朋友没有笑。她后来悄悄问，我们是不是已经开始吵架。我才知道，熟悉的人听懂的东西，对她不一定清楚。她没有看过我们以前怎么说，也不知道笑的时候能不能跟着笑。我们解释说没有生气，汤确实太咸了；她还是可以不笑，不需要先证明自己也喜欢这种幽默。|The newcomer didn’t laugh and quietly asked if an argument had begun. Familiar exchanges were not necessarily clear to her; she didn’t know our history or whether to join in. We explained the actual soup problem and lack of anger, without requiring her to enjoy the humour.
她说自己不喜欢被叫作傻，我马上答应不这样叫。这个要求和她有没有听懂前面的意思，是两件事。她即使明白对方没有真的骂她，也可以不喜欢某种称呼；我们不能用“只是逗你”让她一定忍受。那位朋友说，刚才指的是我的放盐，不是在说她，不过以后也不会随意拿这个字叫她。|She disliked being called silly and we agreed not to. Understanding an intention and liking a form of address are different. Even without an intended insult she needn’t tolerate a disliked name because it is supposedly just teasing. The friend clarified the cooking reference and would avoid addressing her that way.
我拿了水来，想先加一点再尝。另一个人又说真有我的，一道汤可以放两次盐。我起初也笑，可他连续说了几次，我就告诉他别再说了。他答应，却又加了一句“这次终于先尝了”。我问，已经说停了，怎么还要补一句。他这才道歉，不再拿同一件事说，转身去拿碗。|I brought water to add a little and taste again. Another tease about salting twice initially amused me, but repetition didn’t. I asked him to stop. He agreed yet added another remark about finally tasting first; I pointed out the contradiction. He apologised and got the bowls instead.
后来我自己说，拿三个碗就行，这次不用替盐拿一个。大家笑了一下，也就接着吃饭。我这次愿意自己说，不代表前面要求停是假的，也不代表以后别人可以一直说。一次交流里面，一个人可以先觉得好笑，再觉得太多，又在改变话题以后重新放松。这些变化要看他实际说了什么，不是只靠朋友两个字决定。|I then joked that three bowls were enough, without one for the salt. My willingness to joke did not invalidate the earlier stop request or license endless repetition. Someone can find a joke funny, tire of it and relax again after the conversation moves on; actual responses matter beyond simply being friends.
吃饭时，我们又谈到外面的雨。有人说挑的天气真好，新朋友这次马上问，是不是在说本来想去公园，现在去不了。他说对，也说现在在家喝汤不错。同样一个“好”，前一句带着和实际情况相反的意思，后一句却真是在说另一个方面。她把前后连起来问，比直接判断说好就一定在夸，更容易听清。|Over dinner “lovely weather” referred ironically to our cancelled park trip, whereas enjoying soup at home was a sincere positive comment on a different aspect. The newcomer checked the context. The same word need not carry the same intention in successive remarks.
我后来回想，没有把那天下午记成每句话都要猜反话。有人认真问加多少水，有人客气地说谢谢，也有人只是想把话停下来。幽默只是其中一部分。听不准时问清楚，听到对方要求停就真的停，比努力把每句话都说得很聪明更重要；吃饭本来是为了见面，不是让一个人整晚承担大家所有笑声。|I didn’t remember an afternoon where every sentence had to be inverted. Questions about water, polite thanks and requests to stop were sincere. Humour was one part; checking uncertainty and actually stopping mattered more than constant cleverness. The gathering was for company, not making one person carry every joke all evening.
''')
P=rows('''
第一次去朋友家吃饭，我最担心的不是汤好不好喝，而是不知道什么时候该跟着笑。两位朋友认识很久，说话很快。我听见一个人说“你可真会放盐”，看见另外一个笑，自己却不明白是在夸还是在生气。汤看起来和别的汤差不多，我还没有尝，所以没有他们刚才已经知道的那一口味道。|At a first visit I worried about joining laughter more than the soup. Two longstanding friends spoke quickly. “You certainly know how to add salt” might be praise or anger; I hadn’t tasted the soup and lacked that shared information.
我先没有插话，后来悄悄问。朋友把前面放了两次盐的事讲给我，又解释后面那句今天不用吃别的盐。听到完整过程，我才知道笑声和哪一件事有关。这个解释没有让我突然喜欢所有类似的说法，却让我知道这一次不是吵架。我也不用一直猜，是不是自己没笑，就已经得罪了谁。|A quiet question brought the double-salting story and follow-up remark. The explanation connected laughter to a specific event without making me enjoy every similar phrase. It relieved my fear that not laughing was an offence.
我告诉他们，不喜欢有人叫我傻。以前有人这样叫，我说不喜欢，他就说我太认真，后来还继续。我这次想早点讲，不等到自己已经很难受才说。朋友没有要求我先接受他的意思，才允许我不喜欢，而是直接答应不用这个称呼。那一刻我觉得自己可以留在桌边，不必装作和他们认识了很多年。|I stated a dislike of being called silly because past requests to stop had been dismissed. This time I wanted to speak early. A direct agreement, without requiring approval of his intention first, let me stay without pretending years of familiarity.
后来做汤的人也要求停止重复。我原来以为他们熟，就不会在意，结果看见他从笑变成认真说“别再说了”。另一个人又补一句，他就再次提醒。我才发现，刚才笑过并不是后面一直笑的保证。真正熟悉的人也需要听见这个变化，不是把所有不舒服都当成对方脾气突然不好。|The cook’s later stop request showed that familiarity did not mean unlimited tolerance. Laughing earlier didn’t guarantee laughing forever. Friends too needed to notice a change rather than attribute discomfort to a bad temper.
拿碗以后，做汤的人自己又开了一句盐的说法。我没有把这句理解成前面的要求不算数。他是在别人已经停下以后，选择自己再说一点，而且随后就开始吃饭，没有继续把同一件事绕下去。我也笑了，因为这次知道前后经过，听见他自己愿意这样说。下次他愿不愿意，还要看下次，不是今天一次笑就全都决定。|After the others stopped, the cook chose his own short salt joke and moved on to dinner. That didn’t cancel his earlier request. Knowing the context and hearing his willing contribution let me laugh; it didn’t decide what he would want on another occasion.
后来雨一直下，朋友说挑的天气真好。我看见他指向窗外，就问是不是说公园去不了了。他说对，接着又说在家也挺好。这次我没有把第二个好也理解成坏，因为他说的是在家能一起吃饭。只看相同的词不够，还要听现在到底评价什么，是天气、安排，还是有人做的一道菜。|Persistent rain prompted “lovely weather” while he pointed outside. I checked the cancelled park visit; the following sincere approval concerned eating together at home. Repeated vocabulary did not guarantee repeated intention: the object being evaluated mattered.
我也有一次没听清最后几个字，问他能不能再说。他重复得慢一点，没有变成很大声地对着我喊。我听懂以后回应一句，大家就继续聊了。能问，也能让对方重复，让我更愿意参加；不必每次都猜中，也不必为了不打断就一直点头，等回家以后才发现自己答应了什么。|When I missed a few final words, he repeated more slowly without shouting. I responded and conversation continued. Being able to ask and hear a repeat helped participation without always guessing or nodding through an unclear commitment.
回家以后，我给朋友发了一条谢谢，说汤后来好了，聊天也让我放松。我没有说自己已经学会判断所有反话；这一次只是知道怎样补上没听见的部分，怎样说一个不喜欢的称呼。下次如果关系、事情或神情不同，同样一句话可能又要重新问。认识新朋友，是慢慢有共同经历，不是第一次就把所有句子都按同一种意思读。|My thanks noted the improved soup and relaxed company. I had not mastered all irony; I’d learned to recover missing context and name a disliked form of address. With a different relationship, event or expression, the same words could need checking again. Familiarity grows through shared experiences rather than one universal interpretation on day one.
''')
G=[
card('居然…','Mark an unexpected event','居然 presents an outcome as surprising to the speaker. It does not itself say the outcome is good or bad.','我居然把盐放了两次。|I unexpectedly added salt twice.\n他居然记得我以前说过的话。|He unexpectedly remembers what I said before.','我居然把盐放了两次，所以居然总是夸奖。','我居然把盐放了两次。','The adverb marks surprise, not automatic praise.'),
card('明明…，却/还…','Highlight a contradiction with an apparent fact','明明 presents what the speaker treats as clear. 却 or 还 introduces a conflicting action or claim; check the context rather than assuming the speaker is infallible.','明明汤很咸，他还说真会放盐。|The soup is clearly salty, yet he says I’m good at adding salt.\n明明已经到了，却说还在路上。|They have clearly arrived, yet say they are still on the way.','明明汤很咸，所以一定没有放盐。','明明汤很咸，他还说真会放盐。','The contextual contradiction helps identify the tease, not a missing ingredient.'),
card('可 + assertion/negative','Recognise conversational emphasis','This use of 可 adds emphasis. Its force depends on the rest of the line and the situation; 可真 is not an automatic label for anger or praise.','我可没答应一直来。|I certainly didn’t promise to keep coming.\n这句话可不一定是在夸。|This line certainly isn’t necessarily praise.','只要说可真，就一定在生气。','听到可真，还要看前后发生了什么。','The form marks emphasis but does not uniquely determine emotion.'),
card('真有你的','Read an evaluation through the situation','The fixed expression can admire an achievement or tease a surprising mistake. Nearby events and the addressee’s response establish the local reading.','真有你的，这么快就修好了。|Impressive—you fixed it so quickly.\n真有你的，一道汤放两次盐。|Well, look at you—salting one soup twice.','真有你的，所以这次放盐一定恰好。','真有你的，一道汤放两次盐。','Here the preceding mistake prevents a simple literal praise reading.'),
card('X什么X','Recognise a dismissive rhetorical challenge','Repeating the verb around 什么 often challenges the action rather than asking for an object. It can be sharp; compare a straightforward information question.','笑什么笑，先尝了再说。|What are you laughing at? Taste it before commenting.\n急什么急，还没到时间呢。|Why the rush? It isn’t time yet.','急什么急是在问急的物品是什么。','急什么急，还没到时间呢。','This is a challenge to rushing, not an object-identification question.'),
]
spec=dict(title=('When praise is a tease','这句是在夸吗'),goals=['Use preceding events and responses to interpret irony','Distinguish teasing about an event from a literal general judgment','Ask for clarification or stop repetition without pretending agreement'],vocabulary=V,grammar=G,
dialogue=(D,[q('gist','How does the newcomer’s uncertainty get resolved?','Friends explain the salt incident and respect a disliked name','Everyone demands laughter before giving an explanation','The soup’s actual taste is never mentioned'),q('detail','What request is initially not fully followed?','The cook’s request to stop repeating the salt joke','A demand to pour in the entire water bottle','A request to cancel all future visits'),q('inference','What does the cook’s own later joke not establish?','Permission for endless future teasing','That the earlier stop request happened','That the gathering continues over dinner')]),
reading=(R,[q('gist','What guides interpretation and repair?','Context and actual responses, including requests to stop','Every positive adjective always means the opposite','Familiarity removes the need to listen'),q('detail','Why is the soup salty?','Salt was added twice while a phone call interrupted cooking','No salt was added at all','Every guest poured a full bottle into it'),q('inference','Why is the second remark about staying home sincere?','It evaluates enjoying company at home rather than the bad weather','Every good has the same intended meaning','The park trip has definitely resumed')]),
pairedTitle='The first-time guest',pairedReading=(P,[q('gist','What makes participation easier for the newcomer?','Explanation, repetition and respected preferences','Guessing every sentence without asking','Being required to enjoy all joking'),q('detail','What does the newcomer ask not to be called?','傻','陈宇','朋友'),q('inference','Why is laughing once not a universal rule?','Situation and willingness can change later','Laughter proves everyone has the same preference','Requests to stop automatically become false')]),
mediaTitle='Such lovely weather',media=(M,[q('detail','Why are the friends staying home?','Heavy rain prevents the park plan','The park was never planned','The soup proves clear weather'),q('inference','What does the small-spoon comment do?','Playfully expresses caution about tasting salty soup','Guarantees the soup tastes perfect','Demands a separate bowl for the salt')]),
glosses=[('盐','salt'),('聪','clever, as in 聪明'),('聪明','clever'),('缓','ease; slow'),('缓解','ease; alleviate'),('调料','seasoning'),('尴尬','awkwardness'),('逗','tease; amuse'),('称呼','form of address'),('口味','taste; flavour'),('插话','interject'),('反话','ironic wording meaning more than a literal reading'),('承担','bear; take on'),('频繁','frequent'),('客气','polite; formal'),('勺','spoon'),('得罪','offend'),('绕','go around; circle back'),('讲台','lectern'),('前后','preceding and following context')],
place='A rainy-day meal at a friend’s home',context='One soup is accidentally salted twice. A newcomer asks about the joke; a repeated tease is stopped after a second reminder.',
turns=[('你说真会放盐，是夸好喝吗？','Is good at adding salt praise for its taste?','Use the known context',['不是，这次放了两次，太咸了。']),('我不喜欢被这样叫，可以不用吗？','I dislike being called that; could you stop?','Respect the specific preference',['可以，以后不这样叫。']),('刚才笑了，现在就不能让我停吗？','You laughed before; can you not ask me to stop now?','Allow a changed response',['可以，刚才觉得好笑，现在不想再听了。'])],
usage=[('Check an uncertain interpretation','你是在笑这次放多了，不是在生气，对吗？','You’re teasing about adding too much this time, not angry, right?','Name the event and ask; do not assume a vocal cue has only one meaning.'),('Make a concrete stop request','这件事别再说了，我们先吃吧。','Please stop repeating this one; let’s eat.','A bounded request makes the wanted change clear.'),('Repair after missing the request','对不起，我刚才又说了一句。现在停。','Sorry, I added another line. I’ll stop now.','Follow an apology with the actual change, rather than another repetition.')],
tasks=practice(
[(D[7][0],D[7][1],'The speaker says the cook is unable to cook any dish.',False,'The explanation explicitly limits criticism to this soup.'),(D[15][0],D[15][1],'The cook reminds the friend of an earlier request to stop.',True,'The extra remark follows that request.'),(R[5][0],R[5][1],'The cook’s own joke cancels all earlier limits.',False,'The text explicitly keeps the stop request valid.'),(P[6][0],P[6][1],'A repeat at a slower pace helps the newcomer respond.',True,'The speaker repeats more slowly without shouting.')],
 [('汤放了两次盐，很咸。他笑着说真会放盐。是在认真夸味道好吗？','The soup was salted twice and tastes salty. He smiles and says good at adding salt. Is this sincere praise of flavour?',['不是，是在笑这次放多了。','是，说明盐放得刚刚好。','是，而且证明任何菜都很好。'],0,'The explicit mistake and smile establish the local tease.'),('我已经说别再说了，你又加一句。怎么回应？','I asked you to stop, but you added another line. How should you respond?',['对不起，这句也收回，现在停。','你刚才笑过，所以我永远不能停。','你说停，就是让我再说十次。'],0,'Repair follows the actual request instead of denying it.'),('刚才说天气真好，是因为大雨去不了公园。后来在家挺好，指一起吃饭。两个好一样吗？','Lovely weather refers to rain cancelling the park; good at home refers to company over dinner. Do both good remarks mean the same thing?',['不一样，前后评价的事情不同。','一样，所有好都只能表示坏。','一样，所以外面根本没有雨。'],0,'The evaluated situations differ.')],
 [('我居然把盐放了两次。','I unexpectedly added salt twice.','居然'),('这句话可不一定是在夸。','This line certainly isn’t necessarily praise.','可'),('我不想强迫你跟着笑。','I don’t want to force you to laugh along.','强迫')],
 [[(V[i][3],V[i][4]) for i in [0,4,5]],[(V[i][5],V[i][6]) for i in [8,13,17]],[(V[i][3],V[i][4]) for i in [18,21,23]]]),
review='Native review: teasing strength, 真有你的/可真 intonation, the final salt-bowl comeback and X什么X sharpness. Self-review separates interpretation from enjoyment and one laugh from future permission. Salt is added twice; water is added a little at a time, never a complete bottle by assertion. The newcomer lacks the initial tasted-soup context. Same 好 changes referent between rain and company; positive forms are not labelled universally ironic. Fallback audio does not certify ironic prosody. No real performer or copyrighted scene is used.')
# The newcomer has distinct turns: do not misattribute them to the cook.
spec['dialogueSpeakers']=[dict(id='a',name='林安'),dict(id='b',name='陈宇'),dict(id='c',name='小周')]
spec['dialogueSpeakerIds']=['a','b','a','b','c','b','c','b','c','b','b','a','b','a','b','a','b','a']
write(5,11,spec,publish='--publish' in sys.argv)
