"""Discuss an original performance using details rather than invented biography."""
import sys
import common
common.dictionary['弹']='tán'
from advanced_core import write,rows,words,q,card,practice
V=words('''
情节|plot; sequence of events|cốt truyện|情节里先收好旧信，后来才走向窗边。|The plot first has the old letters put away, then a move towards the window.|这个情节前面出现过一次。|This event appeared once earlier in the story.
剧本|script|kịch bản|剧本只写打开窗，没有写是谁回来。|The script says to open the window, not who returns.|他改了剧本的最后两句。|He changed the last two lines of the script.
诗歌|poetry; poem|thơ ca|这段诗歌把灯和等待放在一起。|This poem connects a light with waiting.|她喜欢先朗读诗歌，再讲自己的理解。|She likes reading poetry aloud before explaining her interpretation.
手法|technique; artistic device|thủ pháp|重复同一句是一种手法，不是忘了换词。|Repeating the same line is a device, not forgetting to change words.|这幅画用不同手法表现远处和近处。|The painting uses different techniques for distant and nearby areas.
联想|association; evoke|liên tưởng|窗边的灯让我联想到有人等着。|The light at the window makes me think of someone waiting.|听到这段声音，她联想到小时候的家。|This sound brought her childhood home to mind.
目光|gaze|ánh mắt|最后他的目光从盒子移到窗外。|Finally his gaze shifts from the box to outside the window.|她的目光一直停在那幅画上。|Her gaze remained on the painting.
神情|expression; look|vẻ mặt|他的神情放松了一点，没有立刻笑。|His expression relaxed a little without an immediate smile.|她看信时的神情，和刚才不同。|Her expression reading the letter differed from before.
频道|channel|kênh|这个频道放了完整表演，不只有一小段。|This channel posted the full performance, not just a short extract.|她换了频道，想找刚才的节目。|She changed channels to find the earlier programme.
视频|video|video|我先看完整视频，再比较朋友发来的短版。|I watch the full video before comparing the short version from a friend.|视频里听不清最后一句。|The final sentence is unclear in the video.
拍摄|film; shoot|quay; chụp|这段拍摄只对着上半身，没拍到窗边的动作。|This recording frames only the upper body, missing the action at the window.|他们明天下午拍摄，不是今天晚上。|They will shoot tomorrow afternoon, not this evening.
摄影师|photographer; camera operator|nhiếp ảnh gia|摄影师问，最后要不要把窗也放进画面。|The camera operator asked whether to include the window in the final frame.|她请摄影师晚一点再拍合照。|She asked the photographer to take the group photo later.
朗读|read aloud|đọc thành tiếng|先朗读两句，看看停在哪里。|Read two lines aloud first and consider where to pause.|他朗读的时候，没有把标点读成词。|While reading aloud he didn’t pronounce punctuation as words.
弹|play a stringed or keyboard instrument|chơi đàn|他一开始弹得轻，后来慢慢响起来。|He plays quietly at first, then gradually louder.|她今天想弹一段，不想唱整首。|Today she wants to play a passage, not sing the whole piece.
琴|stringed or keyboard instrument|đàn|琴放在窗边，不在门口。|The instrument is beside the window, not the door.|这把琴是借来的，结束以后要归还。|This instrument is borrowed and must be returned afterwards.
声|sound; classifier for sounds|tiếng|我听见一声响，才注意到盒子关了。|I heard a sound and noticed the box had closed.|她喊了两声，门口的人才听见。|She called twice before the person at the entrance heard.
情形|situation; circumstances|tình hình|只听录音和看现场，是不同的情形。|Hearing a recording and seeing it live are different circumstances.|这种情形以前发生过，但结果不一样。|This situation occurred before, with a different result.
仍旧|still; as before|vẫn|收好信以后，那个人仍旧记得过去。|After putting the letters away, the person still remembers the past.|下雨了，活动仍旧在室内进行。|It is raining, but the event still takes place indoors.
如同|like; as if|như|这里的灯如同一个还没说出的邀请。|The light here resembles an invitation not yet spoken.|这段回忆如同一张慢慢展开的地图。|This memory resembles a map gradually unfolding.
深度|depth|độ sâu|讲清细节，比只说有深度更能解释我的看法。|Explaining details conveys my view better than merely saying it has depth.|我们后来讨论的深度，比第一次大。|Our later discussion went deeper than the first.
时光|time; a period of life|thời gian; quãng đời|旧信让他想起一起住过的时光。|The old letters remind him of their time living together.|她把那段时光记在日记里。|She recorded that period in her diary.
岁月|years; passage of time|năm tháng|岁月过去，信上的字还在。|Years pass, but the writing on the letters remains.|这张照片留下了那段岁月的样子。|This photo preserves how that period looked.
人物|character; person portrayed|nhân vật|我说的是剧里的人物，不知道表演者自己的经历。|I mean the character; I don’t know the performer’s own experience.|两个读者对这个人物看法不同。|Two readers view this character differently.
散文|prose; literary prose|văn xuôi|节目先朗读一段散文，再唱这几句。|The programme reads a prose passage aloud before singing these lines.|这篇散文没有完整故事，写的是一个下午。|This prose piece describes an afternoon rather than a full plot.
展现|show; present; reveal|thể hiện|最后的动作展现了一点变化，没有把未来说死。|The final action shows some change without fixing the future.|她用一个例子展现两种做法的差别。|She used an example to show the difference between two approaches.
''')
D=rows('''
你觉得最后把信收起来，是不想再见那个人了吗？|Does putting the letters away mean never wanting to see that person again?
我觉得是暂时不再一直看，不一定是不想再见。|I think it means no longer constantly reading them, not necessarily refusing another meeting.
可他把盒子关上了。|But he closed the box.
后来又打开窗，灯还留着，你怎么看这一点？|Then he opened the window and left the light on. How do you read that?
像是在等，不过没有说谁会来。|Like waiting, but it doesn’t say who will come.
对，这也是我不想直接说永远不见的原因。|Right. That’s why I don’t want to claim never meeting again.
前半段那句我听成把灯关了。|I heard the earlier line as turning the light off.
是把信收了，不是把灯关了。|Putting letters away, not turning the light off.
难怪我以为后面又开灯，前后不太对。|No wonder I thought the light came back on and the sequence didn’t fit.
完整视频里，灯一直亮着，只有盒子关上。|In the full video the light stays on; only the box closes.
朋友发我的短版，没有最后开窗那一下。|My friend’s short version omitted the final window-opening action.
那你少看了一个能影响理解的动作。|Then you missed an action that could affect the interpretation.
我还是觉得最后有点难过。|I still find the ending a little sad.
我也觉得，没有说有希望就一定不难过。|Me too. Some hope doesn’t necessarily remove sadness.
你会在推荐里写什么？|What would you write in a recommendation?
先看完整的，注意灯、盒子和窗，再说自己的看法。|Watch the full version; notice the light, box and window, then give your view.
不能直接写大家都会被感动吧？|We can’t simply write that everyone will be moved, can we?
对，我可以写自己被哪一点打动，不替所有人答应。|Right. I can say which detail moved me, without speaking for everyone.
''')
M=rows('''
把旧信收进盒里。|Put the old letters in the box.
不是把名字忘记。|It isn’t forgetting the name.
岁月走过这张桌。|Years have passed across this table.
灯仍旧留在窗边。|The light still stays by the window.
雨声轻轻落在门前。|The sound of rain falls softly before the door.
我没有问谁走远。|I did not ask who went far away.
把旧信收进盒里。|Put the old letters in the box.
给今天留一点空。|Leave a little space for today.
如果风带来消息。|If the wind brings news.
我会把窗再打开。|I will open the window again.
你不必现在回来。|You needn’t return now.
我也会走向明天。|I too will move towards tomorrow.
''')
R=rows('''
周末的小型表演有朗读，也有一段新写的短歌。节目先讲一个人整理旧信的情形，再由他自己唱。桌上放着盒子，旁边有灯，窗在更远一点的地方。开头他一直看信，唱到把旧信收进盒里，才把纸慢慢放好。灯没有关，只是他的目光从纸上移开，让观众看到他不再只注意手里那一点过去。|A small weekend performance combined reading and an original song. A person sorted old letters before singing. A box sat on a table, a light beside it and a window farther away. He put the papers away when singing that line, leaving the light on and shifting his gaze from the letters.
我最初听到收信，就以为人物准备完全断开以前的联系。但是下一句唱不是把名字忘记，后面又说灯仍旧留在窗边，这使我的判断停了一下。收好东西可以是改变每天看它的习惯，也可以是想重新安排今天，不一定等于把过去都否定。我没有因此确定他一定会和谁见面，只是发现永远不见的说法也缺乏足够支持。|I first took putting letters away as breaking all contact. “Not forgetting the name” and the light remaining qualified that judgment. Changing a daily habit or making room for today needn’t reject the past. That doesn’t guarantee reunion, but weakens the claim of never meeting again.
短歌重复了两次把旧信收进盒里。第一次后面连着不是把名字忘记，第二次后面接给今天留一点空。同样一句，随着相邻的内容不同，提醒我看的地方也不同：一处解释没有做什么，一处说接下来想给什么留位置。重复不是只为了让观众记住几个字，也让听者把前后的变化放在一起。|The repeated box line first leads to not forgetting, later to space for today. Nearby wording changes its focus: what the action does not mean and what it makes room for. Repetition connects a shift, not merely memorisation of words.
最后唱如果风带来消息，我会把窗再打开。歌停以后，人物没有站在原地等一个确定的人上场，而是自己走向窗，把窗打开一点，又回头收好桌上的笔。这个动作展现愿意接触外面的可能，也保留他继续做自己事情的部分。现场没有别人回来，没有一句话保证未来，所以我不把那个开窗解释成已经团圆。|The final conditional news and window line is followed by opening the window slightly and returning to tidy a pen. No other person enters. Openness to possibilities coexists with ordinary ongoing activity; the action does not establish reunion.
音乐开始时，旁边的人弹得轻，后面有一小段停顿，能听见盒子关上的一声。这样的安排让我注意动作，不是每一秒都由声音填满。有朋友说那里像没准备好，我请他回看盒子关上的时候；他听见那个声音以后，觉得可能是特意留的。不过我们也没有看到全部准备过程，讨论的是作品里可以注意到的效果。|Quiet accompaniment pauses for the box’s closing sound, directing attention to action. A friend initially heard the pause as unpreparedness; seeing its timing suggested an intentional effect. We discussed observable effect without claiming access to all preparation.
我看过完整视频，也收到一个只拍上半身的短版。短版在最后一句以后马上结束，没有人物走向窗的动作。只听这版，确实更容易把结尾想成一直留在过去。朋友的理解不是凭空来的，而是他得到的内容较少。后来我们一起看完整的，他没有立刻变得和我一样，只说开窗让愿意往前走的解释多了一点依据。|The upper-body short video ends before the window action. It plausibly invites a more backward-looking reading because it provides less evidence. Watching the full version didn’t make my friend identical in opinion; it added support for moving forward.
我还是觉得这段有难过的地方：信收起来以前停了一下，唱你不必现在回来时声音很轻。我也看到一点希望：灯留着，窗后来打开，最后一句不是我永远等着，而是我也会走向明天。这些感觉可以同时存在，不必把整个表演只选成高兴或伤心。解释作品的深度，不是把感受说得越来越大，而是能让别人找到你注意的那一处。|Hesitation over the letters and the quiet return line feel sad; the retained light, opened window and moving-towards-tomorrow line suggest hope. Both can coexist. A useful interpretation points others to particular details rather than merely intensifying emotional labels.
推荐给另一位朋友时，我说可以先看完整的，再比较不同版本，不要只因为一句被单独拿出来，就认为知道全部情节。我写了自己喜欢的重复手法，也说最后仍然有不确定的地方。至于唱的人自己经历过什么，我不知道，也没有拿人物的一封信替他写生活。这是一段值得讨论的表演，不需要先发明表演者的过去，才让自己的感受显得认真。|My recommendation suggests the complete version and comparison, describes the repetition I liked and preserves uncertainty. The performer’s personal history is unknown; a character’s letter cannot supply it. Discussion doesn’t need invented biography to make an interpretation meaningful.
''')
P=rows('''
朋友给我发来一个短视频，说这段表演很有意思。我在回家的车上看，声音不大，有几个字没听清。画面只拍到一个人的上半身，手里拿着信，后来把信放下。我看见他的神情，没有看见桌子的全貌，也不知道灯是不是从头就亮着。看完以后，我发了一句，感觉他一直在等以前的人回来。|A friend’s short video reached me on the journey home. Quiet audio obscured words; an upper-body frame showed letters and expression, not the whole table or the light’s earlier state. I replied that the character seemed to wait for someone from the past.
朋友问我最后开窗怎么看。我才知道自己的版本没有这个动作，在最后一句唱完就停了。她没有直接说我看错，而是把完整频道里的视频发来，让我看看前后。回家后我重新看，发现灯始终没关，关的是装信的盒子。原来我听成关灯，也把收信和关灯合成了一件事，难怪觉得没有留下任何联系。|Asked about opening the window, I realised my version ended earlier. The full channel video showed that the light stayed on and the letter box closed. A misheard light action had compounded my interpretation of putting letters away as complete disconnection.
我先把歌词朗读了一遍，不跟音乐，确认把旧信收进盒里后面还有不是把名字忘记。这不是为了证明作品只能有一个答案，而是先分清自己听到的文字。读对以后，我仍然觉得人物没有完全放下，可是不会再用灯已经关了作为理由，因为画面没有支持那个说法。自己的感受可以保留，给它的依据需要改变。|I read the lyric aloud without music to recover the actual words, not prove a single interpretation. I still felt the character hadn’t fully let go, but could no longer cite a switched-off light that the full image didn’t show. The feeling could remain while its evidence changed.
完整画面里，歌结束以后，他走向窗，又回头收桌上的笔。我想了一会儿，说这不是只等别人行动，也在做自己的事。朋友认为这是愿意往前走，我觉得更像还在试着往前走。我们没有争谁已经猜到作者最后决定，而是各自指出走到窗边和回头这两处动作，讨论哪一处更影响自己的判断。|Opening the window and then tidying the pen suggested action beyond waiting. My friend saw moving forward; I saw trying to move forward. We discussed the visible actions instead of competing to know an author’s final private decision.
关于停顿，我第一遍以为弹琴的人忘了下一段。后来我听到停的时候正好有盒子关上的声音，觉得留空可能是一种手法。我没有因此说每一个停顿都一定特别设计，也没有说所有不流畅都等于有深度。这一次能找到声音和动作的联系，就先说这一处，不必把一个新的解释扩大到所有表演。|I first thought the accompanist forgot the next passage. The timed box sound suggested a device, without establishing that every pause is deliberate or every awkwardness profound. One observable connection supports a local interpretation, not a universal rule.
还有人留言说，唱得这么难过，表演者肯定经历过同样的事。我没有接着猜。故事里有信和等待，能说明人物的处境；唱的人可能在表演，也可能有自己的联想，我们并没有问过他。想讨论他的表达，可以说哪一句轻、哪里停、神情怎么变，不必先替他写一个确定的生活经历，再把作品里的每个字放进去。|A comment inferred the performer must have lived the same sadness. I didn’t join the speculation. Letters and waiting establish the character’s situation, not the performer’s unasked history. Vocal and visual details permit discussion without a fabricated biography.
第二天我和朋友一边散步一边聊，没有把所有句子都说成很大的评价。她说灯留着像一个没说出的邀请，我说收信以后还回头，也像还舍不得。两种联想都能在画面里找到一点依据，但也都不是画面直接告诉我们的结论。后来我们各自再想了一句，如果没有最后开窗，我们会怎么理解，这让讨论比只重复很好更具体。|On a walk we compared the retained light as invitation and the backward glance as attachment. Both have some support without being explicitly announced conclusions. Considering how omission of the window would change the reading made discussion more concrete than repeated praise.
我最后给另一位朋友推荐了完整视频，说短版也可以比较，但先知道它少了什么。我没有保证她会喜欢，也没有让她必须赞成我的解释。如果她更注意声音而不是动作，我们还可以接着问原因。看表演以后能这样聊天，对我比把一句话马上背成标准答案更有用；我既想听明白，也想学会把不同的看法讲到别人能继续问。|I recommended the full video while explaining the short version’s omission, without guaranteeing enjoyment or agreement. A friend attending to sound rather than action could add another reason. This conversation mattered more than memorising one approved answer: understanding and explaining views allowed further questions.
''')
G=[
card('随着…','Track a changing relation','随着 introduces a process or developing situation; connect it to an actual change rather than merely listing unrelated facts.','随着相邻内容改变，同一句带出的意思也变了。|As neighbouring wording changes, the same line’s implications change too.\n随着声音变轻，我更注意他的动作。|As the sound grows softer, I attend more to his actions.','随着声音变轻，所以它一直没有任何变化。','随着声音变轻，我更注意他的动作。','The first clause names the developing change.'),
card('不一定 / 未必','Keep an interpretation qualified','These deny certainty, not necessarily the proposition itself. Show the clue and keep the remaining alternatives open.','收好信不一定是不想再见。|Putting letters away does not necessarily mean refusing another meeting.\n有希望未必就不难过。|Hope does not necessarily remove sadness.','不一定再见，所以一定永远不见。','收好信不一定是不想再见。','Uncertainty about reunion is not certainty of permanent separation.'),
card('把…当成…','Identify an interpretation being assigned','把…当成… states what someone treats something as. It does not automatically make that classification correct.','我把关盒子当成关灯了。|I mistook closing the box for switching off the light.\n别把人物的经历当成表演者的经历。|Don’t treat the character’s experience as the performer’s.','我把它当成事实，所以它一定是事实。','我把关盒子当成关灯了。','The construction can describe a mistaken interpretation.'),
card('既…也…','Allow two compatible concerns','The paired clauses can express compatible perspectives or goals. A second feeling does not have to cancel the first.','这里既有难过，也有一点希望。|There is both sadness and some hope here.\n我既想听明白，也想说清自己的看法。|I want both to understand and explain my view.','既有希望，就一定没有难过。','这里既有难过，也有一点希望。','The paired construction explicitly allows coexistence.'),
card('跟…相比…','Name the relevant comparison','Give a comparison basis and an observed difference. A difference between two versions does not identify every viewer’s response.','跟短版相比，完整版多了开窗的动作。|Compared with the short version, the full version adds the window action.\n跟第一遍相比，这次我听清了收信。|Compared with the first viewing, I heard putting letters away clearly this time.','跟短版相比，所有人一定有完全相同的感受。','跟短版相比，完整版多了开窗的动作。','Compare observable content before predicting other people’s feelings.'),
]
spec=dict(title=('Discuss the details that moved you','把感受说具体'),goals=['Support a performance interpretation with visible or audible details','Compare a full performance with an incomplete extract','Retell chronology and discuss different readings without inventing biography'],vocabulary=V,grammar=G,
dialogue=(D,[q('gist','How do the friends develop their discussion?','Check actual lines and actions, then preserve differing interpretations','Declare everyone must share one feeling','Infer a performer’s whole life from the character'),q('detail','Which object closes in the full version?','The letter box','The window at the final moment','The light'),q('inference','Why does the missing final action matter?','It removes a possible clue for moving forward','It proves the friend has never watched any video','It guarantees a reunion shown on stage')]),
reading=(R,[q('gist','What makes the recommendation useful?','Specific evidence, version differences and honest uncertainty','A promise that every viewer will be moved','A biography invented from the lyric'),q('detail','What happens after the window is opened a little?','The character returns to tidy a pen','Another character returns and promises marriage','The light is switched off for the first time'),q('inference','What does the last action not establish?','That a reunion has already happened','That the window is opened','That the character also continues ordinary activity')]),
pairedTitle='The shorter version I received',pairedReading=(P,[q('gist','What changes after watching the full version?','The viewer revises evidence while retaining a qualified personal feeling','The viewer stops allowing different opinions','The performer’s biography becomes certain'),q('detail','What did the viewer initially mishear?','Putting letters away as turning the light off','Leaving a lamp as buying a train ticket','Opening a window as counting sixty-four visits'),q('inference','Why compare the ending with and without the window?','It reveals how one detail supports an interpretation','It proves all pauses are mistakes','It fixes an author’s private thoughts as known')]),
mediaTitle='Original verse: space for today',media=(M,[q('detail','What does putting letters away explicitly not mean?','Forgetting the name','Leaving space for today','Putting paper inside a box'),q('inference','Which interpretation fits the final four lines?','Openness to news alongside continuing one’s own life','A guarantee that someone has already returned','A command to wait forever without acting')]),
glosses=[('归还','return something borrowed'),('歌词','lyrics'),('片段','extract; passage'),('停顿','pause'),('标点','punctuation'),('合照','group photograph'),('调料','seasoning'),('纸张','sheet of paper'),('笔','pen'),('处境','circumstances'),('团圆','reunion'),('流畅','fluent; smooth'),('从头','from the beginning'),('音量','volume'),('上半身','upper body'),('舍不得','reluctant to part with'),('全貌','whole picture'),('拍到','capture on camera')],
place='A walk after an original small performance',context='The full performance closes a letter box, keeps a lamp on, then opens a window slightly and tidies a pen. A short upper-body video omits the final action.',
turns=[('灯关了吧？我听成关灯。','The lamp goes off, right? I heard turning it off.','Repair the misheard detail',['没有，灯一直亮着，关的是盒子。']),('开窗就证明那个人已经回来了？','Does opening the window prove the other person returned?','Separate clue and established event',['不能，现场没有别人回来，只是多一个可能的解释。']),('你觉得唱的人自己也有这段经历吗？','Do you think the performer had this experience personally?','Keep known and unknown apart',['我不知道，可以先谈人物和表演里的细节。'])],
usage=[('Point to a supporting detail','我这样理解，是因为最后又打开了窗。','I read it this way because the window opens again at the end.','Give a clue that another viewer can examine.'),('Preserve a different reading','我还觉得有点难过，不过你说的那一点也有依据。','I still find it somewhat sad, but your point has support too.','Recognising another clue does not require abandoning every feeling.'),('Recover a line','你说收信还是关灯？我最后两个字没听清。','Did you say put letters away or turn off the light? I missed the last two words.','Offer concrete alternatives to make a repeat useful.')],
tasks=practice(
[(D[9][0],D[9][1],'The full version keeps the light on while the box closes.',True,'The speaker explicitly contrasts the two objects.'),(R[3][0],R[3][1],'Another person appears at the end and establishes a reunion.',False,'No other person returns in the scene.'),(P[2][0],P[2][1],'Correcting the heard words removes every personal feeling.',False,'The viewer retains a feeling while changing its evidence.'),(P[5][0],P[5][1],'The character’s situation establishes the performer’s personal history.',False,'That personal history remains unasked and unknown.')],
 [('灯一直亮着，关的是盒子。哪一样关上了？','The light stays on; the box closes. Which closes?',['盒子。','灯。','最后打开的窗。'],0,'Identify the corrected object.'),('短版没有最后开窗，完整版有。两版有这个差别吗？','The short version omits the final window action; the full version includes it. Do they differ on that detail?',['有，短版少一个动作。','没有，两版每个动作都完全相同。','没有，完整版也根本没开窗。'],0,'The stated versions differ on the action, not necessarily every feeling.'),('人物有旧信，但我们没问表演者经历。能确定是他的生活吗？','The character has old letters, but the performer’s history is unasked. Can we establish it is his life?',['不能，先谈作品里看到的。','能，角色的信一定都是表演者本人写的。','能，所有唱歌的人都有同一段经历。'],0,'A portrayed situation is not confirmed biography.')],
 [('他一开始弹得轻，后来慢慢响起来。','He plays quietly at first, then gradually louder.','弹'),('灯仍旧留在窗边。','The light still stays by the window.','仍旧'),('跟短版相比，完整版多了开窗的动作。','Compared with the short version, the full version adds the window action.','相比')],
 [[(V[i][3],V[i][4]) for i in [0,3,4]],[(V[i][5],V[i][6]) for i in [8,11,16]],[(V[i][3],V[i][4]) for i in [18,21,23]]]),
review='Native review: original verse rhythm, 如同 invitation image, coexistence of sadness and hope, and natural performance discussion. 弹 is explicitly tán for playing an instrument. Self-review preserves letters/box/lamp/window chronology, keeps final pen action in both full-view readings, and identifies the omitted short-video action. No reunion or performer biography is established. An interpretation may retain sadness after a detail is corrected; factual comprehension and aesthetic agreement are separate. All prose and lyrics are original.')
write(5,12,spec,publish='--publish' in sys.argv)
