"""Editorial source: updates, message sequences, clarification and friendly teasing."""
from common import *
character_groups.update({
's2-u13':[('忽','suddenly; neglect'),('急','urgent; anxious'),('交','to hand over; exchange'),('司','to manage; in 司机'),('辆','vehicle classifier'),('近','near'),('离','to leave; distance from'),('已','already'),('定','to decide; fixed')],
's2-u14':[('经','to pass through; in 经常'),('又','again; also'),('然','in 然后: then'),('通','to connect; pass through'),('随','to follow; according to'),('件','item classifier'),('业','work; study'),('完','to finish'),('借','to borrow; lend')],
's2-u15':[('确','certain; accurate'),('直','straight; direct'),('论','to discuss'),('思','to think'),('理','reason; to put in order'),('态','state; attitude'),('讨','to discuss; seek'),('提','to raise; mention'),('相','mutual; alike')],
's2-u16':[('故','reason; in 故意'),('喊','to shout'),('睛','eye, in 眼睛'),('脸','face'),('嘴','mouth'),('头','head'),('哭','to cry'),('眼','eye'),('怕','to fear')],
})
unit_glosses.update({
's2-u13':{'迟到':'to arrive late','路口':'road intersection','预计':'to estimate','堵车':'traffic jam','改道':'to change route','安全':'safe; safety','准确':'accurate','站台':'platform; stop waiting area','发车':'departure of a vehicle'},
's2-u14':{'地址':'address','更新':'to update','信号':'signal','顺序':'sequence','确认':'to confirm','重发':'to resend','借书':'to borrow books','作业':'homework','入口':'entrance'},
's2-u15':{'态度':'attitude','语气':'tone of delivery','误会':'misunderstanding','理由':'reason','重点':'main point','核对':'to check against','版本':'version','同意':'to agree'},
's2-u16':{'玩笑':'joke; joking','误会':'misunderstanding','道歉':'to apologize','表情':'facial expression','生气':'to be angry','边界':'boundary','取笑':'to make fun of','尴尬':'awkward'},
})
dictionary.update({'一定':'yí dìng','司机':'sī jī','公共汽车':'gōng gòng qì chē','公交车':'gōng jiāo chē','车辆':'chē liàng','一直':'yì zhí','手表':'shǒu biǎo','信号':'xìn hào','快点儿':'kuài diǎnr','离开':'lí kāi','停车场':'tíng chē chǎng'})

u='s2-u13'
write(u,'我还在路上',['Send a useful delay update without promising an unknown arrival','Distinguish already, still and suddenly','Recognize early or late judgments from context'],[
('忽然','suddenly','đột nhiên','adverb','车忽然停了，我还不知道原因。','The vehicle suddenly stopped; I do not yet know why.'),
('一直','all along; continuously','suốt; liên tục','adverb','我一直在站台等，没有离开。','I have been waiting at the stop all along and have not left.'),
('已经','already','đã','adverb','朋友已经到了，我还在路上。','My friend has already arrived; I am still on the way.'),
('急','anxious; urgent','lo; gấp','adjective','我有点儿急，但先把消息说清楚。','I am a little anxious, but I first explain the message clearly.'),
('交通','traffic; transport','giao thông','noun','今天交通不太顺利，可能晚到。','Traffic is not going smoothly today; I may arrive late.'),
('公共汽车','bus','xe buýt','noun','我坐公共汽车，不是出租车。','I take a bus, not a taxi.'),
('公交车','bus; public bus','xe buýt','noun','这辆公交车还没到站。','This bus has not reached the stop yet.'),
('司机','driver','tài xế','noun','司机说前面的路暂时不能走。','The driver says the road ahead cannot be used for now.'),
('车辆','vehicles','xe cộ','noun','路口的车辆很多，先别猜到达时间。','There are many vehicles at the intersection; do not guess the arrival time first.'),
('出发','to set off','khởi hành','verb','我六点出发，七点还没到。','I set off at six and have not arrived by seven.'),
('等到','until; wait until','đợi đến; đến khi','preposition','等到车停好，我再下来。','I will get off after the vehicle has stopped properly.'),
('经过','to pass through; pass by','đi qua','verb','车经过学校，但没有在那里停。','The vehicle passes the school but does not stop there.'),
('离','away from; distance from','cách; rời','preposition','这个站离学校很近。','This stop is very near the school.'),
('离开','to leave','rời khỏi','verb','我还没有离开站台。','I have not left the stop yet.'),
('路边','roadside','bên đường','noun','不要站在路边等车，先找站台。','Do not wait by the roadside; find the stop first.'),
('停车','to park; stop a vehicle','đỗ xe; dừng xe','verb','这里不能停车，请看指示。','Parking is not allowed here; check the signs.'),
('停车场','car park','bãi đỗ xe','noun','停车场不是公交站。','The car park is not the bus stop.'),
('近','near','gần','adjective','从站台到学校很近，但还要走路。','The school is near the stop, but walking is still needed.'),
('手表','wristwatch','đồng hồ đeo tay','noun','我看手表，已经七点了。','I check my watch; it is already seven.'),
('信号','signal','tín hiệu','noun','手机信号不好，消息可能没发出。','The phone signal is poor; the message may not have gone through.'),
('快点儿','a little faster; hurry up','nhanh lên một chút','adverb','朋友说快点儿，我还是先看安全。','My friend says to hurry, but I still prioritize safety.'),
('一定','certainly; definitely','nhất định; chắc chắn','adverb','时间一确认，我一定发消息。','Once the time is confirmed, I will definitely send a message.')],
[grammar(u,'二15','刚 / 刚刚 / 还 / 忽然 / 一直 / 已经','Locate a change without pretending the journey is finished',
'刚/刚刚 place an event in the recent past; 已经 says it has happened by now. 还 can say a state continues: 还在路上. 一直 describes continuation across the stated period, not literally every moment forever. 忽然 describes a sudden change. Compare 我刚出发、我已经出发 and 我还没到: departure is not arrival. Use a location update instead of inventing an arrival time.',[
('我刚出发，朋友刚刚到。','I have just set off; my friend has just arrived.'),('朋友已经到了，我还在路上。','My friend has already arrived; I am still on the way.'),('我一直在站台等，车忽然停了。','I have been waiting at the stop all along; the vehicle suddenly stopped.')],
('我已经出发了，所以我已经到了。','我已经出发了，但还没到。','Having departed does not entail having arrived.')),
grammar(u,'二20','才 / 都 / 就 / 正好','Read the speaker’s expectation, not just the clock',
'才六点四十 can mean only six forty, earlier than expected; 七点才到 means not arriving until seven, later than expected. 都七点了 expresses that seven is already late in this context. 就三个人 limits the group to only three people; 正好三个人 says exactly the needed three. These words express an expectation or fit. They do not change the factual time or headcount. Context decides whether a time feels early or late.',[
('才六点四十，不用急。','It is only six forty; no need to hurry.'),('都七点了，他七点才到，大家已经等了一会儿。','It is already seven; he did not arrive until seven and everyone has already waited a while.'),('今天就三个人，三个座位正好。','Today there are only three people; three seats are exactly enough.')],
('正好三个人，所以一定有四个人。','正好三个人，没有第四个人。','正好三个人 gives an exact fit of three, not a fourth person.')),
grammar(u,'二80','该 … 了','Say that the time for an action has come',
'该出发了 says it is time to depart now; 该走了 can gently close a visit. It does not say departure already happened. Compare 我们已经出发了. A time-related 该…了 is different from a general obligation 你应该看通知. Give the relevant plan when asking someone to act; urgency is not permission to ignore safety.',[
('集合时间到了，我们该出发了。','The meeting time has come; it is time for us to set off.'),('天晚了，该回家了。','It is late; it is time to go home.'),('该发消息了，还没有发出去。','It is time to send the message; it has not gone through yet.')],
('我们该出发了，就是我们已经到了。','我们该出发了，但还没有出发。','Time to depart is not evidence that the journey is completed.'))],
text(u,'d','A delay update','Find the actual location and the next agreed update.',[
('都七点了，你到了吗？','It is already seven; have you arrived?'),('还没到。我六点出发，坐公共汽车。现在还在车上。','Not yet. I set off at six by bus and am still on the vehicle now.'),
('快点儿，我们已经等了一会儿。','Hurry a little; we have already waited a while.'),('我有点儿急，但不能让司机开快。今天交通不顺利。','I am anxious, but I cannot ask the driver to speed up. Traffic is not going smoothly today.'),
('怎么了？','What happened?'),('车忽然停了。司机说路口的车辆很多，这辆公交车可能要改道。','It suddenly stopped. The driver says there are many vehicles at the intersection and this bus may need a different route.'),
('到学校的站了吗？','Have you reached the school stop?'),('还没有。刚经过学校，没停车。车还没到那个站。','Not yet. We just passed the school without stopping. The vehicle has not reached that stop.'),
('停车场那边近吗？你在那里下吧。','Is the car park nearby? Get off there.'),('停车场不是站台，我先等到车停好再下。离学校近，也不能在路边下。','The car park is not the stop; I will wait until the vehicle stops properly before getting off. Being near the school does not mean I can get off at the roadside.'),
('那该什么时候再问你？','Then when should I ask again?'),('手机信号不好。我看手表了，但到达时间还没确认。时间一确认，我一定发消息。','The phone signal is poor. I checked my watch, but the arrival time is unconfirmed. Once it is confirmed, I will definitely message.')],
[('mainidea','What does the traveller provide?',['A location update and a promise to message once confirmed','A confirmed arrival at seven','Permission to speed up'],0),('detail','Is passing the school the same as reaching its stop?',['No, the bus passed without stopping','Yes, the traveller is already inside the school','Yes, the bus is at the car park'],0),('inference','Can the friend infer an exact arrival time?',['No, it remains unconfirmed','Yes, it is definitely seven','Yes, it is definitely six'],0)],drama=True),
text(u,'r','Still on the bus','Read to distinguish departure, passing a place and actual arrival.',[
('我六点出发，七点还在公共汽车上。朋友已经到了，我还没到。','I set off at six and am still on the bus at seven. My friend has already arrived; I have not.'),('刚才车忽然停了。司机说交通不顺利，路口的车辆很多。','The vehicle suddenly stopped just now. The driver says traffic is not going smoothly and there are many vehicles at the intersection.'),
('这辆公交车刚经过学校，没有在那里停车。经过学校不是到站，更不是进学校。','This bus just passed the school without stopping there. Passing the school is not reaching the stop, much less entering the school.'),('我有点儿急。朋友说快点儿，我还是先看安全，不让司机开快。','I am anxious. My friend says to hurry, but I still prioritize safety and do not ask the driver to speed up.'),
('停车场离学校近，但停车场不是公交站。我等到车停好才下，不在路边下。','The car park is near the school but is not the bus stop. I wait until the vehicle stops properly to get off, not by the roadside.'),('我一直没有离开车。站台的位置还要看清楚，不能只看距离近。','I have not left the vehicle all this time. I still need to check where the stop is; a short distance is not enough.'),
('看手表，已经七点了。手机信号不好，第一条消息可能没有发出去。','My watch says it is already seven. The phone signal is poor, so the first message may not have gone through.'),('到达时间还没确认，我不说一定七点到。时间一确认，就发消息。','The arrival time is unconfirmed, so I do not claim I will definitely arrive at seven. I will send a message once it is confirmed.')],
[('mainidea','Which facts are kept distinct?',['Departure, location, arrival and an uncertain estimate','The identities of two drivers','Only the colours of vehicles'],0),('detail','Where is the traveller at seven?',['Still on the bus','Already inside the school','At home'],0),('inference','Does sending the first message prove it was delivered?',['No, poor signal leaves delivery uncertain','Yes, every phone always sends instantly','Yes, the traveller has already arrived'],0)],[(0,'七点'),(7,'确认')]),
text(u,'media','Not there yet','Read an original scene about an impatient message.',[
('你说刚经过学校，我以为你已经到了。','You said you had just passed the school; I thought you had arrived.'),('我还在车上。经过不是停车，停车也不是进学校。','I am still on the vehicle. Passing is not stopping, and stopping is not entering the school.'),
('都七点了，我才问清楚。','It is already seven, and only now am I asking clearly.'),('急也要说准确。你先别在路边等我。','Even when anxious, be accurate. Do not wait for me by the roadside.'),
('那我该发什么消息？','Then what message should I send?'),('发你在哪里，我确认以后再回。','Send where you are; I will reply after I have confirmation.')],
[('inference','What caused the misunderstanding?',['Treating passing the school as arrival','Knowing the exact arrival time','Checking the actual location'],0)],drama=True),
dict(tf=[('已经','朋友已经到了，我还在车上。','My friend has already arrived; I am still on the vehicle.','Both people have arrived.',False,'Only the friend has arrived.'),('经过','车经过学校，没有在那里停车。','The vehicle passes the school without stopping.','The vehicle did not stop at the school.',True,'没有停车 explicitly denies stopping.')],
reply=[('信号','第一条消息发出去了吗？','Did the first message go through?',['信号不好，还不确定。','我已经进学校了。','停车场不是公交站。'],0,'Acknowledge the uncertain delivery.'),('一定','你一定七点到吗？','Will you definitely arrive at seven?',['时间还没确认，我确认后再发消息。','已经七点了，所以一定到了。','手表是我的。'],0,'Do not turn the current time into a confirmed arrival.')],
fill=[('已经','朋友已经到了。','My friend has already arrived.'),('离开','我还没有离开站台。','I have not left the stop yet.')],
match=[('出发',[('我刚出发。','I have just set off.'),('我已经到了。','I have already arrived.'),('我还在路上。','I am still on the way.')]),('近',[('离学校很近。','Very near the school.'),('经过学校，没停车。','Passed the school without stopping.'),('该出发了。','It is time to set off.')])]),
[('A useful delay update','我还在车上，时间确认后再告诉你。','I am still on the vehicle; I will tell you after the time is confirmed.','Location and next update are useful even when an exact estimate is unknown.'),('Calming urgency','我知道你在等，先别急，我会再发消息。','I know you are waiting; do not worry for now, I will message again.','Acknowledge the wait without claiming control over the driver or traffic.')],
[('你已经到了吗？','Have you arrived yet?','Give the actual state',['还没到，我还在车上。']),('什么时候再发消息？','When will you message again?','State the next update',['时间确认后再发。'])],
'Native check: 经过 versus 到站, the range of 才/都/就/正好, 该…了, clipped driver announcements and the original scene. No route, transport estimate or message delivery is asserted beyond the written scenario.')
