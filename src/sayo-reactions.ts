import type { SayoMood } from "./sayo-voice";

export type ReactionKind =
  "right" | "wrong" | "supported" | "tone" | "saved" | "done" | "levelUp";
export type SayoReaction = {
  kind: ReactionKind;
  mood: SayoMood;
  zh: string;
  py: string;
  en: string;
  rate: number;
  pitchOffset: number;
};

type Row = [string, string, string];
function group(
  kind: ReactionKind,
  mood: SayoMood,
  rows: Row[],
): SayoReaction[] {
  // Lowering by resampling also slows the clip gently; avoid a second time stretch.
  return rows.map(([zh, py, en], i) => ({
    kind,
    mood,
    zh,
    py,
    en,
    rate: 1,
    pitchOffset: [0, -0.25, -0.5][i % 3],
  }));
}

/** Short reactions, never a claim about proficiency or an unmeasured tone. */
export const sayoReactions: SayoReaction[] = [
  ...group("right", "playful", [
    ["哎，对了！", "Āi, duì le!", "Hey, that’s right!"],
    ["这就对了嘛。", "Zhè jiù duì le ma.", "There you go."],
    ["嗯，有点厉害。", "Ńg, yǒudiǎn lìhai.", "Hmm. Pretty good."],
    ["可以啊，你。", "Kěyǐ a, nǐ.", "Look at you."],
    ["嘿，答对了。", "Hēi, dá duì le.", "Hey, you got it."],
    ["这题拿下。", "Zhè tí ná xià.", "That one’s yours."],
    ["好，这个会了。", "Hǎo, zhège huì le.", "Good. You got this one."],
    ["哦，你记得。", "Ó, nǐ jìde.", "Oh, you remembered."],
    ["就这么来。", "Jiù zhème lái.", "Keep doing that."],
    ["好嘛，挺稳。", "Hǎo ma, tǐng wěn.", "Well, that was solid."],
    [
      "这次不用我了。",
      "Zhè cì bú yòng wǒ le.",
      "You didn’t need me this time.",
    ],
    ["有进步嘛。", "Yǒu jìnbù ma.", "Hey, progress."],
    ["好，接住了。", "Hǎo, jiē zhù le.", "Good. You caught it."],
    ["你看，做到了吧。", "Nǐ kàn, zuò dào le ba.", "See? You did it."],
    ["这下记住了。", "Zhè xià jì zhù le.", "Now you’ve got it."],
  ]),
  ...group("right", "deadpan", [
    ["行，有两下子。", "Xíng, yǒu liǎng xiàzi.", "Okay. You’ve got something."],
    ["嗯，我看见了。", "Ńg, wǒ kàn jiàn le.", "Hmm. I saw that."],
    ["不错，真的。", "Bú cuò, zhēn de.", "Not bad. Really."],
    [
      "好吧，夸你一下。",
      "Hǎo ba, kuā nǐ yí xià.",
      "Fine. A little praise for you.",
    ],
    ["别笑，下一题。", "Bié xiào, xià yì tí.", "Don’t grin. Next question."],
    ["嗯，这个漂亮。", "Ńg, zhège piàoliang.", "Hmm. Nicely done."],
    [
      "今天挺认真嘛。",
      "Jīntiān tǐng rènzhēn ma.",
      "Taking this seriously today, huh?",
    ],
    ["好，我没白等。", "Hǎo, wǒ méi bái děng.", "Good. Worth the wait."],
    ["这题过关。", "Zhè tí guò guān.", "This question is cleared."],
    [
      "嗯，放心往下走。",
      "Ńg, fàngxīn wǎng xià zǒu.",
      "Hmm. Go on with confidence.",
    ],
  ]),
  ...group("right", "intense", [
    ["就是这样！", "Jiù shì zhèyàng!", "That’s it!"],
    ["好，继续！", "Hǎo, jìxù!", "Good. Keep going!"],
    ["答得好！", "Dá de hǎo!", "Good answer!"],
    ["这题漂亮！", "Zhè tí piàoliang!", "Beautifully done!"],
    ["行啊！下一题！", "Xíng a! Xià yì tí!", "Nice! Next question!"],
  ]),
  ...group("wrong", "soft", [
    ["没事，慢慢来。", "Méi shì, mànmàn lái.", "It’s okay. Take your time."],
    ["先别急着选。", "Xiān bié jí zhe xuǎn.", "Don’t rush the choice."],
    ["再看一眼就好。", "Zài kàn yì yǎn jiù hǎo.", "Just take another look."],
    [
      "换个思路试试。",
      "Huàn ge sīlù shìshi.",
      "Try another way to think about it.",
    ],
    [
      "这一题再练练。",
      "Zhè yì tí zài liànlian.",
      "Let’s practise this one again.",
    ],
    [
      "先看正确答案。",
      "Xiān kàn zhèngquè dá’àn.",
      "Look at the correct answer first.",
    ],
    [
      "停一下，再想想。",
      "Tíng yí xià, zài xiǎngxiang.",
      "Pause. Think it over.",
    ],
    ["错一次，没关系。", "Cuò yí cì, méi guānxi.", "One mistake is okay."],
    ["我们把它弄清楚。", "Wǒmen bǎ tā nòng qīngchu.", "Let’s get this clear."],
    ["这个容易混。", "Zhège róngyì hùn.", "This one is easy to mix up."],
  ]),
  ...group("wrong", "playful", [
    ["走错路了。", "Zǒu cuò lù le.", "Hey, wrong turn."],
    ["嗯？再瞧瞧。", "Ńg? Zài qiáoqiao.", "Hmm? Look again."],
    [
      "别急，题还在呢。",
      "Bié jí, tí hái zài ne.",
      "Easy. The question isn’t going anywhere.",
    ],
    [
      "这个有点狡猾。",
      "Zhège yǒudiǎn jiǎohuá.",
      "This one is a little sneaky.",
    ],
    ["好，我们重来。", "Hǎo, wǒmen chóng lái.", "Okay. Let’s try again."],
    ["就差那么一点。", "Jiù chà nàme yìdiǎn.", "Hey, just a little off."],
    ["答案在这儿呢。", "Dá’àn zài zhèr ne.", "The answer is right here."],
    [
      "先别和题吵架。",
      "Xiān bié hé tí chǎojià.",
      "Don’t argue with the question yet.",
    ],
    [
      "我们再见它一次。",
      "Wǒmen zài jiàn tā yí cì.",
      "We’ll meet this one again.",
    ],
    [
      "好了，记住这个。",
      "Hǎo le, jì zhù zhège.",
      "All right. Remember this one.",
    ],
  ]),
  ...group("supported", "deadpan", [
    [
      "提示帮忙了，记着哦。",
      "Tíshì bāng máng le, jì zhe o.",
      "The hint helped. Remember that.",
    ],
    [
      "看了提示，也要记住。",
      "Kàn le tíshì, yě yào jì zhù.",
      "You used the hint. Still learn it.",
    ],
    ["下一次，自己来。", "Xià yí cì, zìjǐ lái.", "Next time, on your own."],
    ["这次有帮手。", "Zhè cì yǒu bāngshǒu.", "You had a helper this time."],
    [
      "先记住，再藏起来。",
      "Xiān jì zhù, zài cáng qǐlai.",
      "Learn it, then hide the help.",
    ],
    [
      "提示可以用，别住里面。",
      "Tíshì kěyǐ yòng, bié zhù lǐmiàn.",
      "Use the hints. Don’t move into them.",
    ],
    [
      "现在试着自己记。",
      "Xiànzài shì zhe zìjǐ jì.",
      "Now try remembering it yourself.",
    ],
    [
      "好，下回不偷看。",
      "Hǎo, xià huí bù tōukàn.",
      "Good. No peeking next time.",
    ],
    [
      "这个还要自己练。",
      "Zhège hái yào zìjǐ liàn.",
      "Practise this on your own too.",
    ],
    [
      "帮手先退场。",
      "Bāngshǒu xiān tuì chǎng.",
      "Let’s send the helper offstage.",
    ],
    [
      "字看到了，记住了吗？",
      "Zì kàn dào le, jì zhù le ma?",
      "You saw the characters. Remember them?",
    ],
    [
      "别忘了刚才的提示。",
      "Bié wàng le gāngcái de tíshì.",
      "Remember what the hint showed you.",
    ],
    [
      "再练一次，不看提示。",
      "Zài liàn yí cì, bú kàn tíshì.",
      "Practise once more without the hint.",
    ],
    [
      "答案看过，要收进脑袋。",
      "Dá’àn kàn guo, yào shōu jìn nǎodai.",
      "You saw it. Put it in your head.",
    ],
    [
      "好，提示先放一边。",
      "Hǎo, tíshì xiān fàng yì biān.",
      "Okay. Put the hint aside.",
    ],
  ]),
  ...group("tone", "cool", [
    ["先听声调。", "Xiān tīng shēngdiào.", "Listen to the tone first."],
    [
      "注意声音的走向。",
      "Zhùyì shēngyīn de zǒuxiàng.",
      "Notice where the sound goes.",
    ],
    [
      "再听，不要急。",
      "Zài tīng, bú yào jí.",
      "Listen again. Don’t rush to guess.",
    ],
    [
      "听清楚，再选。",
      "Tīng qīngchu, zài xuǎn.",
      "Listen carefully, then choose.",
    ],
    [
      "把这一声听完。",
      "Bǎ zhè yì shēng tīng wán.",
      "Hear this sound all the way through.",
    ],
    [
      "先听，再跟着说。",
      "Xiān tīng, zài gēn zhe shuō.",
      "Listen, then say it along with me.",
    ],
    [
      "这一声再比较一下。",
      "Zhè yì shēng zài bǐjiào yí xià.",
      "Compare this sound again.",
    ],
    ["别只听开头。", "Bié zhǐ tīng kāitóu.", "Don’t just listen to the start."],
    [
      "慢一点，听完整。",
      "Màn yìdiǎn, tīng wánzhěng.",
      "Slow down. Hear the whole sound.",
    ],
    [
      "声音有区别，找找看。",
      "Shēngyīn yǒu qūbié, zhǎozhao kàn.",
      "The sounds differ. Find how.",
    ],
  ]),
  ...group("saved", "cool", [
    ["好，练过了。", "Hǎo, liàn guo le.", "Okay. You practised it."],
    [
      "先记下这次练习。",
      "Xiān jì xià zhè cì liànxí.",
      "Let’s save this practice.",
    ],
    ["练习留住了。", "Liànxí liú zhù le.", "Your practice is saved."],
    ["好，往下走。", "Hǎo, wǎng xià zǒu.", "Okay. Move on."],
    ["这一步完成了。", "Zhè yí bù wánchéng le.", "This step is done."],
    ["收到，继续吧。", "Shōu dào, jìxù ba.", "Got it. Keep going."],
    ["好，我们接着来。", "Hǎo, wǒmen jiē zhe lái.", "Okay. Let’s carry on."],
    [
      "练过就留个记录。",
      "Liàn guo jiù liú ge jìlù.",
      "Keep a record of the practice.",
    ],
    [
      "这次练习收好了。",
      "Zhè cì liànxí shōu hǎo le.",
      "This practice is saved away.",
    ],
    ["嗯，再走一步。", "Ńg, zài zǒu yí bù.", "Hmm. One more step."],
  ]),
  ...group("done", "playful", [
    [
      "好，今天这一课完成。",
      "Hǎo, jīntiān zhè yí kè wánchéng.",
      "Good. Today’s lesson is done.",
    ],
    [
      "下课了，别全忘了。",
      "Xià kè le, bié quán wàng le.",
      "Class dismissed. Don’t forget everything.",
    ],
    [
      "辛苦了，休息一下。",
      "Xīnkǔ le, xiūxi yí xià.",
      "Good work. Take a little break.",
    ],
    [
      "收工，明天见。",
      "Shōu gōng, míngtiān jiàn.",
      "Done for now. See you tomorrow.",
    ],
    [
      "好，脑袋休息一下。",
      "Hǎo, nǎodai xiūxi yí xià.",
      "Okay. Give your head a break.",
    ],
    ["这一课拿下了。", "Zhè yí kè ná xià le.", "You finished this lesson."],
    [
      "嗯，今天没白来。",
      "Ńg, jīntiān méi bái lái.",
      "Hmm. Today was worth showing up for.",
    ],
    [
      "先歇歇，我也歇歇。",
      "Xiān xiēxie, wǒ yě xiēxie.",
      "Take a break. I’ll take one too.",
    ],
    [
      "学完了，喝点水。",
      "Xué wán le, hē diǎn shuǐ.",
      "Lesson done. Have some water.",
    ],
    [
      "下次来，别装不认识。",
      "Xià cì lái, bié zhuāng bú rènshi.",
      "Next time, don’t pretend we haven’t met.",
    ],
  ]),
  ...group("levelUp", "intense", [
    ["又完成一课！", "Yòu wánchéng yí kè!", "Another lesson finished!"],
    ["好，往前一步！", "Hǎo, wǎng qián yí bù!", "Good. One step forward!"],
    ["新的一课，拿下！", "Xīn de yí kè, ná xià!", "A new lesson, completed!"],
    ["这一步，走到了！", "Zhè yí bù, zǒu dào le!", "You reached this step!"],
    ["行，继续往前！", "Xíng, jìxù wǎng qián!", "Nice. Keep moving forward!"],
  ]),
];

const cursors = new Map<ReactionKind, number>();
const pools = new Map<ReactionKind, SayoReaction[]>();
for (const kind of new Set(sayoReactions.map((r) => r.kind))) {
  const lines = sayoReactions.filter((r) => r.kind === kind);
  const lanes = [...new Set(lines.map((r) => r.mood))].map((mood) =>
    lines.filter((r) => r.mood === mood),
  );
  const pool: SayoReaction[] = [];
  for (let i = 0; i < Math.max(...lanes.map((lane) => lane.length)); i++)
    for (const lane of lanes) if (lane[i]) pool.push(lane[i]);
  pools.set(kind, pool);
}
/** Rotate through every line before repeating, without writing learner data. */
export function nextReaction(kind: ReactionKind): SayoReaction {
  const pool = pools.get(kind)!;
  const cursor = cursors.get(kind) ?? Math.floor(Math.random() * pool.length);
  cursors.set(kind, cursor + 1);
  return pool[cursor % pool.length];
}
