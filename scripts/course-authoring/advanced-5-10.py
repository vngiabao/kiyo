"""Two original opinion texts about a fictional library-hours pilot."""
import sys
from advanced_core import write,rows,words,q,card,practice
V=words('''
主观|subjective|chủ quan|我喜欢晚上读，但这是主观感受。|I like evening reading, but that is a subjective experience.|她提醒我，不要把主观印象当成人数。|She reminded me not to treat a subjective impression as a count.
立场|position; standpoint|lập trường|我的立场是先继续试，不是马上每天延长。|My position is to continue the trial, not extend every day immediately.|他解释了自己的立场，也听了对方的理由。|He explained his position and listened to the other side’s reasons.
逻辑|logic|lô-gic|从有人来跳到人人需要，这个逻辑不成立。|The logic of jumping from some attendance to universal need doesn’t hold.|这个故事的时间逻辑有问题。|The chronology of this story has a logical problem.
矛盾|contradiction; conflict|mâu thuẫn|想安静读和想聊天，在同一个小厅里有矛盾。|Quiet reading and conversation conflict in the same small hall.|他说的两个时间互相矛盾。|The two times he gave contradict each other.
间接|indirect|gián tiếp|报名表间接告诉我们有人有兴趣，不说明一定到场。|Registration indirectly indicates interest, not certain attendance.|我是间接听到这个消息的，没有见到本人。|I heard this news indirectly, without seeing the person.
排除|rule out; remove|loại trừ|还不能排除天气影响人数。|We cannot yet rule out the weather affecting attendance.|先排除时间冲突，再选地点。|Rule out scheduling conflicts before choosing the venue.
控制|control|kiểm soát|可以控制一次试办的时长，不能控制谁一定来。|We can control a trial’s duration, not who will definitely attend.|她把说话的声音控制得很小。|She kept her speaking voice very quiet.
加以|give; apply, before a verb|tiến hành; đưa ra|这些意见要加以讨论，不是直接删掉。|These views need to be discussed, not simply deleted.|发现的问题已经加以说明。|The problems found have been explained.
依据|basis; according to|căn cứ|人数是一个依据，但不是全部。|Attendance is one basis, not the whole picture.|他依据原来的记录核对日期。|He checked dates against the original record.
说法|claim; wording; account|cách nói; nhận định|我不同意“少来一次就是不需要”这个说法。|I disagree with the claim that missing one visit means no need.|请把两种说法都记下来。|Please record both accounts.
前提|premise; prerequisite|tiền đề|继续试办的前提是有人能负责关门。|Continuing the pilot requires someone to close up.|这个建议的前提还没有确认。|The premise of this suggestion has not been confirmed.
评估|evaluate; evaluation|đánh giá|四周以后，再评估延长时间的安排。|Evaluate the extended hours after four weeks.|评估不能只看一次最好结果。|An evaluation cannot look only at one best result.
评论|comment; commentary|bình luận|这条评论提出了安静的问题。|This comment raises the issue of quiet.|她读完文章，写了一条简短评论。|After reading the article she wrote a short comment.
期望|expect; expectation|mong đợi|我期望方便一些，不是要求随时开门。|I hope for more convenience, not opening at any time.|大家对结尾的期望不一样。|People have different expectations of the ending.
局面|situation; state of affairs|tình hình|我们想改变下班以后无处读书的局面。|We want to change the lack of a reading place after work.|一句解释改变了争论的局面。|An explanation changed the course of the argument.
缺乏|lack|thiếu|没有问不来的人，记录就缺乏他们的意见。|Without asking non-attendees, the record lacks their views.|这段解释缺乏具体例子。|This explanation lacks concrete examples.
群体|group of people|nhóm người|不同群体需要的时间可能不同。|Different groups may need different hours.|不能用一个人代表整个群体。|One person cannot stand for a whole group.
比重|proportion; relative share|tỷ trọng|不知道总人数，就算不出这个比重。|Without the total population we cannot calculate this proportion.|这次交通费在总费用中的比重更大。|Travel makes up a larger share of the total cost this time.
成本|cost|chi phí|多开两小时，也有整理和关门的成本。|Two additional hours also involve tidying and closing costs.|便宜的材料不一定让总成本下降。|Cheap material doesn’t necessarily reduce total cost.
成效|effectiveness; result|hiệu quả|有人找到读书时间，是一个成效，但还要继续看。|Some finding time to read is a benefit, but further observation is needed.|我们下周再看看这个办法的成效。|We will look again at this method’s results next week.
大致|approximately; broadly|đại khái|我先大致介绍四周的记录。|I will first give a broad account of the four-week records.|路线大致相同，最后一段不同。|The routes are broadly the same, but differ at the end.
单一|single; one-dimensional|đơn nhất|只看总人数，这个依据太单一。|Total attendance alone is too one-dimensional a basis.|她不想只做单一类型的工作。|She doesn’t want to do only one type of work.
差距|gap; disparity|khoảng cách|想来的时间和开放时间有差距。|There is a gap between desired visiting times and opening hours.|练习的表现和实际比赛还有差距。|There is still a gap between practice performance and competition.
检验|test; examine|kiểm nghiệm|再试四周，可以检验这个安排能不能持续。|Another four-week trial can test whether this arrangement can continue.|这一次检验发现了两个问题。|This examination found two problems.
''')
D=rows('''
你看了小图书馆延长时间的那篇文章吗？|Did you read the article about the small library extending its hours?
看了。我希望周四能继续开到八点，下班后才来得及。|Yes. I hope Thursdays continue until eight; I can only get there after work.
文章说四周共六十四人次，你觉得够吗？|It says sixty-four visits over four weeks. Is that enough, in your view?
够不够要看什么目的吧，至少不是完全没人来。|Enough for what purpose? At least it wasn’t entirely unused.
但也不是六十四个不同的人。|But not necessarily sixty-four different people.
对，我就去了三次，不能把我算成三个居民。|Right. I went three times; that doesn’t make me three residents.
有人评论说，大家都喜欢聊天，应该改成交流活动。|Someone commented that everyone likes chatting, so it should become a discussion event.
我可不是，我去是想安静看书。|I don’t. I go to read quietly.
所以“大家都喜欢”说得太满了。|So “everyone likes it” goes too far.
是啊。我想聊天的时候，会另外找地方。|Yes. When I want to talk, I go somewhere else.
你会要求每天都延长吗？|Would you ask for longer hours every day?
现在不敢这么说。先把周四安排好，再看看别的日子。|Not at this stage. Settle Thursdays first, then look at other days.
负责关门的两个人，每次都多留两小时。|The two people closing up each stay two extra hours.
这也要算进去。不能只问来的人方便不方便。|That matters too. We can’t consider only convenience for visitors.
如果他们下个月没空呢？|What if they are unavailable next month?
就先确认有没有别人接，不要先发继续开放的通知。|Check for someone to take over before announcing continued opening.
看来你的立场是继续试，不是保证马上扩大。|So your position is to keep trying, not guarantee immediate expansion.
对。支持这个办法，也可以说清还不知道什么。|Right. Supporting it can include stating what we still don’t know.
''')
M=rows('''
你一晚上看了多少页？|How many pages did you read this evening?
三页。|Three.
我看了二十页。|I read twenty.
你的书一页只有两句话吧？|Does your book have only two sentences per page?
对，还有很大的画。|Yes, and large pictures.
那别光比页数。|Then don’t compare only page counts.
你的三页是不是一页全是字？|Are your three pages full of text?
是，还来回看了两次。|Yes, and I read them twice.
好，我们都各自看明白一点了。|Okay, we each understood a little more.
我还没完全明白，最后一句要再想。|Not entirely for me; I still need to think about the final sentence.
那我先出去，你留在这里想。|Then I’ll go outside first; you can stay and think.
八点关门以前，我一定收好书。|I’ll put the book away before closing at eight.
''')
R=rows('''
这个社区的小图书馆原来每天下午六点关闭。四周试办中，周四延长到晚上八点，其他日子的时间不变。我支持再试四周，因为下班以后来的人确实找到了一段能读书的时间。不过，我的立场不是马上每天都开到八点，也不是说不来的人都不喜欢读书。这两个更大的判断，需要另外的依据。|The community’s small library normally closed at six. A four-week pilot extended Thursdays to eight, with other days unchanged. I support another four weeks because some workers found time to read, but not immediate daily extension or a claim that non-attendees dislike reading. Those broader judgments need separate support.
工作人员把四个周四的晚间到访分别记为十八、二十、十二和十四人次，共六十四人次。这些记录不包括负责的人。人次说明发生了多少次到访，不等于有六十四个不同的居民。一个人来了三次，就贡献三人次；如果要知道有多少不同的人，需要另一种记录，这次没有做。|The four Thursday evenings recorded eighteen, twenty, twelve and fourteen visitor entries, sixty-four total, excluding staff. These are visits rather than sixty-four distinct residents: one person attending three times contributes three. Unique attendance would require a different record that wasn’t kept.
有人说六十四太少，也有人说已经很多。我觉得先问清比较的对象，才能讨论这个差距。小厅只有三十个座位，不能拿一个晚上来的人数，直接和全社区的居民人数比较，再决定所有人的需要。记录里也没有写谁在外地、谁那个晚上要照顾家人，所以没有到场，并不能独自说明这个时间对他们没有价值。|Some judged sixty-four low, others high. We need to establish the comparison before interpreting a gap. The hall’s thirty seats and one evening’s attendance cannot directly represent the needs of the whole community. Records don’t show travel or caregiving conflicts, so absence alone cannot establish that the hours had no value.
延长开放不是没有成本。两位负责的人每次多留两小时，四周合起来是十六小时的人员时间，整理和关门也在这段时间里。这个数字不是两个人各自留了十六小时，更不是每位居民都花了十六小时。下个月能不能继续，先要问两个人的安排，有没有别人接手，不能只看到访者方便，就替负责的人答应。|Two staff each stayed two extra hours per evening: sixteen staff-hours across four weeks, including tidying and closing. It is not sixteen hours for each person or each resident. Next month depends on availability and potential replacements, not a promise made for staff solely because visitors benefit.
在评论里，有人建议把晚间改成交流活动，说一起聊天更能吸引人。我的主观感受正好不同：我下班以后想有一个安静地方，把没读完的几页读完。还有人愿意来讨论，我不认为他们错了；但在一个小厅里，两种活动同时进行，会有声音的矛盾。能否另找时间或地点，要先问场地安排，不能只把所有人放进去就当作两种需要都满足。|One comment proposed discussion to attract people. My own preference is a quiet place to finish reading after work. Others may want conversation too, but simultaneous activities in one small hall create noise conflict. A separate time or space needs checking; simply combining everyone doesn’t satisfy both needs.
我也担心，只收集来的人意见，会缺乏没来的群体的声音。如果他们说交通不方便，延长两小时可能没有解决那个问题；如果有人只在周二有空，也不能说周四的成效已经替他解决了。可以在原来的公告旁边留一个反馈办法，让愿意的人说明时间和原因，不强迫任何人解释自己的全部生活。|Only asking attendees leaves non-attendees’ views missing. Longer hours may not solve travel difficulty or a Tuesday-only schedule. A feedback channel by the existing notice could invite timing and reasons without demanding accounts of everyone’s whole life.
因此，我建议继续周四四周，把到访次数、安静阅读的情况和负责人的时间分别记下来。一次人多不算每次都好，一次下雨人少也不该直接终止。我们还不能排除天气和不同活动的影响，可以把情况写清，再作评估。继续试是为了检验安排能不能持续，不是先把想要的结论写好，再找数字装进去。|I propose four more Thursdays, recording visits, quiet reading and staffing time separately. One busy evening doesn’t prove all evenings work; one rainy low-attendance evening shouldn’t alone end the trial. Weather and other events remain possible influences. Continued testing should examine sustainability rather than fit numbers into a predetermined conclusion.
这个建议保留了我的期望，也承认它的限制。我希望下班以后有地方读，并愿意提前收好书，不让关门的人不断等。以后如果证据支持扩大，再讨论其他日子；如果人员时间不够，就先缩小或暂停。把支持说得有条件，不会使它变成反对，反而让下一步可以具体地问、具体地做。|I hope for a place after work and will pack before closing. Expansion can be discussed if supported; inadequate staffing may require reducing or pausing hours. Conditional support remains support, while making the next steps concrete.
''')
P=rows('''
我也是这个小图书馆的读者，但没有参加四周的周四晚间试办。不是因为我不需要晚上读书，而是周四有课，结束以后已经八点半。看到有人写“没有来就没有需要”，我想说明自己的情况。开放到八点，对一些人很合适，对我却还是有半小时的差距；这个差距不是一句“不够积极”能消除的。|I use the small library but didn’t attend the Thursday pilot because class ends at 8:30. Absence doesn’t mean no need for evening reading. Closing at eight suits some but leaves a half-hour gap for me, not a problem solved by calling me insufficiently keen.
我没有因此要求立刻延长到九点。听到两位工作人员每次已经多留两小时，我知道他们也有自己的安排。我希望以后评估时，能把像我这样没到场的人意见加进去，而不是由来得最多的人替大家作决定。也许别的日子更合适，也许根本没有足够人手，两个可能都需要先问。|I am not demanding immediate nine-o’clock closing. The two staff already stay two extra hours and have their own schedules. I want non-attendee views included, rather than frequent visitors deciding for all. Another day might suit or staffing might be insufficient; both need asking.
文章里的六十四人次，让我知道这个时间不是没人用。但是我不知道其中多少人只来一次、多少人常来，也不能算出他们在所有读者中的比重。总读者有多少，这次记录没有提供。缺了这个数字，就不能把六十四直接叫作大多数，或者反过来叫作没有价值的一小群人。|Sixty-four visits show use, but don’t reveal unique or repeat visitors or their share of all readers. Total readership is not given. The figure cannot establish either a majority or a supposedly worthless small minority.
有一个评论建议换成交流活动。我其实喜欢聊书，也想认识新朋友，可是如果好不容易找到安静时间，旁边一直有人说话，我就难以看下去。这并不矛盾：同一个人在不同时间，也可以想要不同活动。我愿意周末参加读书交流，但下课以后的短时间，常常只想安静读一会儿。|I like discussing books and meeting people, but constant nearby talk impedes quiet reading. Wanting different activities at different times is consistent. I might join a weekend discussion while preferring quiet reading after class.
如果真要找另外的地方交流，先确认房间能不能用、有没有人负责，再发通知。不能为了让评论里每个人满意，就在没有人接手的时候同时答应两场活动。我看见文章说先继续四周，觉得这个范围清楚；它没有替我解决周四八点半的问题，却给我们一个继续提供意见的时间。|Another discussion venue requires confirmed space and an organiser before notice. Promising two events with no one to run them doesn’t satisfy commenters. Another four-week pilot has a clear scope: it doesn’t solve my 8:30 issue but permits further feedback.
我后来写给负责人的意见很短：说明周四有课，问能不能在以后考虑别的晚间，不要求他们必须照我的时间。我也说愿意帮忙问几位同学，但不能代表整个学校。这样收集来的意见，至少能让他们知道这些人的具体安排；问了五个人，不等于完成了对所有学生的调查。|My feedback stated the Thursday class and asked about other evenings without demanding my own schedule. I offered to ask a few classmates, not represent a whole school. Five people’s detailed schedules would be useful but not a survey of all students.
负责人回复说，会把这些意见和到访记录放在一起看，先确认下个月的人手。我没有把这句答复理解成已经保证换日期，也没有觉得她一时不能答应就是不重视。她给出了下一步要做的事，我也可以等那个结果出来，再决定是否参加。能把暂时不知道的地方说清楚，反而比马上说什么都可以更可信。|The organiser would consider feedback with attendance and check next month’s staff. That is neither a guarantee to change days nor indifference if she cannot promise now. A concrete next step allows a later participation decision; clear uncertainty is more credible than agreeing to everything immediately.
所以，我赞成继续试，也希望最后的评估不要只留下一个总数。来的人读了什么、没来的人有哪些时间限制、负责的人还能不能继续，这些都不是同一个问题。把它们分开问，不会让讨论失去方向。我们仍然想让阅读方便一些，只是不把一种方便说成所有人的方便，也不把一个人的情况说成唯一答案。|I support further trial and an evaluation beyond one total. Reading needs, non-attendee timing constraints and staff availability are separate questions that can guide the shared aim of convenient reading without pretending one convenience fits all or one person has the sole answer.
''')
G=[
card('并不…','Reject a strong inference','并不 emphasises that a proposed inference does not hold. It can reject equivalence without asserting every possible opposite.','没有到场，并不说明没有需要。|Not attending does not establish no need.\n支持继续试，并不等于支持每天延长。|Supporting further trial is not supporting extension every day.','没有到场，并不说明没有需要，所以一定每天都需要。','没有到场，并不说明没有需要。','Rejecting one inference does not establish a different universal claim.'),
card('即使…，也…','Hold a result across a hypothetical condition','即使 introduces a hypothetical or extreme condition; 也 maintains the second clause. Compare actual concessions introduced by 尽管.','即使再试四周，也要先确认人手。|Even if we trial another four weeks, we still need to confirm staffing.\n即使我这周不来，也想知道以后的安排。|Even if I don’t come this week, I want to know later arrangements.','即使再试四周，所以不用确认人手。','即使再试四周，也要先确认人手。','The maintained requirement belongs after 也.'),
card('没有…，就没有…','State a necessary relationship','The pattern states dependence in the present argument; do not confuse necessary support with a sufficient guarantee of every outcome.','没有总人数，就没有计算比重的依据。|Without a total population there is no basis for the proportion.\n没有人关门，就没有继续试办的安排。|Without someone to close up there is no arrangement for continuing.','有总人数，就证明每个人都喜欢。','没有总人数，就没有计算比重的依据。','Knowing a denominator permits a proportion, not a claim about attitudes.'),
card('尽管…，但…','Acknowledge evidence without overstating it','The concession accepts the observed fact while limiting the larger claim.','尽管有人到场，但还不知道多少是第一次来。|Although people attended, we don’t know how many were first-time visitors.\n尽管我赞成继续，但不要求马上每天延长。|Although I favour continuing, I don’t demand daily extension immediately.','尽管有人到场，但所以人人一定都来了。','尽管有人到场，但还不知道多少是第一次来。','A concession should preserve rather than erase the limit.'),
card('凭… / 依据…','Identify the basis for a claim','凭 can introduce evidence or a basis; 依据 is common in organised explanation. Specify what that basis does and does not establish.','凭这四周的记录，还不能决定所有日子。|These four weeks’ records do not settle every day.\n我们依据到访记录和意见作评估。|We evaluate using visit records and feedback.','凭四周记录，就知道每位居民全部的安排。','凭这四周的记录，还不能决定所有日子。','The record’s scope is limited to this pilot.'),
]
spec=dict(title=('Evidence and a position','有依据，也有立场'),goals=['Read an opinion while distinguishing claims, observations and qualifications','Interpret visits, unique people and included staffing time accurately','Give conditional support and a bounded alternative'],vocabulary=V,grammar=G,
dialogue=(D,[q('gist','What position does the speaker support?','Continue the Thursday trial with checks','Guarantee daily extended hours immediately','Replace all quiet reading with compulsory conversation'),q('detail','How many times did the speaker attend?','Three','Sixty-four different times','None'),q('inference','Why mention staff availability?','Visitor convenience alone cannot guarantee continued opening','Staff are included in every attendance count','The pilot ran without anyone closing')]),
reading=(R,[q('gist','What does the author recommend?','Four more Thursdays with several separate checks','Permanent daily extension based solely on one total','Closing because one rainy evening was less busy'),q('detail','What is the sixteen-hour figure?','Combined additional staff-hours across four weeks','Sixteen extra hours for each of two staff every evening','Time spent by every visitor'),q('inference','What does sixty-four visits not tell us?','The number of distinct residents attending','That visits were recorded','That the four counts add to sixty-four')]),
pairedTitle='A reader who did not attend',pairedReading=(P,[q('gist','Why can the reader support a pilot they did not attend?','It benefits some readers while their own timing remains unresolved','They secretly attended every session','The organiser guarantees their preferred date immediately'),q('detail','When does the reader’s Thursday class end?','8:30','Six','Seven'),q('inference','What would asking five classmates establish?','Those classmates’ stated circumstances','A complete survey of all students','The needs of every resident')]),
mediaTitle='Three pages and twenty',media=(M,[q('detail','What differs between the books?','The amount of text on a page','Their closing time','The library used'),q('inference','Why question a comparison of page totals?','Page count alone ignores content and repeated reading','Pages never contain words','Twenty pages proves complete comprehension')]),
glosses=[('贡献','contribute'),('下降','decrease; go down'),('降','fall; decrease'),('人次','visits; person-times, not distinct people'),('人手','available staff or helpers'),('读者','reader'),('到访','visit'),('关门','close up'),('试办','run a pilot'),('讲台','lectern'),('居民','resident'),('分母','denominator'),('反馈','feedback'),('场地','venue'),('照顾','care for'),('唯一','only; sole'),('人员','personnel'),('开馆','open a library')],
place='Friends discussing a fictional community opinion article',context='The pilot extends Thursday closing from six to eight for four weeks. Visitor counts are 18, 20, 12 and 14, excluding staff; unique attendance was not recorded.',
turns=[('六十四人次就是六十四个不同的人，对吧？','Sixty-four visits means sixty-four distinct people, right?','Separate visits and unique people',['不一定，一个人来三次就是三人次。']),('你支持继续，就支持每天都开到八点？','Support for continuing means every day until eight?','Limit your position',['不是，我支持先继续周四，再评估。']),('问五个同学就代表全部学生了吗？','Do five classmates represent every student?','Keep the scope of feedback',['不能，只能先知道这五个人的情况。'])],
usage=[('Disagree with an inference','这个记录能说明有人来，还不能说明人人需要。','This record shows attendance, but not that everyone needs it.','Name both what is established and what remains open.'),('Offer bounded support','我赞成再试四周，前提是先确认人手。','I favour another four-week trial, provided staffing is confirmed.','The condition is part of the position, not a hidden promise.'),('Ask for the denominator','你说比重，比较的总人数是多少？','You mention a proportion; what is the total population being compared?','Ask what a numeric claim uses as its base.')],
tasks=practice(
[(R[1][0],R[1][1],'The record counts visits rather than unique residents.',True,'Repeat visitors contribute multiple entries.'),(R[3][0],R[3][1],'Each of the two staff stayed sixteen extra hours every evening.',False,'Sixteen is the combined four-week staff-hour total.'),(P[0][0],P[0][1],'The reader’s class ends after the pilot closes.',True,'Class ends at 8:30 and the library closes at eight.'),(P[6][0],P[6][1],'The reply guarantees a changed date.',False,'It promises to consider records and confirm staffing.')],
 [('一个人来了三次，记录是三人次。能确定是三个不同的人吗？','One person attended three times, yielding three visits. Does this establish three distinct people?',['不能，是同一个人来了三次。','能，人次一定就是不同的人数。','能，记录明确说三位居民各来一次。'],0,'The premise explicitly identifies a repeat visitor.'),('我支持先继续周四四周，不要求马上每天延长。我的立场是什么？','I support four further Thursdays, without immediate daily extension. What is my position?',['有条件地继续试周四。','马上永久延长每一天。','任何周四都必须立刻关闭。'],0,'Keep the stated scope and conditions.'),('总读者人数没提供，可以算到访者的比重吗？','The total number of readers is absent. Can we calculate visitors’ share?',['不能，还缺总人数。','可以，六十四已经告诉我们全部读者。','可以，没到场的人就不算读者。'],0,'The denominator is not available.')],
 [('只看总人数，这个依据太单一。','Total attendance alone is too one-dimensional a basis.','单一'),('还不能排除天气影响人数。','We cannot yet rule out the weather affecting attendance.','排除'),('我们依据到访记录和意见作评估。','We evaluate using visit records and feedback.','依据')],
 [[(V[i][3],V[i][4]) for i in [0,2,4]],[(V[i][5],V[i][6]) for i in [5,10,15]],[(V[i][3],V[i][4]) for i in [17,20,23]]]),
review='Native review: opinion register, 加以 collocations, 人次 explanation and humorous page-count exchange. The library and all counts are original fiction, not reported research. 18+20+12+14=64 visits; 2 staff × 2 hours × 4 evenings=16 staff-hours total. No unique attendance or denominator was recorded. Separate quiet reading from social discussion without pretending one room meets both needs simultaneously. Staffing and schedule conditions remain explicit; support is neither unconditional expansion nor refusal.')
spec['glosses'].extend([('吸引','attract'),('强迫','force; compel')])
write(5,10,spec,publish='--publish' in sys.argv)
