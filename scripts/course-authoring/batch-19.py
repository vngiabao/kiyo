"""Editorial source: personal priorities, customs, an apology and a useful gift."""
from common import *
from editorial import unit
character_groups.update({
's3-u17':[('内','inside'),('值','value'),('义','meaning; justice'),('体','body; form'),('观','view'),('况','condition'),('态','state; attitude')],
's3-u18':[('民','people'),('族','ethnic group; clan'),('华','splendid; China'),('化','change; transform'),('世','world; generation'),('庆','celebrate'),('古','ancient')],
's3-u19':[('补','supplement'),('怪','strange; blame'),('失','lose'),('伤','hurt'),('事','matter'),('善','good; improve'),('消','disappear; consume')],
's3-u20':[('创','create'),('设','set up'),('彩','colour'),('布','cloth'),('材','material'),('金','gold'),('约','approximately; arrange')],
})
# 体、观、态、事 are already introduced at earlier source levels. These slots
# recognize genuinely new level-3 glyphs in the displayed connected contexts.
character_groups['s3-u17']=[('内','inside'),('值','value'),('义','meaning; justice'),('似','similar'),('显','manifest; show'),('况','condition'),('属','belong to')]
character_groups['s3-u19'][4]=('乱','disorder; confuse')
unit_glosses.update({
's3-u17':{'对……来说':'for; from the perspective of','预算':'budget','安静':'quiet','吵':'noisy','相似':'similar','显然':'evidently','属于':'to belong to','需求':'need','状态':'state','情况':'situation','尊重':'to respect'},
's3-u18':{'习俗':'custom','传统':'tradition','介绍':'to introduce','练习者':'practitioner','每个人':'each person','像':'like; resemble','意义':'meaning','庆祝':'to celebrate','交流':'to exchange','模仿':'to imitate'},
's3-u19':{'道歉':'to apologize','迟到':'to be late','弄乱':'to mess up','误会':'misunderstanding','原因':'cause','责任':'responsibility','改正':'to correct','赔':'to compensate','受伤':'to be injured','正式':'formal','规则':'rule'},
's3-u20':{'礼物':'gift','实用':'practical','贺卡':'greeting card','材料':'materials','包装':'packaging','布袋':'cloth bag','原创':'original','照片':'photo','纪念':'to commemorate','彩色':'coloured'},
})
unit_glosses['s3-u17'].update({'热闹':'lively; bustling','拒绝':'to refuse'})
unit_glosses['s3-u18'].update({'文章':'article','提供':'to provide'})
unit_glosses['s3-u19'].update({'门牌号':'building or house number','漏掉':'to omit','漏':'to omit; leak','被浪费':'to be wasted','恢复':'to recover; restore'})
unit_glosses['s3-u20'].update({'金色':'gold-coloured','银色':'silver-coloured','盒子':'box','回忆':'memory; to recall','镀金':'gold plating; to plate with gold'})

u='s3-u17'
unit(u,'对你来说什么重要',[
'Explain a choice from a person’s perspective','Express concern or happiness directed toward a particular person','Compare personal needs without claiming everyone agrees'],[
('感情','feeling; affection','tình cảm','noun','朋友之间的感情不能只看礼物价格。','Friendship cannot be judged only by gift prices.'),
('感受','feeling; to feel','cảm nhận','noun','先听对方的感受，再解释。','Listen to the other person’s feelings before explaining.'),
('情感','emotion; emotional feeling','cảm xúc','noun','这段话表达情感，不是活动规则。','This passage expresses emotion, not event rules.'),
('内心','inner feelings; heart','nội tâm','noun','她内心想参加，今天却太累。','Inside she wants to join, but today she is too tired.'),
('心','heart; mind','lòng; tim','noun','心里想去，也可以说今天不方便。','Even if one wants to go, one can say today is inconvenient.'),
('思想','thought; ideas','tư tưởng','noun','交流思想，不必有完全一样的答案。','Exchange ideas; identical answers are not required.'),
('价值','value','giá trị','noun','对我来说，实用比价格更有价值。','For me, usefulness has more value than price.'),
('意义','meaning; significance','ý nghĩa','noun','这个选择对她有自己的意义。','This choice has its own significance for her.'),
('个人','individual; personal','cá nhân','noun','个人需要不一定一样。','Individual needs are not necessarily the same.'),
('自身','oneself; one’s own','bản thân','noun','先了解自身需要，再比较。','Understand one’s own needs before comparing.'),
('自主','to act independently; autonomous','tự chủ','verb','她可以自主选择，不必替她决定。','She can choose independently; there is no need to decide for her.'),
('理解','to understand','hiểu','verb','理解理由，不等于必须同意。','Understanding the reason does not mean one must agree.'),
('对方','the other person or party','đối phương','noun','先问对方有没有空。','Ask first whether the other person is free.'),
('对象','object; intended recipient','đối tượng','noun','这份说明的对象是新会员。','This explanation is intended for new members.'),
('合理','reasonable','hợp lý','adjective','按实际需要选择比较合理。','Choosing according to actual needs is more reasonable.'),
('客观','objective','khách quan','adjective','客观记录价格，不代替别人判断价值。','Record prices objectively without judging value for others.'),
('体会','to appreciate through experience; understanding','thấu hiểu','verb','听完她的理由，我能体会她的感受。','After hearing her reasons, I can appreciate her feelings.'),
('体验','to experience','trải nghiệm','verb','先体验一次，再决定要不要继续。','Try it once before deciding whether to continue.'),
('体现','to reflect; embody','thể hiện','verb','这个安排体现对不同需要的尊重。','This arrangement reflects respect for different needs.'),
('相似','similar','tương tự','adjective','需要相似，也不一定选同一个时间。','Similar needs do not necessarily mean choosing the same time.'),
('显然','evidently; obviously','rõ ràng','adverb','她显然还没决定，别替她答应。','She evidently has not decided; do not agree on her behalf.'),
('状况','condition; situation','tình trạng','noun','今天身体状况不好，就先休息。','If one feels unwell today, rest first.')],
[grammar(u,'三23','为：情绪或关心的对象','Identify whom an emotion or concern is directed toward',
'我为你高兴 and 我为她担心 identify the person an emotion concerns. This object use extends, rather than repeats, the earlier beneficiary use 为朋友打印材料. Both use wèi, unlike wéi in 成为. Concern does not authorize deciding for the person; 我替她决定 acts in her place. Preserve the distinction between a feeling toward someone and an action intended to benefit them.',[('我为你高兴，但不替你决定。','I am happy for you but do not decide for you.'),('她为朋友的身体担心。','She is concerned about her friend’s health.'),('别为我的选择着急，我会先问清楚。','Do not worry about my choice; I will clarify it first.')],('我为她担心，所以她必须听我的。','我为她担心，也尊重她自己的选择。','Concern is directed toward a person without removing their agency.')),
grammar(u,'三40','对……来说','State a perspective rather than a universal judgement',
'对我来说，安静很重要 locates the judgement in the speaker’s perspective. It does not establish that everyone prefers silence. 对新会员来说 also allows a group perspective, but avoid asserting uniform preferences without evidence. Compare 客观价格 with personally evaluated value.',[('对我来说，安静很重要。','For me, quiet matters.'),('对她来说，今天休息更合适。','For her, rest today is more appropriate.'),('对新会员来说，先看说明比较方便。','For new members, reading the explanation first is more convenient.')],('对我来说重要，所以对所有人都重要。','对我来说重要，对方的需要还要问。','A personal perspective does not generalize to everyone.'))],
('One event, two preferences','Find what each friend prefers and who makes the decision.',[
('对你来说，活动最重要的是什么？','What matters most to you about the event?'),('安静一点。我今天身体状况不好。','Some quiet. I am not feeling well today.'),('我喜欢热闹，可我能理解你的感受。','I like a lively atmosphere, but I can understand your feelings.'),('你为我担心，还换地点了吗？','You are concerned about me; have you also changed the venue?'),('没有。我为你准备两个选择，你可以自主决定。','No. I prepared two options for you; you can decide independently.'),('那我先体验安静的活动，不合适就休息。','Then I will try the quiet activity first and rest if it does not suit me.'),('好，理解不等于所有需要一样。','Okay; understanding does not mean every need is the same.'),('也别为我的选择着急，我还没定，会先问清楚。','And do not worry about my choice; I have not decided and will clarify first.')],
[('mainidea','What do the friends agree about?',['Respecting different needs and the person’s own choice','Everyone must prefer quiet','One person has already promised for both'],0),('detail','Has the venue been changed?',['No','Yes','It was cancelled'],0),('inference','Must preparing options mean the friend attends?',['No','Yes','Only if she tries once'],0)],[],True),
('Value is not just a price','Read how the organizer records different needs.',[
('对我来说，安静很重要；对朋友来说，交流也有价值。','For me quiet matters; for my friend, interaction also has value.'),('我们交换思想，不要求个人需要完全一样。','We exchange ideas without requiring identical individual needs.'),('我为她准备两个选择，没有替她决定。','I prepared two options for her and did not decide in her place.'),('说明的对象是新会员，可以先体验一次。','The explanation is for new members, who may try once first.'),('她内心想参加，今天的身体状况却不好。','Inside she wants to join, but she is not feeling well today.'),('我客观记录价格，也尊重她对意义和价值的判断。','I record the prices objectively and respect her judgement of meaning and value.'),('相似的需要不等于一样的选择，她显然还没答应。','Similar needs do not mean identical choices; she evidently has not agreed.'),('这个位置属于安静区，选择它也不代表拒绝朋友。','This place belongs to the quiet area; choosing it does not mean rejecting a friend.')],
[('mainidea','What should the record separate?',['Personal perspective, objective price and actual consent','Quiet as a rule for everyone','A prepared option as a promise'],0),('detail','Who makes her final decision?',['She does','The person who prepared options','All new members together'],0),('inference','Does choosing a quiet place reject the friendship?',['Not necessarily','Definitely','Only when the price is low'],0)],[(2,'决定'),(6,'相似')],False),
('Two choices, no invisible promise','Read an original short exchange about helpfulness.',[
('我为你想好了，感动吧？','I worked it out for you; moved, right?'),('两个选择很好，别顺便把我的答案也写了。','Two choices are good; just do not write my answer too.'),('好，笔给你。','Okay, here is the pen.'),('这次真是为我准备的。','This time it really is prepared for me.')],
[('inference','What does the friend want?',['A choice she can make herself','No options at all','The organizer to decide silently'],0)],[],True),
dict(tf=[('自主','她可以自主选择，我不替她决定。','She can choose independently; I do not decide for her.','She makes her own choice.',True,'自主 preserves her decision.'),('感受','我理解你的感受，但我的需要不同。','I understand your feelings, but my needs differ.','Both people have identical needs.',False,'Understanding is distinct from identical needs.')],reply=[('对方','准备好选择以后怎么做？','What should one do after preparing options?',['问对方想选哪个。','直接替她答应。','把个人需要当统一规则。'],0,'Ask the actual recipient.'),('价值','对你来说，价格就是所有价值吗？','For you, is price the whole value?',['不是，实用和意义也重要。','所有人都必须一样。','没有价格就没有朋友。'],0,'Explain the personal criteria.')],fill=[('理解','理解理由，不等于必须同意。','Understanding a reason does not require agreement.'),('相似','需要相似，选择也可能不同。','Needs may be similar while choices differ.')],match=[('客观',[('客观记录价格。','Record prices objectively.'),('她还没答应。','She has not agreed yet.'),('先体验一次。','Try it once first.')]),('状况',[('今天身体状况不好。','Not feeling well today.'),('为她准备两个选择。','Prepare two options for her.'),('对我来说安静重要。','For me quiet matters.')])]),
[('Ask about preferences','对你来说，什么最重要？','What matters most to you?','Ask without supplying the other person’s answer.'),('Preserve agency','我准备了选择，你自己决定。','I prepared options; you decide.','Help without claiming consent.')],
[('你替她答应了吗？','Did you agree on her behalf?','Preserve the undecided status',['没有，她自己决定。']),('今天状态怎么样？','How are you today?','Report a practical limit',['今天有点累，先休息。'])],
'Native check: 为2 wèi emotional object versus earlier 为1 beneficiary and 替 substitution, 对……来说 perspective, 自主 conversational register, 感情/情感 distinction and objective price versus evaluated value. Personal-needs claims are fictional and not universal. Native review pending.')

u='s3-u18'
unit(u,'这个习俗怎么理解',[
'Explain a custom without treating one example as universal','Direct a question to a specific person with 向','Use 像……一样 as a limited comparison'],[
('文化','culture','văn hóa','noun','了解文化，先问具体习俗。','To learn about culture, ask about a specific custom first.'),
('文明','civilization; civilized','văn minh','noun','文明交流也包括认真听不同意见。','Civil communication also includes listening to different opinions.'),
('民间','among the people; folk','dân gian','noun','民间故事有不同版本。','Folk stories have different versions.'),
('民族','ethnic group; nation','dân tộc','noun','一个民族也有不同的生活习惯。','An ethnic group can also have different everyday customs.'),
('华人','people of Chinese heritage','người Hoa','noun','华人的习惯不一定完全一样。','People of Chinese heritage do not necessarily all share identical customs.'),
('中华民族','the Chinese nation','dân tộc Trung Hoa','noun','文章讨论中华民族的文化，不代表每个人都一样。','The article discusses the culture of the Chinese nation; it does not mean every person is alike.'),
('社会','society','xã hội','noun','社会变化，习俗也会变化。','As society changes, customs can change too.'),
('人民','the people','nhân dân','noun','人民的生活不能只看一张照片。','People’s lives cannot be understood from a single photo.'),
('世界','world','thế giới','noun','世界各地有不同习俗。','Different places around the world have different customs.'),
('世纪','century','thế kỷ','noun','上个世纪的照片不代表今天。','A photo from the last century does not represent today.'),
('时代','era; age','thời đại','noun','不同的时代有不同的安排。','Different eras have different arrangements.'),
('古代','ancient times','thời cổ đại','noun','古代的习俗不一定一直保留。','Ancient customs have not necessarily all been preserved.'),
('现代','modern times; modern','hiện đại','noun','现代生活中也有人保留旧习俗。','Some people preserve older customs in modern life too.'),
('当地','local; in that place','địa phương','noun','向当地朋友问问，不要只猜。','Ask a local friend rather than merely guessing.'),
('国庆','national day; national celebration','quốc khánh','noun','国庆活动先看当地通知。','For National Day activities, check local notices first.'),
('庆祝','to celebrate','chúc mừng; kỷ niệm','verb','每个人庆祝的方式可以不同。','Each person may celebrate in a different way.'),
('做客','to visit as a guest','làm khách','verb','做客前问清楚时间。','Ask the time clearly before visiting as a guest.'),
('文学','literature','văn học','noun','文学里的场景不一定是现实规则。','A scene in literature is not necessarily a real-life rule.'),
('美术','fine arts','mỹ thuật','noun','美术作品也可以表现节日。','A work of fine art can depict a festival too.'),
('京剧','Peking opera','Kinh kịch','noun','京剧和普通聊天的声音不同。','Peking opera sounds different from ordinary conversation.'),
('武术','martial arts','võ thuật','noun','武术表演不是所有人的日常习惯。','A martial arts performance is not everyone’s daily habit.'),
('自然','natural; nature; naturally','tự nhiên','adjective','不知道就问，这样很自然。','Ask when you do not know; that is natural.')],
[grammar(u,'三24','向：行为的对象','Direct an action toward a recipient',
'向当地朋友请教 identifies the person approached for advice, not a physical compass direction. 向大家介绍 directs an explanation to an audience. This unit contrasts the action recipient with 朝门口走 from the previous unit. Asking one person does not make their answer representative of everyone.',[('向当地朋友请教。','Ask a local friend for advice.'),('她向大家介绍自己的习惯。','She introduces her own custom to everyone.'),('向主人问清楚时间。','Ask the host to clarify the time.')],('向朋友请教，所以所有人都这样做。','向朋友请教，再说明这是她的习惯。','The recipient is an informant, not proof of universal practice.')),
grammar(u,'三41','像……一样','Compare a stated feature without equating every feature',
'像平时一样先问时间 compares the specific procedure of asking the time. 像朋友一样交流 compares a manner of interaction; it does not literally establish friendship. State the feature being compared. Avoid an analogy that turns a performance, ancient story or one host’s practice into a universal custom.',[('像平时一样，先问时间。','As usual, ask the time first.'),('大家像朋友一样交流。','Everyone communicates like friends.'),('这次的安排像上次一样。','This time’s arrangement is like last time’s.')],('像朋友一样交流，就是所有人已经是朋友。','像朋友一样交流，是比较交流方式。','A comparison of manner does not establish actual identity.'))],
('Ask the host, not the whole world','Find whose practice is described.',[
('做客要带什么？网上说每个人都一样。','What should I bring as a guest? Online it says everyone is the same.'),('先向主人问。这次是她家的安排。','Ask the host first. This is her household’s arrangement.'),('她说像平时一样，先问时间就好。','She says as usual, just ask the time first.'),('那不用把电影里的场景当规则了。','Then I need not treat a film scene as a rule.'),('对。古代、现代和当地习惯，也不能混在一起。','Right. Ancient, modern and local practices should not be mixed together.'),('我向朋友请教，再向大家介绍她的习惯。','I will ask my friend and introduce her practice to everyone.'),('说清楚是她的习惯，不是所有人的。','Clarify that it is hers, not everyone’s.'),('好。不知道就问，比假装都知道自然。','Okay. Asking when unsure is more natural than pretending to know everything.')],
[('mainidea','What is the recommended approach?',['Ask the host and identify the scope of her practice','Treat every film scene as a rule','Assume everyone shares one custom'],0),('detail','What does this host ask the guest to do first?',['Ask the time','Bring a mandatory expensive gift','Perform martial arts'],0),('inference','Does one host’s answer represent all people?',['No','Yes','Only on National Day'],0)],[],True),
('An introduction with a clear scope','Read how an unfamiliar practice is presented.',[
('世界各地有不同习俗，一个民族内部也不一定一样。','Places around the world have different customs, and practices within an ethnic group need not be identical.'),('文章介绍中华民族的文化，但不替每个人决定生活方式。','The article introduces the culture of the Chinese nation but does not decide every person’s way of life.'),('人民的生活会随社会变化，上个世纪的照片不代表今天。','People’s lives change with society; photos from the last century do not represent today.'),('古代习俗可能保留，也可能改变，现代安排要再确认。','Ancient customs may persist or change; modern arrangements need checking.'),('我向当地朋友请教，她介绍自己家国庆庆祝的方式。','I asked a local friend, and she explained how her family celebrates National Day.'),('做客像平时一样，先问时间，不把她的答案当统一规则。','As with an ordinary visit, ask the time first and do not treat her answer as a universal rule.'),('民间故事、文学、美术和京剧提供文化材料，不等于日常规定。','Folk stories, literature, fine arts and Peking opera provide cultural material, not everyday regulations.'),('武术表演有自己的场合，华人也有不同习惯；不知道就问很自然。','Martial arts performances have their own occasions, and people of Chinese heritage have different practices; asking when unsure is natural.')],
[('mainidea','What limitation does the article stress?',['Culture includes variation and changing contexts','An old photo proves every current custom','Every artistic performance is a household rule'],0),('detail','Whose celebration was described?',['The local friend’s family’s','Every family’s','A confirmed universal rule'],0),('inference','May a historical custom change?',['Yes','No','Only in a film'],0)],[(4,'当地'),(6,'文学')],False),
('A guest, not a costume test','Read an original scene about an overgeneralization.',[
('电影里都这样，我也照着做吧。','Everyone does it this way in the film; I will copy it.'),('你去做客，不是去演电影。','You are visiting as a guest, not acting in a film.'),('那先向主人问时间。','Then ask the host for the time first.'),('很好，这个动作不用排练。','Good. That action needs no rehearsal.')],
[('inference','What does the reply favour?',['Asking the actual host','Copying every scene','Requiring a performance'],0)],[],True),
dict(tf=[('当地','我向当地朋友问，这是她家的习惯。','I ask a local friend; this is her family’s custom.','The answer is identified as a family practice.',True,'The scope is explicitly limited.'),('世纪','上个世纪的照片不代表今天。','A photo from the last century does not represent today.','The old photo proves every current custom.',False,'Time and scope differ.')],reply=[('做客','第一次去做客，先做什么？','Before a first visit as a guest, what comes first?',['向主人问清楚时间。','按电影猜所有规则。','替主人写统一习俗。'],0,'Ask the host.'),('文化','一个例子能代表所有人吗？','Can one example represent everyone?',['不能，要说明具体范围。','能，文学就是规定。','能，世界只有一种习惯。'],0,'Identify the actual scope.')],fill=[('庆祝','庆祝的方式可以不同。','Ways of celebrating may differ.'),('自然','不知道就问，这样很自然。','Ask when unsure; that is natural.')],match=[('现代',[('现代安排要再确认。','Check present-day arrangements again.'),('向当地朋友请教。','Ask a local friend for advice.'),('像平时一样先问时间。','Ask the time first as usual.')]),('京剧',[('京剧是表演，不是所有人的聊天方式。','Peking opera is performance, not everyone’s conversational style.'),('这只是她家的习惯。','This is only her family’s custom.'),('古代习俗也可能改变。','Ancient customs can also change.')])]),
[('Ask without assuming','这是你家的习惯，还是活动的规定？','Is this your household practice or an event rule?','Clarify scope respectfully.'),('Introduce a limited example','我朋友家是这样安排的。','My friend’s family arranges it this way.','Avoid claiming everyone does the same.')],
[('向谁问？','Whom should one ask?','Name the relevant recipient',['向主人问。']),('所有人都这样吗？','Does everyone do it this way?','Limit the claim',['不一定，这是她家的习惯。'])],
'Native check: 向 recipient versus 朝 direction, 像……一样 comparison scope, 文明 adjective versus civilization noun, 华人 and 中华民族 sociocultural register, folk/art genres and metaphorical film joke. No essentialist or universal custom claims. Native review pending.')

u='s3-u19'
unit(u,'解释原因，不推责任',[
'Give a cause using 由于 / 因为','Offer a consequence and repair with 因此','Keep an explanation separate from an excuse'],[
('由于','because of; owing to','do; bởi vì','preposition','由于地址写错，朋友走错了地方。','Because the address was wrong, the friend went to the wrong place.'),
('因此','therefore; consequently','vì vậy','conjunction','地址错了，因此需要发新地址。','The address is wrong; therefore a new one needs sending.'),
('发生','to happen; occur','xảy ra','verb','发生问题后，先说明情况。','After a problem occurs, explain the situation first.'),
('事件','event; incident','sự việc','noun','这次事件需要记录经过。','This incident needs a record of what happened.'),
('事故','accident','tai nạn','noun','事故和普通迟到不是同一个词。','Accident and ordinary lateness are not the same word.'),
('后果','consequence','hậu quả','noun','地址错误的后果是朋友多走了一段。','The wrong address caused the friend to travel farther.'),
('反应','reaction; response','phản ứng','noun','先听对方的反应，别急着解释。','Listen to the other person’s response before rushing to explain.'),
('表达','to express','bày tỏ','verb','道歉要表达责任，不只是理由。','An apology should express responsibility, not just reasons.'),
('声明','statement; to declare','tuyên bố','noun','正式声明不能把错误写成对方的问题。','A formal statement should not turn one’s error into the other party’s fault.'),
('宣布','to announce','thông báo','verb','确认以后再宣布新地点。','Announce the new venue after confirming it.'),
('发送','to send; transmit','gửi','verb','我现在发送正确地址。','I am sending the correct address now.'),
('补','to supplement; make up for','bù; bổ sung','verb','漏掉的信息现在补上。','Add the omitted information now.'),
('完善','to improve; make complete','hoàn thiện','verb','完善通知，不让别人再走错。','Improve the notice so others do not go the wrong way again.'),
('注意','to pay attention','chú ý','verb','下次发送前注意日期和地址。','Next time pay attention to the date and address before sending.'),
('奇怪','strange; odd','kỳ lạ','adjective','地址前后不同，让人觉得奇怪。','The inconsistent addresses seem strange.'),
('伤心','sad; hurt emotionally','buồn','adjective','她有点伤心，因为道歉像是在怪她。','She feels hurt because the apology sounds like blame.'),
('伤','injury; to hurt','vết thương; làm bị thương','noun','没有人受伤，但时间被浪费了。','No one was injured, but time was wasted.'),
('失去','to lose','mất đi','verb','不要因为解释不清而失去信任。','Do not lose trust because of an unclear explanation.'),
('消失','to disappear','biến mất','verb','消息消失了，也不能假装没发生。','Even if the message disappears, do not pretend nothing happened.'),
('信任','to trust; trust','tin tưởng','verb','修正错误以后，信任还要慢慢恢复。','After correcting the error, trust still takes time to recover.'),
('对待','to treat; deal with','đối xử','verb','认真对待朋友的时间。','Treat a friend’s time seriously.'),
('相关','related; relevant','liên quan','adjective','把相关信息一次发清楚。','Send all relevant information clearly at once.')],
[grammar(u,'三25','由于 / 因为','Identify the actual cause',
'由于地址写错 can introduce a cause noun phrase or clause. 因为我写错地址 directly identifies an agent and cause. 由于 is often more written; do not use it to obscure responsibility. A cause can explain a delay without excusing it. This unit concerns an incorrect address, not a real accident.',[('由于地址写错，朋友走错了地方。','Because the address was wrong, the friend went to the wrong place.'),('因为我写错地址，你多走了一段。','Because I wrote the wrong address, you travelled farther.'),('因为没核对，我发了旧通知。','Because I did not check, I sent the old notice.')],('由于你看了我写错的地址，所以是你的问题。','因为我写错地址，让你多走了一段，对不起。','Name the actual cause without shifting responsibility.')),
grammar(u,'三71','（由于）……，所以 / 因此……','Connect cause and consequence without inventing completion',
'由于地址错了，因此需要发新地址 states a consequence and needed action, not proof that the new address has been sent. Compare 已经发送 with 现在要发送. 因此 is a concise written connector; 所以 is frequent conversationally. The consequence should follow from the stated cause, not from blame unrelated to the facts.',[('地址错了，所以朋友多走了一段。','The address was wrong, so the friend travelled farther.'),('我漏了门牌号，因此现在补上。','I omitted the building number, so I add it now.'),('由于通知有错，所以先停止传播旧通知。','Because the notice is wrong, stop circulating the old one first.')],('需要补上，所以已经补好了。','需要补上，因此我现在补。','A necessary repair is not evidence of a completed repair.'))],
('The apology is not a defence speech','Find the error, the consequence and the actual repair.',[
('你怎么到了另一个门口？','How did you end up at the other entrance?'),('你发的地址是旧的，我多走了一段。','The address you sent was old, and I travelled farther.'),('对不起，因为我没核对，发了旧地址。','Sorry; because I did not check, I sent the old address.'),('刚才你只说我应该早一点出发，我有点伤心。','Just now you only said I should have left earlier; I felt a little hurt.'),('是我的错误，不是你的问题。我现在发正确地址。','It was my error, not your fault. I will send the correct address now.'),('还有门牌号，别漏了。','Include the building number too; do not omit it.'),('好，相关信息一起发。下次发送前再核对。','Okay; I will send the relevant information together and check again before sending next time.'),('谢谢，先把通知改好。','Thanks; correct the notice first.')],
[('mainidea','What makes the second apology more useful?',['It accepts responsibility and proposes a concrete repair','It blames earlier departure','It claims the old address never existed'],0),('detail','Why did the friend travel farther?',['The sent address was old','She refused the new address','The event was cancelled'],0),('inference','Has future checking already prevented every error?',['No, it is a future intention','Yes','Only if the message disappears'],0)],[],True),
('A cause and a responsibility','Read what is known and what remains to be done.',[
('由于我没核对地址，朋友到了旧门口，多走了一段。','Because I did not check the address, my friend reached the old entrance and travelled farther.'),('这次事件没有人受伤，但朋友的时间被浪费了。','No one was injured in this incident, but the friend’s time was wasted.'),('我先听她的反应，再表达道歉，不把后果当她的问题。','I listen to her response before apologizing, without treating the consequence as her fault.'),('通知漏了门牌号，因此现在补上并发送正确地址。','The notice omitted the building number, so I add it now and send the correct address.'),('发生了错误，消息消失也不能假装没发生。','An error happened; even if the message disappears, do not pretend it did not happen.'),('旧通知需要修正，不能宣布一个未经确认的新地点。','The old notice needs correcting; do not announce an unconfirmed new venue.'),('我把信息弄乱了，就要认真对待修正，不急着说信任已经恢复。','I confused the information and must take correction seriously, without rushing to say trust has already recovered.'),('完善通知是一次修正，下次发送前还要注意核对。','Improving the notice is one repair; next time still check before sending.')],
[('mainidea','What should the record contain?',['Cause, consequence and concrete correction','An excuse that erases responsibility','An invented accident'],0),('detail','Was anyone injured?',['No','Yes, the friend','The statement does not say'],0),('inference','Does deleting a message erase the incident?',['No','Yes','Only if the old notice is gone'],0)],[(0,'由于'),(3,'因此')],False),
('An apology does not need a scoreboard','Read an original scene about blame.',[
('可是我也等了五分钟。','But I waited five minutes too.'),('我们先改地址，不先比谁等得久。','Let us correct the address first, not compete over who waited longer.'),('好，是我发错了。','Okay; I sent it incorrectly.'),('这句比五分钟有用。','That sentence is more useful than the five minutes.')],
[('inference','What is prioritized?',['Accepting the error and correcting it','Winning a waiting contest','Deleting the evidence'],0)],[],True),
dict(tf=[('由于','由于地址写错，朋友多走了一段。','The wrong address made the friend travel farther.','The stated cause is the wrong address.',True,'The cause is explicit.'),('补','门牌号需要补上。','The building number needs adding.','The number has definitely already been added.',False,'需要 states a need, not completed action.')],reply=[('表达','你发错地址，怎么道歉？','You sent the wrong address; how do you apologize?',['对不起，是我没核对，我现在改。','你应该自己猜。','旧消息消失就没发生。'],0,'Accept responsibility and offer a repair.'),('相关','地址里还缺什么？','What is still missing from the address?',['门牌号，和地址一起发清楚。','一张比赛成绩。','朋友的所有秘密。'],0,'The dialogue identifies the omitted number.')],fill=[('注意','发送前注意核对日期。','Check the date before sending.'),('信任','信任还要慢慢恢复。','Trust still needs time to recover.')],match=[('后果',[('朋友多走了一段。','The friend travelled farther.'),('我发了旧地址。','I sent an old address.'),('现在补上门牌号。','Add the building number now.')]),('完善',[('完善通知，不让别人再走错。','Improve the notice to avoid another wrong trip.'),('先听对方的反应。','Listen to the other person’s reaction first.'),('不是你的问题。','It is not your fault.')])]),
[('Accept responsibility','是我没核对，给你添麻烦了。','I did not check and caused you trouble.','Explain without blaming the recipient.'),('Offer a concrete repair','我现在补上门牌号，再发一次。','I will add the building number now and send it again.','Keep promised and completed repairs separate.')],
[('谁写错地址？','Who wrote the wrong address?','Accept responsibility',['是我写错了。']),('现在怎么补？','How should it be repaired now?','Give the actual step',['补上门牌号，再发一次。'])],
'Native check: 由于 versus 因为 register, 因此 causal consequence, apology phrasing, 相关 attributive usage, emotional 伤心 versus physical 伤 and incomplete versus completed repair. Fictional wrong-address incident is not medical guidance. Native review pending.')

u='s3-u20'
unit(u,'礼物为什么这样选',[
'Explain a purpose with 为了','Choose a gift using the recipient’s actual needs','Distinguish material, artistic authorship and price'],[
('为了','in order to; for the purpose of','để','preposition','为了方便带书，我选了布袋。','To make carrying books easier, I chose a cloth bag.'),
('爱心','kindness; caring heart','lòng yêu thương','noun','爱心不只看礼物的价格。','Care is not judged only by a gift’s price.'),
('设计','to design; design','thiết kế','verb','这个设计方便放书。','This design makes storing books convenient.'),
('创作','to create an artistic work','sáng tác','verb','这张贺卡是我自己创作的。','I created this greeting card myself.'),
('创造','to create; bring into being','tạo ra','verb','一起创造回忆，比买贵东西重要。','Creating memories together matters more than buying expensive things.'),
('创新','to innovate; innovation','đổi mới','verb','创新不等于把别人的作品改个名字。','Innovation does not mean renaming someone else’s work.'),
('作品','work; artistic creation','tác phẩm','noun','这幅作品是朋友画的。','This work was drawn by my friend.'),
('作者','author; creator','tác giả','noun','送作品时说明作者是谁。','When giving a work, state who created it.'),
('彩色','coloured; colour','có màu','noun','彩色贺卡上写着祝福。','The coloured greeting card carries good wishes.'),
('布','cloth','vải','noun','这个袋子是布做的。','This bag is made of cloth.'),
('金','gold','vàng','noun','金色不等于材料是金。','Gold colour does not mean the material is gold.'),
('银','silver','bạc','noun','银色包装也不一定含银。','Silver-coloured packaging does not necessarily contain silver.'),
('纪念','to commemorate; keepsake','kỷ niệm','verb','这张照片可以纪念第一次见面。','This photo can commemorate the first meeting.'),
('祝','to wish someone well','chúc','verb','我祝她学习顺利。','I wish her success with her studies.'),
('节约','to economize; save resources','tiết kiệm','verb','用已有的纸，可以节约材料。','Using paper already available can save materials.'),
('浪费','to waste','lãng phí','verb','包装太多，反而浪费。','Too much packaging is wasteful instead.'),
('利用','to use; make use of','tận dụng','verb','利用现有材料，不冒充新的作品。','Use existing materials without pretending they are new original works.'),
('功能','function','chức năng','noun','布袋的功能是装书，不是表示价格。','The cloth bag’s function is to carry books, not display a price.'),
('适用','applicable; suitable for use','thích hợp để dùng','adjective','这个袋子适用的场合要看大小。','Its size determines the occasions this bag suits.'),
('应用','to apply; put to use','ứng dụng','verb','把课堂知识应用到贺卡上。','Apply classroom knowledge to the greeting card.'),
('消费','to consume; spend','tiêu dùng','verb','为了送礼，不必超过自己的消费预算。','Giving a gift does not require exceeding one’s spending budget.'),
('现金','cash','tiền mặt','noun','买材料付了二十块现金。','Paid twenty yuan cash for the materials.')],
[grammar(u,'三26','为了 + 目的','Distinguish a purpose from a recipient or cause',
'为了方便带书 states the intended goal. 为朋友准备礼物 identifies the beneficiary instead. 因为她喜欢读书 gives a cause motivating the choice. An intended purpose is not proof that the goal has already been achieved; ask whether the bag fits the recipient’s books.',[('为了方便带书，我选了布袋。','To make carrying books easier, I chose a cloth bag.'),('为了纪念第一次见面，我选了照片。','To commemorate the first meeting, I chose a photo.'),('因为她喜欢读书，我为她准备布袋。','Because she likes reading, I prepared a cloth bag for her.')],('为了方便带书，所以已经证明袋子合适。','为了方便带书选布袋，还要看大小是否合适。','An intention does not verify suitability.')),
grammar(u,'三72','为了……，……','Link an intended purpose to the chosen action',
'为了节约材料，我用了已有的纸 presents goal then action. It does not require 所以; distinguish causal 因为……所以 from purposive 为了. The alternative 我用了已有的纸，为了节约材料 is possible with context, but the exercise asks for the ordinary initial-purpose ordering. Keep the action concrete and verify the result separately.',[('为了节约材料，我用了已有的纸。','To save materials, I used paper already available.'),('为了让她方便带书，我选了布袋。','To let her carry books conveniently, I chose a cloth bag.'),('为了说明作者，我在卡片上写了名字。','To identify the creator, I wrote the name on the card.')],('为了她喜欢读书，我买了袋子。','因为她喜欢读书，我买了袋子。','Her existing preference is a cause; use 为了 for a goal to achieve.'))],
('A useful bag and an original card','Find why the gift was chosen and what was actually paid.',[
('你为什么选布袋，不选金色盒子？','Why choose a cloth bag instead of a gold-coloured box?'),('为了方便她带书，布袋的功能更适合。','To make carrying books easier for her; the bag’s function is more suitable.'),('金色盒子是金做的吗？','Is the gold-coloured box made of gold?'),('不是，只是颜色。银色包装也不一定是银。','No, just the colour. Silver-coloured packaging is not necessarily silver either.'),('这张彩色贺卡是谁创作的？','Who created this coloured greeting card?'),('我自己写的，照片是朋友拍的，作者都写清楚了。','I wrote it myself; a friend took the photo, and all creators are identified.'),('材料花了多少？','How much did the materials cost?'),('二十块现金，用了已有的纸，没有超过预算。','Twenty yuan cash; used paper already available and did not exceed the budget.')],
[('mainidea','What guides the gift?',['Usefulness, clear authorship and a budget','Metal colour proving expensive materials','Price alone proving care'],0),('detail','How much cash was paid for materials?',['Twenty yuan','Two hundred yuan','No cash at all'],0),('inference','Does gold colour prove gold material?',['No','Yes','Only on a greeting card'],0)],[],True),
('A gift note without inflated claims','Read the purpose, the authors and the material.',[
('为了方便朋友带书，我选了一个布袋，先确认大小。','To make carrying books easier, I chose a cloth bag and checked the size first.'),('布袋的设计实用，功能是装书，不是表示消费多少。','The bag’s design is practical; its function is carrying books, not displaying spending.'),('为了节约材料，我利用已有的纸创作彩色贺卡。','To save materials, I used existing paper to create a coloured greeting card.'),('照片是朋友的作品，卡片说明作者，不把别人的作品当成自己创作。','The photo is my friend’s work; the card identifies the creator rather than claiming another’s work as mine.'),('为了纪念第一次见面，选照片；为了表达祝福，写一句汉语。','To commemorate the first meeting, choose a photo; to express good wishes, write a Mandarin sentence.'),('金色和银色是颜色说明，不保证材料里有金或银。','Gold and silver colour describe appearance; they do not guarantee gold or silver content.'),('材料付了二十块现金，没有超过预算；过多包装会浪费。','Materials cost twenty yuan cash within budget; excessive packaging would waste resources.'),('把知识应用到实际表达，创造回忆，不必用价格证明爱心。','Apply knowledge to real expression and create memories; no need to prove care through price.')],
[('mainidea','What does the note avoid?',['Overstating price, material and authorship','Acknowledging a friend’s photo','Using existing paper'],0),('detail','Why use existing paper?',['To save materials','To pretend the bag is gold','To hide the creator'],0),('inference','Is the intended purpose itself proof the bag fits?',['No, size must be checked','Yes','Only with silver packaging'],0)],[(2,'节约'),(4,'纪念')],False),
('The box does not study for her','Read an original exchange about a useful gift.',[
('盒子看起来贵，应该更有爱心吧。','The box looks expensive; that should mean more care, right?'),('她要带书，盒子又不会替她读。','She needs to carry books; the box will not read for her.'),('那选合适的布袋，卡片自己写。','Then choose a suitable cloth bag and write the card myself.'),('很好，祝福不用镀金。','Good. A good wish needs no gold plating.')],
[('inference','What is the joke emphasizing?',['Use and sincerity over an expensive appearance','Gold proves friendship','A box can do the studying'],0)],[],True),
dict(tf=[('金','金色不等于材料是金。','Gold colour does not mean gold material.','Colour alone proves gold content.',False,'Appearance and material differ.'),('作者','照片是朋友拍的，卡片说明作者。','A friend took the photo; the card identifies the creator.','The friend’s authorship is acknowledged.',True,'The attribution is explicit.')],reply=[('功能','为什么选布袋？','Why choose a cloth bag?',['为了方便她带书。','因为金色一定是金。','为了替她决定所有事。'],0,'State the actual purpose.'),('消费','送礼必须超过预算吗？','Must giving a gift exceed the budget?',['不必，选合适的就好。','必须，价格等于爱心。','没有包装就不能送。'],0,'The recipient’s needs matter without overspending.')],fill=[('为了','为了节约材料，我用已有的纸。','To save materials, I use existing paper.'),('创作','贺卡是我自己创作的。','I created the greeting card myself.')],match=[('现金',[('材料付了二十块现金。','Materials cost twenty yuan cash.'),('照片是朋友拍的。','The photo was taken by a friend.'),('先确认布袋大小。','Check the bag’s size first.')]),('应用',[('把知识应用到贺卡上。','Apply knowledge to the greeting card.'),('包装太多会浪费。','Too much packaging is wasteful.'),('为了纪念第一次见面。','To commemorate the first meeting.')])]),
[('Explain a useful purpose','为了方便你带书，选了这个。','I chose this to make carrying books easier for you.','Ask about suitability instead of assuming it.'),('Credit a creator','照片是朋友拍的，贺卡是我写的。','A friend took the photo; I wrote the card.','Preserve each person’s actual contribution.')],
[('为了什么？','For what purpose?','State the recipient-focused purpose',['为了方便带书。']),('是谁的照片？','Whose photograph is it?','Credit the creator',['朋友拍的照片。'])],
'Native check: 为了 purpose versus 因为 cause and 为 beneficiary, 适用 versus 适合, 彩色 as modifier, 创作 versus 创造, 金/银 colour-material contrast, gift politeness and gold-plating metaphor. Original card/scene only, no copied lyrics or scripts. Native review pending.')

from retrievals import apply_ids
apply_ids(['s3-u17','s3-u18','s3-u19','s3-u20'])
