"""An original scene and verse for a final social/media retelling, not a readiness certificate."""
import sys
import common
from advanced_core import write,rows,words,q,card,practice
common.dictionary.update({'乐曲':'yuè qǔ','主角':'zhǔ jué','收藏':'shōu cáng'})
V=words('''
心愿|wish|mong muốn|她的心愿是走之前再一起唱一次。|Her wish is to sing together once before leaving.|这个心愿一直没有说出口。|This wish has remained unspoken.
心灵|inner spirit; mind|tâm hồn|这首歌写心灵里没有说完的话。|The song concerns words left unsaid in the inner self.|书里的故事触动了她的心灵。|The story moved her deeply.
海浪|sea waves|sóng biển|海浪的声音接在最后一句后面。|Sea-wave sounds follow the final line.|他们坐在岸边听海浪。|They sit by the shore listening to waves.
远方|a distant place|phương xa|她要去远方，但没有说永远不回来。|She's going far away without saying she'll never return.|这封信来自远方。|This letter comes from far away.
孤独|lonely; loneliness|cô độc|这一句有孤独，也有期待。|This line contains loneliness and anticipation.|她有时觉得孤独，仍愿意联系朋友。|She sometimes feels lonely but still wants to contact friends.
增进|increase; deepen|tăng thêm|一起排练增进了了解。|Rehearsing together deepened understanding.|这些交流能增进感情。|These exchanges can strengthen affection.
平衡|balance|cân bằng|我想平衡演出和休息。|I want to balance performing and resting.|两种安排之间需要平衡。|The two arrangements need balancing.
融合|blend; integrate|kết hợp|这段把说话和音乐融合起来。|This passage blends speech and music.|作品融合了两种形式。|The work blends two forms.
元素|element|yếu tố|雨声是这段音乐的一个元素。|Rain sounds are an element of this music.|别把每个元素都解释成一个人。|Don't interpret every element as a person.
演奏|play music|biểu diễn|演奏结束后，她才把信拿出来。|She takes out the letter after the performance.|他愿意演奏最后一段。|He's willing to play the final passage.
歌词|lyrics|lời bài hát|歌词没有写归来的日期。|The lyrics give no return date.|我先把歌词读完整。|I'll read the full lyrics first.
节奏|rhythm; pace|nhịp|这一段节奏慢下来，话却没变。|The passage slows while the words remain unchanged.|她想找到合适的节奏。|She wants to find a suitable rhythm.
乐曲|musical piece|bản nhạc|乐曲在说话之后开始。|The piece starts after the spoken dialogue.|这首乐曲我想再听一遍。|I'd like to hear this piece again.
上演|be staged|diễn|这段短剧今晚首次上演。|This short play is staged for the first time tonight.|同一场景又上演了一次。|The same scene was staged again.
上台|go onstage|lên sân khấu|她上台以前先喝了水。|She drank water before going onstage.|上台并不表示不紧张。|Going onstage doesn't mean not being nervous.
主角|lead character|nhân vật chính|主角最后没有拆信。|The lead doesn't open the letter at the end.|你从哪一幕改变了对主角的看法？|Which scene changed your view of the lead?
场景|scene; setting|cảnh|这个场景发生在车站。|This scene takes place at the station.|换了场景，人物关系没有全变。|The setting changes without every relationship changing.
场馆|venue building|địa điểm|场馆十点关闭。|The venue closes at ten.|先确认场馆的开放时间。|First confirm the venue's opening hours.
送行|see someone off|tiễn|明早我们去车站送行。|We'll see her off at the station tomorrow morning.|她说不用每个人都来送行。|She says not everyone needs to see her off.
难忘|unforgettable; memorable|đáng nhớ|那段安静让我很难忘。|That quiet passage is memorable to me.|这是一场难忘的见面。|This is a memorable meeting.
遗憾|regret; disappointment|tiếc nuối|没唱完有点遗憾，但还能下次接着唱。|Not finishing is disappointing,but we can continue next time.|她为错过那一幕感到遗憾。|She regrets missing that scene.
情绪|emotion; mood|cảm xúc|她的情绪在最后一段变了。|Her mood changes in the final passage.|先听情绪，再看具体的词。|Listen to the mood,then inspect the actual words.
隐藏|hide; conceal|che giấu|她没有隐藏要走的事。|She didn't hide that she was leaving.|那句话里隐藏着一个没问出来的问题。|That sentence conceals an unasked question.
透露|reveal|tiết lộ|结尾只透露他已经写过信。|The ending only reveals he has written a letter.|她透露了下一场的地点。|She revealed the next venue.
收藏|keep in a collection|lưu giữ|我想收藏这张节目单。|I'd like to keep this programme.|她收藏了几张旧照片。|She keeps a few old photographs in a collection.
一番|a spell or round; classifier for effort or talk|một phen|经过一番商量，我们先收东西。|After some discussion,we put things away first.|她一番话让我明白了。|Her explanation helped me understand.
时而|sometimes; now and then|lúc thì|这段时而轻，时而响。|This passage is now quiet,now loud.|她时而笑，时而看窗外。|She alternately laughs and looks outside.
早晚|sooner or later|sớm muộn|早晚还会见面，不等于已经定好日期。|Seeing each other sooner or later isn't a fixed date.|这个问题早晚要面对。|This issue needs facing sooner or later.
仿佛|as if|như thể|她仿佛想说什么，又停了。|She seems about to speak,then stops.|雨声仿佛从窗外进来。|The rain sounds seem to come in from outside.
盼望|look forward to|mong đợi|我盼望下次一起唱。|I look forward to singing together next time.|她盼望收到朋友的消息。|She looks forward to a friend's message.
留言|leave a message|nhắn|到了以后给我们留言。|Leave us a message after arriving.|他留言说今天会晚一点。|He left a message saying he'd be late today.
承诺|promise|hứa|没有确定时间，就别承诺周末回来。|Don't promise a weekend return before the time is settled.|她承诺到了以后发消息。|She promised to message after arriving.
''')
D=rows('''
最后一段你没拆信，我还以为忘了。|You didn't open the letter at the end.I thought you'd forgotten.
没忘，写的就是没拆。|I hadn't—that's what's written.
那里面到底是什么？|What exactly is inside?
没写给观众看。你可以猜，别说你已经知道。|The audience isn't shown.You can guess,but can't call it known.
我猜是让她别走。|I guessed it asks her not to leave.
也可能是到了再看。结尾没有给答案。|It could be for after arrival.The ending gives no answer.
你唱的那句灯还亮着，是等她回来？|The light still on in the song—is that waiting for her return?
可以这么听，也可以是今晚还没结束。|You can hear it that way,or as tonight not being over yet.
没有写下周回来，对吧？|No next-week return date,right?
对。别替歌词订车票。|Right.Don't book a ticket on the lyrics' behalf.
好。那现实里你明天几点的车？|Okay.In real life,when's your train tomorrow?
九点。八点半在入口见就行。|Nine.See you at the entrance at eight thirty.
我来送你。想吃点什么？|I'll see you off.Want anything to eat?
不用特意买，带水就好。|No special shopping.Just water.
其他人也来？|Are the others coming too?
他们要上班，别替我把全组叫来。|They have work.Don't call the whole group for me.
知道了。今晚还能再唱一遍吗？|Got it.Can we sing once more tonight?
九点半了，先收东西。场馆十点关。|It's nine thirty.Put things away first.The venue closes at ten.
那你要回去休息。|Then you need rest.
好，没唱完留一点，下次接着唱。|Yes.Leave a little unfinished;continue next time.
这句可以写到群里。|We can put that in the group.
可以，别写下周已经约好了。|Yes,but don't say next week is already booked.
到了给我们留言。|Message when you arrive.
会的。这句是承诺，不用拿来猜结尾。|I will.That one's a promise,no need to interpret it like the ending.
''')
M=rows('''
窗边的雨还没有停，|The rain beside the window hasn't stopped,
你把最后一句留在门边。|You leave the final sentence by the door.
我把灯调暗一点，|I turn the light down a little,
让没说完的话坐在身边。|And let unfinished words sit beside me.
远处有人叫你的名字，|Someone far away calls your name,
脚步从这一页走向明天。|Footsteps walk from this page towards tomorrow.
灯还亮着，门还没关，|The light is still on,the door still open,
不是每一次等候都要答案。|Not every wait needs an answer.
我在雨里听见一段歌，|In the rain I hear a piece of song,
唱到这里，先停一停。|Sing this far,and pause for now.
下一页留给下一次见面，|Leave the next page for the next meeting,
今晚这句，已经有人听见。|Someone has already heard tonight's line.
''')
R=rows('''
短剧最后一幕在车站，主角把一封信递给要走的朋友。朋友接了，放进包里，没有拆开。灯暗下来，音乐从旁边起，歌词唱到门还没关。我坐在第三排，看见她把包带拉好，突然觉得那封信里一定是在叫她别走。散场后我把自己的理解讲给陈宇，他问哪一句写了别走。我翻节目单，找了半天才发现，信里的字根本没有给观众看，自己说得最肯定的一句，原来是从表情和音乐里猜出来的。|In the station ending,a lead hands a letter to a departing friend.She puts it away unopened.Lights dim and lyrics mention an open door.Her tightening the bag strap made me certain the letter said don't leave.Chen Yu asked which line established that.The programme revealed no contents;my most confident claim came from expression and music.
他没有说不能这样理解，而是把看见和猜想分开。看见的是递信、收信、没拆，猜想的是写了什么、她为什么暂时不看。我们想到前面她说到了再告诉你，也想到他曾在桌边写了很久，却没有一个场景展示整封信。于是我把原来的肯定改成我猜他舍不得她走，但信也可能是留到到了以后再读。改了说法以后，那个结尾反而有更多可以聊的地方，不必让所有人争着证明一张观众没看见的纸上只有一种话。|He allowed my interpretation while separating observation from inference:handing over,receiving and not opening were visible.Contents and motives were guesses.Earlier dialogue and writing scenes offered clues without showing the letter.I changed certainty to a tentative reading with another possibility.The ending then offered more discussion rather than competing assertions about unseen words.
林安从后台出来，还拿着半杯水。她今晚演要走的朋友，明早现实里也要坐车去另一个城市，所以大家一看见她就想把戏继续问下去。她笑着说角色没拆，不是自己忘了台词，还问我们有没有听见最后一句。一个朋友马上问那你下周就回来吧，她摆手说戏里的门没关，不等于现实的车票已经买好。她很愿意听我们说自己的理解，却没有因此让每个愿望都变成她已经答应的安排。|Lin An emerged with water.She played the departing friend and was really travelling the next morning,so people carried the play into their questions.She hadn't forgotten a line;the character deliberately didn't open the letter.An open door in the song wasn't a booked return ticket.She welcomed interpretations without turning each wish into an agreed plan.
我想再听一遍歌，看看自己刚才是不是只抓住了灯亮着。林安说现在九点半，先收东西，场馆十点关闭，她还得回去准备明早。我们帮忙把椅子排回，音乐设备由负责的人检查，不能为了多唱一次把收尾都推给别人。等到门口，她轻声又唱了今晚这句已经有人听见，我才发现歌词后面不是一味等候，还写了把下一页留给下一次见面。那次见面没有日期，却也没有被取消，留一点没说完正好跟这晚相合。|I wanted the song again,but it was9:30and the venue closed10.Lin An also needed preparation for the morning.We restored chairs while responsible staff checked equipment.Extra singing couldn't dump closing work on others.Outside she quietly repeated the line about someone hearing tonight.I noticed the lyric's later next page,not just waiting.A meeting remained undated,not cancelled;unfinished words suited this evening.
第二天我八点半到车站入口，带水，没有特意买早饭。林安说另外几个人要上班，我没有替她把全组叫来。我们站到不挡人的地方，聊了昨天谁差点忘了拿包，又说信到底要不要拆。她说到了以后会给群里留言，这句话是她直接答应的，我就不用再猜。九点的车快开，她挥手走进去，我没有把送行写成大家都能随时陪着，也没有因为只有我在就觉得这次见面少了什么。|At8:30I met her at the station entrance with water,no specially bought breakfast.Others had work;I hadn't summoned them.We stood clear of the passage and chatted.She explicitly promised an arrival message,unlike an inferred lyric.Train time approached and she entered.Seeing her off didn't require everyone's availability;one friend was enough for this meeting.
晚上她发来照片，窗外有很远的灯，配了一句到了，明天再收东西。我把昨天的节目单夹进书里，写下看到递信、猜舍不得、未定下次时间、答应到后留言四件不同的事。不是为了把朋友的晚上写成一张检查表，而是想记住自己从哪一刻开始听得更完整。下一次聊一部剧、一首歌，或者一个朋友要走的事，我还会有猜错的地方，但可以说这是我的理解，再让对方告诉我他的那一段。|That evening her photo of distant lights said she'd arrived and would unpack tomorrow.I kept the programme and noted separate observations,inferences,undated plans and an explicit promise.Not to turn friendship into a checklist,but to remember hearing more fully.Future films,songs and departures would still allow wrong guesses.I could state my interpretation and hear another person's part.
''')
P=rows('''
写这首歌的时候，我先写了灯还亮着，再把它放进车站那场戏后面。排练时有人说灯肯定就是等那个朋友回来，我没有马上改掉，也没有说作者脑子里只能有一种答案。我的最初想法是一个晚上没有一下结束，人走了，话还在；放进戏里以后，它又跟车站、信和明天连在一起。愿意听的人可以从这些地方讲自己的理解，但若要说歌里已经约好下周见，就得找到真正写出时间的句子。|I wrote the still-lit light before placing it after the station scene.Some read it as waiting for the friend.I didn't reject that or insist on one authorial answer.My initial idea was an evening continuing in words after departure.The play linked it with station,letter and tomorrow.Readers could interpret those clues,but a next-week date would require an actual line naming it.
后来林安建议把下一页留给下一次见面放到后面，而不是开头。前面的雨声和脚步让人先听见离开，后面的那句才把还可以联系的机会带回来。我喜欢这个顺序，可第一次唱太快，下一页几乎跟上一句粘在一起，朋友只听见先停一停，以为结尾把见面也停掉了。我们先读完整，再按句子分开唱，没有为了追求一种特别轻的声音把词尾都吞掉。说话时能听清的词，放进音乐里仍需要给听的人留位置。|Lin An moved the next-page line later.Rain and steps introduced departure before future contact.But in the first fast rendition,next page stuck to the preceding line;listeners heard pause and assumed meetings were ending.We read the words fully,then phrased by sentences rather than swallowing endings for a delicate sound.Words still need space to be heard in music.
我负责演奏，不演拿信的角色，所以排练时常从旁边看两人。有一次林安忘了把信放进包，直接拿在手上走，画面就像她随时会拆。我们试了两次，发现收进包的动作比较符合这场戏想留下的空白。包带拉好以后，她看了一眼对方，再转身走。这个动作让人猜到关系和心情，却仍不公开信的内容。导演没有给信写一个只供答案看的秘密版本，讨论题也只能问看得见的动作和有根据的理解。|As musician rather than letter-holder,I watched the actors.Once she left with the letter in hand,looking about to open it.Putting it in the bag suited the intended gap.She looked back after fastening it,then left.The action suggested relationship and feeling without revealing contents.No hidden answer-only letter existed;discussion needed visible action and supported interpretations.
演出那晚，有人把角色的要走跟林安现实里明早坐车连起来，一下问了很多以后会不会回来。她没有藏着自己的行程，也不想把告别弄得很重。她说明早九点的车，八点半入口见，带水就好，别人需要上班的不用请假。说得很具体，我听起来反而舒服，因为我第二天不能去，但还能今晚帮收东西，也能等她到了发消息。朋友之间不是只有站在车站一个选项，留在自己已经答应的事情里，也能照顾这次离开。|People linked the role to Lin An's real travel.She didn't hide the journey or want a heavy farewell:9train,8:30entrance,water,and no need to miss work.Her specificity reassured me.I couldn't attend but could close tonight and await the arrival message.Friendship offered more than standing at a station;keeping my actual agreed role could support departure too.
九点半以后我们没有再开一遍设备。读书的人把纸收好，工作人员检查电源，我把乐器装回盒子。有人说多唱一分钟也没关系，可一分钟前后还要重新接线、调音和收好，不能只数唱出的那一分钟。我在门口轻轻哼了一句，没有打开扩音设备，林安把最后一行接上，大家笑了。这不是又办了一场完整演出，也不是把未完成都补齐，只是收尾路上一个很短的回应，刚好留在大家还能一起站着的时间里。|After9:30we didn't restart equipment.Readers collected papers,staff checked power,and I packed.One extra minute of singing also meant wiring,tuning and repacking,not merely that minute.I hummed outside without amplification,and Lin An added the last line.It wasn't a full performance or completion of everything,just a short response within our remaining shared time.
第二天我在群里看见她到了的消息，回了一个慢慢收的表情。之后有人问下一次什么时候，我说还没定，等大家各自的时间清楚再约。歌里下一页可以让人盼望，群里实际的日期却得有人确认。我们后来把两段歌词和演出录像整理到一起，保留原来的停顿，也在文字旁说明哪个地方重复。想跟唱的人能先看完整句，想聊戏的人能看见信确实没拆。这一页到这里结束，不表示朋友的来往也必须在同一个地方结束。|The arrival message prompted a gentle reply.Next-meeting timing remained undecided;it depended on everyone's schedules.The lyric could evoke anticipation,while the group needed confirmation.We later organised lyrics and recording with original pauses and repetitions clear.Singers could read full lines;discussion viewers could see the unopened letter.This page ending needn't end the friendship at the same point.
''')
G=[
card('仿佛…','Frame an impression rather than a known fact','仿佛 marks resemblance or impression. A visible action can support a reading without revealing an unseen text.','她仿佛想说什么，又停了。|She seems about to speak,then stops.\n雨声仿佛从窗外进来。|Rain seems to come from outside.','仿佛想说，表示已经说出全部内容。','她仿佛想说什么，又停了。','An impression does not establish spoken contents.'),
card('时而…，时而…','Describe alternating states','The parallel form describes variation,not an identical state throughout.','她时而笑，时而看窗外。|She alternately laughs and looks outside.\n这段时而轻，时而响。|This passage alternates quiet and loud.','时而轻时而响，表示全程音量一样。','这段时而轻，时而响。','The states vary.'),
card('一番','Read a measure for an effort or discourse','一番 can describe a round of effort,discussion or words;choose a suitable action rather than replacing every quantity.','经过一番商量，我们先收东西。|After some discussion,we put things away.\n她一番话让我明白了。|Her explanation helped me understand.','一番话必定只有一个字。','她一番话让我明白了。','The measure does not specify one character.'),
card('早晚','Distinguish sooner-or-later from a fixed date','In this sense 早晚 indicates eventuality,not necessarily morning/evening or a booked day.','早晚还会见面，不等于已经定好日期。|Meeting sooner or later is not a fixed date.\n这个问题早晚要面对。|This issue needs facing sooner or later.','早晚见面，表示已经约好下周一。','早晚还会见面，不等于已经定好日期。','The specific date remains unknown.'),
card('并不… / 不等于…','Limit a claimed implication','A limit can separate performer emotion,lyric interpretation and actual arrangements without rejecting all connection.','上台并不表示不紧张。|Going onstage does not mean no nerves.\n歌词的期待不等于已经买好车票。|Lyric anticipation does not mean a ticket is booked.','上台了，就证明完全不紧张。','上台并不表示不紧张。','An action does not prove absence of nerves.'),
card('不是每…都…','Keep the scope of a partial negation','This denies universality,not every possible instance. Keep 每 and 都 when reading the lyric.','不是每一次等候都要答案。|Not every wait needs an answer.\n不是每一个没说完的故事都取消了结尾。|Not every unfinished story cancels its ending.','不是每次都要答案，表示任何一次都不能有答案。','不是每一次等候都要答案。','Not all does not mean none.'),
]
spec=dict(title=('Leave a page for next time','把下一页留给下次'),goals=['Retell an original scene and discuss a supported interpretation','Read lyrics as imagery while keeping practical plans explicit','Write a concise account separating observation,interpretation and promises'],vocabulary=V,grammar=G,wordPos={'乐曲':'noun'},
dialogue=(D,[q('gist','What distinction do the friends preserve?','An open fictional ending versus real travel arrangements','Every lyric predicts a return date','Every audience guess is a known fact'),q('detail','When and where is the real send-off?','Eight thirty at the station entrance before the nine train','Nine thirty inside the venue tonight','Next Monday at a café'),q('inference','Why stop singing before ten?','Closing duties and the traveller’s rest need time','The friendship has ended','Every song has been permanently banned')]),
reading=(R,[q('gist','What does the audience narrator learn?','State an interpretation as one,and retain actual promises separately','Claim the unseen letter contents as certain','Treat one friend’s departure as a universal ban on contact'),q('detail','Is the letter opened for the audience?','No','Yes,the whole text is projected','Yes,before the music'),q('inference','Which is an explicit real promise?','Message after arrival','Return next week','Everyone will join the station send-off')]),
pairedTitle='The musician keeps the pause',pairedReading=(P,[q('gist','What does the musician add?','Authored phrasing,staging and closing work behind the audience’s experience','A secret answer-only letter','A guaranteed next-week show'),q('detail','What is changed after a too-fast rehearsal?','Read full lines and phrase them clearly','Delete every word ending','Change to a new speaker identity'),q('inference','Why not count only one extra minute of singing?','Restarting,tuning and packing also take time','The venue permits infinite extensions','No equipment is involved in a full repeat')]),
mediaTitle='The light is still on',media=(M,[q('detail','What is left for a later meeting?','The next page','A guaranteed next-Monday ticket','An opened letter with every answer'),q('inference','Does not every wait needs an answer mean none can have one?','No,it denies all,not every instance','Yes,no answer can ever occur','Yes,it proves the date')]),
glosses=[('粘', 'stick together'),('吞', 'swallow'),('后台','backstage'),('台词','spoken script'),('包带','bag strap'),('扩音','amplification'),('哼','hum'),('调音','tune; adjust sound'),('接线','connect cables'),('停顿','pause'),('秘密','secret'),('幕后','behind the scenes'),('放映','screening'),('拆信','open a letter'),('未完成','unfinished'),('空白','gap'),('车票','train or bus ticket'),('调暗','dim'),('乐器','musical instrument'),('电源','power supply'),('夹','insert between'),('舍不得','be reluctant to part with'),('角色','role; character'),('影像','images'),('下一页','next page'),('文字','written text'),('仪式','ceremony'),('主角','lead character'),('仿佛','as if'),('柜','cabinet'),('合奏','play together')],
place='After a fictional short play,then a real friend’s station send-off',context='Originalplay lettergiven/received/unopened;contentsunseen.Originallyrics openendedanticipation,notfixeddate.RealLinAn9train,nextmorning8:30stationentrance,wateronly,otherswork.21:30closingstarts,venue22closed.Explicitarrivalmessagepromise fulfilled;nextmeetingundated. Audienceandmusicianknowdifferentdetails.',
turns=[('信没拆，那里面一定让她别走？','Unopened letter must say do not leave?','State supported interpretation',['可以这样猜，但内容没给观众看，不能说一定。']),('歌词说下次见面，所以已经约好下周？','Next meeting lyric means next week booked?','Separate imagery and schedule',['不是，具体日期还没定。']),('再唱一分钟，收尾时间就只多一分钟吧？','One minute singing adds only one minute?','Account for setup and packing',['还要接线、调音和收好，不能只数唱的时间。']),('你答应到了留言，这也是歌词猜想？','Your arrival-message promise is also a lyric guess?','Retain explicit practical commitment',['不是，这是现实里直接答应的事。'])],
usage=[('Offer an interpretation with room to reply','我猜他舍不得她走，你从哪里听出别的意思？','I think he is reluctant to part;what suggests another meaning to you?','Discuss actual clues without making an unseen text certain.'),('Make a practical promise explicit','到了以后我发消息，时间没定的先不答应。','I will message after arrival;I will not promise an unsettled date.','Keep a commitment separate from poetic anticipation.'),('Retell in useful categories','我看见她收信，猜她想以后读；下次见面还没定。','I saw her put the letter away and guess she plans to read later;the next meeting is undated.','A concise account can retain fact,inference and practical uncertainty.')],
tasks=practice([(R[0][0],R[0][1],'The letter contents are shown to the audience.',False,'They remain unseen.'),(R[4][0],R[4][1],'The real train leaves at nine and meeting is eight thirty.',True,'Both times are explicit.'),(P[2][0],P[2][1],'A hidden letter supplies a single answer for tests.',False,'No secret answer-only letter exists.'),(P[4][0],P[4][1],'Repeating a full performance requires only its sung minute.',False,'Setup,tuning and packing also count.')],
[('观众没看见信的字，哪种复述合适？','Audience cannot see the letter.Which retelling fits?',['我猜是舍不得，但信的内容没给看。','信肯定写明下周回来。','我已经读过整封信。'],0,'An interpretation retains the unseen content.'),('九点车，八点半入口见。几点来符合？','9train,8:30entrancemeeting.Which fits?',['八点半在车站入口。','九点半去场馆。','下周一在咖啡店。'],0,'The explicit practical arrangement is separate from the scene.'),('歌词说不是每次等候都要答案，表示什么？','Not every wait needs an answer.Meaning?',['并非全部都需要，不是一个都不能有。','所有等候都不能有答案。','已经写出每个人的日期。'],0,'Not all is not none.'),('她答应到了发消息，哪句是履行承诺？','She promised an arrival message.Which fulfils it?',['到了，明天再收东西。','歌词里的门还没关。','我猜信里让她回来。'],0,'A real arrival update fulfils the explicit promise.')],
[('经过一番商量，我们先收东西。','After some discussion,we put things away first.','一番'),('她仿佛想说什么，又停了。','She seems about to speak,then stops.','仿佛'),('她时而笑，时而看窗外。','She alternates laughing and looking outside.','时而'),('没有确定时间，就别承诺周末回来。','Do not promise a weekend return before timing is settled.','承诺')],
[[(V[i][3],V[i][4]) for i in [0,2,4]],[(V[i][5],V[i][6]) for i in [6,8,10]],[(V[i][3],V[i][4]) for i in [12,15,18]],[(V[i][5],V[i][6]) for i in [21,24,27]],[(V[i][3],V[i][4]) for i in [28,30,31]]]),
review='Native review: original verse imagery/collocation,poeticunfinishedwords,letter/ticket banter,musician register and lexical乐曲yuèqǔ/主角zhǔjué/收藏shōucáng. Self-review differentiates visibleactions/unseenletter/interpretation,poeticnextmeeting/real8:30→9travel,21:30→22closingduties,wateronly/noinvoluntarygroupinvite,and explicitfulfilledarrivalmessage. Originallyrics not existing song. Capstone asks retelling and meaning,no fabricated voice or HSK readiness grade.')
write(6,12,spec,publish='--publish' in sys.argv)
