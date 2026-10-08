"""Independent retrieval examples for words no longer forced into the scene."""
import json
from pathlib import Path
from common import line

ROOT=Path(__file__).resolve().parents[2]
ROWS={
41:[
('这个节目每周六播出。','This programme airs every Saturday.'),
('请播放第二段，我想再听一次。',"Please play the second part. I'd like to hear it again."),
('记者采访了几位游客。','A reporter interviewed several visitors.'),
('这部连续剧我已经看到第十集了。',"I've reached episode ten of this drama."),
('我爷爷每天早上听收音机。','My grandpa listens to the radio every morning.'),
('她对影视工作很感兴趣。',"She's very interested in film and television work."),
('我错过了直播，晚上再看录像。','I missed the live broadcast; I’ll watch the recording tonight.'),
('这件事对他有重大影响。','This had a major effect on him.'),
('我觉得她是一位伟大的作家。',"I think she's a great writer."),
('把背坐直，别趴在桌子上。',"Sit with your back straight. Don't lean over the desk."),
('我的手表不准，快了五分钟。',"My watch isn't accurate. It's five minutes fast."),
('她把照片放在我眼前，让我看看。','She put the photo in front of me so I could look at it.'),
('眼前这座楼就是我们的学校。','The building in front of us is our school.'),
('我为朋友准备了一份礼物。','I prepared a gift for my friend.'),
('这张表只写姓名，没有写性别。','This form asks for your name but does not list gender.'),
],
42:[
('教练指导我们练这个动作。','The coach guides us through this movement.'),
('我把椅子的高度调整了一下。','I adjusted the height of the chair.'),
('这根线太短，够不到桌子。',"This cable is too short to reach the desk."),
('这个盒子是铁做的，很重。','This box is made of iron and is heavy.'),
('我不小心打破了一个杯子。','I accidentally broke a cup.'),
('这件事使我想起小时候。','This reminded me of my childhood.'),
('她的话使我很高兴。','What she said made me happy.'),
('我们慢慢形成了周末一起吃饭的习惯。','We gradually developed the habit of having dinner together at weekends.'),
('这块石头的形状像一颗心。','This stone is shaped like a heart.'),
('出门前，我把一切都准备好了。','I had everything ready before leaving.'),
('你应当早点告诉她。','You should have told her earlier.'),
('这本书是我专门给你买的。','I bought this book especially for you.'),
('今天的专题是城市里的树。',"Today's special topic is trees in the city."),
('我最近一直关注这位导演的新作品。',"I've been following this director's new work recently."),
('讲座结束以后，大家可以提问。','Everyone can ask questions after the talk.'),
('他第一个举手提问。','He was the first to raise his hand and ask a question.'),
],
43:[
('今天我代她来取材料。',"I'm collecting the materials on her behalf today."),
('再向前进一点，就能看到湖了。','Go forward a little more and you’ll see the lake.'),
('这个队很团结，大家总是互相帮助。','This team is close-knit; everyone helps one another.'),
('学校想推广这项活动，让更多人参加。','The school wants to promote the activity so more people can join.'),
('她在大学学习外交。','She studies diplomacy at university.'),
('博物馆里有古代的武器。','The museum has weapons from ancient times.'),
('厨房里有烟，谁把菜烧糊了？',"There's smoke in the kitchen. Who burnt the food?"),
('我们一直聊，直到最后一辆车来了才告别。','We talked until the last bus arrived, then said goodbye.'),
('音乐停止以后，她还在唱。','She was still singing after the music stopped.'),
('他随老师一起去参观。','He goes on the visit with his teacher.'),
('孩子把玩具放回盒子里。','The child puts the toys back in the box.'),
],
44:[
('这家店已经不存在了，原来的房子也拆了。',"This shop no longer exists, and the old building has been demolished."),
('这本教材一共有十个单元。','This textbook has ten units in total.'),
('她发动朋友一起打扫小区。','She rallied her friends to clean the neighbourhood together.'),
('他相信自己会有一个光明的未来。','He believes he will have a bright future.'),
('这把椅子很结实，坐两个人也没问题。','This chair is sturdy; it can even hold two people.'),
('她读了一篇关于联合国的报道。','She read a report about the United Nations.'),
('这座城市的气候很适合我。',"This city's climate suits me very well."),
('她的爷爷前年去世了。','Her grandfather passed away the year before last.'),
('这些变化影响着人类的生活。','These changes affect human life.'),
('我以为她不喜欢这首歌，实际上她每天都听。',"I thought she didn't like this song, but actually she listens to it every day."),
('他属牛，我属马。','His Chinese zodiac sign is the Ox; mine is the Horse.'),
('这辆自行车属于我姐姐。','This bicycle belongs to my sister.'),
('双方谈判了三天，终于签了合同。','The two sides negotiated for three days and finally signed the contract.'),
('见面时，他微笑着和我握手。','He smiled and shook my hand when we met.'),
('这个游戏可以四个人一起玩。','Four people can play this game together.'),
('我照着朋友给的地址找到了这家店。',"I found the shop using the address my friend gave me."),
('把这三种颜色组合起来，试试看。','Try combining these three colours.'),
],
}
for n,rows in ROWS.items():
    path=ROOT/f'content/packs/s3-u{n}.json'
    p=json.loads(path.read_text('utf-8'))
    t=next(t for t in p['extraReadings'] if t['id'].endswith('-word-notebook'))
    existing={l['zh'] for l in t['lines']}
    t['lines'].extend(line(zh,en) for zh,en in rows if zh not in existing)
    p['notes']='\n'.join(dict.fromkeys(p.get('notes','').splitlines()))
    for w,meaning in [('趴','lean forward over'),('感兴趣','be interested'),('颗','classifier for small rounded things'),('打扫','clean; tidy'),('烧糊','burn food'),('拆','demolish; take apart'),('签','sign'),('微笑','smile')]:
        if any(w in l['zh'] for l in t['lines']) and not any(g['hanzi']==w for g in t.get('glosses',[])):
            from common import py
            t.setdefault('glosses',[]).append(dict(hanzi=w,pinyin=py(w),meaning=meaning))
    path.write_text(json.dumps(p,ensure_ascii=False,indent=2)+'\n','utf-8')
    print(path.stem,len(rows),'new retrieval situations')
