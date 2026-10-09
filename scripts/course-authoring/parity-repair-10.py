"""HSK 3 natural conversations: a lost file, dinner, group supplies and karaoke."""
import json,sys
from common import ROOT,py
from advanced_core import rows
from editorial_repair import repair,tf,reply,fill,match
from parity_repair_10_contexts import VOCAB

TEXTS={
5:(
'''你找到上次的活动文件了吗？|Have you found the file from our last event?
找到了，在第一个文件夹里。|Yes, in the first folder.
发给我看看，我想保留那张合照。|Send it over. I'd like to keep the group photo.
好。还有通知，我整理一下再发。|Sure. There's a notice too. I'll sort it out and send it.
等等，标题写星期六，表格里却是星期日。|Wait, the title says Saturday but the table says Sunday.
啊，是我修改的时候漏了一处。|Oh, I missed one part when editing it.
具体改哪一页？|Which page needs changing?
第二页。我改好以后，把完整的文件发你。|The second. I'll send the complete file after fixing it.
原来那份也存着吧，下次还能用。|Keep the original too. We might use it next time.
行。你现在就要吗？|Okay. Do you need it now?
不急，六点以前给我就好。|No rush. Before six is fine.
那我先处理这一页，弄好就告诉你。|I'll deal with this page and let you know when it's ready.
''',
'''我想找上次活动的合照，就问陈宇文件存在哪里。他说找到了，在第一个文件夹里，顺便把通知也发给我。|I wanted the group photo from our last event and asked Chen Yu where he'd saved it. It was in the first folder, he said, and he sent the notice too.
照片里六个人站得整整齐齐，只有我手上的杯子快要掉了。我想把照片保留下来，以后见面再给大家看。|The six of us stood neatly in the photo, except that the cup in my hand was about to fall. I wanted to keep it and show everyone when we met again.
打开通知，我发现标题写星期六，第二页的表格却写星期日。我给陈宇发消息，他一下就想起来，上次只修改了标题。|The notice title said Saturday, but the table on page two said Sunday. I messaged Chen Yu, who remembered he'd changed only the title last time.
他问我具体什么时候要，我说六点以前就行。他先保留原件，再把第二页的日期改好，保存以后重新发来。|He asked exactly when I needed it. Before six was fine. He kept the original, changed the date on page two, saved it and sent it again.
这次文件一共三页，内容都在。我回了一句收到，又把合照单独存到照片里，免得下次还得找半天。|The file now had all three pages. I replied that I'd received it and saved the group photo separately so I wouldn't spend ages looking next time.
傍晚陈宇问我照片选好了没有。我说选好了，就是那张杯子快掉的。他笑我每次拍照，都要先给大家找点事做。|That evening Chen Yu asked if I'd chosen a photo. I had: the one with the falling cup. He laughed that every time I posed I found something for everyone to do.
''',
'''你那杯子怎么还没掉？|How has your cup still not fallen?
照片里的杯子不会掉。|Cups in photos don't fall.
那你以后每次都拿这一张？|Will you carry this photo every time, then?
带照片比带杯子轻多了。|A photo's much lighter than a cup.
好，下次我负责拍，你负责拿稳。|Okay. Next time I'll take the photo and you hold it steady.
拿照片的话，我有把握。|If it's the photo I'm holding, I can manage.
'''),
6:(
'''今晚四个人吃饭，桌子够大吗？|Is the table big enough for the four of us tonight?
够。再拿两把椅子就行。|Yes. We just need two more chairs.
筷子放哪儿了？|Where are the chopsticks?
右边。拿四双，再给每人放一张纸巾。|On the right. Get four pairs and put a napkin out for each person.
今天有什么菜？|What's for dinner?
白菜、鸡蛋和汤。你想喝什么？|Chinese cabbage, eggs and soup. What would you like to drink?
果汁吧，红茶也行。我不喝啤酒。|Fruit juice, or black tea. I don't drink beer.
行，冰箱里还有可乐，你自己拿。|Okay. There's cola in the fridge too; help yourself.
汤好了，我先尝一口。|The soup's ready. I'll taste it.
小心，还很烫，等一会儿。|Careful, it's still hot. Wait a moment.
好。桌上这束花也是给今晚准备的？|Okay. Are these flowers for tonight too?
是啊，吃顿饭也可以好看一点。|Yes. Dinner can look nice too.
''',
'''今晚朋友来吃饭，一共四个人。桌子旁边原来只有两把椅子，我又从房间里搬来两把，把四双筷子放好。|There were four of us at dinner tonight. The table had only two chairs, so I brought two more from the room and laid out four pairs of chopsticks.
陈宇带来一束花，我把它放在桌子中间。他问今晚有什么菜，我说有白菜、鸡蛋和汤，都是刚做好的。|Chen Yu brought flowers, which I placed in the middle of the table. He asked about the food: Chinese cabbage, eggs and soup, all freshly cooked.
陈宇想喝果汁，小周选红茶，王宁从冰箱拿了可乐。我自己倒水，四个人的杯子很快就不一样了。|Chen Yu wanted fruit juice, Xiao Zhou chose black tea, and Wang Ning fetched cola from the fridge. I poured water for myself; soon all four cups contained different drinks.
汤刚端上桌，陈宇就想喝一口。我让他等等，先吃别的菜。他把碗放下，却说光看着就觉得饿。|When the soup arrived Chen Yu wanted a taste immediately. I asked him to wait and try the other food first. He put down the bowl, saying the sight alone made him hungry.
我们边吃边聊上次旅行，我拿出手机给大家看照片。每张照片都有一只猫，我说当地的猫比人还会找好吃的。|We chatted about our last trip over dinner. I showed everyone photos on my phone. Each had a cat; I said the local cats were better than people at finding good food.
这顿饭吃到八点。剩下的汤我放进冰箱，四个人一起收拾桌子，那束花留着，明天还想放在窗边。|Dinner lasted until eight. I put the remaining soup in the fridge. We cleared the table together and kept the flowers to put by the window tomorrow.
''',
'''你拍的每张照片怎么都有猫？|Why is there a cat in every photo you took?
它们知道哪里有好吃的。|They know where the good food is.
那今天怎么没有猫来？|Why hasn't a cat come today, then?
可能还不知道地址。|Maybe it doesn't know the address yet.
别发，我这碗汤还没喝完。|Don't send it. I haven't finished my soup.
放心，今天只请了你们三个人。|Relax. I've invited only the three of you today.
'''),
7:(
'''今天小组六个人，纸够吗？|Do we have enough paper for the six people in the group today?
只有四张，还缺两张。|Only four sheets. We're short of two.
我去拿，你把笔放好。|I'll fetch them. You lay out the pens.
行，给每组配两支笔？|Okay. Two pens per group?
对。两组分别拿三张纸。|Yes. Three sheets for each of the two groups.
纸上要写名字吗？|Do we need names on the paper?
写吧，大家一张一张递给我。|Yes. Have everyone pass me theirs one at a time.
好。这个活动收费吗？|Okay. Is there a charge for this activity?
不收费，大家来坐坐，聊聊书就行。|No. People can just sit and chat about books.
那我再叫一个朋友来？|Shall I invite another friend?
可以，不过我得再拿一张纸。|Sure, but I'll need one more sheet.
我来拿吧，你今天已经跑三次了。|I'll fetch it. You've gone three times already today.
''',
'''读书小组今天有六个人，我到得早，先帮忙放纸和笔。桌上只有四张纸，我又拿来两张，分成两组，每组放三张。|Six people came to today's reading group. I arrived early to help with paper and pens. There were four sheets; I fetched two more and put three on each group's table.
林安问笔怎么配，我说每组两支，大家轮着用。她把椅子也放好，门口很快就有人进来了。|Lin An asked about pens. Each group could share two. She arranged the chairs too, and people soon began arriving.
有人第一次来，问活动是不是收费。我说不收费，只要带一本自己想说的书。她笑了，说这次带了两本，正好可以借给别人。|A new visitor asked about the charge. There was none; people just needed a book they wanted to talk about. She smiled: she'd brought two and could lend one.
六个人到齐以后，大家在纸上写名字，再一张一张递过来。我看见两个相同的姓，就问他们是不是已经认识。|Once all six had arrived, everyone wrote their name and passed over their sheet. Two shared a surname, so I asked if they knew each other already.
他们以前没见过，今天却带了同一本书。两个人马上坐到一起，说好一人先讲一段，另一人再接着讲。|They hadn't met, but had brought the same book. They sat together immediately and agreed to take turns talking about a passage.
活动结束时，桌上六张纸都还在，有一支笔却不知道是谁的。我刚问完，大家都笑了，那是我自己带来的。|At the end all six sheets were still on the table, but we couldn't identify one pen. Everyone laughed when I asked: I'd brought it myself.
''',
'''这支笔是谁的？|Whose pen is this?
你的啊，你刚才拿出来的。|Yours! You took it out earlier.
我只记得今天缺两张纸。|I only remembered being short of two sheets.
纸已经齐了，笔也找到主人了。|We have all the paper now, and the pen has its owner.
那我可以回家了。|I can go home, then.
先拿笔，不然明天又问一次。|Take your pen first, or you'll ask again tomorrow.
'''),
8:(
'''昨天那首歌，你今天还想练吗？|Do you want to practise yesterday's song again today?
想。今天比昨天清楚多了，不过最后一句还没唱好。|Yes. It's much clearer today, but I still can't get the last line right.
我唱一遍，你听听？|Shall I sing it once for you?
好。别太快，我想听清每个字。|Yes. Not too fast; I want to hear every word.
这样行吗？|Is this okay?
行，这次比较容易跟。再来一遍吧。|Yes. This time it's fairly easy to follow. Once more, please.
你已经唱了三遍，我只唱了两遍。|You've sung it three times; I've sung it only twice.
那你再唱一次，正好。|One more from you will make it even.
下周五的演唱会，你买票了吗？|Have you got a ticket for next Friday's concert?
买了，七点开门，八点开始。|Yes. Doors open at seven; it starts at eight.
我们六点半在车站见？|Meet at the station at six thirty?
好，在路上还可以唱，不过小声一点。|Okay. We can sing on the way, but quietly.
''',
'''陈宇昨天和我练一首歌，最后一句我总是唱不清。他今天又来，我们先把这句读慢一点，再一起唱。|Chen Yu and I practised a song yesterday, but I couldn't sing the last line clearly. When he came today we read it slowly first, then sang it together.
我唱了三遍，他唱了两遍。我让他再唱一次，他故意拿着笔当话筒，站得像已经上了舞台。|I sang it three times and he sang it twice. I asked for one more; he used his pen as a microphone and stood as though already onstage.
这一遍我听清了最后两个字，就跟着唱。他说比昨天好听，我也觉得今天更加轻松，不再只顾着赶上音乐。|I heard the last two words this time and sang along. He thought it sounded better than yesterday. I felt more relaxed too, rather than just trying to keep up with the music.
下周五我们要去看演唱会。七点开门，八点开始，所以约好六点半在车站见，先一起吃点东西。|We're going to a concert next Friday. Doors open at seven and it starts at eight. We'll meet at the station at six thirty and get something to eat first.
我最喜欢的歌手这次和乐队一起演出。以前我只听过歌声，这次还想看看他们在舞台上怎么互相配合。|My favourite singer is performing with a band. Before I'd only heard the singing; now I wanted to see how they worked together onstage.
晚上我把笔收好，陈宇还问下次有没有话筒。我说话筒没有，两支笔倒是有，让他选一个颜色就行。|That evening I put away the pen. Chen Yu asked whether we'd have a microphone next time. We wouldn't, I said, but I had two pens; he could choose a colour.
''',
'''蓝色的笔还是黑色的笔？|The blue pen or the black pen?
哪个唱得好听？|Which one sounds better when singing?
笔都一样，是你唱。|They're just pens. You're the one singing.
那我选蓝色，看起来像上台了。|I'll take the blue one. It makes me look ready for the stage.
先把盖子盖好，别把嘴涂蓝了。|Put the cap on first. Don't colour your mouth blue.
好，今天只唱歌，不画画。|Okay. Singing today, no drawing.
''')}

QUESTIONS={
5:([
('gist','What do they arrange?',['Correcting a notice and sending the complete file','Buying new cups','Cancelling the group photo'],0),
('detail','Which page has the wrong date?',['The second','The first','The third'],0),
('inference','Why keep the original?',['They might reuse it','It contains no information','The computer refuses new files'],0)], [
('gist','What does the narrator obtain?',['The corrected file and a group photo','A new computer','A Sunday invitation only'],0),
('detail','By when is the file needed?',['Six','Midnight','Three in the morning'],0),
('inference','Why save the photo separately?',['To find it more easily next time','To remove everyone from it','To change the date again'],0)]),
6:([
('gist','What are they preparing?',['Dinner for four','A piano delivery','A shop opening'],0),
('detail','How many more chairs do they need?',['Two','Four','One'],0),
('inference','Why wait before tasting the soup?',['It is still hot','It has no ingredients','The flowers are in the bowl'],0)], [
('gist','How does the dinner go?',['Friends eat, chat and clear up together','Nobody arrives','They move a piano instead'],0),
('detail','What does Xiao Zhou drink?',['Black tea','Beer','Cola'],0),
('inference','Why keep the flowers?',['The host wants them by the window tomorrow','They must be eaten','They are someone’s ticket'],0)]),
7:([
('gist','What are the two preparing?',['Paper and pens for a reading group','A paid concert','A bus ticket'],0),
('detail','How many sheets do they initially lack?',['Two','Six','Three'],0),
('inference','Why fetch another sheet for one more friend?',['Each person needs one','The first six were burned','The friend is paying for paper'],0)], [
('gist','What happens at the group?',['People share books and the organiser forgets their own pen','All the books vanish','Nobody has the same surname'],0),
('detail','Why do the two people sit together?',['They brought the same book','They are sisters','They are waiting for payment'],0),
('inference','Why does everyone laugh at the end?',['The unidentified pen belongs to the narrator','The group has no paper','The narrator has bought a plane'],0)]),
8:([
('gist','What do the friends do?',['Practise a song and plan their concert trip','Cancel the concert','Buy two microphones'],0),
('detail','When will they meet at the station?',['Six thirty','Eight','Seven thirty'],0),
('inference','Why ask for slower singing?',['To hear every word','To make the concert start late','To finish reading a notice'],0)], [
('gist','How does practice develop?',['The difficult line becomes clearer and a pen becomes a pretend microphone','The singer loses every ticket','They stop practising permanently'],0),
('detail','What time does the concert start?',['Eight','Seven','Six thirty'],0),
('inference','Why offer two pens at the end?',['To continue the microphone joke','To pay for tickets','To repair the station'],0)])}

REPLIES={
5:[('具体改哪一页？','Which exact page needs changing?',['第二页，日期写错了。','合照在我手上。','下次买六个杯子。']),('六点以前发给我，可以吗？','Can you send it before six?',['可以，改好就发。','好，我明天八点才发。','这顿饭我请。'])],
6:[('汤还烫，等一下吧。','The soup is still hot. Wait a moment.',['好，我先吃白菜。','好，我马上喝完。','钢琴在门外。']),('你想喝什么？','What would you like to drink?',['果汁吧，谢谢。','两把椅子够了。','我已经修好了。'])],
7:[('纸只有四张，还缺两张。','There are only four sheets; we lack two.',['我再拿两张来。','那六个人一共拿一张。','演唱会八点开始。']),('这支笔是谁的？','Whose pen is this?',['我的，我刚才拿来的。','活动不收费。','我想喝红茶。'])],
8:[('别唱太快，我想听清每个字。','Please sing slowly enough for me to hear every word.',['好，这一遍慢一点。','那我再快一点。','车站在第二页。']),('六点半在车站见，好吗？','Shall we meet at the station at six thirty?',['好，我们再一起吃点东西。','好，八点在房间见。','你的文件是三页。'])]}

GLOSSES=[('合照','group photo'),('文件夹','folder'),('原件','original document'),('漏','miss out; omit'),('单独','separately'),('杯子','cup'),('掉','fall; drop'),('标题','title'),('核对','check against the source'),('半天','a long time; half a day'),('拿稳','hold steadily'),('食品','food products'),('进口','import'),('伞','umbrella'),('头顶','overhead; top of the head'),('袜子','sock'),('电视','television'),('新鲜','fresh'),('冰箱','fridge'),('当地','local'),('本地','local area'),('糖','sugar; sweets'),('香味','pleasant smell'),('窗边','by the window'),('剩下','remain'),('端','carry in the hands; serve a dish'),('收拾','tidy up; clear away'),('轮着','take turns'),('相同','the same'),('姓','surname'),('缺','lack'),('开支','expenses'),('漏水','leak water'),('堵车','traffic jam'),('温度','temperature'),('格','field or cell; grid square'),('课程','course'),('负责','be responsible for'),('责任','responsibility'),('功能','function'),('明确','clear; definite'),('数量','quantity'),('满足','satisfy'),('整体','whole; overall'),('全面','comprehensive'),('眼镜','glasses'),('盒子','small box'),('人民币','renminbi'),('停车','park a vehicle'),('同意','agree'),('经历','experience'),('技术','technique'),('相当','fairly; equivalent'),('改进','improve'),('精彩','wonderful'),('话筒','microphone'),('故意','deliberately'),('轻松','relaxed'),('配合','cooperate'),('涂','apply colour'),('嘴','mouth'),('盖子','lid; cap'),('拍手','applaud'),('阳光','sunlight'),('清新','fresh'),('团队','team'),('盖','cover; put a lid on'),('倒','on the contrary; pour'),('一排','a row'),('林安','Lin An, a name'),('陈宇','Chen Yu, a name'),('小周','Xiao Zhou, a name')]

GLOSSES += [('王宁','Wang Ning, a name'),('免得','so as to avoid'),('傍晚','early evening'),('把握','confidence; assurance'),('光','merely; only'),('苹果','apple'),('并不','actually not'),('整顿','put in order; reorganise'),('赶上','keep up with'),('纸巾','paper napkin; tissue')]

for number,(d,r,m) in TEXTS.items():
    pack=json.loads((ROOT/f'content/packs/s3-u{number:02}.json').read_text('utf-8'))
    examples={};contexts=[]
    for raw in VOCAB[number].splitlines():
        word,z,e,z2,e2=raw.split('|');assert word in z and word in z2 and z!=z2
        examples[word]=(z,e);contexts.extend([(z,e),(z2,e2)])
    assert set(examples)=={v['hanzi'] for v in pack['vocabulary']}
    dqs,rqs=QUESTIONS[number]
    index={5:7,6:1,7:1,8:9}[number]
    yes={5:'The second page needs changing.',6:'Two more chairs are needed.',7:'They lack two sheets.',8:'The concert starts at eight.'}[number]
    no={5:'Chen Yu says the narrator never gives anyone something to do when posing.',6:'The host throws away the flowers.',7:'The unidentified pen belongs to a stranger.',8:'The narrator offers a real microphone for next time.'}[number]
    tasks=[tf(*rows(d)[index],yes,True,'The heard line states this fact.'),tf(*rows(r)[-1],no,False,'The heard line explicitly describes a different result.'),
           *[reply(z,e,c,0,'This reply addresses the immediate question.') for z,e,c in REPLIES[number]]]
    for word in {5:['文件','修改'],6:['红茶','果汁'],7:['缺','配合'],8:['演唱会','精彩']}[number]:tasks.append(fill(*examples[word],word))
    example_rows=list(examples.values());tasks.extend(match(example_rows[i:i+3]) for i in [0,3,6])
    inherited=[(g['hanzi'],g['meaning']) for t in [pack['dialogue'],pack['reading'],*pack['extraReadings']] for g in t.get('glosses',[])]
    repair(number,dict(dialogue=(rows(d),dqs),reading=(rows(r),rqs),media=(rows(m),[]),examples=examples,contexts=contexts,tasks=tasks,
        dialogueSpeakers={6:['陈宇','林安'],7:['陈宇','林安'],8:['陈宇','林安']}.get(number,['林安','陈宇']),mediaSpeakers={8:['林安','陈宇']}.get(number,['陈宇','林安']),
        glosses=list(dict.fromkeys(inherited+GLOSSES)),
        usage=[('Ask about the next practical detail',REPLIES[number][0][0],REPLIES[number][0][1],'State the concrete next action.')],
        turns=[(z,e,'Respond to the immediate practical question',[c[0]]) for z,e,c in REPLIES[number]],
        review='Naturalness correction: finding a group photo and fixing a date, preparing dinner for four, supplying a six-person reading group, and practising a song before a concert. Replaced assessment-policy lectures, lexical analysis inside conversations and robotic examples with independently authored situations. All 88 word records have two different notebook contexts. Original IDs and grammar evidence remain. Self-review: exact four-person dinner seating and three invited guests; two groups of three; two missing sheets; page two and before-six deadline; concert doors at seven, start at eight, station at six thirty. False listening statements contradict their own heard line. Native flags: bound 富/整 senses, classifiers 行/架/支/只, 相当 equivalent versus fairly, 比较 compare versus relatively, 证明 evidence examples, emphatic 倒是 and pretend-microphone teasing. Native review pending.'),publish='--publish' in sys.argv)

DEPENDENCIES={
    's3-u21':[('归','return; put back')],
    's3-u26':[('订','book; reserve'),('遇','meet; encounter')],
    's3-u27':[('遇','meet; encounter')],
    's3-u31':[('订','book; reserve')],
    's3-u32':[('订','book; reserve')],
    's3-u33':[('荐','recommend'),('村','village')],
    's3-u36':[('陪','accompany')],
    's3-u37':[('桥','bridge'),('产','produce')],
    's3-u39':[('删','delete; remove')],
    's4-u04':[('细','careful; fine; detailed')],
    's5-u02':[('凭','rely on; on the strength of')],
    's5-u06':[('享','enjoy; share in')],
    's5-u07':[('符','match; symbol')],
    's5-u08':[('厅','hall; public room')],
    's5-u10':[('缩','shorten; contract')],
    's6-u05':[('仔细','careful; carefully')],
    's6-u08':[('盯','fix one’s gaze on')],
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
