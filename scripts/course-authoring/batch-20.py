"""Editorial source: a delivery, exceptions, agreement and a chat joke."""
from common import *
from editorial import unit
character_groups.update({
's3-u21':[('被','passive marker; cover'),('挂','to hang'),('解','to untie; resolve'),('紧','tight'),('旧','old; used'),('衬','to line; shirt component'),('裤','trousers')],
's3-u22':[('除','to exclude; remove'),('播','to broadcast; sow'),('媒','medium; intermediary'),('类','kind; category'),('界','boundary; world'),('众','many; crowd'),('式','form; style')],
's3-u23':[('防','to prevent; guard'),('范','pattern; model'),('止','to stop'),('议','to discuss'),('及','to reach; and'),('制','system; to make'),('危','danger')],
's3-u24':[('哈','laughter syllable'),('精','fine; spirit'),('神','spirit; expression'),('速','speed'),('演','to perform'),('突','sudden; protrude'),('烈','intense')],
})
selected_source_rows.update({'s3-u21:把':'75','s3-u21:被':'288','s3-u21:叫':'4108'})
unit_glosses.update({'s3-u21':{'衣架':'clothes hanger','椅子':'chair','收件人':'recipient','交给':'to hand to','弄湿':'to get wet','绳子':'rope; cord','外套':'coat','袖子':'sleeve','袋子':'bag','领口':'collar opening','签收':'to sign for receipt','打包':'to pack','被弄湿':'to be made wet (passive expression)','结果':'result','处置':'handling; disposal'}})
dictionary.update({'解开':'jiě kāi','被子':'bèi zi','衬衫':'chèn shān','衬衣':'chèn yī','皮包':'pí bāo','紧':'jǐn'})
unit_glosses['s3-u21']['单独']='separately; alone'
u='s3-u21'
unit(u,'请把它放在门边',[
'Specify where a known object should be put','Distinguish an agent’s handling from an affected object’s experience','Name the resulting state rather than merely the action'],[
('把','object-disposal marker','dấu hiệu đưa tân ngữ lên trước','preposition','请把这件衣服放在椅子上。','Please put this item of clothing on the chair.'),
('被','passive marker','dấu hiệu bị động','preposition','袋子被雨弄湿了。','The bag was made wet by rain.'),
('叫','colloquial passive marker','dấu hiệu bị động khẩu ngữ','preposition','这张纸叫雨弄湿了。','This sheet of paper was made wet by rain.'),
('房东','landlord','chủ nhà','noun','房东说包裹可以先放门边。','The landlord says the parcel can be left by the door first.'),
('房屋','house; building','nhà ở','noun','这张纸写的是房屋地址。','This paper gives the building address.'),
('房租','rent','tiền thuê nhà','noun','房租和这次快递的费用分开付。','Rent and this delivery’s charge are paid separately.'),
('订','to order; book','đặt','verb','我订了衣架，还没收到。','I ordered clothes hangers but have not received them.'),
('放到','to put at or into','đặt vào; đặt tới','verb','把书放到书架上。','Put the book on the bookcase.'),
('挂','to hang','treo','verb','先挂好外套，再打开包裹。','Hang the coat properly before opening the parcel.'),
('解开','to untie; undo','tháo; cởi','verb','把绳子解开，再看里面。','Untie the cord before looking inside.'),
('紧','tight','chặt','adjective','绳子太紧，先别拉。','The cord is too tight; do not pull yet.'),
('旧','old; used','cũ','adjective','旧衣服也要分清是谁的。','Identify whose used clothes they are too.'),
('书架','bookcase; bookshelf','giá sách','noun','书架前面不要放袋子。','Do not put bags in front of the bookcase.'),
('沙发','sofa','ghế sô pha','noun','沙发上还有两个包。','There are still two bags on the sofa.'),
('被子','quilt; blanket','chăn','noun','被子还在袋子里。','The quilt is still in the bag.'),
('裤子','trousers','quần','noun','这条裤子是她的。','These trousers belong to her.'),
('衬衫','shirt','áo sơ mi','noun','把衬衫挂好，别放地上。','Hang up the shirt; do not put it on the floor.'),
('衬衣','shirt; undershirt','áo sơ mi; áo lót','noun','这件衬衣的袖子太长。','This shirt’s sleeves are too long.'),
('上衣','upper-body garment','áo','noun','上衣放在左边的袋子里。','The top is in the bag on the left.'),
('裙子','skirt','váy','noun','裙子和裤子放在不同袋子里。','The skirt and trousers are in different bags.'),
('皮包','leather bag','túi da','noun','皮包不是这个包裹里的东西。','The leather bag is not an item in this parcel.'),
('皮','skin; leather','da','noun','这张卡写着皮，不是布。','This card says leather, not cloth.')],
[grammar(u,'三27','把 / 被 / 叫 / 让','Separate the actor and the affected object',
'把 introduces a known object that the subject handles: 我把衣服挂好了. 被 introduces the agent of a passive event: 衣服被雨弄湿了; the agent may be omitted with 被. 叫 and 让 can also introduce a passive agent in colloquial speech: 衣服叫雨弄湿了 / 衣服让雨弄湿了. These passive uses require an agent and differ from 叫/让 meaning ask or allow. Do not infer the cause or actor from a bare changed state.',[
('我把衣服挂好了。','I have hung up the clothes properly.'),('衣服被雨弄湿了。','The clothes were made wet by rain.'),('衣服叫雨弄湿了，也可以说衣服让雨弄湿了。','One can colloquially say the clothes were made wet by rain using either 叫 or 让.')],
('衣服叫弄湿了。','衣服被弄湿了。','For this agentless passive, use 被. With colloquial passive 叫/让, state the agent.')),
grammar(u,'三54','把 + 已知物 + 处所 / 接收者 / 结果','Give the full handling instruction',
'Use a known or specified object, then a predicate describing its placement, transfer or changed state. Placement: 把包裹放在门边 / 放到门边. Transfer: 把这本书交给她. Result or direction: 把绳子解开 / 把箱子搬进去. The action alone in 请把书放 is incomplete here. Negation and modal verbs precede 把: 不要把衣服放地上; 可以把书交给她.',[
('请把包裹放在门边。','Please put the parcel by the door.'),('把这本书交给她。','Hand this book to her.'),('不要把绳子拉紧，先把它解开。','Do not tighten the cord; untie it first.')],
('请把这本书放。','请把这本书放到书架上。','State the intended placement or other result in this handling instruction.'))],
('The parcel has a recipient','Find where the parcel should go and what has happened to the bag.',[
('你订的包裹到了，放哪里？','Your ordered parcel has arrived; where should I put it?'),
('请把包裹放在门边，别放沙发上。','Please put the parcel by the door, not on the sofa.'),
('房东说先放这里，房屋地址没错吧？','The landlord said to leave it here first; the building address is correct, right?'),
('没错。房租另付，不在这次快递费用里。','Correct. Rent is paid separately and is not part of this delivery charge.'),
('袋子被雨弄湿了，里面的被子呢？','The bag got wet in the rain; what about the quilt inside?'),
('先把绳子解开看看。绳子很紧，别直接拉。','Untie the cord and check first. It is tight; do not just pull.'),
('那我把书交给你，你看衣服。','Then I will hand the book to you, and you check the clothes.'),
('好，书放到书架上，衣服再分开。','Okay; put the book on the bookcase and separate the clothes next.')],
[('mainidea','What is being coordinated?',['A delivery’s placement and checking','Paying everyone’s rent together','Choosing a new apartment'],0),('detail','Where should the parcel be left?',['By the door','On the sofa','On the floor outside the building'],0),('inference','Is the quilt certainly wet?',['No; only the bag is known to be wet','Yes, every item is wet','No; the quilt is confirmed dry'],0)],[],True),
('Open before guessing','Distinguish the known bag condition from the items still being checked.',[
('包裹到了，房东让我们先放在门边，房屋地址已经核对。','The parcel arrived; the landlord asked us to leave it by the door, and the building address has been checked.'),
('房租单独付，不能把订衣架的费用当房租。','Rent is paid separately; the charge for ordering clothes hangers is not rent.'),
('袋子被雨弄湿了；口语里也有人说叫雨弄湿了、让雨弄湿了。','The bag was made wet by rain; colloquially some also use 叫 or 让 to introduce rain as the cause.'),
('绳子很紧，要先解开，不能只看袋子就说被子也湿了。','The cord is tight and needs untying first; seeing the bag alone does not establish that the quilt is wet too.'),
('书放到书架上，旧上衣先从沙发上拿下来。','Put the book on the bookcase and take the used top off the sofa first.'),
('衬衫和衬衣挂好，裙子跟裤子放在两个袋子里。','Hang up the shirts and put the skirt and trousers in separate bags.'),
('这张卡写着皮，皮包还没找到，不要把布袋当皮包。','The card says leather; the leather bag has not been found, so do not mistake the cloth bag for it.'),
('把物品交给收件人以前，先问清楚，不替别人签收。','Clarify before handing items to the recipient; do not sign for someone else without asking.')],
[('mainidea','What does the note prioritize?',['Checking before inferring the parcel contents’ condition','Assuming every item is damaged','Using the rent bill as a clothing label'],0),('detail','Which condition is directly known?',['The outer bag is wet','The quilt is wet','The leather bag is missing forever'],0),('inference','Does the material label prove the cloth bag is leather?',['No','Yes','Only when placed on the sofa'],0)],[(4,'书架'),(5,'裤子')],False),
('A sofa is not a parcel shelf','Read an original scene about a misplaced delivery.',[
('我把包裹放好了。','I have put the parcel down properly.'),('在哪儿？','Where?'),('沙发上，坐着正好看。','On the sofa; one can look at it while sitting.'),('先把包裹搬下来。沙发没有订衣架。','Move the parcel off first. The sofa did not order clothes hangers.')],
[('inference','Why is the parcel moved?',['The sofa is needed for sitting','The sofa signed for it','All its contents are wet'],0)],[],True),
dict(tf=[('把','把包裹放在门边，不放沙发上。','Put the parcel by the door, not on the sofa.','The instructed location is by the door.',True,'The contrast gives the intended location.'),('被','袋子被雨弄湿了，里面还没看。','The bag was made wet by rain; the inside has not been checked.','Every item inside is definitely wet.',False,'The inner condition is unknown.')],
reply=[('放到','书放哪里？','Where should the book go?',['放到书架上。','房租先放晴天。','把书放。'],0,'Specify the location after the handling verb.'),('紧','绳子太紧，先做什么？','What comes first when the cord is too tight?',['先解开。','替所有人签收。','把沙发当地址。'],0,'Undo the cord first.')],
fill=[('挂','把衬衫挂好。','Hang up the shirt properly.'),('皮包','皮包还没找到。','The leather bag has not been found yet.')],
match=[('房租',[('房租另付。','Rent is paid separately.'),('书交给她。','Hand the book to her.'),('袋子被雨弄湿了。','The bag was made wet by rain.')]),('裙子',[('裙子和裤子分开放。','Keep the skirt and trousers separate.'),('先把绳子解开。','Untie the cord first.'),('衣架还没收到。','The clothes hangers have not been received yet.')])]),
[('Specify a result','请把它放在门边。','Please put it by the door.','A precise placement request avoids guessing.'),('Check first','里面还没看，先别说都湿了。','The inside has not been checked; do not say it is all wet yet.','Distinguish a known observation from an inference.')],
[('放哪里？','Where should it be put?','Name the intended location',['放在门边。']),('里面也湿了吗？','Is the inside wet too?','State the uncertainty',['还没看，先打开看看。'])],
'Native check: colloquial passive 叫/让 with rain as agent, 衬衫 versus 衬衣 overlap by region, 皮 as material noun, natural delivery and landlord register, and the personified-sofa joke. No permission to sign for another person is inferred. Native review pending.')

unit_glosses['s3-u22']={'播出':'to broadcast','节目':'programme','方式':'method; way','世界':'world','区别':'difference; to distinguish','除外':'excepted','画面':'picture; visual image','文字':'written words','联合':'joint; to unite','开会':'to hold a meeting','线上':'online','声音':'sound; voice','爱好':'hobby','民族':'ethnic group','经历':'experience'}
u='s3-u22'
unit(u,'除了我，大家都来吗',[
'Distinguish excluding one member from adding another activity','State the scope of 都 after an exception','Compare media habits without generalizing about a whole population'],[
('除了','except for; besides','ngoại trừ; ngoài ra','preposition','除了我，大家都看过这个节目。','Everyone except me has watched this programme.'),
('普遍','widespread; common','phổ biến','adjective','这个爱好很普遍，但不是人人都有。','This hobby is common, but not everyone has it.'),
('类','kind; category','loại','noun','你喜欢哪一类节目？','What kind of programme do you like?'),
('类似','similar','tương tự','adjective','两个节目类似，不等于内容相同。','The two programmes are similar, not identical in content.'),
('区别','difference; to distinguish','khác biệt; phân biệt','noun','先说两种方式的区别。','Explain the difference between the two methods first.'),
('具有','to possess; have','có','verb','这个节目具有自己的特色。','This programme has its own distinctive features.'),
('人生','human life; life’s course','cuộc đời','noun','这部故事讲人生，不是活动通知。','This story concerns a life, not an event notice.'),
('全场','the whole audience or venue','toàn khán phòng','noun','全场都听见了，不等于每个人都同意。','The whole venue heard it; that does not mean everyone agrees.'),
('观众','audience; viewer','khán giả','noun','观众还没进场，门口有人等。','The audience has not entered yet; people are waiting at the entrance.'),
('观看','to watch; view','xem','verb','我们一起观看节目。','We watch the programme together.'),
('收看','to watch a broadcast','xem chương trình phát sóng','verb','她晚上收看电视节目。','She watches a television programme in the evening.'),
('收听','to listen to a broadcast','nghe chương trình phát sóng','verb','我早上收听广播。','I listen to the radio in the morning.'),
('听众','listeners; radio audience','thính giả','noun','听众的问题由主持人读出来。','The presenter reads listeners’ questions aloud.'),
('广播','radio broadcast; to broadcast','phát thanh','noun','广播没有画面，先听清名字。','The radio has no pictures; listen carefully to the names first.'),
('电台','radio station','đài phát thanh','noun','这家电台今天播出什么？','What is this radio station broadcasting today?'),
('电视台','television station','đài truyền hình','noun','电视台的新节目还没开始。','The TV station’s new programme has not started yet.'),
('国内','within the country; domestic','trong nước','noun','国内有不同的节目，不是一种风格。','There are different domestic programmes, not just one style.'),
('全球','the whole world; global','toàn cầu','noun','全球的观众不可能都有同一个习惯。','Viewers worldwide cannot all share the same habit.'),
('广大','broad; numerous','đông đảo; rộng lớn','adjective','通知面向广大观众，不只面向学生。','The notice addresses the broader audience, not just students.'),
('媒体','media','truyền thông','noun','不同媒体可以报道同一件事。','Different media can report the same event.'),
('互联网','Internet','Internet','noun','我在互联网上查播出时间。','I check the broadcast time on the Internet.'),
('联合','to unite; joint','liên kết; chung','verb','两个小组联合举办活动。','Two groups jointly organize the event.')],
[grammar(u,'三28','除了 + 范围','Identify whether an exception or addition is intended',
'除了 introduces a noun phrase or activity. Its interpretation depends on the following clause: 除了我，大家都来 excludes me; 除了看节目，我还听广播 adds an activity. 以外 can follow the phrase. The same 除了 phrase without its continuation does not decide the meaning by itself.',[
('除了我，大家都来了。','Everyone except me came.'),('除了看节目，我还听广播。','Besides watching programmes, I also listen to the radio.'),('除了周末以外，她晚上也有空。','Besides weekends, she is also free in the evenings.')],
('除了我，大家都来，所以我也来。','除了我，大家都来，我不来。','In this 都 construction, the named person is excluded.')),
grammar(u,'三38','除了……（以外），还 / 也 / 都……','Read the continuation and its scope',
'还/也 commonly signal addition: 除了电视节目，她也看网上的视频. 都 commonly totals the remaining group after an exception: 除了我，大家都看过. State the remainder rather than treating 都 as a claim about all people everywhere. Do not infer whether another person joins from their preference for a similar activity.',[
('除了广播，我还看电视节目。','Besides the radio, I also watch TV programmes.'),('除了她以外，我也没看过。','Besides her, I too have not watched it.'),('除了周五，其他几天都可以。','Any of the other days works, except Friday.')],
('除了我，大家都看过，所以所有人都看过。','除了我，其他人都看过。','The total applies to the remaining group, not the excluded member.'))],
('One exception and one more habit','Find who has not watched and what else the host listens to.',[
('除了我，大家都看过这个节目吗？','Has everyone except me watched this programme?'),
('不是，除了你，我也没看过。','No; besides you, I have not watched it either.'),
('那今晚一起观看吧，电视台六点播出。','Then watch it together tonight; the TV station broadcasts it at six.'),
('我除了收看电视，还收听电台的广播。','Besides watching TV, I listen to the radio station’s broadcasts too.'),
('观众和听众有什么区别？','What is the difference between viewers and listeners?'),
('这里一个看画面，一个主要听声音，不能说所有媒体都相同。','Here one watches pictures and the other mainly listens; we cannot say all media are the same.'),
('互联网也能看，大家都来线下吗？','It can also be watched online; is everyone joining in person?'),
('除了周五以外，其他几天都可以，先问每个人。','Apart from Friday, the other days work; ask everyone first.')],
[('mainidea','Which distinction matters?',['Exception versus an additional person or activity','All media having identical content','Every person joining in person'],0),('detail','How many speakers have not watched?',['Both speakers','Only the first','Neither'],0),('inference','Does access online confirm in-person attendance?',['No','Yes','Only at six'],0)],[],True),
('A broad audience is not one habit','Read how a group chooses media without making a universal claim.',[
('两个小组联合办观看活动，面向广大观众。','Two groups organize a viewing event jointly for a broad audience.'),
('除了电视台的节目，他们还介绍电台广播，让听众也有选择。','Besides television programmes, they introduce radio broadcasts, offering listeners choices too.'),
('有人收看画面，有人收听声音，互联网提供另一种参加方式。','Some watch pictures, others listen to sound; the Internet offers another way to join.'),
('国内和全球都有不同媒体，世界不只有一种节目，类似的节目也可能具有不同特色。','There are varied media domestically and globally; the world has more than one kind of programme, and similar programmes can have different distinctive features.'),
('哪一类爱好普遍，要说明调查范围，不能从全场都笑推断所有人都同意。','Claims about a common kind of hobby need a stated survey scope; the whole audience laughing does not establish universal agreement.'),
('一部讲人生的故事不是每个人的经历，节目和现实要区分。','A story about a life is not everyone’s experience; distinguish the programme from reality.'),
('这次除了周五，其他几天都可以，但具体时间还没统一。','For this occasion, all days except Friday work, but the exact time is unsettled.'),
('把区别说清楚，再问朋友想看还是想听。','Explain the differences, then ask whether the friends want to watch or listen.')],
[('mainidea','What should the organizers avoid?',['Turning a group’s reaction into a universal claim','Offering listeners a choice','Explaining different media'],0),('detail','Which day is excluded?',['Friday','Saturday','Every evening'],0),('inference','Is an exact meeting time fixed?',['No','Yes, six for every person','Only for online viewers'],0)],[(0,'联合'),(3,'特色')],False),
('One more voice','Read an original verse about inclusion and exceptions.',[
('除了屏幕，还有声音。','Besides the screen, there is sound.'),('除了你，我也没听。','Besides you, I have not heard it either.'),('大家的路，不必一样。','Everyone’s path need not be the same.'),('先问一句，再选一场。','Ask first, then choose an event.')],
[('inference','What does the verse encourage?',['Asking about differing preferences','Assuming one habit fits all','Excluding every listener'],0)],[],False),
dict(tf=[('除了','除了周五，其他几天都可以。','Any of the other days works except Friday.','Friday is excluded.',True,'都 totals the remaining days.'),('普遍','这种爱好普遍，但不是人人都有。','This hobby is widespread, but not everyone has it.','Every person has this hobby.',False,'普遍 is not universal.')],
reply=[('收听','不看画面，想听节目。','I do not want pictures; I want to listen to a programme.',['可以收听广播。','所有人都必须看。','除了我就是我一定来。'],0,'Offer a listening option.'),('区别','两个节目类似，能说完全一样吗？','The programmes are similar; are they entirely identical?',['不能，还要看区别。','能，类似就是相同。','能，观众就是电视台。'],0,'Similarity does not prove identity.')],
fill=[('媒体','不同媒体可以讲同一件事。','Different media can discuss the same matter.'),('观众','观众还没进场。','The audience has not entered yet.')],
match=[('广播',[('我收听广播。','I listen to radio broadcasts.'),('她收看电视节目。','She watches TV programmes.'),('除了我，大家都来。','Everyone except me is coming.')]),('互联网',[('互联网也能观看。','It can also be watched on the Internet.'),('除了她，我也没看过。','Besides her, I have not watched it either.'),('全场都笑了。','The whole audience laughed.')])]),
[('Clarify the exception','除了你，我也没看过。','Besides you, I have not watched it either.','Keep addition separate from exclusion.'),('Limit a claim','这只是我们小组的选择。','This is only our group’s choice.','Do not speak for all viewers.')],
[('周五可以吗？','Does Friday work?','Name the excluded day',['除了周五，其他几天都可以。']),('只看电视吗？','Do you only watch television?','Add another habit',['除了电视，我还听广播。'])],
'Native check: 普遍 versus universal scope, 除了…也 negation, 收看/观看 and 收听 register, 广大 audience collocation, and the original verse’s ellipsis. No population survey is claimed. Native review pending.')

unit_glosses['s3-u23']={'表决':'to vote','报名':'to register','私人':'private','场地':'venue','许可':'permission','危险':'dangerous; danger','费用':'expense','参与':'to participate','规则':'rule','安全':'safety; safe','意见':'opinion','建议':'suggestion','拒绝':'to refuse','方案':'proposed plan','取消':'to cancel','公布':'to publish; announce','以及':'as well as'}
unit_glosses['s3-u23'].update({'符合':'to conform to','拥挤':'crowded; crowding','与否':'whether or not','是否':'whether; whether or not','不合法':'not lawful','项':'classifier for projects, provisions or systems'})
u='s3-u23'
unit(u,'只有大家同意才公布',[
'State a necessary condition without claiming it guarantees an outcome','Add reasons and alternatives with explicit connectors','Separate an approved plan from a proposed one'],[
('并且','and; moreover','và; hơn nữa','conjunction','先确认场地，并且问清费用。','Confirm the venue and clarify the expenses first.'),
('不光','not only','không chỉ','conjunction','不光问时间，还要问地点。','Ask not only the time but also the location.'),
('不仅','not only','không chỉ','conjunction','不仅要公布，也要让大家看得懂。','Not only publish it, but make it understandable too.'),
('要是','if','nếu','conjunction','要是有人不同意，先听原因。','If someone disagrees, listen to the reasons first.'),
('只有','only if; only','chỉ khi','conjunction','只有大家同意，才公布新安排。','Announce the new arrangements only if everyone agrees.'),
('同意','to agree; consent','đồng ý','verb','她还没同意，不要替她报名。','She has not agreed; do not register on her behalf.'),
('反对','to oppose','phản đối','verb','她反对这个时间，不是反对活动本身。','She opposes this time, not the event itself.'),
('坚决','firm; resolute','kiên quyết','adjective','她坚决不同意公开私人地址。','She firmly opposes making the private address public.'),
('主张','to advocate; position','chủ trương','verb','我主张先问所有参与者。','I advocate asking all participants first.'),
('主意','idea; plan','ý tưởng','noun','这是一个主意，还不是决定。','This is an idea, not a decision yet.'),
('制定','to formulate; draw up','lập; xây dựng','verb','先讨论，再制定规则。','Discuss before drawing up the rules.'),
('制度','system; rules','chế độ; hệ thống quy định','noun','这项制度还在讨论中。','This system of rules is still being discussed.'),
('规范','standard; norm; standardize','quy chuẩn; chuẩn hóa','noun','格式规范写在通知后面。','The formatting standard is written after the notice.'),
('合法','lawful; legal','hợp pháp','adjective','合法不合法，要看实际规定。','Whether it is lawful depends on the actual rules.'),
('批准','to approve; authorize','phê duyệt','verb','场地申请还没批准。','The venue application has not been approved.'),
('认可','to recognize; accept','công nhận','verb','我认可你的努力，不代表同意这个时间。','I recognize your effort; that does not mean agreeing to this time.'),
('确保','to ensure','đảm bảo','verb','先确保每个人都收到通知。','Make sure everyone receives the notice first.'),
('防止','to prevent','ngăn ngừa','verb','核对日期，防止发旧消息。','Check the date to prevent sending an old message.'),
('预防','to take preventive measures','phòng ngừa','verb','预防问题，要先看入口是否够用。','To prevent problems, check whether the entrance is adequate first.'),
('情况','situation; circumstances','tình hình','noun','先了解情况，不急着反对。','Understand the situation before rushing to oppose it.'),
('如何','how','như thế nào','pronoun','如何报名，通知还没说明。','The notice has not explained how to register.'),
('能不能','whether one can; can or cannot','có thể hay không','phrase','能不能用这个房间，还要问管理人员。','Ask the staff whether this room may be used.')],
[grammar(u,'三30','并且 / 不光 / 不仅 / 另外 / 要是 / 因此 / 由于 / 只有','Connect clauses according to their relationship',
'并且 adds a connected statement; 不光/不仅 introduce the first part of an additive pair with 还/也/而且. 另外 adds a separate point. 要是 introduces an if-condition, commonly answered by 就. 由于 introduces the cause clause and 因此 the consequence; here 由于……，因此…… links two clauses, contrasting the earlier preposition plus cause phrase. 只有 names a necessary condition with 才. Do not interchange cause, addition and condition just because all link statements.',[
('先确认地点，并且问清费用；另外，还要问人数。','Confirm the venue and expenses; additionally ask the number of people.'),
('不光要问时间，还要问地点；不仅要公布，也要解释清楚。','Ask not only the time but the venue; not only announce it but explain clearly.'),
('要是下雨，就换室内；由于场地没批准，因此先不公布。','If it rains, move indoors; because the venue is unapproved, do not announce yet.'),
('只有大家同意，才公布。','Announce only if everyone agrees.')],
('要是大家同意，因此大家同意。','要是大家同意，就再确认场地。','An if-condition does not assert its own fulfillment; give the corresponding next action.')),
grammar(u,'三70','只有……，才……','Name a necessary, not sufficient, condition',
'只有大家同意才公布 sets agreement as necessary for announcing. It does not say agreement alone makes a venue available or forces an announcement. Contrast 要是大家同意，就再确认场地, an if-then step. 不同意就不公布 is compatible with the necessary condition; 同意了还要确认场地 is also compatible. Keep the stated condition and remaining requirements distinct.',[
('只有大家同意，才公布新安排。','Only if everyone agrees will the new arrangements be announced.'),
('只有确认场地，才可以发地址。','Only after confirming the venue may the address be sent.'),
('大家同意了，还要等场地批准。','Everyone has agreed; venue approval is still needed.')],
('只有大家同意才公布，所以同意以后一定立刻公布。','大家同意以后，还要确认其他要求，再公布。','A necessary condition alone does not guarantee immediate action.'))],
('An idea is not an approved plan','Find what is agreed and which requirement remains.',[
('我有个主意，周五办活动，大家能不能来？','I have an idea: an event on Friday. Can everyone come?'),
('我认可你的努力，但反对周五这个时间。','I recognize your effort but oppose Friday as the time.'),
('那先了解情况，如何改合适？','Then let us understand the situation; how should we change it?'),
('我主张先问每个人，并且确认场地。','I advocate asking each person and confirming the venue.'),
('不光要问时间，还要问费用；另外，私人地址别公开。','Ask not only the time but the expense; also do not make private addresses public.'),
('好，只有大家同意，才公布。现在有人同意了，可以发了吗？','Okay, announce only if everyone agrees. Some agree now; can we send it?'),
('还不行，场地还没批准。我坚决不同意先发旧地址。','Not yet; the venue is not approved. I firmly oppose sending an old address first.'),
('先制定清楚的规则，防止大家收到不同版本。','First draw up clear rules to prevent people receiving different versions.')],
[('mainidea','What needs distinguishing?',['A proposal, partial agreement and approval','Recognition and complete agreement as the same thing','Every venue as automatically available'],0),('detail','What is still unapproved?',['The venue','The private address owner’s identity','A completed exam result'],0),('inference','Does some agreement meet “everyone agrees”?',['No','Yes','Only because the organizer worked hard'],0)],[],True),
('A notice with conditions','Read the proposed steps without mistaking them for completed actions.',[
('这个主意还没成为决定，先问能不能参加，了解每个人的情况。','This idea is not yet a decision; ask whether each person can attend and understand their circumstances.'),
('有人认可组织者的努力，却反对时间，不能因此说他同意。','Someone recognizes the organizer’s effort but opposes the time; that does not mean consent.'),
('组织者主张不光问地点，还问费用；并且说明如何报名，以及参加的时间。','The organizer advocates asking not only the venue but the fee, and explaining how to register as well as the time for participating.'),
('不仅通知要清楚，格式也要符合规范；另外，私人信息不能随便公布。','The notice must be clear and its format meet the standard; additionally private information cannot be announced casually.'),
('场地还没批准，要是下雨，就再讨论室内方案。','The venue is unapproved; if it rains, discuss the indoor alternative again.'),
('只有大家同意，才公布；同意以后还要确认场地许可。','Announce only if everyone agrees; venue permission still needs confirmation after agreement.'),
('有人建议制定制度，也要检查入口，预防拥挤，确保大家收到同一通知，不能保证没有危险。','Someone suggests drawing up rules; still check the entrance, prevent crowding and ensure everyone receives the same notice, without guaranteeing an absence of danger.'),
('由于地址还没核实，因此先不发布；合法与否要看实际规定，不凭一句玩笑判断。','Because the address is unverified, do not publish yet; legality depends on actual rules, not a joke.')],
[('mainidea','What does the notice make explicit?',['Conditions and remaining checks','A guarantee against every future problem','A final legal opinion'],0),('detail','What follows agreement?',['Confirmation of venue permission','Automatic immediate publication','Deletion of the rules'],0),('inference','Is the discussion a legal determination?',['No; it says to check actual rules','Yes','Only if the joke is funny'],0)],[(5,'只有'),(7,'因此')],False),
('Not every yes is the same yes','Read an original scene about counting agreement.',[
('一个人点头了，可以公布吧？','One person nodded; we can announce now, right?'),('你说的是只有大家同意。','You said only if everyone agrees.'),('我的主意听起来很热闹。','My idea sounds lively.'),('热闹不是表决。先问清楚。','Lively is not a vote. Ask clearly first.')],
[('inference','Why is announcing premature?',['One nod does not establish everyone’s consent','Lively ideas are always forbidden','The room has already been booked'],0)],[],True),
dict(tf=[('只有','只有大家同意，才公布；场地还要确认。','Announce only if everyone agrees; the venue still needs confirming.','Agreement alone guarantees immediate publication.',False,'A necessary condition is not sufficient.'),('认可','我认可你的努力，但不同意时间。','I recognize your effort but disagree with the time.','Recognition is not consent to the time.',True,'The contrast explicitly separates them.')],
reply=[('批准','场地还没批准，先发地址吗？','The venue is unapproved; should we send the address?',['先不发，再确认许可。','发完就自动批准。','有人点头就是所有人同意。'],0,'Wait for confirmation.'),('如何','有人反对这个时间，怎么办？','Someone opposes this time; what now?',['先问原因，再讨论。','替他报名。','把反对写成同意。'],0,'Hear the reasons.')],
fill=[('并且','先确认场地，并且问清费用。','Confirm the venue and clarify expenses first.'),('防止','先核对，防止发旧消息。','Check first to avoid sending old information.')],
match=[('主意',[('这是主意，还没决定。','This is an idea, not yet a decision.'),('场地还没批准。','The venue remains unapproved.'),('先问如何报名。','First ask how to register.')]),('同意',[('她还没同意。','She has not agreed yet.'),('要是下雨，就换室内。','If it rains, move indoors.'),('大家收到同一通知。','Everyone receives the same notice.')])]),
[('Separate appreciation and agreement','谢谢你的安排，但这个时间我不行。','Thanks for arranging it, but this time does not work for me.','Appreciation does not require consent.'),('State what remains','同意以后还要等批准。','Approval is still needed after agreement.','Keep a pending requirement visible.')],
[('有人反对，怎么办？','What should we do if someone opposes it?','Listen before deciding',['先问原因，再讨论。']),('现在可以公布吗？','Can we announce now?','Name the remaining requirement',['还要确认场地。'])],
'Native check: conjunction 由于 versus cause-preposition use, connector scope, 认可/同意 distinction, necessary versus sufficient 只有 conditions, and club-rule language. Legal and safety vocabulary are language practice only; no real determination or event safety guarantee is claimed. Native review pending.')

unit_glosses['s3-u24']={'语调':'intonation','声调':'lexical tone','疑问':'question; doubt','确认':'to confirm','提问':'to ask a question','气氛':'atmosphere','调侃':'light teasing','针对':'directed toward','表情':'facial expression','害羞':'shy','热烈':'enthusiastic; intense','认真':'serious; conscientiously','停顿':'pause','模仿':'to imitate','笑话':'joke','误会':'misunderstanding','记录':'to record; record','心情':'mood','突然':'suddenly'}
selected_source_rows['s3-u24:精神']='4365'
vocabulary_readings['s3-u24:精神']='jīng shen'
dictionary.update({'很精神':'hěn jīng shen','精神一点':'jīng shen yì diǎn','看着很精神':'kàn zhe hěn jīng shen','干吗':'gàn má','乐':'lè','好好':'hǎo hǎo'})
unit_glosses['s3-u24']['起落']='rise and fall'
u='s3-u24'
unit(u,'笑一下，也问清楚',[
'Understand laughter in context without assuming mockery','Recognize an intonation question without 吗','Separate lively delivery from speed and pronunciation accuracy'],[
('哈哈','ha ha; laughter','ha ha; tiếng cười','onomatopoeia','她写哈哈，是笑自己的玩笑。','She writes “ha ha,” laughing at her own joke.'),
('干吗','why; what for','làm gì; tại sao','pronoun','你干吗突然安静了？','Why did you suddenly go quiet?'),
('话题','topic','chủ đề','noun','这个话题还没说完。','We have not finished discussing this topic.'),
('念','to read aloud; recite','đọc thành tiếng','verb','请把这句话念出来。','Please read this sentence aloud.'),
('突然','sudden; unexpected','đột nhiên','adjective','声音突然变大了。','The voice suddenly became louder.'),
('快速','fast; rapid','nhanh','adjective','快速回答不等于回答正确。','A fast reply does not necessarily mean a correct reply.'),
('速度','speed','tốc độ','noun','速度慢一点，先说清楚。','Slow down a little and speak clearly first.'),
('静','quiet; still','yên tĩnh','adjective','屋里很静，我听见她笑了。','The room is quiet; I hear her laugh.'),
('紧张','nervous; tense','căng thẳng','adjective','她有点紧张，不是在生气。','She is a little nervous, not angry.'),
('乐','to enjoy; be amused','vui; thích thú','verb','听到这个玩笑，她乐了。','Hearing the joke amused her.'),
('乐观','optimistic','lạc quan','adjective','她很乐观，也承认还有困难。','She is optimistic and also acknowledges remaining difficulties.'),
('欢乐','joyful; joyous','vui vẻ','adjective','现场很欢乐，不代表每个人都想大声说。','The scene is joyful, but that does not mean everyone wants to speak loudly.'),
('活','alive; lively','sống; sống động','adjective','她说得很活，不是只把字念完。','Her delivery is lively, not merely finishing the written words.'),
('生动','vivid; lively','sinh động','adjective','这个例子很生动，也要准确。','This example is vivid, and must also be accurate.'),
('动人','moving; touching','cảm động','adjective','一句简单的感谢也很动人。','Even a simple thank-you can be moving.'),
('表现','performance; to display','thể hiện','noun','这次表现要看具体做了什么。','Judge this performance by what was actually done.'),
('表演','to perform; performance','biểu diễn','verb','表演时可以夸张，教学时仍要说清。','Performance can be exaggerated; teaching still requires clear speech.'),
('明显','obvious; clear','rõ ràng','adjective','她的笑意很明显，但意思还要看上下文。','Her amusement is obvious, but meaning still depends on context.'),
('精神','lively; smart-looking','tươi tỉnh; gọn gàng','adjective','她今天看着很精神。','She looks lively and smart today.'),
('状态','state; condition','trạng thái','noun','今天状态不一样，先慢慢来。','Today’s condition is different; take it slowly first.'),
('自觉','self-motivated; conscious','tự giác','adjective','她很自觉，没听清就再问。','She is conscientious and asks again when she has not heard clearly.'),
('好好','properly; carefully','đàng hoàng; cẩn thận','adverb','先好好听，再学她的玩笑。','Listen carefully before learning her joke.')],
[grammar(u,'三31','哈哈：笑声的文字表示','Interpret laughter through the surrounding turn',
'哈哈 writes a laugh, not an automatic insult or agreement. It can follow amusement, self-directed humour or relaxed banter. Who or what the joke targets depends on context. If the listener is uncomfortable, clarify rather than insisting that a laugh proves friendliness. Spoken laughter need not literally pronounce two citation syllables; these written examples are read as language practice.',[
('哈哈，我又把日期看错了。','Ha ha, I misread the date again.'),('你笑什么？我在笑自己的玩笑。','What are you laughing at? My own joke.'),('哈哈只是笑声，不能证明大家同意。','“Ha ha” is only laughter; it does not prove everyone agrees.')],
('她写哈哈，所以一定在笑我。','她写哈哈，我先问她在笑什么。','Laughter alone does not identify its target.')),
grammar(u,'三78','用疑问语调提问，不必都有吗','Recognize a confirmation question in context',
'An utterance with statement word order can be a confirmation question through intonation and context: 你今天也来参加这个活动？ No 吗 is required. Question intonation does not erase Mandarin lexical tones; it is not a rule to replace every final syllable’s tone with a rise. Compare a question seeking confirmation with a statement giving confirmed information. These synthesized examples are practice, not a certified acoustic minimal-pair test.',[
('你今天也来参加这个活动？我确认一下。','Are you also joining this event today? Let me confirm.'),('他今天也来，我已经问过了。','He is joining today too; I have already asked.'),('你说的时间是周五晚上？我怕记错了。','The time you said was Friday evening? I am worried I remembered incorrectly.')],
('没有吗，所以不能是问题。','没有吗，也可以用疑问语调确认。','Question particles are not the only way to ask a question.'))],
('The laugh was about the date','Find the target of the joke and the actual question.',[
('哈哈，我又把日期看错了。','Ha ha, I misread the date again.'),
('你在笑我？我有点紧张。','Are you laughing at me? I am a little nervous.'),
('没有，我在笑自己。你干吗突然不说话了？','No, I am laughing at myself. Why did you suddenly stop talking?'),
('我以为你在表演那个话题，声音变大了。','I thought you were performing that topic; your voice got louder.'),
('我乐了才大声一点，先好好说清楚。','I spoke a little louder because I was amused; let me clarify properly.'),
('你今天也来参加这个活动？我确认一下。','Are you also joining this event today? Let me confirm.'),
('来。你把通知慢一点念，速度太快我没听清。','Yes. Read the notice more slowly; I could not hear clearly at that speed.'),
('好，状态不同就调整，不把快速当表现好。','Okay; adjust for different conditions, without equating speed with good performance.')],
[('mainidea','What misunderstanding is resolved?',['The laugh concerned the speaker’s own date mistake','The listener was definitely being mocked','All loud voices express anger'],0),('detail','What does the listener request?',['A slower reading of the notice','A new joke targeting her','Cancellation of the event'],0),('inference','Does the absence of 吗 rule out a question?',['No','Yes','Only when the room is quiet'],0)],[],True),
('Lively, not careless','Read what changes with delivery and what must stay clear.',[
('屋里很静，朋友突然写了哈哈，笑的是自己看错日期。','The room is quiet; the friend suddenly writes “ha ha,” laughing at her own date mistake.'),
('听者紧张，不一定是生气，先问干吗停下来，别猜心情。','The listener’s nervousness is not necessarily anger; ask why she paused rather than guessing her mood.'),
('笑意明显，现场欢乐，气氛热烈，但这个话题仍要好好说明。','The amusement is obvious and the atmosphere joyful and enthusiastic, but this topic still needs careful explanation.'),
('说得活、例子生动，会让普通感谢也动人；表演不是模糊发音的理由。','Lively delivery and vivid examples can make ordinary thanks moving; performance is no excuse for unclear pronunciation.'),
('她听了玩笑就乐了，看着很精神，也自觉把速度放慢。','The joke amused her; she looks lively and conscientiously slows down.'),
('乐观不等于没有困难，快速不等于准确，表现要看实际完成的事。','Optimism does not mean absence of difficulty, speed does not mean accuracy, and performance depends on actual accomplishments.'),
('她把问题念出来：你说的时间是周五晚上？然后等对方确认。','She reads the question aloud: the time you said was Friday evening? Then she waits for confirmation.'),
('状态不合适就休息，声音大小不能代替意思和声调。','Rest if the condition is unsuitable; volume cannot replace meaning and lexical tones.')],
[('mainidea','What balance does the note advocate?',['Expressiveness with clear meaning and pronunciation','Speed regardless of accuracy','Interpreting every laugh as agreement'],0),('detail','What made the speaker laugh?',['Her own date mistake','The listener’s failure','A confirmed cancellation'],0),('inference','Does sounding optimistic prove no difficulties remain?',['No','Yes','Only with loud delivery'],0)],[(2,'明显'),(5,'快速')],False),
('Read the date, not my mind','Read an original playful verse.',[
('哈哈，笑的是我。','Ha ha, I am laughing at myself.'),('你今天也来？先等你说。','Are you coming today too? I will wait for your answer.'),('声音有起落，字要念清楚。','The voice rises and falls; pronounce the words clearly.'),('日期没记准，再问也不错。','If the date was not remembered accurately, asking again is fine.')],
[('inference','What is encouraged?',['Clarifying after a mistake','Guessing another person’s thoughts','Replacing lexical tones with volume'],0)],[],False),
dict(tf=[('哈哈','哈哈，我在笑自己看错日期。','Ha ha, I laugh at my own date mistake.','The stated target is the speaker’s own mistake.',True,'The target is explicit.'),('快速','她说得快速，但还没念清楚。','She speaks quickly but has not pronounced it clearly.','Speed proves clear pronunciation.',False,'Speed and clarity are distinct.')],
reply=[('紧张','你在笑我吗？','Are you laughing at me?',['没有，我在笑自己看错日期。','哈哈就是所有人都同意。','你紧张就是生气。'],0,'Clarify the target rather than assume.'),('念','没听清通知，怎么办？','The notice was unclear; what should we do?',['慢一点再念。','只加大声音，不管字。','把日期猜出来。'],0,'Repeat more slowly and clearly.')],
fill=[('速度','速度慢一点，先说清楚。','Slow down and speak clearly first.'),('状态','今天状态不同，先调整。','Today’s condition differs; adjust first.')],
match=[('话题',[('话题还没说完。','The topic has not been finished.'),('她看着很精神。','She looks lively and smart.'),('她自觉再问一次。','She conscientiously asks again.')]),('表现',[('表现要看实际做了什么。','Performance depends on what was actually done.'),('乐观也可以承认困难。','One can be optimistic and acknowledge difficulties.'),('笑声不证明同意。','Laughter does not prove agreement.')])]),
[('Clarify gently','我笑的是自己，不是你。','I am laughing at myself, not at you.','Humour should not override the other person’s interpretation.'),('Ask without guessing','你今天也来参加活动？','Are you joining the event today too?','Wait for confirmation.')],
[('你在笑什么？','What are you laughing at?','Name the actual target',['我在笑自己看错日期。']),('速度太快，怎么办？','What if the speed is too fast?','Ask for a clear repeat',['慢一点，再念一遍。'])],
'Native check: 精神 adjective jīngshen versus noun jīngshén, 活 for lively delivery, 乐 verb register, 干吗 casual tone, 哈哈 target and written-versus-spontaneous laughter, original verse rhythm, and question intonation preserving lexical tones. Synthesized intonation has not been certified by a native listener. Native review pending.')

from retrievals import apply_ids
apply_ids(['s3-u21','s3-u22','s3-u23','s3-u24'])
