"""Repair a travel plan using a notice, a deadline and a clear update."""
import sys
from advanced_core import write,rows,words,q,card,practice
V=words('''
航班|flight|chuyến bay|这个航班明天早上出发。|This flight departs tomorrow morning.|我的航班晚点了两个小时。|My flight was delayed by two hours.
航空|aviation; air transport|hàng không|这家航空公司有晚上的航班。|This airline has evening flights.|航空运输比以前方便多了。|Air transport is much more convenient than before.
长途|long-distance|đường dài|这次长途旅行，我们准备坐火车。|We plan to take the train on this long trip.|长途汽车站在城北。|The long-distance bus station is in the north of the city.
高铁|high-speed rail|tàu cao tốc|坐高铁到那里大约两小时。|It takes around two hours to get there by high-speed train.|高铁票已经买好了，不用再订。|The high-speed train tickets are already bought; no need to book again.
晚点|be delayed, of transport|trễ chuyến|这趟车晚点了半小时。|This service is half an hour late.|广播说列车晚点，时间还没确定。|The announcement says the train is delayed, with no time fixed yet.
预订|book in advance|đặt trước|我想预订周六晚上的房间。|I’d like to book a room for Saturday night.|预订成功以后，记得保存号码。|Keep the number once the booking is confirmed.
确认|confirm|xác nhận|你再确认一下车站名字。|Check the station name once more.|他已经确认周五能来。|He’s confirmed he can come on Friday.
途中|on the way; en route|trên đường|我们途中休息了十分钟。|We took a ten-minute break on the way.|途中下雨了，我们就放慢了速度。|It rained on the way, so we slowed down.
堵车|be held up in traffic|kẹt xe|路上堵车，我可能晚一点到。|I’m stuck in traffic and may arrive a little late.|这边早上容易堵车，最好早点走。|Traffic often backs up here in the morning; it’s best to leave early.
距离|distance|khoảng cách|两个车站之间的距离有多远？|How far apart are the two stations?|我想找距离学校近一点的房间。|I’d like a room closer to the school.
立即|immediately|ngay lập tức|看到通知以后，我立即给她打了电话。|I called her immediately after seeing the notice.|不用立即决定，今晚回复也可以。|No need to decide immediately; you can reply tonight.
期限|deadline; time limit|thời hạn|申请期限到周四晚上。|The application deadline is Thursday evening.|这个期限能不能延长两天？|Could this deadline be extended by two days?
延期|postpone; extend a deadline|hoãn; gia hạn|这次活动延期到下周了。|This event has been postponed until next week.|我想申请延期交材料。|I’d like to request more time to submit the documents.
取消|cancel|hủy|两点那趟车取消了。|The two o’clock service has been cancelled.|他取消了房间预订，准备当天回家。|He cancelled the room booking and plans to go home the same day.
转告|pass a message on|nhắn lại|请转告陈宇，我会晚半小时。|Please tell Chen Yu I’ll be half an hour late.|老师让我转告大家，明天换教室。|The teacher asked me to tell everyone we’re changing classrooms tomorrow.
出发|depart; set off|khởi hành|我们几点出发比较好？|What time should we set off?|出发之前，我又检查了一遍地址。|I checked the address once more before leaving.
''')
D=rows('''
你到哪儿了？我们已经到车站了。|Where are you? We’re already at the station.
还在公交车上，路上堵车。你先看看两点那趟还在不在。|Still on the bus, stuck in traffic. Check whether the two o’clock service is still running.
刚看到通知，两点那趟取消了。可以申请换到三点十分那趟。|I’ve just seen a notice: the two o’clock service is cancelled. We can apply to switch to the 3:10 service.
直接拿原来的票上车吗？|Can we board with the original tickets?
不行，通知写着要先去窗口，三点之前办好。|No. The notice says we need to go to the counter and finish before three.
那我先别着急下车。你能问问我没到，能不能先办你的？|Then I shouldn’t rush off the bus. Could you ask whether you can arrange your ticket before I arrive?
问过了，可以各自办。你到了直接找三号窗口。|I’ve asked; we can each do it separately. Go straight to counter three when you arrive.
好。我大约二点四十到，还有二十分钟。|Okay. I’ll arrive around 2:40, so I’ll have twenty minutes.
时间不多，到了先办票，再买水。|That’s not much time. Sort out the ticket before buying water.
知道了。你转告林安，我们到她那儿可能比原来晚一个小时。|Got it. Tell Lin An we may get to her place an hour later than planned.
我来说。她不用现在就出门等我们。|I’ll tell her. She doesn’t need to go out and wait now.
谢谢。早知道这样，我早上就多吃点了。|Thanks. If I’d known, I’d have eaten more this morning.
''')
R=rows('''
通知：原定今日十四点出发的长途汽车取消。已购票的乘客可以到三号窗口申请改乘十五点十分的汽车。办理期限为十五点前。原车票不能直接用于新班次。|Notice: the long-distance bus scheduled for 14:00 today is cancelled. Ticket holders may request transfer to the 15:10 service at counter three. This must be processed before 15:00. Original tickets cannot be used directly on the new service.
我看到通知的时候是二点二十，朋友还在去车站的公交车上。我先确认了窗口的位置，再问工作人员能不能各自办理。他说可以，不用等所有人到齐。|It was 2:20 when I saw the notice, and my friend was still on a city bus to the station. I found the counter and asked whether we could process our tickets separately. The staff member said yes; we didn’t need everyone present.
我办完以后给朋友发了两条消息。第一条是三号窗口的位置，第二条是期限。我没有只说“车改时间了”，因为他还需要知道先做什么。|After sorting mine out, I sent my friend two messages: the counter’s location and the deadline. I didn’t just say “the bus time changed,” because he also needed to know what to do first.
朋友二点四十到了。我在门口接他，一起去窗口。办好票还有一点时间，他买了水和面包，终于不再一直问车上有没有吃的。|My friend arrived at 2:40. I met him at the entrance and went with him to the counter. After the tickets were ready there was time for water and bread, and he finally stopped asking whether there was food on the bus.
我们又给林安确认了新的到达时间。她说会晚一点出门，还把饭馆的预订推迟了。一个人知道变化不够，等我们的人也要知道。|We confirmed our new arrival time with Lin An. She said she’d leave home later and postponed the restaurant booking. It wasn’t enough for us to know the change; the person waiting needed it too.
这次没有按原计划出发，不过该办的都办好了。我把通知保存下来，也把新车票和原来的放在不同地方，免得上车时拿错。|We didn’t depart as originally planned, but everything was arranged. I saved the notice and kept the new and original tickets apart so I wouldn’t take the wrong one when boarding.
''')
M=rows('''
你发消息说快到了，现在又说晚点？|You messaged that you were almost here, and now you’re delayed?
我说的是快到车站，不是快到你家。|I meant almost at the station, not almost at your place.
下次把地方一起说。我都穿好鞋了。|Name the place next time. I’ve already put my shoes on.
那先坐一会儿吧。我们三点十分才出发。|Then sit down for a while. We won’t depart until 3:10.
好，到了附近再给我电话，别只说快到了。|Okay. Call when you’re nearby rather than just saying almost there.
这次说清楚：快到你家楼下时，我打电话。|I’ll make it clear this time: I’ll call when we’re nearly downstairs at your place.
总算听懂了。你饿不饿？|Now I understand. Are you hungry?
已经买了面包，终于能等了。|I’ve bought bread, so I can finally manage the wait.
''')
G=[
card('除非…否则…','State what exception prevents an outcome','除非 supplies the exception or necessary condition; 否则 gives the outcome if it is not met. Compare the condition to the notice rather than inferring general transport rules.','除非先办好新票，否则不能直接上这趟车。|Unless the new ticket is processed first, you can’t board this service directly.\n除非大家都有空，否则我们不改到周一。|Unless everyone is free, we won’t move it to Monday.','除非先办好新票，否则就已经办好了。','除非先办好新票，否则不能直接上这趟车。','The 否则 clause must describe what happens without the exception.'),
card('万一…','Prepare for a less expected possibility','万一 presents a possible unwelcome contingency. It does not state that it will happen or give a numerical probability.','万一来不及，我就先给你电话。|If I happen to run out of time, I’ll call you first.\n带点水，万一路上买不到呢？|Bring some water in case we can’t buy any on the way.','万一路上买不到，所以一定买不到。','带点水，万一路上买不到呢？','A contingency is not a confirmed fact.'),
card('才 / 就 with time','Express later or earlier than expected','Place the time before 才/就 and the action after it. The choice conveys an expectation, so the clock time alone is insufficient.','我们三点十分才出发。|We won’t depart until 3:10.\n我两点就到车站了。|I was already at the station at two.','我们才三点十分出发了就。','我们三点十分才出发。','才 sits between the time phrase and the action in this sentence.'),
card('免得','Give an action intended to avoid a problem','The first clause supplies the precaution; 免得 names an unwanted possible result. It naturally appears in practical reminders.','把两张票分开放，免得拿错。|Keep the tickets apart so you don’t take the wrong one.\n先告诉她，免得她一直等。|Tell her first so she doesn’t keep waiting.','把两张票分开放，免得不会拿错。','把两张票分开放，免得拿错。','The problem being prevented is taking the wrong ticket, not avoiding the error.'),
]
spec=dict(title=('A late trip, a clear message','别只说快到了'),goals=['Extract an action and deadline from a fictional transport notice','Update a waiting friend with a specific location and time','Keep a fallback plan separate from a confirmed result'],vocabulary=V,grammar=G,dialogue=(D,[q('gist','What needs to be arranged?','Replacement tickets after a cancelled service','A new phone number for every traveller','An immediate airline booking'),q('detail','Which counter handles the switch?','Counter three','Counter fourteen','Every counter except three'),q('inference','Why inform Lin An?','So she can adjust when she leaves to meet them','To make her wait at the station from two','To cancel every future meeting')]),reading=(R,[q('gist','What does the notice require before the replacement trip?','Visit the specified counter before the deadline','Board using the original ticket without action','Wait for every member of the group to arrive'),q('detail','What is the processing deadline?','Before 15:00','At departure time 15:10','After 16:00'),q('inference','Why send two specific messages?','The friend needs both where to go and when to finish','The staff requires two phones','Only the new departure time matters')]),mediaTitle='Almost where?',media=(M,[q('detail','Which place did “almost there” originally mean?','The station','Lin An’s home','The restaurant kitchen'),q('inference','Why ask for a place with the update?','The vague phrase made the waiting person leave too early','The friend has forgotten how to call','The bus has already arrived at the house')]),glosses=[('改乘','switch to a different service'),('班次','scheduled service'),('窗口','service counter'),('乘客','passenger'),('办理','process; arrange formally'),('各自','each separately'),('到齐','all arrive'),('免得','so as to avoid'),('十四点','14:00'),('十五点','15:00')],place='At a fictional bus station',context='The two o’clock service is cancelled; a replacement requires counter processing before three.',turns=[('可以直接用原票吗？','Can I directly use the original ticket?','Explain the required action',['不行，要先到三号窗口办新票。']),('你说快到哪儿了？','Where are you nearly arriving?','Name the exact location',['我快到车站了，还没到你家附近。']),('要我现在出门吗？','Should I leave now?','Update the waiting person',['先不用，我们三点十分才出发。'])],usage=[('Provide both place and next step','到了先找三号窗口，三点前要办好。','Find counter three when you arrive; it must be done before three.','The message distinguishes the processing deadline from departure time.'),('Correct a vague update','我说的是快到车站，还没到你家。','I meant nearly at the station, not at your home yet.','Name the location that was missing from the earlier message.')],tasks=practice([(D[4][0],D[4][1],'The original tickets can be used directly without visiting a counter.',False,'The notice requires processing at the counter.'),(R[3][0],R[3][1],'The friend arrives at 2:40.',True,'That exact time is stated.')],[('我三点十分去窗口行吗？','Can I go to the counter at 3:10?',['不行，通知说三点前要办好。','行，通知只要求三点十分出发，没有办理期限。','只要拿原票就不用办理。'],0,'The counter deadline is earlier than departure.'),('我还在去车站的路上，没上长途车。别人问快到了吗，怎么说？','I am still on the way to the station, not on the coach. How should I answer about nearly arriving?',['我快到车站，还没上长途车。','我已经坐在长途车上了。','我已经到了你家门口。'],0,'The response supplies the exact travel stage.')],[('请再确认一下车站名字。','Please check the station name once more.','确认'),('把两张票分开放，免得拿错。','Keep the two tickets apart to avoid taking the wrong one.','免得')],[[(V[i][3],V[i][4]) for i in [0,4,7]],[(V[i][5],V[i][6]) for i in [8,11,14]]]),review='Native review: informal arrival updates, counter wording and long-distance travel terms. All processing rules are specific to this original fictional notice, not universal carrier policies. Timeline checked: arrival 2:40, processing before 3:00, departure 3:10. A tentative one-hour-later arrival is confirmed later without inventing its clock time.')
spec['glosses'].append(('列车','train'))
write(4,9,spec,publish='--publish' in sys.argv)
