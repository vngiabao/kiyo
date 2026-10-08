"""Ask for practical help and report a small work problem precisely."""
import sys
from advanced_core import write,rows,words,q,card,practice
V=words('''
程序|procedure; computer program|quy trình; chương trình|我们先确认办理程序，再去交材料。|Let’s check the procedure before submitting the documents.|这个程序打开以后一直没反应。|This program hasn’t responded since it opened.
操作|operate; operation|thao tác; vận hành|这个机器怎么操作？|How do you operate this machine?|操作之前，先看一下说明。|Read the instructions before operating it.
产品|product|sản phẩm|这个产品主要给小房间用。|This product is mainly for small rooms.|他们正在改进上一代产品。|They’re improving the previous generation of the product.
测试|test|kiểm tra; thử nghiệm|我们先测试一下新设计。|Let’s test the new design first.|测试结束以后，把结果发给我。|Send me the results after the test.
测量|measure|đo|先测量桌子的宽度。|Measure the width of the table first.|她测量了两次，结果一样。|She measured it twice and got the same result.
承受|bear; withstand|chịu đựng|这个架子承受不了这么重的东西。|This stand can’t hold something so heavy.|他不想一个人承受那么大的压力。|He doesn’t want to bear that much pressure alone.
材料|material; documents|vật liệu; tài liệu|这种材料太薄，我们换一种吧。|This material is too thin; let’s use another.|我把会议材料放在你桌上了。|I’ve put the meeting documents on your desk.
数据|data|dữ liệu|先把这两次的数据放在一起比较。|Put the data from these two trials together to compare.|原来的数据还在，不用重新做。|The original data is still there; no need to redo it.
尺寸|size; dimensions|kích thước|这个盒子的尺寸不对，放不进去。|This box is the wrong size; it won’t fit.|请把门的尺寸发给我。|Please send me the dimensions of the door.
修理|repair|sửa chữa|这把椅子还能修理吗？|Can this chair still be repaired?|修理完以后，先检查一下。|Check it after the repair.
工具|tool|dụng cụ|你用完工具放回原来的地方。|Put the tools back where they were after using them.|我没带工具，今天只能先看看。|I didn’t bring tools, so today I can only take a look.
设备|equipment|thiết bị|这些设备下周才送到。|This equipment won’t arrive until next week.|旧设备还能用，我们先别换。|The old equipment still works; let’s not replace it yet.
指导|guide; guidance|hướng dẫn|老师指导我们做第一次测试。|The teacher guided us through the first test.|谢谢你的指导，我知道怎么改了。|Thanks for your guidance; I know what to change now.
说明|explain; instructions|giải thích; hướng dẫn|你能说明一下为什么要改尺寸吗？|Could you explain why the dimensions need changing?|说明里写着要先打开这个盖子。|The instructions say to open this lid first.
合作|collaborate; cooperation|hợp tác|我们第一次合作，就把任务分清楚了。|We clarified our tasks at the start of our first collaboration.|我很喜欢和她合作，她有问题会直接问。|I like working with her; she asks directly when she has a problem.
方案|plan; proposed approach|phương án|两个方案都可以，我们比较一下费用。|Both plans work; let’s compare their costs.|这个方案还没定，你有意见可以说。|This plan isn’t settled yet; you can share your thoughts.
''')
D=rows('''
你那边做好了吗？我把手机带来了。|Have you finished your part? I’ve brought the phone.
差不多了。不过这个架子一放手机就往后倒。|Almost, but the stand falls backwards as soon as I put the phone on it.
我看看。你是不是只测量了手机的宽度？|Let me see. Did you measure only the width of the phone?
对。尺寸放得下，我就以为没问题了。|Yes. It fit, so I thought it was fine.
放得下是一回事，站不站得住是另一回事。先别改外面的样子。|Fitting is one thing; staying upright is another. Don’t change the appearance yet.
那你帮我拿一下，我把后面这一块加宽。|Then hold it for me while I widen this piece at the back.
好。材料够吗？|Okay. Do we have enough material?
还有一张厚的，够做两个。我们可以先试一个。|There’s one thick sheet left, enough for two. We can try one first.
做完再放手机，看看能不能站住。两次测试的数据都留下。|Put the phone on it after finishing and see whether it stays upright. Keep the data from both tests.
你负责记录，我负责做？|You’ll record it and I’ll make it?
对。要是第二个也不行，我们就换个方案。|Right. If the second one doesn’t work either, we’ll try a different plan.
行。我先把这个扶住，别让你的手机也跟着倒。|Okay. I’ll hold this one steady first so your phone doesn’t fall with it.
''')
R=rows('''
小组要做一个放在桌上的手机架。我负责做，陈宇负责测试和记录。我们一开始只讨论了颜色和外形，觉得好看就够了。|Our group was making a desktop phone stand. I made it, and Chen Yu tested it and recorded results. At first we discussed only colour and shape, thinking appearance was enough.
第一次做完以后，手机放得进去，架子却站不住。我把尺寸写在纸上：前面宽十二厘米，后面只有六厘米。陈宇让我先保留这个设计，再做一个后面更宽的。|The phone fit in the first version, but the stand wouldn’t stay upright. I wrote down the measurements: twelve centimetres wide in front, just six at the back. Chen Yu asked me to keep that version and make another with a wider back.
我们没有同时换材料和尺寸。第二个仍然用同一种厚纸，只把后面的宽度改成十厘米。这样再测试时，比较的条件会少一点。|We didn’t change both material and size at once. The second used the same thick paper, with just the back widened to ten centimetres. That reduced the changes being compared in the next test.
第二个放上这部手机以后能站住了。不过我换了一部更重的手机，它又倒了。陈宇把两次的情况写下来，没有把“这部能用”写成“所有手机都能用”。|The second stood upright with this phone. But when I tried a heavier phone, it fell again. Chen Yu wrote down both results instead of turning “works with this phone” into “works with every phone.”
老师看过以后，让我们把适用的尺寸和重量写清楚，再讨论能不能改成正式产品。我们还没走到那一步，先把这次结果说明白。|After checking it, the teacher asked us to state which dimensions and weight it worked with before discussing a finished product. We weren’t at that stage yet; first we needed a clear account of this trial.
下次合作，我想早点问清楚怎么测试。把问题说得具体一点，比快做一个看起来完成了的东西更有用。|Next time, I want to ask earlier how we’ll test it. Describing the problem specifically is more useful than quickly producing something that merely looks finished.
''')
M=rows('''
你在找什么？|What are you looking for?
尺子。刚才还在桌上，现在没了。|The ruler. It was on the table a moment ago, but now it’s gone.
你手里拿的是什么？|What’s that in your hand?
啊，就是它。我还以为自己拿的是笔。|Oh, that’s it. I thought I was holding a pen.
先喝点水吧。你刚才还问我手机在哪儿，手机就在你面前。|Have some water first. You just asked where the phone was when it was right in front of you.
别说了，今天我负责做，你负责提醒我看眼前。|Enough. Today I’ll make things, and you’ll remind me to look in front of me.
那我的任务可不轻。|That’s quite a job for me.
合作嘛。等会儿请你喝咖啡。|That’s teamwork. I’ll buy you a coffee later.
''')
G=[
card('按照 / 根据','Follow instructions or use evidence','按照 usually describes following a rule, sequence or specification. 根据 introduces the information on which a judgment or action is based. Their uses overlap, so inspect what follows.','按照说明，先打开盖子。|Following the instructions, open the lid first.\n根据测试结果，我们改了尺寸。|We changed the dimensions based on the test results.','根据没有结果，我们已经知道所有情况。','根据这次结果，这部手机放上去能站住。','Keep the claim within what the actual test showed.'),
card('一回事 / 另一回事','Separate two related issues','X是一回事，Y是另一回事 distinguishes criteria that cannot be substituted for each other. This is a discourse frame rather than a technical proof.','放得下是一回事，站得住是另一回事。|Fitting is one thing; staying upright is another.\n认识字是一回事，跟上对话是另一回事。|Knowing the characters is one thing; following dialogue is another.','放得下，所以一定站得住。','放得下是一回事，站得住是另一回事。','The second property does not follow just from the first.'),
card('得 / 不 result potential','Describe whether a result is achievable','Insert 得 or 不 between the verb and a result or direction: 放得下/放不下，站得住/站不住. This differs from 得 before a degree phrase such as 站得很稳.','这个盒子放不下手机。|This box won’t fit the phone.\n这个架子站得住。|This stand can stay upright.','这个盒子放下不手机。','这个盒子放不下手机。','不 goes between the verb and the result/directional complement.'),
card('要是…就…','Offer a conditional fallback','要是 introduces a possible situation in conversational speech; 就 introduces the proposed response. Neither says the condition has already occurred.','要是第二个也不行，我们就换方案。|If the second doesn’t work either, we’ll try a different plan.\n要是材料不够，我就再去买。|If there isn’t enough material, I’ll buy more.','要是第二个也不行，所以它已经坏了。','要是第二个也不行，我们就换方案。','A conditional trial result is not an established failure.'),
]
spec=dict(title=('Tell me what is going wrong','放得下，却站不住'),goals=['Ask a collaborator for one specific action','Describe measurements and distinguish two test results','Propose a conditional next step instead of overstating success'],vocabulary=V,grammar=G,dialogue=(D,[q('gist','What problem are the collaborators solving?','A phone stand that tips backwards','A phone that cannot receive calls','A missing application form'),q('detail','How much thick material remains?','Enough for two stands','None','Exactly twelve sheets'),q('inference','Why keep data from both tests?','To compare the attempts','To claim every phone will fit','To avoid testing the second version')]),reading=(R,[q('gist','What does the team learn?','A fit and one successful trial are not enough to establish every use','Appearance alone proves a product is finished','All failures were caused by phone software'),q('detail','How wide is the back in the second version?','Ten centimetres','Six centimetres','Twelve metres'),q('inference','Why keep the same material in the second attempt?','To change fewer conditions in the comparison','To guarantee every heavy phone works','Because the colour changes automatically')]),mediaTitle='The missing ruler',media=(M,[q('detail','Where is the ruler?','In the speaker’s hand','At the coffee shop','Inside a phone'),q('inference','Why joke that the reminder job is not light?','The friend keeps overlooking things in front of them','The ruler weighs several kilograms','The work has already been cancelled')]),glosses=[('架子','stand; rack'),('外形','appearance; external shape'),('厘米','centimetre'),('重量','weight'),('适用','be suitable for a specific use'),('扶住','hold steady'),('尺子','ruler'),('盖子','lid'),('稳','steady')],place='A small classroom design project',context='Two collaborators test a paper phone stand and keep the measurements.',turns=[('我该先做什么？','What should I do first?','Ask for a bounded measurement',['先测量手机的宽度。']),('现在可以说都能用了吗？','Can we say it works for all phones now?','Limit the claim to the trial',['还不能，我们只测试了这两部手机。']),('要是第二个也不行呢？','What if the second does not work either?','Offer another plan',['我们就换个方案，再试一次。'])],usage=[('Describe a specific failure','手机放得下，但架子站不住。','The phone fits, but the stand will not stay upright.','Separate the observed results instead of saying only 不行.'),('Ask for a single practical action','你帮我扶一下，我来改后面这一块。','Hold this steady for me while I change the back piece.','This gives the helper a concrete action and names your own part.')],tasks=practice([(D[3][0],D[3][1],'The maker initially checked whether the phone fit.',True,'The speaker says it fit and they assumed that was enough.'),(R[3][0],R[3][1],'The second version also worked with the heavier phone.',False,'It tipped over again with the heavier phone.')],[('这个架子一放手机就倒，你能先帮我扶住吗？','This stand tips when I put the phone on it. Can you hold it steady first?',['先扶住，我看看后面这一块。','不用扶，它已经稳稳站住了。','不用看，把这次倒了算成测试成功。'],0,'The reply offers concrete help with the observed problem.'),('你在找尺子，手里已经拿着尺子。拿的是什么？','You are looking for a ruler while holding one. What are you holding?',['啊，就是我在找的尺子。','是手机，尺子还没找到。','是架子，尺子还在包里。'],0,'The reply identifies the supposedly missing ruler.')],[('她测量了两次，结果一样。','She measured twice and got the same result.','测量'),('要是第二个也不行，我们就换方案。','If the second does not work either, we will change plans.','就')],[[(V[i][3],V[i][4]) for i in [0,5,8]],[(V[i][5],V[i][6]) for i in [9,11,14]]]),review='Native review: practical design vocabulary and the ruler banter. Measurements and outcomes checked: back six then ten centimetres; front twelve; heavier phone still tips. This is a fictional learning project, not an engineering certification or a safety instruction.')
spec['glosses'].extend([('宽','wide; width'),('厚','thick'),('薄','thin'),('嘛','particle presenting something as obvious in context')])
write(4,7,spec,publish='--publish' in sys.argv)
