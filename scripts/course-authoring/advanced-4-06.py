"""Choose a course by real goals, deadlines and workload."""
import sys
from advanced_core import write,rows,words,q,card,practice
V=words('''
课程|course; classes|khóa học|这门课程每周上两次。|This course meets twice a week.|课程结束以后，我们还会一起练习。|We’ll keep practising together after the course ends.
参考|consult; use as a reference|tham khảo|你可以参考去年的课程表。|You can consult last year’s timetable.|这只是参考价格，实际费用还没定。|This is only an indicative price; the actual fee isn’t fixed yet.
选择|choose; choice|lựa chọn|你为什么选择晚上的班？|Why did you choose the evening class?|这次有三种选择，不用马上决定。|There are three options this time; you don’t need to decide immediately.
申请|apply; application|đăng ký; xin|我准备申请下个月的课程。|I’m planning to apply for next month’s course.|申请通过以后，学校会发邮件通知你。|The school will email you after your application is approved.
本科|undergraduate degree; undergraduate|bậc đại học|她本科读的是中文。|She studied Chinese for her undergraduate degree.|本科毕业以后，他先工作了两年。|He worked for two years after completing his undergraduate degree.
毕业|graduate|tốt nghiệp|我姐姐去年毕业了。|My sister graduated last year.|毕业前，我们想再一起去一次海边。|Before graduation, we’d like one more trip to the sea together.
充分|sufficient; fully|đầy đủ|我还没充分了解这门课，想先问问。|I don’t know enough about this course yet and want to ask some questions.|准备充分以后，我说话没那么紧张了。|After preparing thoroughly, I felt less nervous speaking.
材料|material; documents|tài liệu; vật liệu|申请材料要在周五前交齐。|All application documents must be submitted before Friday.|这些材料太重，一次拿不完。|These materials are too heavy to carry in one trip.
条件|condition; requirement|điều kiện|报名条件是什么？|What are the enrolment requirements?|这里条件不错，但离家有点远。|The facilities here are good, but it’s a little far from home.
兴趣|interest|hứng thú|我对电影里的日常对话很有兴趣。|I’m interested in everyday dialogue in films.|这本书让我对历史产生了兴趣。|This book sparked my interest in history.
目的|purpose; aim|mục đích|你来上课的目的是什么？|What’s your aim in taking classes?|这次见面的目的不是讨论钱。|The purpose of this meeting isn’t to discuss money.
水平|level; standard|trình độ|我的阅读水平比听力好一点。|My reading is a little stronger than my listening.|这家店的服务水平一直不错。|This shop’s service has consistently been good.
安排|arrange; arrangement|sắp xếp|我想先安排好周末的时间。|I’d like to sort out my weekend schedule first.|老师已经安排了两次讨论。|The teacher has arranged two discussions.
费用|costs; fees|chi phí|这个费用包括材料吗？|Does this fee include the materials?|交通费用由我们三个人分。|The three of us will split the transport costs.
适合|suit; be suitable for|phù hợp|这门课适合已经学过基础的人。|This course suits people who’ve studied the basics.|这双鞋不适合走很远的路。|These shoes aren’t suitable for long walks.
决定|decide; decision|quyết định|我想看完介绍再决定。|I’d like to read the description before deciding.|我们决定周六在车站见。|We decided to meet at the station on Saturday.
''')
D=rows('''
你不是想报名吗？怎么还在看课程介绍？|Weren’t you going to enrol? Why are you still reading the descriptions?
一个班练口语，一个班读文章。我两个都想选。|One class practises speaking; the other reads articles. I want both.
时间不一样？|Are they at different times?
都在周三晚上。选阅读的话，周末还能参加免费的口语活动。|They’re both on Wednesday evenings. If I choose reading, I can join a free speaking activity at the weekend.
那听起来挺适合你。你不是说平时没机会读长一点的东西？|That sounds like a good fit. Didn’t you say you rarely get to read anything longer?
对。不过报名条件写着要先完成基础课程，我不知道以前的课算不算。|Right, but enrolment requires a foundation course. I don’t know whether my earlier class counts.
先问老师，别自己猜。申请什么时候结束？|Ask the teacher first rather than guessing. When do applications close?
周五前要交齐材料。今天才周一，还有时间。|All documents have to be in before Friday. It’s only Monday today, so there’s time.
费用呢？别看见免费活动就忘了课程的钱。|What about the fee? Don’t forget the course costs just because the activity’s free.
一千二，包括课本。我已经问清楚了。|Twelve hundred, including the textbook. I’ve already checked.
不错，这次准备得比我充分。选好了周末叫我一起去。|Good, you’re better prepared than I am this time. Once you’ve chosen, invite me along at the weekend.
行。不过先说好，你不能只在旁边点头。|Sure. But let’s be clear: you can’t just stand there nodding.
''')
R=rows('''
我以前选课程，总是先看时间和价格。只要有空、费用不高，就觉得可以试试。上了几次以后，才发现有些课并不适合自己的目的。|I used to choose courses mainly by time and price. If I was free and the fee wasn’t high, I’d try one. After a few classes, I sometimes found it didn’t fit my goals.
这次我先写了两件想做的事：读懂朋友推荐的短文章，和新认识的人聊得久一点。考试当然也重要，但我不想只会选答案。|This time I wrote down two things I wanted to do: understand short articles friends recommended and talk longer with people I’d just met. Exams mattered too, but I wanted more than choosing answers.
我参考了课程介绍，也给老师写了邮件。老师说，阅读班每周读一篇文章，再讨论不同的看法；周末的口语活动没有作业，不过参加的人水平不完全一样。|I consulted the descriptions and emailed the teacher. The reading class uses one article a week with discussion of different views. The weekend speaking activity has no homework, but participants have different levels.
老师看过我以前的学习材料以后，说我可以报名阅读班。她还提醒我，申请不是交一张表就结束，周五前要交齐两份材料。|After looking at my previous study material, the teacher said I could enrol in reading. She reminded me that applying meant more than submitting a form: both documents were due before Friday.
我没有同时报第二门课。每周读完一篇文章、准备讨论，再加一次口语活动，已经需要不少时间。先把这个安排坚持四周，再决定要不要增加。|I didn’t enrol in a second course as well. Reading an article, preparing for discussion and joining one speaking activity each week already took time. I’d keep that routine for four weeks before deciding whether to add more.
报名成功那天，朋友问我能不能马上看懂整部电影。我说还不能，不过下周见到新同学，至少知道该从什么话题开始了。|When my enrolment was confirmed, a friend asked whether I could immediately understand a whole film. I said no, but at least I’d know how to start talking to my new classmates next week.
''')
M=rows('''
你把表交了？|Did you submit the form?
交了，课本也拿到了。老师说下周带一篇自己喜欢的短文章。|Yes, and I’ve got the textbook. The teacher asked us to bring a short article we like next week.
你打算带什么？|What will you bring?
还没决定。你上次发我的那篇挺有意思。|I haven’t decided. That one you sent me was interesting.
那篇太长了，你不是说带短文章吗？|That one’s too long. Didn’t you say a short article?
所以我想问问你，有没有同一个作者写的短一点的。|That’s why I wanted to ask whether the same writer has anything shorter.
有，我找给你。你可别把我的回复也当文章交了。|Yes, I’ll find one. Just don’t submit my reply as the article.
那得看你回复多长。|That depends on how long your reply is.
''')
G=[
card('对…来说','Frame a judgment from a specific perspective','Place the person or group after 对 and before 来说. The comment is relevant to that perspective; it is not automatically true for everyone.','对我来说，周末比晚上方便。|For me, weekends are more convenient than evenings.\n对刚开始学的人来说，这篇文章太长了。|For beginners, this article is too long.','对我来说大家都一定喜欢这门课。','对我来说，这门课比较合适。','A personal perspective does not establish everyone else’s preference.'),
card('只要…就…','Present a sufficient condition','只要 gives a condition the speaker treats as enough for the outcome. It does not claim the condition is the only route; that distinction matters for eligibility statements.','只要材料交齐，就可以开始审核。|Once all documents are in, the review can start.\n只要周末有空，我就来参加。|If I’m free at the weekend, I’ll join.','只要材料交齐，才可以开始审核。','只要材料交齐，就可以开始审核。','Use 就 with a sufficient condition; 只有…才 expresses a necessary one.'),
card('只有…才…','State a necessary requirement','只有 introduces what must be satisfied; 才 indicates the outcome becomes available after that condition. A requirement does not guarantee success by itself.','只有完成基础课程，才可以申请。|You can apply only after completing the foundation course.\n只有把时间安排好，才能坚持下来。|Only by organising your time can you keep it up.','只有完成基础课程，就一定能被录取。','只有完成基础课程，才可以申请。','Eligibility to apply is different from guaranteed admission.'),
card('先…再决定要不要…','Delay a decision until after evidence','先 names an action that supplies information; 再 introduces a later decision. 要不要 embeds the yes/no choice inside the sentence.','先坚持四周，再决定要不要增加。|Keep it up for four weeks, then decide whether to add more.\n先问清楚，再决定要不要报名。|Ask for the details first, then decide whether to enrol.','再决定报名，先问清楚，所以我还没决定。','先问清楚，再决定要不要报名。','The ordering should reflect that the information comes before the decision.'),
]
spec=dict(title=('Choose a course that fits your life','这门课适合我吗'),goals=['Compare two course options against your study goals','Ask about entry requirements and application deadlines','Explain a sustainable study choice to a friend'],vocabulary=V,grammar=G,dialogue=(D,[q('gist','What choice is being considered?','A reading course plus weekend speaking activity','Two Wednesday classes at the same time','Giving up study entirely'),q('detail','What does the 1,200 fee include?','The textbook','All future transport','A professional degree'),q('inference','Why ask the teacher about the earlier class?','To check whether it satisfies the foundation requirement','To demand a free textbook','To move the deadline to Monday')]),reading=(R,[q('gist','What is different about this course choice?','Goals and workload guide it','Only the cheapest price matters','The narrator enrols in every available class'),q('detail','How long will the narrator try the routine before adding more?','Four weeks','Four days','A year'),q('inference','What does the final reply show?','The narrator sees a practical next step without claiming instant fluency','The narrator already understands every film','The narrator will never speak to classmates')]),mediaTitle='A short article, please',media=(M,[q('detail','What is needed for next week?','A short article the learner likes','Every message from the friend','A full-length book'),q('inference','Why ask for a shorter piece by the same writer?','The recommended piece is interesting but too long','The writer has stopped writing','The teacher banned that writer')]),glosses=[('报名','enrol'),('审核','review an application'),('录取','admit to a school or course'),('点头','nod'),('课本','textbook'),('交齐','submit all required items'),('两份','two copies or documents'),('作者','writer; author')],place='Choosing a course with a friend',context='Two classes share a Wednesday slot; one can be combined with a free weekend speaking activity.',turns=[('你为什么选这个班？','Why choose this class?','Connect the choice to a goal',['我想练习读文章，也想和同学讨论。']),('以前的课算吗？','Does the earlier class count?','Ask for verification',['我想先问老师是否符合报名条件。']),('还要再选一门吗？','Will you add another class?','Defer a decision until after a trial',['我先坚持四周，再决定要不要增加。'])],usage=[('Separate price from included items','这个费用包括课本吗？','Does this fee include the textbook?','A total price does not by itself tell you which items are included.'),('Ask instead of assuming eligibility','我以前上过基础课，符合报名条件吗？','I took a foundation course before. Do I meet the requirements?','State your background and ask whether it satisfies the actual requirement.')],tasks=practice([(D[3][0],D[3][1],'Both classes meet on Wednesday evenings.',True,'The speaker says 都在周三晚上.'),(R[4][0],R[4][1],'The narrator immediately adds a second course.',False,'The narrator tries one routine first.')],[('我不知道以前的课算不算，老师还没看材料。怎么办？','I don’t know whether my earlier class counts; the teacher hasn’t seen the documents. What should I do?',['先把材料给老师看，问清楚。','没看材料也已经确定不能申请了。','没看材料也已经确定符合要求了。'],0,'The reply proposes checking the prerequisite.'),('两门都在周三晚上，我只能上一门。怎么决定？','Both classes meet Wednesday evenings; I can attend only one. How should I decide?',['我先比较时间和目的，再决定。','时间相同，就可以同时去两门课。','只要课名好听，就一定符合我的目的。'],0,'The reply describes the relevant choice process.')],[('我想参考去年的课程表。','I want to consult last year’s timetable.','参考'),('只有完成基础课程，才可以申请。','You can apply only after completing the foundation course.','才')],[[(V[i][3],V[i][4]) for i in [2,6,10]],[(V[i][5],V[i][6]) for i in [7,12,14]]]),review='Native review: college/course terminology and friendly final tease. Deadline means before Friday, not including Friday. A completed foundation course permits application; admission is not promised. A four-week trial is a personal plan, not a validated universal study prescription.')
spec['glosses'].extend([('免费','free of charge'),('历史','history')])
write(4,6,spec,publish='--publish' in sys.argv)
