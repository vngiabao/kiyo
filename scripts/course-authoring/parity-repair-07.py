"""Earlier HSK 3: introduce a friend, compare plans, share photos, start a course."""
import json,sys
from editorial_repair import repair,tf,reply,fill,match,ROOT
from advanced_core import rows
from common import dictionary,py
from parity_repair_07_contexts import VOCAB

TEXTS={
25:(
'''你说的那个朋友，是我们初中同学小周吗？|Is the friend you mentioned Xiao Zhou, our classmate from junior secondary school?
对，她最近写了一篇旅行的文章。|Yes. She recently wrote an article about a trip.
我看过！里面那张窗边的照片，也是她拍的？|I've read it! Did she take the photo beside the window too?
是。她文字写得好，照片也拍得好。|Yes. She writes well and takes good photos too.
真有本事。我写到一半就不知道写什么了。|She's talented. I never know what to write halfway through.
你不是没有事情写，是一开始就想把整年都写完。|You have things to write about. You just try to fit the whole year in from the start.
那我只写上次去看表演？|Should I just write about seeing that performance?
可以。先写门口等人的那一段，我读着就想笑。|Yes. Start with waiting for people at the entrance. That makes me smile when I read it.
我能不能请小周帮我看一下？|Could I ask Xiao Zhou to take a look?
我问问她。她这周在赶文章，周末可能有空。|I'll ask. She's finishing an article this week and may be free at the weekend.
好，我先把那一段写好，别空着手请人家改。|Good. I'll finish that passage first rather than ask her to revise a blank page.
写完发给我，我也想看你怎么写那天。|Send it when it's done. I'd like to see your version of that day too.
''',
'''陈宇提起小周，我才想起她是我们初中同学。上次见她时，我们都还在准备考试，现在她已经会给杂志写文章了。|When Chen Yu mentioned Xiao Zhou, I remembered our junior secondary school classmate. Last time we met we were preparing for exams; now she writes for magazines.
我读了她写的旅行故事。文章里没有把每一天都列出来，只写在一座小城住的三个晚上。房东的猫每天来窗边，她就从那只猫开始写。|I read her travel story. It did not list every day, just three nights in a small town. The landlord's cat came to the window daily, and that was where she began.
我原来想把一年的事情都放进自己的文章，写到一半就停了。陈宇让我先写一个晚上，我选了上次和朋友去看表演的那天。|I had tried to put a whole year in my own article and stopped halfway. Chen Yu suggested one evening. I chose the night we went to a performance with friends.
最开始我只写大家很高兴，读起来却没有什么画面。后来写到陈宇在门口找票、朋友从包里拿出三张票，我自己读着都笑了。|At first I only wrote that everyone was happy, which gave little to picture. Later I described Chen Yu searching for his ticket while a friend took three out of her bag. I smiled reading it myself.
周末，小周看了那一段，问票为什么在朋友包里。我才发现忘了写买票的事，赶紧加上前面的两句。她没有替我全部重写，只指出读者可能会问的地方。|At the weekend Xiao Zhou read it and asked why the tickets were in the friend's bag. I had left out buying them, so I added two earlier sentences. She did not rewrite everything; she pointed out where a reader might ask a question.
我把改好的文章发给陈宇。他说这回能看见那天的样子了，还问能不能把最后一句留给他。那句写着，你下次先看看是谁买票，再找自己的口袋。|I sent the revised article to Chen Yu. He said he could picture that evening now and asked to keep the last line for himself: next time, check who bought the tickets before searching your pockets.
''',
'''小周说你这篇文章读着很轻松。|Xiao Zhou says your article is an easy read.
真的吗？我改了三遍。|Really? I revised it three times.
读的人轻松，不等于写的人也轻松。|An easy read needn't be easy to write.
那你也试试，写一下你找票的样子。|You try, then. Write about searching for your ticket.
我怕写得太生动，大家以后都记得。|If it's too vivid, everyone will remember it forever.
已经记得了，你放心写吧。|They remember already. Go ahead and write it.
'''),
26:(
'''周六去哪儿看电影？你选的那家店怎么样？|Where shall we watch the film on Saturday? How is the place you chose?
好是好，就是离车站有点远。|It's good, but a little far from the station.
多远？下车还要走很久？|How far? Is it a long walk after getting off?
大概二十分钟。优点是旁边有小店，看完能吃饭。|About twenty minutes. The good part is the shops nearby; we can eat afterwards.
要是下雨，二十分钟就不好玩了。|Twenty minutes won't be much fun in the rain.
那看看靠车站的那家？房间不大不小，三个人正好。|Shall we try the one near the station? The room is just right for three.
我看过照片，椅子好像不太舒服。|I've seen the photos. The chairs don't look very comfortable.
上次我坐过，还行。电影只有一个多小时。|I've sat there before. They're all right. The film is only a little over an hour.
那就选这家吧。我宁愿椅子简单一点，也不想淋雨。|Let's choose it. I'd rather have simple chairs than get rained on.
行。我来订房间，你问小周几点能到。|Fine. I'll book the room; you ask when Xiao Zhou can get there.
好，选个地方也真考验耐心。|Okay. Choosing a place really tests your patience.
只要你别再拿出第四家，我们已经快选好了。|Just don't bring out a fourth place. We're nearly done.
''',
'''我们想周六和小周一起看一部电影，找了三家有小房间的店。第一家照片很好看，但离车站要走二十分钟。|We wanted to watch a film with Xiao Zhou on Saturday and found three places with small rooms. The first looked lovely in photos but was a twenty-minute walk from the station.
我本来最喜欢第一家，陈宇问我下雨时还想不想走。我看了一下天气，周六可能下雨，只好再看另外两家。|I liked the first best until Chen Yu asked about walking in the rain. The forecast suggested rain on Saturday, so I reconsidered the other two.
第二家就在车站旁边，房间不大不小，三个人够坐。椅子看上去简单，陈宇说自己上次坐过，坐一个多小时没有问题。|The second was right by the station, with a room sized for three. The chairs looked plain, but Chen Yu had sat there before and found them fine for a little over an hour.
第三家椅子很舒服，可星期六只剩上午有空房间。小周上午要上班，所以这一家这次不合适。|The third had comfortable chairs, but only a morning slot remained on Saturday. Xiao Zhou worked in the morning, so it did not suit us this time.
我们最后订了第二家下午三点的房间。我把地址发给小周，她说下车就能到，正好不用赶路。|We booked the second place for three in the afternoon. I sent Xiao Zhou the address. She was pleased it was right by the stop, so she would not have to rush.
周六果然下雨了。我从车站走到店门口，只用了一分钟。陈宇问我还想不想去第一家，我说先让我把伞收好，再想那二十分钟的事。|It did rain on Saturday. The walk from the station took one minute. Chen Yu asked if I still wanted the first place. I told him to let me fold my umbrella before considering that twenty-minute walk.
''',
'''这椅子好像真的有点硬。|This chair really does feel a little hard.
你换这把，我上次坐的是这把。|Try this one; it's the one I used last time.
你怎么不早说？|Why didn't you say that earlier?
你刚才一直站着看菜单嘛。|You were standing there looking at the menu.
菜单好是好，就是每一样我都想吃。|It's a good menu; I just want everything on it.
那等电影看完再慢慢选，椅子已经选好了。|Choose after the film. We've sorted out the chairs.
'''),
27:(
'''你昨天发的照片，是在哪里拍的？|Where did you take the photo you sent yesterday?
河边。你看照片里的那座桥。|By the river. Look at the bridge in the photo.
看起来很近，你们走过去了吗？|It looks close. Did you walk there?
走了二十分钟，比照片里远。|It took twenty minutes; it's farther than it looks in the photo.
这块石头看上去也很大。|The rock looks big too.
其实不高，我坐上去刚好能把脚放在地上。|It's not tall. Sitting on it, I could put my feet on the ground.
照片里的天空真蓝，景色很美。|The sky is so blue in the photo. The scenery is beautiful.
上午有阳光，下午就下雨了。我们赶紧往桥那边走。|It was sunny in the morning but rained in the afternoon. We hurried towards the bridge.
我下次也想去，你带我吧？|I'd like to go next time. Will you take me?
好，带双好走的鞋。我的鞋里全是沙子。|Sure. Bring shoes you can walk in. Mine were full of sand.
那你先把沙子倒出来，别带到我家。|Empty the sand first. Don't bring it into my home.
放心，我回家才发现，已经倒过了。|Don't worry. I found it when I got home and emptied them already.
''',
'''朋友发给我一张河边的照片。天空很蓝，阳光照着石头，远处有一座桥。我看着照片，觉得这个地方很美，也想去一次。|A friend sent a riverside photo. The sky was blue, sunlight fell on a rock, and a bridge stood in the distance. It looked beautiful, and I wanted to visit.
她说照片是上午拍的，下午下了雨。我问桥是不是就在旁边，她笑着说从石头那里走过去要二十分钟。|She had taken the photo in the morning; it rained in the afternoon. When I asked if the bridge was nearby, she laughed: it was a twenty-minute walk from the rock.
第二个周末，我们带水和一点吃的去河边。她指给我看那块石头，我才发现它没有照片里那么大，坐上去脚还能放在地上。|The following weekend we took water and snacks to the river. She showed me the rock. It was smaller than it looked in the photo; I could sit with my feet on the ground.
我想拍一张和她上次一样的照片，她站到旁边指了指方向。我把桥也放进画面里，拍完看看，桥又显得很近了。|I wanted a photo like hers. She stood beside me and pointed out the angle. I included the bridge and checked the result; once again it looked close.
这次我们慢慢走到桥边，没有遇到雨。桥上风很大，我拿出一根香蕉，朋友说别站着吃，我们下去找地方坐。|This time we walked slowly to the bridge and had no rain. It was windy up there. When I took out a banana, my friend suggested finding a place to sit below.
回家以后，我把照片发给陈宇。他问从石头走到桥要多久，我说二十分钟，别只看照片就以为下车已经到了。|Back home I sent the photo to Chen Yu. He asked about the walk from the rock to the bridge. Twenty minutes, I said; the photo did not mean he would arrive as soon as he stepped off the bus.
''',
'''这张照片里，你看起来比我高。|You look taller than me in this photo.
我站在石头上，你站在沙子里。|I'm standing on the rock; you're in the sand.
怪不得。我还以为自己变矮了。|No wonder. I thought I'd got shorter.
要不要换个位置再拍？|Shall we swap places for another photo?
要。这次让我站石头上。|Yes. Let me stand on the rock this time.
好，但石头就这么高，别期待变成大树。|Sure, but the rock is only so tall. Don't expect to turn into a tree.
'''),
28:(
'''你报的初级游泳课，什么时候开始？|When does your beginner swimming course start?
从下周起，周二和周四晚上六点半上课。|From next week, Tuesdays and Thursdays at six thirty in the evening.
下班以后赶得上吗？|Can you get there after work?
我五点半下班，坐车二十分钟，应该来得及。|I finish at five thirty. The bus takes twenty minutes, so I should have time.
我也想报。我从初中以后就很少游泳了。|I'd like to join too. I haven't swum much since junior secondary school.
那我们一起。教练说第一节不用游很远，先慢慢来。|Let's go together. The coach says we won't swim far in the first class; we can take it slowly.
几点到比较好？|What time should we arrive?
六点十五分吧，还要换衣服。|Six fifteen. We need time to change.
好。你第一次别等我到了才进去。|Good. Don't wait for me before going in the first time.
为什么？你要迟到？|Why? Will you be late?
不是，我怕你在门口等，我在里面等，两个人就这么一直等着。|No. You might wait outside while I wait inside, and we'd both just keep waiting.
那就在门口见，到了先发消息。|Let's meet at the entrance, then. Send a message when you arrive.
''',
'''从下周起，我周二和周四晚上要去上初级游泳课。陈宇也报了，我们约好第一天六点十五分在门口见。|My beginner swimming classes were due to start the following week, on Tuesday and Thursday evenings. Chen Yu joined too. We arranged to meet at the entrance at six fifteen on the first day.
周二我五点半下班，坐车去游泳馆。下车时才六点，我慢慢走到门口，先发消息说自己已经到了。|On Tuesday I finished work at five thirty and took a bus to the pool. It was only six when I got off, so I walked slowly to the entrance and messaged that I had arrived.
陈宇说还要等十分钟，我就坐在门边的椅子上。等他到了，两个人一起进去换衣服，没有一个人在里面、一个人在外面互相等待。|Chen Yu needed another ten minutes, so I sat on a chair by the door. We went in and changed together when he arrived, rather than waiting for each other in different places.
教练先让我们在水边坐好，说第一节主要练习怎么在水里放松。我从初中以后很少游泳，刚下水有点紧张，他让我先扶着池边试。|The coach sat us by the water and said the first lesson focused on relaxing in it. I had rarely swum since junior secondary school and felt nervous getting in. He suggested holding the side first.
下课十分钟了，我们还坐在门口喝水。陈宇问累不累，我说还好，只是脚一离开地面，就总想站起来。他说自己也是，下次再慢慢试。|Ten minutes after class we were still drinking water outside. Chen Yu asked if I was tired. I was all right, but whenever my feet left the ground I wanted to stand up. He felt the same; we could try again gradually next time.
回家路上，我们约好周四还是六点十五分见。我把时间写进手机，又把游泳的东西放回包里，这次不用到出门前才找。|On the way home we arranged the same six-fifteen meeting for Thursday. I put the time in my phone and the swimming things back in my bag, so I would not have to search just before leaving.
''',
'''下课十分钟了，你还不想回家？|Class finished ten minutes ago. Don't you want to go home?
想，但我还在等你把水喝完。|Yes, but I'm waiting for you to finish your water.
我还以为你在等下一节。|I thought you were waiting for the next class.
下次周四才来，今天已经够了。|The next one is Thursday. I've had enough for today.
行，我们慢慢走去车站。|All right, let's walk slowly to the stop.
好，这回不用赶了。|Good. No rushing this time.
''')}

QUESTIONS={
25:([
('gist','What does the narrator want?',['Help with writing one passage','A new job as a guard','To buy a camera'],0),
('detail','When might Xiao Zhou be free?',['At the weekend','Immediately that morning','Never again'],0),
('inference','Why write one evening first?',['A concrete small scene is easier to develop','There is nothing to say about that evening','Every article must cover a whole year'],0)], [
('gist','How does the article improve?',['Details and the missing ticket purchase are added','Xiao Zhou writes the entire article','All mention of the performance is deleted'],0),
('detail','What does Xiao Zhou ask?',['Why the tickets are in the friend’s bag','Why nobody sees the show','Why the landlord has no cat'],0),
('inference','What is the final pocket remark?',['Friendly teasing about the ticket search','A ban on seeing performances','A complaint about the price of tickets'],0)]),
26:([
('gist','What are they choosing?',['A place for a film with friends','An expensive new car','A whole new apartment'],0),
('detail','How far is the first place from the station?',['A twenty-minute walk','One minute','Two hours'],0),
('inference','Why accept plain chairs?',['A short walk matters more in possible rain','They will stand throughout the film','They are choosing a morning appointment'],0)], [
('gist','Which place do they book?',['The second, near the station','The first, far from the station','The third, morning only'],0),
('detail','Why reject the third this time?',['Xiao Zhou works in the morning','It has no comfortable chairs','It is twenty minutes from the station'],0),
('inference','What does the rainy arrival show?',['The short walk was useful','The first place had closed permanently','The film was cancelled'],0)]),
27:([
('gist','What are they discussing?',['How a riverside photo compares with the place','Buying a dragon picture','A television studio'],0),
('detail','How long was the walk to the bridge?',['Twenty minutes','Two minutes','One hour'],0),
('inference','Why bring walking shoes next time?',['The bridge is farther away than the photo suggests','They are entering a swimming race','They plan to stand still all day'],0)], [
('gist','What does the second visit reveal?',['The rock is smaller and the bridge farther than they look','There is no bridge','The sky is always rainy'],0),
('detail','Does it rain during their second visit?',['No','Yes, throughout','The reading does not say'],0),
('inference','Why give Chen Yu the walking time?',['The photo makes the distance look short','He already walked there that day','The rock has been moved to the station'],0)]),
28:([
('gist','What are they arranging?',['Joining beginner swimming lessons and meeting outside','A performance on Monday','A bus to another city'],0),
('detail','What time does class start?',['Six thirty in the evening','Six fifteen in the morning','Five thirty in the evening'],0),
('inference','Why choose the entrance as a meeting point?',['To avoid waiting in different places','The coach only teaches outdoors','They want to miss the first class'],0)], [
('gist','How does the first lesson go?',['They meet, practise gradually and arrange Thursday','They miss it entirely','They finish every level'],0),
('detail','What does the coach suggest at first?',['Hold the side of the pool','Swim as far as possible','Go home immediately'],0),
('inference','Why put the swimming things back in the bag?',['To avoid a last-minute search next time','To give them away','Because Thursday’s class has been cancelled'],0)])}

REPLIES={
25:[('我想请小周帮我看文章，先做什么？','What should I do before asking Xiao Zhou to look at the article?',['先写好一段，再请她看。','空着手等她全部写好。','先买一年的票。']),('照片下面的文字太小，看不清。','The text under the photo is too small to read.',['把图放大一点看看。','她是我们初中同学。','这篇文章讲旅行。'])],
26:[('周六可能下雨，那家店离车站二十分钟，换吗？','Change the place with a twenty-minute walk if rain is forecast?',['看看车站旁边那家吧。','下雨一定不用带伞。','只有上午有房间正好。']),('小周上午上班，我们什么时候看电影？','When should we watch if Xiao Zhou works in the morning?',['约下午三点吧。','上午上班时一起看。','周六没有椅子。'])],
27:[('照片里桥很近，实际走多久？','How long is the actual walk to the bridge that looks close in the photo?',['从石头那里走二十分钟。','桥就在你脚下。','上午天空很蓝。']),('我也想去河边，你带我吗？','Will you take me to the riverside too?',['好，记得带双好走的鞋。','我昨天已经把沙子倒了。','照片里的石头不高。'])],
28:[('六点半上课，还要换衣服，几点见？','When shall we meet for a six-thirty class with time to change?',['六点十五分在门口见。','下课十分钟再来。','五点半已经下课了。']),('下次周四还来吗？','Are you coming again on Thursday?',['来，还是六点十五分见。','昨天我已经等了十分钟。','我们今天周四下班。'])]}

for number,(d,r,m) in TEXTS.items():
    dictionary['精神']='jīng shén'  # Unit 26 teaches spirit, not the energetic adjective.
    pack=json.loads((ROOT/f'content/packs/s3-u{number:02}.json').read_text('utf-8'))
    examples={};contexts=[]
    for raw in VOCAB[number].splitlines():
        word,z,e,z2,e2=raw.split('|');assert word in z and word in z2 and z!=z2
        examples[word]=(z,e);contexts.extend([(z,e),(z2,e2)])
    assert set(examples)=={v['hanzi'] for v in pack['vocabulary']}
    dqs,rqs=QUESTIONS[number]
    index={25:9,26:3,27:3,28:1}[number]
    yes={25:'The friend says Xiao Zhou may be free at the weekend.',26:'The walk is about twenty minutes.',27:'The walk took twenty minutes.',28:'Classes are on Tuesday and Thursday evenings at six thirty.'}[number]
    no={25:'Chen Yu says he cannot picture the evening in the revised article.',26:'The walk from the station to the chosen place took twenty minutes.',27:'The narrator tells Chen Yu the bridge is right beside the rock.',28:'They cancel the Thursday meeting.'}[number]
    tasks=[tf(*rows(d)[index],yes,True,'This heard line explicitly supplies the information.'),tf(*rows(r)[-1],no,False,'The heard line explicitly gives a different result.'),
        *[reply(z,e,c,0,'Only this reply addresses the immediate question with the given facts.') for z,e,c in REPLIES[number]]]
    targets={25:['文章','写作'],26:['相比','考验'],27:['观察','看起来'],28:['以来','纪录']}[number]
    tasks.extend(fill(*examples[word],word) for word in targets)
    example_rows=list(examples.values());tasks.extend(match(example_rows[i:i+3]) for i in [0,3,6])
    if len(pack['tasks'])==10:tasks.append(match(example_rows[9:12]))
    glosses=[(g['hanzi'],g['meaning']) for t in [pack['dialogue'],pack['reading'],*pack['extraReadings']] for g in t.get('glosses',[])]
    glosses += [('灰','dust'),('层','layer'),('摇头','shake one’s head'),('屏幕','screen'),('出版','publish'),('毕业','graduate'),('工程师','engineer'),('淋雨','get caught in rain'),('椅子','chair'),('空位','vacant seat'),('耐心','patience'),('伞','umbrella'),('收好','put away properly'),('脚','foot'),('摸','touch'),('挖','dig'),('喂','feed an animal'),('熟','ripe'),('叶子','leaf'),('放大','enlarge'),('泳池','swimming pool'),('游泳馆','swimming centre'),('下水','get into the water'),('扶','hold onto'),('池','pool'),('圈','lap; round'),('录入','enter data'),('打破','break a record'),('放松','relax'),('将近','nearly'),('三遍','three times'),('半途','halfway'),('画面','scene; picture'),('指出','point out'),('口袋','pocket'),('修改','revise'),('原来','it turns out; previously'),('沙子','sand'),('倒','empty out; pour'),('抬头','raise one’s head'),('度过','spend a period of time'),('柔软','soft'),('一群','a group; a flock'),('故障','fault'),('迟迟','for a long time without doing something'),('产品','product'),('钥匙','key'),('值得','be worth'),('地面','ground surface'),('够','be enough'),('硬','hard'),('嘛','conversational explanatory particle')]
    glosses += [('列','list'),('轻松','easy; relaxed'),('苹果','apple'),('丢','lose'),('宁愿','would rather'),('熟悉','be familiar with'),('放弃','give up'),('吵','noisy'),('矮','short in height'),('朵','classifier for flowers'),('洞','hole'),('游泳','swim')]
    spec=dict(dialogue=(rows(d),dqs),reading=(rows(r),rqs),media=(rows(m),[]),examples=examples,contexts=contexts,tasks=tasks,glosses=list(dict.fromkeys(glosses)),
        usage=[('Ask about one concrete detail',REPLIES[number][0][0],REPLIES[number][0][1],'Use the detail to decide the next small action.')],
        turns=[(z,e,'Respond to the immediate practical question',[c[0]]) for z,e,c in REPLIES[number]],
        review='Earlier HSK 3 naturalness correction: a classmate helps with a small article, friends choose a rainy-day film venue, a photo makes a bridge look close, and two adults start swimming lessons. Removed identity/privacy/assessment cautions and report-like conversation. All target words have independently authored contexts instead of being stuffed into speech. Formed six text questions and nine or ten mixed tasks from the actual new facts while keeping all old IDs. Native flags: colloquial teasing about tickets and photos; 大主语/小主语 description; 好是好，就是; time-from 起 and elapsed 了; 精神 jīngshén as spirit versus the earlier energetic jīngshen; 录 as a bound verb in 录入; realistic descriptions of a first swimming class.')
    repair(number,spec,publish='--publish' in sys.argv)

# These meanings used to be met incidentally in the replaced scenes.
# Define them at the later use without changing its text or assessment IDs.
for uid,terms in [('s3-u37',[('阅读','read; reading'),('固定','fixed; regular'),('扩大','expand'),('几乎','almost'),('翻译','translate; translation'),('鼓励','encourage'),('绕','go around'),('临时','temporary'),('咨询','ask for information')]),('s3-u40',[('眼镜','glasses')]),('s3-u42',[('模型','model; scale model')]),('s3-u43',[('与','and; with, in a written register')]),('s4-u11',[('结构','structure')]),('s5-u01',[('挥','wave')]),('s5-u03',[('犹豫','hesitate')])]:
    path=ROOT/f'content/packs/{uid}.json'
    source=path if path.exists() else ROOT/f'output/advanced-course-drafts/{uid}.json'
    pack=json.loads(source.read_text('utf-8'))
    for text in [pack['dialogue'],pack['reading'],*pack['extraReadings']]:
        for word,meaning in terms:
            if any(word in l['zh'] for l in text['lines']) and not any(g['hanzi']==word for g in text.get('glosses',[])):
                text.setdefault('glosses',[]).append(dict(hanzi=word,pinyin=py(word),meaning=meaning))
    destination=ROOT/('content/packs' if '--publish' in sys.argv else 'output/parity-editorial-drafts')/path.name
    destination.write_text(json.dumps(pack,ensure_ascii=False,indent=2)+'\n','utf-8')
