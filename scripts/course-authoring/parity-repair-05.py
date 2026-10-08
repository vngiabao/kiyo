"""Independent contexts and task repairs for the four already rewritten media scenes."""
import sys,json
from common import line,py
from editorial_repair import ROOT,tf,reply,fill,match

ROWS={
41:'''播出|这期节目明天播出。|This episode airs tomorrow.|这个节目每周六播出。|This programme airs every Saturday.
播放|请播放第二段，我想再听一次。|Please play the second part; I'd like to hear it again.|这首歌刚才已经播放过了。|This song was already played just now.
导演|导演正在跟演员说话。|The director is speaking to the actor.|我很喜欢这位导演以前的作品。|I really like this director's earlier work.
话剧|我们周末一起去看话剧。|Let's see a play together this weekend.|这部话剧我已经看过两次。|I've seen this play twice.
记者|记者采访了几位游客。|A reporter interviewed some visitors.|那位记者想问我们几个问题。|That reporter would like to ask us a few questions.
剧场|剧场门口已经有人在等了。|People are already waiting outside the theatre.|这个剧场离车站不远。|This theatre is near the station.
连续剧|这部连续剧我看到第十集了。|I've reached episode ten of this drama.|她每周都等着看这部连续剧。|She looks forward to this drama each week.
收音机|我爷爷每天早上听收音机。|Grandpa listens to the radio every morning.|这个收音机用了很多年。|This radio's been used for many years.
现场|我们到现场的时候，比赛还没开始。|The match hadn't started when we reached the venue.|现场的声音比录像里大。|It was louder in person than in the recording.
影视|她对影视工作很感兴趣。|She's interested in film and television work.|学校有一个影视社团。|The school has a film and television club.
直播|我错过了直播，晚上再看录像。|I missed the live broadcast; I'll watch the recording tonight.|这次演出有直播吗？|Will this performance be streamed live?
演|她在这部剧里演老师。|She plays a teacher in this drama.|你来演姐姐，我演妹妹。|You play the older sister; I'll play the younger one.
热爱|她一直热爱音乐。|She's always loved music.|我认识几位热爱话剧的朋友。|I know some friends who love theatre.
古|我们明天去看看那座古城。|We'll visit that old city tomorrow.|这是一本介绍古代生活的书。|This book is about life in ancient times.
重大|这件事对他有重大影响。|This had a major effect on him.|她做了一个重大决定。|She made a major decision.
伟大|我觉得她是一位伟大的作家。|I think she's a great writer.|书里讲了几位伟大的科学家。|The book describes several great scientists.
直|把背坐直，别趴在桌上。|Sit with your back straight; don't lean over the desk.|这条路又长又直。|This road is long and straight.
准|我的手表不准，快了五分钟。|My watch is inaccurate; it's five minutes fast.|她回答得很准。|Her answer was precise.
眼前|眼前这座楼就是我们的学校。|This building in front of us is our school.|她把照片放在我眼前。|She put the photo in front of me.
为|这位作家为很多读者所喜爱。|This writer is loved by many readers.|这首歌为很多人所熟悉。|This song is familiar to many people.
性别|这张表上要写姓名和性别。|This form asks for name and gender.|我忘了填性别那一项。|I forgot to complete the gender field.
迎接|我去门口迎接朋友。|I'll meet my friend at the entrance.|大家准备了一个小活动迎接新同学。|Everyone prepared a small event to welcome the new classmate.
''',
42:'''指|她指着门口，叫我看那张牌子。|She pointed to the door and asked me to look at the sign.|你指的是昨天那个朋友吗？|Do you mean the friend from yesterday?
指出|她指出通知上的日期错了。|She pointed out the wrong date on the notice.|老师指出了我文章里的几个问题。|The teacher pointed out some problems in my article.
指导|教练指导我们练这个动作。|The coach guides us through this movement.|谢谢你指导我做完这件事。|Thanks for guiding me through this.
调|把声音调低一点。|Turn the volume down a little.|你能把灯调亮一点吗？|Could you make the light brighter?
调整|我把椅子的高度调整了一下。|I adjusted the chair's height.|我们需要调整一下时间。|We need to adjust the time.
线|这根线太短，够不到桌子。|This cable is too short to reach the table.|纸上有三条线。|There are three lines on the paper.
铁|这个架子是铁做的。|This frame is made of iron.|铁比这种木头重。|Iron is heavier than this kind of wood.
造|我们想在这里造一座小桥。|We want to build a little bridge here.|爷爷小时候造过一条小船。|Grandpa built a little boat as a child.
造成|大雨造成了很多不便。|The heavy rain caused inconvenience.|地址写错造成了误会。|The wrong address caused a misunderstanding.
打破|球打破了窗户。|The ball broke the window.|他一句玩笑打破了安静。|His joke broke the silence.
使|这个办法使工作方便多了。|This approach made the work much easier.|朋友的帮助使我安心了。|My friend's help reassured me.
形成|讨论以后，我们形成了一个计划。|We formed a plan after discussing it.|他已经形成了每天读书的习惯。|He's developed a daily reading habit.
形状|这个盒子的形状很特别。|This box has an unusual shape.|你能画出它的形状吗？|Can you draw its shape?
转|把牌子转过来，让我看看。|Turn the sign around so I can see.|这个小灯转得很慢。|This little lamp rotates slowly.
转变|她的想法有了转变。|Her thinking has changed.|这个地区正在发生转变。|This region is undergoing change.
总结|会议结束以后，他写了一份总结。|He wrote a summary after the meeting.|这份总结只有一页。|This summary is just one page.
一切|一切都准备好了。|Everything is ready.|谢谢你为我做的一切。|Thanks for everything you've done for me.
应当|你应当先休息一下。|You should rest first.|我们应当按时到。|We should arrive on time.
专门|她专门来给我送这本书。|She came especially to bring me this book.|我专门留了一个下午给你。|I set aside an afternoon especially for you.
专题|这期节目有一个关于家乡的专题。|This programme has a special feature about hometowns.|我们正在准备这个专题的材料。|We're preparing materials for this special topic.
关注|我最近很关注这位作家的新书。|I've been following this writer's new book closely.|谢谢你关注我们的活动。|Thanks for taking an interest in our event.
提问|讲完以后，大家可以提问。|You can ask questions after the talk.|她先举手，再提问。|She raised her hand before asking a question.
''',
43:'''重|他把这段话重读了一遍。|He read this passage again.|请把这个字重写一次。|Please rewrite this character once.
代|她代我去取了书。|She collected the books on my behalf.|我今天不能去，请你代我参加。|I can't attend today; please go on my behalf.
带动|她的笑带动大家也笑起来。|Her laughter got everyone laughing.|这个活动带动了更多人参加。|This event encouraged more people to join.
管|谁管这里的钥匙？|Who's in charge of the keys here?|这件事不归我管。|This isn't my responsibility.
合|把这两块木头合在一起。|Join these two pieces of wood.|两张桌子合起来，就能坐八个人。|Eight people can sit at the two tables joined together.
和平|大家都希望和平。|Everyone hopes for peace.|这本书讲的是战争与和平。|This book is about war and peace.
划船|周六我们去湖里划船。|Let's go rowing on the lake Saturday.|他从小就会划船。|He's been able to row since childhood.
排|请把椅子排好。|Please arrange the chairs.|他们在门外排成一条长队。|They formed a long queue outside.
前进|这条路不好走，我们只能慢慢前进。|This road is difficult; we can only move forward slowly.|大家继续向前进。|Everyone kept moving forward.
团|我们跟一个旅行团一起去。|We're going with a tour group.|这个艺术团下周来演出。|This arts group will perform here next week.
团结|大家很团结，一起完成了工作。|Everyone worked together and completed the job.|这次活动让我们更加团结。|This event brought us closer together.
推广|他们想推广这个新办法。|They'd like to promote this new approach.|学校正在推广读书活动。|The school is promoting reading activities.
外交|她想了解这个国家的外交历史。|She wants to learn about this country's diplomatic history.|这本书介绍了几次重要的外交活动。|This book describes several important diplomatic events.
武器|这部电影里出现了几种武器。|Several weapons appear in this film.|博物馆里有古代的武器。|The museum has ancient weapons.
烟|厨房里突然有了很多烟。|Smoke suddenly filled the kitchen.|远处的烟挡住了山。|Smoke in the distance hid the mountain.
直到|直到晚上，他才回复我。|He didn't reply until evening.|我一直等到下课，直到她走出来。|I waited until class ended and she came out.
停止|雨终于停止了。|The rain finally stopped.|音乐停止以后，大家都坐下了。|Everyone sat down after the music stopped.
随|你随我来，我带你去看看。|Come with me; I'll show you.|他随老师一起进了教室。|He entered the classroom with the teacher.
追|我跑了两步，才追上她。|I had to run a few steps to catch up with her.|小狗追着球跑。|The puppy ran after the ball.
争|他们争着要帮老师拿东西。|They eagerly offered to carry things for the teacher.|两个人都想争第一。|Both want to compete for first place.
争取|我想争取一次上场的机会。|I'd like to earn a chance to play.|我们争取明天把事情做完。|We'll try to finish it tomorrow.
玩具|这个玩具是弟弟的。|This toy belongs to my younger brother.|她把旧玩具送给了邻居家的孩子。|She gave her old toys to the neighbour's child.
''',
44:'''存在|这个问题仍然存在。|This problem still exists.|这两种情况都可能存在。|Both situations may exist.
单元|这个单元一共有三课。|This unit has three lessons.|下个单元我们学习新的内容。|We'll study new material in the next unit.
发动|她发动同学一起整理教室。|She rallied classmates to tidy the classroom.|他发动朋友们来帮忙。|He got his friends together to help.
光明|走出屋子以后，眼前一片光明。|Outside the room, everything ahead was bright.|他希望孩子有光明的未来。|He hopes the child has a bright future.
结实|这个袋子很结实，能用很久。|This bag's sturdy and should last.|椅子不太结实，先别站上去。|The chair isn't sturdy; don't stand on it.
开业|这家店明天开业。|This shop opens for business tomorrow.|小店开业以后，来了不少客人。|Many customers came after the little shop opened.
联合国|报上有一篇关于联合国的报道。|The newspaper has a report about the United Nations.|老师让我们找联合国的资料。|The teacher asked us to find information on the United Nations.
牌子|门口的牌子写着下午休息。|The sign outside says closed this afternoon.|这块牌子太小，我看不清。|This sign's too small for me to read clearly.
气候|这里的气候很干燥。|The climate here is dry.|我还没适应这里的气候。|I haven't adapted to this climate yet.
去世|她爷爷去年去世了。|Her grandfather died last year.|那位作家去世以后，朋友整理了他的作品。|The writer's friends organised his works after he died.
人类|这本书介绍了人类的历史。|This book introduces human history.|老师在课上讲了人类生活的变化。|The teacher discussed changes in human life.
实际上|我看着很安静，实际上很紧张。|I look calm, but I'm actually nervous.|实际上，她已经来过这里两次。|She's actually been here twice.
属|这里属城南区。|This place falls under the southern district.|这项工作属他负责。|This task falls under his responsibility.
属于|这个包属于她。|This bag belongs to her.|这里已经不属于我们的学校了。|This place no longer belongs to our school.
谈|我们先谈时间，再谈地点。|Let's discuss the time before the place.|她不想谈这件事。|She doesn't want to talk about this.
谈判|谈判进行了三个小时。|The negotiation lasted three hours.|双方下周继续谈判。|The two sides will resume negotiations next week.
握手|我们见面的时候握了握手。|We shook hands on meeting.|她笑着跟我握手。|She smiled and shook my hand.
游戏|这个游戏可以三个人一起玩。|Three people can play this game together.|游戏结束以后，我们再聊天。|Let's talk after the game.
照|照着这张图做，就能找到地方。|Follow this diagram to find the place.|你照着说明慢慢来。|Follow the instructions and take your time.
组合|这几个词可以组合成一句话。|These words can form a sentence.|这个组合里有三个人。|There are three people in this group.
左右|十个人左右会来。|About ten people will come.|我们在这里等了半小时左右。|We waited here for about half an hour.
'''}

for number,raw in ROWS.items():
    uid=f's3-u{number:02}'
    p=json.loads((ROOT/f'content/packs/{uid}.json').read_text('utf-8'))
    examples={};contexts=[]
    for s in raw.strip().splitlines():
        w,z,e,z2,e2=s.split('|');assert w in z and w in z2
        examples[w]=(z,e);contexts.extend([line(z,e),line(z2,e2)])
    assert set(examples)=={v['hanzi'] for v in p['vocabulary']}
    for v in p['vocabulary']:v['example']=line(*examples[v['hanzi']])
    if number==44:
        next(v for v in p['vocabulary'] if v['hanzi']=='属')['register']='formal'
    notebook=next(t for t in p['extraReadings'] if t['id'].endswith('-word-notebook'))
    notebook.update(title=p['unit']['title']+': words in context',lines=contexts,questions=[])
    notebook.pop('cloze',None)
    glossary=[('历史','history'),('喜爱','love; be fond of'),('熟悉','familiar'),('趴','lie or lean face-down'),('采访','interview'),('游客','visitor; tourist'),('古代','ancient times'),('科学家','scientist'),('改','change; revise'),('尺寸','dimensions'),('钥匙','key'),('球','ball'),('战争','war'),('和平','peace'),('艺术团','arts group'),('湖','lake'),('邻居','neighbour'),('双方','both sides'),('干燥','dry'),('普','general; universal'),('熟','familiar; ripe'),('届','classifier for an event edition'),('重','again'),('移','move')]
    for z,e in glossary:
        if any(z in l['zh'] for l in contexts) and not any(g['hanzi']==z for g in notebook.get('glosses',[])):
            notebook.setdefault('glosses',[]).append(dict(hanzi=z,pinyin=py(z),meaning=e))
    checks={
        41:[('直播','The speaker watched the live broadcast.',False),('为','Many readers like this writer.',True)],
        42:[('应当','They have already arrived on time.',False),('造','Grandpa built a boat as a child.',True)],
        43:[('争取','The speaker has already been selected to play.',False),('直到','He did not reply until evening.',True)],
        44:[('开业','The shop opens today.',False),('属于','The bag belongs to her.',True)]}[number]
    responses={
        41:[('咖啡太甜了，怎样才能少甜一点？','How can we make this coffee less sweet?',['加一点没放糖的咖啡吧。','再放两勺糖吧。','把杯子放在桌上吧。']),('你在哪里看到导演的采访？','Where did you see the director’s interview?',['在网上，我把地址发给你。','采访大约有二十分钟。','导演说他很喜欢这部剧。'])],
        42:[('我漏听了刚才那一句，怎么再听一次？','How can I hear the line I just missed again?',['倒回去再看看吧。','直接跳到最后吧。','把画面调亮一点吧。']),('隔壁已经睡了，怎么不吵到他们？','How can we avoid disturbing the neighbours who are asleep?',['把声音调低一点。','把声音调大一点。','把字幕切换成大一点的字。'])],
        43:[('我一快就唱不清楚，应该先练什么？','What should I practise first if the words become unclear when I speed up?',['先慢一点，把字唱清楚。','再快一点，别管字。','先把音量调到最大。']),('读完一遍以后，接下来怎么练？','What should I practise after reading it through once?',['跟着节拍慢慢唱。','先读一遍再说。','这首歌大约三分钟。'])],
        44:[('老板的新通知在哪里？','Where is the owner’s new notice?',['在群里，我发给你。','六点半去吃面。','小周明天可能加班。']),('她要是加班，咱们怎么办？','What will we do if she works overtime?',['咱们先吃，她有空再来。','她就在新开的店工作。','店里的面听说不错。'])]}[number]
    replacements=[]
    for word,statement,answer in checks:
        z,e=examples[word]
        if number==42 and word=='造':z,e='爷爷小时候造过一条小船。','Grandpa built a little boat as a child.'
        replacements.append(tf(z,e,statement,answer,'The stated action or time directly supports the key.'))
    replacements.extend(reply(z,e,c,0,'This reply answers the specific question; the other lines do not.') for z,e,c in responses)
    for i,t in enumerate(replacements):p['tasks'][i]=dict(id=p['tasks'][i]['id'],phrase=p['tasks'][i]['phrase'],**t)
    choices={41:['导演','剧场'],42:['调整','总结'],43:['推广','和平'],44:['实际上','组合']}[number]
    for i,w in zip([4,5],choices):p['tasks'][i]=dict(id=p['tasks'][i]['id'],phrase=p['tasks'][i]['phrase'],**fill(*examples[w],w))
    values=list(examples.values())
    for i in range(6,len(p['tasks'])):
        p['tasks'][i]=dict(id=p['tasks'][i]['id'],phrase=p['tasks'][i]['phrase'],**match(values[(i-6)*3:(i-6)*3+3]))
    p['notes']+='\n2026-10-08 independent vocabulary review: removed abstract cautionary/meta examples. Two authored contexts per stated sense, exact old IDs retained. Task keys checked against explicit statements; reply tasks ask for a constructive response to a concrete problem. Native review pending: passive 为, chong 重, formal 属, short colloquial statements and bereavement wording. No automatic native or pronunciation certification.'
    target=ROOT/('content/packs' if '--publish' in sys.argv else 'output/parity-editorial-drafts')
    (target/f'{uid}.json').write_text(json.dumps(p,ensure_ascii=False,indent=2)+'\n','utf-8')
    print(uid,'drafted' if '--publish' not in sys.argv else 'published')

from advanced_reading_repair import dependencies
dependencies({'s5-u08':[('扫','sweep; scan (a code)')],
              's6-u06':[('拆','take apart; separate')],
              's6-u12':[('拆','open (a letter); take apart')]},publish='--publish' in sys.argv)

# Preserve definitions that later texts previously inherited from an earlier
# incidental story occurrence. No saved IDs or recorded lines change here.
for uid,entries in {'s4-u09':[('申','state; apply'),('码','code')], 's4-u10':[('赞','praise')], 's4-u11':[('赞','praise'),('藏','hide')]}.items():
    p=json.loads((ROOT/f'content/packs/{uid}.json').read_text('utf-8'))
    for t in [p['dialogue'],p['reading'],*p['extraReadings']]:
        for w,e in entries:
            if any(w in l['zh'] for l in t['lines']) and not any(g['hanzi']==w for g in t.get('glosses',[])):
                t.setdefault('glosses',[]).append(dict(hanzi=w,pinyin=py(w),meaning=e))
    target=ROOT/('content/packs' if '--publish' in sys.argv else 'output/parity-editorial-drafts')
    (target/f'{uid}.json').write_text(json.dumps(p,ensure_ascii=False,indent=2)+'\n','utf-8')
