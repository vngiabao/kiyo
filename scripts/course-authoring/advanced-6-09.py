"""Read a magazine feature against its notice, keeping conditions in the summary."""
import sys
from advanced_core import write,rows,words,q,card,practice
V=words('''
稿子|draft; manuscript|bản thảo|这份稿子先讲借书的故事，再给出数字。|The draft starts with a borrowing story before giving numbers.|她把稿子改短了。|She shortened the draft.
章|chapter classifier|chương|第二章写夜间开放的安排。|Chapter two describes evening opening arrangements.|这本书一共有六章。|This book has six chapters.
说明书|instruction manual|hướng dẫn|设备的说明书放在柜台旁。|The equipment manual is beside the counter.|先看说明书再操作。|Read the manual before operating it.
评|evaluate; comment on|đánh giá|别只凭一句标题评整篇文章。|Don't judge the whole article from its headline alone.|你先读完，再评这段。|Read it through before commenting on this passage.
评选|select through evaluation|bình chọn|读者可以评选最想参加的活动。|Readers can vote for the activity they most want to attend.|这次评选下周结束。|This selection ends next week.
优质|high-quality|chất lượng tốt|优质的活动也要安排合适的时间。|Even a high-quality event needs suitable timing.|他们希望提供优质的服务。|They hope to offer high-quality service.
外观|outward appearance|bề ngoài|外观变新不表示借书方式也变了。|A new appearance doesn't mean borrowing procedures changed.|我喜欢这张桌子的外观。|I like the appearance of this table.
本地|local|địa phương|本地杂志采访了图书馆工作人员。|A local magazine interviewed library staff.|她想认识一些本地朋友。|She wants to meet some local friends.
前来|come to a place|đến|前来活动的人也有只听不借书的。|Some event visitors listen without borrowing.|他前来领取自己的资料。|He came to collect his materials.
此处|here; this place|tại đây|此处登记活动，不办理借书。|Event registration happens here, not book borrowing.|此处暂时不能停车。|Parking here is temporarily prohibited.
截至|up to a stated point|đến thời điểm|截至月底，共有六十四次到访。|By month's end there were sixty-four visits.|截至周五，名额还没有满。|As of Friday the places weren't full.
发放|distribute|phát|工作人员在门口发放节目单。|Staff hand out programmes at the entrance.|资料明天统一发放。|The materials will be distributed tomorrow.
发起|initiate|khởi xướng|两个读者发起了晚间读书活动。|Two readers initiated the evening reading event.|她发起了一个小范围的讨论。|She started a small discussion.
提交|submit|nộp|想带作品的人先提交一段介绍。|People bringing work first submit a short introduction.|他按时提交了申请。|He submitted the application on time.
通报|inform relevant people|thông báo|馆员向报名的人通报时间调整。|The librarian told registrants about the time change.|小组通报了活动结果。|The group announced the event results.
场馆|venue building|địa điểm|场馆平日六点关门。|The venue normally closes at six.|那个场馆就在车站旁。|That venue is beside the station.
场地|space for an activity|không gian|夜间活动只用一楼场地。|The evening event uses only the downstairs space.|活动临时换了场地。|The event changed location at short notice.
名额|available places|suất|周末讲座有二十个名额。|The weekend talk has twenty places.|我想问还有没有名额。|I'd like to ask whether any places remain.
常规|routine|thông lệ|常规借书时间没有延长。|Normal borrowing hours have not been extended.|这是常规安排的一部分。|This is part of the usual arrangement.
试点|pilot|thí điểm|夜间开放先试点四周。|Evening opening is initially a four-week pilot.|试点结束后再听取意见。|Hear feedback after the pilot ends.
切实|practical and effective|thiết thực|错开收尾时间是一个切实的改进。|Separating closing duties is a practical improvement.|她想找到切实的办法。|She wants to find a workable solution.
能否|whether it is possible|liệu có thể|能否继续开放，还得看人员安排。|Continued opening depends on staffing.|能否带朋友参加，请先确认。|Please confirm whether a friend can join.
因素|factor|yếu tố|附近演出也是到访增加的因素。|A nearby performance also contributed to visits.|她考虑了几个不同因素。|She considered several different factors.
关联|connection|liên quan|这两件事有关联，文章却没有说谁造成谁。|The two are connected, but the article doesn't state which caused which.|这张图和正文有什么关联？|How does this picture relate to the text?
核心|core|cốt lõi|文章的核心是一次有条件的尝试。|The article centres on a trial with conditions.|先说核心问题，细节以后补。|Start with the central issue and add details later.
差异|difference|khác biệt|两份材料的差异主要在关注的事。|The materials chiefly differ in what they focus on.|数字的差异需要解释。|The numerical difference needs explanation.
据|according to|theo|据值班记录，六十四是到访次数。|According to the duty record, sixty-four counts visits.|据通知，周四只开放一楼。|According to the notice, only downstairs opens on Thursday.
至于|as for|còn về|至于借书，还是白天办理。|Borrowing is still handled during the day.|至于下个月的安排，还没确定。|Next month's arrangements are undecided.
最终|final; ultimately|cuối cùng|最终决定要等试点结束。|The final decision will wait until the pilot ends.|他们最终选了小房间。|They finally chose the small room.
只得|have no alternative but|đành phải|忘了带卡，她只得白天再来借书。|Having forgotten her card, she had to return in daytime to borrow.|雨太大，我们只得换到室内。|The heavy rain left us no choice but to move indoors.
免得|so as to avoid|để tránh|把借书时间写上，免得读者白跑。|Include borrowing hours so readers don't make a wasted trip.|先确认地点，免得走错。|Confirm the venue first to avoid going to the wrong place.
听取|hear and consider|lắng nghe|馆员先听取到访者的意见。|The librarian first hears visitors' views.|小组会听取不同意见。|The group will hear differing views.
''')
D=rows('''
你把杂志那篇看完了吗？|Have you finished that magazine article?
看了，标题说图书馆把夜晚还给读者。|Yes. The headline says the library gives the night back to readers.
那今晚能去借书？|Can we borrow books tonight then?
先别急，文章后面说夜里只开一楼。|Hold on—the article later says only the ground floor opens at night.
借书柜台不是也在一楼？|Isn't the lending counter there too?
在，但夜间只办活动，不办借书。|Yes, but evenings are for events, not borrowing.
这标题把我带远了。|That headline led me a bit far.
所以我让你看完嘛。|That's why I told you to finish it.
六十四个人来过，听着不少。|Sixty-four people visited—that sounds like quite a few.
六十四次，不是六十四个人。有的人每周都来。|Sixty-four visits, not people. Some came every week.
那有没有单独的人数？|Is there a separate count of people?
没有，至少这篇没给。|No, at least not in this article.
你都看到哪了？|How far did you get?
最后一段。还写了收椅子的安排。|The final paragraph. It even describes putting chairs away.
你现在连椅子都查？|You're checking chairs now too?
不是查椅子，是别让九点走的人替十点走的人收。|Not the chairs; we shouldn't assign closing work to people who leave at nine.
通知写八点结束，八点半清场。|The notice says finish at eight, clear the room by eight thirty.
对，文章讲故事，通知给实际安排。|Right. The article tells the story; the notice gives practical arrangements.
我想参加下周那场，先报名？|I'd like next week's event. Register first?
好，二十个名额，周五前回复。|Yes—twenty places; reply before Friday.
要带一本书吗？|Should I bring a book?
可以带，也可以只听。借书得白天来。|You can bring one or just listen. Borrowing needs a daytime visit.
行，那今晚先听。我的书先不用跟着加班。|Fine—I'll listen tonight. My book needn't work overtime too.
你把卡带着，下次白天就能借。|Keep your card with you so you can borrow next time during the day.
''')
M=rows('''
标题说整座城都醒了。|The headline says the whole city woke up.
我家楼下还挺安静。|It's still pretty quiet downstairs from me.
那是写得热闹，不是调查全城睡没睡。|That's lively writing, not a survey of whether the entire city is asleep.
我知道。我是在问今晚开不开。|I know. I'm asking whether it opens tonight.
周四开，你现在看的通知是周末讲座。|Thursday opens; the notice you're reading is for a weekend talk.
两张放一起，我看串了。|They're together; I mixed them up.
把日期也看上。|Read the date too.
周四八点结束，周末两点开始。|Thursday finishes at eight; the weekend event starts at two.
这回对了。|Right this time.
我终于把夜晚跟下午分开了。|Finally I've separated night from afternoon.
不用起这么大的标题。|No need for such a grand headline.
那叫我今天没跑错。|Then call it 'I didn't go to the wrong event today'.
''')
R=rows('''
每到周四晚上，社区图书馆一楼的灯会比平时多亮两个小时。白天经过那里的人，常以为六点以后门就锁了；现在有人下班吃过饭，又拿着一本薄书走进来。活动不是正式的课，也不要求读者准备长篇介绍。桌上有热水，椅子围成半圈，先由两个人读一小段，再让愿意的人接着说。有人每周都来，有人只是等附近演出开场时进来坐一会儿。灯亮起来，首先改变的是这几种普通的经过方式。|Each Thursday the neighbourhood library's ground floor stays lit two hours longer. People who thought it closed at six now come after dinner with a slim book. It isn't a formal class or a long prepared presentation. There is hot water and a semicircle of chairs. Two readers read a passage, then others may speak. Some come weekly; others wait for a nearby performance. The lights first change these ordinary ways of passing through.
这个尝试由两位常来的读者发起，馆员帮他们申请场地。原来的想法很简单：白天忙的人也能有个地方见面谈书。为了不打乱常规服务，借书柜台仍按六点结束办理，夜间只开一楼的活动区域，二楼不开放。第一阶段安排四个周四，结束后再根据值班、参加情况和反馈决定下一步。有人问能不能每天都开到八点，馆员说现在的人手只能支持这四次，不能把一个小范围试点写成已经开始的长期服务。|Two regular readers initiated the trial and librarians helped apply for space. The aim was a place for busy daytime workers to discuss books. Normal lending still ends at six; only the ground-floor activity area opens in the evening. Four Thursdays form the initial trial, followed by review of staffing, participation and feedback. Current staffing supports those four evenings, not daily long-term opening.
四次活动结束，到访记录分别是十八、二十、十二和十四次，共六十四次。这里记录的是每次走进活动区的人次，不是去掉重复以后的六十四位居民。前两次正好遇到附近有演出，有几个人听一小段就离开；第三次下雨，也有人提前发消息说不方便来。组织者没有把每一种变化都归到读书内容上。大家更关心留下的人能不能听清、椅子够不够，以及八点结束时还有没有人临时才知道不能借书。|The four visit counts were eighteen, twenty, twelve and fourteen, totalling sixty-four visits rather than sixty-four unique residents. The first two coincided with nearby performances; some left shortly. Rain affected the third. Organisers didn't assign every change to reading content. They cared about audibility, seating and whether anyone learned only at eight that lending was unavailable.
第一次的通知没有把最后一点写醒目。有位读者带着想借的书名赶来，等讨论结束才发现柜台已经下班。他没有责怪读书的人，只问为什么亮着灯却不能借。馆员解释白天服务和晚间活动的人员安排不同，随后把借书时间加到入口的纸上，也放进报名回复里。第二次仍有一个人看漏了，但他进门就问清，决定先留下听，下周白天再来办理。修改一张通知没让问题马上消失，却减少了把期待一路带到散场才落空的情况。|The first notice didn't make that clear. A visitor arrived with book titles to borrow, learning after discussion that lending had closed. Staff explained the separate arrangements and added lending hours to the entrance and registration reply. Someone missed it the next week but asked on arrival, chose to listen and planned a daytime return. A changed notice didn't erase every problem, but reduced disappointment discovered only at the end.
晚间开放也把一些原来不明显的工作带到了大家眼前。读者八点离开，工作人员还要把椅子收回、检查热水设备、关好门窗，到八点半才结束。两名工作人员每次各多值班两个小时，四次合起来是十六个人小时，不是每个人都多工作十六小时。读者可以帮忙排椅子，但这份帮助不能代替场馆规定的检查。组织者说，若以后想继续，既要问参加的人想不想，也要问承担这些工作的人能不能保持同样安排。|Evening opening made closing work visible. Readers left at eight; staff restored chairs, checked hot water and closed windows until eight thirty. Two staff each did two extra hours per event, totalling sixteen staff-hours over four events, not sixteen extra hours per person. Reader help didn't replace required checks. Continuing would depend on both participants' interest and staff capacity.
最后一次结束，发起活动的读者在门口碰到那个曾想借书的人。他这回带来的书已经白天借好，还把朋友一起叫来。两人坐得不算前，听到有人读一段关于离家的文字时，互相看了一眼。散场以后，他们没有说自己从此都会来，只问下个月还有没有安排。馆员说还在商量，确定了就发通知。夜晚留给读者的，不是一个已经答应永远开放的门，而是四次实在的相遇，以及能继续商量下一次的机会。|At the final event the would-be borrower returned with a book borrowed during daytime and a friend. During a passage about leaving home they glanced at each other. Afterwards they didn't promise permanent attendance, only asked about next month. Staff were still discussing it and would notify people once settled. The trial offered four real encounters and a chance to discuss another, not a promise of a permanently open door.
''')
P=rows('''
本周图书馆有两项活动，请报名时留意日期、时间和地点。周四是晚间读书活动，六点半入场，七点开始，八点结束，活动区域为一楼小厅。周六是作者见面会，下午一点半入场，两点开始，三点结束，地点也是一楼小厅。两项活动需要分别报名，周四的回复不能代替周六报名。由于地方有限，两场各有二十个名额，额满后可以留下联系方式，若有人退出，工作人员会按登记顺序联系。|Two library events require attention to dates, times and locations. Thursday reading admits at6:30,starts7,ends8 in the ground-floor room. Saturday's author meeting admits1:30,starts2,ends3 there. Register separately; Thursday confirmation doesn't cover Saturday. Each has twenty places. A waiting list will be contacted in registration order if places open.
周四活动属于晚间开放试点，本月一共安排四次，不代表图书馆每日延长开放。试点只开放一楼小厅和入口通道，二楼及其他区域不开放。常规借书、还书办理时间仍到下午六点，晚上不提供借书服务。若您计划借书，请在常规开放时间前来，或把这次到访作为参加活动的安排。已有借阅证也不表示夜间柜台有人值班，请不要因为白天办理过，就把晚间活动理解成所有服务都继续。|Thursday is one of four pilot evenings, not daily extension. Only the ground-floor room and entry passage open. Lending and returns still end at6; no evening lending service is provided. Visit during normal hours for books or attend the event only. Having a library card doesn't mean lending-counter staff are on duty in the evening or that all daytime services continue.
参加周四读书活动，可以带一本自己的书，也可以只听。想分享的人，请在周三晚八点前提交书名和一段简短介绍，现场每人先读不超过三分钟，再留时间交流。不想发言的读者无需提交介绍，报名回复里写只听即可。若已经提交而临时不方便分享，请告诉工作人员，不会因此取消您的参加资格。读者可以选择怎么参与，组织者需要提前知道分享人数，才能把结束时间安排得清楚。|For Thursday, bring a book or just listen. Speakers submit a title and short introduction by Wednesday8pm. Each initially reads no more than three minutes, followed by conversation. Listeners needn't submit an introduction; say 'listen only' in registration. If a planned speaker withdraws from speaking, notify staff; attendance isn't cancelled. Participation is optional; knowing speaker numbers helps plan the finish.
周六作者见面会不要求事先准备介绍。想问作者的问题可以在报名时提交，也可以活动现场写在纸上交给工作人员。主持人会选取与作品相关的问题，不保证每一条都在现场回答。活动结束后有十分钟签名时间，只供已报名的参加者，不另开放入场。签名时请按照工作人员安排排队，不要因为想多聊一会儿占据后面读者的时间。有关下一次活动的信息会另行通知，作者当天也不能替图书馆确认还没决定的日期。|Saturday needs no prepared introduction. Submit questions during registration or on paper at the event. The host selects work-related questions; not all are guaranteed an answer. Ten minutes for signing follow for registered attendees only. Queue as directed; longer personal conversation takes others' time. Future dates will be announced separately; the author cannot confirm undecided library arrangements.
两项活动都请提前十分钟到场核对报名信息。周四八点结束后，工作人员需要检查设备并整理场地，到八点半关闭。读者愿意帮助排椅子，可以在活动结束后问工作人员，不要自行收起仍在使用的设备。周六签名结束后也请按通知离场。提前结束讨论是为了留出实际工作时间，不表示读者可以一直留到关门前一刻。若需要无障碍座位或有其他实际需要，请报名时说明，工作人员会按现有条件回复，不会只凭一句需求就保证所有安排都能做到。|Arrive ten minutes early to check registration. Thursday ends8; staff inspect and restore the room before8:30closure. Ask before helping; don't put away equipment still in use. Leave after Saturday signing too. Closing time includes work, not permission to remain until the last moment. State accessibility or other needs when registering; staff will reply based on available arrangements rather than guarantee every request.
如需取消报名，请尽早回复确认消息，让等候的人有机会参加。不要把朋友带入而不另行登记，尤其不要把一场已经确认的名额转到另一场。通知里所说的二十个名额是参加者座位，现场工作人员另有工作位置，不占这二十个座位。试点结束后，图书馆会听取读者和工作人员的意见，再决定是否继续。请以正式通知为准；杂志里的采访帮助您了解这次尝试的故事，不能代替本周两场活动的报名确认和日期说明。|Cancel promptly so waiting people can join. Friends require separate registration; a confirmed place cannot move between events. Twenty places are participant seats; staff work positions are separate. After the pilot, staff and reader views inform continuation. Follow formal notices: the magazine interview explains the story but doesn't replace this week's registration confirmation or dates.
''')
G=[
card('一方面…，另一方面…','Organise two relevant considerations','The two sides can support or complicate a proposal; this form does not say each has equal numerical weight.','一方面读者想留下，另一方面工作人员要收尾。|Readers want to stay; staff also need to close.\n一方面场地有限，另一方面有人只想听。|Space is limited and some only want to listen.','一方面另一方面表示每边一定各占百分之五十。','一方面读者想留下，另一方面工作人员要收尾。','Parallel considerations are not measured halves.'),
card('从…来看','Frame the basis of a judgement','Name the perspective or evidence used. The judgement should stay within that basis.','从记录来看，这是六十四次到访。|The record shows sixty-four visits.\n从人员安排来看，暂时只能开四次。|Staffing permits four evenings for now.','从记录来看六十四次，说明六十四个不同的人。','从记录来看，这是六十四次到访。','A visit count is not deduplicated people.'),
card('尽管…，仍…','Retain a limit despite another fact','A concession acknowledges a fact without letting it remove the following constraint.','尽管灯还亮着，借书柜台仍然下班了。|Though the lights remain on,lending has closed.\n尽管有卡，仍要在白天办理。|Even with a card,you need daytime service.','灯亮着就说明借书柜台也值班。','尽管灯还亮着，借书柜台仍然下班了。','Lighting does not override the service-hours limit.'),
card('不仅…，也…','Add a second participant or requirement','Keep both groups when a decision concerns different responsibilities.','不仅要问读者，也要问工作人员。|Ask readers and staff.\n不仅看人数，也看收尾安排。|Consider attendance and closing duties.','只要读者同意，就不用问工作人员。','不仅要问读者，也要问工作人员。','The second required group cannot be dropped.'),
card('章 / 篇','Distinguish chapters from complete texts','章 counts chapters within a work; 篇 can count articles and other complete written pieces. They are not interchangeable in every context.','第二章写夜间开放的安排。|Chapter two describes evening arrangements.\n我读了两篇关于图书馆的文章。|I read two articles about the library.','第二章一定就是第二篇独立文章。','第二章写夜间开放的安排。','A chapter can belong to one larger work.'),
card('若…，则…','Read a formal conditional arrangement','The notice condition governs the stated follow-up. It does not assert the condition has occurred.','若有人退出，则按登记顺序联系。|If someone withdraws,contact the waiting list in order.\n若时间调整，则另行通知。|If timing changes,a separate notice follows.','写若有人退出，表示已经有人退出。','若有人退出，则按登记顺序联系。','A conditional notice is not a report of an actual withdrawal.'),
]
spec=dict(title=('The feature and the notice','采访之外的通知'),goals=['Read a feature and practical notice together','Keep visit counts,staff-hours and service conditions distinct','Summarise a dense article without losing its qualifications'],vocabulary=V,grammar=G,
dialogue=(D,[q('gist','What do the friends correct?','The headline does not make night borrowing available','The library is permanently closed','All sixty-four visits were different people'),q('detail','Which borrowing service is available at night?','None; borrowing remains daytime','All services','Only borrowing on the second floor'),q('inference','Why read the notice too?','It supplies dates and registration conditions','It removes the need to register','It guarantees permanent extension')]),
reading=(R,[q('gist','What does the feature describe?','A limited four-evening trial with real encounters and practical limits','A permanent daily full-service extension','A universal rule that readers prefer night'),q('detail','What does sixty-four count?','Visits over four evenings','Unique residents','Extra hours per staff member'),q('inference','Why retain staff feedback in the decision?','Continuing depends on the people doing closing work too','Only visitors ever do closing work','All staff have already approved permanent opening')]),
pairedTitle='This week’s registration notice',pairedReading=(P,[q('gist','How does the notice complement the feature?','It gives separate dates,registration and service limits','It contradicts the fact of a trial','It promises all questions will be answered'),q('detail','When does the Saturday meeting begin?','Two in the afternoon','Seven in the evening','One thirty in the afternoon'),q('inference','Does Thursday confirmation admit a friend on Saturday?','No,separate event and person registration are needed','Yes,the venue is the same','Yes,twenty places mean unlimited friends')]),
mediaTitle='A headline for an ordinary Thursday',media=(M,[q('detail','What did the reader mix up?','Thursday evening and Saturday afternoon notices','Two different libraries','Author and host identities'),q('inference','How should the lively headline be read?','As expressive framing,not a citywide sleep survey','As literal proof nobody sleeps','As permission to ignore dates')]),
glosses=[('阶段', 'stage; phase'),('串', 'mix up; put together'),('尤其', 'especially'),('试点','pilot programme'),('柜台','service counter'),('人次','visits or attendances with repeat people counted again'),('借阅证','library card'),('清场','clear the venue'),('额满','places filled'),('无障碍','accessible; accessibility'),('签名','sign a name'),('另行','separately'),('人手','available staff'),('值班','be on duty'),('半圈','semicircle'),('核对','check against records'),('醒目','easy to notice'),('落空','not materialise'),('不保证','not guarantee'),('自主','independent'),('去重','deduplicate'),('延期','postpone'),('名额','available place'),('柜','cabinet'),('稿','draft'),('签','sign'),('采访','interview'),('锁','lock'),('勾','tick'),('人小时','person-hours'),('办理','handle a procedure'),('薄','thin')],
place='A library foyer after reading a local magazine',context='Fictional4Thursday pilot,usual lending ends18:00.Thursday entry18:30,start19,end20,staff close20:30;Saturday entry13:30,start14,end15,10min signing.20participantplaces each,event/personregistration separate.18+20+12+14=64visits not uniquepeople;2staff×2hours×4=16staff-hours.',
turns=[('灯亮着，那我可以晚上借书吧？','Lights on means I can borrow in the evening?','Retain service distinction',['不能，晚上只办活动，借书仍到六点。']),('六十四次就是六十四个人？','Sixty-four visits means sixty-four people?','Name the counting unit',['不是，人次可能重复，单独人数没给。']),('周四有确认，我能带朋友去周六吗？','With Thursday confirmation,may I take a friend Saturday?','Read event and person scope',['要另报周六，朋友也要单独登记。']),('两人四次各两小时，每人多十六小时？','Two people,four events,two hours each means16extra per person?','Retain total staff-hours',['合计十六个人小时，每人八小时。'])],
usage=[('Ask about the intended service','今晚可以借书，还是只参加活动？','Can I borrow tonight,or only attend the event?','A useful practical question distinguishes lights from service availability.'),('Keep a notice qualification in a summary','先试四个周四，是否继续还没决定。','Four Thursdays first;continuation is undecided.','Do not erase the pilot limit to make a stronger headline.'),('Read across two materials','采访讲来由，报名要看本周通知。','The interview explains the background;registration follows this week’s notice.','Different genres serve complementary purposes.')],
tasks=practice([(R[2][0],R[2][1],'Sixty-four is a unique-person count.',False,'Repeat visits are counted.'),(R[4][0],R[4][1],'Extra staffing totals sixteen staff-hours.',True,'2people×2hours×4events.'),(P[0][0],P[0][1],'Thursday and Saturday share one registration.',False,'They need separate registration.'),(P[2][0],P[2][1],'Listening-only attendees must submit an introduction.',False,'Only planned speakers submit one.')],
[('文章说夜间试点四周。能概括成每天都开到八点吗？','Four-week evening pilot. Can it be summarised as daily8pmopening?',['不能，只是四个周四。','能，夜间等于每天。','能，标题已经承诺永久开放。'],0,'Retain the stated days and duration.'),('周六两点开始，一点半入场。几点正式开始？','Saturday2start,1:30entry. Start time?',['下午两点。','下午一点半。','晚上七点。'],0,'Entry and programme start are different.'),('两人每次各两小时，四次合计多少人小时？','Two staff,two hours each,four events. Total?',['十六个人小时。','八个人小时。','三十二个人小时。'],0,'2×2×4=16.'),('白天办借阅证，晚上是不是所有柜台都值班？','Daytime library card means all counters staffed at night?',['不是，还要看夜间服务范围。','是，有卡就能随时借。','是，亮灯就全开。'],0,'Service hours remain limited.')],
[('截至月底，共有六十四次到访。','By month end there were64visits.','截至'),('两个读者发起了晚间读书活动。','Two readers initiated evening reading.','发起'),('至于借书，还是白天办理。','Borrowing is still handled during the day.','至于'),('先确认地点，免得走错。','Confirm the place to avoid going wrong.','免得')],
[[(V[i][3],V[i][4]) for i in [0,1,2]],[(V[i][5],V[i][6]) for i in [5,8,11]],[(V[i][3],V[i][4]) for i in [14,17,20]],[(V[i][5],V[i][6]) for i in [23,26,29]],[(V[i][3],V[i][4]) for i in [27,30,31]]]),
review='Native review: feature ending, book-overtime joke, event-notice register and chapter classifier. Self-review checks64visits vs uniquepeople,2×2×4=16staff-hours/8perperson,Thursday versusSaturday dates,twenty participant seats excluding staff,optional speaking,borrowing18:00limit,and conditional continuation. Entire scenario and article are original; no actual venue or promise of accessibility is represented. Summary keeps trial scope,source and responsibilities without inserting a lecture into the friends’ chat.')
write(6,9,spec,publish='--publish' in sys.argv)
