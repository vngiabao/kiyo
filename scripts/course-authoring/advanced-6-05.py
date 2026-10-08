"""An original lyric changes address across verses; singing practice keeps the words intact."""
import sys
import common
from advanced_core import write,rows,words,q,card,practice
common.dictionary.update({'乐曲':'yuè qǔ'})
V=words('''
歌词|words of a song|lời bài hát|歌词没有变，第二遍唱时我想到的人变了。|The lyrics stayed the same; on the second singing I imagined a different person.|她把歌词写在纸上。|She wrote the lyrics on paper.
古典|classical|cổ điển|这段配乐有古典的感觉，不等于歌词是古人写的。|The accompaniment feels classical, not proof the words are ancient.|她常听古典音乐。|She often listens to classical music.
民歌|folk song|dân ca|我们听过民歌的唱法，再试自己的新歌。|We listened to a folk-song style before trying our new song.|奶奶教我一首家乡的民歌。|Grandmother taught me a folk song from home.
戏曲|traditional Chinese opera|hí khúc|戏曲里的长音给了我们一个想法，不是照搬整段。|A held note in Chinese opera gave us an idea; we didn’t copy a whole section.|她带朋友去听戏曲。|She took a friend to listen to Chinese opera.
乐曲|musical composition; piece|bản nhạc|这首乐曲没有歌词，可以只听节奏。|This piece has no lyrics, so we can attend to its rhythm.|他演奏了一首短乐曲。|He played a short musical piece.
节奏|rhythm; pace|nhịp điệu|先跟上节奏，不要把没听清的字跳过去。|Follow the rhythm without skipping words you haven’t caught.|他说话的节奏很快。|He speaks at a fast pace.
演奏|perform instrumental music|biểu diễn nhạc|她演奏时，我先小声读歌词。|While she plays I first read the words quietly.|他在小厅演奏钢琴。|He plays the piano in the small hall.
歌唱|sing; singing|ca hát|歌唱把一个音拉长，字本身还是那个字。|Singing stretches a sound, but the word remains that word.|她喜欢歌唱，也喜欢听别人唱。|She enjoys singing and listening to others.
屏幕|screen|màn hình|屏幕上一行消失了，我还没唱到最后。|The screen line vanished before I sang its end.|她把屏幕调暗一点。|She dimmed the screen a little.
音量|volume of sound|âm lượng|音量小一点，才能听见自己在哪个字停。|A lower volume lets me hear which word I pause on.|这段录音的音量比前面小。|This recording is quieter than the previous one.
音像|audio and video material|tư liệu nghe nhìn|课程的音像资料按单元放在一起。|The course’s audio-video materials are grouped by unit.|他负责整理音像资料。|He is responsible for organising audio-video materials.
多媒体|multimedia|đa phương tiện|多媒体课件同时有画面、文字和声音。|The multimedia lesson contains images, text and sound.|这间教室有多媒体设备。|This classroom has multimedia equipment.
黑夜|dark night|đêm tối|黑夜里的灯可以像等候，也可以像一个方向。|A lamp in the night can suggest waiting or a direction.|黑夜过去，窗外慢慢亮了。|After the night the outside gradually brightened.
海浪|sea wave|sóng biển|海浪没有替人物回答，歌里仍留着空白。|The sea waves don’t answer for the character; the song leaves an opening.|她听见海浪拍到岸边。|She heard waves reach the shore.
海洋|ocean|đại dương|歌里的海洋很宽，房间里的声音却很近。|The song’s ocean is broad, but the room’s voice is close.|这本书介绍海洋里的动物。|This book introduces ocean animals.
波浪|wave; waves|làn sóng|波浪是一幅流动的画面，不是一个人的姓名。|Waves form a moving image, not a person’s name.|湖面的波浪比海边小。|The lake’s waves are smaller than those by the sea.
渡|cross a stretch of water|qua sông, nước|人物说想渡过河，还没说已经到了对岸。|The character wants to cross the river, not says they already reached the far bank.|他们乘船渡河。|They crossed the river by boat.
船只|boats; vessels|tàu thuyền|船只离开岸边，我想的是距离在变化。|As vessels leave the bank, I think of changing distance.|大风时船只没有出发。|The vessels did not depart in strong winds.
远方|a distant place|phương xa|远方是一个方向，没有写具体城市。|The distant place is a direction without a named city.|她收到一封远方朋友的信。|She received a letter from a friend far away.
远离|become or stay far from|xa rời|远离旧房间，不一定远离所有朋友。|Leaving the old room needn’t mean leaving every friend behind.|他们远离城市，住在小村庄。|They live in a village far from the city.
远远|far, as an intensifier|rất xa; hơn hẳn|第二遍的速度远远超过我能读清的速度。|The second pass is far faster than I can read clearly.|他的安排远远比我想的细。|His plan is far more detailed than I imagined.
一代|a generation|một thế hệ|一代人熟悉的唱法，不一定下一代也常听。|A style familiar to one generation may not be common listening for the next.|这本书写了上一代人的生活。|This book describes the previous generation’s lives.
时节|season; particular time of year|mùa; thời điểm|这段写雨的时节，不一定是作者今天的天气。|This describes a rainy season, not necessarily the writer’s weather today.|到了这个时节，天黑得早。|At this time of year it gets dark early.
阴影|shadow|bóng tối|窗边的阴影在动，我把它听成没有说完的话。|The moving window shadow suggests unfinished words to me.|树的阴影落在墙上。|The tree’s shadow falls on the wall.
一时|for the moment; temporarily|nhất thời|我一时没跟上，停下来再读。|I momentarily lost pace and stopped to reread.|她一时想不起那个人的名字。|She couldn’t recall that person’s name for a moment.
仿佛|as if; seem|dường như|重复的那句仿佛换了一个说话的人。|The repeated line seems to have a different speaker.|屋里安静得仿佛没人。|The room is as quiet as if empty.
好似|seem like; resemble|giống như|那盏灯好似一个没回答的问题。|That lamp seems like an unanswered question.|河面好似一条发亮的带子。|The river looks like a shining ribbon.
幻想|imagine an unreal or hoped-for situation|tưởng tượng|我幻想过再次见面，歌里没有把它写成事实。|I imagined meeting again; the song doesn’t make it a fact.|她把小时候的幻想写进故事。|She put her childhood imaginings into the story.
孤独|lonely; loneliness|cô đơn|这一段唱得孤独，下一段又多了一点希望。|This verse sounds lonely; the next adds some hope.|他在人多的地方也会觉得孤独。|He can feel lonely even among people.
心灵|inner emotional life; mind or spirit|tâm hồn|这首歌让我想起心灵里还没有说出的感受。|This song recalls feelings within me that I haven’t yet expressed.|音乐让她的心灵慢慢平静。|Music gradually calms her inner world.
融合|blend; integrate|hòa quyện|新歌融合两种唱法，但词和旋律都是我们新写的。|The new song blends two styles, with newly written words and melody.|这个活动融合了阅读和演奏。|The event combines reading and instrumental performance.
元素|element; component|yếu tố|门、灯和风是反复出现的元素。|Door, lamp and wind are recurring elements.|这个设计只保留了三个主要元素。|The design keeps just three main elements.
''')
D=rows('''
你第二遍唱的时候，那个你是在叫谁？|Who are you addressing as “you” on the second pass?
一开始像门外的朋友，后面也像以前的我。|At first a friend outside; later it also feels like my earlier self.
因为镜子那句吗？|Because of the mirror line?
对，不过我没把朋友完全拿掉。两个想法可以一起留着。|Yes, but I didn’t entirely remove the friend. Both thoughts can remain.
我原来一直在等一个人回来。|I kept imagining waiting for someone’s return.
这样也能听。只是最后没有写他真的回来。|That works too. It just doesn’t say they actually return.
那灯关了是不是就没有希望了？|Then if the lamp switches off, is there no hope?
也可以是夜里要睡，明天还继续走啊。|It can mean sleeping at night and continuing tomorrow.
你这么一说，我唱法就变了。|That changes how I sing it.
先别急着加快，刚才留给我的留漏了。|Don’t speed up yet; you missed “leave” in “leave for me.”
我跟着节奏过去，没发现少一个字。|I followed the beat and didn’t notice the missing word.
我们先读一遍，再接上声音。|Read it once first, then join the sound.
要每个字都用说话时的声调唱吗？|Must every word be sung with its spoken tone?
旋律会变音高，学说话还是要另听说话的读法。|Melody changes pitch; to learn speech we still need its spoken reading separately.
那我先确认词没听错，不把高音当成四声？|So confirm the words, not call a high note fourth tone?
对。字确认以后，再唱这段旋律。|Right. Confirm the words, then sing the melody.
你把风留给我，这里停一下，好不好？|Could we pause after “you leave the wind for me”?
可以，留给我后面停，别把留和给分得太开。|Yes, after “for me”; don’t separate “leave” and “for” too much.
屏幕上的字怎么一下就过去了？|Why did the screen words pass so quickly?
这一遍快了。我们回到慢一点的版本。|That pass was fast. Let’s return to the slower version.
慢一点不会把感觉都唱没吧？|Won’t singing slower lose all the feeling?
不会自动没。先唱清，情绪可以再试，不用一口气都解决。|Not automatically. Get the words clear first, then try the feeling; not all at once.
那我第二遍唱给以前的我，你唱给门外的朋友？|Then I address my earlier self on the second pass, and you the friend outside?
好，唱完听听哪里不一样。别先说只有一种才对。|Okay. Hear how they differ afterwards, without declaring only one correct first.
''')
M=rows('''
你把风留给我，我把灯留给你。|You leave the wind for me; I leave the lamp for you.
门外的脚步，走向看不见的远方。|Footsteps outside lead towards a distant unseen place.
海浪一遍一遍，没替我们回答。|Sea waves repeat without answering for us.
我把没说完的话，放在窗下。|I leave the unfinished words beneath the window.
镜子里的我，比昨天安静。|The self in the mirror is quieter than yesterday.
旧衣还在椅边，新的路还没画完。|Old clothes remain by the chair; the new road isn’t fully drawn.
你把风留给我，我把灯留给你。|You leave the wind for me; I leave the lamp for you.
这一声你，也落在我自己心里。|This “you” also lands within me.
夜深了，灯可以关，话不必忘。|Late at night the lamp can switch off without forgetting the words.
明天的船只，不保证带谁归来。|Tomorrow’s vessels don’t guarantee whose return.
你把风留给我，我把灯留给你。|You leave the wind for me; I leave the lamp for you.
走到新的岸边，还愿听你讲。|At a new shore I still wish to hear you speak.
''')
R=rows('''
第一次听我们新写的短歌，我把开头的你听成门外离开的朋友。门外有脚步，远方看不见，窗下还有没说完的话，这些都让人想到一次告别。我唱你把风留给我，觉得自己留下的是房间，朋友留下的是风。可是歌里没有说明谁去了哪座城市，也没有写两个人什么时候再见。我可以带着自己的经历听，不需要先把所有空白填成确定的安排。|On first hearing our original short song I imagined a departing friend. Footsteps, unseen distance and unfinished words support farewell. I brought my own experience without inventing a named city or settled reunion.
第二段出现镜子里的我，旧衣在椅边，新的路还没画完。到了这里，重复的你又像是在向过去的自己说话。那个人没有真的从房门出去，变化也可以发生在同一个房间里：旧习惯还在，新选择已经开始。下一句说这一声你也落在我自己心里，没有把第一段的朋友完全删掉。我因此把第二遍唱得轻一点，不再只想追回一个远处的人。|The mirror, old clothes and unfinished new road make the repeated address feel inward too. Change can happen in the same room. The line about “you” landing within me adds rather than erases the first friend interpretation.
林安唱的时候仍然想到朋友，她说镜子像是离开以后看见自己的地方。我听完觉得有道理，不用把自己的解释变成考试里唯一的答案。我们各自指出支持想法的词，也承认没有写出的部分。说我这样听，跟说作者只能这样写，是不同的分量。两种理解能不能都留下，要看它们能不能跟后面的字一起读，不是只要感觉好就能随便添故事。|Lin An still heard the friend through the mirror. We compared textual support without turning one interpretation into the sole answer. Both need to fit the later words rather than justify any invented story by preference.
最后一段说灯可以关，话不必忘。我以前一听关灯就觉得希望结束，现在也能想到人要休息，明天还走。歌又写船只不保证带谁归来，直接留下等待没有确定结果这一层。这不是说一定不会见面，而是没有保证会见。唱到新的岸边，还愿听你讲，我感到的希望更像愿意继续，不像已经收到下一次回来的车票。|A switched-off lamp can mean rest rather than ended hope. Vessels offer no guaranteed return, which is not a guarantee of no return. The ending’s wish to hear someone again supports willingness without a booked meeting.
我们排练时把三个重复句放在不同位置，第一遍靠近门外脚步，第二遍靠近镜子，第三遍在新的岸边。同样的文字，因为前后内容不同，让我听到不同的方向。不是每次重复都等于完全一样的事情，也不是必须每次都换一个人。我唱完可以问，这一遍前面发生了什么、后面又留下什么，再决定自己的声音想把哪一层带出来。|The repeated line follows footsteps, mirror and new shore respectively. Surrounding verses shift emphasis without requiring a new referent on every repeat. I ask what precedes and follows each before choosing my delivery.
字本身也要先听清。有一遍我漏了留，只唱你把风给我，意思还像一句完整的话，所以当时没发现。林安提醒我，原稿写的是留给，不只是给；少一个字就把保留下来的意味减了。我先对着纸读，再回到声音里找那个字。唱得顺不能说明歌词已经准确，就像一段话说得快，也可能把关键的部分带过去。|I once omitted 留 and sang a grammatical but changed phrase. Checking the page restored the sense of leaving or preserving something, rather than simply giving. Smooth delivery did not establish accurate words.
节奏快起来以后，屏幕上一行已经换掉，我却还唱到中间。我们没有继续追到更快，先选慢一点的版本，让整句从头到尾都有机会出来。读字、听声音和跟节奏是相互帮助的事，也会同时增加负担。我这次只检查没有漏词，下次再听停在哪里舒服；不是把一首歌分成冷冰冰的规定，而是给自己一个能真正听出变化的办法。|When screen timing outpaced me, we slowed and checked complete words before refining pauses. Reading, hearing and rhythm can help but also add load; focusing on one observable change made progress listenable.
我问能不能把每个字的声调都原样唱出来。林安说旋律会让音高沿着乐曲走，长音也会改变平时说话的节奏。我们另外听歌词的说话读法，再跟旋律唱，没有把高音低音当成声调训练的成绩。这样不是说唱歌对学习没用，只是唱得像一段旋律和说话时字读得准，需要分别知道自己正在练什么。|We separated spoken readings from melody-driven pitch and stretched duration. Singing could help learning, but following a tune wasn’t a spoken-tone grade; we identified which task we were practising.
后来我们试两个版本，我第二段对以前的自己唱，林安对门外的朋友唱。唱完她问，门外的人会不会以为我在叫他回来。我说最后一句确实像在等回答，自己的那一句却像回头看一眼。她又唱了一次，把最后两个字放轻，我坐在桌边听，觉得那个人这回已经走远了。她说也许留第一版，既然想念，就不用装作一点也不想。我们各自记下喜欢的唱法，明天再一起听录音。|We tried two versions: I sang the second verse to my former self, and Lin An sang to a friend outside the door. Afterwards she asked whether it sounded like she was calling him back. I said her ending seemed to wait for an answer; mine felt like a glance backwards. She sang again, softening the final two words. This time I pictured him already far away. She thought she might keep the first version: if she missed him, why pretend she did not? We noted our preferred versions and planned to listen to the recordings tomorrow.
唱完以后，我想把这个方法带到别的歌：先看完整歌词，找重复句附近的变化，再确认听不清的字。熟悉的唱法可能来自一代人的听歌习惯，也可能融合不同风格，不能只凭声音像古典就说词一定古老。我们这首的文字和旋律都是新写的，有门、灯、风这些常见元素，却让它们在自己的句子里慢慢变方向。我愿意再唱一次，不急着把每一个空白都关上。|For other songs I will read the whole lyric, trace changing context around refrains and check unclear words. Style can blend influences without proving ancient authorship. Our newly written words and melody reuse familiar images while changing their direction.
''')
P=rows('''
写这首短歌时，我最早只有门外脚步和窗边的灯两个画面。那时候想的确实是一个朋友离开，留下的人不知道该再说什么。陈宇后来问能不能放一面镜子，让留下的人也看见自己。我喜欢这个想法，把旧衣和还没画完的新路放进去。不是把原来的朋友删掉，而是让告别以后还有自己的变化，不让房间只成为等别人回来的一处地方。|The initial images concerned a friend leaving. Adding a mirror, old clothes and unfinished road expanded the remaining person’s change without removing the friend or making the room only a waiting place.
我们写重复句你把风留给我，我把灯留给你，觉得两个动作并不相同。风留不住，灯也可能要关，人不能用东西真的交换一份永远不变的关系。可它们放在歌里，可以像两个人各留一点感受。写到这一声你也落在我自己心里时，我想让读者听见新的方向，同时不规定必须从哪一秒起把你全部换成自己。|Wind cannot literally be kept and lamps switch off, yet the exchange can suggest leaving feelings. The inward-address line offered another direction without a precise instant at which every “you” must change referent.
最后我写灯可以关，话不必忘，是因为不想让留下的人为了证明还在等，就永远不敢关灯睡觉。希望也可以跟正常的休息一起发生。新的岸边没有具体地名，船只没有保证带谁回来，我们没有把最后唱成以后再也见不到。如果有人听见的是往前走，也能听到还愿听你讲，这两个方向在结尾里可以互相牵着，不一定要只保留其中一个。|The lamp line allows rest alongside hope. Unnamed shore and unguaranteed return do not establish permanent separation; forward movement and a continued wish to listen coexist.
排练第一次，我听见陈宇省掉留，以为自己给他的稿子有旧版本。我们对了一遍纸，才知道文字没有变，是他跟着快节奏漏过那个音。我没有叫他把整首从头责怪自己一遍，只把这句慢慢读清，再让乐器一起进来。发现一个字漏了，需要具体修这一处，不需要把唱的人说成从来不认真；原来顺的地方也没有因此都变错。|An omitted word first looked like an old-page problem. We checked and repaired that specific phrase at a slower pace with accompaniment, without turning one omission into a character judgement or invalidating every correct part.
说话的读法和歌唱的声音，我们都留了一份。说话时可以仔细听每个词的常用读音，歌唱时音高跟着旋律，有些音留得长。长音本身不证明词错，也不证明词一定对，所以我们还是对照歌词。我没有把练歌说成自动练准每个声调，也没有因此取消练歌。知道不同版本解决什么问题，才不会拿一种声音去要求另一种任务的全部结果。|We retained spoken and sung versions for different purposes: lexical readings versus melody and duration, both checked against words. Neither held notes nor musical flow certify spoken-tone accuracy.
为了看哪里最容易跟丢，我把屏幕上的一行分成两次出现，但没有在字词中间乱切。陈宇说留给我连着看，比留在上一行、给我在下一行更容易懂。我于是让一句里的搭配留在一起，停顿放在意思能暂时停的地方。字幕的方便不是把每个字单独跳出来，而是让唱的人看得见一小段完整的关系，再顺着往下接。|We split screen timing at meaningful boundaries rather than break 留给我 across lines. Helpful timing showed short connected relationships rather than isolated flashing characters.
有朋友听了慢版，说感觉更孤独；另一个人却觉得像认真跟朋友讲话。我没有急着给这个速度贴一个固定情绪。音量、停顿、前后段落和听的人自己的经验，都会改变他听见的东西。我们可以说这一次我感觉怎样，也可以让别人指出是哪一句带来这种感觉。不需要为了让讨论有一个结束，就宣布某个速度只能属于某种情绪。|Listeners heard the slower version differently. We described perceptions and supporting lines rather than assign speed a fixed emotion; volume, pauses, context and experience all contributed.
后来陈宇唱给以前的自己，我听到镜子那段停得久一点。我的朋友版本在门外脚步后留了一点空间，好像等对方说一句。两次没有换一个嗓子，也没有追求突然变成完全不同的人。我们想试的是同样的词在不同关系里怎么站住，不是用夸张声音盖住词。当一处拖得太长，大家开始听不见后面的给我，我们就把那一处收回来。|Two interpretations retained one voice, varying pause placement. When stretching a phrase obscured later words, we shortened it rather than use exaggerated delivery to conceal the text.
这首歌里有海洋和船只，其实我们排练的小厅离海很远。写的人可以用没有站在眼前的画面，听的人也不用为了理解歌先去查作者住在哪里。我愿意说自己借这些画面想什么，却不会把每句都变成生活记录。歌里有孤独，不代表当天所有参与的人都孤独；朋友听出希望，也不需要证明现实里的每个告别都有好结果。|Imagined seascapes did not require the rehearsal to be seaside or the lyric to be a biography. Discussing the images did not establish everyone’s emotional state or guaranteed real-world outcomes.
最后我们给原稿记下了几个选择：重复句在三处出现，镜子提供第二种方向，最后保留向前和想再听的两层。以后如果改一行，就重新看它会不会让前后的关系变了，而不是只看字数够不够。唱法可以慢慢试，歌词也可以继续改。现在这版留下的空白，是我们有意留给听的人去连，不是因为忘了写一个确定结局。|Our notes preserved three refrains, the mirror’s second direction and the ending’s movement plus continued listening. Future edits should check surrounding relationships, not only length. The opening remained intentional rather than an accidentally omitted fixed ending.
''')
G=[
card('好似 / 仿佛','Recognise resemblance without literal identity','These words describe appearance or experience, often in literary narration. They do not assert that the compared thing is literally true.','那盏灯好似一个没回答的问题。|That lamp seems like an unanswered question.\n重复的那句仿佛换了一个说话的人。|The repeated line seems to have a different speaker.','那盏灯好似一个问题，意思是灯真的会开口问句子。','那盏灯好似一个没回答的问题。','The resemblance is figurative.'),
card('一时 / 时时 / 早晚','Distinguish temporary, repeated and eventual time scope','一时 can mean temporarily; 时时 means repeatedly or all the time; 早晚 can mean sooner or later. Context can also make 早晚 literal morning/evening.','我一时没跟上，停下来再读。|I temporarily lost pace and stopped to reread.\n她时时提醒我看后面的字。|She repeatedly reminds me to look at the following words.','我一时没跟上，表示以后永远都不可能跟上。','我一时没跟上，停下来再读。','The temporary scope does not establish permanent inability.'),
card('或A或B','Keep alternate readings available','或 can coordinate alternatives in written analysis. It does not mean every interpretation fits regardless of the surrounding lines.','你或是门外的朋友，或是镜中的自己。|“You” may be the friend outside or the self in the mirror.\n这一段或像等候，或像准备出发。|This section may resemble waiting or preparing to leave.','或像等候或像出发，所以歌词保证两件事都已经发生。','这一段或像等候，或像准备出发。','Possible readings do not certify two literal events.'),
card('不是…还/还是…','Recognise a rhetorical additive question','With question intonation, 不是 asks for confirmation of a known fact; 还 adds another fact. The speaker expects agreement rather than simply negating the first clause.','你不是已经看过歌词了吗，还漏了那个留字？|Haven’t you already read the lyrics? You still missed that 留?\n这版不是慢一点了吗，还是觉得跟不上？|Isn’t this version slower? You still feel unable to keep up?','你不是已经看过歌词了吗，断定你从来没看过。','你不是已经看过歌词了吗，还漏了那个留字？','The rhetorical question refers to prior reading and adds the unexpected omission; it does not assert never reading.'),
card('X来X去，都是…','Recognise repeated activity with a shared result','Verb来verb去 marks repeated activity. 都是 identifies what remains across those attempts; it does not prove no other future choice is possible.','唱来唱去，都是这几个词在不同地方出现。|Across repeated singing the same words appear in different places.\n看来看去，都是门、灯和风这几个元素。|On repeated looking the elements are door, lamp and wind.','看来看去都是这些元素，意思是以后禁止写新的元素。','看来看去，都是门、灯和风这几个元素。','A description of this text does not ban future revision.'),
card('除了…，…都…','Read an exception without erasing the main set','除/除了 specifies an excluded part. The main statement applies to the remaining group; the excluded item requires its own information.','除了漏掉的留字，其他字这遍都唱出来了。|Apart from the omitted 留, the other words were sung this pass.\n除了最后一行，前面的歌词都已确认。|Except for the final line, the preceding lyrics are confirmed.','除了最后一行前面都确认了，所以最后一行也已经确认。','除了最后一行，前面的歌词都已确认。','An exception is not confirmed by the statement about the rest.'),
]
spec=dict(title=('The refrain changes its direction','同一句，唱给谁？'),goals=['Track repeated images and shifting address in an original lyric','Support an interpretation while leaving unwritten outcomes open','Use spoken readings and paced rehearsal without confusing melody with Mandarin tones'],vocabulary=V,grammar=G,
dialogue=(D,[q('gist','How do the singers treat the repeated你?','Try friend and earlier-self readings with supporting context','Declare it must identify one real named person','Delete every word that permits two readings'),q('detail','Which word was omitted from留给我?','留','给','我'),q('inference','Does a high musical note establish a spoken tone grade?','No, melody and spoken lexical readings serve different tasks','Yes, high always means fourth tone','Yes, singing fast proves every word is correct')]),
reading=(R,[q('gist','What changes across the refrain?','Surrounding verses shift its possible address and emphasis','The words are rewritten on every repeat','A specific return date becomes guaranteed'),q('detail','Which image introduces a possible inward address?','The self in the mirror','A named train ticket','A speaker announcing a city'),q('inference','What does不保证带谁归来leave open?','Return is neither promised nor ruled out','Return next week is confirmed','Permanent separation is certified')]),
pairedTitle='Writing and rehearsing the opening',pairedReading=(P,[q('gist','What guides the revisions?','Word accuracy, meaningful boundaries and relations between images','Only making each version faster','Treating every image as a biographical fact'),q('detail','Why keep留给我together on screen?','It is a connected phrase that should not be split arbitrarily','The phrase has no meaning','The character给must always be hidden'),q('inference','Why shorten an overlong stretch?','It was obscuring the later words','Slowness is forbidden','Only one emotional delivery is permitted')]),
mediaTitle='Wind, lamp, and a new shore',media=(M,[q('detail','Where does the second direction appear?','Mirror and the address landing within the self','A guaranteed return ticket','A named city and date'),q('inference','Which ending claim is supported?','Moving on can coexist with wishing to hear someone again','A reunion has already occurred','Closing the lamp forbids any future contact')]),
glosses=[('添','add'),('庄','village; estate'),('牵','draw; lead; hold'),('旋律','melody'),('重音','emphasis; stress'),('岸','shore; bank'),('归来','return'),('嗓子','voice; throat'),('语气','tone of delivery'),('参','take part; refer to'),('空白','blank; opening left unfilled'),('阴影','shadow'),('放慢','slow down'),('省掉','omit'),('搭配','connected combination'),('不禁','cannot help'),('跳过','skip'),('泄','leak'),('钩','hook'),('版','version'),('镜','mirror'),('镜子','mirror'),('拖','stretch; drag'),('幕','curtain; screen'),('嫁','marry'),('笔','stroke; pen'),('标','mark'),('节拍','beat'),('停顿','pause'),('译','translate'),('拖长','stretch out'),('重','heavy; important'),('欣','joyful'),('照搬','copy wholesale'),('节奏','rhythm')],
place='Friends rehearsing their own short lyric',context='Three identical refrains follow footsteps, mirror and new shore.留is omitted in one rehearsal, not removed from the page. Slower versions and a spoken reading are used; no musical performance is treated as tone assessment.',
turns=[('第二遍的你只能是同一个门外朋友吗？','Must the second “you” refer only to the same friend outside?','Use the added mirror clue',['也可以想到以前的自己，要跟前后的词一起看。']),('没写一定回来，就是确定永远不见吧？','No guaranteed return means certainly never meeting again?','Keep both unconfirmed outcomes open',['不是，没有保证回来，也没有说一定不见。']),('唱得很顺，留字没唱也算准确吗？','It sounds smooth; is it accurate despite omitting 留?','Check actual words',['不算这一处准确，先把留给我读清再唱。']),('慢版一定只能唱得孤独吗？','Must the slower version always sound lonely?','Avoid a fixed speed-emotion claim',['不一定，还要听停顿、前后内容和唱法。'])],
usage=[('Offer an interpretation','我这样听，是因为后面有镜子里的我。','I hear it this way because of the later self-in-the-mirror line.','Point to a supporting line rather than announce the only meaning.'),('Recover a missing word','这里是不是少了一个留？我们看一下原稿。','Is 留 missing here? Let’s check the page.','Repair the specific word without sweeping judgement.'),('Separate listening tasks','这遍先确认词，下一遍再试停顿。','Check the words on this pass; try pauses on the next.','Use an observable target without pretending melody grades spoken tones.')],
tasks=practice(
[(R[1][0],R[1][1],'The mirror entirely erases the earlier friend reading.',False,'The text explicitly allows both directions.'),(R[3][0],R[3][1],'The ending guarantees that nobody can ever return.',False,'It removes a guarantee without ruling out return.'),(P[3][0],P[3][1],'Checking the page identifies a specific omitted word.',True,'The page retains 留; the singer omitted it.'),(P[7][0],P[7][1],'The stretched phrase is shortened because later words become unclear.',True,'Intelligibility matters alongside delivery.')],
[('第一段像朋友，第二段出现镜子里的我。可以讨论两个方向吗？','The first verse suggests a friend; the next includes the mirrored self. May we discuss both?',['可以，要指出前后支持的词。','不行，重复一次就只能永远同一个人。','可以，任何没写的城市和车票都已确定。'],0,'Supported alternatives differ from invented facts.'),('我一时没跟上，就说明永远学不会吗？','I momentarily lose pace. Does that mean permanent inability?',['不说明，先停下再读这一处。','说明，一时就是永远。','说明，不用再看具体漏了什么。'],0,'Temporary scope remains temporary.'),('这一遍除留字以外都唱出来，留字也已经唱准吗？','Every word except 留 was sung. Was 留 also sung correctly?',['没有，那正是需要修的一处。','是，其他字对就自动补上了。','是，留字以后永远不用唱。'],0,'Keep the explicit exception.'),('歌词有海洋，小厅离海很远。能说歌词一定记录眼前地理吗？','The lyric has an ocean while the hall is far inland. Must it document local geography?',['不能，画面可以来自想象。','能，唱到海就证明小厅在海边。','能，歌词一定是当天的地图。'],0,'A lyric image need not be an immediate location report.')],
[('我一时没跟上，停下来再读。','I momentarily lost pace and stopped to reread.','一时'),('那盏灯好似一个没回答的问题。','That lamp seems like an unanswered question.','好似'),('除了最后一行，前面的歌词都已确认。','Except for the final line, the preceding lyrics are confirmed.','除了'),('看来看去，都是门、灯和风这几个元素。','On repeated looking the elements are door, lamp and wind.','元素')],
[[(V[i][3],V[i][4]) for i in [0,1,3]],[(V[i][5],V[i][6]) for i in [4,5,6]],[(V[i][3],V[i][4]) for i in [12,13,16]],[(V[i][5],V[i][6]) for i in [18,19,21]],[(V[i][3],V[i][4]) for i in [24,25,30]]]),
review='Native review: lyric imagery/rhythm, inward/outward address, 一时/时时 distinctions and rhetorical 不是…还/还是 questions. Self-review keeps all text original, preserves three identical refrains and the added mirror clue, distinguishes omitted 留 from an authored revision, and does not certify a return or permanent separation. Spoken lexical readings remain separate from melodic pitch; the app supplies spoken Sayo audio rather than claiming sung tone assessment. Two separately authored readings develop listener and co-writer perspectives. No new voice identity, music source or copyrighted lyric is used.')
write(6,5,spec,publish='--publish' in sys.argv)
