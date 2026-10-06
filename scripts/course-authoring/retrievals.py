"""Concrete later retrieval tasks, using existing screened course sentences."""
import json
from pathlib import Path
from common import py
ROOT = Path(__file__).resolve().parents[2]

RETRIEVALS = {
13:('一02',[('我会说英语。','I can speak English.'),('今天我不能去上课。','I cannot attend class today.'),('我能教你汉字。','I can teach you Chinese characters.')]),
14:('一15',[('从这儿到机场远吗？','Is the airport far from here?'),('从机场到我家，你坐地铁吧。','Take the subway from the airport to my home.'),('从大学站到我家不远，走路五分钟。','My home is not far from University Station: five minutes on foot.')]),
15:('一21',[('我昨天看了两个电影。','I watched two films yesterday.'),('我昨天没出去。','I did not go out yesterday.'),('昨天下雨了。','It rained yesterday.')]),
16:('一34',[('请坐！','Please sit down.'),('请进！请坐！','Please come in and sit down.'),('请坐，喝点儿茶吧。','Please sit down and have some tea.')]),
17:('一40',[('我病了。','I have become ill.'),('我好点儿了。','I am a little better now.'),('我感冒了。','I have caught a cold.')]),
18:('一02 / 一41',[('我会说英语。','I can speak English.'),('我在家看了两个电影。','I watched two films at home.'),('我昨天没出去。','I did not go out yesterday.')]),
19:('一15 / 一43',[('从这儿到机场远吗？','Is the airport far from here?'),('这件衣服一百二十块。','This item of clothing costs one hundred and twenty yuan.'),('水三块。','Water costs three yuan.')]),
20:('一21 / 一47',[('我昨天看了两个电影。','I watched two films yesterday.'),('中文字幕还是英语字幕？','Chinese subtitles or English subtitles?'),('周末你做了什么？','What did you do at the weekend?')]),
21:('一34 / 二26 / 一20 / 一26',[('请坐，喝点儿茶吧。','Please sit down and have some tea.'),('给我你的微信吧。','Give me your WeChat contact.'),('我找钱包，你帮我。','I will look for my wallet; please help me.')]),
22:('一40 / 二72 / 一07 / 一23',[('我好点儿了。','I am a little better now.'),('这是我第一次来中国。','This is my first visit to China.'),('两杯水和半杯奶。','Two glasses of water and half a cup of milk.')]),
23:('一41 / 一08 / 一37 / 一12 / 一28',[('我在家看了两个电影。','I watched two films at home.'),('一家商店，两间房，三口人。','One shop, two rooms, three family members.'),('我常在家读书，她常常上午学习。','I often read at home; she often studies in the morning.')]),
24:('一43 / 一20 / 一26 / 一14 / 一48',[('这件衣服一百二十块。','This item of clothing costs one hundred and twenty yuan.'),('这是我的课本，那是别人的。','This is my textbook; that one belongs to someone else.'),('星期日有没有课？','Is there class on Sunday?')]),
25:('一47 / 一16 / 一29 / 一44',[('中文字幕还是英语字幕？','Chinese subtitles or English subtitles?'),('我在车站旁边等你。','I will wait beside the station.'),('我们八点零五分见面。','Let us meet at eight oh five.')]),
26:('二26 / 一12 / 一28 / 一17 / 一19',[('给我你的微信吧。','Give me your WeChat contact.'),('先吃晚饭，再去上课。','Eat dinner first, then go to class.'),('爷爷和奶奶都来。','Grandfather and grandmother are both coming.')]),
27:('二72 / 一14 / 一48 / 一09 / 一30 / 一35',[('这是我第一次来中国。','This is my first visit to China.'),('星期日没有课，别去学校。','There is no class on Sunday; do not go to school.'),('真好看！','That really looks good!')]),
28:('一16 / 一29 / 一44 / 一18 / 一38',[('我买车票，你等朋友。','I buy tickets; you wait for our friend.'),('星期日两点半上车。','Board on Sunday at half past two.'),('商场没有图书馆安静。','The shopping centre is not as quiet as the library.')]),
29:('一12 / 一28 / 一17 / 一19 / 一10 / 一39',[('我常在家读书，她常常上午学习。','I often read at home; she often studies in the morning.'),('爷爷和奶奶都来。','Grandfather and grandmother are both coming.'),('我们一边走路，一边聊天。','We walk and chat at the same time.')]),
30:('一14 / 一48 / 一09 / 一30 / 一35 / 一22 / 一33 / 一45',[('星期日有没有课？','Is there class on Sunday?'),('真好看！','That really looks good!'),('我可以进去吗？','May I go in?')]),
}

def apply(first, last):
    scripts=json.loads((ROOT/'content/audio-scripts.json').read_text('utf-8'))
    by_text={e['text']:e for e in scripts}
    for n in range(first,last+1):
        if n not in RETRIEVALS:continue
        code, pairs=RETRIEVALS[n]
        uid=f's1-u{n:02}'
        path=ROOT/'content/packs'/f'{uid}.json'
        p=json.loads(path.read_text('utf-8'))
        task_pairs=[]
        for zh,en in pairs:
            source=by_text.get(zh,{})
            task_pairs.append(dict(left=en,right=dict(zh=zh,py=source.get('pinyin') or py(zh),en=en)))
        task=dict(type='match',id=f'{uid}-t9',phrase=p['vocabulary'][0]['id'],
                  title='Bring back earlier language',pairs=task_pairs)
        p['tasks']=[t for t in p['tasks'] if t['id']!=task['id']]+[task]
        p['notes']=p['notes'].split(' Planned retrieval ')[0]+f' Planned retrieval {code}: '+', '.join(zh for zh,_ in pairs)+'.'
        path.write_text(json.dumps(p,ensure_ascii=False,indent=2)+'\n','utf-8')

if __name__=='__main__':apply(13,16)
