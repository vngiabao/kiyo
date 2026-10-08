"""A final rehearsal, a quoted line, and an unfinished farewell."""
import sys
import common
from advanced_core import write,rows,words,q,card,practice
common.dictionary.update({'主角':'zhǔ jué','看管':'kān guǎn','收藏':'shōu cáng','一番':'yì fān'})
V=words('''
稿子|written draft; script pages|bản thảo|我拿的是改过的稿子，最后一句已经换了。|I have the revised pages; the last line has changed.|她把稿子读了两遍。|She read the draft twice.
台灯|desk lamp|đèn bàn|台灯照着桌面，门口看不清纸上的字。|The lamp lights the desk; the writing isn’t visible from the door.|他关掉台灯才出门。|He turns off the desk lamp before leaving.
收藏|collect; keep as a collection|sưu tầm|我想收藏这张节目单，记住最后一次。|I want to keep the programme as a memory of the final performance.|她收藏旧照片。|She collects old photos.
歌词|words of a song|lời bài hát|歌词里说等，不说明等的人一定会回来。|The lyrics mention waiting, not a guarantee of someone’s return.|这首歌的歌词是她写的。|She wrote the song’s lyrics.
演奏|perform music, usually with an instrument|biểu diễn nhạc|最后一段由陈宇演奏，我不唱。|Chen Yu plays the last section; I don’t sing.|她用钢琴演奏这首曲子。|She plays the piece on the piano.
掌声|applause|tiếng vỗ tay|掌声停下以后，我们才说最后的告别。|We say our final farewell after the applause stops.|他听见掌声，回头笑了。|He heard applause and turned with a smile.
上台|go onto the stage|lên sân khấu|上台以前，我还没决定最后那句话。|Before going onstage I still hadn’t decided the final words.|第一次上台时，她有点紧张。|She was nervous on her first time onstage.
上演|be performed; be staged|được trình diễn|这段短剧只在周日上演一次。|This short play is performed once on Sunday.|新的节目下周开始上演。|The new show starts next week.
主角|central character; lead role|vai chính|主角说别找我，下一场却回头等。|The lead says not to look for them, then waits in the next scene.|这部电影有两个主角。|The film has two central characters.
看管|look after; supervise|trông coi|排练时请他看管门口的设备。|Ask him to supervise the equipment by the door during rehearsal.|她帮朋友看管行李。|She watches a friend’s luggage.
截止|close; reach a stated deadline|kết thúc thời hạn|报名周五中午截止，演出在周日。|Registration closes Friday noon; the performance is Sunday.|申请明天截止。|Applications close tomorrow.
隐藏|hide; conceal|che giấu|她没有隐藏明天要走，只是还没想好怎么告别。|She isn’t hiding tomorrow’s departure; she hasn’t settled on a farewell.|字被折起来的一角隐藏了。|The folded corner concealed the writing.
透露|disclose; reveal|tiết lộ|她只透露新工作在邻城，没有说住哪里。|She only revealed that the new job was in the neighbouring city, not where she would live.|信的开头透露了写信的原因。|The letter’s opening revealed its reason.
名义|name; stated capacity or purpose|danh nghĩa|别以送行的名义，把整晚都排成我的讲话。|Don’t use a send-off as a reason to schedule speeches from me all evening.|她以小组的名义发出邀请。|She sent the invitation on behalf of the group.
情绪|mood; emotion|tâm trạng|台词里的情绪重，不等于排练的人真的在吵。|The line carries strong emotion, not necessarily a real quarrel between performers.|她走了一会儿，情绪慢慢平静。|After walking a while her mood gradually settled.
遗憾|regret; a disappointing lack|tiếc nuối|没能每个人都说一句，是这晚的小遗憾。|Not everyone getting a turn was a small regret that evening.|没赶上开头，我觉得遗憾。|I regret missing the opening.
心愿|wish from the heart|mong ước|我的心愿是再一起排一次，不是办一场大送行。|I wish for one more shared rehearsal, not a grand send-off.|她把心愿写进新年卡。|She wrote her wish in a New Year card.
孤独|lonely; loneliness|cô đơn|诗里的孤独不一定等于写诗人此刻的心情。|The poem’s loneliness needn’t equal the writer’s current feeling.|一个人住有时舒服，有时孤独。|Living alone is sometimes pleasant and sometimes lonely.
增进|promote; deepen a relationship or understanding|tăng cường|一起排练增进了了解，也让我们发现不同习惯。|Rehearsal deepened understanding and revealed differing habits.|这次交流增进了两组的联系。|This exchange strengthened links between the groups.
平衡|balance|cân bằng|想感谢朋友，也想保留安静的时间，需要平衡。|Thanking friends and keeping quiet time need balancing.|她在工作和休息之间找平衡。|She seeks a balance between work and rest.
一番|one sustained instance of words or effort|một phen|一番讨论以后，我们决定把最后的歌留短。|After some discussion we decided to keep the last song short.|听完一番解释，他重新想了想。|After hearing an explanation he reconsidered.
场景|scene; setting|khung cảnh|这个场景里有一扇门和一盏台灯。|The scene contains a door and a desk lamp.|我记得那个雨里的场景。|I remember the scene in the rain.
场馆|venue building or complex|nhà, khu tổ chức|场馆十点关门，我们九点半开始收。|The venue closes at ten; we start packing at 9:30.|新场馆离车站不远。|The new venue isn’t far from the station.
送行|see someone off|tiễn|明天我自己去车站，今晚就算送行。|I’ll go to the station myself tomorrow; tonight can be our send-off.|她到门口给朋友送行。|She went to the doorway to see her friend off.
送礼|give a gift|tặng quà|不用再送礼，这张一起写的卡已经够了。|No extra gift is needed; this jointly written card is enough.|她喜欢送礼，也会先问对方需要什么。|She likes giving gifts and first asks what someone needs.
难忘|unforgettable; memorable|khó quên|这次难忘，不只是因为有人离开。|This is memorable for more than someone leaving.|那顿饭成了一个难忘的晚上。|That meal became a memorable evening.
过后|after something has passed|sau đó|掌声过后，灯又亮了一点。|After the applause the lights brightened a little.|雨过后，路上还有水。|After the rain water remained on the road.
不再|no longer|không còn|我不再每周来这里，也还可以跟你们联系。|I won’t come here weekly any longer, but can stay in touch.|他不再把那句话当作真的告别。|He no longer treats that line as a real farewell.
时而|at times, alternating with another state|lúc thì|她时而看稿子，时而望向门口。|She alternates between the pages and the doorway.|灯光时而亮，时而暗。|The light is bright at times and dim at others.
盼望|look forward to; hope for|mong đợi|我盼望下次再见，不保证哪天就能回来。|I look forward to meeting again, without guaranteeing a return date.|她盼望那封信早一点到。|She hopes the letter arrives sooner.
录像|record video; video recording|quay video|录像在最后一句以前停了，不能说已经拍完整。|The recording stops before the final line, so it isn’t complete.|她把排练录像留给没能到的人。|She kept a rehearsal recording for absent friends.
开头|beginning; opening|mở đầu|开头像在生气，后面才知道是排练。|The opening seems angry; later we learn it is rehearsal.|文章开头写的是一天早晨。|The article opens on a morning.
''')
D=rows('''
以后别找我了。|Don’t look for me again.
你这句要对着门，不是对着我。|That line is towards the door, not me.
我看见你站那儿，就说过去了。|I saw you standing there and aimed it at you.
幸好我知道是台词，不然真不知道怎么接。|Good thing I know it’s a line; otherwise I wouldn’t know how to answer.
你本来下句是什么？|What is your next line?
我说你忘了带伞，还得追出去。|I say you forgot your umbrella and have to chase you out.
那我说完就走太快了，你追不上。|Then I walked too fast after the line; you couldn’t catch me.
对，停一下，让我有机会开口。|Right. Pause and give me time to speak.
周日最后一场，你真的准备这样结束？|For Sunday’s last performance, are you really ending it this way?
戏这样结束。我们这晚别只剩一句别找我。|The play ends that way. Our evening shouldn’t end with only “Don’t look for me.”
我想让大家一人说一句，你会不会不喜欢？|I thought everyone could say something. Would you dislike that?
喜欢，只是别每个人都让我回一大段。|I’d like it; just don’t make me give a long reply to each person.
那最后唱一段，你想唱哪首？|Then one final song—which do you want?
唱我们自己写的那段，短一点。陈宇最后弹，我听。|Our own short verse. You play at the end, and I’ll listen.
歌词里说灯还亮，是不是一定会回来？|The lyric says the lamp is still lit. Does it guarantee a return?
可以让人盼望，别替我保证下周。|It can offer hope; don’t promise next week for me.
明天车票几点？要不要送你？|What time is tomorrow’s train? Shall we see you off?
九点。我自己去，今晚已经够热闹了。|Nine. I’ll go myself; tonight is lively enough.
那这把钥匙怎么还？|Then how will you return the key?
收完东西交给管理员，不是带去邻城。|After packing I’ll hand it to the venue manager, not take it to the next city.
我看见你把钥匙放包里，以为要先走。|I saw you put it in your bag and thought you were leaving early.
只是怕排练时丢了。你又给一个动作加了剧情。|Just to avoid losing it in rehearsal. You gave one action a plot again.
好，我不猜了。九点半收，十点以前走？|Okay, no guessing. Pack at 9:30 and leave before ten?
对。最后这晚还要一起收，别只留给我一个人。|Right. We pack together on this last evening too, not leave it all to me.
''')
M=rows('''
门还开着，灯还亮着。|The door is still open; the lamp still lit.
旧纸上，名字没有变。|On old paper the names haven’t changed.
风经过，不替我回答。|The passing wind doesn’t answer for me.
我听见，你慢一点的呼唤。|I hear your slower call.
走到门前，回头看一眼。|At the doorway I look back once.
不是昨天，也不只明天。|It isn’t yesterday, nor only tomorrow.
把没说完的话，放在桌边。|Leave the unfinished words by the desk.
这一晚，我们仍在这里见。|This evening we still meet here.
灯会关上，窗会合上。|The lamp will switch off; the window will close.
歌声停了，脚步还向前。|The singing stops; footsteps still go on.
再见不写成永远的保证。|Goodbye isn’t written as an eternal guarantee.
愿下一次，还能听你讲。|May I hear you talk again next time.
''')
R=rows('''
我到小厅门口时，听见林安说以后别找我了。那句话声音低，却很重，我差点以为她跟里面的人真的发生了什么。接着陈宇说你这句要对着门，我才知道他们在排练。门边只有一张桌子、一盏台灯和两页稿子，场景很简单。他们已经试了几次，陈宇每次追出去都来不及，因为林安把最后一句说完就走得太快。|At the hall I heard Lin An’s low, heavy “Don’t look for me again.” Chen Yu’s direction revealed rehearsal. A table, lamp and two pages formed the scene; her quick exit kept him from delivering the following line.
这段短剧是小组自己写的，主角说不想再见，下一句另一个人却喊他忘了带伞。两个人不是立刻和好，而是在门口有了重新开口的机会。林安试着停半拍，陈宇终于接上。我觉得那个小停顿比刚才的强烈语气更重要：它没有直接告诉观众以后会怎样，只让已经快关上的交流又有一点可能。|The original short play puts a forgotten umbrella after apparent farewell. A half-beat pause allows renewed speech without resolving the future; the pause matters more than intensity.
周日是这个小组在旧小厅的最后一场，场馆随后要重新安排用途。林安周一九点坐车去邻城，准备新工作。我们都知道这两件事，却不一定知道她对它们的感觉。有人很兴奋，觉得她终于开始新的生活；有人一直想多留她一会儿。林安自己既收节目单，也认真改稿子，没有选一个表情来代表整个晚上。|Sunday is the group’s last old-hall performance before a venue-use change, and Lin An leaves at nine Monday for a new job nearby. Excitement and a wish to linger coexist; her collection of programmes and revisions do not reduce to one emotion.
陈宇想把最后一晚办成送行，让每个人都说几句感谢。林安说喜欢听，但不想每听一段就被请上台回答一段。她想跟大家坐在一起，不想成为整晚唯一的主角。这个要求没有取消感谢，只是把感谢的形式改了。我们于是把讲话放在短剧以后，谁想说就说，她听完可以只回谢谢，也可以以后再写消息。|She welcomed thanks but did not want repeated onstage responses or to be the sole focus. The plan changed to optional remarks after the play, with short or later replies allowed.
排练里那句以后别找我，跟现实里的告别正好放在同一个晚上，很容易让人连起来想。可是我没有把她说那句时的低声当作她不想联系。她随后说不再每周来，还可以在群里聊，也想听大家以后排的东西。我能从这些话知道她没有关闭联系，却不能进一步替她安排固定回来几次。愿意继续联系和保证随时到场，不是同一份承诺。|The play’s line could colour the real farewell, but she explicitly wanted contact and future work updates. That supports continued contact without a fixed return schedule.
原来的节目里有一段很长的歌，林安觉得最后会累，就选了我们自己写的短歌段。歌里有灯、门和没说完的话，可以让人想到等一个朋友，也可以想到一个人走进新的生活。陈宇问灯还亮是不是等于一定回来，她笑着说别替我保证下周。她没有拒绝那种盼望，只是不愿意让一句歌词变成具体的车票。|She chose the group’s short original verse. Its lamp, door and unfinished words permit waiting or new beginnings. She welcomed hope without converting a lyric into a promised ticket home.
有人提议周一一起去车站，林安谢过，说自己去就好。听起来有一点可惜，我们也没有继续问是不是不愿意让大家送。她九点要走，早上还要收自己的行李；今晚想热闹，明早想安静，都可以是真的。我们可以觉得舍不得，也不用把每一次拒绝都解释成对整个小组的拒绝。当天愿意做什么，还要听她自己说。|She declined a group station send-off, retaining a lively night and quiet morning. Missing her did not justify turning one refusal into rejection of the whole group.
快结束时，我看见她把钥匙放进包，以为她准备先走。她说怕排练时掉，收完东西再交给管理员。后来我回想，如果只拍那个动作，旁边写马上离开，大家也可能相信。钥匙进包确实发生，什么时候还、为什么先收，得从后面的安排知道。看见一个动作可以开始提问，却不必立刻为它找一个最大、最难受的解释。|Her bagged key initially looked like an early exit. She explained safe storage and return after packing. A real action did not establish the inferred motive or departure time.
短剧上演时，林安说完以后别找我，在门口停了一下，陈宇带着伞追上去。观众笑了，后面又安静。我没有觉得那一笑把前面的难过全部消掉，也没有把最后的沉默当成看不懂。故事让不同的感受留在一个场景里，最后没有写两个人以后每天都会见面。灯关下去时，观众还可以继续想，他们会怎么开口。|The staged pause allowed the umbrella line; laughter and later quiet both remained. The play did not promise daily reunions or cancel sadness, leaving future speech open.
九点半大家开始收，林安也搬椅子。陈宇说今天别让她做，她却说最后一次也不是坐着看你们忙。我们没有把这句话听成她不需要任何照顾，就分两个人去搬重一点的桌子，其余各做一段。十点以前钥匙交了，大家走到门口说再见。最后一晚没有留下一个完美、完全不遗憾的结尾，但每个人都真正来过，做过一点事情，也说过自己想说的话。|At 9:30 everyone packed, including Lin An, with heavier work shared. They returned the key and left before ten. The evening remained imperfect and somewhat regretful, with real presence and contributions rather than a perfect ending.
''')
P=rows('''
最后一场的稿子改到周五，我已经知道林安周一要走。我把节目单最后一段写成送行，想让她在大家的掌声里说一段话。这样安排看起来很完整：我们感谢，她回应，再一起唱歌。可是我没先问她愿不愿意每一段都站到前面。排练休息时她说想听大家讲，也想和大家坐在一起，我才想到完整的节目不一定让被感谢的人舒服。|I initially made a tidy send-off programme with thanks, response and song, without asking how much onstage response she wanted. Her wish to sit with everyone exposed the difference between a complete plan and a comfortable recipient.
她没有对我说别办了，只是请我别把整晚都排成她的讲话。我把最后改成自愿说几句，林安不需要逐个长篇回答。有朋友担心这样显得不够重视，我说重视也可以是听见她希望怎样。我们不是少了一段感谢，而是少了一种规定好的回答。她以后在消息里回谁、回多少，是她自己的时间，不需要为了节目好看提前全部决定。|She limited the format rather than cancel it. We kept voluntary thanks without mandatory lengthy responses. Respect included hearing her preference, not prescribing later messages for a tidy show.
排练时她那句以后别找我总说得太快，我得追着说伞，可她已经出了门。后来她停一下，我就能把话接上。这个短剧不是我在劝她现实里留下，我们写的是两个想结束却又有话的人。把台词排清楚，是让观众有机会跟上转折；如果我一边排一边把每句话都变成对林安的挽留，她就不能安心演一个不完全像自己的角色。|The pause repaired the scripted umbrella turn. The play concerns fictional people who want to end things yet still have something to say; it wasn’t a covert attempt to keep Lin An from moving. She needed room to perform a different character.
有人只听见开头那句，问我们是不是有点不高兴。林安笑着说我下一句还得把伞给她，哪有那么快结束。我觉得这个解释很自然，比坐下来讲一长段人物跟本人不同有用得多。朋友听到后面，就明白我们在排练，也看见台灯和稿子。现实里我们当然也可能不高兴，只是不能把这一句被截下来的台词当成证据。|A listener mistook the opening for real tension. Explaining the next umbrella line and seeing the pages restored the rehearsal context without a lecture about actor identity. A quoted line alone wasn’t evidence of a real quarrel.
短歌是大家以前一起写的，里面有门和灯，还有桌边没说完的话。我本来很想把灯还亮唱成以后每次回来都有这里等她。可小厅也要换用途，这个地点未必一直不变。林安说可以保留盼望，不必保留同一间房。我们就没有给那句加固定回来的解释，让灯也可以是记忆里的灯，或者下一个地方的新灯。|The shared lyric’s lamp initially tempted me to promise the unchanged hall waiting for her. The venue was changing too, so we retained hope without requiring one physical room or fixed returns; the lamp could be remembered or new.
她把几张节目单放进袋子，说想带走。我还以为她要把其他资料都拿走，问后面排练怎么办。她指给我看，带的是自己收藏的几张，新的稿子留在桌上，录像也会发给没到的人。我松了一口气，觉得自己又把一件小事想得太大。收藏旧纸可以是喜欢过去，不是准备把小组的未来一并收进自己的包。|She kept selected programmes but left current pages and promised the recording. I had overread packing papers as taking all materials. Keeping memories didn’t mean removing the group’s future.
这晚很多人想跟她多聊，时间却不是无限的。场馆十点关闭，九点半要开始收。我们把长歌缩短，给自由讲话留十分钟，短剧结束以后先让大家坐一会儿。如果有人没来得及说，可以写在卡上。我们没有保证十分钟让每个人讲完整的人生，也没把到了关闭时间还不能结束，当作友情特别深的表现。|We kept the closing deadline, shortened the song and allowed ten minutes of optional remarks with a card for later words. Ten minutes did not promise exhaustive life stories or justify overstaying as proof of friendship.
上演以后，有个平时安静的朋友说第一次来时不敢开口，是林安问他喜欢哪本书。我才知道自己漏掉了这段小事。林安听见笑了一下，没有给出长篇回答，后来把那句写进自己的卡里。不是每份感谢都要在台上立刻换成同样长的回应；有时候听见、记住、以后再说，也会让说话的人知道自己的经历没有落空。|A quiet friend recalled Lin An’s first book question helping them speak. She smiled and later wrote it on her card rather than match its length onstage. Listening and remembering were real responses too.
收东西时，她想搬重桌子，我说换我，她说别什么都抢。我把另一边留给自己，两个人一起搬到原来的地方。这比争论她最后一晚到底该不该做事简单。她愿意参与，不等于我不能帮；我想帮，也不等于她必须完全坐着。我们把一个具体动作分好，就不用靠谁赢了讨论来决定这个晚上有没有照顾到她。|When she wanted to move a heavy table, we shared it instead of arguing whether the departing friend should do no work. Both participation and help remained possible.
到门口时，她把钥匙交给管理员，回头说下次有什么新东西发来听听。我说好，却没有再追问下次哪天回来。九点的车是已经确定的，下一次见面还没有。她走进新生活，我们继续排新的东西，联系可以在不同地方慢慢发生。小厅的最后一晚结束了，不必连同所有来往一起结束；这句是我当晚真的说得出口的，比永远不变更具体。|At the door she returned the key and requested future recordings. Monday’s train was settled; the next meeting wasn’t. The hall’s last evening could end without ending contact, which could develop across places without an eternal guarantee.
''')
G=[
card('X是X，…','Concede one judgement while adding a limit','Repeating X with 是 acknowledges that aspect, then qualifies it. Delivery can be matter-of-fact, reluctant or playful.','热闹是热闹，不过我明早想自己去车站。|It is lively, but tomorrow morning I want to go to the station myself.\n喜欢是喜欢，别让我每次都回一大段。|I do like it; just don’t make me give a long reply every time.','喜欢是喜欢，所以所有安排都必须照旧。','喜欢是喜欢，别让我每次都回一大段。','Acknowledging liking can coexist with a limit.'),
card('早不…，晚不…，…','Recognise an irritated timing complaint','This rhetorical pattern complains that something happens at a particularly inconvenient moment. It can sound sharp; recognise it without using it to pressure someone’s schedule.','早不问，晚不问，偏偏上台前问我车票。|Of all times, you ask about my ticket just before I go onstage.\n早不改，晚不改，偏在开场时改。|You choose the start of the show to change it.','早不问晚不问，表示早晚都已经问过了。','早不问，晚不问，偏偏上台前问我车票。','The complaint does not state that the question happened at both other times.'),
card('放着X不Y','Recognise a complaint about overlooking an available option','This construction highlights an available thing X that someone fails to use in the expected way Y. It often sounds teasing or critical, so recognise its force before copying it.','放着稿子不看，只看那张截图。|You have the script available but only look at the screenshot.\n放着椅子不坐，偏要站着。|You have a chair but insist on standing.','放着稿子不看，表示已经认真读完整份稿子。','放着稿子不看，只看那张截图。','The complaint says the available script was not read.'),
card('时而…，时而…','Follow shifting attention in a scene','时而 alternates attention or state across moments. It is common in narration and does not require equal time for each.','她时而看稿子，时而望向门口。|She alternates between the pages and the doorway.\n灯光时而亮，时而暗。|The light brightens and dims at different moments.','时而亮时而暗，表示每一秒都同时一样亮和暗。','灯光时而亮，时而暗。','The states occur at different moments.'),
card('为了…而…','Read purpose in organised narration','而 links an action to its purpose after 为了. A stated purpose does not guarantee the action produces that result.','为了让台词接上而停半拍。|Pause half a beat to let the next line connect.\n为了保留时间而缩短最后的歌。|Shorten the final song to retain time.','为了让台词接上而停半拍，所以每次都必然接得完美。','为了让台词接上而停半拍。','Purpose is not a guarantee of perfect execution.'),
card('一番 / 这番','Count a stretch of words or effort','番 can measure an extended instance of discussion, explanation or effort, rather than one individual sentence.','一番讨论以后，我们决定把最后的歌留短。|After discussion we decided to keep the last song short.\n听完一番解释，他重新想了想。|After hearing an explanation he reconsidered.','一番讨论规定只有一个汉字。','一番讨论以后，我们决定把最后的歌留短。','The measure does not count individual characters.'),
]
spec=dict(title=('The last rehearsal is not the last conversation','最后一晚，还没说完'),goals=['Follow a longer scene with quotation, motives and shifting feelings','Use subsequent details to revise a first interpretation','Retell the performance and real farewell without conflating them'],vocabulary=V,grammar=G,
dialogue=(D,[q('gist','What is the opening别找我line?','A rehearsal line whose following turn mentions an umbrella','A real ban on contacting Lin An','A promise to stay at the hall forever'),q('detail','When does Lin An plan to return the key?','After packing, to the venue manager','At Monday’s train platform','Before rehearsal so she can leave early'),q('inference','What does welcoming thanks without long replies show?','She welcomes thanks while limiting the response format','She refuses every expression of thanks','She agrees to speak for the whole evening')]),
reading=(R,[q('gist','What remains open at the end?','Future meetings and the play’s relationship, while the evening ends','Whether Monday’s train is at nine','Whether packing begins at 9:30'),q('detail','Why put the key in the bag?','To avoid losing it during rehearsal','To leave before the performance','To carry it permanently to the next city'),q('inference','What does continued contact not promise?','Fixed return dates or constant availability','Interest in later recordings','Willingness to talk in the group')]),
pairedTitle='The friend planning the programme',pairedReading=(P,[q('gist','How does the programme change?','It respects Lin An’s wishes rather than require long public replies','It cancels every thanks and song','It assigns Lin An every closing task'),q('detail','What does Lin An take away?','Selected old programmes; current script pages stay','All future materials and the venue key','Every recording so nobody else can rehearse'),q('inference','Why share the heavy table instead of argue about helping?','Her participation and someone else’s help can coexist','She must accept being completely passive','No one needs to pack before closing')]),
mediaTitle='The lamp and the unfinished words',media=(M,[q('detail','Does the lyric promise an eternal reunion?','No, it explicitly refuses an eternal guarantee','Yes, next week is fixed','Yes, the venue can never change'),q('inference','Which interpretation fits without becoming a factual promise?','Hope of hearing someone again despite an ending','A booked return train next week','Proof the lamp will remain switched on every night')]),
glosses=[('盏','measure for a lamp'),('奋','strive; become excited'),('唤','call'),('呼唤','call out to someone'),('折','fold; bend'),('挽留','ask someone to stay'),('台词','lines spoken in a play'),('半拍','half a beat'),('转折','turn; shift in a story'),('回应','respond'),('借','borrow'),('管理员','person responsible for managing a place'),('剧情','plot'),('重视','take seriously'),('孤独','loneliness'),('用途','purpose; use'),('表情','expression'),('番','measure for a stretch of speech or effort'),('挪','move aside'),('漏','miss; overlook'),('落空','come to nothing; not be realised'),('侧','side'),('截','cut out; section'),('抢','rush to take; compete for'),('舍不得','be reluctant to part'),('照顾','look after'),('嗓','throat; voice'),('缩','shorten; shrink'),('永远','forever'),('独','alone'),('片段','short section'),('拍','beat;拍照 take a photo'),('诗','poem')],
place='The group’s final old-hall rehearsal and performance',context='A fictional umbrella farewell scene is rehearsed. Final performance Sunday; Monday nine train to a neighbouring-city job. Pack at 9:30, venue closes ten, key goes to manager after packing. Future meetings are not scheduled.',
turns=[('她说别找我，是不想再联系了吗？','She said not to look for her; does she want no further contact?','Restore the rehearsal context',['那是台词，后面陈宇还要追出去送伞。']),('灯还亮，就答应下周一定回来吧？','The lamp is lit, so she promises to return next week?','Distinguish a lyric from a commitment',['不是，可以有盼望，没有具体回来的约定。']),('她把钥匙放包里，是要先走吗？','She put the key in her bag; is she leaving early?','Use the actual later explanation',['不是，她怕排练时丢，收完再交给管理员。']),('她喜欢听感谢，就要逐个讲很久吗？','If she likes hearing thanks, must she give every person a long speech?','Keep the stated format limit',['不用，她想坐在一起听，可以只说谢谢。'])],
usage=[('Check a quoted line','这是台词，还是她刚才对你说的？','Is that a script line or something she just said to you?','Recover the relevant setting before interpreting the words.'),('Allow mixed feelings','我想开始新生活，也舍不得这一晚。','I want to start a new life and am reluctant to leave this evening.','Both feelings can be present.'),('Keep hope without a date','我也盼望再见，哪天还没定。','I look forward to meeting again too; no date is set.','Do not convert hope into an agreed schedule.')],
tasks=practice(
[(R[0][0],R[0][1],'The first farewell line is spoken in rehearsal.',True,'The following direction and pages establish the setting.'),(R[4][0],R[4][1],'Interest in contact guarantees fixed return dates.',False,'No fixed return schedule is promised.'),(P[5][0],P[5][1],'All future materials are taken away.',False,'Selected programmes are kept; new pages stay.'),(P[8][0],P[8][1],'Sharing the table lets participation and help coexist.',True,'They divide the concrete action instead of forcing passivity.')],
[('她想听大家感谢，但不想每次回长篇。应该取消全部感谢吗？','She wants thanks but not lengthy responses each time. Cancel all thanks?',['不用，可以改成自愿说，她简短回应。','必须，她没有答应长篇就是讨厌所有感谢。','不用改，让她一直上台回答就好。'],0,'The request changes format, not all appreciation.'),('她说不再每周来，也想听新节目。能写以后不联系吗？','She will no longer come weekly and wants future recordings. Can we say no future contact?',['不能，少到场不等于关闭联系。','能，不每周来就是从不再联系。','能，她要的新节目其实不存在。'],0,'Her explicit request preserves contact.'),('钥匙在包里，后面说收完交管理员。她要带去邻城吗？','The key is in the bag; she says she will return it after packing. Is it going to the next city?',['不是，是暂时收好。','是，放包里就不能再交出来。','是，管理员要到邻城收。'],0,'The full explanation specifies temporary storage.'),('星期一九点车票确定，下次见面没定。哪一个可以写成确定？','Monday’s nine train is settled; the next meeting is not. Which is fixed?',['周一九点的车。','下周一定回来。','以后每周都在旧小厅见。'],0,'Retain the given certainty distinction.')],
[('掌声过后，灯又亮了一点。','After the applause the lights brightened a little.','过后'),('她时而看稿子，时而望向门口。','She alternates between the pages and the doorway.','时而'),('为了让台词接上而停半拍。','Pause half a beat to let the next line connect.','而'),('一番讨论以后，我们决定把最后的歌留短。','After discussion we decided to keep the last song short.','一番')],
[[(V[i][3],V[i][4]) for i in [0,1,2]],[(V[i][5],V[i][6]) for i in [4,5,8]],[(V[i][3],V[i][4]) for i in [10,11,12]],[(V[i][5],V[i][6]) for i in [15,16,17]],[(V[i][3],V[i][4]) for i in [23,29,30]]]),
review='Native review: final-rehearsal banter, X是X concession, original lyric rhythm, 早不晚不 and 放着X不Y register force. Self-review distinguishes quoted script from real contact, keeps Sunday performance and Monday-nine departure separate, returns key only after 9:30 packing before ten. A lyric image does not guarantee a return date; interest, regret and a wish for quiet coexist. No character discusses legal identity or safety disclaimers. Selected 32 introductions do not imply full advanced coverage.')
write(6,4,spec,publish='--publish' in sys.argv)
