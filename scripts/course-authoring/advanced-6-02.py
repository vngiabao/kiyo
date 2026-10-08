"""An indirect request becomes a specific, limited agreement."""
import sys
from advanced_core import write,rows,words,q,card,practice
V=words('''
意愿|willingness; wish|ý muốn|愿意来听，不等于有意愿负责整个活动。|Wanting to listen doesn’t mean wanting to run the whole event.|先问她的意愿，再安排她的工作。|Ask what she wants before assigning her work.
能否|whether someone can|có thể hay không|请问能否在周五下午送到？|Could you deliver it Friday afternoon?|他还没答复能否参加。|He hasn’t said whether he can attend.
协助|assist|hỗ trợ|我能协助开头的介绍，不能负责全场。|I can assist with the opening introduction, not the entire event.|她协助同事整理资料。|She helps a colleague organise materials.
协商|discuss to reach an agreement|thương lượng|时间不合适，我们再协商。|If the time doesn’t work, we can discuss it again.|双方协商以后改了日期。|After discussion the two sides changed the date.
协调|coordinate|điều phối|谁来协调借东西和归还东西的时间？|Who will coordinate borrowing and returning the items?|她在协调两个小组的安排。|She is coordinating the two groups’ arrangements.
分工|divide responsibilities|phân công|把分工写清，别都叫帮一下。|Write out the division of work instead of calling everything a little help.|我们先分工，再一起准备。|We divide responsibilities before preparing together.
职责|responsibilities of a role|trách nhiệm|保管设备不在我这次的职责里。|Looking after the equipment isn’t my responsibility this time.|检查门有没有锁好是他的职责。|Checking whether the door is locked is his responsibility.
物品|items; belongings|đồ vật|借来的物品不能直接留给下一组。|Borrowed items can’t simply be left to the next group.|她把个人物品放进柜子。|She puts her belongings in the cabinet.
专用|for a specific use|chuyên dụng|这条线是音箱专用的，不能换成手机的。|This cable is specifically for the speaker, not interchangeable with the phone cable.|这里有一张工作人员专用的桌子。|There is a table reserved for staff here.
指定|designate; specify|chỉ định|通知指定的是小厅，不是大礼堂。|The notice specifies the small hall, not the main auditorium.|请送到指定的地点。|Please deliver it to the designated place.
允许|permit|cho phép|主人允许带走，不代表允许转借。|The owner permits taking it away, not necessarily lending it on.|这里不允许吸烟。|Smoking isn’t allowed here.
到期|reach the end of an agreed period|đến hạn|借用时间周六五点到期。|The borrowing period ends Saturday at five.|这张卡月底到期。|This card expires at the end of the month.
变更|change an arrangement formally|thay đổi|要变更归还时间，先问物品的主人。|To change the return time, ask the owner first.|报名信息有变更，请及时通知。|Please promptly report changes to registration information.
提交|submit|nộp|周五中午以前提交最终的分工。|Submit the final division of work before noon Friday.|她提交了新的申请。|She submitted a new application.
此次|this occasion|lần này|此次我只负责开头十五分钟。|This time I am only responsible for the first fifteen minutes.|此次演出换了一个场地。|This performance uses a different venue.
有关|related; concerning|liên quan|有关音箱的问题，请直接联系陈宇。|For questions about the speaker, contact Chen Yu directly.|她想了解有关课程的安排。|She wants to learn about arrangements for the course.
音量|sound volume|âm lượng|先试音量，别一开就太大声。|Test the volume first instead of starting too loud.|请把音量调小一点。|Please turn the volume down a little.
通话|have a phone conversation|cuộc gọi|我们通话时，把几点到和几点走都说了。|In the call we stated both arrival and departure times.|她正在通话，稍后回复消息。|She is on a call and will reply later.
名额|available places; quota|suất|二十个名额已经满了，先别加人。|The twenty places are filled; don’t add people yet.|这次课程还有三个名额。|There are three places left on this course.
场地|venue; space used for an activity|địa điểm|场地五点关闭，所以四点半开始收。|The venue closes at five, so we begin packing at 4:30.|雨太大，户外场地不能用了。|The rain is too heavy to use the outdoor venue.
免得|so as to avoid|để khỏi|先把时间写下来，免得又记成一整天。|Write down the times so it isn’t remembered as a whole day again.|带一件外衣，免得晚上冷。|Bring a jacket so you aren’t cold tonight.
只顾|focus only on, overlooking something else|chỉ lo|我只顾问谁能来，忘了问能待多久。|I only asked who could come and forgot to ask how long.|他只顾看手机，没看见门口的人。|He was absorbed in his phone and missed the person at the door.
只管|go ahead and do, without worrying|cứ việc|不懂的地方只管问，不用装懂。|Go ahead and ask about anything you don’t understand.|你只管先吃，不用等我。|Go ahead and eat; you needn’t wait for me.
只得|have no alternative but to|đành phải|五点必须还回去，我们只得提前收好。|We must return it at five, so we have to pack up ahead.|末班车走了，他只得步行回去。|The last bus had gone, so he had to walk home.
再说|leave until later; besides|để sau; hơn nữa|借不借等问过主人再说。|We’ll decide about borrowing after asking the owner.|我今晚不去，再说已经很晚了。|I’m not going tonight; besides, it’s already late.
算了|let it go; never mind|thôi vậy|她这周不方便，那就算了，别再追问。|She can’t this week, so let it go instead of asking repeatedly.|找不到那张纸就算了，用新的吧。|If we can’t find that sheet, never mind; use a new one.
不便|not convenient; unavailable|bất tiện|周六下午不便到场，我可以周五先介绍。|I can’t attend Saturday afternoon, but can make an introduction Friday.|现在不便通话，晚点联系。|A call isn’t convenient now; contact me later.
若|if, in a formal or written condition|nếu|若时间有变，请提前通知。|If the time changes, please notify us ahead.|若无法到场，可以在线参加。|If unable to attend, you may join online.
凡是|all those that; whenever|hễ; tất cả|凡是借来的物品，都要按约定归还。|All borrowed items must be returned as agreed.|凡是报名的人，都能收到通知。|Everyone who registers receives a notice.
罢了|merely; that is all|mà thôi|我只说可以介绍一下罢了，没有答应全程负责。|I only offered an introduction; I didn’t agree to manage everything.|这只是一次尝试罢了。|This is merely one trial.
本身|itself|bản thân|问题本身不难，难的是大家想的范围不同。|The issue itself isn’t hard; the assumed scope differs.|这句话本身没有写结束时间。|The sentence itself gives no finishing time.
听取|hear and consider someone’s views|lắng nghe|先听取她的安排，再决定怎么分工。|Hear her availability before deciding responsibilities.|他们听取了参加者的意见。|They heard participants’ views.
''')
D=rows('''
你周六下午是不是正好没事？|Are you free Saturday afternoon, by any chance?
不太行，三点得走。怎么了？|Not really; I have to leave at three. What’s up?
我们有个小活动，缺一个人帮忙。|We have a small event and need another helper.
帮哪一段？是开头介绍，还是一直留着？|Which part? The introduction, or staying the whole time?
原来想请你从两点待到五点。|We originally hoped you’d stay from two to five.
那不行。我能两点来，介绍十五分钟，三点以前走。|I can’t do that. I can come at two, introduce things for fifteen minutes and leave before three.
你先来，后面到时再说？|Could you come first and we’ll work out the rest then?
后面不能再说，我三点真的要走。|We can’t leave the rest open; I really have to leave at three.
明白，那我找别人接后面。|Understood. I’ll find someone for the rest.
你是想借音箱，还是要我一起负责声音？|Do you want the speaker, or for me to manage the sound too?
想借音箱。你能顺便带来吗？|The speaker. Could you bring it along?
那是我室友的，我只能帮你问。|It’s my flatmate’s; I can only ask for you.
我以为是你的。那先别写成已经借到了。|I thought it was yours. Then let’s not mark it as borrowed yet.
对，借不借、几点还回去，都要问清。|Right. We need permission and a return time.
要是他允许，我负责取和送回去，不麻烦你来回跑。|If he agrees, I’ll collect and return it, so you don’t have to travel back and forth.
好，你直接跟他联系，我先问他愿不愿意。|Okay. Contact him directly; I’ll first ask if he is willing.
你这么问，是不是其实不太想来？|Does all this mean you don’t really want to come?
不是不想，是我不能答应整个下午。|It isn’t that I don’t want to; I can’t commit to the whole afternoon.
那我们写两点介绍到两点十五，不把你排到五点。|Then we’ll write two to 2:15 for the introduction, not schedule you until five.
这样可以。三点要走也写一下，免得临时又叫我。|That works. Write that I must leave at three too, so I’m not called on later.
音箱有消息我再通知你，没借到就用小厅原来的。|I’ll tell you about the speaker; otherwise we’ll use the one already in the small hall.
先试过那个能不能用，别等开场才发现。|Test whether it works before the event starts.
好，周五一起试。你只管来听，不用留下收东西。|Okay, we’ll test it Friday. Come and listen; you needn’t stay to pack up.
这句我听明白了。不过我听完也得走，别又给我加一段。|I understand that. But I leave after listening too—don’t add another job.
''')
M=rows('''
你先把名字写上吧。|Put your name down first.
写哪一栏？参加，还是负责？|Which column? Attending or responsible?
都差不多，都是来嘛。|Nearly the same—you’re coming either way.
差得可不少。参加能听，负责还得收。|Quite a difference. Attending means listening; being responsible includes packing up.
那你想写哪一栏？|Then which do you want?
参加。不过这周我连参加都没答应。|Attending. But I haven’t even agreed to that this week.
我以为你刚才说看看，就是能来。|I thought “I’ll see” meant you could come.
看看是还没确定，不是偷偷答应。|“I’ll see” means uncertain, not secretly agreeing.
行，我先不写。确定了你告诉我。|Okay, I won’t enter it yet. Tell me once you know.
这就对了。笔先放下，比替我决定容易。|Exactly. Putting the pen down is easier than deciding for me.
那我给你留个位置？|Then shall I keep a place for you?
也先不用。有空我再问还有没有名额。|Not yet. If I’m free I’ll ask whether there’s space.
''')
R=rows('''
林安问我周六下午有没有事，我听见的不是一个完整邀请，而是邀请的开头。我说三点必须走，接着问有什么安排。她说社区的小活动缺人帮忙。我愿意了解，却没有因此把整个下午交给她。以前遇到这种问法，我常常先答应来，到了才知道帮忙还包括接人、试音箱和最后收东西。这次我想先听清需要哪一段，再判断自己能不能做。|Lin An’s availability question began an invitation, not a complete proposal. I said I had to leave at three and asked about the plan. I was interested, but had not offered the entire afternoon. Previous vague requests had grown into greeting guests, testing equipment and packing up, so I wanted the scope first.
她原来希望我两点到五点都留着。我两点能到，也熟悉开头要介绍的几本书，所以提出介绍十五分钟，结束以后留一会儿听，但三点以前走。这不是把三小时缩成一句有空，而是把到场、负责和离开分开。她说先来，后面到时再说，我又重复三点要走。不是故意把话说硬，只是那个时间已经约了别的事情，到了也不会自动消失。|She wanted me from two to five. I offered a fifteen-minute opening and a little listening time, leaving before three. Arrival, responsibility and departure were separate. When she suggested deciding later, I repeated the limit: my other appointment would not disappear on arrival.
林安听完说找别人接后面，这时我才觉得我们真的约到了同一件事。我没有要求她证明一个人也能办好，也没有因为她需要帮助就改变三点的安排。她需要全程有人，和我只能来一段，都可以是真的。若最后找不到后面的人，她要重新决定活动怎么办，不能把未解决的部分默默放进我已经答应的十五分钟。|Her offer to find someone for the rest established shared scope. Her need for full coverage and my limited availability could both be real. If no one else was found, she would need another plan rather than silently add unsolved duties to my fifteen minutes.
音箱是另一件事。林安看见我以前带过，就以为是我的。我说那是室友的，只能先问他，不等于现在就能答应借。她赶忙把安排里的已经借到删掉，改成等待回复。我觉得这个改动很重要：一件物品曾经跟着谁出现，不说明那个人有权决定下一次怎么用；愿意代问也没有自动变成替主人保证。|She assumed a previously seen speaker was mine. It belonged to my flatmate, so I could ask but not consent. She changed “borrowed” to “awaiting reply.” Having carried an item did not establish ownership or authority to promise it.
室友说可以借，条件是周六五点以前送回家，线也要一起带回来。他下午要用，不能放在小厅等周日再收。林安听取这个条件，决定自己周五取、周六四点半开始收，活动结束前把归还安排给陈宇。她也向室友确认，陈宇替她送回来可以。负责归还的人变了，主人同意才算安排好，不是写上另一个名字就自动变更。|The owner allowed borrowing with the cable returned home before five Saturday. Lin An planned Friday collection and packing at 4:30, and obtained consent for Chen Yu to return it. A new name on the plan alone did not change the owner’s agreement.
周五试声音时，我们先看小厅自己的音箱。它能放介绍的声音，音量也够，所以借来的那台只是备用选择，不是活动能不能开始的唯一条件。活动有二十个名额，小厅五点关闭。林安把时间重新写成两点开始、四点半收，五点以前离开。借到东西和场地可以无限使用，是两件不同的事；试得好听，也不能把结束时间往后推。|Friday testing established that the venue’s own speaker worked. The borrowed one was optional backup. The event had twenty places, began at two, packed at 4:30 and left before the venue’s five closing. Equipment availability did not extend venue hours.
她把最终分工发给我：我两点到两点十五介绍，陈宇之后负责声音和收东西，林安联系参加者。有关借来音箱的取还，由她和室友直接联系。我读完才回复确认，不把整张表都当成自己的职责。表里也写了三点以前离开，所以我不需要活动当天不断解释，也不用把每一次有人问我事情都听成不能走。|The final plan assigned my opening, Chen Yu’s later sound and packing, and Lin An’s participant contact and equipment arrangements. I confirmed my part, not every task, with my departure limit recorded.
周六有位参加者问我能不能最后再介绍一本书。我说今天三点要走，后面可以问林安。对方说可惜，我也觉得可惜，但这句话没有让我欠下最后一段。我已经完成十五分钟，就可以按约定离开；如果我自己决定临时多留，那是新的选择，也要看后面的安排，不能把可惜当作已经答应。|A participant asked for another book introduction at the end. I referred them to Lin An and retained my departure. Shared disappointment was not a new commitment. Staying longer would require a new choice and availability.
走到门口时，林安说谢谢我先把范围讲清，不然她还会把帮一下想成帮完整场。我说也谢谢她听完以后真的改了分工，没有一边说知道一边把我的名字放到五点。这次活动没有因为每个人都无条件答应而顺利，而是大家知道谁来、做什么、做到几点，以及哪里还没有人答应。没确定的部分写成没确定，比把它们藏在客气话里更容易处理。|At departure we appreciated a clear scope and a plan that actually reflected it. The event benefited from knowing who had agreed to what and until when, with unresolved parts labelled unresolved rather than hidden in politeness.
回家以后，室友收到音箱，确认线也在。我没有参加归还，却收到一句已经还好，因为开头是我介绍双方认识。我看完很放心，没有觉得消息发给我就使我负责了整个下午。介绍联系、负责运送、允许借出和检查归还，分别属于不同的人；把这些事说清，人情反而不用靠一个人一直不好意思离开来维持。|The owner received the speaker and cable and sent me confirmation because I had introduced them. Receiving that update did not make me responsible for transport. Clear roles supported goodwill without relying on someone feeling unable to leave.
''')
P=rows('''
我准备社区的小活动时，先列了需要的东西，却没列每件事需要多少时间。陈宇能帮忙放声音，我还想找一个熟悉书的人介绍。看到林安的朋友周六可能有空，我就问下午有没有事。我希望得到一个简单的可以，却忘了对方需要知道的不是我的希望，而是活动从几点到几点、我要请他做什么、有没有别的人接后面。|I listed equipment before the time each task required. I needed someone knowledgeable about books alongside Chen Yu’s sound support. My availability question sought a simple yes without supplying the scope needed to decide.
他先说三点要走，我只顾想到两点能来，差点把三点当作到时可以商量的小事。等他说只能介绍十五分钟，我仍想先让他来，后面再说。他重复不能再说，我有一点失望，也有点担心后面没人。但他没有拒绝我这个人，只是拒绝从两点一直待到五点。我把这两件事分开，才没有继续用你是不是不想来追问他的意愿。|I focused on his two arrival and almost dismissed his three departure. His repeated limit disappointed and worried me, but refusing the whole afternoon was not rejecting me personally. That distinction stopped further pressure about willingness.
我们一同看了分工，我问十五分钟里面能介绍多少。他说两本书，每本讲一个最想让大家注意的地方，最后留五分钟提问。我本来想放五本，这样就得换人或减少每本的内容，不能只把五本加到他十五分钟里。他建议先用两本，把其他三本放在桌上让大家自己翻，我采纳了这个办法，活动的开头也因此更清楚。|Together we planned two books and five minutes of questions within fifteen minutes. My original five books would require another arrangement. We adopted two introductions and placed the remaining books out for browsing rather than silently enlarge his task.
借音箱时我又犯了类似的错。我见过他带，就在纸上写已借到。他说是室友的，得先问。我赶忙改了，觉得有点不好意思。他没有笑我，只说还好现在问了。愿意帮忙问、对方允许借、谁来取和几点还回去，是四个不同问题。如果只写一个音箱有了，后面每个人都可能以为这些问题已经由别人解决。|I similarly wrote “speaker secured” before discovering it belonged to his flatmate. We separated asking, consent, collection and return instead of letting “got a speaker” conceal unanswered questions.
室友同意借到周六五点，并要求线一起还回去。我原来活动结束才收，这样再走回去肯定来不及。我把收东西提前到四点半，安排陈宇送回去，问室友可不可以由他送。对方答应以后，我把地址和联系办法直接发给陈宇，没有请那位介绍书的朋友继续转消息。既然已经分工，就要让真正做事的人拿到需要的信息。|The five return deadline required packing at 4:30. I secured permission for Chen Yu to return it and sent him details directly rather than retain the introducer as a message relay.
我们还准备了一份短通知，写活动两点开始，小厅五点关闭，二十个名额满了以后不再继续报名。若时间有变，会提前联系已经报名的人。凡是借来的物品，都要按双方同意的时间归还。这几句适合写在安排里，朋友见面聊天时我没有照着念整份通知，只把谁带东西和几点走再确认了一次。写下来的条件可以清楚，口头的话也可以自然。|The notice specified start, closing, capacity, changes and returns. Those formal conditions suited writing; in conversation we confirmed essentials rather than recite the notice.
周六开头的介绍结束得正好，两本书没有讲成一场长课。有人说还想听第三本，我也想多听，但是想到他后面有安排，就说第三本可以自己翻，有问题先问我。我不是为了替他表现得特别冷淡，而是已经知道他答应的范围。如果一有新要求就回头找他，分工表写得再清楚也没有实际作用。|The two-book introduction finished on time. A request for a third went to browsing and me, rather than extending his role. Clear written limits mattered only if acted on.
三点以前他准备离开，有人问收东西时找谁。我说找陈宇，没说你再等等。他向我道别时仍然很友好，我才发现把结束时间说清，并没有让参加的人都变得疏远。相反，我知道不能一直依赖他，就早点准备后面的安排；他知道能按时走，就能安心把答应的开头做完。彼此都少了一点猜来猜去的压力。|He left before three; packing enquiries went to Chen Yu. Clear departure did not damage friendliness. Knowing the limit let me prepare and him complete the opening without ongoing uncertainty.
四点半我们开始收，原来的音箱留在小厅，借来的和专用线送回主人家。五点以前收到确认，整个安排才真的结束。我把每个人帮了哪一段写进感谢的消息，没有把每个人都说成从头忙到尾。感谢不需要把事实说大；把有限的一段也认真看见，比夸成所有人都做了全部更像真的感谢。|We packed at 4:30 and confirmed the borrowed speaker and cable were returned before five. Thanks named each actual contribution rather than exaggerate everyone’s help into working all day.
下一次再问朋友有空吗，我想先补一句事情的范围。可以客气地开头，也要允许对方问具体内容。如果对方说不便，我可以失望，可以另找办法，却不用把多问一遍、留个位置、先写名字当作让拒绝消失的办法。帮忙本身可以有限，关系也可以继续；我们不是靠谁一直不敢说不能来，才算是朋友。|Next time I will state scope early and welcome questions. Unavailability can prompt disappointment and another plan, not repeated questioning or pre-entering a name to erase refusal. Limited help and continued friendship can coexist.
''')
G=[
card('若…，请/可以…','Recognise a written condition','若 is more formal than 如果 in ordinary conversation. It introduces a condition, not proof that a change has occurred.','若时间有变，请提前通知。|If the time changes, please notify us ahead.\n若无法到场，可以在线参加。|If unable to attend, you may join online.','若时间有变，所以时间一定已经变了。','若时间有变，请提前通知。','A condition does not announce an actual change.'),
card('凡是…，都…','Apply a rule to every member of a stated group','The scope after 凡是 matters. All borrowed items does not include every item in the venue.','凡是借来的物品，都要按约定归还。|All borrowed items must be returned as agreed.\n凡是报名的人，都能收到通知。|Everyone who registers receives a notice.','凡是借来的物品都要还，所以小厅自己的桌子也要送到别人家。','凡是借来的物品，都要按约定归还。','The rule applies to the stated borrowed group.'),
card('至于…','Change to a connected topic','至于 introduces another aspect rather than assigning it to the preceding person. It often separates responsibilities or qualifications.','至于音箱，你直接跟主人联系。|As for the speaker, contact the owner directly.\n至于最后谁收，我们还没有确定。|As for who packs up, we haven’t decided.','至于最后谁收，我们还没有确定，所以已经确定由我收。','至于最后谁收，我们还没有确定。','A topic marker does not turn an unresolved role into a promise.'),
card('要么…，要么…','Offer stated alternatives','The speaker presents alternatives for this decision; other possibilities may exist outside that proposal.','要么减少书的数量，要么另找人接后面。|Either reduce the number of books or find someone for the rest.\n要么周五试，要么周六提前试。|Either test Friday or early Saturday.','要么周五试，要么周六提前试，意思是两个时间都必须试。','要么周五试，要么周六提前试。','Alternatives do not require doing both.'),
card('再说','Distinguish postponement from an added reason','等…再说 defers a decision. At the start of a following reason, 再说 means besides. Neither use secretly confirms attendance.','借不借等问过主人再说。|We’ll decide about borrowing after asking the owner.\n我今晚不去，再说已经很晚了。|I’m not going tonight; besides, it’s already late.','等问过主人再说，意思是主人已经同意了。','借不借等问过主人再说。','Deferring a decision leaves it open.'),
card('只是…罢了','Limit the scope of a claim','罢了 presents something as only or merely. It can sound corrective or dismissive; do not use it to minimise someone else’s effort.','我只是说可以介绍一下罢了。|I only said I could make an introduction.\n这只是一次尝试罢了，后面还要看看。|This is only one trial; we still need to see how it goes.','我只是说可以介绍一下罢了，所以已经答应全场负责。','我只是说可以介绍一下罢了。','The limitation excludes an automatic whole-event commitment.'),
]
spec=dict(title=('What does a little help include?','帮一下，是哪一段？'),goals=['Clarify an indirect request before agreeing','Separate assistance, permission and responsibility','Keep a refusal or limited offer intact across several turns'],vocabulary=V,grammar=G,
dialogue=(D,[q('gist','What agreement do the speakers reach?','An opening introduction with a stated departure limit','Full responsibility until five','Borrowing equipment without its owner’s reply'),q('detail','What can the speaker promise about the borrowed speaker at first?','Only to ask the owner','That it is already borrowed','That it may be lent onward'),q('inference','Why repeat the three departure?','To keep later duties from being silently added','To cancel the opening introduction','To make the equipment owner leave at three')]),
reading=(R,[q('gist','What makes the limited assistance workable?','Specific scope, responsibilities and times','Everyone agreeing to every task','Leaving all later duties undecided'),q('detail','By when must the borrowed speaker be home?','Before five Saturday','Sunday after packing','Three Saturday'),q('inference','Does receiving the return update make the introducer responsible for transport?','No, an update does not change the assigned role','Yes, any message assigns the whole task','Yes, introducing people makes every later job theirs')]),
pairedTitle='The organiser revises the plan',pairedReading=(P,[q('gist','How does the organiser change?','They act on limits rather than merely acknowledge them','They keep everyone’s name until five anyway','They avoid telling people the actual work'),q('detail','What happens to the other three books?','They are placed out for people to browse','All five are squeezed into the fifteen minutes','They are removed from the venue permanently'),q('inference','Why name actual contributions in thanks?','To recognise limited help accurately','To imply everyone worked the whole day','To erase the need for a return confirmation')]),
mediaTitle='Which column?',media=(M,[q('detail','Has the speaker agreed to attend this week?','No, they are still undecided','Yes, saying看看 confirms it','Yes, the organiser may decide'),q('inference','What does putting the pen down accomplish?','It avoids recording an agreement that does not exist','It cancels the event','It guarantees a spare place')]),
glosses=[('硬','firm; hard'),('欠','owe'),('偷','do secretly; steal'),('锁','lock'),('罢了','merely; that is all'),('转借','lend onward'),('备用','backup'),('职责','role responsibilities'),('接人','meet or collect someone'),('到场','arrive; be present'),('疏远','become distant'),('猜','guess'),('压力','pressure'),('范围','scope'),('归还','return something'),('开场','start of a performance or event'),('音箱','loudspeaker'),('专用','for a specified use'),('表','table; form'),('栏目','column; section'),('保管','look after; keep safely'),('缩','reduce; shrink'),('权','right; authority'),('有限','limited'),('藏','hide'),('分工','division of responsibilities'),('数量','quantity')],
place='Planning a small community book event',context='Opening at two for fifteen minutes; departure before three. Venue closes at five; packing begins at 4:30. Borrowed speaker and cable must be returned home before five with the owner’s permission.',
turns=[('你先来，后面再说？','Come first and decide the rest later?','Keep a stated time limit',['我可以介绍十五分钟，但三点以前必须走。']),('那音箱就算借到了？','So the speaker is secured?','Separate asking from permission',['还没有，我只能先问主人。']),('你说看看，我先写你的名字？','You said you would see; shall I enter your name?','Keep uncertainty explicit',['先别写，我还没确定能不能来。']),('你介绍完再留下收东西吧？','Stay to pack after your introduction?','Refer to the agreed division of work',['我三点要走，收东西请找陈宇。'])],
usage=[('Ask about the scope','帮哪一段？大概需要多久？','Which part? Roughly how long?','Questions clarify the request rather than signal acceptance.'),('Decline the larger request','我能介绍十五分钟，不能一直待到五点。','I can introduce things for fifteen minutes, but can’t stay until five.','A limited offer leaves the larger request declined.'),('Leave a decision open','我先问问，有回复再告诉你。','I’ll ask first and tell you once there is a reply.','Passing on a question is not giving permission.')],
tasks=practice(
[(R[0][0],R[0][1],'The speaker has already offered the entire afternoon.',False,'Interest precedes agreement on scope.'),(R[4][0],R[4][1],'Changing the return person requires the owner’s agreement.',True,'The owner is asked to accept Chen Yu’s return.'),(P[2][0],P[2][1],'The organiser adds all five books to the fifteen minutes.',False,'Two are introduced and three left for browsing.'),(P[8][0],P[8][1],'Thanks names the parts each person actually did.',True,'It does not exaggerate every helper into working all day.')],
[('我能两点来，三点以前走。可以让我负责到五点吗？','I can arrive at two and leave before three. Can I be responsible until five?',['不能，需要找人接后面。','可以，来了就自动负责到五点。','可以，只要不写结束时间。'],0,'A later duty conflicts with the stated limit.'),('我只是帮你问主人，能写成已借到吗？','I am only asking the owner. Can we mark the item as secured?',['不能，还要等主人回复。','能，问了就等于同意。','能，见过东西就有权借出。'],0,'An enquiry is not consent.'),('我说看看，还没确定。你先写名字好吗？','I said I would see and am undecided. Enter my name now?',['先别写，确定以后再写。','写吧，没确定就是答应。','写成全程负责，免得再问。'],0,'The given premise explicitly leaves attendance open.'),('借来的要五点以前还回去，小厅自己的也要送到别人家吗？','Borrowed items must be returned before five. Must the venue’s own ones be delivered to someone else too?',['不用，这条约定只说借来的。','要，所有东西都属于借来的。','要，小厅自己的也归借出人。'],0,'Keep the stated rule’s scope.')],
[('先把时间写下来，免得又记成一整天。','Write down the times so it isn’t remembered as a whole day again.','免得'),('凡是借来的物品，都要按约定归还。','All borrowed items must be returned as agreed.','都'),('这只是一次尝试罢了。','This is merely one trial.','罢了'),('借不借等问过主人再说。','We will decide about borrowing after asking the owner.','再说')],
[[(V[i][3],V[i][4]) for i in [0,2,5]],[(V[i][5],V[i][6]) for i in [8,10,11]],[(V[i][3],V[i][4]) for i in [13,16,18]],[(V[i][5],V[i][6]) for i in [20,21,22]],[(V[i][3],V[i][4]) for i in [26,28,30]]]),
review='Native review: indirect availability requests, firmness of repeating a departure, corrective 罢了 and pen joke. Self-review separates attendance, fifteen-minute introduction, equipment ownership, consent, transport and return. Saturday five deadline requires 4:30 packing; no indefinite or onward lending is implied. The two readings show request recipient and organiser independently. No polite hesitation is scored as acceptance; limited offers remain limited. Source inventory labels are not a claim of complete level coverage.')
spec['glosses'].append(('稍后','a little later'))
write(6,2,spec,publish='--publish' in sys.argv)
