"""Early HSK 3: ordinary group introductions, reading, volunteering and a favour."""
import json,sys
from common import ROOT,py
from advanced_core import rows
from editorial_repair import repair,tf,reply,fill,match
from parity_repair_08_contexts import VOCAB

TEXTS={
1:(
'''你好，我姓李，叫我小李就行。|Hi, my surname is Li. Just call me Xiao Li.
你是上周来过的那位？我认得你的声音。|Were you here last week? I recognise your voice.
对，不过你当时坐在里面，我们没说上话。|Yes, but you were sitting inside and we didn't get to talk.
那今天坐这儿吧，我帮你留个位子。|Sit here today, then. I'll save you a seat.
谢谢。刚才门口那位男子也是组里的成员吗？|Thanks. Is the man at the entrance a member too?
是，大家叫他老王。他来得最早，连门口的猫都认得他。|Yes, we call him Lao Wang. He comes so early even the cat outside knows him.
猫也来参加？|Does the cat join in too?
不，它只来吃东西。你家乡在哪里？|No, it's only here for food. Where's your hometown?
在南方。我父母还住在那里。|In the south. My parents still live there.
我母亲也是南方人，下次你们可以聊聊。|My mother's from the south too. You could chat next time.
好。今天还有谁没到？|Sure. Who hasn't arrived today?
第三位新成员还在路上，我们先拿书。|The third new member is still on the way. Let's get the books first.
''',
'''我第二次去读书小组，刚到门口就有人叫小李。我一开始没反应过来，才想起上周自己说可以这样称呼。|On my second visit to the reading group someone called out Xiao Li at the entrance. It took me a moment to remember I'd suggested that name last week.
陈宇认得我的声音，给我留了一个位子。这次我坐在中间，刚坐下就和旁边两位成员聊了起来。|Chen Yu recognised my voice and saved me a seat. This time I sat in the middle and started chatting with the two members beside me as soon as I sat down.
门口的男子是老王，他已经参加小组两年了。他每次都早到，先开窗，再把书放到各张桌子上。|The man by the entrance was Lao Wang. He'd been in the group for two years and always arrived early to open the windows and put books on the tables.
一只猫跟着他进来，在椅子旁边坐下。陈宇说猫只认得带吃的来的人，老王说今天没带吃的，它也跟来了。|A cat followed him in and sat beside a chair. Chen Yu said it only knew people who brought food. Lao Wang pointed out that it followed him today even though he hadn't brought any.
大家聊天时，我说自己的家乡在南方，父母还住在那里。陈宇说他母亲也是南方人，下次可能一起来。|While we chatted I said my hometown was in the south and my parents still lived there. Chen Yu's mother was from the south too and might come with him next time.
第三位新成员到了以后，我们才开始读书。回家时，我已经能叫出几位成员的名字，也和陈宇约好了下周再见。|We began reading after the third new member arrived. By the time I left I could name several members and had arranged to see Chen Yu again the next week.
''',
'''你刚才说那只猫也认得我？|Did you say that cat knows me too?
你上次带了吃的，它记得。|You brought food last time. It remembers.
那今天没带怎么办？|What happens if I didn't bring any today?
你问它呀，它就在你椅子下面。|Ask it. It's right under your chair.
怪不得我一坐下，它就看着我。|No wonder it looked at me as soon as I sat down.
你们慢慢聊，我们先读书。|You two have a chat. We'll start reading.
'''),
2:(
'''今天谁都可以来听吗？我没报比赛。|Can anyone listen today? I haven't entered the competition.
可以，今天是读书活动，比赛是下个月的事。|Yes. Today is a reading event. The competition is next month.
那就好。我有点害怕在很多人面前读。|Good. I'm a little afraid of reading in front of lots of people.
你先和我坐一桌，想读什么就选什么。|Sit at my table first. Choose whatever you'd like to read.
这两篇的难度差不多吗？|Are these two passages about equally difficult?
左边的短一点。我上次读过，还挺有意思。|The one on the left is shorter. I've read it before; it's interesting.
那我先选这篇，先听你读一遍。|I'll pick that one and listen to you read it first.
行。每个人读一小段，轮到你还早呢。|Sure. We each read a short section. It'll be a while before your turn.
这里有各种书，我还想看看旁边那本。|There are all sorts of books here. I'd like to look at the one beside it too.
等这段读完再看吧。时间足够，不用急。|Let's finish this section first. There's enough time; no rush.
好，我读第一句，你帮我听听？|Okay, shall I read the first sentence while you listen?
来吧。我听着，你慢慢读。|Go ahead. I'm listening; take your time.
''',
'''周末的读书活动对大家开放。我没有报名下个月的比赛，还是可以参加今天的活动。门口有一群人在选书，我站在后面看了一会儿。|The weekend reading event was open to everyone. I hadn't entered next month's competition, but I could join today's activity. A group was choosing books at the entrance, and I watched for a while.
陈宇看见我，把我带到他的桌子旁边。桌上放着两篇文章，他说左边的短一点，自己上次读过。|Chen Yu saw me and brought me to his table. There were two passages on it. The left one was shorter, and he'd read it before.
我选了短的那篇，想先听别人读。他给我指了第一段，我一边听，一边用手跟着字走。|I chose the shorter one and wanted to listen first. He pointed to the first paragraph, and I followed the characters with my finger while listening.
轮到我时，我读了第一句。声音不太大，陈宇把椅子往我这边挪了一点，说这样听得更清楚。|When my turn came I read the first sentence. I was quiet, so Chen Yu moved his chair closer and said he could hear more clearly that way.
后来各桌开始聊天，每个人说自己喜欢哪一段。旁边一位朋友喜欢结尾，我喜欢开头，两个人又一起看了一遍。|Later the tables began chatting about favourite sections. Someone beside me liked the ending; I liked the beginning. We looked through it together again.
回去的路上，我问陈宇下周还有没有活动。他说有，我就把时间记下来。这次只读了一句，下次想试试一整段。|On the way home I asked if there was another event next week. There was, so I wrote down the time. I'd read one sentence this time and wanted to try a whole paragraph next time.
''',
'''你刚才读得比我大声。|You read louder than me just now.
因为你坐得近，我不用往后面喊。|You were nearby, so I didn't have to shout to the back.
下次也坐这儿吧？|Shall we sit here next time too?
行，不过你得早点来，别让我一直留着椅子。|Sure, but come early. Don't make me save the chair forever.
好，我给椅子也带一杯茶。|Okay, I'll bring tea for the chair too.
给我就行，椅子喝不了。|Give it to me. The chair can't drink.
'''),
3:(
'''周六活动需要两位志愿者，你能来吗？|We need two volunteers for Saturday's event. Can you come?
能，我两点到，三点要走。|Yes. I'll arrive at two and need to leave at three.
正好。两点到三点你负责名单，我负责入口。|That works. You handle the list from two to three; I'll handle the entrance.
名单放在哪里？|Where's the list?
放在门口那张桌子上。我会提前拿过去。|On the table by the entrance. I'll bring it over beforehand.
还需要搬椅子吗？|Do we need to move chairs too?
需要。这里共有四把，每人搬两把就行。|Yes. There are four here. We can move two each.
行，搬到窗户旁边？|Okay, beside the window?
对。有人想坐着等朋友，放那里比较方便。|Yes. People may want to sit while waiting for friends; that's a convenient spot.
那我到的时候先搬。|I'll move them when I arrive, then.
谢谢，三点以后小周来接你的班。|Thanks. Xiao Zhou will take over from you after three.
好，那我把名单直接交给她。|Good. I'll give her the list directly.
''',
'''周六我去帮读书小组办活动，两点到门口时，陈宇已经把名单放在桌子上了。我三点要走，所以我们先说好交接的时间。|I helped with the reading group's event on Saturday. When I arrived at two, Chen Yu had put the list on the table. I needed to leave at three, so we agreed on the handover time first.
门边共有四把椅子，我们每人搬两把，放到窗户旁边。刚搬好，就有两位朋友坐下来等人。|There were four chairs by the door. We moved two each to the window. As soon as they were in place, two friends sat down to wait for someone.
我负责名单，陈宇负责入口。有人问房间在哪里，他就指给对方看；有人要登记，我就请对方到桌子前面来。|I handled the list, and Chen Yu handled the entrance. He showed people where the room was; I invited anyone registering to the table.
一位新朋友没带书，我问陈宇还有没有。他从包里拿出一本，放到桌上，让朋友先选一段看。|A newcomer hadn't brought a book. I asked Chen Yu if there were any left. He took one from his bag and let the visitor choose a section.
快三点时，小周到了。我把名单给她，又告诉她那本借来的书是谁在看。她拿笔记了下来，我才去拿自己的包。|Xiao Zhou arrived just before three. I gave her the list and told her who had the borrowed book. She wrote it down, and I went to get my bag.
走到门口，陈宇还问我下次来不来。我说来，下次如果有时间，可以多留一会儿。他笑着说先去忙今天的事吧。|At the entrance Chen Yu asked if I'd come again. I would, and might stay longer if I had time next time. He smiled and told me to get on with today's plans first.
''',
'''你刚才搬了几把椅子？|How many chairs did you move?
两把，怎么了？|Two. Why?
我也搬两把，可这里怎么有五把？|I moved two too, but why are there five here?
第五把是老王自己拿过来的。|Lao Wang brought the fifth one himself.
怪不得。他已经坐上去了。|No wonder. He's already sitting on it.
那不用搬了，连人一起搬太重。|Then leave it. Moving him with it would be too heavy.
'''),
4:(
'''麻烦你帮我一个忙，问问小周周六几点能到。|Could you do me a favour and ask when Xiao Zhou can arrive on Saturday?
行，我下午联系她。她现在去理发了。|Sure. I'll contact her this afternoon. She's getting a haircut now.
我想约她一起去书店，三点还是四点都可以。|I'd like to go to the bookshop with her. Three or four would work.
那我把两个时间都问一下。|I'll ask about both times.
好。我先去办公室复印两页，回来再看消息。|Good. I'll photocopy two pages at the office and check the messages when I return.
你去办公室？能帮我也复印这一页吗？|You're going to the office? Could you copy this page for me too?
能，发给我吧。|Yes. Send it over.
谢谢。书店还有一位朋友要来，我也问问她。|Thanks. Another friend wants to come to the bookshop; I'll ask her too.
那我们到了先互相介绍一下。|We can introduce ourselves when we get there.
好，别一下问太多，让我先等小周回消息。|Sure. Don't ask me everything at once; let me wait for Xiao Zhou's reply first.
行，你不是一边理发一边回消息吧？|Okay. You're not replying while getting a haircut too, are you?
没有，我还在这里听你说呢。|No. I'm still here listening to you.
''',
'''我想周六约小周去书店，三点和四点都可以。陈宇说她去理发了，下午再联系。我就先去办公室复印两页材料。|I wanted to go to the bookshop with Xiao Zhou on Saturday; three or four would work. Chen Yu said she was getting a haircut and would contact her that afternoon. I went to the office to photocopy two pages first.
出门以前，陈宇把自己的一页发给我，麻烦我一起复印。办公室没有排队，我很快就印好了三页，放进包里。|Before I left, Chen Yu sent me a page and asked me to copy it too. There was no queue at the office. I quickly copied all three pages and put them in my bag.
回来的路上，我看手机，小周还没回答。陈宇说不用急，她理完发还要坐车回家，可能到家以后才看消息。|On the way back I checked my phone. Xiao Zhou hadn't replied yet. Chen Yu said not to rush; she had a bus ride home after her haircut and might only check messages there.
下午两点，她说三点半能到。这个时间也合适，我就在手机里写好书店的地址，发给陈宇和她。|At two she said she could arrive at three thirty. That worked too, so I wrote out the bookshop address on my phone and sent it to both of them.
另外一位朋友四点到，我们先找了四个位子。她来了以后，陈宇介绍我们认识；聊了一会儿，才发现我们上次去过同一个活动。|The other friend would arrive at four, so we found four seats first. Chen Yu introduced us when she came. After chatting, we discovered we'd been to the same event before.
走以前，我把复印的那一页给陈宇。他拿着纸笑了，说我们忙着等消息，他自己都忘了这件事。|Before leaving I gave Chen Yu his copied page. He smiled: we'd been so busy waiting for messages that he'd forgotten it himself.
''',
'''你这张纸上怎么有个茶杯印？|Why is there a teacup mark on this page?
我拿到以后放桌上，茶也放桌上了。|I put it on the table after getting it, alongside my tea.
幸好字还看得清。|Luckily the writing is still clear.
要不要再复印一张？|Shall I make another copy?
不用，这个印也会一起印上去。|No. The mark would be copied too.
也是。下次先把茶喝完。|True. I'll finish the tea first next time.
''')}

QUESTIONS={
1:([
('gist','What happens between the two members?',['They get acquainted and sit together','They argue about food','They cancel the reading group'],0),
('detail','Where is Xiao Li’s hometown?',['In the south','In the north','At the station'],0),
('inference','Why mention that even the cat knows Lao Wang?',['He comes early and often','He is the cat’s doctor','The cat reads the books'],0)], [
('gist','How does the second visit feel different?',['The narrator gets to know members and their names','Nobody speaks to the narrator','Only the cat attends'],0),
('detail','When do they start reading?',['After the third new member arrives','Before Lao Wang arrives','Only the following week'],0),
('inference','Why is the new seat useful?',['The narrator can talk with the people beside them','It is reserved for the cat','It is farther away from everyone'],0)]),
2:([
('gist','What does the newcomer decide to try?',['A first sentence after listening','Every book in the room','A competition that day'],0),
('detail','Which passage is shorter?',['The left one','The right one','They are exactly the same length'],0),
('inference','Why sit with Chen Yu?',['To listen first and try reading nearby','To avoid entering the room','To receive a competition prize'],0)], [
('gist','What is the outcome of the visit?',['The narrator reads one sentence and wants to return','The event is cancelled','Everyone goes home without reading'],0),
('detail','Why does Chen Yu move his chair?',['To hear the quiet reader more clearly','To get closer to the exit','Because the chair is broken'],0),
('inference','Why note next week’s time?',['The narrator plans to try a whole paragraph next time','The next event is a compulsory exam','The narrator wants to avoid the activity'],0)]),
3:([
('gist','What do they arrange?',['A one-hour volunteer shift and its tasks','A full-day trip','Buying a new window'],0),
('detail','Who handles the entrance?',['Chen Yu','Xiao Zhou','The volunteer with the list'],0),
('inference','Why hand the list to Xiao Zhou?',['She takes over after three','She will throw it away','The list is her shopping list'],0)], [
('gist','How does the volunteer shift go?',['They prepare, help arrivals and hand over','Nobody comes','The volunteer forgets to leave'],0),
('detail','How many chairs do they move together?',['Four','Two','Every chair in the building'],0),
('inference','Why tell Xiao Zhou who borrowed the book?',['She can keep track after taking over','The borrower has stolen it','The volunteer wants to cancel the event'],0)]),
4:([
('gist','What favour do they agree to do?',['Ask Xiao Zhou’s time and help with photocopying','Cut each other’s hair','Book a flight'],0),
('detail','When will Chen Yu contact Xiao Zhou?',['In the afternoon','Immediately during her haircut','Next year'],0),
('inference','Why offer both three and four?',['Either time works for the narrator','Xiao Zhou has refused both times','They are two different days'],0)], [
('gist','What happens after the messages?',['They agree on three thirty and meet another friend','They cancel the outing','The office closes before copying'],0),
('detail','How many pages are copied altogether?',['Three','Two','One'],0),
('inference','Why does Chen Yu smile at the end?',['He had forgotten his page while waiting for replies','He dislikes the bookshop','The narrator copied the wrong book'],0)])}

REPLIES={
1:[('你好，我姓李，怎么称呼你？','Hi, my surname is Li. What should I call you?',['叫我陈宇就行。','第三位还没到。','猫在椅子下面。']),('今天还有谁没到？','Who has not arrived today?',['第三位新成员还在路上。','我父母住在南方。','老王已经坐下了。'])],
2:[('这两篇，我想先读短一点的。','I’d like to try the shorter of these two passages.',['选左边这篇吧。','下个月有比赛。','时间是周六下午。']),('我先听你读一遍，行吗？','May I listen to you read it once first?',['行，你跟着第一段看。','你已经读完了。','请把所有书都买了。'])],
3:[('我两点到，三点要走，能帮忙吗？','Can I help if I arrive at two and leave at three?',['能，小周三点来接班。','要到晚上才能走。','今天没有名单。']),('这里四把椅子，我们怎么搬？','How shall we move these four chairs?',['每人搬两把吧。','只搬一把就都搬完了。','三点她会来接班。'])],
4:[('小周三点和四点都可以的话，你帮我问问？','Could you ask Xiao Zhou whether three or four works?',['行，我下午联系她。','我已经替她理发了。','两页就是一页。']),('你去复印，能帮我也印这一页吗？','Could you copy this page too while you’re photocopying?',['能，把这一页发给我吧。','小周四点还没说话。','我认识门口那只猫。'])]}

GLOSSES=[('夫妻店','shop run by a couple'),('眼镜','glasses'),('方言','dialect'),('家乡话','hometown dialect'),('寄','send by post'),('填写','fill in a form'),('依靠','rely on'),('经验','experience'),('集合','gather'),('留','save; keep'),('开窗','open a window'),('窗口','window opening'),('位子','seat'),('猫','cat'),('空手','empty-handed'),('猫咪','cat'),('怪不得','no wonder'),('门口','entrance'),('列','list'),('名单','list of names'),('突出','stand out'),('发挥','make use of'),('资格','eligibility'),('标','mark'),('评分','marking; scoring'),('评','evaluate'),('游客','visitor; tourist'),('暂时','temporarily'),('尝试','try'),('挪','move a little'),('喊','shout'),('培训','training'),('登记','register'),('交接','handover'),('接班','take over a shift'),('借','borrow; lend'),('整理','organise; tidy'),('书架','bookshelf'),('需求','demand'),('交通','transport'),('填报','complete and submit a form'),('课程','course'),('承担','take on'),('照看','look after'),('壶','pot; kettle'),('地图','map'),('报名','sign up'),('采访','interview'),('记者','reporter'),('邻居','neighbour'),('窗户','window'),('纸','paper'),('茶杯印','teacup mark'),('印','print; mark'),('排队','queue'),('一边','while'),('收到','receive'),('复印','photocopy'),('才','only then'),('当','serve as; act as'),('到齐','all arrive'),('接待','welcome; receive visitors'),('故乡','hometown'),('训练','train; training'),('行李','luggage'),('挡住','block'),('兴趣','interest'),('申请','apply'),('鼓励','encourage'),('补充','add information'),('范围','range; scope')]

GLOSSES += [('反应过来','realise; catch on'),('呀','conversational exclamation particle'),('被','marks a passive construction'),('敢','dare'),('轮到','be someone’s turn'),('文章','article'),('结尾','ending'),('复杂','complicated'),('项','classifier for tasks and projects'),('发挥','make use of'),('表演','performance; perform'),('内','inside; within'),('打扫','clean'),('附近','nearby'),('根据','according to'),('作品','a work or creation'),('幸好','luckily'),('错误','error; mistake')]

for number,(d,r,m) in TEXTS.items():
    p=json.loads((ROOT/f'content/packs/s3-u{number:02}.json').read_text('utf-8'))
    examples={};contexts=[]
    for raw in VOCAB[number].splitlines():
        word,z,e,z2,e2=raw.split('|');assert word in z and word in z2 and z!=z2
        examples[word]=(z,e);contexts.extend([(z,e),(z2,e2)])
    assert set(examples)=={v['hanzi'] for v in p['vocabulary']}
    dqs,rqs=QUESTIONS[number]
    index={1:8,2:5,3:1,4:4}[number]
    true_statement={1:'The hometown is in the south.',2:'The left passage is shorter.',3:'The volunteer arrives at two and leaves at three.',4:'The narrator will copy two pages at the office.'}[number]
    false_statement={1:'The narrator does not plan to return next week.',2:'The narrator decides not to return.',3:'The narrator refuses to help next time.',4:'Chen Yu had been thinking about his copied page the whole time.'}[number]
    tasks=[tf(*rows(d)[index],true_statement,True,'The heard line states this fact.'),tf(*rows(r)[-1],false_statement,False,'The heard line states a different outcome.'),
           *[reply(z,e,c,0,'This reply responds directly to the immediate question.') for z,e,c in REPLIES[number]]]
    for word in {1:['家乡','父亲'],2:['范围','资格'],3:['负责','分组'],4:['理发','复印']}[number]:tasks.append(fill(*examples[word],word))
    example_rows=list(examples.values());tasks.extend(match(example_rows[i:i+3]) for i in [0,3,6])
    inherited=[(g['hanzi'],g['meaning']) for t in [p['dialogue'],p['reading'],*p['extraReadings']] for g in t.get('glosses',[])]
    repair(number,dict(dialogue=(rows(d),dqs),reading=(rows(r),rqs),media=(rows(m),[]),examples=examples,contexts=contexts,tasks=tasks,
        dialogueSpeakers={1:['李宁','陈宇'],3:['陈宇','林安']}.get(number,['林安','陈宇']),
        mediaSpeakers={1:['陈宇','李宁'],3:['陈宇','林安']}.get(number,['林安','陈宇']),
        glosses=list(dict.fromkeys(inherited+GLOSSES)),
        usage=[('Ask about the next practical action',REPLIES[number][0][0],REPLIES[number][0][1],'Ask one clear question at a time.')],
        turns=[(z,e,'Answer the immediate question',[c[0]]) for z,e,c in REPLIES[number]],
        review='Early HSK 3 correction: warm introductions at a reading group, a hesitant reader taking a first turn, a one-hour volunteer handover and friends helping with messages and copying. Removed relationship-inference, unlimited-consent and assessment-policy cautions from ordinary speech. All 22 target records have two independent authored contexts, including formal or bound forms outside the casual scene. Preserved all old unit/word/task IDs. Native flags: 老王 and 小李 forms of address; bound 者/员 and 志愿 application sense; 怕是 cautious prediction; colloquial 留个位子/接班 and quiet cat/chair teasing; 没收到 méi shōu dào rather than 没收 mò shōu; warmth versus familiarity in 亲切; 亲 as blood relation or closeness. Check every factual key against its own heard line.'),publish='--publish' in sys.argv)

for uid,terms in [('s3-u24',[('陪','accompany; keep someone company')]),('s3-u32',[('邀请','invite; invitation')]),('s4-u01',[('打招呼','greet; say hello')]),('s5-u11',[('允许','allow')])]:
    path=ROOT/f'content/packs/{uid}.json'
    source=path if path.exists() else ROOT/f'output/advanced-course-drafts/{uid}.json'
    pack=json.loads(source.read_text('utf-8'))
    for text in [pack['dialogue'],pack['reading'],*pack['extraReadings']]:
        for word,meaning in terms:
            if any(word in l['zh'] for l in text['lines']) and not any(g['hanzi']==word for g in text.get('glosses',[])):
                text.setdefault('glosses',[]).append(dict(hanzi=word,pinyin=py(word),meaning=meaning))
    destination=ROOT/('content/packs' if '--publish' in sys.argv else 'output/parity-editorial-drafts')/path.name
    destination.write_text(json.dumps(pack,ensure_ascii=False,indent=2)+'\n','utf-8')
