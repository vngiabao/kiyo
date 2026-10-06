"""Authored entrance directions and first-month recap; final two L1 units."""
from common import *
character_groups.update({
29:[('北','north'),('东','east'),('南','south'),('西','west'),('后','behind; after'),('左','left'),('右','right'),('旁','beside'),('字','written character')],
30:[('还','still; also'),('进','to enter'),('渴','thirsty'),('块','piece; yuan classifier'),('树','tree'),('坏','bad; broken'),('着','continuing-state particle'),('条','strip; classifier for long things'),('最','most')],
})
character_contexts.update({'桌':('桌子','table')})
unit_glosses.update({29:{'入口':'entrance','出口':'exit','门':'door; gate','门口':'at the door; entrance','面向':'to face toward','箭头':'arrow','地图':'map','停车场':'car park','指':'to point; indicate','北门':'north gate','南门':'south gate','位置':'position'},
30:{'邻居':'neighbour','照顾':'to look after','搬':'to move','院子':'courtyard','热情':'warm; welcoming','一直':'all along; continuously','故事':'story','医生':'doctor','桌子':'table','收':'to collect; clear away','借':'to lend; borrow','朋友们':'friends, as a group','口渴':'thirsty'}})
u='s1-u29'
write(29,'我们在入口等你',['Read entrance signs and relative directions','Distinguish map directions from your own left and right','Use short answers only when their referent is clear'],[
('北','north','phía bắc','noun','地图的上边是北。','The top of the map is north.'),
('北边','on the north side','phía bắc','noun','车站在学校北边。','The station is north of the school.'),
('东','east','phía đông','noun','面向北，右边是东。','When facing north, east is on the right.'),
('东边','on the east side','phía đông','noun','入口在楼的东边。','The entrance is on the east side of the building.'),
('南','south','phía nam','noun','地图的下边是南。','The bottom of the map is south.'),
('南边','on the south side','phía nam','noun','商店在学校南边。','The shop is south of the school.'),
('西','west','phía tây','noun','面向北，左边是西。','When facing north, west is on the left.'),
('西边','on the west side','phía tây','noun','书店在学校西边。','The bookshop is west of the school.'),
('后','behind; after','sau; phía sau','noun','先看前，再看后。','Look in front first, then behind.'),
('后边','behind; at the back','phía sau','noun','停车场在楼后边。','The car park is behind the building.'),
('前','in front; before','trước; phía trước','noun','我们在门前等你。','We are waiting in front of the gate.'),
('前边','in front; at the front','phía trước','noun','前边有一个入口。','There is an entrance ahead.'),
('左','left','bên trái','noun','这个箭头指左。','This arrow points left.'),
('右','right','bên phải','noun','那个箭头指右。','That arrow points right.'),
('上边','above; upper side','phía trên','noun','地图上边有一个北字。','There is a north character at the top of the map.'),
('下边','below; lower side','phía dưới','noun','地图下边有一个南字。','There is a south character at the bottom of the map.'),
('中间','in the middle','ở giữa','noun','我在两个入口中间。','I am between the two entrances.')],
[grammar(u,'一01','above / below · inside / outside · front / back · left / right · east / south / west / north','Locate an object using a clear reference',
'The twelve direction words are 上、下、里、外、前、后、左、右、东、南、西、北. Their side forms are 上边、下边、里边、外边、前边、后边、左边、右边、东边、南边、西边、北边. Say what they are relative to: 楼的东边, 门外. Left/right depend on the person’s orientation; east/west do not. This unit’s map explicitly puts north at the top; do not assume every map does.',[
('门里、门外，楼上、楼下。','Inside and outside the gate; upstairs and downstairs.'),('楼前、楼后，门左边、门右边。','In front of and behind the building; to the left and right of the gate.'),('上边、下边、里边、外边、前边、后边。','Above, below, inside, outside, in front, behind.'),('左边、右边、东边、南边、西边、北边。','Left, right, east, south, west, north.'),('面向北，右边是东，左边是西。','Facing north, east is on the right and west on the left.')],
('右边就是东边。','面向北，右边是东边。','Right is east only in this stated orientation.')),
grammar(u,'一31','short answer · exclamation · sign','Understand an utterance without an expressed subject and predicate',
'A context can support a short non-subject-predicate utterance: 在北门外 answers 在哪儿？; 两个人 answers 几个人？; 好！ accepts a suggestion. Signs can simply say 入口 or 出口. These are complete communicative utterances in context, not a reason to omit necessary information in every sentence. Use a full statement if the reference could be ambiguous.',[
('在哪儿？在北门外。','Where? Outside the north gate.'),('几个人？两个人。','How many people? Two.'),('入口。出口。好！','Entrance. Exit. Okay!')],
('在哪儿？两个。','在哪儿？在北门外。','A location question needs a place, not a number.'))],
text(u,'d','Which entrance?','Find the meeting gate and the orientation used for directions.',[
('我到学校南边了，你们在哪儿？','I have reached the south side of the school. Where are you?'),('在北门外。北边有车站，南边有商店。','Outside the north gate. There is a station to the north and a shop to the south.'),
('我看地图，上边是北，下边是南，对吗？','On the map, the top is north and the bottom is south, right?'),('对，这张地图上边有一个北字。东在右，西在左。','Yes, this map has a north character at the top. East is right, west is left.'),
('楼的东边有两个入口，我走哪个？','There are two entrances on the east side of the building. Which do I take?'),('先到北门。我们不在东边的入口，也不在西边的书店。','Come to the north gate first. We are not at the eastern entrance or the western bookshop.'),
('我现在面向北，左边是西，右边是东。','I am facing north now: west is on the left, east on the right.'),('对。前边是北，后边是南。你先看前，再看后。','Correct. Ahead is north, behind is south. Look ahead first, then behind.'),
('北门前边有两个人，是你们吗？','There are two people in front of the north gate. Is that you?'),('是，我们在门前等你。停车场在楼后边。','Yes, we are waiting in front of the gate. The car park is behind the building.'),
('我在两个入口中间，现在看到你们了。','I am between the two entrances. I can see you now.'),('好！看箭头，入口指左，出口指右。我们从入口进去。','Good! Look at the arrows: entrance points left, exit points right. We will go in through the entrance.')],
[('mainidea','Where will the group meet?',['Outside the north gate','Inside the west bookshop','At the south shop'],0),('detail','Which orientation makes right equal east?',['Facing north','Facing south','Any orientation'],0),('inference','Does the friend need the east-side entrance to meet the group?',['No, the group says to reach the north gate first','Yes, the group waits at that entrance','They do not name a meeting gate'],0)],drama=True),
text(u,'r','Directions in a message','Find the meeting location before following the entry sign.',[
('今天我们在学校北门外等朋友。','Today we are waiting for a friend outside the school’s north gate.'),('学校北边是车站，南边有商店，西边有书店。','There is a station north of the school, a shop to the south and a bookshop to the west.'),
('楼的东边有两个入口，但我们在北门前。','There are two entrances on the east side of the building, but we are in front of the north gate.'),('这张地图上边是北，下边是南；右是东，左是西。','On this map, north is at the top and south at the bottom; east is right, west is left.'),
('面向北的时候，前边是北，后边是南。','When facing north, north is ahead and south is behind.'),('停车场在楼后边，门前有两个人。','The car park is behind the building; there are two people in front of the gate.'),
('朋友先在两个入口中间，后来看到我们。','Our friend was between the two entrances first, then saw us.'),('我们一起看箭头：入口在左，出口在右。','We look at the arrows together: entrance on the left, exit on the right.')],
[('mainidea','What is the message for?',['Finding the meeting point and entrance','Buying clothes','Announcing an exam'],0),('detail','What is north of the school?',['A station','A bookshop','A car park'],0),('inference','Why does the message specify 面向北?',['To make front/back and left/right unambiguous','To change the map’s north','To say every map faces north'],0)],[(0,'北门'),(5,'后边')]),
text(u,'media','Read the arrow','Follow an original scene about a confused entrance.',[
('地图上边是北，下边是南。我们在北门外。','The map’s top is north and bottom is south. We are outside the north gate.'),('我在南边的商店。东边的两个入口中间有人吗？','I am at the southern shop. Is anyone between the two eastern entrances?'),
('有，可是我们在门前，不在那边。西边是书店。','Yes, but we are in front of the gate, not over there. The west side has the bookshop.'),('我面向北，左是西，右是东，前是北，后是南。','I am facing north: left is west, right east, ahead north, behind south.'),
('对。楼后边是停车场。来北门前边吧。','Right. The car park is behind the building. Come to the front of the north gate.'),('看到了！入口指左，出口指右。好！','I see you! Entrance points left, exit right. Okay!')],
[('detail','Which gate does the friend need?',['The north gate','The south shop','The west bookshop'],0)],drama=True),
dict(tf=[('北边','车站在学校北边。','The station is north of the school.','The station is south of the school.',False,'北边 is north, not south.'),('右','面向北，右边是东。','Facing north, east is on the right.','East is to the right when facing north.',True,'The direction is explicitly relative to facing north.')],
reply=[('中间','你现在在哪儿？','Where are you now?',['在两个入口中间。','两个朋友。','明年再来。'],0,'Give a location.'),('前边','门前边是你们吗？','Is that you in front of the gate?',['是，我们在门前。','半杯奶。','昨天没上课。'],0,'Confirm the people and place.')],
fill=[('南边','商店在学校南边。','The shop is south of the school.'),('后边','停车场在楼后边。','The car park is behind the building.')],
match=[('上边',[('地图上边是北。','North is at the top of the map.'),('地图下边是南。','South is at the bottom of the map.'),('西边有书店。','There is a bookshop to the west.')]),('左',[('这个箭头指左。','This arrow points left.'),('那个箭头指右。','That arrow points right.'),('我们在门前。','We are in front of the gate.')])]),
[('Clarifying relative directions','你面向哪边？','Which way are you facing?','Ask orientation before interpreting left and right.'),('Short but useful reply','在北门外。','Outside the north gate.','A short reply is useful when it answers the actual location question.')],
[('你现在在哪儿？','Where are you now?','Say outside the north gate',['在北门外。']),('面向北，右边是哪边？','Facing north, which direction is on the right?','Say east',['右边是东。'])],
'Native check: 北门 and east-side entrance geometry, localizer shortening on signs, and relative versus cardinal directions. No claim that every map is north-up.')

u='s1-u30'
vocabulary_readings[u+':还']='huán'
dictionary.update({'还你':'huán nǐ','还给':'huán gěi'})
write(30,'在这里的第一个月',['Write a concrete first-month recap','Invite a neighbour in and make a simple request','Distinguish descriptions from questions and requests'],[
('还','to return; give back','trả lại','verb','我明天还你的课本。','I will return your textbook tomorrow.'),
('们','neutral group suffix in 朋友们','hậu tố chỉ nhóm trong 朋友们','suffix','朋友们来我家。','My friends come to my home.'),
('面条儿','noodles, with a northern rhotic ending','mì sợi, cách nói có âm r ở miền bắc','noun','今天我们吃面条儿。','Today we are having noodles.'),
('进来','to come in','đi vào phía người nói','verb','朋友从门外进来。','My friend comes in from outside the door.'),
('进去','to go in','đi vào xa người nói','verb','他们从门外进去。','They go in from outside the door.'),
('请进','please come in','mời vào','verb','门开了，请进。','The door is open; please come in.'),
('请坐','please sit down','mời ngồi','verb','你口渴了？请坐，喝水吧。','Are you thirsty? Please sit down and have water.'),
('坐下','to sit down','ngồi xuống','verb','我坐下写今天的日记。','I sit down to write today’s diary.'),
('外','outside','bên ngoài','noun','门外有一棵树。','There is a tree outside the door.'),
('工人','worker','công nhân','noun','我的邻居是工人。','My neighbour is a worker.'),
('树','tree','cây','noun','这棵树下有两个孩子。','There are two children under this tree.'),
('着','neutral continuing-state particle','trợ từ chỉ trạng thái đang tiếp diễn','particle','门开着，请进。','The door is open; please come in.'),
('小孩儿','young child, with a northern rhotic ending','trẻ nhỏ, cách nói có âm r ở miền bắc','noun','那个小孩儿在树下玩。','That young child is playing under the tree.'),
('点','a little; classifier for a small amount','một ít; lượng nhỏ','measure word','请喝点水。','Please have a little water.'),
('子','neutral noun suffix in 桌子','hậu tố danh từ trong 桌子','suffix','桌子上有两个杯子。','There are two cups on the table.'),
('最后','last; finally','cuối cùng','noun','我们最后一起洗杯子。','We wash the cups together at the end.'),
('坏','bad; broken','xấu; hỏng','adjective','这个杯子坏了，别用。','This cup is broken; do not use it.')],
[grammar(u,'一25','subject + verb phrase / adjective phrase','Say what someone does or what something is like',
'A predicate can be a verb or verb phrase: 朋友们进来; 我学习汉语. It can also be an adjective phrase: 邻居很热情; 杯子坏了. Match the subject to the action or property. 是 is not required before an ordinary adjective predicate. A word’s category is not a command to use it in every possible predicate position.',[
('朋友们进来，我们一起吃面条儿。','Our friends come in; we have noodles together.'),('邻居很热情，杯子坏了。','The neighbours are welcoming; the cup is broken.')],
('邻居是很热情。','邻居很热情。','A neutral adjective description does not need 是.')),
grammar(u,'一32','positive statement · negative statement','Report a fact without turning it into a question',
'A statement gives information: 我住在这里; 我不是工人. It normally ends with a full stop, not a question particle 吗. Use 不 for present negation of 是 or a general habit, and 没 for an action that did not happen. A statement can include 了 or an appropriate adverb. Do not infer that someone completed a course merely because they say 我学习汉语.',[
('我住在这里，我还在学习汉语。','I live here; I am still learning Mandarin.'),('我不是工人，昨天没去学校。','I am not a worker; I did not go to school yesterday.')],
('我住在这里吗。','我住在这里。','Remove 吗 when stating where you live.')),
grammar(u,'一36','identity / category · defining characteristic · presence at a place','Use 是 with the intended relation',
'Identity/category: 我的邻居是工人. A characteristic can use a noun phrase: 她是一个热情的人; this differs from the direct adjective predicate 她很热情. A place + 是 + noun phrase describes what occupies it: 门外是一棵树; 前边是学校. Compare 门外有一棵树, which introduces something present. These location descriptions require a clear scene, not a blanket substitution of 是 for every 有.',[
('我的邻居是工人。','My neighbour is a worker.'),('她是一个热情的人。','She is a welcoming person.'),('门外是一棵树，前边是学校。','Outside the door is a tree; ahead is the school.')],
('我的邻居有工人。','我的邻居是工人。','Use 是 to identify the neighbour’s category, not 有.'))],
text(u,'d','A neighbour visits','Find who visits, what the host offers, and what must not be used.',[
('你在这里住一个月了，还在学习汉语吗？','You have lived here for a month. Are you still studying Mandarin?'),('还在学习。朋友们常常来，我们一起读书。','I still am. My friends often visit; we read together.'),
('门开着，我可以进来吗？','The door is open. May I come in?'),('请进，请坐！先喝点水。','Please come in and sit down! Have a little water first.'),
('门外的小孩儿是谁？他在树下玩。','Who is the young child outside? He is playing under the tree.'),('是邻居的儿子。那个小孩儿常和小朋友一起玩。','He is my neighbour’s son. That young child often plays with other children.'),
('你的邻居是工人吗？','Is your neighbour a worker?'),('是，她很热情，也常照顾孩子。我们今天吃面条儿。','Yes, she is welcoming and often looks after the children. We are having noodles today.'),
('桌子上的两个杯子可以用吗？','Can we use the two cups on the table?'),('这个坏了，别用。那个是好的，你坐下喝水吧。','This one is broken; do not use it. That one is fine. Sit down and have water.'),
('大家从门外进去吃饭，最后洗杯子，对吗？','Everyone goes inside to eat, then washes the cups at the end, right?'),('对。这本书是你的，我明天还给你。','Right. This book is yours; I will return it tomorrow.')],
[('mainidea','What is happening?',['A neighbour is being welcomed into the home','A formal exam is starting','The host is moving away'],0),('detail','Which cup must not be used?',['The broken one','Both cups','The good one'],0),('inference','Does 还在学习 mean the host claims Mandarin mastery?',['No, study is continuing','Yes, all learning is finished','The host has stopped studying'],0)],drama=True),
text(u,'r','My first month here','Read for the new routine and one practical problem, not a proficiency claim.',[
('我在这里住一个月了，还在学习汉语。','I have lived here for a month and am still learning Mandarin.'),('朋友们常来，我请他们进来，请坐，喝点水。','My friends often visit. I invite them in, ask them to sit and offer a little water.'),
('门外是一棵树，前边是学校。我的邻居是工人。','Outside the door is a tree and ahead is the school. My neighbour is a worker.'),('她很热情，她的儿子是个小孩儿，常在树下玩。','She is welcoming. Her son is a young child who often plays under the tree.'),
('今天门开着，大家从门外进去吃面条儿。','Today the door is open; everyone goes inside to have noodles.'),('我坐下读日记，朋友们坐在桌子旁边。','I sit down to read my diary; my friends sit beside the table.'),
('桌子上有两个杯子，一个坏了，另一个可以用。','There are two cups on the table; one is broken and the other can be used.'),('最后我们一起收桌子。朋友借我一本书，我明天还给她。我还想学新的词。','At the end we clear the table together. A friend lent me a book; I will return it tomorrow. I still want to learn new words.')],
[('mainidea','What does the recap describe?',['A new local routine and continuing study','A guarantee of exam success','A journey to the airport'],0),('detail','What is wrong with one cup?',['It is broken','It is too heavy','It is not on the table'],0),('inference','What suggests learning continues?',['The writer wants new words and diary entries','The neighbours are workers','There is a tree outside'],0)],[(1,'朋友们'),(7,'最后')]),
text(u,'media','A small place to begin','Read an original verse about study and company.',[
('门外有树，树下有小孩儿。','A tree outside, a young child under it.'),('门开着，朋友们进来，请进，请坐。','The door is open; friends come in. Come in, sit down.'),
('工人邻居请大家进去，一起吃面条儿。','Our worker neighbour invites everyone in to have noodles together.'),('口渴了，坐下喝点水。桌子旁有朋友们。','Thirsty? Sit down, have a little water. Friends beside the table.'),
('杯子坏了，别用。换一个，再喝水。','A broken cup: do not use it. Take another, then have water.'),('最后收桌子，还读书。一个月，不是最后。','Clear the table at the end, keep reading. One month is not the end.')],
[('inference','What does the last line suggest?',['The first month is a beginning','Study is finished forever','The home is closing'],0)]),
dict(tf=[('坏','这个杯子坏了，别用。','This cup is broken; do not use it.','The speaker says to use this cup.',False,'别用 explicitly says not to use it.'),('还','我还在学习汉语。','I am still learning Mandarin.','The learning is continuing.',True,'还在学习 describes continuing study.')],
reply=[('请进','我可以进来吗？','May I come in?',['请进，请坐。','那个杯子坏了。','昨天星期日。'],0,'Welcome the visitor in.'),('点','口渴了，可以喝水吗？','I am thirsty; may I have water?',['可以，喝点水吧。','他是工人。','门外是一棵树。'],0,'Offer some water.')],
fill=[('最后','我们最后一起收桌子。','We clear the table together at the end.'),('工人','我的邻居是工人。','My neighbour is a worker.')],
match=[('们',[('朋友们常常来。','My friends often visit.'),('我们还在读书。','We are still reading.'),('门外有一棵树。','There is a tree outside the door.')]),('子',[('桌子上有两个杯子。','There are two cups on the table.'),('我坐下喝水。','I sit down to drink water.'),('他们从门外进去。','They go in from outside the door.')])]),
[('Inviting a visitor','请进，请坐。','Please come in and sit down.','A brief welcome is enough; offer a seat and water without pressuring the visitor.'),('An honest recap','我还在学习汉语。','I am still learning Mandarin.','Describe actual ongoing study rather than making a proficiency claim.')],
[('可以进来吗？','May I come in?','Welcome your visitor',['请进，请坐。']),('这个杯子可以用吗？','Can this cup be used?','Say it is broken and offer the other',['这个坏了，用那个吧。'])],
'Native check: 小孩儿 and 面条儿 rhotic pronunciation; short poetic omissions and the last line’s metaphor. 们/子 are explicit neutral suffix entries, never standalone spoken zǐ. 着 is recognized as a continuing state here; its full grammar owner is s2-u28.')

from retrievals import apply
apply(29,30)
