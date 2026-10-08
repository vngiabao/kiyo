"""Two independently authored contexts per existing word, not dialogue stuffing."""
VOCAB={
9:'''光|光看菜单我就饿了。|Just looking at the menu makes me hungry.|你光带手机，不带钱吗？|Are you bringing only your phone and no money?
仅|这张票仅限今天使用。|This ticket is valid only today.|门口仅剩两个座位。|Only two seats remain by the door.
仅仅|我仅仅看了开头，还没看完。|I've only watched the beginning, not the whole thing.|他仅仅比我早到一分钟。|He arrived just a minute before me.
至少|从这里走过去至少要二十分钟。|It takes at least twenty minutes to walk there.|你至少告诉我几点回来吧。|At least tell me when you'll be back.
有的是|别急，周末有的是时间。|Don't rush. We've got plenty of time at the weekend.|冰箱里有的是吃的。|There's plenty to eat in the fridge.
目前|目前还没有回家的车票。|There are no tickets home available at present.|我目前住在学校附近。|I'm currently living near the school.
近期|这家店近期要搬家。|This shop is moving soon.|她近期不在北京。|She hasn't been in Beijing recently.
空|这个盒子是空的。|This box is empty.|桌上还有一个空杯子。|There's another empty cup on the table.
公布|比赛结果明天公布。|The competition results will be announced tomorrow.|学校公布了放假时间。|The school announced the holiday dates.
规定|这里规定十点以后不能唱歌。|The rules here prohibit singing after ten.|他给自己规定每天读十页。|He set himself a rule of reading ten pages a day.
保证|我保证这次不迟到。|I promise I won't be late this time.|这个袋子能保证书不淋湿吗？|Will this bag keep the books dry in the rain?
确定|你确定是在这个门口等吗？|Are you sure we're waiting at this entrance?|日期确定以后，发消息给我。|Message me once the date is confirmed.
票价|周末的票价比平时高。|Tickets cost more at weekends.|儿童票价是多少？|How much is a child's ticket?
费用|这次旅行的费用我们平分。|We'll split the cost of this trip.|换电池的费用包括在里面吗？|Does that include the cost of replacing the battery?
价格|这件衣服的价格有点高。|This garment's price is a little high.|我想比较一下两家店的价格。|I'd like to compare prices at the two shops.
价钱|这个包是什么价钱？|How much is this bag?|价钱差不多，我选蓝色的。|The prices are similar, so I'll choose the blue one.
必要|有必要提前订位子吗？|Do we need to book seats in advance?|没必要为这点小事生气。|There's no need to get angry over such a small thing.
场所|附近有没有适合聊天的场所？|Is there somewhere nearby that's suitable for a chat?|这个场所晚上八点关门。|This venue closes at eight in the evening.
场合|这种场合穿衬衫比较合适。|A shirt would be appropriate for this occasion.|我在不同的场合见过她两次。|I've met her twice on different occasions.
公共|请别把包放在公共通道里。|Please don't leave your bag in the shared passageway.|这里的公共交通很方便。|Public transport is convenient here.
有效|这张优惠券今天还有效。|This voucher is still valid today.|换一种办法可能更有效。|A different approach might work better.
取消|下雨了，野餐取消吧。|It's raining. Let's cancel the picnic.|我取消了明天的订位。|I cancelled tomorrow's reservation.''',
10:'''本来|我本来想走路，后来下雨了。|I'd planned to walk, but then it rained.|这本书本来就在我包里。|This book was in my bag all along.
曾经|我曾经在这条街上住过。|I once lived on this street.|她曾经教过我弹钢琴。|She taught me piano once.
从来|我从来没来过这家店。|I've never been to this shop.|他从来不吃辣的。|He never eats spicy food.
赶紧|车来了，赶紧走吧。|The bus is here. Let's hurry.|赶紧把窗户关上，雨进来了。|Quick, close the window; rain's coming in.
赶快|快八点了，赶快起床。|It's almost eight. Get up quickly.|汤要凉了，赶快喝。|The soup will get cold. Drink it while it's hot.
立刻|她听见门铃，立刻去开门。|She heard the doorbell and went straight to open the door.|收到地址，我立刻出发。|I'll leave as soon as I get the address.
连忙|杯子倒了，我连忙拿纸擦。|The cup tipped over and I quickly grabbed paper to wipe it up.|看到朋友进来，他连忙站起来。|He hurriedly stood up when he saw his friend come in.
始终|比赛的时候，她始终没有放弃。|She never gave up throughout the competition.|那张照片始终放在他的桌上。|That photo has stayed on his desk all this time.
已|您的订单已收到。|Your order has been received.|通知上写着活动已取消。|The notice says the event has been cancelled.
早已|电影早已开始了，快进去吧。|The film started ages ago. Go in quickly.|这件事我早已忘了。|I'd forgotten about that long ago.
自从|自从搬家以后，我每天坐地铁。|Since moving, I've taken the metro every day.|自从那次见面，我们常常联系。|We've kept in touch often since that meeting.
从前|从前这儿有一家书店。|There used to be a bookshop here.|奶奶喜欢讲从前的事。|Grandma likes talking about the old days.
过去|过去我不爱喝茶，现在每天喝。|I used not to like tea; now I drink it every day.|我们聊了一会儿过去的生活。|We talked about our lives in the past for a while.
当初|当初怎么想到搬来这里？|What made you decide to move here in the first place?|当初买这辆车的时候，它还是新的。|This car was new when I first bought it.
至今|那件外套我至今还留着。|I still have that coat to this day.|他至今没有回复那封信。|He still hasn't replied to that letter.
年代|这张照片是哪个年代的？|What era is this photo from?|我喜欢看八十年代的电影。|I like watching films from the eighties.
年初|年初我买了一辆自行车。|I bought a bicycle at the beginning of the year.|我们年初约好了夏天见面。|We arranged at the beginning of the year to meet in summer.
年底|我年底准备回家。|I'm planning to go home at the end of the year.|这家店到年底就开了十年了。|This shop will have been open for ten years by the end of the year.
变化|这条街变化很大。|This street has changed a lot.|天气有变化，记得带外套。|The weather's changing. Remember a coat.
变为|旧教室变为了一间阅览室。|The old classroom became a reading room.|水慢慢变为了冰。|The water gradually turned to ice.
成长|我在这个小城里成长。|I grew up in this small town.|看着孩子成长，她很高兴。|She's happy watching her child grow up.
印象|我对那家店的印象很好。|I have a good impression of that shop.|这首歌给我留下了很深的印象。|This song made a deep impression on me.''',
11:'''通常|我通常七点起床。|I usually get up at seven.|这家店通常周一休息。|This shop is usually closed on Mondays.
往往|周末这里往往人很多。|It's often crowded here at weekends.|他一着急，往往就忘了带钥匙。|When he's in a hurry, he tends to forget his keys.
总|这把伞怎么总找不到？|Why can I never find this umbrella?|你总比我早到。|You always arrive before me.
总是|她总是把杯子放在窗边。|She always puts her cup by the window.|这条路晚上总是很安静。|This road is always quiet at night.
日常|日常购物我都去这家店。|I come here for everyday shopping.|这是我日常用的包。|This is the bag I use every day.
长期|他长期住在国外。|He's lived abroad for a long time.|长期不用的东西，先收起来吧。|Put away the things you won't use for a long time.
短期|我想找一个短期课程。|I'd like to find a short course.|短期内我们不打算搬家。|We're not planning to move in the near future.
定期|我定期给家里打电话。|I call home regularly.|这辆车需要定期检查。|This car needs regular checks.
持续|雨持续了一整天。|The rain lasted all day.|音乐会持续了两个小时。|The concert lasted two hours.
连续|他连续三天都迟到了。|He was late three days in a row.|我们连续看了两集。|We watched two episodes in a row.
坚持|我坚持每天读一点书。|I keep up a little reading every day.|再坚持一会儿，就到山顶了。|Keep going a little longer; we're almost at the top.
保持|请保持门口通道畅通。|Please keep the entrance passage clear.|我们毕业以后一直保持联系。|We've stayed in touch since graduation.
经历|她给我讲了旅行的经历。|She told me about her travel experiences.|经历那次比赛以后，他不那么紧张了。|After that competition he wasn't as nervous.
经验|他做饭很有经验。|He's experienced at cooking.|第一次搬家，我一点经验也没有。|I had no experience at all when I first moved home.
整天|你整天坐着，不出去走走吗？|You've been sitting all day. Won't you go out for a walk?|猫整天睡在椅子上。|The cat sleeps on the chair all day.
整整|我等了你整整一个小时。|I waited for you for a whole hour.|这本书我读了整整一个星期。|I spent a full week reading this book.
久|好久没见，你还好吗？|Long time no see. How are you?|这家店开了多久了？|How long has this shop been open?
散步|吃完饭，我们去河边散步。|We'll go for a walk by the river after dinner.|奶奶每天早上在公园散步。|Grandma walks in the park every morning.
跑步|明早一起跑步吗？|Shall we go jogging together tomorrow morning?|跑步以后，我先喝点水。|I drink some water after jogging.
营养|午饭也要注意营养。|Think about nutrition at lunch too.|鸡蛋和牛奶都很有营养。|Eggs and milk are both nutritious.
暖和|今天比昨天暖和。|It's warmer today than yesterday.|这件外套很暖和。|This coat is warm.
困|我有点困，先回家了。|I'm a little sleepy, so I'll head home.|昨晚睡得晚，现在很困。|I went to bed late last night and I'm sleepy now.''',
12:'''尽量|明天我尽量早点到。|I'll try to arrive early tomorrow.|箱子尽量放里面一点。|Put the box further in if you can.
亲自|这封信是她亲自写的。|She wrote this letter herself.|老板亲自来接我们。|The boss came to meet us in person.
继续|雨小了，我们继续走吧。|The rain's lighter. Let's keep walking.|你继续说，我在听。|Carry on. I'm listening.
反复|他反复检查了三遍地址。|He checked the address three times.|这句话我反复听了好几遍。|I listened to this sentence several times.
训练|球队明天下午有训练。|The team has training tomorrow afternoon.|训练结束以后，我们一起吃饭。|We'll eat together after training.
克服|她克服了紧张，走上舞台。|She overcame her nerves and went onstage.|我们一起想办法克服这个困难。|Let's find a way to overcome this difficulty together.
困难|有什么困难，就告诉我。|Tell me if you're having difficulties.|这道题对我来说有点困难。|This question is a little difficult for me.
改造|这间旧屋准备改造为书店。|This old building will be converted into a bookshop.|厨房改造以后，地方大多了。|The kitchen is much bigger after the remodelling.
采取|漏水了，我们得采取措施。|There's a leak; we need to take action.|他们采取了新的办法。|They adopted a new approach.
采用|我们采用了小周的建议。|We took up Xiao Zhou's suggestion.|这家店采用网上订位。|This shop uses online reservations.
加强|下周我们加强最后一段的练习。|We'll put more practice into the final section next week.|下雨的时候，工作人员加强检查。|The staff carry out more checks when it rains.
加快|快迟到了，我们加快脚步吧。|We're almost late. Let's walk faster.|这次练习我想加快一点速度。|I'd like to speed up a little in this practice run.
目标|我今年的目标是读完这十本书。|My goal this year is to finish these ten books.|我们的目标是七点到家。|We're aiming to get home at seven.
进展|你的新厨房进展怎么样？|How's the work on your new kitchen going?|今天的练习有了一点进展。|We made a little progress in practice today.
效果|灯关掉一盏，效果更好。|Turning off one light gives a better effect.|这个办法效果不错。|This approach works well.
压力|最近工作压力有点大。|Work's been a little stressful recently.|你别给自己太大压力。|Don't put too much pressure on yourself.
力量|两个人的力量比一个人大。|Two people have more strength than one.|她的鼓励给了我力量。|Her encouragement gave me strength.
决心|他下决心每天早起。|He resolved to get up early every day.|她的决心很大，不肯放弃。|She's determined and won't give up.
把握|这道题我有把握。|I'm confident about this question.|你有把握找到那家店吗？|Are you confident you can find that shop?
成功|蛋糕第一次就做成功了。|The cake turned out right on the first try.|演出很成功，大家都很高兴。|The performance was a success and everyone was happy.
成果|这是大家一个月工作的成果。|This is the result of a month's work by everyone.|展览上能看到学生们的成果。|You can see the students' work at the exhibition.
成就|她在音乐上有很大的成就。|She has significant achievements in music.|完成这件事，让他很有成就感。|Finishing this gave him a strong sense of accomplishment.'''}
