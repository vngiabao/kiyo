"""HSK 5 readings 1–4: events and recognisable voices instead of policy lectures."""
import sys
import json
from common import ROOT,py
from advanced_reading_repair import apply,dependencies

EDITS={
1:{'-r':{
3:('他想马上开始做事，我请他先听我说完。两次电话没人接的时候，我还在楼下等，以为他过一会儿就到。司机已经把车停在门口，我却不知道该让司机再等，还是去找邻居。他听完，低头看了看那两个未接电话，说下次开会以前就联系我。',"He wanted to start helping straight away, but I asked him to hear me out. When my two calls went unanswered, I was still downstairs expecting him soon. The driver was waiting outside, and I didn't know whether to ask him to wait longer or fetch a neighbour. My friend looked at the missed calls and said he'd contact me before the meeting next time."),
4:('后来，我们一起把剩下的书放上书架。他先问我按什么顺序放，没有像上次那样只按颜色排。我把字典和常用的几本放在手边，其余的按书名排好。最后一箱打开时，里面竟然还有一杯没喝完的水。他笑我搬家连水都不肯扔，我才想起那是早上随手放进去的。',"Later we put the remaining books on the shelves together. He asked how I wanted them arranged, rather than sorting by colour as he'd done before. I kept the dictionary and a few frequently used books within reach and sorted the others by title. The last box contained a half-finished cup of water. He laughed that I wouldn't even throw water away when moving; I'd put it there absent-mindedly that morning."),
5:('晚上，我给邻居发消息谢谢他，也把借来的工具还了。朋友问下周还需要他做什么，我看了看空了一半的房间，说先让我把今天这些东西放好吧。他说行，周末有空一起吃饭。我答应了，又提醒他别到时候直接来旧地址。他拿起手机，马上把新地址存好了。',"That evening I thanked the neighbour by message and returned the borrowed tools. My friend asked what I needed next week. Looking at the half-empty room, I said to let me put today's things away first. He suggested dinner at the weekend. I agreed and reminded him not to turn up at my old address. He took out his phone and saved the new one immediately."),
6:('几天以后，朋友发来周末吃饭的时间。这次他先说星期六下午还要上班，六点以后才方便。我回他六点半见，又把饭馆门口的照片发过去。到了那天，他下班时给我打电话，说车站人有点多，可能晚十分钟。我先进去找座位，等他到了再点菜，没有像搬家那天一样站在门外猜。',"A few days later he messaged about weekend dinner. This time he said he was working on Saturday afternoon and was free after six. I suggested half past six and sent a photo of the restaurant entrance. On the day he called after work: the station was busy, and he might be ten minutes late. I went in to find a table and waited to order with him, instead of standing outside guessing as I had on moving day.")},
'-paired-reading':{
0:('那天进门以后，我看见箱子都到了楼上，刚要说“看来已经弄好了”，朋友就指了指地上的两箱书。她的外套搭在椅子上，袖口有一块灰，手里的水也已经凉了。我问重箱子是谁搬的，她说邻居帮了十分钟，司机刚才已经走了。我把包放下，才发现自己来得有多晚。',"When I walked in, the boxes were already upstairs. I was about to say, 'Looks like it's done,' when my friend pointed to two boxes of books on the floor. Her coat was on a chair, its sleeve dusty, and the water in her hand had gone cold. A neighbour had helped for ten minutes, she said, and the driver had just left. Putting down my bag, I realised how late I was."),
1:('临时开会的时候，我的手机还在桌上。同事叫我过去，我以为只要说几句话，结果一坐下就讨论了很久。中间我想到朋友可能在等，却总觉得下一句说完就能走。直到会议结束拿起手机，看见两个未接电话，我才赶紧出门。一路上我想好了一堆解释，见到她却只说出对不起。',"My phone was on my desk when the unexpected meeting began. I thought my colleague needed a quick word, but the discussion went on. I kept thinking my friend might be waiting, then telling myself I could leave after the next point. Only after the meeting, seeing two missed calls, did I hurry out. I prepared plenty of explanations on the way; face to face, all I managed was sorry."),
2:('她把没接到电话以后的情况讲完，我才知道，她一直以为我已经在路上。司机在楼下问还有多久，她没法回答；到了两点二十，才去敲邻居的门。邻居本来在做饭，关了火下来帮忙。我问能不能去谢谢他，她说工具晚上要还，到时候一起过去。我先接过她手里那杯凉水，重新倒了一杯。',"When she told me what had happened after the unanswered calls, I learned she'd thought I was already on the way. She couldn't tell the driver how much longer I'd be. At 2:20 she knocked on the neighbour's door; he'd stopped cooking to help. I asked if we could thank him. We could return his tools together that evening, she said. First I took her cold water and poured a fresh cup."),
3:('我本来想说以后绝不迟到，话到了嘴边，又想起单位下次也可能临时开会。最后我说，下次会先看安排再答应，有变化就提前打电话。她问手机又留在桌上怎么办，我说向同事借一个。她看了我一会儿，说那就这样吧，先把地上的书放好。我蹲下来打开箱子，这才知道她想按什么顺序排。',"I almost promised never to be late again, then remembered work might spring another meeting on me. I said I'd check my schedule before agreeing and call ahead if anything changed. What if my phone was on the desk again? I'd borrow a colleague's. She looked at me, then said okay: first put away the books on the floor. I crouched to open a box and finally asked how she wanted them arranged."),
5:('那天中午，我又发了一条消息，确认四点仍然可以到。她回复说，三点开始搬桌子的人已经找好了，让我到时直接整理最后留下的材料。我把工作做完，带上胶带和剪刀，出门前再看了一眼地址。那是活动室，不是她的新家，我上次存好的地址今天还用不上。',"At midday I confirmed I could still arrive at four. She'd found someone for the tables at three; I should sort the remaining materials. I finished work and packed tape and scissors, checking the address before leaving. It was the activity room, not her new home, so the address I'd saved last time wouldn't help today."),
6:('四点到了，我发消息说自己已在门口。她出来开门，说还剩两张桌子没收，材料先放在右边。我卷起袖子，和她把桌子抬回墙边，再把纸按下次要用的顺序收好。快做完时，她问我要不要一起吃点东西。我看了看手机，没有新电话，就说好，这回我真的不赶时间。',"At four I messaged that I was at the door. She opened it: two tables were still out, and the materials should go on the right. We carried the tables to the wall, then sorted the papers for next time. Near the end she suggested something to eat. I checked my phone—no new calls—and said yes: this time I really wasn't in a hurry.")}},
2:{'-r':{
6:('那天回家，我把第二句要练的位置在纸上圈出来，又存下新朋友的联系方式。他已经发来一条消息，说下次别忘了先唱再问听不听得见。我一边看一边笑，回他你也别忘了听音乐。我还是想把那两个字练好，不过想到下次进去已经有认识的人，心里没有刚出门时那么紧了。',"At home I circled the spot in the second line that needed practice and saved my new friend's contact details. He'd already messaged: next time, sing before asking if anyone could hear me. Laughing, I told him not to forget to listen for the music either. I still wanted to get those two words right, but knowing I'd recognise someone next time made me less anxious.")},
'-paired-reading':{
2:('后来有人问，刚才鼓掌是不是让他别再唱。我说不是，我是在他唱完以后鼓掌，谢谢他参加。那个人说自己坐在后面，只听见一阵掌声，没看见他已经放下话筒。我指了指旁边的空椅子，让他下次坐近一点。他笑着说好，上次也是没看清，回来以后自己想了半天。',"Someone later asked whether the applause meant he should stop singing. No, I said: I clapped after he finished, to thank him. Sitting at the back, the questioner had heard applause but hadn't seen the microphone lowered. I pointed to an empty chair nearby and suggested sitting closer next time. He laughed: last time he'd missed something too and spent ages wondering about it afterwards."),
5:('活动结束前，那位出去休息的朋友回来了，手里拿着刚买的面包。他问下次还能不能带同一段，又说已经找到了要练的位置。我把日期发给他，请他想好唱哪几句以后告诉我。旁边的人凑过来看，说这首他也在练，两个人很快交换了联系方式，约好先把第二句一起读清楚。',"Before the event ended, the friend who'd stepped outside returned with a newly bought bread roll. He wanted to bring the same section next time and knew what needed practice. I sent the date and asked him to tell me which lines he chose. Someone beside him leaned over: he was practising that song too. They exchanged details and agreed to read the second line together first."),
6:('收好东西以后，我在群里发了今天的照片。有一张拍到两个人低头看同一页歌词，另一张里，第一次拿话筒的朋友正在笑。第二天，群里有人问下一次的时间，也有人发来自己在家练的短录音。我把报名的位置留在消息最后，写了完整唱和只试几句两种选择，没想到最先回复的还是昨天出去休息的那位。',"After packing up I posted the photos to our group. One showed two people studying the same lyric sheet; another caught the first-time microphone holder laughing. The next day people asked about the next date and shared short practice recordings. At the end of the message I offered full sections or just a few lines. To my surprise, yesterday's friend who'd gone out for a rest replied first.")}},
3:{'-r':{
5:('我仍然觉得这首诗可以读出恋人分开的意思。朋友说那就把你喜欢的两句留下，我也选两句，我们交换着读。我写到“肯定是恋人”时，他指了指旁边的树和旧画，问这两样怎么放进去。我想了一会儿，把肯定改成也可能。轮到读他的笔记，我发现他说家里的那一段，也让我想起了很久没回去的院子。',"I still heard a story of separated lovers. My friend suggested we each keep two favourite lines and swap notes. When I wrote 'definitely lovers,' he pointed to the tree and old drawing: how did those fit? After thinking, I changed 'definitely' to 'possibly.' Reading his note about home then reminded me of a courtyard I hadn't visited for years.")}},
4:{'-r':{
0:('这段短剧从林安走进小厅开始。陈宇说“你总算来了”，林安没有回答问候，先问为什么大家全在这里。只看开头，我以为林安迟到，陈宇已经等得不耐烦。可第二句提到大门口等了半个小时，我又把字幕往回拖了一点。原来林安早就来了，只是一直站在另一扇门外，难怪进来就问大家怎么都换了地方。',"The short scene opens with Lin An entering the small hall. Chen Yu says, 'You're finally here,' but she asks why everyone is there. At first I thought she was late and he'd grown impatient. Then she mentions waiting at the main entrance for half an hour, so I dragged the subtitles back a little. She'd arrived earlier but stood outside another door, which explained her first question."),
5:('后面陈宇说，下次应该再等她回一句，不能发完就算了。林安也说应该早点借电话，别一直站在门外猜。我把这两句抄下来，又看了一遍前面的消息和通知：陈宇一直以为她已经知道，林安却以为大家忘了。朋友问哪一句可以改得早一点，我指了指“你没看到”，说换成先问她在哪里，也许那时就能找到人。',"Chen Yu says next time he should wait for her reply instead of assuming sending a message is enough. Lin An says she should have borrowed a phone earlier. I copied those lines and reread the message and notice: Chen thought she knew; she thought everyone had forgotten. Asked which earlier line I'd change, I pointed to 'Didn't you see it?' Asking where she was might have helped them find her sooner.")}}
}
apply(5,EDITS,'Moving and singing readings now recount observable actions, ordinary banter and follow-up plans. Removed repeated friendship guarantees, consent analysis and grand claims from the narrator. Lyric discussion remains literary interpretation; its two readings and uncertain addressee are preserved. Corrected Lin An pronoun continuity in the drama summary. Retained all tested times, two missed words, two short performances and original question/task IDs. Native flags: 搬家连水都不肯扔 banter, 抬桌子/收材料 collocations, 鼓掌 misunderstanding and lyric interpretations.',
glosses=[('未接电话','missed call'),('袖口','sleeve cuff'),('胶带','adhesive tape'),('剪刀','scissors'),('话筒','microphone'),('面包','bread'),('低头','lower one’s head'),('报名','sign up'),('录音','audio recording'),('搭','drape; put over'),('一堆','a pile; a lot'),('蹲','squat; crouch'),('卷起','roll up'),('凑','move close; come together'),('传统','tradition'),('凭','on the basis of; rely on'),('符合','conform to; be consistent with'),('抄','copy out')],publish='--publish' in sys.argv)

dependencies({'s5-u02':[('圈','circle; mark with a circle')],
              's5-u06':[('偶尔','occasionally')]},publish='--publish' in sys.argv)

# The rewritten paragraph no longer states the old lost-hour counterfactual.
# Test what this paragraph actually says, retaining the task ID and false key.
target=ROOT/('content/packs' if '--publish' in sys.argv else 'output/parity-editorial-drafts')/'s5-u01.json'
pack=json.loads(target.read_text('utf-8'))
task=next(t for t in pack['tasks'] if t['id']=='s5-u01-t03')
task.update(statement='They arrange all the books only by colour.',answer=False,
            why='The dictionary and frequently used books stay within reach; the others are sorted by title.')
question=pack['reading']['questions'][2]
question.update(q='What changes in the later dinner arrangement?',
                choices=['The friend states his availability and calls when delayed',
                         'The narrator waits outside without an update again',
                         'They return to the old address without checking'],
                answer='The friend states his availability and calls when delayed')
paired=pack['extraReadings'][-1]
before=paired['lines'][4]
after={**before,'zh':before['zh'].replace('他说需要三点开始','她说需要三点开始')}
after['en']=before['en'].replace('he asked me','she asked me').replace('He needed','She needed')
after['py']=py(after['zh'])
paired['lines'][4]=after
for gap in paired.get('cloze',{}).get('lines',[]):
    if gap['zh'].replace('【','').replace('】','')==before['zh']:
        gap['zh']=gap['zh'].replace('他说需要三点开始','她说需要三点开始')
        gap['py']=py(gap['zh'])
        gap['en']=after['en']
def update_pronoun_reference(value):
    if isinstance(value,dict):
        if value.get('zh')==before['zh']:value.update(after)
        for child in value.values():update_pronoun_reference(child)
    elif isinstance(value,list):
        for child in value:update_pronoun_reference(child)
update_pronoun_reference(pack['tasks'])
target.write_text(json.dumps(pack,ensure_ascii=False,indent=2)+'\n','utf-8')
