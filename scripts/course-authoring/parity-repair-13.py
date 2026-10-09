"""Friend scenes replace abstract policy lectures without forcing word coverage."""
import json,sys
from common import ROOT,py
from advanced_core import rows
from editorial_repair import repair,tf,reply,fill,match
from parity_repair_13_contexts import VOCAB

TEXTS={
17:(
'''今天还想去那个热闹的活动吗？|Do you still want to go to that lively event today?
我有点累，想找个安静的地方坐坐。|I'm a little tired. I'd like somewhere quiet to sit.
那我们去河边的小店吧，里面人少。|Let's go to the little shop by the river. It's quieter inside.
会不会耽误你？你不是想看演出吗？|Will that hold you up? Didn't you want to see the show?
不急。对我来说，跟你见面更重要。|No rush. Meeting you matters more to me.
谢谢。那家店我没去过，茶怎么样？|Thanks. I haven't been there. How's the tea?
挺好，窗边还有两把椅子。我先问问有没有位子。|Good. There are two chairs by the window. I'll ask if they're available.
好。我不想让你白跑，晚点还可以去听一首歌。|Okay. I don't want to waste your trip. We could still hear a song later.
先喝茶吧，喝完再看你想不想去。|Let's have tea first and see how you feel afterwards.
行，你已经出门了吗？|Okay. Have you left yet?
还没。你到了，发消息给我。|Not yet. Message me when you arrive.
好，我先慢慢走过去。|Okay. I'll walk over slowly.
''',
'''今天我和陈宇约好去听演出，出门以前却觉得累。我给他发消息，说想找一个安静的地方坐坐，他提议去河边的小店。|Chen Yu and I had planned to see a performance today, but I felt tired before leaving. I messaged that I'd like somewhere quiet to sit; he suggested the little shop by the river.
我怕他失望，问要不要他先去看演出。他说今天主要是想和我见面，演出下次也能听。我看到这句话，心里轻松了一点。|Worried he'd be disappointed, I asked if he'd like to go to the show first. He said he mainly wanted to see me today; the show could wait. Reading that made me feel more relaxed.
到店里以后，我找了窗边的两把椅子。陈宇过来时带了一本薄书，说以前在那里读过，想给我看看。|At the shop I found two chairs by the window. Chen Yu arrived with a slim book he'd read there before and wanted to show me.
我们点了茶，他翻到里面的一张照片。照片里是一条我小时候走过的路，我指给他看。他说去年也去过那里，我们就聊起那条路旁边的小店。|We ordered tea. He turned to a photo of a road I'd walked along as a child. I pointed it out. He said he'd been there last year too, and we talked about the little shops beside that road.
聊了一会儿，我不那么累了。他问还想不想去听歌，我说今天就坐在这里吧。这本书还没看完，茶也很好喝。|After chatting I felt less tired. He asked if I wanted to hear music now. I'd rather stay here today, I said; I hadn't finished the book and the tea was good.
傍晚我们一起走到车站。他说下次还坐窗边，我说好，不过这次的书先借我。他把书递来，说椅子不能借，书可以。|That evening we walked to the station together. He suggested the window seats again next time. Yes, I said, but could I borrow today's book first? He handed it over: the chairs couldn't be borrowed, but the book could.
''',
'''椅子不能借，书可以。|You can borrow the book, but not the chair.
我家有椅子，缺的是这本书。|I have chairs at home. It's this book I need.
那茶呢？|What about the tea?
茶已经喝完了。|We've finished the tea already.
好，至少不用帮你搬椅子。|Good. At least I don't have to move a chair for you.
不用，你下次记得来就行。|No need. Just remember to come next time.
'''),
18:(
'''周日来我家做客吧，奶奶也在。|Come to my home on Sunday. Grandma will be there too.
好啊。几点来合适？|I'd love to. What time would suit you?
三点吧，先喝茶，晚饭一起吃。|Three. We'll have tea first and dinner together.
我带点水果？|Shall I bring some fruit?
可以。奶奶喜欢橙子，我给你发地址。|Sure. Grandma likes oranges. I'll send the address.
她是不是喜欢听京剧？你以前说过。|Does she like Peking opera? You mentioned it before.
对，周日下午她常听。你可以向她请教，她知道好多故事。|Yes. She often listens on Sunday afternoons. You could ask her; she knows lots of stories.
我怕听不懂，她会不会笑我？|I'm afraid I won't understand. Will she laugh at me?
不会。我也常问，她每次都讲得很高兴。|No. I ask often too, and she's always happy to explain.
好，那我带橙子，也带上问题。|Okay. I'll bring oranges and some questions.
问题不用装袋子，橙子要。|No bag needed for the questions. The oranges need one.
放心，橙子我会装好。|Don't worry. I'll pack the oranges properly.
''',
'''周日陈宇请我去家里做客，我三点到，带了一袋橙子。奶奶在客厅听京剧，见我进来，就把声音调小，招呼我坐下。|Chen Yu invited me over on Sunday. I arrived at three with oranges. Grandma was listening to Peking opera in the living room; she turned it down when I came in and welcomed me.
我问奶奶，这段讲的是什么。她指着屏幕，先介绍两个角色，再讲他们为什么在这里见面。我听懂以后，再看就有意思多了。|I asked Grandma what this scene was about. Pointing to the screen, she introduced the two characters and explained why they were meeting here. Understanding that made it much more interesting.
陈宇端来茶，说他小时候也像我一样，总问同一个问题。奶奶说他那时更爱问，问完还要跟着唱两句。|Chen Yu brought tea and said he'd asked the same questions as a child. Grandma said he'd asked even more, then tried singing a couple of lines himself.
我们聊到附近的公园。奶奶说国庆的时候，那里有京剧和武术表演，陈宇去年陪她看过。我说今年也想去，他们就让我到时一起。|We talked about the nearby park. Grandma said it had Peking opera and martial arts performances over National Day. Chen Yu had gone with her last year. I'd like to go this year too, so they invited me along.
晚饭前，我帮陈宇把碗放好。他让奶奶再说一段，我才发现她不看屏幕，也记得那些人物的名字和话。|Before dinner I helped Chen Yu set out bowls. He asked Grandma to tell us another part. I realised she knew the characters' names and lines without looking at the screen.
回家时，她塞给我两个橙子，说路上带着。我说本来是送给她的，她笑着说吃了一下午，还想让我明天也尝尝。|When I left she gave me two oranges to take. I'd brought them for her, I said. She laughed that she'd had some all afternoon and wanted me to enjoy them tomorrow too.
''',
'''你小时候也跟着唱？|You sang along as a child too?
就两句，奶奶听得懂就行。|Just two lines. As long as Grandma understood.
现在来一句？|How about a line now?
先吃饭，唱完饭可能凉了。|Dinner first. The food might get cold if I sing.
那明年国庆再听？|Shall I wait until next National Day to hear it?
别急，饭吃完再说。|Don't rush. Ask me again after dinner.
'''),
19:(
'''我到门口了，怎么没看见你？|I'm at the entrance. Why can't I see you?
你在哪个门？我在东门。|Which entrance? I'm at the east gate.
你发的地址写西门，我在西门啊。|The address you sent says west gate. That's where I am.
对不起，我发了上次的地址，忘了改。|Sorry. I sent the previous address and forgot to change it.
那我还要走多久？|How much farther do I have to walk?
大约十分钟。我过去接你吧。|About ten minutes. I'll come and meet you.
好，我在西门旁边的小店等。|Okay. I'll wait at the little shop by the west gate.
你先坐下，别在太阳底下等。|Have a seat. Don't wait in the sun.
行。我还以为今天没有活动。|Okay. I thought there was no event today.
有，是我发错了。新的地址已经发送给你。|There is. My mistake. I've sent you the new address.
收到了，这次也有门口的照片。|Got it. There's a photo of the entrance too this time.
对，我快到了，先给你买瓶水。|Yes. I'm almost there. I'll get you a bottle of water first.
''',
'''我按照陈宇发的地址到了西门，却没看见他。打电话才知道，他在东门，地址是上次的。他马上道歉，说忘了改。|I followed Chen Yu's address to the west gate but couldn't see him. On the phone I learnt he was at the east gate; he'd sent the previous address. He immediately apologised for forgetting to change it.
从西门到东门大约十分钟，太阳又大。我问应该怎么走，他说先找地方坐下，他过来接我。我就在小店门口等。|It was about ten minutes to the east gate, under a strong sun. I asked the way. He told me to find a seat and he'd come over, so I waited by the little shop.
他给我发送了新地址和门口照片，我放大照片一看，上面挂着今天活动的名字。这才知道刚才找不到的原因。|He sent the new address and a photo of the entrance, showing today's event name. That explained why I hadn't been able to find it earlier.
陈宇过来时，手上拿着两瓶水。他又说对不起，我说没事，先喝一口再走。他把另一瓶给我，带我从旁边的小路过去。|Chen Yu arrived with two bottles of water and apologised again. It was okay, I said; let's have a drink before walking. He handed me a bottle and led me along the little path.
到东门以后，我们看见几个朋友也刚到。陈宇把新地址和照片一起发到群里，又问有没有人已经去了西门。|At the east gate some friends were arriving too. Chen Yu sent the new address and photo to the group and asked if anyone else had gone to the west gate.
只有我走错了，大家都笑着说我替他们看过另一边。我说下次就让我发地址，陈宇说好，不过今天先进去，第一首歌已经开始了。|Only I'd gone to the wrong gate. Everyone joked that I'd checked the other side for them. Next time I'd send the address, I said. Okay, said Chen Yu, but let's go in now; the first song had begun.
''',
'''下次让我发地址。|Let me send the address next time.
好，你已经认识两个门了。|Okay. You know both gates now.
多认识一个门，多走十分钟。|One more gate, ten more minutes walking.
我下次先带水。|I'll bring water first next time.
先发对地址，水我自己带。|Send the right address first. I'll bring my own water.
行，这次记住了。|Okay. I'll remember this time.
'''),
20:(
'''小周生日，你准备送什么？|What are you giving Xiao Zhou for her birthday?
我做了一个布袋，她平时带书，可以用。|I made a cloth bag. She carries books, so it should be useful.
你自己设计的？让我看看。|You designed it yourself? Let me see.
蓝色的布，里面加了一层，袋口有个扣子。|Blue cloth, with another layer inside and a button at the opening.
金色扣子？不会真是金的吧？|A gold-coloured button? Don't tell me it's real gold?
想得美，就是普通扣子，好看一点。|You wish. It's an ordinary button. Just looks nice.
那这张彩色卡也是你做的？|Did you make this coloured card too?
对，用了我们上次旅行的照片。她看见应该会笑。|Yes. With a photo from our last trip. It should make her laugh.
哪张？不会是她拿着两杯茶那张吧？|Which one? Not the one where she's holding two cups of tea?
就是那张，卡上写祝你每天都有好茶。|That's the one. The card wishes her good tea every day.
那袋子是不是应该装茶，不装书？|Should the bag hold tea rather than books, then?
先装书吧，茶倒进去就不好洗了。|Books first. Tea poured inside would be hard to wash out.
''',
'''小周生日快到了，我想给她做一个能装书的布袋。家里有一块蓝色布，我先画了设计图，再把里面加上一层。|Xiao Zhou's birthday was approaching. I wanted to make her a cloth book bag. I had blue cloth at home, drew a design and added an inner layer.
袋口需要一个扣子，我去附近的小店买。银色和金色都有，我选了金色，付了五元现金，回家把它缝好。|I needed a button for the opening and went to the nearby shop. It had silver-coloured and gold-coloured ones. I chose gold-coloured, paid five yuan in cash and sewed it on at home.
陈宇来看袋子，问是不是我自己设计的。我说是，这个袋子只能手提，不过装书很方便。他把自己的书放进去，两本都装下了。|Chen Yu came to see the bag and asked if I'd designed it. Yes; it could only be carried by hand, but was handy for books. He tried his books, and both fitted.
我又做了一张彩色卡，用了上次旅行时小周拿着两杯茶的照片。为了让她想起那一天，我写了祝你每天都有好茶。|I made a coloured card with the travel photo of Xiao Zhou holding two cups of tea. To remind her of that day I wrote a wish for good tea every day.
生日那天，她打开袋子，先看见卡，就笑了。她说那天明明是替陈宇拿茶，照片里却像两杯都是自己的。|On her birthday she opened the bag, saw the card and laughed. She'd actually been holding Chen Yu's tea that day, but the photo made both cups look like hers.
她把卡收进袋子，说这张要留作纪念，书也正好能放。我问扣子喜欢吗，她说喜欢，像袋口有一点小太阳。|She put the card into the bag, saying she'd keep it as a souvenir and her books would fit too. Did she like the button? Yes; it was like a little sun at the bag's opening.
''',
'''那两杯茶有一杯是你的。|One of those two cups was yours.
我知道，可她拿着，看起来更稳。|I know, but she was holding it and looked steadier.
你只负责拍照？|You just took the photo?
对，茶的颜色很好看。|Yes. The tea had a lovely colour.
下次你拿，我拍。|Next time you hold it and I'll take the photo.
那卡上写祝我别洒就行。|Then the card can just wish me not to spill it.
''')}

QUESTIONS={
17:([
('gist','How do they adjust their meeting?',['Choose a quiet shop instead of the lively show','Cancel their friendship','Meet at a furniture shop'],0),
('detail','Which seats does Chen Yu ask about?',['Two by the window','Four outside','One onstage'],0),
('inference','Why does Chen Yu agree to the change?',['Seeing the friend matters more to him','The show has no music','The friend needs a new phone'],0)],[
('gist','What makes the meeting enjoyable?',['Tea, a shared memory and a borrowed book','A competition for chairs','Watching the whole performance'],0),
('detail','What does the narrator borrow?',['The slim book','A chair','The shop’s phone'],0),
('inference','Why do they stay at the shop?',['The narrator enjoys the book and tea','They cannot walk to the station','The owner forbids leaving'],0)]),
18:([
('gist','What do they plan?',['A Sunday visit with tea, dinner and opera stories','A martial arts lesson at nine','A book sale at school'],0),
('detail','What fruit will the guest bring?',['Oranges','Apples','Grapes'],0),
('inference','Why does Chen Yu think Grandma will explain willingly?',['She enjoys explaining when he asks too','She has never heard opera','She wants questions in a bag'],0)],[
('gist','What is the visit like?',['Grandma shares opera stories and invites the guest to a future outing','The guest never meets Grandma','They visit a museum instead'],0),
('detail','What makes the opera scene easier to follow?',['Grandma explains the characters and their meeting','The guest switches off the screen','Chen Yu sells tickets'],0),
('inference','Why does Grandma give the guest oranges?',['To share some for the next day','To reject the entire gift','To pay for a map'],0)]),
19:([
('gist','Why have they missed each other?',['Chen Yu sent the old entrance address','The event has been cancelled','Both phones are broken'],0),
('detail','Where does the narrator wait?',['The little shop by the west gate','Onstage at the east gate','At home'],0),
('inference','Why does Chen Yu offer to come over?',['To meet the friend after his address mistake','To leave the event permanently','To buy a new phone'],0)],[
('gist','How is the wrong-address problem resolved?',['Chen Yu sends the correction, meets the friend and informs the group','Everyone cancels the event','The narrator never reaches the east gate'],0),
('detail','How many friends went to the wrong gate?',['Only the narrator','All of them','Three besides Chen Yu'],0),
('inference','Why send the photo to the group?',['To help everyone identify the correct entrance','To replace the first song','To advertise the water'],0)]),
20:([
('gist','What gift is being prepared?',['A cloth book bag and a photo card','A real gold box','Two cups full of tea'],0),
('detail','What colour is the cloth?',['Blue','Silver','Red'],0),
('inference','Why use the two-cup photo?',['It recalls their funny travel moment','It proves the button is gold','It shows where to pay cash'],0)],[
('gist','How does Xiao Zhou respond to the gift?',['She laughs at the card and likes the bag','She refuses the bag','She asks for all the cash back'],0),
('detail','How much did the button cost?',['Five yuan','Twenty yuan','Fifty yuan'],0),
('inference','Why does she want to keep the card?',['As a memory of the trip','To cover a hole in the bag','To buy another button'],0)])}

REPLIES={
17:[('我有点累，想找个安静的地方坐坐。','I’m tired and would like somewhere quiet to sit.',['那去河边的小店吧。','那我们去最热闹的地方。','扣子是五元。']),('这次的书先借我，好吗？','Could I borrow today’s book?',['好，给你，下次再还。','好，把椅子搬回家吧。','她喜欢吃橙子。'])],
18:[('周日三点来，奶奶也在。','Come at three on Sunday; Grandma will be there.',['好，我带点橙子。','好，我周一才去。','新地址是东门。']),('这段讲的是什么？','What is this scene about?',['我先给你介绍这两个人。','水果都放在袋里了。','我去买个扣子。'])],
19:[('对不起，我发了上次的地址。','Sorry, I sent the previous address.',['那你把新地址发给我吧。','所以是我发错了。','那本书还没看完。']),('你先坐下，我过去接你。','Have a seat; I’ll come to meet you.',['好，我在西门的小店等。','好，我立刻回家不等了。','奶奶听京剧。'])],
20:[('这个金色扣子是真金的吗？','Is this gold-coloured button real gold?',['不是，就是普通扣子。','对，蓝色布有两层。','明天去东门。']),('哪张照片？两杯茶那张吗？','Which photo? The two-cup one?',['对，她看到应该会笑。','不是，我就用了两杯茶那张。','我上午还有课。'])]}

GLOSSES=[('林安','Lin An, a name'),('陈宇','Chen Yu, a name'),('小周','Xiao Zhou, a name'),('薄书','slim book'),('薄','thin'),('翻','turn pages'),('递','hand over'),('耽误','hold up; delay'),('失望','disappointed'),('轻松','relaxed'),('放在心上','care about; keep in mind'),('随身','on one’s person'),('随身带好','keep with oneself'),('怪','blame'),('陶杯','pottery cup'),('陶','pottery'),('用心','care; thoughtfulness'),('平静','calm'),('思念','miss someone'),('细','subtle; fine'),('状况','condition'),('橙子','orange'),('客厅','living room'),('调小','turn down'),('招呼','greet; welcome'),('屏幕','screen'),('角色','character; role'),('端','carry in the hands; serve'),('国庆','National Day'),('塞','stuff; press into someone’s hands'),('袋','bag'),('吃','eat'),('服饰','clothing and accessories'),('社团','club'),('文明','civilisation; courteous'),('纪念碑','monument'),('建于','built in'),('建','build'),('镜头','camera lens; shot'),('大自然','nature'),('华人','people of Chinese heritage'),('当','serve as; when'),('东门','east gate'),('西门','west gate'),('太阳','sun'),('放大','enlarge; zoom in'),('挂','hang'),('道歉','apologise'),('瓶','bottle'),('群','group'),('另一边','the other side'),('由于','owing to'),('维修','repair; maintain'),('暂时','temporarily'),('绕行','detour'),('绕','go round'),('报道','report news'),('退货','return goods'),('停课','suspend classes'),('设备','equipment'),('冰箱','fridge'),('洞','hole'),('彼此','each other'),('伤','injure; injury'),('信任','trust'),('作者','author; creator'),('设计图','design drawing'),('扣子','button'),('金色','gold-coloured'),('银色','silver-coloured'),('层','layer'),('缝','sew'),('手提','carry by hand'),('装下','fit inside'),('洒','spill'),('稳','steady'),('普通','ordinary'),('想得美','you wish; teasing rejection'),('义卖','charity sale'),('项链','necklace'),('戒指','ring'),('耳环','earring'),('旅途','journey'),('环境','environment'),('防水','waterproof'),('功能','function'),('适用','suitable for use'),('消费','spending'),('创新','innovation')]

GLOSSES += [('辛苦','hard work; tiring'),('陪','accompany'),('邀请','invite'),('研究','study; research'),('诗歌','poetry'),('幅','classifier for pictures'),('建筑','building; architecture'),('戴','wear an accessory'),('请教','ask for someone’s knowledge or advice')]

for number,(d,r,m) in TEXTS.items():
    pack=json.loads((ROOT/f'content/packs/s3-u{number:02}.json').read_text('utf-8'))
    examples={};contexts=[]
    for raw in VOCAB[number].splitlines():
        word,z,e,z2,e2=raw.split('|');assert word in z and word in z2 and z!=z2
        examples[word]=(z,e);contexts.extend([(z,e),(z2,e2)])
    assert set(examples)=={v['hanzi'] for v in pack['vocabulary']}
    dqs,rqs=QUESTIONS[number]
    index={17:4,18:4,19:5,20:3}[number]
    yes={17:'Seeing the friend matters more to Chen Yu.',18:'Grandma likes oranges.',19:'The gates are about ten minutes apart.',20:'The cloth is blue.'}[number]
    no={17:'The book cannot be borrowed.',18:'Grandma gives the narrator no oranges to take home.',19:'All the friends went to the wrong gate.',20:'Xiao Zhou dislikes the button.'}[number]
    tasks=[tf(*rows(d)[index],yes,True,'The heard line explicitly states this fact.'),tf(*rows(r)[-1],no,False,'The heard line explicitly states a different result.'),*[reply(z,e,c,0,'This response fits the immediate question or proposal.') for z,e,c in REPLIES[number]]]
    for word in {17:['理解','相似'],18:['做客','京剧'],19:['发送','注意'],20:['彩色','现金']}[number]:tasks.append(fill(*examples[word],word))
    example_rows=list(examples.values());tasks.extend(match(example_rows[i:i+3]) for i in [0,3,6])
    inherited=[(g['hanzi'],g['meaning']) for t in [pack['dialogue'],pack['reading'],*pack['extraReadings']] for g in t.get('glosses',[])]
    repair(number,dict(title=('Opera stories at Grandma’s','奶奶讲京剧') if number==18 else (pack['unit']['title'],pack['unit']['titleZh']),dialogue=(rows(d),dqs),reading=(rows(r),rqs),media=(rows(m),[]),examples=examples,contexts=contexts,tasks=tasks,
        dialogueSpeakers={17:['陈宇','林安'],18:['陈宇','林安'],20:['陈宇','林安']}.get(number,['林安','陈宇']),mediaSpeakers={17:['陈宇','林安'],18:['林安','陈宇'],20:['林安','陈宇']}.get(number,['林安','陈宇']),
        glosses=list(dict.fromkeys(inherited+GLOSSES)),usage=[('Respond to the concrete situation',REPLIES[number][0][0],REPLIES[number][0][1],'Give the next practical detail instead of a general lecture.')],
        turns=[(z,e,'Respond to the person’s immediate request',[c[0]]) for z,e,c in REPLIES[number]],
        review='Naturalness correction: a quiet tea/book meeting for a tired friend, Grandma sharing opera stories over a home visit, correcting a west/east gate mistake with an apology and water, and a handmade birthday book bag/photo card. No identity, copyright or assessment-policy lecture inside ordinary speech. All 88 word records retain IDs and get two independent contexts; abstract/formal senses use suitable separate sentences. Self-review: Chen Yu offers the quiet venue; Grandma expects Sunday three and oranges; only Lin An goes to wrong gate, Chen Yu sends old address and fetches her; blue cloth, ordinary gold-coloured five-yuan button, birthday recipient Xiao Zhou, two books fit. Every false statement contradicts its own clip. Native flags: 感情/情感/感受, 自主 and 客观 register, 民族/中华民族/华人 definitions, civilisation/courteous 文明, printed 由于/因此/声明, 补/完善, 创作/创造/创新, 适用/应用, and playful 想得美/塞给. Native review pending.'),publish='--publish' in sys.argv)

DEPENDENCIES={
    's3-u27':[('未','not yet; has not')],
    's5-u07':[('混','mix; muddle together')],
    's5-u08':[('混','mix; muddle together')],
    's5-u10':[('提供','provide')],
    's5-u12':[('接触','contact; come into contact with')],
    's6-u01':[('估计','estimate; suppose')],
    's6-u05':[('结局','ending; outcome'),('提供','provide')],
    's6-u06':[('允许','permit; allow'),('厉害','impressive; formidable')],
    's6-u08':[('下降','decrease; decline'),('提供','provide')],
    's6-u09':[('提供','provide'),('区域','area; region'),('组织','organise; organisation'),('反馈','feedback')],
    's6-u10':[('提供','provide'),('允许','permit; allow'),('朗读','read aloud')],
    's6-u11':[('结局','ending; outcome')],
    's6-u12':[('提供','provide'),('接触','contact; come into contact with')],
}
for uid,terms in DEPENDENCIES.items():
    path=ROOT/f'content/packs/{uid}.json'
    source=path if path.exists() else ROOT/f'output/advanced-course-drafts/{uid}.json'
    pack=json.loads(source.read_text('utf-8'))
    for text in [pack['dialogue'],pack['reading'],*pack['extraReadings']]:
        for word,meaning in terms:
            if any(word in l['zh'] for l in text['lines']) and not any(g['hanzi']==word for g in text.get('glosses',[])):
                text.setdefault('glosses',[]).append(dict(hanzi=word,pinyin=py(word),meaning=meaning))
    destination=ROOT/('content/packs' if '--publish' in sys.argv else 'output/parity-editorial-drafts')/path.name
    destination.write_text(json.dumps(pack,ensure_ascii=False,indent=2)+'\n','utf-8')
