"""Reconstruct a misplaced bag through overlapping accounts without invented chronology."""
import sys
from advanced_core import write,rows,words,q,card,practice
V=words('''
当成|take for; treat as|coi như|他把个人的袋子当成交换活动的物品了。|He took a personal bag for an exchange-event item.|别把暂时没回复当成最后拒绝。|Don’t treat a temporary lack of reply as a final refusal.
当天|on that day|ngày hôm đó|当天我先还袋子，后来陈宇才放进稿子。|That day I returned the bag before Chen Yu put pages into it.|当天的安排临时改了。|The plan changed at short notice that day.
仓库|storeroom; warehouse|kho|袋子在二楼仓库，不在活动桌上。|The bag is in the upstairs storeroom, not on the event table.|她去仓库找多余的椅子。|She went to the storeroom for extra chairs.
地下室|basement|tầng hầm|有人说找地下室，可我们没有把东西搬到那里。|Someone suggested the basement, but we hadn’t moved items there.|地下室里放着旧桌子。|Old tables are kept in the basement.
楼道|building corridor|hành lang|我在楼道里看到一张掉出来的纸。|I saw a loose sheet in the corridor.|请别在楼道里放太多东西。|Please don’t leave too much in the corridor.
楼房|multi-storey building|tòa nhà|这座楼房有两层，活动在一楼。|This two-storey building hosts the event downstairs.|新楼房旁边有一条小路。|There is a small path beside the new building.
物品|items; belongings|đồ vật|个人物品和可交换的书要分开放。|Keep personal belongings separate from exchangeable books.|他把物品列成一张表。|He made a list of the items.
领取|collect something assigned or available|nhận|领书在大厅，不能到私人物品里随便领取。|Collect books in the hall, not from private belongings.|她去门口领取资料。|She went to collect materials at the door.
拿走|take away|mang đi|袋子被拿走了，不说明一定离开了楼房。|The bag was taken away, not necessarily out of the building.|请别把那张还没改完的纸拿走。|Please don’t take away the unfinished page.
储存|store for later use|lưu trữ|二楼储存的是活动用的桌椅。|The upper floor stores tables and chairs for events.|他把资料储存在自己的电脑里。|He stores the materials on his own computer.
看管|look after; supervise|trông coi|看管个人袋子不是志愿者已经答应的工作。|Watching personal bags isn’t a duty the volunteer has agreed to.|她帮同事看管设备。|She watches the equipment for a colleague.
收藏|keep in a collection|sưu tầm|我想收藏稿子，不是把它放进交换的书里。|I want to keep the pages, not place them among books for exchange.|她收藏了几张老节目单。|She kept a few old programmes in her collection.
场馆|venue building|khu tổ chức|场馆管理员知道仓库在哪，但没看见每个袋子。|The venue manager knows the storeroom, not every bag’s movements.|这个场馆周日才开放。|This venue only opens on Sunday.
场地|event space; venue|địa điểm|场地太满，我们把不用的东西先移开。|The venue is crowded, so we move unneeded things aside.|这次演奏换了场地。|This performance has changed location.
前来|come to a stated place|đến|前来换书的人越来越多，门口需要留空。|More people came to exchange books, so the entrance needed clearing.|她前来确认活动时间。|She came to confirm the event time.
路过|pass by|đi ngang|我只是路过楼道，不知道谁拿着袋子上楼。|I only passed the corridor and don’t know who carried the bag upstairs.|他路过门口时听见音乐。|He heard music while passing the entrance.
沿着|along|dọc theo|沿着楼道走到尽头，就是仓库。|Follow the corridor to its end for the storeroom.|他们沿着河边走。|They walk along the river.
两侧|both sides|hai bên|门的两侧都有箱子，我把袋子放到右边。|Boxes stand on both sides of the door; I put the bag on the right.|通道两侧放着椅子。|Chairs stand on both sides of the passage.
前方|ahead; in front|phía trước|前方正在搬桌子，我们先等一下。|They are moving a table ahead, so we wait.|前方那栋楼就是我们要去的。|The building ahead is our destination.
此处|this place; here|nơi này|纸条写此处放个人物品，后来位置变了。|The note says personal items go here; the location later changes.|此处暂时不能进入。|This area is temporarily closed to entry.
此前|previously; before this|trước đó|此前我只知道袋子还回来了。|Before this I only knew the bag had been returned.|此前活动一直在小厅。|Previously the event was always in the small hall.
事后|after the event|sau sự việc|事后我们一起补清了每一步。|Afterwards we reconstructed each step together.|他事后才听说时间改了。|Only afterwards did he hear that the time had changed.
当作|treat as|coi là|我把袋子的颜色当作位置的证明，记错了。|I wrongly treated the bag’s colour as proof of its location.|他把这次尝试当作练习。|He treats this attempt as practice.
恰好|happen to; just|vừa đúng|她恰好看见我放纸，知道袋子那时还在。|She happened to see me insert the pages and knew the bag was there then.|今天恰好没有别的安排。|Today happens to have no other plans.
特地|especially for a purpose|đặc biệt|我特地带来原稿，想请大家排练。|I specially brought the original pages for rehearsal.|她特地来听最后一场。|She came specially for the final performance.
抱歉|sorry|xin lỗi|抱歉，我以为这个也是活动的东西。|Sorry, I thought this belonged to the event too.|现在不便通话，抱歉。|Sorry, a call is inconvenient now.
道歉|apologise|xin lỗi|我为没有问就搬走道歉。|I apologise for moving it without asking.|她先道歉，再说明自己的安排。|She apologised first, then explained her arrangement.
通报|inform relevant people|thông báo|我们向在找袋子的人通报已经找到。|We told the people searching that the bag was found.|负责人通报了新的地点。|The organiser announced the new location.
传出|come from inside; spread|truyền ra|仓库里传出搬椅子的声音。|The sound of moving chairs came from the storeroom.|这个消息从小组里传出去了。|This news spread outside the group.
回应|respond; response|phản hồi|志愿者回应说袋子是他搬上去的。|The volunteer responded that he had moved the bag upstairs.|她回应了关于时间的问题。|She answered the timing question.
追究|investigate responsibility|truy trách nhiệm|先把经过问清，不急着追究谁故意做了什么。|Clarify the events before pursuing claims of deliberate acts.|他们还在追究记录出错的原因。|They are still investigating the cause of the recording error.
涉及|involve; concern|liên quan|这个误会涉及放的位置和搬的人，不只涉及颜色。|The confusion concerns placement and the mover, not only colour.|讨论涉及三个不同的安排。|The discussion concerns three different arrangements.
''')
D=rows('''
蓝袋子你还给我了吗？|Did you return the blue bag?
早上放门右边了，还是空的。|I put it on the right of the door this morning, empty.
我后来把稿子放进去，现在袋子不见了。|I put the pages in later, and now the bag is gone.
你不是一直拿着？|Weren’t you holding it the whole time?
没有，放完纸就去搬桌子了。|No, after putting in the pages I went to move a table.
那我们先找刚才在门口的人。|Then ask who was at the door.
有人说东西都搬地下室了。|Someone said everything went to the basement.
那是猜的吧？今天没有用地下室。|Isn’t that a guess? We haven’t used the basement today.
我在楼道看到一张稿纸，不知道怎么掉出来的。|I saw a page in the corridor; I don’t know how it fell out.
先别把它跟任何人连起来，问问谁搬过袋子。|Don’t attach it to a person yet; ask who moved the bag.
志愿者说门口太满，袋子和纸箱一起放到二楼了。|The volunteer says the entrance was crowded, so he moved it upstairs with the boxes.
原来还在楼里。那稿子应该也在？|So it’s still in the building. The pages should be there too?
先去看。我只看到楼道那一张，还没看袋子里面。|Let’s check. I only saw that one sheet, not the contents.
找到啦，这就是我的。里面少了哪一页？|Found it—this is mine. Which page is missing?
先按页码排，别只数张数。|Sort by page number, not just count sheets.
三在这里，四就是楼道那张。后面五也在。|Three is here; four is the corridor sheet, and five is here too.
好，连上了。没有少新的那一段。|Good, they connect. The new section isn’t missing.
我早上放的是空袋子，你后面放纸，我真的不知道。|I returned an empty bag this morning; I didn’t know you added pages later.
我现在知道了，刚才一着急像是在问你丢哪了。|I understand now. In my rush I sounded like I was asking where you lost it.
你可以问，我也没把放的位置写给你。|You can ask. I also hadn’t written the location to you.
志愿者道歉说以为是交换的东西。|The volunteer apologised; he thought it was exchange material.
那给个人袋子换个地方，不跟活动纸箱放一起。|Then give personal bags a different spot, away from event boxes.
行，先把这段排了。等会儿我拿着袋子，你搬桌子。|Okay. Rehearse first; then I’ll hold the bag while you move the table.
这回谁拿着说清了。别又把我的伞也当稿子。|Now we know who has it. Don’t take my umbrella for script pages too.
''')
M=rows('''
你不是说那张纸一直在包里吗？|Didn’t you say that page was always in the bag?
我是说我放进去的时候在。|I meant it was there when I put it in.
后面呢？|And later?
后面我去搬桌子，没一直看着。|I moved a table afterwards and didn’t watch constantly.
所以不是一直，是那时候。|So not always, but at that time.
对。刚才急了，把一刻说成一上午。|Right. I was rushed and turned one moment into the whole morning.
那现在袋子谁拿？|Then who has the bag now?
我拿，直到排练结束。|I do, until rehearsal ends.
这句能记下来。|We can note that.
你别连伞也记进去。|Don’t include the umbrella too.
伞是谁的？|Whose umbrella?
我的，这次不用重新找一个下午。|Mine. We needn’t spend another afternoon finding it this time.
''')
R=rows('''
周五晚上我借了陈宇的蓝袋子，带几本书回家。周六上午到换书活动时，书已经拿出来，我把空袋子放在一楼门右边，准备等他来搬东西时交还。门的两侧都堆着箱子，我特意放到里面一点，没有挡住入口。我没有发消息写具体位置，以为他一到就会看见。那一刻袋子里是空的，这一点我知道；后面谁再放了东西，我不在旁边。|I borrowed Chen Yu’s blue bag Friday and returned it empty beside the downstairs door Saturday. I placed it inside the boxes to clear the entrance but sent no exact location. I knew its initial state, not later additions.
陈宇来了以后先把蓝袋子找到，放进去五页新稿子，接着去搬桌子。我当时在活动桌旁帮人找书，只看到他从门口走过，没有看到他放纸。后来他说你还了吗，我才知道袋子又不见了。我第一句话问他不是一直拿着吗，其实把自己想象的交还过程当成了后面一直发生的事。袋子到了他的眼前，不等于后来始终在他手里。|He inserted five new pages and moved a table while I helped find books. His question revealed the missing bag. My assumption he had held it continuously turned an imagined handover into an unsupported duration claim.
我们先问门口几个人，有人说不用的东西都到地下室去了。场馆有地下室，可今天没有用。我问这个人是不是看见蓝袋子，他说只是想到以前的活动常放那里。这个答复让我们少走一段路：地下室存在、以前放过东西，都不能说明今天的袋子也在那里。我们没有怪他愿意出主意，只把这个线索留在还没看到的那一类。|A basement suggestion came from past events, not seeing today’s bag. We kept it as an unconfirmed possibility rather than blame someone offering an idea or treat a possible storage place as an observed move.
我后来路过楼道，看见一张纸，字像陈宇的新稿子。他看了说是第四页，另外几页还不知道在哪。纸在这里说明它离开了袋子，可谁掉的、怎么掉的，我们那时不知道。我差点说是不是搬桌子时自己掉了，又停住，因为陈宇搬的是桌子，不一定带着袋子。把两个同时出现的东西连成一个动作，听起来顺，却可能让时间又错一遍。|A corridor sheet was page four. It had left the bag, but we didn’t yet know who dropped it. His moving a table did not establish carrying the bag simultaneously; a smooth account could misjoin actions.
负责门口的志愿者听见我们问，才说蓝袋子跟两只纸箱一起搬到二楼仓库。他看见门口越来越满，以为都是活动待用的东西，就先移开。他记得上楼时纸从袋口露出来，不知道后来有没有掉。他没有把袋子送出楼房，也没有带给来换书的人。这个说明把我们要找的地方缩到二楼，不是立刻证明里面每页都完好。|The entrance volunteer said he moved the bag with two boxes to the upstairs storeroom, assuming event material. He remembered exposed paper, not whether one later fell. The account narrowed location without certifying contents.
我们沿着楼道上去，仓库里正有人收椅子。管理员把门开大一点，让我们看见靠墙的一排东西。蓝袋子在纸箱旁，里面的稿子还有四张。陈宇先看页码，一、二、三、五都在，再把楼道的四放回去。这样不只是重新数成五张，也确认是原来五页各有一份，没有靠两张相同的纸把缺的一页遮过去。|Upstairs we found the bag with pages one, two, three and five. Adding corridor page four restored the distinct set, not merely a count of five possibly including duplicates.
志愿者说抱歉，以为是交换的书和资料，没有先问就搬了。他没有答应看管每个人的包，我们也没说他本来就应该整场守着，只请他以后遇到不确定的个人物品先问。陈宇也承认自己的稿子应该收好，不跟可领取的资料放同一处。我说早上还的时候该把位置发清，而不是只靠大家碰巧都看见同一个颜色。|The volunteer apologised for moving without asking, not for an unagreed duty to guard every bag. We requested questions on uncertain personal items; Chen Yu planned better storage and I a clearer return message.
我们把个人袋子移到另一张桌子，贴了说明，再向还在找的人说已经找到了。有位朋友说我就知道没丢，我笑说刚才我们可不知道。他拿起水杯，问还用不用去地下室，我赶紧说不用了，也在群里补了一句。楼下的朋友回复，幸好看见消息，要不就白跑一趟。管理员让我们把蓝袋子带走，桌上只留下场馆的东西。陈宇收好五页稿子，说明天交给演出的人，今晚先不再挪地方。|We moved the personal bags to another table, labelled them and told the searchers we had found the bag. A friend said he had known it was not lost; I laughed that we certainly had not known that earlier. He asked whether he still needed to check the basement. I quickly said no and updated the group. A friend downstairs was glad to see the message before making a wasted trip. The manager asked us to take the blue bag away and leave only venue equipment on the table. Chen Yu put all five pages together. He would hand them to the performers tomorrow; tonight they would stay put.
排练开始时，陈宇从第一句读起，读到第四页还专门晃了一下，大家都笑了。那张纸回来以后有一点折痕，但字能看清，我们用它继续排。小组没有为了把故事讲得完美，就说所有东西从来没出过问题，也没有因为一次移动就取消换书活动。活动能继续，是我们把稿子找回、把位置分开，并把谁拿着说清以后做出的安排。|We rehearsed using the slightly creased but legible recovered page, with a small joke at page four. Continuing depended on retrieval and clearer placement, not pretending nothing happened or cancelling the whole event.
后来我跟没在场的朋友讲，先说周五借、周六空袋子还到门边，再说陈宇放稿、志愿者搬到二楼、楼道找到第四页。我没有按自己发现线索的顺序把上楼放到放纸以前，也没有把每一步都说成自己亲眼看见。哪些是我做的、哪些后来听别人说明，讲到那里就说明。故事终于有了顺序，不必因此把讲的人变成整个上午一直站在所有地方的人。|My later retelling ordered lending, empty return, added pages, upstairs move and page recovery. Discovery order did not replace event order, and I attributed others’ accounts instead of claiming to witness the whole morning.
''')
P=rows('''
我特地带五页新稿子来换书活动，想结束以后请大家排一次。到门口看见自己的蓝袋子，我很自然地把纸放进去，觉得比一直拿在手里方便。门边箱子很多，我知道有人在搬，却没有问蓝袋子会不会也被移走。放好以后我去帮忙搬桌子，回头准备排练时才发现原来的地方空了。那一刻我想起袋子昨晚借给林安，先问她还了没有。|I brought five pages for later rehearsal, found my returned bag and put them in without asking about relocation. After table moving I found the space empty and first asked the borrower about returning it.
林安说早上放右边，空的。我有点着急，听见空就以为她在说现在仍然没有纸，差点打断。她解释说那是自己还的时候，不知道我后来放了什么。我才明白我们说的是两个时间里的同一个袋子。她能说明自己交还的一段，我能说明自己放纸的一段，谁都还不知道后面被移到哪里；不能把她不知道后面理解成她没说清前面所有事情。|Her “empty” described the return time, not current contents. We each knew different stages of the same bag; missing later knowledge didn’t invalidate her initial account.
有人建议地下室，我很想马上下去找。林安问是不是看到那里，我觉得多问这一句有点慢，后来反而省了路。那个人只记得以前，今天没有看见。我们没有把这个建议删掉说完全不可能，而是先去问今天搬过东西的人。找东西时很想每句话都有确定答案，可一个可能的地方跟已经知道的地点，仍然需要分开。|I wanted to chase the basement idea immediately; her source question saved a trip. We retained a possible place without calling it known and prioritised people who had actually moved items that day.
林安拿来楼道的一张纸，我认出是第四页。我记得放进去五张，却不能靠这个记忆保证现在仍是五张。稿子从手里进入袋子的那一刻很清楚，之后我没有一直看。那时我说一直在袋里，她问你后来也看着吗，我承认没有。把一句一直改成放进去时在，让我们能继续找后面的变化，不必为保留自己最初说法跟朋友争很久。|Page four established a changed state after my insertion. I revised “always in the bag” to “there when I put it in,” allowing us to investigate later movement without defending an overstated duration.
志愿者说搬到二楼时，我终于松口气。他先把袋子当成活动物品，跟两只纸箱一同搬走，目的是让入口空出来。他说纸露在袋口，我想到自己没有拉好。我没有要求他承认故意弄丢，也没有因为他是在帮助活动，就说所有后果都不需要处理。先找到东西、确认有没有少，才是当时最需要一起做的事。|The volunteer’s clearing-the-entrance account gave a location. Exposed pages reminded me I had not closed the bag. Neither alleged intent nor good intentions removed the need to locate and check contents.
上楼以后，袋子里面只有四张，我一时又紧张，直到把页码逐个排出来。一到三和五都在，楼道那张正好是四。纸上有新的折痕，我想收藏原稿，多少觉得可惜，但是不妨碍这次读和排。说找齐了不等于每张跟以前一模一样，我可以为折痕遗憾，同时知道最重要的新段落还完整，活动不必因为这点遗憾全部停下。|Four sheets upstairs plus page four restored the set. A new crease was disappointing for a kept original but did not impair reading. Completeness did not mean unchanged physical condition.
我们跟志愿者一起把放东西的地方改了，他为没问就搬道歉，我也谢谢他说明自己做了哪一步。林安没有看到他上楼，管理员没有看到我放纸，所以后来要讲完整经过，还是得把不同人的说明连起来。我不把自己从头到尾问出来的答案都改成亲眼见到，也不让一个人负责证明所有人的动作；每个知道一段的人把那一段说明白，就能接成一个有用的过程。|We changed placement and combined the volunteer’s, borrower’s and my accounts. Reconstructing through others did not make every fact my direct observation or require one person to certify everyone’s actions.
排练时林安说这次袋子我拿，桌子你搬，大家觉得比刚才清楚。我说好，不过伞还是你自己拿。那个玩笑没有把袋子走错地方的事再次变成谁没用，只提醒我们现在的分工。稿子在我手里直到排练结束，然后我放进自己的背包，回家又确认一遍。这次不用问一上午到底都在哪里，因为我主动把后面一段也安排了。|A specific division of bag holding and table moving supported rehearsal, with an umbrella joke rather than personal blame. I retained the pages until rehearsal ended and then in my backpack.
晚饭时有人问今天是不是有人拿走我们的资料，我说有人移到了仓库，不是带走离开楼房；纸掉了一页，后来找齐了。这些话听起来不如差点全丢了戏剧化，却更像真的发生过的事。若只说拿走，朋友可能以为活动里有人把私人东西领回家。我补上从哪里到哪里，也说找回以后仍有折痕，让结果不把过程全部盖住。|At dinner I described relocation within the building and recovered pages rather than sensational loss. “Taken away” needed origin and destination so it wasn’t heard as someone claiming private materials. Remaining creases stayed in the account.
我后来把新稿整理成一份副本，原来的留在家里，活动带副本。这不是因为从此每个人都不可信，而是我想收藏的东西不必每次都经过同样的搬动。我们还会互相借袋子，也会遇到东西临时换地方。重要的是交还时多说位置、个人物品跟活动资料分开，以及讲起一个上午时知道自己到底看见了哪一段、又在哪一段听了别人的说明。|I kept originals at home and brought copies later, a practical choice rather than universal distrust. Future loans and moves could continue with location messages, separated items and accurate account attribution.
''')
G=[
card('此前 / 当天 / 事后','Keep the time reference attached to each account','These expressions organise before, on the relevant day and after. The reference event must remain clear; discovery order is not necessarily event order.','此前我只知道袋子还回来了。|Before this I only knew the bag had been returned.\n事后我们一起补清了每一步。|Afterwards we reconstructed each step together.','事后知道的事一定都是事后才发生。','事后我们一起补清了每一步。','Knowing something later does not place its occurrence later.'),
card('沿着 / 至','Read route and endpoint in organised language','沿着 introduces the path followed; 至 introduces an endpoint in more formal directions. Neither necessarily means passing every room.','沿着楼道走至尽头，就能看到仓库。|Follow the corridor to its end to see the storeroom.\n沿着河边走至桥旁再停。|Follow the riverbank to the bridge, then stop.','沿着楼道走至尽头，表示每一间房都已经进去看过。','沿着楼道走至尽头，就能看到仓库。','A route instruction does not establish inspection of every room.'),
card('或…，或…','Keep alternative causes unconfirmed','Written 或 clauses offer possibilities. They are not a list of events all known to have happened.','纸或是上楼时掉的，或是放下时掉的。|The sheet may have fallen while going upstairs or when put down.\n他或在门口，或在活动桌旁。|He may be at the door or the event table.','或上楼时掉或放下时掉，证明这张纸掉过两次。','纸或是上楼时掉的，或是放下时掉的。','Alternatives do not establish two falls.'),
card('被…给…','Retell the affected object in a colloquial passive','Give the object, agent and result only as known. 给 adds colloquial emphasis; it does not imply intention.','袋子被志愿者给搬到二楼了。|The bag was moved upstairs by the volunteer.\n那张纸被风给吹到桌边了。|The sheet was blown to the table edge by the wind.','袋子被志愿者给搬到二楼，证明他故意想弄丢。','袋子被志愿者给搬到二楼了。','The passive describes an effect without proving a motive.'),
card('A一量，B一量','Recognise a distributed description','Parallel noun-plus-one-measure phrases can present things distributed over space. The measure should suit the item; this is a written descriptive form, not a precise inventory by itself.','门口一箱，楼道一箱，东西放在不同位置。|A box at the entrance and a box in the corridor put things in different places.\n这边一张，那边一张，纸散在桌上。|A sheet here and a sheet there lie across the table.','这边一张那边一张，说明全部页码已经核对过。','这边一张，那边一张，纸散在桌上。','Distribution is not confirmation of a complete numbered set.'),
card('就算…，也…','Maintain a limit after a recovered result','A later good result does not retroactively certify earlier knowledge or perfect condition. 就算 may be hypothetical or concessive according to context.','就算找齐了，也不能说从来没有移动过。|Even with the complete set recovered, we cannot say it never moved.\n就算现在知道，也不能说刚才一直知道。|Even knowing now doesn’t mean always knowing earlier.','就算现在知道，也说明刚才一直知道。','就算现在知道，也不能说刚才一直知道。','Later knowledge does not rewrite its earlier absence.'),
]
spec=dict(title=('The bag has another route','把一个上午讲清楚'),goals=['Reconstruct event order from overlapping first-person accounts','Retain source, time and location in a longer retelling','Distinguish recovered completeness from unchanged condition'],vocabulary=V,grammar=G,
dialogue=(D,[q('gist','How is the missing bag found?','Combine accounts of return, insertion and upstairs relocation','Assume every item is in the basement','Conclude it left the building from its absence at the door'),q('detail','Which page is found in the corridor?','Page four','Page one','Page five'),q('inference','Why check numbers rather than only count sheets?','To restore each distinct page, not a total containing duplicates','To prove every paper stayed perfect','To discover a sixth page had always existed')]),
reading=(R,[q('gist','What does the narrator improve in the retelling?','Event order and attribution instead of imagined continuous observation','An accusation of intentional loss','A claim that nothing moved'),q('detail','Where is the bag found?','The upstairs storeroom','The basement','Outside the building'),q('inference','Did earlier basement use prove today’s location?','No, it was an unobserved suggestion','Yes, past use determines every future location','Yes, the volunteer had said basement')]),
pairedTitle='The friend who put in the pages',pairedReading=(P,[q('gist','What does the other account add?','Insertion time, incomplete observation and a practical later copy','Proof the borrower watched every later action','A claim that no crease remained'),q('detail','What remains different after recovery?','A new crease, though the pages are readable and complete','All five pages are missing','The new section has disappeared'),q('inference','Why keep originals at home later?','To protect a valued original from repeated moving without ending trust','To ban every future bag loan','To prove the volunteer intended damage')]),
mediaTitle='At that moment, not all morning',media=(M,[q('detail','What claim is corrected?','Always in the bag becomes there when inserted','Nobody inserted pages','The bag never existed'),q('inference','What does the new statement add?','Who holds the bag and until when','A guarantee of every future day','Proof of all unknown earlier movements')]),
glosses=[('啦','particle expressing a lively or changed state'),('副本','copy of a document'),('折痕','crease'),('页码','page number'),('重复','repeat; duplicate'),('副','copy; auxiliary'),('原稿','original manuscript'),('志愿者','volunteer'),('纸箱','cardboard box'),('堆','pile up'),('袋口','opening of a bag'),('露','be exposed; show'),('拉好','close or fasten properly'),('背包','backpack'),('晃','shake; wave slightly'),('暂','temporary'),('暂时','temporarily'),('领','receive; collect'),('空','empty'),('挡','block'),('信任','trust'),('痕','mark; trace'),('叙述','narrate'),('归还','return something'),('管理员','venue manager'),('藏','keep; hide'),('全丢','lose everything'),('遮','cover; conceal'),('失误','mistake'),('折','fold; crease'),('可靠','reliable')],
place='A community book exchange followed by rehearsal',context='Friday bag loan; Saturday empty return at downstairs door; Chen Yu inserts pages1–5 then moves table. Volunteer relocates bag with boxes to upstairs storeroom. Page4 found in corridor; bag contains1,2,3,5. Set recovered with a crease; basement suggestion is based only on prior events.',
turns=[('林安早上还的是空袋子，说明陈宇后来没放纸吗？','Lin An returned an empty bag. Does that mean Chen Yu never added pages later?','Retain the two time references',['不说明，说的是不同时间里的袋子。']),('门口不见了，就一定出了楼房吧？','Gone from the entrance means it left the building?','Avoid an enlarged location claim',['不一定，也可能移到楼里别处，先问搬的人。']),('四张加一张等于五，就不用看页码吧？','Four plus one is five, so no need for page numbers?','Check the distinct set',['还要看页码，确认每页都有，不是重复一张。']),('现在找齐，就能说刚才一直知道在哪吗？','Now recovered, can we say we always knew where it was?','Preserve earlier uncertainty',['不能，找齐是后来的结果。'])],
usage=[('Attach the time to the observation','我放进去时在，后来没有一直看。','It was there when I inserted it; I wasn’t watching afterwards.','Do not stretch one moment into a whole period.'),('Name the account source','志愿者说他搬到二楼，我没看见上楼那段。','The volunteer says he moved it upstairs; I didn’t see that part.','A reconstructed account retains attribution.'),('Update the result accurately','页码都齐了，有一张多了折痕，但还能读。','All page numbers are present; one has a crease but remains legible.','Complete contents need not mean unchanged condition.')],
tasks=practice(
[(R[0][0],R[0][1],'The borrower directly sees all later contents.',False,'They know the empty return, not subsequent insertion.'),(R[3][0],R[3][1],'The corridor sheet is page four.',True,'Chen Yu identifies its page number.'),(P[5][0],P[5][1],'Recovery means every sheet is physically unchanged.',False,'A new crease remains.'),(P[9][0],P[9][1],'Bringing copies later ends every future bag loan.',False,'Practical protection does not imply universal distrust.')],
[('她先还空袋子，他后放五页纸。两个说法冲突吗？','She first returns an empty bag; he adds five pages later. Do these accounts conflict?',['不冲突，时间不同。','冲突，袋子只能永远空。','冲突，还过就不可能再放东西。'],0,'Sequential states can differ.'),('一二三五在袋里，楼道找到四。把四放回后齐了吗？','Pages one, two, three and five are in the bag; four is found in the corridor. Is the set complete after adding four?',['齐了，原来五个页码各有一页。','没齐，还缺第四页。','齐了，所以每页一定没有新折痕。'],0,'Completeness concerns the distinct numbered set, not physical perfection.'),('有人只说以前用地下室，这能确定今天的袋子在那吗？','Someone says the basement was used before. Does this determine today’s bag location?',['不能，要问今天有没有看到。','能，以前用过就永远在那里。','能，他已经看见袋子了。'],0,'Previous use is not present observation.'),('志愿者移动了袋子，能直接写故意弄丢吗？','The volunteer moved the bag. Can we write deliberate loss directly?',['不能，移动和故意弄丢不同。','能，任何移动都证明恶意。','能，找到以后也证明没有搬过。'],0,'An action does not alone establish the claimed motive.')],
[('事后我们一起补清了每一步。','Afterwards we reconstructed each step together.','事后'),('沿着楼道走到尽头，就是仓库。','Follow the corridor to its end for the storeroom.','沿着'),('他把个人的袋子当成交换活动的物品了。','He took a personal bag for an exchange-event item.','当成'),('就算现在知道，也不能说刚才一直知道。','Even knowing now does not mean always knowing earlier.','也')],
[[(V[i][3],V[i][4]) for i in [0,2,4]],[(V[i][5],V[i][6]) for i in [6,7,9]],[(V[i][3],V[i][4]) for i in [12,14,16]],[(V[i][5],V[i][6]) for i in [20,21,24]],[(V[i][3],V[i][4]) for i in [26,29,31]]]),
review='Native review: bag/page banter, colloquial time-scope correction, parallel A一量B一量 description and source-attributed retelling. Self-review preserves loan→empty return→five-page insertion→upstairs move→page4 recovery. The basement is merely a suggestion; bag stays inside building. Four distinct pages plus4 restore1–5; a crease remains. No one is marked witness to all steps, volunteer has not promised personal-bag supervision, and an action is not scored as intentional loss. Two accounts contain different available information while agreeing on the recovered sequence.')
write(6,7,spec,publish='--publish' in sys.argv)
