"""Editorial source: uncertain plans, evidence, event roles and moving boxes."""
from common import *
from editorial import unit
character_groups.update({
's3-u13':[('概','general outline'),('恐','fear'),('险','risk; danger'),('预','in advance'),('望','hope; look into the distance'),('将','will; forthcoming'),('念','think of; idea')],
's3-u14':[('并','also; alongside'),('根','root'),('简','simple; brief'),('绝','absolute; cut off'),('传','transmit'),('判','judge'),('实','real; solid')],
's3-u15':[('按','press; according to'),('管','manage; tube'),('集','gather'),('领','lead; receive'),('程','procedure; journey'),('宣','announce'),('派','send; faction')],
's3-u16':[('搬','move; carry'),('朝','toward'),('底','bottom'),('箱','box'),('具','tool; equipment'),('输','transport; lose'),('屋','room; house')],
})
# 实 is a previously taught level-1 character; the allocation below consolidates
# the genuinely new level-3 glyph 纪 in a displayed report context instead.
character_groups['s3-u14'][-1]=('纪','record; period')
unit_glosses.update({
's3-u13':{'要是':'if','下雨':'to rain','室内':'indoors','确认':'to confirm','安排':'arrangement','概念':'concept','念头':'thought; idea','天气':'weather','取消':'to cancel','条件':'condition','保险':'insurance; safer'},
's3-u14':{'核对':'to check against','通知':'notice','日期':'date','凭':'on the strength of','谣言':'rumour','纪录':'record','并不':'not actually','误会':'misunderstanding','传来':'to come through; be heard'},
's3-u15':{'组织者':'organizer','集合':'to assemble','分工':'division of work','负责人':'person in charge','流程':'procedure','签到':'to sign in','纪念':'to commemorate','派':'to send; assign','场地':'venue','批准':'to approve'},
's3-u16':{'箱子':'box','楼梯':'stairs','门口':'doorway','重':'heavy','轻':'light','抬':'to lift together','出口':'exit','入口':'entrance','绳子':'rope','台阶':'step','运输':'transportation','背包':'backpack','屋里':'inside the room'},
})
dictionary.update({'背包':'bēi bāo','背起来':'bēi qǐ lái'})
unit_glosses['s3-u14'].update({'来源':'source','模糊':'blurry','一趟':'one trip','提醒':'to remind'})
unit_glosses['s3-u15'].update({'话筒':'microphone','头衔':'title; rank','帽子':'hat'})
unit_glosses['s3-u16'].update({'挡住':'to block','轮子':'wheel'})
vocabulary_readings.update({'s3-u16:背':'bēi','s3-u16:朝':'cháo'})
selected_source_rows.update({'s3-u16:背':'258'})

u='s3-u13'
unit(u,'计划还没定',[
'Express estimates without presenting them as confirmed facts','Make a conditional indoor plan','Separate a wish, a decision and a forecast'],[
('大概','probably; roughly','có lẽ','adverb','她大概六点到，还没确认。','She will probably arrive at six; it is not confirmed.'),
('恐怕','I am afraid; probably, often unwelcome','e rằng','adverb','恐怕要下雨，先看预报。','I am afraid it may rain; check the forecast first.'),
('大约','approximately','khoảng','adverb','路上大约要二十分钟。','The journey takes approximately twenty minutes.'),
('希望','to hope; hope','hy vọng','verb','我希望能在外面见面。','I hope we can meet outside.'),
('愿望','wish; aspiration','nguyện vọng','noun','愿望不是已经定好的计划。','A wish is not an already settled plan.'),
('将来','in the future; the future','tương lai','noun','将来可以再组织活动。','We can organize another activity in the future.'),
('决定','to decide; decision','quyết định','verb','等天气确认了再决定地点。','Decide the venue after the weather is confirmed.'),
('适合','to suit; be suitable for','phù hợp','verb','室内更适合下雨天。','Indoors is more suitable for a rainy day.'),
('理由','reason','lý do','noun','改地点的理由是天气，不是不想见面。','Weather is the reason for changing the venue, not unwillingness to meet.'),
('不得不','have no choice but to','buộc phải','expression','场地关了，我们不得不改地点。','The venue is closed; we have no choice but to change locations.'),
('不必','need not','không cần','adverb','只是可能下雨，不必马上取消。','Rain is only possible; there is no need to cancel immediately.'),
('不安','uneasy','bất an','adjective','消息没确认，我有点不安。','The message is unconfirmed; I feel a little uneasy.'),
('风险','risk','rủi ro','noun','在外面办活动有下雨的风险。','An outdoor event carries the risk of rain.'),
('保险','safer; insurance','an toàn hơn; bảo hiểm','adjective','先准备室内地点比较保险。','Preparing an indoor venue first is safer.'),
('意外','unexpected; accident','bất ngờ','adjective','她提前到，让我很意外。','Her early arrival surprised me.'),
('预计','to estimate; expect','dự kiến','verb','预计六点到，不等于一定六点到。','Expected arrival at six does not mean certain arrival at six.'),
('预报','forecast; to forecast','dự báo','noun','预报说下午可能下雨。','The forecast says rain is possible this afternoon.'),
('预习','to prepare for a lesson','chuẩn bị bài','verb','活动前先预习要用的句子。','Prepare the sentences needed before the activity.'),
('仍','still, concise written form','vẫn','adverb','地点仍未确定。','The venue remains undecided.'),
('仍然','still','vẫn còn','adverb','我们仍然希望见面。','We still hope to meet.'),
('概念','concept','khái niệm','noun','可能和确定是不同的概念。','Possible and certain are different concepts.'),
('观念','notion; outlook','quan niệm','noun','计划可以改变，这个观念很重要。','The notion that plans can change is important.')],
[grammar(u,'三18','大概 / 恐怕','Signal uncertainty and an unwelcome possibility',
'大概六点到 is an estimate, not a guarantee. 恐怕要下雨 often presents an unwelcome possibility politely; it is not simply the verb 害怕. Neither adverb proves the event occurred. 大约 estimates an amount or time; avoid silently upgrading any estimate to a confirmed appointment.',[('她大概六点到。','She will probably arrive at six.'),('恐怕要下雨。','I am afraid it may rain.'),('大概会来，但还没确认。','She will probably come, but it is not confirmed.')],('大概六点到，就是保证六点到。','大概六点到，还要确认。','An estimate does not guarantee an exact time.')),
grammar(u,'三69','要是……就……','Make a conditional plan',
'要是下雨，就在室内见 states what to do under a condition, without asserting that the condition will occur. 就 belongs with the resulting plan. Use 如果 similarly, and distinguish a hypothetical consequence from a report of an event that has already happened.',[('要是下雨，就在室内见。','If it rains, meet indoors.'),('要是她还没到，我们就先发消息。','If she has not arrived, we will message first.'),('要是地点关了，就换一个。','If the venue is closed, change it.')],('要是下雨，所以已经取消了。','要是下雨，就改在室内见。','Keep the conditional plan separate from a completed cancellation.'))],
('A forecast, not a cancellation','Find what is confirmed and what is only conditional.',[
('你大概几点到？','About what time will you arrive?'),('预计六点，路上大约二十分钟。','I expect six; the journey takes about twenty minutes.'),('恐怕下午要下雨。我们取消吗？','I am afraid it may rain this afternoon. Should we cancel?'),('不必马上取消。要是下雨，就在室内见。','No need to cancel immediately. If it rains, meet indoors.'),('室内地点已经定了吗？','Is the indoor venue already settled?'),('还没有。我先确认，再告诉你。','Not yet. I will confirm it and then tell you.'),('好，我仍然希望见面。','Okay; I still hope we can meet.'),('我也是。愿望有了，地点还要查。','Me too. We have the wish; the venue still needs checking.')],
[('mainidea','What is the plan?',['Keep meeting possible and check an indoor option','Cancel immediately','Guarantee the outdoor venue'],0),('detail','Is six o’clock guaranteed?',['No, it is an estimate','Yes, precisely','No, arrival is confirmed at eight'],0),('inference','Does the conditional plan prove it will rain?',['No','Yes','Only if the journey is twenty minutes'],0)],[],True),
('A plan with two conditions','Separate the wish from the confirmed arrangement.',[
('我们仍然希望见面，地点仍未确定。','We still hope to meet; the venue remains undecided.'),('朋友预计六点到，路上大约二十分钟。','The friend expects to arrive at six; the journey is about twenty minutes.'),('预报说下午可能下雨，这不等于已经下雨。','The forecast says rain is possible this afternoon; it does not mean rain has already started.'),('要是下雨，就在室内见；室内地点也要先确认。','If it rains, meet indoors; the indoor venue also needs prior confirmation.'),('恐怕有下雨的风险，先准备另一个地点比较保险。','There may be a risk of rain; preparing another venue first is safer.'),('可能和确定是两个概念，计划能改变的观念也很重要。','Possible and certain are two concepts; the idea that plans can change matters too.'),('我有个念头：活动前预习句子，将来也可以继续用。','I have an idea: prepare the sentences before the event and use them in the future.'),('愿望不是决定，还没确认时不必写成已经安排好。','A wish is not a decision; do not record an unconfirmed plan as settled.')],
[('mainidea','What should the note distinguish?',['Estimates, wishes and confirmed arrangements','Every hope as a decision','A forecast as proof of past rain'],0),('detail','What needs confirmation?',['The indoor venue','A guarantee of sunshine','The friend’s refusal'],0),('inference','Is immediate cancellation required?',['No','Yes','Only because a wish exists'],0)],[(0,'希望'),(7,'决定')],False),
('The forecast is not your boss','Read an original exchange about a flexible plan.',[
('大概下雨，恐怕不能来了吧。','It will probably rain; perhaps we cannot come.'),('雨还没来，你先把见面取消了？','The rain has not arrived and you have cancelled the meeting already?'),('那我先查室内地点。','Then I will check an indoor venue first.'),('对。计划可以换，朋友不用换。','Right. The plan can change; the friend need not.')],
[('inference','What does the exchange suggest?',['Change the arrangement before assuming cancellation','Replace the friend','Ignore every forecast'],0)],[],True),
dict(tf=[('预计','她预计六点到，还没确认。','She expects to arrive at six; it is unconfirmed.','Arrival at six is guaranteed.',False,'预计 signals an estimate.'),('不必','不必马上取消，先查室内地点。','No need to cancel immediately; check indoors first.','The speaker proposes checking another venue first.',True,'The proposal keeps the meeting possible.')],reply=[('恐怕','恐怕要下雨，已经取消了吗？','It may rain; has the meeting been cancelled?',['还没有，先确认室内地点。','六点就是二十个人。','愿望已经证明下雨。'],0,'Report the actual undecided status.'),('适合','下雨时在哪里见更适合？','Where is more suitable for meeting in rain?',['确认好的室内地点。','没有查过的门口。','大约是一个决定。'],0,'Suitability does not remove the need to confirm.')],fill=[('希望','我们仍然希望见面。','We still hope to meet.'),('决定','先确认，再决定。','Confirm first, then decide.')],match=[('大概',[('她大概六点到。','She will probably arrive at six.'),('地点仍未确定。','The venue remains undecided.'),('要是下雨，就在室内见。','If it rains, meet indoors.')]),('愿望',[('愿望不是决定。','A wish is not a decision.'),('恐怕要下雨。','Rain may be an unwelcome possibility.'),('不必马上取消。','There is no need to cancel immediately.')])]),
[('Report uncertainty','大概六点到，还没确认。','Probably at six; not confirmed.','Do not give an estimate as a guarantee.'),('Offer a conditional alternative','要是下雨，就在室内见。','If it rains, meet indoors.','The alternative also needs an available venue.')],
[('地点定了吗？','Is the venue settled?','Report uncertainty',['还没确认。']),('要是下雨呢？','What if it rains?','Offer a conditional arrangement',['就在室内见。'])],
'Native check: 恐怕 pragmatic unwelcome possibility, 大概 versus 大约, adjective 保险 versus insurance noun, 仍 written register, possible versus certain concepts and the friend/plan joke. No claim that forecasts guarantee weather. Native review pending.')

u='s3-u14'
unit(u,'消息是真的吗',[
'Distinguish a rumour from a checked fact','Understand rhetorical questions without treating them as neutral questions','Correct an assumption using 并不'],[
('白','in vain; for nothing','uổng công','adverb','没核对日期，白跑了一趟。','Without checking the date, made a trip in vain.'),
('并','actually, with negation; also','thực ra; cũng','adverb','活动并没有取消。','The event has not actually been cancelled.'),
('当然','of course; certainly','tất nhiên','adverb','当然要看正式通知。','Of course we need to read the official notice.'),
('到底','after all; on earth','rốt cuộc','adverb','活动到底在哪一天？','On which day is the event, after all?'),
('反正','anyway; in any case','dù sao','adverb','反正还没出发，先核对日期。','Anyway, we have not set off; check the date first.'),
('根本','at all; fundamentally','hoàn toàn','adverb','旧消息根本不是今天的通知。','The old message is not today’s notice at all.'),
('果然','as expected','quả nhiên','adverb','核对后发现，果然是旧日期。','After checking, found that the date was old, as expected.'),
('简直','simply; practically','quả thật; gần như','adverb','这张模糊的图简直看不清。','This blurry image is practically unreadable.'),
('绝对','absolutely','tuyệt đối','adverb','没确认就说绝对取消，不合适。','It is inappropriate to say definitely cancelled without confirmation.'),
('难道','could it be that, rhetorical','chẳng lẽ','adverb','难道旧图片就能证明今天取消了吗？','Can an old picture really prove today’s cancellation?'),
('其实','actually; in fact','thực ra','adverb','其实只是换了房间。','Actually, only the room changed.'),
('千万','be sure to; by all means','nhất định','adverb','千万别把猜测当事实。','Be sure not to treat a guess as fact.'),
('确实','indeed; verified as true','quả thật','adverb','通知确实写着换房间。','The notice does indeed state a room change.'),
('只好','have no choice but to','đành phải','adverb','图片看不清，只好问负责人。','The image is unclear; there is no choice but to ask the organizer.'),
('终于','finally','cuối cùng','adverb','核对日期后，终于弄清楚了。','After checking the date, finally clarified it.'),
('事实','fact','sự thật','noun','换房间是事实，取消是猜测。','A room change is fact; cancellation is a guess.'),
('事实上','in fact','trên thực tế','adverb','事实上，时间没变。','In fact, the time did not change.'),
('判断','to judge; judgement','phán đoán','verb','判断前先看日期。','Check the date before judging.'),
('消息','message; news','tin tức','noun','这条消息没有写来源。','This message has no source indicated.'),
('传','to pass on; transmit','truyền','verb','没确认的消息先别传。','Do not pass on an unconfirmed message yet.'),
('传播','to spread; disseminate','truyền bá','verb','旧消息也会被传播。','Old messages can also be spread.'),
('真实','real; truthful','chân thực','adjective','图片真实，也可能不是今天的。','An image can be real and still not be from today.')],
[grammar(u,'三19','白 / 并 / 当然 / 到底 / 反正 / 根本 / 果然 / 简直 / 绝对 / 难道 / 其实 / 千万 / 确实 / 只好 / 终于','Track attitude and evidential limits',
'白跑 means a trip in vain. 并没有 challenges an assumed cancellation; it is not English however by itself. 根本不是 strengthens negation. 果然 says a finding matches an expectation, not that expectation alone proves it. 其实 and 事实上 introduce a correction. 绝对 is a strong commitment; avoid it for a guess. 千万别 is emphatic caution, 只好 constrained choice, 终于 an eventual result. Attitude adverbs do not supply evidence.',[('活动并没有取消，只是换了房间。','The event is not cancelled; only the room changed.'),('果然是旧日期，今天的时间没变。','It is an old date as expected; today’s time is unchanged.'),('千万别把猜测当事实。','Be sure not to treat a guess as fact.')],('果然，我猜了，所以是真的。','核对后，果然和我猜的一样。','果然 comments on a verified outcome matching an expectation.')),
grammar(u,'三76','不是……吗？ / 难道……吗？','Recognize rhetorical force',
'不是写着换房间吗？ points to information the speaker expects the listener to acknowledge. 难道旧图片就能证明今天取消了吗？ challenges that inference and expects no; it is not neutral uncertainty about any cancellation. Tone and context matter. For a genuinely open question use 活动取消了吗？ without forcing agreement.',[('不是写着换房间吗？','Does it not say the room changed?'),('难道旧图片就能证明今天取消了吗？','Can an old picture really prove today’s cancellation?'),('活动取消了吗？','Has the event been cancelled?')],('难道旧图能证明吗？一定是在认真问图片大小。','难道旧图能证明吗？是在质疑这个判断。','The rhetorical question challenges an inference, not image dimensions.'))],
('Read the date before forwarding','Find what changed in the actual notice.',[
('我收到消息，说今天活动绝对取消了。','I received a message saying today’s event is definitely cancelled.'),('来源呢？图片上有日期吗？','What is the source? Is there a date on the picture?'),('图很模糊，简直看不清。','The image is blurry, practically unreadable.'),('难道看不清的旧图就能证明取消了吗？','Can an unreadable old picture really prove cancellation?'),('那只好问负责人了。','Then there is no choice but to ask the organizer.'),('我查了正式通知。确实换房间，时间没变。','I checked the official notice. The room did change; the time did not.'),('活动并没有取消，我先不传那条消息。','The event is not cancelled; I will not forward that message yet.'),('对，反正还没出发，先看新房间。','Right; we have not set off anyway, so check the new room first.')],
[('mainidea','What is corrected?',['A cancellation claim: only the room changed','A confirmed cancellation','A changed event time'],0),('detail','What did the checked notice change?',['The room','The time','The event date'],0),('inference','What answer is expected by the rhetorical question?',['No, the image does not prove cancellation','Yes, every old image proves it','The image is twenty minutes long'],0)],[],True),
('A true image can be out of date','Read how a message was checked.',[
('传来的消息说活动取消，图片却没有清楚的日期。','A message that came through said the event was cancelled, but its picture lacked a clear date.'),('图片真实，不等于它就是今天的通知。','An image being real does not mean it is today’s notice.'),('我问了负责人，再核对正式通知和纪录。','I asked the organizer and checked the official notice and record.'),('事实是换房间，事实上时间没有变。','The fact is a room change; in fact the time has not changed.'),('活动并没有取消，旧消息根本不能证明今天的安排。','The event is not cancelled; the old message cannot establish today’s arrangements at all.'),('没确认的消息先别传播，千万别让朋友白跑一趟。','Do not spread unconfirmed news yet; be sure not to make a friend travel in vain.'),('终于弄清楚了，再告诉朋友新房间。','Having finally clarified it, tell the friend the new room.'),('不是写着换房间吗？是在提醒看通知，不是在报告取消。','Does it not say the room changed? This reminds one to read the notice, not reports cancellation.')],
[('mainidea','What is the check based on?',['The organizer, notice and record','Only the image looking real','The strength of the word absolutely'],0),('detail','Has the event time changed?',['No','Yes','It became unknown because the picture is blurry'],0),('inference','Can an authentic image still be outdated?',['Yes','No','Only after someone forwards it'],0)],[(3,'事实'),(6,'终于')],False),
('Your adverb is not a source','Read an original exchange about certainty.',[
('我说了绝对，听起来不是很确定吗？','I said absolutely; does that not sound certain?'),('很确定。来源呢？','Very certain. Where is the source?'),('还没查。','I have not checked it yet.'),('先查。声音大不算核对。','Check first. A loud voice does not count as verification.')],
[('inference','What does the reply ask for?',['Evidence, not a stronger delivery','A louder repetition','A new image colour'],0)],[],True),
dict(tf=[('并','活动并没有取消，只是换房间。','The event is not cancelled; only the room changed.','The event is cancelled.',False,'并没有 negates the assumed cancellation.'),('真实','图片真实，但不是今天的。','The image is real but not from today.','Real and current are different claims.',True,'Authenticity does not establish the date.')],reply=[('消息','没确认的消息现在传吗？','Forward the unconfirmed message now?',['先别传，核对日期和来源。','加上绝对就可以。','把房间当时间。'],0,'Check before spreading it.'),('事实','到底改了什么？','What changed after all?',['房间改了，时间没变。','声音更大了。','朋友一定白跑了。'],0,'Answer with the verified change.')],fill=[('其实','其实只是换了房间。','Actually, only the room changed.'),('终于','终于弄清楚了。','Finally clarified it.')],match=[('只好',[('图看不清，只好问负责人。','The image is unreadable; one has to ask the organizer.'),('千万别把猜测当事实。','Be sure not to treat a guess as fact.'),('反正还没出发。','We have not set off anyway.')]),('判断',[('判断前先看日期。','Check the date before judging.'),('消息没有来源。','The message has no source.'),('果然是旧日期。','The date is old, as expected.')])]),
[('Correct a mistaken claim','并没有取消，只是换房间。','It is not cancelled; only the room changed.','Give the actual correction without exaggerating evidence.'),('Ask neutrally','活动取消了吗？','Has the event been cancelled?','Use an open question when the answer is genuinely unknown.')],
[('改了什么？','What changed?','State the verified change',['只是换了房间。']),('现在传吗？','Forward it now?','Recommend checking first',['先核对来源。'])],
'Native check: 白跑, 并 with negation, 反正 versus indifference, 果然 expectation and evidence, strong 绝对, rhetorical question polarity and polite alternatives. Distinguish 纪录 as record from 记录 as recording. No unverified claims marked facts. Native review pending.')

u='s3-u15'
unit(u,'谁来组织活动',[
'Assign responsibility with 由','Follow a specified procedure with 按 / 按照','Distinguish a representative from an organizer'],[
('由','by; through; from','do; bởi','preposition','这次活动由学生举办。','This event is organized by students.'),
('按','according to; press','theo','preposition','按名单分组，不按到达时间。','Group by the list, not arrival time.'),
('按照','according to','theo đúng','preposition','按照通知上的流程签到。','Sign in according to the procedure on the notice.'),
('举办','to hold; organize an event','tổ chức','verb','学生部门举办交流活动。','The student department holds an exchange event.'),
('部门','department','bộ phận','noun','这个部门负责报名。','This department handles registration.'),
('部长','department head; minister','trưởng bộ phận','noun','部长不是每场活动的主持人。','The department head is not the host of every event.'),
('主任','director; head','chủ nhiệm','noun','主任确认场地，不负责主持。','The director confirms the venue and does not host.'),
('主持','to host; chair','dẫn chương trình','verb','活动由一位学生主持。','One student hosts the event.'),
('代表','representative; to represent','đại diện','noun','每组派一位代表发言。','Each group sends one representative to speak.'),
('代表团','delegation','đoàn đại biểu','noun','代表团来交流，不等于举办方。','The delegation comes for an exchange; it is not necessarily the organizer.'),
('带领','to lead','dẫn dắt','verb','工作人员带领大家进场。','Staff lead everyone into the venue.'),
('管理','to manage; management','quản lý','verb','场地由学校管理。','The school manages the venue.'),
('集中','to concentrate; assemble','tập trung','verb','大家先在门口集中。','Everyone first assembles at the entrance.'),
('会议','meeting; conference','cuộc họp','noun','会议结束后再交流。','Have the exchange after the meeting ends.'),
('会员','member of an association','hội viên','noun','不是会员也可以先听。','Even nonmembers may listen first.'),
('办理','to handle; complete formalities','làm thủ tục','verb','报名手续在门口办理。','Registration formalities are handled at the entrance.'),
('手续','formalities; procedure','thủ tục','noun','办完手续再进场。','Enter after completing the formalities.'),
('报到','to report for arrival; register on arrival','đến trình diện','verb','到达后先报到。','Report on arrival first.'),
('发言','to speak at a meeting','phát biểu','verb','代表发言两分钟。','The representative speaks for two minutes.'),
('派','to send; assign','cử','verb','每组派一人，不是全组都上台。','Each group sends one person, not the whole group onto the stage.'),
('过程','process; course of events','quá trình','noun','活动过程写在通知里。','The event process is written in the notice.'),
('宣传','to publicize; publicity','tuyên truyền; quảng bá','verb','宣传前先确认时间。','Confirm the time before publicizing it.')],
[grammar(u,'三20','由：行动的负责方','Name the agent responsible for an action',
'活动由学生举办 names the responsible agent before the action. Compare 场地由学校管理 with a person merely attending. A delegation or representative need not be the organizer. In these agentive examples 由 does not mean because; 由于 is a separate causal expression.',[('活动由学生举办。','Students organize the event.'),('场地由学校管理。','The school manages the venue.'),('会议由一位学生主持。','One student chairs the meeting.')],('代表来了，所以活动由他举办。','代表来交流，举办方要另查。','Attendance or representation does not establish responsibility.')),
grammar(u,'三29','按 / 按照 + 依据','Identify the basis for a procedure',
'按名单分组 gives the grouping basis, while 按照通知上的流程签到 gives a procedural basis. 按到达时间 and 按名单 may yield different groups; read which is stated. The verb 按 in 按按钮 is press, not the preposition according to.',[('按名单分组。','Group according to the list.'),('按照通知上的流程签到。','Sign in according to the procedure in the notice.'),('按组发言，不按到达时间。','Speak by group, not by arrival time.')],('按名单分组，就是谁先到谁先说。','按名单分组，顺序要看名单。','Do not replace the stated criterion with arrival order.'))],
('A host, a head and a representative','Find who organizes, who hosts and how speaking turns are assigned.',[
('这次交流由谁举办？','Who organizes this exchange?'),('由学生部门举办，场地由学校管理。','The student department organizes it; the school manages the venue.'),('部长主持吗？','Does the department head host?'),('不，一位学生主持，主任确认场地。','No; a student hosts, and the director confirms the venue.'),('我们代表团怎么报到？','How should our delegation report on arrival?'),('先在门口集中，按照通知办理手续。','Assemble at the entrance first and complete the formalities according to the notice.'),('每组都上台吗？','Does every entire group go on stage?'),('每组派一位代表，按名单发言，每人两分钟。','Each group sends one representative, speaking according to the list, two minutes each.')],
[('mainidea','What does the conversation clarify?',['Responsibilities and speaking procedure','Every participant is a host','Arrival order replaces the list'],0),('detail','Who hosts?',['A student','The director','Every delegation member'],0),('inference','Do four people from one group all speak?',['No, one representative is assigned','Yes, all four','Only if they arrive late'],0)],[],True),
('Read the role, not just the title','Find the difference between venue management and event hosting.',[
('活动由学生部门举办，学校负责管理场地。','The student department organizes the event; the school manages the venue.'),('主任确认场地，学生主持会议；部长不主持。','The director confirms the venue and a student chairs the meeting; the department head does not host.'),('工作人员带领大家进场，所有人先在门口集中。','Staff lead everyone in; everyone assembles at the entrance first.'),('代表团先报到，再按照通知办理手续。','The delegation reports on arrival and completes formalities according to the notice.'),('分组和发言都按名单，不按到达的先后。','Grouping and speaking both follow the list, not arrival order.'),('每组派一位代表，每人发言两分钟。','Each group sends one representative who speaks for two minutes.'),('活动流程已经确认，宣传不能把时间写错。','The event procedure is confirmed; publicity must not give the wrong time.'),('集合后先看分工，再进去。纪念活动也要按通知安排。','After assembling, check responsibilities before entering. A commemorative event also follows the notice.')],
[('mainidea','Why read the stated role?',['A title alone does not tell who hosts','Every head must host','Venue managers always speak first'],0),('detail','What sets speaking order?',['The list','Arrival order','The representative’s age'],0),('inference','Must a visiting delegation organize the event?',['No','Yes','Only with four members'],0)],[(0,'举办'),(5,'代表')],False),
('The title does not hold the microphone','Read an original role mix-up.',[
('部长到了，话筒给他吧。','The department head is here; give him the microphone.'),('先看通知，今天由学生主持。','Read the notice first; a student hosts today.'),('那头衔不能当发言名单。','Then a title cannot serve as the speaking list.'),('对。名单不会因为帽子大就改。','Right. A grand title does not change the list.')],
[('inference','What corrects the assumption?',['The assigned role in the notice','A bigger hat','The order of arrival'],0)],[],True),
dict(tf=[('主持','学生主持，主任确认场地。','The student hosts; the director confirms the venue.','The director hosts.',False,'The stated roles are different.'),('代表','每组派一位代表，每人两分钟。','Each group sends one representative, two minutes each.','One group sends one speaker.',True,'每组一位 gives the group allocation.')],reply=[('按','按什么顺序发言？','What determines speaking order?',['按名单，不按到达时间。','部长就是所有会员。','每个人都能改通知。'],0,'Use the specified list.'),('报到','到达后先做什么？','What comes first on arrival?',['先在门口报到。','先替全组发言。','先写取消通知。'],0,'Arrival registration precedes entry.')],fill=[('由','活动由学生举办。','Students organize the event.'),('按照','按照通知办理手续。','Complete formalities according to the notice.')],match=[('管理',[('场地由学校管理。','The school manages the venue.'),('学生主持会议。','A student chairs the meeting.'),('代表发言两分钟。','The representative speaks for two minutes.')]),('集中',[('先在门口集中。','Assemble at the entrance first.'),('每组派一位代表。','Each group sends one representative.'),('宣传前确认时间。','Confirm the time before publicity.')])]),
[('Check responsibility','这次由谁举办？','Who organizes this event?','Do not infer the organizer from an attendee’s title.'),('Ask for the actual order','按名单还是按到达时间？','By the list or by arrival time?','Ask when the basis is unclear.')],
[('谁主持？','Who hosts?','State the assigned role',['一位学生主持。']),('每组派几人？','How many does each group send?','State the exact allocation',['每组一位代表。'])],
'Native check: 由 agent construction versus 由于, 按 and 按照 register, 报到 versus 报道, department/head/member roles, 纪念 activity context and grand-title metaphor. No implication of real institution rules. Native review pending.')

u='s3-u16'
unit(u,'箱子往哪里搬',[
'Interpret direction relative to the speaker','Follow a sequence of movement instructions','Ask before moving a heavy item'],[
('朝','toward; face','hướng về','preposition','朝门口走，别朝楼梯走。','Walk toward the doorway, not toward the stairs.'),
('搬','to move; carry objects','chuyển; mang','verb','把轻箱子搬到门口。','Move the light box to the doorway.'),
('搬家','to move house','chuyển nhà','verb','搬家先确认新地址。','Confirm the new address before moving house.'),
('背','to carry on the back','cõng; đeo','verb','轻背包可以背起来。','The light backpack can be carried on the back.'),
('背后','behind; at the back','phía sau','noun','背后的门不要挡住。','Do not block the door behind you.'),
('底下','underneath; below','bên dưới','noun','箱子底下没有轮子。','The box has no wheels underneath.'),
('里面','inside','bên trong','noun','里面是书，先别倒过来。','There are books inside; do not turn it upside down.'),
('外面','outside','bên ngoài','noun','外面下雨，先别搬出去。','It is raining outside; do not move it out yet.'),
('上面','on top; above','bên trên','noun','上面写着轻，不代表里面没有东西。','Light is written on top; it does not mean nothing is inside.'),
('下面','under; below','bên dưới','noun','下面的纸不要压住。','Do not pin down the paper underneath.'),
('前面','in front','phía trước','noun','前面是入口，出口在后面。','The entrance is in front; the exit is at the back.'),
('后面','behind; afterward','phía sau','noun','后面的箱子比较重。','The box behind is heavier.'),
('上来','to come up','lên phía người nói','verb','你先上来，我在二楼。','Come up first; I am on the second floor.'),
('上去','to go up','đi lên','verb','把箱子搬上去，我在一楼等。','Carry the box up; I will wait on the first floor.'),
('下来','to come down','xuống phía người nói','verb','你下来吧，我在一楼。','Come down; I am on the first floor.'),
('下去','to go down','đi xuống','verb','你先下去，我在二楼等。','Go down first; I will wait on the second floor.'),
('运输','to transport; transportation','vận chuyển','noun','运输前先把箱子装好。','Pack the boxes properly before transport.'),
('安装','to install','lắp đặt','verb','这张桌子还要安装。','This desk still needs installing.'),
('家具','furniture','đồ nội thất','noun','家具搬完再整理书。','Organize the books after moving the furniture.'),
('工具','tool','dụng cụ','noun','安装工具在小箱子里。','The installation tools are in the small box.'),
('木头','wood','gỗ','noun','这块木头不是座位。','This piece of wood is not a seat.'),
('推开','to push open; push aside','đẩy ra','verb','先推开门，再搬箱子。','Push the door open before moving the box.')],
[grammar(u,'三22','朝 + 方向 / 目标','Give a direction without claiming arrival',
'朝门口走 names the direction of movement; it does not say the person has already reached the doorway. Compare 搬到门口, which specifies the resulting location. 朝这里走 depends on the speaker’s position. Verify which entrance or stairway is intended before moving a heavy object.',[('朝门口走。','Walk toward the doorway.'),('朝这里走，先别上楼。','Walk this way; do not go upstairs yet.'),('搬到门口，再停下。','Move it to the doorway and then stop.')],('朝门口走了，所以已经到门口了。','朝门口走了，还没说是否到达。','Direction of motion does not establish the endpoint.')),
grammar(u,'三47','出来 / 出去 / 过来 / 过去 / 回来 / 回去 / 进来 / 进去 / 起来 / 上来 / 上去 / 下来 / 下去','Interpret compound directional complements',
'来 generally directs movement toward the reference speaker, 去 away. 我在二楼，你上来 contrasts with 我在一楼，你上去. 出/进 locate movement across a boundary, 回 indicates returning, 过 crossing toward or away from a point. 起来 can mean upward movement, not necessarily toward the speaker. With a location keep it before 来/去: 搬到门口来. Ask for the reference position when unclear; do not give dangerous lifting instructions.',[('我在二楼，你上来。','I am on the second floor; come up.'),('我在一楼，你先上去。','I am on the first floor; go up first.'),('把轻箱子搬到门口来，再把工具拿进去。','Bring the light box to the doorway, then take the tools inside.')],('我在二楼，你从一楼下来找我。','我在二楼，你从一楼上来找我。','Align upward or downward movement with the actual floors.'))],
('A light box and a heavy box','Track the floor and the speaker’s position.',[
('你在哪儿？箱子朝哪里搬？','Where are you? Which way should the boxes be moved?'),('我在一楼门口。先把轻箱子搬过来。','I am at the first-floor doorway. Bring the light box over first.'),('后面那个比较重，也搬过来吗？','The one behind is heavier; bring it over too?'),('先别动，等两个人一起抬。出口不能挡住。','Leave it for now; wait for two people to lift it together. Do not block the exit.'),('轻箱子里面是什么？','What is inside the light box?'),('书和安装工具。工具先拿进去，书先放在门口。','Books and installation tools. Take the tools inside first; leave the books at the doorway for now.'),('我现在上去吗？','Should I go upstairs now?'),('先在一楼等。桌子安装好以后再上去。','Wait on the first floor for now. Go upstairs after the desk is installed.')],
[('mainidea','What determines the movement?',['The speaker’s location and the stated sequence','Every box going upstairs immediately','The label alone proving weight'],0),('detail','Where is the speaker?',['At the first-floor doorway','On the second floor','Outside in the rain'],0),('inference','Should one move the heavier box alone now?',['No, wait for help','Yes, immediately','Only because it is behind'],0)],[],True),
('First the tools, then the furniture','Read the movement sequence without reversing directions.',[
('我在一楼门口，请先朝这里走。','I am at the first-floor doorway; walk this way first.'),('轻箱子先搬过来，重箱子暂时不动。','Bring the light box over first; leave the heavy box for now.'),('箱子底下没有轮子，重箱子等两个人一起抬。','There are no wheels beneath the box; wait for two people to lift the heavy box together.'),('小箱子里面是工具，先拿进去；书先放在门口。','The small box contains tools; take them inside first, leaving the books at the doorway.'),('背包可以背起来，箱子要装好，运输时不能散开。','Carry the backpack on the back; pack the box properly so it does not come apart in transport.'),('前面是入口，后面是出口，家具不能挡住出口。','The entrance is in front and the exit behind; furniture must not block the exit.'),('桌子还没安装好，先在一楼等，不要把书搬上去。','The desk is not yet installed; wait downstairs and do not carry the books up yet.'),('外面下雨，木头和下面的纸都先留在屋里。','It is raining outside; leave the wood and paper underneath indoors for now.')],
[('mainidea','What is the note asking readers to follow?',['An ordered sequence with a clear reference location','All objects out into the rain','A claim that every box is light'],0),('detail','What goes inside first?',['The tools','The heavy box alone','Every book upstairs'],0),('inference','Does 朝这里走 mean arrival is complete?',['No','Yes','Only on the first floor'],0)],[(1,'搬'),(3,'工具')],False),
('The box has no legs','Read an original scene about asking for help.',[
('我让箱子过来，它怎么不动？','I told the box to come over; why is it not moving?'),('它没有腿，你也不用假装有四只手。','It has no legs; you need not pretend to have four hands either.'),('那重的先不动，等人帮忙。','Then leave the heavy one and wait for help.'),('这次方向和力气都算对了。','This time both the direction and the strength are accounted for.')],
[('inference','What does the joke encourage?',['Waiting for suitable help','Moving every heavy box alone','Blocking the exit'],0)],[],True),
dict(tf=[('上来','我在二楼，你上来。','I am on the second floor; come up.','Movement is toward the speaker on the second floor.',True,'来 uses the speaker as the reference.'),('工具','工具先拿进去，书先放在门口。','Take the tools in first; leave books at the doorway.','Books go upstairs first.',False,'Tools go inside; books stay by the doorway.')],reply=[('搬','重箱子现在一个人搬吗？','Move the heavy box alone now?',['先别动，等人一起抬。','出口挡住也可以。','箱子会自己上来。'],0,'Wait for appropriate help.'),('朝','你在一楼门口，我朝哪儿走？','You are at the first-floor doorway; which way should I walk?',['朝一楼门口走。','先去二楼再下雨。','把工具当楼梯。'],0,'Name the actual target.')],fill=[('上去','先安装好，再上去。','Install it first, then go up.'),('里面','工具在小箱子里面。','The tools are inside the small box.')],match=[('底下',[('箱子底下没有轮子。','There are no wheels underneath the box.'),('我在一楼，你先上去。','I am downstairs; go up first.'),('我在二楼，你上来。','I am upstairs; come up.')]),('家具',[('家具不能挡住出口。','Furniture must not block the exit.'),('先把工具拿进去。','Take the tools inside first.'),('重箱子暂时不动。','Leave the heavy box for now.')])]),
[('Clarify the reference','你在楼上还是楼下？','Are you upstairs or downstairs?','Ask before interpreting 来 and 去.'),('Set a safe boundary','这个太重，等人一起抬。','This is too heavy; wait for help lifting it.','The lesson does not teach lifting technique or promise a safe weight.')],
[('先搬哪个？','Which should be moved first?','Follow the sequence',['先搬轻箱子。']),('书现在上去吗？','Do the books go up now?','State the condition',['先等桌子安装好。'])],
'Native check: directional viewpoint, 上来/上去 and reference floor, 朝 versus 到 endpoint, 背 bēi versus bèi, 箱子运输 wording and informal four-hands joke. No specific safe-weight or lifting-technique claim. Native review pending.')

from retrievals import apply_ids
apply_ids(['s3-u13','s3-u14','s3-u15','s3-u16'])
