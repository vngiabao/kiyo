"""Authored compliments, comparisons, walks and plan-confirmation units."""
from common import *
character_groups.update({
25:[('穿','to wear'),('贵','expensive'),('非','not; very in 非常'),('很','quite; very'),('太','too; very'),('差','poor; difference'),('医','medical; to treat'),('茶','tea'),('牛','cow'),('冷','cold'),('热','hot'),('个','general classifier'),('客','guest'),('岁','year of age')],
26:[('比','to compare; than'),('场','field; place'),('馆','public building'),('教','to teach'),('商','commerce'),('住','to live; stay'),('房','room; house'),('雨','rain'),('风','wind'),('快','fast'),('慢','slow'),('假','leave; holiday'),('难','difficult'),('试','to try; test')],
27:[('出','to go out'),('回','to return'),('跑','to run'),('行','okay; to go'),('都','all'),('玩','to play'),('饭','meal; cooked rice'),('面','face; noodles'),('桌','table'),('唱','to sing'),('歌','song'),('饿','hungry'),('告','to tell in 告诉'),('诉','to tell in 告诉')],
28:[('吧','suggestion particle'),('呢','question or continuing-action particle'),('过','to pass; spend'),('就','just; then'),('飞','to fly'),('考','to examine; test'),('您','polite you'),('哥','older brother'),('道','way; to know in 知道'),('果','fruit; result'),('气','air; mood'),('系','relation; connection'),('样','appearance; kind'),('怎','how in 怎么')],
})
character_contexts.update({'医':('医生','doctor'),'桌':('桌子','table'),'茶':('茶','tea'),'哥':('哥哥','older brother'),'系':('没关系','it is okay; never mind')})
unit_glosses.update({25:{'衣服':'clothes','换':'to change','颜色':'colour','平时':'usually','笑话':'joke','夸':'to compliment'},
26:{'安静':'quiet','声音':'sound','人多':'crowded','座位':'seat','硬':'hard','水杯':'drinking cup'},
27:{'散步':'to take a walk','聊天':'to chat','安全':'safety; safe','路灯':'streetlight','口袋':'pocket'},
28:{'确认':'to confirm','航班':'flight','张':'Zhang, a surname','证件':'identity document','通知':'notice','报名':'to register'}})
unit_glosses[25].update({'普通':'ordinary','练':'to practise','但':'but','另':'another; other'})
unit_glosses[26].update({'湿':'wet','让':'to let; allow','选':'to choose'})
unit_glosses[27].update({'但':'but','不一定':'not necessarily'})
unit_glosses[28].update({'发':'to send'})
dictionary.update({'一块儿':'yī kuàir','一下儿':'yī xiàr'})
u='s1-u25'
dictionary['干']='gān'
write(25,'具体一点的夸奖',['Give a specific compliment without exaggerating','Use an adjective predicate without adding 是','Recognize an exclamation without treating every 太 as praise'],[
('很','quite; very','khá; rất','adverb','这件衣服很好看。','This item of clothing looks good.'),
('真','really; truly','thật; rất','adverb','这个颜色真好看。','This colour looks really good.'),
('真的','really; true','thật sự','adverb','我真的喜欢这个颜色。','I really like this colour.'),
('觉得','to feel; think','cảm thấy; nghĩ','verb','我觉得白色很好看。','I think white looks good.'),
('有名','well-known','nổi tiếng','adjective','这家商店很有名。','This shop is well-known.'),
('一样','the same','giống nhau','adjective','这两个杯子的颜色一样。','The two cups are the same colour.'),
('身上','on the body; on one’s person','trên người','noun','你身上的衣服很好看。','The clothes you are wearing look good.'),
('重','heavy','nặng','adjective','这个包很重。','This bag is heavy.'),
('干','dry','khô','adjective','这件衣服还没干。','This item of clothing is not dry yet.'),
('开玩笑','to joke','đùa','verb','我没有开玩笑，真的很好看。','I am not joking; it really looks good.'),
('生气','to get angry','giận','verb','别生气，我在开玩笑。','Do not get angry; I am joking.'),
('差','poor; bad','kém','adjective','我的汉语还很差，还要多练。','My Chinese is still poor; I need more practice.'),
('看见','to see','nhìn thấy','verb','我看见你身上的新衣服了。','I saw the new clothes you are wearing.'),
('看到','to see','nhìn thấy','verb','我看到这个颜色了。','I saw this colour.'),
('早','early','sớm','adjective','现在还早。','It is still early.'),
('晚','late','muộn','adjective','现在太晚了，明天再看吧。','It is too late now; let us look again tomorrow.'),
('最好','best; had better','tốt nhất','adverb','这三件衣服，我觉得白色的最好看。','Of these three, I think the white one looks best.')],
[grammar(u,'一09','很 / 非常 / 太 / 真 / 最 + adjective','Choose the strength of a description',
'很 often makes a neutral adjective predicate natural and need not mean an unusually high degree. 非常 is stronger. 真 gives a sincere reaction. 太…了 can praise or complain according to the adjective and context: 太好看了 / 太贵了. 最 selects the highest degree within an understood set; make the comparison set clear.',[
('这件衣服很好看，那件非常好看。','This item looks good; that one looks very good.'),('这个颜色真好看，太好看了！','This colour looks really good—so good!'),('这三件，白色的最好看。','Of these three, the white one looks best.')],
('这件衣服最很好看。','这三件衣服，白色的最好看。','Use 最 without 很 before the same adjective, and state the comparison set.')),
grammar(u,'一30','subject + degree word + adjective','Describe an attribute directly',
'An adjective can be the predicate: 包很重; 衣服很好看. Do not routinely put 是 before it. In a neutral positive sentence 很 is often useful without strong “very”; a contrast can omit it, as 白色好看，黑色不好看. Negative adjectives use 不: 不重. A context-sensitive adjective needs an appropriate subject.',[
('这个包很重，那个不重。','This bag is heavy; that one is not.'),('衣服还没干，现在不冷。','The clothes are not dry yet; it is not cold now.')],
('这个包是很重。','这个包很重。','Do not add 是 to this neutral adjective predicate.')),
grammar(u,'一35','太…了！ · 真…！','React with a real exclamation',
'A positive reaction can use 太好看了！ or 真好看！; a complaint can use 太晚了！. The delivery and context carry the emotion. Exclamation marks do not change an ordinary statement into a question. A plain compliment is also valid; choose the intensity to suit the relationship.',[
('真好看！','That really looks good!'),('太晚了！明天再看吧。','It is too late! Let us look again tomorrow.')],
('真好看吗！','真好看！','Use a statement exclamation for praise, not 吗 unless you mean a question.'))],
text(u,'d','A compliment with a reason','Find what is praised and whether the friend is joking.',[
('我看见你身上的新衣服了。真好看！','I saw your new clothes. They look really good!'),('真的？我觉得白色很普通。','Really? I think white is ordinary.'),
('这三件衣服，白色的最好看。颜色和你的包一样。','Of these three, the white one looks best. It is the same colour as your bag.'),('这家商店很有名，不过这个包很重。','This shop is well-known, but this bag is heavy.'),
('我看到那个小包了，它不重。你可以换一个。','I saw that small bag; it is not heavy. You could change to it.'),('你在开玩笑吗？我平时不穿白色。','Are you joking? I do not usually wear white.'),
('没开玩笑，我真的觉得好看。别生气。','I am not joking; I really think it looks good. Do not get angry.'),('没有生气。昨天那件衣服还没干。','I am not angry. Yesterday’s clothes are still not dry.'),
('今天的颜色不差，唱歌的声音也很好听。','Today’s colour is good, and your singing voice sounds good too.'),('我的汉语还很差，还要多练。','My Chinese is still poor; I need more practice.'),
('现在还早，先喝茶，再唱一次吧。','It is still early. Have tea first, then sing once more.'),('好，但别太晚。太晚了，明天上学会累。','Okay, but not too late. If it is too late, school tomorrow will be tiring.')],
[('mainidea','What does the friend praise specifically?',['The white clothes and colour match','The bag’s weight','An exam score'],0),('detail','Why change the bag?',['It is heavy','It is wet','It belongs to a teacher'],0),('inference','Is the compliment intended as a joke?',['No, the friend explicitly denies joking','Yes, the friend admits it','The friend has not seen the clothes'],0)],drama=True),
text(u,'r','After the compliment','Find the concrete praise and the practical plan.',[
('今天朋友看见我身上的白衣服，说真好看。','Today a friend saw the white clothes I was wearing and said they looked really good.'),
('我觉得白色很普通，他真的喜欢这个颜色。','I think white is ordinary; he really likes this colour.'),
('这三件衣服，白色的最好看，和包的颜色一样。','Of these three items, the white one looks best and matches the bag’s colour.'),
('商店很有名，可是我的包很重，另一个包不重。','The shop is well-known, but my bag is heavy; another bag is not.'),
('昨天的衣服还没干，今天先穿白色。','Yesterday’s clothes are not dry yet; today I will wear white first.'),
('朋友说没开玩笑，我也没有生气。','My friend said he was not joking, and I was not angry.'),
('我的汉语还很差，还想练一次。','My Chinese is still poor; I would like to practise once more.'),
('现在还早，我们先喝茶，再唱歌，不要太晚。','It is still early. We will have tea first, then sing, without staying too late.')],
[('mainidea','What is the writer describing?',['A specific compliment and an evening plan','A new examination','How to make clothes'],0),('detail','Why wear white today?',['The other clothes are not dry','White is required for school','The bag is new'],0),('inference','Does sincere praise mean the writer has nothing to improve?',['No, the writer still wants Chinese practice','Yes, no practice is needed','The friend gives a formal grade'],0)],[(2,'一样'),(4,'干')]),
text(u,'media','Not a joke','Hear a friendly compliment in an original scene.',[
('我看到你的衣服了，白色的真好看。','I saw your clothes; the white one looks really good.'),('真的？不是开玩笑？','Really? You are not joking?'),
('真的。这三件里，我觉得这件最好看。','Really. Of these three, I think this one looks best.'),('那就好，我没有生气。昨天那件还没干。','Good, then. I am not angry. Yesterday’s item is still not dry.'),
('包太重了，换小包吧。现在还早。','The bag is too heavy; change to the small one. It is still early.'),('好，先喝茶，再唱歌。别太晚。','Okay, tea first, then singing. Not too late.')],
[('inference','What makes the praise concrete?',['It identifies the white item among three','It promises a high exam score','It praises every possible item'],0)],drama=True),
dict(tf=[('重','这个包很重。','This bag is heavy.','The bag is light.',False,'重 means heavy.'),('开玩笑','我没有开玩笑。','I am not joking.','The speaker says this is sincere.',True,'没有开玩笑 denies joking.')],
reply=[('觉得','你觉得哪个好看？','Which do you think looks good?',['我觉得白色的好看。','昨天七点。','在车站。'],0,'Give a specific judgment.'),('干','衣服干了吗？','Are the clothes dry yet?',['还没干。','三个人。','我下车了。'],0,'Answer about dryness, gān.')],
fill=[('真','这个颜色真好看。','This colour looks really good.'),('最好','这三件，白色的最好看。','Of these three, the white one looks best.')],
match=[('身上',[('你身上的衣服很好看。','The clothes you are wearing look good.'),('这个颜色和包一样。','This colour is the same as the bag’s.'),('现在还早。','It is still early.')]),('差',[('我的汉语还很差。','My Chinese is still poor.'),('现在太晚了。','It is too late now.'),('这家店很有名。','This shop is well-known.')])]),
[('Specific praise','这个颜色真好看。','This colour looks really good.','Praise something you actually noticed instead of claiming all abilities are perfect.'),('Reassuring after teasing','没开玩笑，我真的觉得好看。','I am not joking; I really think it looks good.','Clarify sincerity if the friend seems uncertain.')],
[('你在开玩笑吗？','Are you joking?','Say the compliment is sincere',['没开玩笑，我真的觉得好看。']),('衣服干了吗？','Are the clothes dry?','Say not yet',['还没干。'])],
'Native check: specific compliment register and 太 in praise versus complaint. Self-review replaced the awkward singing-voice 差 wording with a natural language-proficiency example. 干 is gān dry, distinct from gàn do.')
dictionary['干']='gàn'

u='s1-u26'
dictionary['地']='dì'
write(26,'选个安静的地方',['Compare two study places','Use 比 and 没有 in the right comparison direction','Choose a place using practical reasons'],[
('比','than; compare','hơn; so sánh','preposition','图书馆比商场安静。','The library is quieter than the shopping centre.'),
('图书馆','library','thư viện','noun','我想去图书馆读书。','I would like to read at the library.'),
('教学楼','teaching building','tòa nhà giảng dạy','noun','教学楼在学校里面。','The teaching building is inside the school.'),
('饭店','restaurant; hotel depending on context','nhà hàng; khách sạn tùy ngữ cảnh','noun','这家饭店的菜很好吃。','The food at this restaurant is tasty.'),
('商场','shopping centre; department store','trung tâm mua sắm','noun','商场里人很多。','There are many people in the shopping centre.'),
('商店','shop','cửa hàng','noun','这家商店有水杯。','This shop has drinking cups.'),
('快','fast','nhanh','adjective','这辆车很快。','This vehicle is fast.'),
('慢','slow','chậm','adjective','走路比坐车慢。','Walking is slower than taking a vehicle.'),
('病人','patient; sick person','người bệnh','noun','病人在家休息。','The patient is resting at home.'),
('生病','to become ill; be ill','bị bệnh','verb','朋友生病了，今天请假。','My friend is ill and is taking leave today.'),
('渴','thirsty','khát','adjective','我很渴，想喝水。','I am thirsty and would like water.'),
('雨','rain','mưa','noun','今天的雨很大。','The rain is heavy today.'),
('住','to live; stay','sống; ở','verb','我住在学校旁边。','I live next to the school.'),
('地','ground; land','đất; mặt đất','noun','这里的地很干。','The ground here is dry.'),
('请假','to request leave','xin nghỉ','verb','我生病了，想请假。','I am ill and would like to request leave.'),
('放假','to have a holiday; be on break','được nghỉ','verb','学校明天放假。','The school has a holiday tomorrow.'),
('次','time; occasion','lần','measure word','我去过一次这家饭店。','I have been to this restaurant once.')],
[grammar(u,'一18','A + 比 + B + adjective','Name the comparison reference',
'比 introduces the reference B: 图书馆比商场安静 compares the library with the shopping centre. Keep the adjective after both A and B. Do not add 很 before that adjective in this simple comparison. State the same attribute for both things; 比 does not mean every attribute is better.',[
('图书馆比商场安静。','The library is quieter than the shopping centre.'),('坐车比走路快。','Taking a vehicle is faster than walking.')],
('图书馆比商场很安静。','图书馆比商场安静。','Do not insert 很 in this basic 比 comparison.')),
grammar(u,'一38','A 比 B + adjective · A 没有 B + adjective','Keep the direction of a comparison clear',
'A 比 B 快 means A is faster than B. A 没有 B 快 means A is not as fast as B. It does not mean A lacks B. This negative comparison differs from A不比B快, which need not assert that A is slower; here practise 没有. Compare objects on a relevant shared attribute.',[
('走路没有坐车快。','Walking is not as fast as taking a vehicle.'),('商场没有图书馆安静。','The shopping centre is not as quiet as the library.')],
('走路比坐车没有快。','走路没有坐车快。','Put 没有 between A and B for not-as comparison.'))],
text(u,'d','Quiet, close, and open','Find the place they choose and the alternative they reject.',[
('今天去商场还是图书馆？','The shopping centre or the library today?'),('图书馆比商场安静，我想读书。','The library is quieter than the shopping centre; I would like to read.'),
('你住在哪里？图书馆远吗？','Where do you live? Is the library far?'),('我住在教学楼旁边。走路很慢，坐车快一点。','I live beside the teaching building. Walking is slow; taking a vehicle is a little faster.'),
('今天雨大，外面的地很湿。坐车吧。','The rain is heavy and the ground outside is wet. Let us take a vehicle.'),('行。我很渴，先在商店买水，再去图书馆。','Okay. I am thirsty; first buy water at the shop, then go to the library.'),
('这家饭店的菜好吃，要先吃饭吗？','This restaurant has tasty food. Shall we eat first?'),('我去过一次。它没有图书馆安静，先读书吧。','I have been once. It is not as quiet as the library; let us read first.'),
('朋友今天请假，是生病了吗？','Our friend took leave today. Is she ill?'),('对，病人在家休息，我们不用等她。','Yes, she is resting at home; we do not need to wait for her.'),
('学校明天放假，教学楼不开门。图书馆呢？','The school has a holiday tomorrow and the teaching building is closed. What about the library?'),('明天不知道。今天开门，我们今天去。','I do not know about tomorrow. It is open today, so we will go today.')],
[('mainidea','What do they choose?',['The library for reading','The shopping centre for an exam','A restaurant for a meeting'],0),('detail','Where do they buy water?',['The shop','The teaching building','The friend’s home'],0),('inference','Why discuss opening rather than assume tomorrow is suitable?',['A school holiday may affect access','Every library closes permanently','They have already visited tomorrow'],0)],drama=True),
text(u,'r','A place comparison','Find the actual reasons for the choice, not a universal ranking.',[
('我住在教学楼旁边，今天想去图书馆。','I live beside the teaching building and would like to go to the library today.'),
('图书馆比商场安静，商场里人多。','The library is quieter than the shopping centre; the shopping centre is crowded.'),
('我去过一次旁边的饭店，菜好吃，可是没有图书馆安静。','I have visited the nearby restaurant once. The food is good, but it is not as quiet as the library.'),
('今天雨很大，地上有水，外面的地不干。','There is heavy rain today; water is on the ground and the ground outside is not dry.'),
('走路比坐车慢，所以我们先坐车到商店。','Walking is slower than taking a vehicle, so we will go to the shop by vehicle first.'),
('我很渴，在商店买水，再去读书。','I am thirsty; I will buy water at the shop, then go and read.'),
('朋友生病请假了，今天在家休息，不等她。','Our friend is ill and took leave; she is resting at home today, so we will not wait for her.'),
('学校明天放假，今天图书馆开门，我们今天去。','The school has a holiday tomorrow; the library is open today, so we will go today.')],
[('mainidea','Why choose the library today?',['It is quiet and known to be open today','It sells cheap food','It has no books'],0),('detail','Why is the friend absent?',['She is ill and took leave','She is at the shopping centre','She is teaching'],0),('inference','Does quietness alone settle every practical choice?',['No, transport and opening also matter','Yes, opening never matters','No one compares quietness'],0)],[(1,'比'),(6,'请假')]),
text(u,'media','Not all places do the same job','Read an original verse comparing useful places.',[
('商场人多，图书馆安静。饭店菜好吃，读书不一样。','The shopping centre is crowded; the library is quiet. The restaurant has good food; reading is another matter.'),
('我住教学楼旁边，雨大，地不干。','I live beside the teaching building; heavy rain, wet ground.'),
('走路慢，坐车快。商店买水，我很渴。','Walking is slow; taking a vehicle is fast. Buy water at the shop; I am thirsty.'),
('朋友生病，请假休息。不等病人，让她好好睡。','Our friend is ill; leave and rest. Do not wait for her; let her sleep well.'),
('去过一次饭店，没有图书馆安静。','Visited the restaurant once; not as quiet as the library.'),
('明天放假，今天开门。选今天，先读书。','A holiday tomorrow; open today. Choose today and read first.')],
[('detail','Which place is chosen for reading?',['The library','The restaurant','The shopping centre'],0)]),
dict(tf=[('比','走路没有坐车快。','Walking is not as fast as taking a vehicle.','Walking is faster.',False,'没有…快 is not-as-fast.'),('放假','学校明天放假。','The school has a holiday tomorrow.','The school holiday is tomorrow.',True,'明天 gives the day.')],
reply=[('渴','你想喝水吗？','Would you like water?',['想，我很渴。','我九点下车。','两本书。'],0,'State the need for water.'),('请假','为什么今天请假？','Why take leave today?',['我生病了。','这本书一百页。','汽车是蓝色的。'],0,'Give the reason.')],
fill=[('商场','商场没有图书馆安静。','The shopping centre is not as quiet as the library.'),('慢','走路比坐车慢。','Walking is slower than taking a vehicle.')],
match=[('地',[('这里的地很干。','The ground here is dry.'),('今天的雨很大。','The rain is heavy today.'),('病人在家休息。','The patient is resting at home.')]),('快',[('坐车比走路快。','Taking a vehicle is faster than walking.'),('教学楼在学校里面。','The teaching building is inside the school.'),('我住在学校旁边。','I live next to the school.')])]),
[('Choosing a place','图书馆比商场安静，我们去那里吧。','The library is quieter than the shopping centre; let us go there.','Tie the comparison to the shared activity rather than insulting a place.'),('Respecting an absent friend','她生病了，今天先休息。','She is ill; let her rest today.','Do not diagnose or suggest treatment; this is coordination about attendance.')],
[('去哪里读书？','Where shall we read?','Choose the library',['去图书馆吧。']),('走路快还是坐车快？','Is walking or taking a vehicle faster?','Say taking a vehicle',['坐车比走路快。'])],
'Native check: quietness comparisons, 饭店 restaurant versus hotel context, and referral to a sick friend without repeatedly calling her 病人. 地 is dì ground, not de.')
dictionary['地']='de'

u='s1-u27'
write(27,'一起走一会儿',['Combine two compatible activities','Use 都 for a whole stated group and 一起/一块儿 for togetherness','Distinguish hearing a sound from understanding its meaning'],[
('一块儿','together','cùng nhau','adverb','我们一块儿去散步吧。','Let us go for a walk together.'),
('一边','one side; while in paired actions','một bên; vừa…vừa…','adverb','我们一边走，一边聊天。','We walk and chat at the same time.'),
('有些','some','một số','pronoun','有些朋友想走，有些想坐车。','Some friends want to walk; some want to take a vehicle.'),
('行','okay; all right','được','verb','先回家，再出来，行吗？','Go home first, then come out again. Would that work?'),
('走','to walk; leave','đi bộ; rời đi','verb','我们现在走吧。','Let us leave now.'),
('跑','to run','chạy','verb','别跑，路上车很多。','Do not run; there is heavy traffic.'),
('听到','to hear','nghe thấy','verb','我听到你说话了。','I heard you speaking.'),
('听见','to hear','nghe thấy','verb','我听见旁边有人唱歌。','I hear someone singing nearby.'),
('出','to go out; exit','ra','verb','我下午出门。','I go out in the afternoon.'),
('出来','to come out','ra đây','verb','你先出来，我在楼下。','Come out first; I am downstairs.'),
('回','to return','về','verb','我先回家。','I will go home first.'),
('回到','to return to','trở về','verb','我七点回到家。','I return home at seven.'),
('回来','to come back','quay về đây','verb','你什么时候回来？','When are you coming back?'),
('回去','to go back','trở về đó','verb','太晚了，我要回去。','It is too late; I need to go back.'),
('开','to open; turn on','mở; bật','verb','我开门，你先出来。','I will open the door; come out first.'),
('打','to make in 打电话; hit','gọi trong 打电话; đánh','verb','我先打电话，再出门。','I will call first, then go out.'),
('一下儿','a brief action; a moment','một chút','measure word','你等一下儿，我马上出来。','Wait a moment; I will come out right away.')],
[grammar(u,'一10','all + 都 · 一起 / 一块儿 + action','Coordinate the whole group',
'都 refers to every member of a stated group and normally precedes the verb: 我们都去. 一起 and colloquial 一块儿 say people act together; they do not by themselves say that every possible person comes. Compare 我们都回家 with 我们一起回家: everyone goes home versus going home together.',[
('我们都想走，有些朋友想跑。','We all want to walk; some friends want to run.'),('我们一起走，也一块儿聊天。','We walk together and chat together.')],
('我们走都。','我们都走。','Place 都 before the verb it modifies.')),
grammar(u,'一39','clause, clause · 一边…一边… · …也…','Connect compatible actions',
'Related clauses can be placed together without a connector: 我开门，你出来. 一边…一边… coordinates simultaneous activities by the same actor, such as walking and chatting. It does not mean “first…then”. 也 adds a parallel action or fact: 我想走，也想聊天. Choose activities that can actually happen together and keep street safety in mind.',[
('我开门，你出来。','I will open the door; you come out.'),('我们一边走，一边聊天。','We walk and chat at the same time.'),('我想散步，也想听你说话。','I want to take a walk and also hear you speak.')],
('我一边睡觉，一边上课。','我先上课，再睡觉。','Attending class and sleeping are not the intended simultaneous actions; use 先…再… for the sequence.'))],
text(u,'d','Walk after the call','Find the safe shared activity and the time to return.',[
('我们一块儿出门吧。有些朋友也想去。','Let us go out together. Some friends want to come too.'),('行，我先打电话，再出来。你等一下儿。','Okay. I will call first, then come out. Wait a moment.'),
('好，我在楼下。我开门，你出来。','Okay, I am downstairs. I will open the door; you come out.'),('我听到你说话了。你在门口吗？','I heard you speaking. Are you at the doorway?'),
('在。我们都想走，不跑。','Yes. We all want to walk, without running.'),('我也想散步，一边走，一边聊天。','I also want a walk; we can walk and chat.'),
('你听见旁边有人唱歌吗？','Do you hear someone singing nearby?'),('听见了，但没有听懂。我想再听一次。','Yes, but I did not understand it. I would like to listen again.'),
('先过马路，过了再听。别一边走一边看手机。','Cross the road first, then listen. Do not look at your phone while walking.'),('好。七点我回到家，先回去做晚饭。','Okay. I will be home at seven and go back to make dinner first.'),
('你什么时候回来？','When are you coming back?'),('八点再来。你们先走，我也想和大家一起走。','I will come again at eight. You go on first; I also want to walk with everyone.')],
[('mainidea','What activity do they choose together?',['Walking and chatting','Running in traffic','Sleeping in class'],0),('detail','When does one friend return home?',['At seven','At eight','At noon'],0),('inference','Does hearing the song prove understanding?',['No, the friend explicitly did not understand it','Yes, 听见 always means understand','No song was heard'],0)],drama=True),
text(u,'r','Walk plan in the group chat','Find which actions are simultaneous and which happen in order.',[
('今天有些朋友想出门，我们一块儿走一会儿。','Some friends want to go out today; we will walk together for a while.'),
('我先打电话，再出来，请大家等一下儿。','I will call first, then come out; please wait a moment.'),
('朋友开门，我从家里出来，在楼下见面。','A friend opens the door; I come out of my home and we meet downstairs.'),
('我们都想散步，一边走，一边聊天，不跑。','We all want a walk; we will walk and chat, without running.'),
('我听到朋友说话，也听见旁边有人唱歌。','I hear my friend speaking and also hear someone singing nearby.'),
('听见不一定听懂，我们过马路以后再听。','Hearing does not necessarily mean understanding; we will listen again after crossing the road.'),
('七点我回到家，先回去做晚饭。','I will be home at seven and go back to make dinner first.'),
('八点我回来，和朋友一起走，也一起说汉语。','I will come back at eight to walk with friends and speak Chinese together.')],
[('mainidea','What does the plan distinguish?',['Concurrent activities and ordered steps','Different school subjects','Two ticket prices'],0),('detail','What must happen before leaving?',['A phone call','An exam','Singing the whole song'],0),('inference','Why postpone listening when crossing?',['To give attention to crossing safely','Because the song is forbidden','Because no one has ears'],0)],[(1,'打'),(3,'一边')]),
text(u,'media','A sound is not its meaning','Follow a brief original street-side conversation.',[
('我听见有人唱歌，你听到了吗？','I hear someone singing. Did you hear it?'),('听到了，没听懂。先走，不跑。','I heard it but did not understand. Walk first; do not run.'),
('我们一边走，一边聊天，行吗？','Can we walk and chat?'),('行，但过马路的时候先不聊天。','Yes, but pause the chat when crossing the road.'),
('七点回到家，八点再出来，一块儿走。','Home at seven, out again at eight to walk together.'),('好，我先回去，你也回吧。等一下儿再说。','Okay, I will go back first; you go back too. We will talk again in a moment.')],
[('inference','What do they pause while crossing?',['The conversation','Going home forever','Every future walk'],0)],drama=True),
dict(tf=[('一边','我们一边走，一边聊天。','We walk and chat at the same time.','Chatting happens only after walking finishes.',False,'一边…一边… marks simultaneity.'),('回到','我七点回到家。','I arrive back home at seven.','The speaker returns home at seven.',True,'回到家 gives the return destination.')],
reply=[('一下儿','你等一下儿，行吗？','Could you wait a moment?',['行，我在楼下等。','三杯水。','这是北京。'],0,'Agree to wait.'),('听见','你听见唱歌了吗？','Did you hear the singing?',['听见了，但没听懂。','明天八点。','我的钱包。'],0,'Distinguish hearing from understanding.')],
fill=[('回去','太晚了，我先回去。','It is too late; I will go back first.'),('出来','你先出来，我在楼下。','Come out first; I am downstairs.')],
match=[('跑',[('别跑，先走。','Do not run; walk first.'),('我开门，你出来。','I open the door; you come out.'),('我先回家。','I will go home first.')]),('一块儿',[('我们一块儿去散步。','We will go for a walk together.'),('有些朋友想坐车。','Some friends want to take a vehicle.'),('你什么时候回来？','When are you coming back?')])]),
[('Leaving the group briefly','我先回去，八点再来。','I will go back first and come again at eight.','A return time lets friends continue without waiting indefinitely.'),('Keeping a walk safe','过马路的时候先不聊天。','Pause the chat when crossing the road.','The simultaneous-action pattern is not advice to divide attention in traffic.')],
[('一起散步，行吗？','Shall we walk together?','Agree',['行，我们一块儿走吧。']),('你什么时候回来？','When are you coming back?','Say eight',['八点回来。','我八点回来。'])],
'Native check: 来/去 viewpoint in the group scene, short 出/回 versus compounds, the rhotic 一下儿, and natural phrasing of sound versus understanding.')

u='s1-u28'
write(28,'还去不去',['Confirm a travel or study plan rather than assume it','Choose between 吗, a question word, 还是 and A-not-A','Use 吧/呢/了 without adding a universal question particle'],[
('吧','suggestion or tentative particle','trợ từ gợi ý; phỏng đoán','particle','我们明天再看吧。','Let us look again tomorrow.'),
('呢','what-about or ongoing-action particle','trợ từ hỏi tiếp; hành động đang diễn ra','particle','我在家，你呢？','I am at home; what about you?'),
('过','to pass; spend a holiday','qua; đón dịp lễ','verb','我们一起过新年。','We celebrate the new year together.'),
('就','just; right away; then','ngay; thì','adverb','我现在就去。','I will go right now.'),
('年','year','năm','measure word','这是我来北京的第二年。','This is my second year in Beijing.'),
('新年','new year','năm mới','noun','新年你回家吗？','Are you going home for the new year?'),
('上次','last time','lần trước','noun','上次我忘记买票了。','Last time I forgot to buy a ticket.'),
('机票','plane ticket','vé máy bay','noun','我的机票在手机里。','My plane ticket is on my phone.'),
('飞','to fly','bay','verb','明天上午飞北京。','Fly to Beijing tomorrow morning.'),
('网上','online; on the internet','trên mạng','noun','我在网上买机票。','I buy plane tickets online.'),
('网友','online friend; internet user','bạn quen trên mạng; người dùng mạng','noun','这个网友也学习汉语。','This online friend also studies Chinese.'),
('考','to take a test; examine','thi; kiểm tra','verb','我明天考汉语。','I have a Chinese test tomorrow.'),
('考试','examination; take an exam','kỳ thi; thi','noun','考试是星期五。','The exam is on Friday.'),
('知道','to know','biết','verb','你知道几点考试吗？','Do you know what time the exam is?'),
('名字','name','tên','noun','请问，您的名字怎么写？','May I ask how your name is written?'),
('请问','excuse me; may I ask','xin hỏi','verb','请问，明天几点开门？','Excuse me, what time do you open tomorrow?'),
('小姐','Miss; young woman in specific contexts','cô; cách gọi Miss trong ngữ cảnh phù hợp','noun','通知上写的是张小姐。','The notice is addressed to Miss Zhang.')],
[grammar(u,'一22','吧 / 了 / 吗 / 呢','Hear what a sentence-ending particle does',
'吧 can suggest a plan or make a tentative assumption. Sentence-final 了 marks a changed situation: 我知道了. 吗 makes a neutral yes/no question from a statement. 呢 can ask “what about…?” or close an ongoing-action statement. They are not interchangeable endings. A word question such as 几点考试 already asks for missing information and does not add 吗.',[
('明天再看吧。','Let us look again tomorrow.'),('我知道了。','I know now; understood.'),('你明天回家吗？','Are you going home tomorrow?'),('我在家，你呢？','I am at home; what about you?'),('我读书呢。','I am reading.')],
('你几点考试吗？','你几点考试？','Do not add 吗 to the question word 几点 in this direct question.')),
grammar(u,'一33','吗? · question word? · A 还是 B? · A-not-A?','Choose the information you need',
'A yes/no question checks a proposition: 明天考试吗？ A question-word question asks a missing detail: 几点考试？ A choice question offers alternatives: 上午还是下午？ An A-not-A question checks a choice of positive/negative: 考不考？ These are different ways to ask, not four endings to combine. A choice needs an actual offered answer; do not answer a time question only with 是.',[
('明天考试吗？','Is the exam tomorrow?'),('几点考试？','What time is the exam?'),('上午还是下午考试？','Is the exam in the morning or afternoon?'),('明天考不考？','Is there a test tomorrow or not?')],
('上午还是下午考试吗？','上午还是下午考试？','Do not combine the direct 还是 alternatives with 吗 here.')),
grammar(u,'一45','statement + 吗?','Check a proposition politely',
'Add 吗 to an ordinary statement to ask whether it is true: 你买票了 → 你买票了吗？ Answer the specific predicate or give a short fact. This is a neutral question; 不 forms a negative proposition, so 你不回家吗？ may sound surprised in context. Do not mechanically add 吗 to question-word, choice or A-not-A questions.',[
('你买机票了吗？','Have you bought a plane ticket?'),('你在网上买的吗？','Did you buy it online?')],
('你买不买机票吗？','你买机票吗？','Use one direct yes/no question structure, not two combined.'))],
text(u,'d','One plan, four useful questions','Find what changes and what still needs checking.',[
('新年我们还一起过吗？你回家吗？','Are we still celebrating the new year together? Are you going home?'),('回家。今年是我来北京的第二年，上次没回去。','I am going home. This is my second year in Beijing; I did not go back last time.'),
('你买机票了吗？在网上买的吗？','Have you bought a plane ticket? Did you buy it online?'),('买了，在网上买的。明天上午飞。','Yes, I bought it online. I fly tomorrow morning.'),
('上午还是下午？我记得你有考试。','Morning or afternoon? I remember that you have an exam.'),('对，我明天考汉语，考试是下午。机票要改。','Right, I have a Chinese test tomorrow afternoon. I need to change the plane ticket.'),
('你知道几点考试吗？','Do you know what time the exam is?'),('不知道。我现在就看通知。你呢？','No. I will check the notice right now. What about you?'),
('我在家读书呢。通知的名字是张小姐吗？','I am reading at home. Is the name on the notice Miss Zhang?'),('对，是我。网友发给我的通知，先问学校吧。','Yes, that is me. An online friend sent me the notice; I should ask the school first.'),
('请问，明天几点考试？先这样问。','“Excuse me, what time is the exam tomorrow?” Ask that first.'),('好，我知道了。先确认考试，再改机票。','Okay, understood. Confirm the exam first, then change the plane ticket.')],
[('mainidea','What conflict needs resolving?',['A flight and an exam on the same day','Two restaurants','Two people with one bag'],0),('detail','When is the stated exam?',['Tomorrow afternoon','Tomorrow morning','Last year'],0),('inference','Why contact the school?',['The notice came through an online friend','The ticket proves the exam time','The speaker has no name'],0)],drama=True),
text(u,'r','Confirm before changing','Find what is known and what should be verified directly.',[
('新年我想回家，和家里人一起过。','I would like to go home for the new year and celebrate with my family.'),
('今年是我来北京的第二年，上次没有回去。','This is my second year in Beijing; I did not go back last time.'),
('我在网上买了明天上午的机票，想上午飞。','I bought an online ticket for tomorrow morning and plan to fly in the morning.'),
('朋友问我明天考不考汉语，我才想起考试。','A friend asked whether I have a Chinese test tomorrow; only then did I remember the exam.'),
('网友发的通知写下午考试，名字是张小姐。','The notice sent by an online friend says the exam is in the afternoon and is addressed to Miss Zhang.'),
('我还不知道几点，也不知道这个通知对不对。','I do not yet know the time or whether the notice is correct.'),
('我现在就问学校：请问，明天几点考试？','I will ask the school right now: “Excuse me, what time is tomorrow’s exam?”'),
('先确认考试，再改机票。朋友在家读书呢，我们明天再说吧。','Confirm the exam first, then change the ticket. My friend is reading at home; we will talk again tomorrow.')],
[('mainidea','What should happen first?',['Verify the exam with the school','Assume the notice is correct','Miss every flight'],0),('detail','Who sent the notice?',['An online friend','The airline directly','A doctor'],0),('inference','Can the exact exam time be stated confidently?',['No, it has not been verified','Yes, eight in the morning','Yes, midnight'],0)],[(2,'机票'),(6,'请问')]),
text(u,'media','Ask the actual question','Read an original verse with four question shapes.',[
('新年回家吗？回家。去年没回，今年过新年。','Going home for the new year? Yes. Not last year; celebrate this year.'),
('机票买了吗？买了。网上买，明天飞。','Ticket bought? Yes. Bought online; fly tomorrow.'),
('上午还是下午？考试几点？先看通知，再问学校。','Morning or afternoon? What time is the exam? Read the notice, then ask the school.'),
('明天考不考？还不知道，先问学校。','An exam tomorrow or not? Still unknown; ask the school first.'),
('名字张小姐，网友发通知。别猜，确认吧。','Name: Miss Zhang; notice from an online friend. Do not guess; confirm it.'),
('我在家，你呢？读书呢。知道了，明天再说。','I am at home; you? Reading. Understood; talk tomorrow.')],
[('inference','What attitude does the verse recommend?',['Check uncertain information','Treat every forwarded notice as official','Change a ticket without checking'],0)]),
dict(tf=[('机票','我在网上买机票。','I buy plane tickets online.','The ticket is bought online.',True,'网上 gives the purchasing channel.'),('考试','我还不知道几点考试。','I do not yet know what time the exam is.','The exact exam time is known.',False,'还不知道 explicitly says it is unknown.')],
reply=[('吧','先问学校吧。','Let us ask the school first.',['好，我现在就问。','两张床。','白色的包。'],0,'Accept the practical suggestion.'),('呢','我在家，你呢？','I am at home; what about you?',['我在车站。','我不知道谁的。','六块钱。'],0,'Provide your own location.')],
fill=[('请问','请问，明天几点考试？','Excuse me, what time is tomorrow’s exam?'),('知道','我知道了，先确认时间。','Understood; first confirm the time.')],
match=[('过',[('我们一起过新年。','We celebrate the new year together.'),('明天上午飞北京。','Fly to Beijing tomorrow morning.'),('上次我没回去。','I did not go back last time.')]),('名字',[('通知上写的是张小姐。','The notice is addressed to Miss Zhang.'),('您的名字怎么写？','How is your name written?'),('这个网友学习汉语。','This online friend studies Chinese.')])]),
[('Formal name reference','通知上写的是张小姐。','The notice is addressed to Miss Zhang.','小姐 after a surname can occur in formal written references; for a stranger, 请问 avoids assuming an appropriate personal title. It is not a default restaurant-server address.'),('Checking rather than guessing','请问，明天几点考试？','Excuse me, what time is tomorrow’s exam?','Ask the institution for the missing detail; a forwarded notice is not independent verification.')],
[('你买机票了吗？','Have you bought a plane ticket?','Say you bought it online',['买了，在网上买的。']),('你知道几点考试吗？','Do you know what time the exam is?','Say unknown and propose checking',['不知道，先问学校吧。'])],
'Native check: formal 小姐 after a surname, travel/exam timing, question-particle combinations, and the clipped original verse. No exam result or travel booking is claimed.')

from retrievals import apply
apply(25,28)
