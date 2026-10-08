"""Host a useful discussion without confusing summary, consent and assigned work."""
import sys
from advanced_core import write,rows,words,q,card,practice
V=words('''
议题|topic for discussion|chủ đề|今天的议题是活动先读书还是先听歌。|Today's topic is whether reading or music comes first.|这个议题留到下次。|Leave this topic for next time.
座谈会|discussion meeting|buổi tọa đàm|这是小范围座谈会，不是长篇报告。|This is a small discussion meeting, not a long report.|座谈会结束后还能单独提问。|Individual questions are possible after the discussion meeting.
主持人|host; facilitator|người dẫn|主持人负责让不同的人有机会说。|The host helps different people have a chance to speak.|主持人提醒大家剩下的时间。|The host reminds everyone of the time left.
发言人|spokesperson|người phát ngôn|发言人转达小组已经确认的安排。|The spokesperson conveys arrangements the group has confirmed.|发言人没有宣布未决定的事。|The spokesperson hasn't announced undecided matters.
协会|association|hiệp hội|协会愿意提供小厅。|The association is willing to provide the small room.|她加入了本地的音乐协会。|She joined the local music association.
会长|association president|chủ tịch|会长周五才能确认场地。|The president can confirm the space on Friday.|会长让大家先提交想法。|The president asked people to submit ideas first.
新人|new member; newcomer|người mới|新人也可以先听，不急着上台。|Newcomers can listen first without rushing onstage.|她带一个新人来认识大家。|She brings a new member to meet everyone.
分工|divide up work|phân công|分工要写谁做和什么时候做。|Division of work should say who does what and when.|我们先分工，再开始整理。|We divide up work before sorting.
职责|responsibility; duty|trách nhiệm|检查设备是工作人员的职责。|Checking equipment is the staff's responsibility.|这个职责不能随便交给没答应的人。|This responsibility can't simply be assigned to someone who hasn't agreed.
协调|coordinate|phối hợp|我来协调两组的时间。|I'll coordinate the two groups' times.|她协调了场地和人员安排。|She coordinated venue and staffing arrangements.
承诺|promise|cam kết|还没问过场地，就不能承诺日期。|Without checking the venue,we can't promise a date.|她承诺周五前回复。|She promised to reply by Friday.
派出|send; dispatch|cử|协会派出两个人帮助布置。|The association sends two people to help set up.|小组派出一人去核对设备。|The group sends one person to check equipment.
区分|distinguish|phân biệt|先区分建议和已经同意的事。|First distinguish suggestions from agreed matters.|这两种情况要区分。|These two situations need distinguishing.
提升|raise; improve|nâng cao|我们想提升听歌时的体验。|We want to improve the listening experience.|新安排提升了参加的便利性。|The new arrangement made participating more convenient.
听取|hear and consider|lắng nghe|先听取还没开口的人的意见。|First hear those who haven't spoken yet.|她愿意听取相反的看法。|She is willing to hear opposing views.
提交|submit|nộp|会后可以提交补充意见。|Additional views can be submitted after the meeting.|请把确认过的名单提交给工作人员。|Please submit the confirmed list to staff.
留言|leave a message|để lời nhắn|她留言说不能负责周六布置。|She left a message saying she can't set up on Saturday.|有问题先留言，我晚点回复。|Leave a message with questions;I'll reply later.
回应|respond|phản hồi|我先回应时间的问题。|I'll respond to the timing question first.|他没有马上回应这个建议。|He didn't immediately respond to this suggestion.
探讨|discuss in depth|thảo luận|音量的问题需要单独探讨。|Volume needs a separate discussion.|我们想探讨更合适的安排。|We want to discuss a more suitable arrangement.
至于|as for|còn về|至于节目单，我来整理。|As for the programme,I will organise it.|至于费用，等确认以后再说。|Costs can wait until confirmation.
再说|besides; discuss later|hơn nữa|先确认房间，买东西以后再说。|Confirm the room first;discuss purchases later.|再说，设备也还没检查。|Besides,the equipment hasn't been checked yet.
凡是|all those that; whenever|tất cả|凡是上台的人，都先确认自己的时间。|Everyone going onstage should confirm their timing first.|凡是改过的安排，都写进消息里。|Put every changed arrangement in the message.
若|if; formal conditional|nếu|若小厅不能用，就改期。|If the room is unavailable,we'll reschedule.|若人数增加，请提前联系。|Contact us beforehand if attendance grows.
只得|have no choice but|đành|场地没确认，我们只得先等。|With the venue unconfirmed,we have to wait.|她赶车，只得提前离开。|She has to leave early for her bus.
不便|inconvenient|bất tiện|周六上午对她不便。|Saturday morning is inconvenient for her.|现在不便长谈，晚点再说。|A long talk is inconvenient now;let's talk later.
能否|whether possible|liệu có thể|能否安排两次演奏，还没确定。|Whether two performances are possible is undecided.|请确认能否提前进场。|Please confirm whether we may enter early.
切实|practical; effective|thiết thực|先解决切实的问题。|First address the practical issues.|这个办法切实可行。|This approach is workable.
最终|final; ultimately|cuối cùng|最终顺序还要等周五确认。|The final running order waits for Friday's confirmation.|他们最终同意先试一次。|They ultimately agreed to try once first.
占据|take up; occupy|chiếm|别让一个问题占据全部时间。|Don't let one question take all the time.|设备占据了桌子的一半。|The equipment occupies half the table.
打断|interrupt|ngắt|我打断一下，先确认你说的是哪天。|Let me interrupt briefly to confirm which day you mean.|她没打断，让朋友把话说完。|She let her friend finish without interrupting.
笑声|laughter|tiếng cười|笑声过后，我们继续讨论时间。|After the laughter,we returned to timing.|隔壁传来一阵笑声。|Laughter came from next door.
掌声|applause|tiếng vỗ tay|掌声表示喜欢，不一定表示同意分工。|Applause shows appreciation,not necessarily agreement to duties.|演奏结束后响起掌声。|Applause followed the performance.
''')
D=rows('''
今天先聊顺序，四十分钟够不够？|Shall we focus on running order today? Is forty minutes enough?
够。场地和设备另有两个人去问。|Yes. Two others will check the venue and equipment.
那先读书还是先听歌？|Reading or music first then?
我想先听歌，大家比较容易坐下来。|Music first might help people settle.
我倒想先读。歌结束以后有人要赶车。|I'd prefer reading first. Some leave after the music for a bus.
你说的是演奏的人，还是听的人？|Do you mean performers or listeners?
演奏的，两个人八点以后不便留下。|Performers—two can't stay after eight.
那得把他们的时间先留出来。|Then we need to reserve their time first.
我补一句，先听歌也不一定非得全听完。|One thing:music first needn't mean all of it at once.
分成两段？|Split it into two parts?
对，一首开头，一首后面。|Yes,one song at the start and another later.
这个可以试，不过先问演奏的人愿不愿意。|Worth trying,but first ask whether the performers want that.
我能联系他们，周五前回复。|I can contact them and reply before Friday.
谢谢。那节目单先别写成已经确定。|Thanks. Let's not call the programme confirmed yet.
你今天终于没替我答应周六早起。|Finally you didn't agree to an early Saturday for me.
记住了，你的闹钟归你管。|I've learned—your alarm is your business.
还有人想补充顺序吗？|Anyone else want to add something about running order?
我只听。现在还不知道会不会上台。|I'm just listening.I don't yet know whether I'll go onstage.
好，愿意的时候再告诉我们。|Fine,tell us when you want to.
音量要不要现在聊？|Should we discuss volume now?
只剩五分钟，先记下来，下次单独聊。|Five minutes left.Let's note it for a separate discussion.
我把已答应的分工念一遍，你听有没有漏。|I'll read agreed duties back;check if I missed anything.
念吧，没答应的别替我们加上。|Go ahead.Don't add duties we haven't agreed to.
放心，今天只替你保住了闹钟。|Don't worry—today I only protected your alarm.
''')
M=rows('''
你刚才鼓掌，我以为你同意了。|You applauded.I thought you agreed.
我是觉得那首歌好，不是答应搬桌子。|I liked the song.I didn't agree to move tables.
那我把名单改一下。|Then I'll change the list.
你先问我哪天有空。|Ask which day I'm free first.
周六早上？|Saturday morning?
不行，下午两点以后可以。|No.After two in the afternoon works.
那只排你两点以后。|Then I'll schedule you only after two.
还要问做什么。|You still need to ask what I'll do.
搬四把椅子，不搬桌子。|Move four chairs,not tables.
行，这次可以鼓掌了。|Okay.Now we can applaud.
给椅子鼓掌？|For the chairs?
给你终于问清楚了。|For you finally asking properly.
''')
R=rows('''
我第一次主持小组讨论时，以为把每个人的话都记下来就够了。讨论结束，纸上写满想法，我很满足，直到周六有人问为什么名字出现在布置名单上。她只是在听到一个节目建议时点头，并没有答应上午来。我翻记录，发现自己把她可以帮忙的那句，跟旁边另一个人的周六上午连在一起了。她不是临时反悔，而是我把两段不同的话记成一件已经确定的事。那次以后，我会在散会前念一遍谁答应做什么。|At my first meeting,I thought recording every idea was enough.I left satisfied until someone asked why she'd been listed for Saturday setup.She had nodded at a programme suggestion,not agreed to come that morning.I had joined her offer to help with someone else's Saturday timing.She hadn't changed her mind;I'd combined separate remarks.From then on I read agreed duties back before ending.
这次协会愿意借小厅给我们办读书和听歌活动，日期还得等会长周五确认。我先把今天的议题缩到节目顺序，场地和设备由两个人另外联系。讨论安排四十分钟，我把剩下时间写在纸角上，免得自己一开口就忘了。大家一开始意见相反，有人想先听歌，让陌生人容易坐下来；有人想先读，因为两位演奏者八点以后不能留。我没有马上挑一个顺耳的，而是先问到底是谁需要早走。|The association offered a small room,but the president couldn't confirm the date until Friday.We focused today's forty-minute meeting on running order.Two people would check venue and equipment separately.I noted time left.People differed:music first to settle newcomers,reading first because two performers couldn't stay after eight.Rather than pick the proposal I liked,I clarified whose time was limited.
把演奏者和听众分清以后，另一个朋友说能不能把歌分成两段，开头一首，后面一首。这句话让我们看到并不只有两种整块交换的安排。可是现场喜欢这个想法，不等于演奏者已经同意，更不等于设备能随时开关。陈宇答应去问两个人愿不愿意，周五以前回复。我们把这个任务写在确认栏，节目顺序仍放在待定栏。小周问周四几点能知道，陈宇说下午六点前，晚饭的时候再一起看。我们先各自去问需要的人，没有坐着等一个现在还没人能给的答案。|Once we distinguished the performers from the audience, a friend suggested one song at the start and another later. This offered more than swapping two whole blocks. Our liking it did not mean the performers had agreed or that the equipment could be switched at any time. Chen Yu would ask both performers and reply before Friday. We wrote his task under confirmation and left the running order undecided. Xiao Zhou asked what time on Thursday. Chen Yu said before six; we could look at the answer over dinner. We went to ask the people involved instead of waiting for an answer no one could give yet.
有位新人一直没说话。我问全场还有没有人想补充，她说先听，还不知道会不会上台。我说好，愿意的时候再告诉我们，就继续听别人的意见。她散会后走过来，说自己带了一小段文字，但不想当着所有人试读。我陪她在门边读了一遍，才问要不要先发给负责节目的朋友。她想了想说可以，但别先写名字上台。这是一个比会议里点头更明确的答复，也仍然只允许分享文字，不允许替她决定公开朗读。|A quiet newcomer said she wanted to listen and didn't know whether she'd perform.I accepted that.Afterwards she privately showed a short text and didn't want to try it before everyone.We read it by the door.She allowed sending it to the programme organiser,but not listing her for the stage.That clear answer permitted sharing the text,not deciding on public reading for her.
快结束时有人想谈音量，另一个人又开始讲上回什么设备不好。只剩五分钟，我打断了一下，先说这个问题值得单独谈，再请他们把具体情况发给负责设备的人。打断不是因为问题不重要，而是已经约好的时间也需要有人守住。我们用最后几分钟念确认过的分工，提醒场地和最终顺序等周五回复。有人改了一处，原来他答应的是下午帮四把椅子换位置，不是上午搬所有桌子，我当场改掉。|With five minutes left,volume led into equipment complaints.I interrupted,said it deserved separate discussion and asked for details to the equipment contact.The interruption protected agreed time,not dismissed the issue.We used the remaining minutes to read confirmed duties and note Friday decisions.Someone corrected his task:four chairs in the afternoon,not all tables in the morning.I changed it immediately.
散会后我发了一条很短的消息，没有把整张记录直接贴出去。消息先列已经确认的联系人和回复时间，再列还待确认的场地与顺序，最后放补充意见的方式。有朋友回复一个鼓掌的表情，我笑着回谢谢，这次不把掌声算成搬桌子的报名。她马上又发一条，说周六下午真的可以帮。我们这才问清具体时间和事情，把名字加到新的名单里。会议没有得到所有人同意所有事，却让需要做的下一步有了人，也让还没决定的地方留在原处。|My short follow-up listed confirmed contacts and reply times,then undecided room and order,and how to add views.An applause emoji prompted my joke that I wouldn't count it as volunteering for tables.She then genuinely offered Saturday-afternoon help.We clarified the task and time before adding her.The meeting didn't secure everyone's consent to everything,but gave the next steps owners while leaving undecided matters undecided.
''')
P=rows('''
我原本不想去今天的讨论，因为上次只是帮忙提了一句建议，最后就被安排周六一早去搬东西。后来主持人道歉，改掉名单，我知道她不是故意的，可下一次听到要开会，还是先想起那张纸。林安跟我说这回散会前会念确认过的分工，没答应的事情不会直接加进去。我才决定去看看，而且先在群里留言，周六上午不便参加，下午两点以后可以考虑，具体要做什么再问我。|I hesitated about today's meeting because a suggestion last time had become an early Saturday moving duty.The host apologised and corrected it,but I still remembered that list.Lin An said duties would now be read back.I went,and first messaged that Saturday morning didn't work;after two might,depending on the task.
今天讨论节目先后，我先说想把读书放前面。两位演奏者八点以后要走，我怕大家读得长，他们的时间就只剩一点。我没有说全体听众都要早走，主持人问清是谁以后，把这点记成演奏安排的条件。有人建议先一首、后面一首，我觉得比我原先只想交换两块更好。这时我点了点头，是赞成把建议拿去问，不是已经知道两位朋友一定愿意。陈宇说去联系，我就等他的回复，不替别人把同意补出来。|I preferred reading first because two performers had to leave after eight.The host clarified that I meant performers,not all listeners.Splitting music into opening and later songs seemed better than my block swap.I nodded in support of asking,not as proof the performers would agree.Chen Yu would contact them;I waited rather than supply their consent.
中间有个新人一直听，我本来差点问她怎么不说，后来想起自己有时也要先弄明白大家在聊什么。主持人给全场一个补充的机会，没有点她名字，她说先听。那之后她坐得明显放松些，还在纸上记了两句。沉默的人并不都需要别人马上把话递到嘴边，留一个能自己走进来的入口，有时比当众让她解释为什么不说更舒服。她散会后留下来找林安，我先走了，不知道两人后来谈了什么。|A newcomer listened quietly.I nearly asked why,but remembered sometimes I need to understand first.The host invited additions without naming her;she chose listening and relaxed,scribbling notes.An opening someone can choose may be more comfortable than demanding an explanation for silence.She stayed to talk to Lin An.I left and don't know their later conversation.
我比较在意音量，听说要留到下次，起初觉得自己的问题又被推开了。主持人没有只说时间不够，而是明确请我把上次设备的情况发给联系人，下一次单独谈。我把发生在哪首歌、坐在哪边、声音怎样写下来，觉得比现场一口气说所有设备都不好更有用。她也没有承诺一定换新设备，只说先核对。我能接受先弄清楚再决定，不能接受没有人接着管；这次至少知道把消息发给谁。|I cared about volume and initially felt postponed again.The host named a contact and a separate discussion.I wrote which song,where I sat and what the sound was like,more useful than condemning all equipment.She promised checking,not new equipment.I could accept checking before deciding,so long as someone owned the next step.Now I knew whom to message.
最后念分工时，有人把我的下午两点以后听成上午两点，我差点笑出声。大家看了一眼日期和时间，把它写成周六下午，任务也从搬桌子改成移动四把椅子。我说这样可以，主持人才在我的名字后面画上确认。那个动作很小，却让我知道这次不需要回家以后再纠正一张已经发到群里的名单。别人不必猜我有没有在生气，我也不必用越来越硬的语气保护一个原本就没答应的早起安排。|At readback,someone misheard after two in the afternoon as two in the morning.We checked date and time,and changed the task to four chairs.I agreed before the host marked it confirmed.A small act saved me from correcting a published list later,and from sounding increasingly sharp to protect a morning I'd never promised.
会后我给消息回了个鼓掌的表情，主持人拿上次的误会开玩笑，说这次不把掌声算成搬桌子的报名。我觉得能这样笑，说明我们已经把问题放到能处理的位置。之后我正式回复下午可以帮四把椅子，若场地周五确认不了，就先不安排。音乐顺序仍没定，下一次也可能有新问题，但我没有像上次一样只想退出。愿意再来，不是因为每个意见都照我的做，而是因为我的时间、建议和真正答应的工作，这回终于分开记了。|I sent applause,and the host joked it wouldn't count as volunteering for tables.We could laugh because the problem was now manageable.I confirmed four chairs in the afternoon,conditional on Friday venue confirmation.The music order was still undecided.I wanted to return not because every idea went my way,but because my time,my suggestion and my actual agreed work had been recorded separately.
''')
G=[
card('凡是…，都…','State a rule with a defined group','凡是 selects a group; 都 applies the rule to its members,not everyone present.','凡是上台的人，都先确认时间。|All performers confirm timing first.\n凡是改过的安排，都写进消息。|Include all changed arrangements.','凡是上台的人都确认，表示所有听众都必须上台。','凡是上台的人，都先确认时间。','The group is performers,not all attendees.'),
card('与其…，不如…','Offer a preferred alternative','This comparison states a preference; it does not establish that others have consented.','与其临时赶人，不如先写清结束时间。|Better state the finish than hurry people out later.\n与其猜她有空，不如先问。|Better ask than guess her availability.','说不如先问，表示她已经答应。','与其猜她有空，不如先问。','A proposed action is not its result.'),
card('不是…，而是…','Correct the category of an answer','Use an explicit contrast when appreciation has been misread as consent.','我不是答应搬桌子，而是想谢谢演奏的人。|I liked the song;I was thanking performers,not agreeing to move tables.\n这是待确认的建议，不是已经确定的顺序。|This is a pending suggestion,not confirmed order.','鼓掌就是答应所有分工。','这是待确认的建议，不是已经确定的顺序。','Keep appreciation and accepted work distinct.'),
card('先…，再…','Preserve the order of checking and announcing','Confirmation precedes listing a person or publishing an arrangement.','先问时间，再写名字。|Ask timing before adding a name.\n先确认场地，再发最终节目单。|Confirm the room before the final programme.','先发最终节目单，再问场地，跟原顺序一样。','先确认场地，再发最终节目单。','Reversing dependencies changes the arrangement.'),
card('若…，就…','Keep an action conditional','A formal condition may introduce an ordinary 就 consequence. The condition is not assumed true.','若小厅不能用，就改期。|If the room is unavailable,reschedule.\n若周五没确认，就先不安排。|If unconfirmed Friday,do not schedule yet.','若没确认就不安排，表示现在已经确认了。','若周五没确认，就先不安排。','The condition does not report confirmation.'),
card('至于… / 免得…','Move topics and give a practical prevention purpose','至于 shifts topic; 免得 introduces what the action is intended to prevent,not a guaranteed outcome.','至于节目单，我来整理。|As for the programme,I will organise it.\n把时间念一遍，免得记错。|Read the time back to reduce mistakes.','写免得记错，证明之后绝不会出错。','把时间念一遍，免得记错。','An intended prevention does not guarantee perfect results.'),
]
spec=dict(title=('Keep the next step clear','让讨论有下一步'),goals=['Facilitate a discussion with useful time boundaries','Read back consent and tasks without assigning unaccepted work','Compare a host’s and participant’s accounts'],vocabulary=V,grammar=G,
dialogue=(D,[q('gist','What does the meeting establish?','Who checks the proposal and when,with final order still pending','A permanently confirmed programme','Mandatory speaking for newcomers'),q('detail','When does Chen Yu promise a reply?','Before Friday','After the Saturday show','Immediately without contacting anyone'),q('inference','Why postpone volume to a named contact?','To preserve agreed time while keeping a next step','To dismiss volume as unimportant','To guarantee brand-new equipment')]),
reading=(R,[q('gist','What does the host change after a mistaken list?','Read agreed duties back and keep pending matters separate','Treat every nod as consent','Publish all notes without checking'),q('detail','What does the newcomer permit?','Sharing her text privately,not listing her for stage','A guaranteed public performance','Changing the venue'),q('inference','Why is laughter possible in the follow-up?','The earlier mistake has been acknowledged and tasks clarified','Nothing ever went wrong','Applause now automatically volunteers everyone')]),
pairedTitle='A participant decides to come back',pairedReading=(P,[q('gist','Why does the participant want to return?','Time,suggestions and accepted work are separately respected','Every opinion was adopted','No disagreement remained'),q('detail','What setup work is agreed?','Four chairs after two Saturday afternoon,subject to room confirmation','All tables Saturday morning','Two chairs Friday evening'),q('inference','Does the participant know the newcomer’s private later conversation?','No;they had already left','Yes;they witnessed everything','Yes;a quiet person must have agreed to perform')]),
mediaTitle='What applause does not volunteer',media=(M,[q('detail','What does the friend actually agree to move?','Four chairs after two','All tables in the morning','The stage at midnight'),q('inference','What repairs the misunderstanding?','Ask both time and task before listing a name','Treat an emoji as blanket consent','Ignore the list')]),
glosses=[('顺耳', 'pleasant to hear'),('纠正', 'correct a mistake'),('待定','undecided'),('转达','convey'),('布置','set up'),('麦克风','microphone'),('名册','name list'),('反悔','go back on an agreement'),('确认栏','confirmation column'),('待定栏','pending column'),('闹钟','alarm clock'),('表格','table; form'),('记录','record'),('同意','agree'),('鼓掌','applaud'),('签','sign'),('音量','volume'),('陌生人','stranger'),('核对','check'),('节目单','programme'),('散会','end a meeting'),('插','insert'),('默契','mutual understanding'),('栏','column'),('催','urge'),('语气','tone'),('硬','firm; hard'),('退出','withdraw'),('设备','equipment')],
place='A small music-and-reading association meeting',context='40minute meeting about running order only;venue/date pending president Friday;two performers cannot stay after20:00. Split-song proposal requires performer consent. Chen Yu contacts/replies beforeFriday. Setup volunteer accepts4chairs after14Saturday conditional room. Newcomer permits private text sharing,not public stage. Equipment contact owns volume follow-up.',
turns=[('她鼓掌了，就排她周六早上搬桌子？','She applauded,so schedule Saturday-morning tables?','Separate appreciation from consent',['先问时间和任务，鼓掌不算答应。']),('一首开头一首后面，就直接发节目单？','A song each end—publish now?','Retain dependency',['先问演奏的人，再等场地确认。']),('那个新人没说话，要不要点名让她讲？','A newcomer is quiet;call on her?','Offer without pressure',['可以问谁想补充，不必点名，她可以只听。']),('没时间聊音量，是不是就不管了？','No time for volume means ignore it?','Name a next step',['留给设备联系人单独讨论，说明谁接着处理。'])],
usage=[('Interrupt with a purpose','我打断一下，先确认你说的是哪天。','Let me interrupt briefly to confirm the day.','Explain the brief intervention rather than claim the issue is unimportant.'),('Read consent back','周六下午两点以后，移动四把椅子，对吗？','After two Saturday afternoon,four chairs,right?','Specific readback catches mismatched time and task.'),('Distinguish a pending proposal','这个值得试，但还要问演奏的人。','Worth trying,but we still need to ask the performers.','Positive evaluation does not provide somebody else’s consent.')],
tasks=practice([(R[0][0],R[0][1],'The earlier volunteer had promised Saturday morning and then changed her mind.',False,'The host wrongly combined remarks.'),(R[3][0],R[3][1],'The newcomer permits private text sharing but not a stage listing.',True,'Consent scope is explicit.'),(P[3][0],P[3][1],'The host promises to replace all equipment.',False,'Checking,not replacement,is promised.'),(P[4][0],P[4][1],'The participant agrees to all tables in the morning.',False,'Four chairs after two afternoon.')],
[('小厅周五确认，节目单现在能写最终吗？','Room confirmation Friday.Can the programme now say final?',['不能，等确认再发。','能，有人喜欢就算确认。','能，鼓掌已经代替场地回复。'],0,'Venue confirmation is still pending.'),('她只许把文字给联系人，能列上台名单吗？','She permits sharing text with a contact.Can she be listed for stage?',['不能，公开朗读要另问。','能，发文字就自动上台。','能，沉默表示答应。'],0,'Private sharing is limited consent.'),('四十分钟只剩五分钟，音量有联系人。怎么处理？','Five of forty minutes left,volume has a contact.What next?',['记下来交联系人，最后核对分工。','宣布音量永远不用管。','保证马上换全部设备。'],0,'Keep a concrete follow-up and readback.'),('说周六下午两点以后搬四把椅子，哪项符合？','Which fits four chairs after2Saturdayafternoon?',['下午两点半移动四把椅子。','上午九点搬全部桌子。','周五凌晨两点搬四把椅子。'],0,'Both day,time and task match.')],
[('凡是改过的安排，都写进消息里。','Include every changed arrangement.','凡是'),('她承诺周五前回复。','She promised a reply beforeFriday.','承诺'),('我打断一下，先确认你说的是哪天。','Let me interrupt to confirm the day.','打断'),('至于节目单，我来整理。','As for the programme,I will organise it.','至于')],
[[(V[i][3],V[i][4]) for i in [0,1,3]],[(V[i][5],V[i][6]) for i in [6,8,11]],[(V[i][3],V[i][4]) for i in [14,16,18]],[(V[i][5],V[i][6]) for i in [20,22,25]],[(V[i][3],V[i][4]) for i in [28,30,31]]]),
review='Native review: chair/applause/alarm banter, gentle interruption,the self-correcting host narrative and formal association terms. Self-review separates nod/applause from task consent,private text from stage consent,performer from audience timing,40minute scope/5minute closing,Friday conditional venue and Saturday14:00+fourchairs. No invented agreement or native certification. Participants retain distinct information; useful facilitation does not mean every opinion wins.')
write(6,10,spec,publish='--publish' in sys.argv)
