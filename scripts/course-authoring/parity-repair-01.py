"""Authored naturalness corrections; keep IDs and assessment anchors stable."""
import json
from pathlib import Path
from common import line, py

ROOT = Path(__file__).resolve().parents[2]
DATA = {
41: {
 'dialogue': [
 ('你笑什么啊？我还没讲完呢。', "What are you laughing at? I haven't finished yet."),
 ('我不是笑你。我把咖啡倒进你的杯子里了。', "I'm not laughing at you. I poured my coffee into your cup."),
 ('怪不得这么甜！你到底放了多少糖？', "No wonder it's so sweet! How much sugar did you put in?"),
 ('别问了。我再给你买一杯，好不好？', "Don't ask. I'll get you another cup, okay?"),
 ('行。对了，明天的连续剧你还看吗？', "Okay. By the way, are you still watching that drama tomorrow?"),
 ('看啊。导演的采访也挺好笑的，我发给你。', "Of course. The director's interview is pretty funny too. I'll send it to you."),
 ],
 'dq': [('Why is the drink surprisingly sweet?', ['The friend put sugar in the coffee', 'The café changed its opening time', 'The drama starts tomorrow'], 0), ('What does the friend offer to do?', ['Buy another drink', 'Cancel drama night', 'Finish the story alone'], 0), ('What will the friend send?', ['An interview with the director', 'A train ticket', 'The café menu'], 0)],
 'reading': [
 ('周六，我去剧场看朋友的话剧。她热爱表演，练了三个月才第一次上台。', "On Saturday I went to the theatre to see my friend's play. She loves acting and practised for three months before her first performance."),
 ('我刚到门口，她就出来迎接我，把我带到前面的位置。现场比我想象的热闹。', "As soon as I reached the entrance, she came out to greet me and took me to a seat near the front. It was livelier than I'd expected."),
 ('故事发生在一座古城。一个好奇的孩子走到海边，听见远处传来的海浪声。', "The story takes place in an old city. A curious child walks to the shore and hears waves in the distance."),
 ('灯一暗，孩子吓了一跳。旁边的朋友小声说：怕什么啊，我陪你。', "When the lights dim, the child startles. A friend whispers, 'What are you afraid of? I'm here with you.'"),
 ('演出结束，我想跟她聊聊最后一场。她说先喝杯咖啡，慢慢聊。', "After the performance I wanted to talk to her about the final scene. She suggested coffee first, so we could take our time."),
 ],
 'rq': [('Where does the narrator go on Saturday?', ['A theatre', 'A train station', 'A school office'], 0), ('How long did the friend practise?', ['Three months', 'Three days', 'Three years'], 0), ('Why suggest coffee after the performance?', ['To have time to talk about the play', 'To rehearse the whole play again', 'To catch the last train'], 0)],
},
42: {
 'dialogue': [
 ('把声音调低一点，隔壁已经睡了。', "Turn the volume down a little. Our neighbour's already asleep."),
 ('这么低，你听得清吗？', "Can you hear it at this volume?"),
 ('听得清，可刚才那句话我没听懂。她到底在等谁？', "I can hear it, but I didn't understand that line. Who is she waiting for?"),
 ('她姐姐。前面不是说姐姐的车坏了吗？', "Her sister. Didn't they say earlier that her sister's car broke down?"),
 ('哦，我刚才去拿水了，漏了那一句。倒回去看看。', "Oh, I went to get water and missed that line. Let's go back."),
 ('等一下，我先把字幕切换成大一点的字。这样看得清楚。', "One second. I'll make the subtitles bigger first. They're easier to read that way."),
 ],
 'dq': [('Why turn down the volume?', ['The neighbour is asleep', 'The television is broken', 'The episode has ended'], 0), ('Who is the character waiting for?', ['Her sister', 'Her teacher', 'Her neighbour'], 0), ('Why did one friend miss the earlier line?', ['They went to get water', 'They had already fallen asleep', 'The subtitles were in another language'], 0)],
 'reading': [
 ('昨晚我和朋友看一部连续剧。她看过前两集，我是第一次看。', "Last night I watched a drama with a friend. She'd seen the first two episodes; it was my first time."),
 ('开头，一个人抓住门口的牌子，把它转过来，露出背面的地址。', "At the start someone grabs the sign by the door and turns it around, revealing an address on the back."),
 ('我没看清那个地址，就问朋友：这是她要去的地方吗？朋友让我先看下去。', "I couldn't make out the address, so I asked whether that was where she was going. My friend told me to keep watching."),
 ('过了一会儿，老师指出信上的日期错了。她马上打电话，叫姐姐别出发。', "A little later a teacher points out that the date on the letter is wrong. She immediately calls her sister and tells her not to leave."),
 ('这时我才明白，旧地址造成了误会。我倒回开头再看一次，终于把两件事连起来了。', "Then I understood: the old address had caused the misunderstanding. I went back to the start and finally connected the two events."),
 ],
 'rq': [('Who has seen the first two episodes?', ['The narrator’s friend', 'The narrator', 'The sister in the drama'], 0), ('What does the teacher notice?', ['The date on the letter is wrong', 'The sign is missing', 'The telephone is broken'], 0), ('Why does the narrator watch the opening again?', ['To connect it with the later scene', 'To hear a different song', 'To choose a new programme'], 0)],
},
43: {
 'dialogue': [
 ('你把这两段合起来试试，别一到最后就停。', "Try joining these two parts. Don't stop as soon as you reach the end."),
 ('我一快就乱，字都唱不清楚了。', "When I speed up I get muddled. You can't make out the words."),
 ('那就慢一点。比起快，我更想听清你在唱什么。', "Then slow down. I'd rather understand what you're singing than hear you go fast."),
 ('这首歌明明很安静，我怎么唱得像在吵架？', "This song is so quiet. Why do I sound like I'm arguing?"),
 ('你太用力了。先读一遍，再跟着节拍唱。', "You're pushing too hard. Read it once first, then sing with the beat."),
 ('好。你别笑啊，我再来一次。', "Okay. Don't laugh! I'll give it another try."),
 ],
 'dq': [('What happens when the singer speeds up?', ['The words become unclear', 'The microphone turns off', 'The song ends early'], 0), ('What does the friend suggest doing before singing?', ['Reading the words once', 'Changing every word', 'Buying another microphone'], 0), ('How does the singer feel about trying again?', ['Willing, but a little embarrassed', 'Certain the friend has left', 'Determined to stop permanently'], 0)],
 'reading': [
 ('我们语言社团周五晚上练一首自己写的歌。谁也不是专业歌手，唱错了就再来。', "Our language club practises a song we wrote ourselves on Friday evenings. None of us is a professional singer; when we make a mistake, we try again."),
 ('我管材料，把歌词按顺序排好。朋友拿着吉他，用简单的节拍带动大家。', "I'm in charge of the materials and put the lyrics in order. A friend plays guitar and gets everyone going with a simple beat."),
 ('第一段讲一个人划船回家，第二段写他追着岸边的灯光。最后，他终于看见家门。', "The first verse is about someone rowing home; the second follows him chasing the lights on shore. At the end he finally sees his front door."),
 ('唱到这里，我总想唱快一点。朋友说别急，这个人走了很远，现在才到家。', "At this point I always want to sing faster. My friend says not to rush: he's travelled a long way and has only just got home."),
 ('我重新读了一遍，慢慢唱。字清楚了，大家也更容易跟上。', "I read it again and sang slowly. The words were clearer, and everyone found it easier to join in."),
 ],
 'rq': [('Who wrote the song?', ['The club members', 'A professional singer', 'The narrator’s teacher'], 0), ('What does the person in the song do?', ['Row home', 'Wait at a railway station', 'Buy a new guitar'], 0), ('Why slow down near the end?', ['The words and homecoming moment need time', 'Everyone has forgotten the first verse', 'The room is too small'], 0)],
},
44: {
 'dialogue': [
 ('明天去新开的店吧，听说那里的面不错。', "Let's go to the new place tomorrow. I've heard the noodles are good."),
 ('我看门口的牌子写着周五才开业，明天不是周四吗？', "The sign says it opens on Friday. Isn't tomorrow Thursday?"),
 ('那块旧牌子还没换。老板刚在群里发了新通知。', "They haven't replaced that old sign yet. The owner just posted a new notice in the group chat."),
 ('你把通知发给我。几点去？', "Send me the notice. What time should we go?"),
 ('六点半。你把小周也叫上，我来订位子。', "Six thirty. Ask Xiaozhou too. I'll book a table."),
 ('行，我问问她。她要是加班，咱们就先吃。', "Sure, I'll ask her. If she's working late, we'll eat first."),
 ],
 'dq': [('Why is the old sign misleading?', ['The opening date has changed', 'The shop has permanently closed', 'The group has chosen another city'], 0), ('What time do they plan to go?', ['Six thirty', 'Five thirty', 'Seven thirty'], 0), ('What will they do if Xiaozhou works late?', ['Eat first', 'Cancel the booking immediately', 'Move the meal to Friday'], 0)],
 'reading': [
 ('小周在群里说她今天要加班，可能赶不上晚饭。我就把订位时间改到七点。', "Xiaozhou said in the group chat that she had to work late and might miss dinner, so I moved the booking to seven."),
 ('她看见消息以后给我打电话，说别等她，大家先吃，晚上她再来找我们。', "After seeing the message she called me and said not to wait: everyone should eat first, and she'd join us later."),
 ('店里的旧牌子已经被老板换了。新牌子上写着开业时间，门口还挂着几张照片。', "The owner had replaced the old sign. The new one showed the opening time, and a few photographs hung by the door."),
 ('我们把包放在椅子旁边，点了三碗面。朋友说这家店让他想起小时候的学校门口。', "We put our bags beside the chairs and ordered three bowls of noodles. A friend said the place reminded him of the entrance to his school when he was young."),
 ('八点多，小周终于到了。我们又点了一碗，听她讲今天发生的事，一直聊到店快关门。', "Xiaozhou finally arrived after eight. We ordered another bowl and listened to her day, chatting until the shop was almost closing."),
 ],
 'rq': [('Why did the narrator move the booking?', ['Xiaozhou might work late', 'The owner lost the sign', 'Everyone disliked noodles'], 0), ('Who replaced the old sign?', ['The owner', 'Xiaozhou', 'The narrator'], 0), ('What suggests the friends enjoyed the evening?', ['They talked until almost closing time', 'They left without ordering', 'Nobody spoke after Xiaozhou arrived'], 0)],
},
}

def questions(rows):
    return [dict(type='inference' if i == 2 else 'detail', q=q, choices=choices, answer=choices[answer]) for i,(q,choices,answer) in enumerate(rows)]

for number, spec in DATA.items():
    path = ROOT / f'content/packs/s3-u{number}.json'
    pack = json.loads(path.read_text('utf-8'))
    for section, qkey in [('dialogue','dq'), ('reading','rq')]:
        passage = pack[section]
        passage['lines'] = [dict(line(zh,en), **({'speaker': 'a' if i % 2 == 0 else 'b'} if section=='dialogue' else {})) for i,(zh,en) in enumerate(spec[section])]
        passage['questions'] = questions(spec[qkey])
        glosses = {41: [('吓了一跳', 'to get a fright')], 42: [('隔壁', 'next door; the neighbour'), ('露出', 'to reveal; to show')], 43: [('吉他','guitar'), ('岸边','the shore')], 44: []}
        for hanzi, meaning in glosses[number]:
            if any(hanzi in row['zh'] for row in passage['lines']) and not any(g['hanzi']==hanzi for g in passage.get('glosses', [])):
                passage.setdefault('glosses', []).append(dict(hanzi=hanzi, pinyin=py(hanzi), meaning=meaning))
        if section == 'reading':
            passage['purpose'] = 'Follow what happened and explain the people’s choices from the text.'
        else:
            passage['purpose'] = 'Listen for the problem, the proposed response and the next action.'
        # Gap fills must be copied from this revised text, never stale lines.
        if 'cloze' in passage:
            selected=[]
            for row in passage['lines']:
                word = next((v['hanzi'] for v in pack['vocabulary'] if v['hanzi'] in row['zh'] and v['hanzi'] not in [w for _,w in selected]),None)
                if word: selected.append((row,word))
                if len(selected)==3: break
            if not selected: selected=[(passage['lines'][0],'我')]
            passage['cloze']={'lines':[{**row,'zh':row['zh'].replace(word,f'【{word}】',1)} for row,word in selected], 'bank':[word for _,word in selected]+['学校','明天']}
    note = '2026-10-07 editorial correction: dialogue and core reading rewritten as coherent everyday interaction; no recycled-word quota, app policy or safety caveats in character speech. IDs preserved. AI editorial review; native review remains outstanding.'
    pack['notes'] = '\n'.join(dict.fromkeys([*pack.get('notes','').splitlines(),note]))
    path.write_text(json.dumps(pack,ensure_ascii=False,indent=2)+'\n','utf-8')
