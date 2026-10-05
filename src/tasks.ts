/**
 * Practice tasks for the phrase lessons, in the formats HSK and good
 * textbooks actually use: conversation listening, true/false (判断对错),
 * choose the reply, fill the missing word you hear (听写填空), word-bank
 * fill-in (选词填空) and matching. New words are tested in NEW sentences,
 * after the learner has met them, never straight after their introduction.
 *
 * Blanks are marked with 【】 inside the Chinese; the marked text is the answer.
 * Every Chinese line here is voiced by Sayo (see prompts/voice-task-mapping.md).
 * AI-assisted draft, awaiting native review.
 */
import type { Task, TaskLine } from "./types";

const L = (zh: string, py: string, en: string, speaker?: string): TaskLine => ({ zh, py, en, speaker });

export const lessonTasks: Record<string, Task[]> = {
  first: [
    {
      type: "dialogue", id: "first-d", phrase: "thanks", title: "Before class",
      setting: "Chen Yu hands Lin An a cup of tea before class.",
      lines: [
        L("你好！", "Nǐ hǎo!", "Hello!", "陈宇"),
        L("你好！", "Nǐ hǎo!", "Hi!", "林安"),
        L("谢谢！", "Xièxie!", "Thanks!", "林安"),
        L("好。再见！", "Hǎo. Zàijiàn!", "Okay. Bye!", "陈宇"),
        L("再见！", "Zàijiàn!", "Bye!", "林安"),
      ],
      questions: [
        { kind: "gist", q: "What happens in this exchange?", choices: ["A hello, a thank-you and a goodbye", "An argument", "Ordering food"], answer: "A hello, a thank-you and a goodbye" },
        { kind: "detail", q: "What does Lin An say when she gets the tea?", choices: ["Thank you", "Goodbye", "Hello"], answer: "Thank you" },
        { kind: "inference", q: "Who says goodbye first?", choices: ["Chen Yu", "Lin An", "Nobody leaves"], answer: "Chen Yu" },
      ],
    },
    { type: "truefalse", id: "first-tf1", phrase: "bye", audio: L("再见！", "Zàijiàn!", "Goodbye!"), statement: "The speaker has just arrived.", answer: false, why: "再见 is what you say when leaving." },
    { type: "truefalse", id: "first-tf2", phrase: "thanks", audio: L("谢谢！", "Xièxie!", "Thanks!"), statement: "The speaker is thanking someone.", answer: true, why: "谢谢 means thank you." },
    { type: "reply", id: "first-r1", phrase: "hello", prompt: L("你好！", "Nǐ hǎo!", "Hello!"), choices: ["你好！", "再见！", "谢谢！"], answer: "你好！" },
    { type: "reply", id: "first-r2", phrase: "bye", prompt: L("再见！", "Zàijiàn!", "Bye!"), choices: ["谢谢！", "再见！", "你好！"], answer: "再见！" },
    { type: "listenfill", id: "first-f1", phrase: "thanks", line: L("你好，【谢谢】！", "Nǐ hǎo, xièxie!", "Hi, thanks!"), blankPy: "xièxie" },
    {
      type: "cloze", id: "first-c", phrase: "hello", title: "Fill in the exchange",
      lines: [L("【你好】！", "Nǐ hǎo!", "Hello!", "陈宇"), L("你好！【谢谢】！", "Nǐ hǎo! Xièxie!", "Hi! Thanks!", "林安"), L("好。【再见】！", "Hǎo. Zàijiàn!", "Okay. Bye!", "陈宇")],
      bank: ["你好", "谢谢", "再见", "好"],
    },
  ],

  tones: [
    { type: "truefalse", id: "tones-tf1", phrase: "mother", audio: L("妈", "mā", "mum"), statement: "You hear the high, level tone (mā).", answer: true, why: "妈 mā stays high and level." },
    { type: "truefalse", id: "tones-tf2", phrase: "scold", audio: L("骂", "mà", "scold"), statement: "You hear a rising tone (má).", answer: false, why: "骂 mà falls sharply from high to low." },
    { type: "truefalse", id: "tones-tf3", phrase: "horse", audio: L("马", "mǎ", "horse"), statement: "You hear the low tone (mǎ).", answer: true, why: "马 mǎ stays low." },
    { type: "truefalse", id: "tones-tf4", phrase: "hemp", audio: L("麻", "má", "hemp"), statement: "You hear the falling tone (mà).", answer: false, why: "麻 má rises, like a question." },
  ],

  names: [
    {
      type: "dialogue", id: "names-d", phrase: "namequestion", title: "Name tags",
      setting: "At a language exchange, Chen Yu meets someone new.",
      lines: [
        L("你好！你叫什么名字？", "Nǐ hǎo! Nǐ jiào shénme míngzi?", "Hi! What's your name?", "安娜"),
        L("我叫陈宇。你呢？", "Wǒ jiào Chén Yǔ. Nǐ ne?", "I'm Chen Yu. And you?", "陈宇"),
        L("我叫安娜。", "Wǒ jiào Ānnà.", "I'm Anna.", "安娜"),
        L("安娜，你好！", "Ānnà, nǐ hǎo!", "Hi, Anna!", "陈宇"),
      ],
      questions: [
        { kind: "gist", q: "What are they doing?", choices: ["Introducing themselves", "Saying goodbye", "Asking for directions"], answer: "Introducing themselves" },
        { kind: "detail", q: "What's the man's name?", choices: ["Chen Yu", "Anna", "Lin An"], answer: "Chen Yu" },
        { kind: "intent", q: "What does 你呢 do in his reply?", choices: ["Turns the question back to her", "Asks where she's from", "Says goodbye"], answer: "Turns the question back to her" },
      ],
    },
    { type: "truefalse", id: "names-tf1", phrase: "myname", audio: L("我叫林安。", "Wǒ jiào Lín Ān.", "I'm Lin An."), statement: "The speaker says her name is Lin An.", answer: true, why: "我叫… introduces your name." },
    { type: "truefalse", id: "names-tf2", phrase: "namequestion", audio: L("你叫什么名字？", "Nǐ jiào shénme míngzi?", "What's your name?"), statement: "The speaker is telling you her name.", answer: false, why: "It's a question: she's asking for yours." },
    { type: "reply", id: "names-r1", phrase: "namequestion", prompt: L("你叫什么名字？", "Nǐ jiào shénme míngzi?", "What's your name?"), choices: ["我叫安娜。", "你呢？", "再见！"], answer: "我叫安娜。" },
    { type: "reply", id: "names-r2", phrase: "youquestion", prompt: L("我叫陈宇。你呢？", "Wǒ jiào Chén Yǔ. Nǐ ne?", "I'm Chen Yu. And you?"), choices: ["谢谢！", "我叫林安。", "你好！"], answer: "我叫林安。" },
    { type: "listenfill", id: "names-f1", phrase: "myname", line: L("我【叫】林安。", "Wǒ jiào Lín Ān.", "My name is Lin An."), blankPy: "jiào" },
    { type: "listenfill", id: "names-f2", phrase: "namequestion", line: L("你叫什么【名字】？", "Nǐ jiào shénme míngzi?", "What's your name?"), blankPy: "míngzi" },
    {
      type: "cloze", id: "names-c", phrase: "namequestion", title: "First meeting",
      lines: [
        L("你好！你叫什么【名字】？", "Nǐ hǎo! Nǐ jiào shénme míngzi?", "Hi! What's your name?", "安娜"),
        L("我【叫】陈宇。你【呢】？", "Wǒ jiào Chén Yǔ. Nǐ ne?", "I'm Chen Yu. And you?", "陈宇"),
        L("我叫安娜。", "Wǒ jiào Ānnà.", "I'm Anna.", "安娜"),
      ],
      bank: ["名字", "叫", "呢", "好"],
    },
  ],

  yesno: [
    {
      type: "dialogue", id: "yesno-d", phrase: "notright", title: "Taking the register",
      setting: "The teacher checks a name, then Lin An points at the window and asks if she can open it.",
      lines: [
        L("你叫安娜？", "Nǐ jiào Ānnà?", "You're Anna?", "王老师"),
        L("不对，我叫林安。", "Bú duì, wǒ jiào Lín Ān.", "No, I'm Lin An.", "林安"),
        L("林安，好。", "Lín Ān, hǎo.", "Lin An, okay.", "王老师"),
        L("可以吗？", "Kěyǐ ma?", "Is that okay?", "林安"),
        L("可以。", "Kěyǐ.", "Sure.", "王老师"),
      ],
      questions: [
        { kind: "detail", q: "Is the student called Anna?", choices: ["No, she's Lin An", "Yes", "We aren't told"], answer: "No, she's Lin An" },
        { kind: "detail", q: "Does the teacher say yes to the window?", choices: ["Yes", "No", "She doesn't answer"], answer: "Yes" },
      ],
    },
    { type: "truefalse", id: "yesno-tf1", phrase: "notright", audio: L("不对。", "Bú duì.", "That's not right."), statement: "The speaker agrees with you.", answer: false, why: "不对 means that's not right." },
    { type: "truefalse", id: "yesno-tf2", phrase: "cant", audio: L("不可以。", "Bù kěyǐ.", "Not allowed."), statement: "The speaker says no, it's not allowed.", answer: true, why: "不可以 refuses permission." },
    { type: "reply", id: "yesno-r1", phrase: "yes", prompt: L("你叫林安？", "Nǐ jiào Lín Ān?", "You're Lin An?"), choices: ["对，我叫林安。", "不可以。", "再见！"], answer: "对，我叫林安。" },
    { type: "reply", id: "yesno-r2", phrase: "can", prompt: L("可以吗？", "Kěyǐ ma?", "Is that okay?"), choices: ["你呢？", "可以。", "我叫林安。"], answer: "可以。" },
    { type: "listenfill", id: "yesno-f1", phrase: "notright", line: L("【不】对，我叫林安。", "Bú duì, wǒ jiào Lín Ān.", "No, I'm Lin An."), blankPy: "bú" },
    {
      type: "cloze", id: "yesno-c", phrase: "can", title: "In class",
      lines: [
        L("你叫安娜？", "Nǐ jiào Ānnà?", "You're Anna?", "王老师"),
        L("【不对】，我叫林安。", "Bú duì, wǒ jiào Lín Ān.", "No, I'm Lin An.", "林安"),
        L("【可以】吗？", "Kěyǐ ma?", "Is that okay?", "林安"),
        L("【好】。", "Hǎo.", "Okay.", "王老师"),
      ],
      bank: ["不对", "可以", "好", "谢谢"],
    },
  ],

  rescue: [
    {
      type: "dialogue", id: "rescue-d", phrase: "notunderstand", title: "Too fast",
      setting: "Chen Yu speaks very fast. Anna needs a moment.",
      lines: [
        L("你叫什么名字？", "Nǐ jiào shénme míngzi?", "(very fast) What's your name?", "陈宇"),
        L("我没听懂。慢一点！", "Wǒ méi tīng dǒng. Màn yìdiǎn!", "I didn't catch that. Slower, please!", "安娜"),
        L("你，叫，什么，名字？", "Nǐ, jiào, shénme, míngzi?", "(slowly) What… is… your… name?", "陈宇"),
        L("等一下……我叫安娜！", "Děng yíxià… wǒ jiào Ānnà!", "Wait a sec… I'm Anna!", "安娜"),
      ],
      questions: [
        { kind: "inference", q: "Why does Anna say 我没听懂?", choices: ["She didn't catch what he said", "She doesn't like him", "She wants to leave"], answer: "She didn't catch what he said" },
        { kind: "detail", q: "What does she ask him to do?", choices: ["Speak more slowly", "Say goodbye", "Speak English"], answer: "Speak more slowly" },
        { kind: "intent", q: "What does 等一下 tell us?", choices: ["She needs a moment", "She's leaving", "She's annoyed"], answer: "She needs a moment" },
      ],
    },
    { type: "truefalse", id: "rescue-tf1", phrase: "slow", audio: L("慢一点！", "Màn yìdiǎn!", "A little slower!"), statement: "The speaker wants you to speak faster.", answer: false, why: "慢一点 asks you to slow down." },
    { type: "truefalse", id: "rescue-tf2", phrase: "again", audio: L("可以再说一次吗？", "Kěyǐ zài shuō yí cì ma?", "Could you say that again?"), statement: "The speaker asks you to repeat.", answer: true, why: "再说一次 means say it once more." },
    { type: "reply", id: "rescue-r1", phrase: "notunderstand", prompt: L("你吃饭了吗？", "Nǐ chīfàn le ma?", "(a question you haven't learned yet)"), choices: ["我没听懂。", "对。", "再见！"], answer: "我没听懂。", why: "When you don't understand, say so. It keeps the conversation alive." },
    { type: "reply", id: "rescue-r2", phrase: "wait", prompt: L("等一下！", "Děng yíxià!", "Wait a moment!"), choices: ["不对。", "你呢？", "好。"], answer: "好。" },
    { type: "listenfill", id: "rescue-f1", phrase: "again", line: L("可以【再】说一次吗？", "Kěyǐ zài shuō yí cì ma?", "Could you say that again?"), blankPy: "zài" },
    { type: "listenfill", id: "rescue-f2", phrase: "notunderstand", line: L("我没【听懂】。", "Wǒ méi tīng dǒng.", "I didn't understand."), blankPy: "tīng dǒng" },
    {
      type: "match", id: "rescue-m", phrase: "slow", title: "What would you say?",
      pairs: [
        { left: "You didn't catch it", right: L("我没听懂。", "Wǒ méi tīng dǒng.", "") },
        { left: "They're talking too fast", right: L("慢一点！", "Màn yìdiǎn!", "") },
        { left: "You need a second to think", right: L("等一下。", "Děng yíxià.", "") },
      ],
    },
  ],

  identity: [
    {
      type: "dialogue", id: "identity-d", phrase: "from", title: "After class",
      setting: "Anna and Chen Yu chat after class.",
      lines: [
        L("你是哪国人？", "Nǐ shì nǎ guó rén?", "Where are you from?", "安娜"),
        L("我是中国人。你呢？", "Wǒ shì Zhōngguó rén. Nǐ ne?", "I'm Chinese. And you?", "陈宇"),
        L("我是美国人。", "Wǒ shì Měiguó rén.", "I'm American.", "安娜"),
        L("林安呢？", "Lín Ān ne?", "And Lin An?", "陈宇"),
        L("她是越南人。", "Tā shì Yuènán rén.", "She's Vietnamese.", "安娜"),
      ],
      questions: [
        { kind: "detail", q: "Where is Chen Yu from?", choices: ["China", "The United States", "Vietnam"], answer: "China" },
        { kind: "detail", q: "Where is Lin An from?", choices: ["Vietnam", "China", "The United States"], answer: "Vietnam" },
        { kind: "gist", q: "What are they talking about?", choices: ["Where people are from", "Their names", "Food"], answer: "Where people are from" },
      ],
    },
    { type: "truefalse", id: "identity-tf1", phrase: "vietnam", audio: L("我是越南人。", "Wǒ shì Yuènán rén.", "I'm Vietnamese."), statement: "The speaker is from China.", answer: false, why: "越南 is Vietnam." },
    { type: "truefalse", id: "identity-tf2", phrase: "us", audio: L("她是美国人。", "Tā shì Měiguó rén.", "She's American."), statement: "She's American.", answer: true, why: "美国人 is an American." },
    { type: "reply", id: "identity-r1", phrase: "from", prompt: L("你是哪国人？", "Nǐ shì nǎ guó rén?", "Where are you from?"), choices: ["我叫安娜。", "我是美国人。", "不对。"], answer: "我是美国人。" },
    { type: "reply", id: "identity-r2", phrase: "from", prompt: L("我是中国人。你呢？", "Wǒ shì Zhōngguó rén. Nǐ ne?", "I'm Chinese. And you?"), choices: ["我是越南人。", "再见！", "不可以。"], answer: "我是越南人。" },
    { type: "listenfill", id: "identity-f1", phrase: "from", line: L("你是【哪】国人？", "Nǐ shì nǎ guó rén?", "Where are you from?"), blankPy: "nǎ" },
    { type: "listenfill", id: "identity-f2", phrase: "american", line: L("我是【美国】人。", "Wǒ shì Měiguó rén.", "I'm American."), blankPy: "Měiguó" },
    {
      type: "cloze", id: "identity-c", phrase: "from", title: "Where from?",
      lines: [
        L("你是【哪】国人？", "Nǐ shì nǎ guó rén?", "Where are you from?", "陈宇"),
        L("我是美国人。你【呢】？", "Wǒ shì Měiguó rén. Nǐ ne?", "I'm American. And you?", "安娜"),
        L("我是【中国】人。", "Wǒ shì Zhōngguó rén.", "I'm Chinese.", "陈宇"),
      ],
      bank: ["哪", "呢", "中国", "叫"],
    },
  ],

  language: [
    {
      type: "dialogue", id: "language-d", phrase: "learning", title: "A word she doesn't know",
      setting: "Chen Yu notices Anna studying.",
      lines: [
        L("你在学中文？", "Nǐ zài xué Zhōngwén?", "You're learning Chinese?", "陈宇"),
        L("对，一点。", "Duì, yìdiǎn.", "Yes, a little.", "安娜"),
        L("“加油”，什么意思？", "“Jiāyóu”, shénme yìsi?", "“Jiayou”: what does it mean?", "安娜"),
        L("“Keep going！”", "“Keep going!”", "“Keep going!”", "陈宇"),
      ],
      questions: [
        { kind: "detail", q: "What is Anna learning?", choices: ["Chinese", "English", "Vietnamese"], answer: "Chinese" },
        { kind: "detail", q: "How much does she say she knows?", choices: ["A little", "A lot", "Nothing"], answer: "A little" },
        { kind: "gist", q: "What does Anna ask about?", choices: ["What a word means", "Chen Yu's name", "The time"], answer: "What a word means" },
      ],
    },
    { type: "truefalse", id: "language-tf1", phrase: "know", audio: L("我不知道。", "Wǒ bù zhīdào.", "I don't know."), statement: "The speaker knows the answer.", answer: false, why: "不知道 means don't know." },
    { type: "truefalse", id: "language-tf2", phrase: "meaning", audio: L("什么意思？", "Shénme yìsi?", "What does it mean?"), statement: "The speaker asks what something means.", answer: true, why: "意思 is meaning." },
    { type: "reply", id: "language-r1", phrase: "learning", prompt: L("你在学中文？", "Nǐ zài xué Zhōngwén?", "You're learning Chinese?"), choices: ["对，一点。", "我是美国人。", "再见！"], answer: "对，一点。" },
    { type: "reply", id: "language-r2", phrase: "know", prompt: L("“加油”是什么意思？", "“Jiāyóu” shì shénme yìsi?", "What does “jiayou” mean?"), choices: ["你好！", "我不知道。", "可以。"], answer: "我不知道。" },
    { type: "listenfill", id: "language-f1", phrase: "learning", line: L("我在学【中文】。", "Wǒ zài xué Zhōngwén.", "I'm learning Chinese."), blankPy: "Zhōngwén" },
    { type: "listenfill", id: "language-f2", phrase: "meaning", line: L("什么【意思】？", "Shénme yìsi?", "What does it mean?"), blankPy: "yìsi" },
    {
      type: "match", id: "language-m", phrase: "learning", title: "Match the meaning",
      pairs: [
        { left: "I'm learning Chinese", right: L("我在学中文。", "Wǒ zài xué Zhōngwén.", "") },
        { left: "I don't know", right: L("我不知道。", "Wǒ bù zhīdào.", "") },
        { left: "What does it mean?", right: L("什么意思？", "Shénme yìsi?", "") },
      ],
    },
  ],

  numbers: [
    {
      type: "dialogue", id: "numbers-d", phrase: "howmuch", title: "At a small shop",
      setting: "Anna points at something at a market stall.",
      lines: [
        L("这个多少钱？", "Zhège duōshao qián?", "How much is this?", "安娜"),
        L("十块。", "Shí kuài.", "Ten yuan.", "店员"),
        L("三个多少钱？", "Sān ge duōshao qián?", "How much for three?", "安娜"),
        L("三十。", "Sānshí.", "Thirty.", "店员"),
      ],
      questions: [
        { kind: "detail", q: "How much is one?", choices: ["10 yuan", "3 yuan", "30 yuan"], answer: "10 yuan" },
        { kind: "detail", q: "How many does Anna ask about next?", choices: ["Three", "Two", "Ten"], answer: "Three" },
        { kind: "detail", q: "How much for three?", choices: ["30 yuan", "13 yuan", "3 yuan"], answer: "30 yuan" },
      ],
    },
    { type: "truefalse", id: "numbers-tf1", phrase: "ten", audio: L("十块。", "Shí kuài.", "Ten yuan."), statement: "The price is ten yuan.", answer: true, why: "十 is ten; 块 is the everyday word for yuan." },
    { type: "truefalse", id: "numbers-tf2", phrase: "two", audio: L("二十。", "Èrshí.", "Twenty."), statement: "The number is twelve.", answer: false, why: "二十 is 2 × 10 = twenty. Twelve is 十二." },
    { type: "reply", id: "numbers-r1", phrase: "howmuch", prompt: L("多少钱？", "Duōshao qián?", "How much?"), choices: ["十块。", "你好！", "我叫林安。"], answer: "十块。" },
    { type: "listenfill", id: "numbers-f1", phrase: "howmuch", line: L("【多少】钱？", "Duōshao qián?", "How much?"), blankPy: "duōshao" },
    { type: "listenfill", id: "numbers-f2", phrase: "threeNum", line: L("【三】十块。", "Sānshí kuài.", "Thirty yuan."), blankPy: "sān" },
    {
      type: "match", id: "numbers-m", phrase: "ten", title: "Build the numbers",
      pairs: [
        { left: "20", right: L("二十", "èrshí", "") },
        { left: "12", right: L("十二", "shí'èr", "") },
        { left: "30", right: L("三十", "sānshí", "") },
      ],
    },
  ],

  people: [
    {
      type: "dialogue", id: "people-d", phrase: "myfriend", title: "Introductions",
      setting: "Lin An bumps into Chen Yu at a café, with company.",
      lines: [
        L("陈宇，这是我朋友，安娜。", "Chén Yǔ, zhè shì wǒ péngyou, Ānnà.", "Chen Yu, this is my friend Anna.", "林安"),
        L("你好，安娜！", "Nǐ hǎo, Ānnà!", "Hi, Anna!", "陈宇"),
        L("你好！这是我哥哥。", "Nǐ hǎo! Zhè shì wǒ gēge.", "Hi! This is my older brother.", "安娜"),
        L("你好！我叫陈宇。", "Nǐ hǎo! Wǒ jiào Chén Yǔ.", "Hi! I'm Chen Yu.", "陈宇"),
      ],
      questions: [
        { kind: "detail", q: "Who is Anna to Lin An?", choices: ["Her friend", "Her sister", "Her teacher"], answer: "Her friend" },
        { kind: "detail", q: "Who is with Anna?", choices: ["Her older brother", "Her mum", "Her teacher"], answer: "Her older brother" },
      ],
    },
    { type: "truefalse", id: "people-tf1", phrase: "myfriend", audio: L("这是我朋友。", "Zhè shì wǒ péngyou.", "This is my friend."), statement: "The speaker is introducing a friend.", answer: true, why: "朋友 is friend." },
    { type: "truefalse", id: "people-tf2", phrase: "brother", audio: L("这是我哥哥。", "Zhè shì wǒ gēge.", "This is my older brother."), statement: "This is the speaker's younger brother.", answer: false, why: "哥哥 is an older brother." },
    { type: "reply", id: "people-r1", phrase: "myfriend", prompt: L("这是我朋友，安娜。", "Zhè shì wǒ péngyou, Ānnà.", "This is my friend Anna."), choices: ["不对。", "你好，安娜！", "多少钱？"], answer: "你好，安娜！" },
    { type: "listenfill", id: "people-f1", phrase: "friend", line: L("这是我【朋友】。", "Zhè shì wǒ péngyou.", "This is my friend."), blankPy: "péngyou" },
    { type: "listenfill", id: "people-f2", phrase: "brother", line: L("这是我【哥哥】。", "Zhè shì wǒ gēge.", "This is my older brother."), blankPy: "gēge" },
    {
      type: "cloze", id: "people-c", phrase: "myfriend", title: "At the café",
      lines: [
        L("陈宇，这是我【朋友】，安娜。", "Chén Yǔ, zhè shì wǒ péngyou, Ānnà.", "Chen Yu, this is my friend Anna.", "林安"),
        L("你好！这是我【哥哥】。", "Nǐ hǎo! Zhè shì wǒ gēge.", "Hi! This is my older brother.", "安娜"),
      ],
      bank: ["朋友", "哥哥", "名字"],
    },
  ],

  reactions: [
    {
      type: "dialogue", id: "reactions-d", phrase: "really", title: "A story",
      setting: "Chen Yu bumps into Anna, then tells her about a friend.",
      lines: [
        L("不好意思！", "Bù hǎoyìsi!", "Sorry!", "陈宇"),
        L("没关系。", "Méi guānxi.", "No problem.", "安娜"),
        L("我有一个美国朋友。", "Wǒ yǒu yí ge Měiguó péngyou.", "I have an American friend.", "陈宇"),
        L("然后呢？", "Ránhòu ne?", "And?", "安娜"),
        L("他在学中文，说得很好！", "Tā zài xué Zhōngwén, shuō de hěn hǎo!", "He's learning Chinese, and he speaks it really well!", "陈宇"),
        L("真的假的？", "Zhēn de jiǎ de?", "Seriously?", "安娜"),
      ],
      questions: [
        { kind: "inference", q: "Why does Chen Yu say 不好意思?", choices: ["He bumped into her", "He's thanking her", "He's leaving"], answer: "He bumped into her" },
        { kind: "intent", q: "What does Anna mean by 然后呢?", choices: ["She wants him to go on", "She wants to leave", "She didn't hear"], answer: "She wants him to go on" },
        { kind: "intent", q: "How does Anna react at the end?", choices: ["Surprised", "Angry", "Bored"], answer: "Surprised" },
      ],
    },
    { type: "truefalse", id: "reactions-tf1", phrase: "noproblem", audio: L("没关系。", "Méi guānxi.", "No problem."), statement: "The speaker is upset.", answer: false, why: "没关系 means it's fine." },
    { type: "truefalse", id: "reactions-tf2", phrase: "really", audio: L("真的假的？", "Zhēn de jiǎ de?", "Seriously?"), statement: "The speaker sounds surprised.", answer: true, why: "真的假的 literally asks “true or false?”." },
    { type: "reply", id: "reactions-r1", phrase: "noproblem", prompt: L("不好意思！", "Bù hǎoyìsi!", "Sorry!"), choices: ["没关系。", "然后呢？", "多少钱？"], answer: "没关系。" },
    { type: "reply", id: "reactions-r2", phrase: "then", prompt: L("我有一个中国朋友。", "Wǒ yǒu yí ge Zhōngguó péngyou.", "I have a Chinese friend."), choices: ["没关系。", "再见！", "然后呢？"], answer: "然后呢？" },
    { type: "listenfill", id: "reactions-f1", phrase: "noproblem", line: L("没【关系】。", "Méi guānxi.", "No problem."), blankPy: "guānxi" },
    { type: "listenfill", id: "reactions-f2", phrase: "then", line: L("【然后】呢？", "Ránhòu ne?", "And then?"), blankPy: "ránhòu" },
    {
      type: "match", id: "reactions-m", phrase: "sorry", title: "Match the reaction",
      pairs: [
        { left: "Sorry / excuse me", right: L("不好意思", "bù hǎoyìsi", "") },
        { left: "No problem", right: L("没关系", "méi guānxi", "") },
        { left: "Seriously?", right: L("真的假的", "zhēn de jiǎ de", "") },
      ],
    },
  ],

  meet: [
    {
      type: "dialogue", id: "meet-d", phrase: "namequestion", title: "First day",
      setting: "The first day of a language exchange.",
      lines: [
        L("你好！我叫林安。你叫什么名字？", "Nǐ hǎo! Wǒ jiào Lín Ān. Nǐ jiào shénme míngzi?", "Hi! I'm Lin An. What's your name?", "林安"),
        L("你好！我叫陈宇。", "Nǐ hǎo! Wǒ jiào Chén Yǔ.", "Hi! I'm Chen Yu.", "陈宇"),
        L("陈宇，你是哪国人？", "Chén Yǔ, nǐ shì nǎ guó rén?", "Chen Yu, where are you from?", "林安"),
        L("我是中国人。你呢？", "Wǒ shì Zhōngguó rén. Nǐ ne?", "I'm Chinese. And you?", "陈宇"),
        L("我是越南人。不好意思，我要走了。再见！", "Wǒ shì Yuènán rén. Bù hǎoyìsi, wǒ yào zǒu le. Zàijiàn!", "I'm Vietnamese. Sorry, I have to go. Bye!", "林安"),
        L("再见！", "Zàijiàn!", "Bye!", "陈宇"),
      ],
      questions: [
        { kind: "gist", q: "Who are they?", choices: ["Two people meeting for the first time", "Old friends", "A shopkeeper and a customer"], answer: "Two people meeting for the first time" },
        { kind: "detail", q: "Where is Chen Yu from?", choices: ["China", "Vietnam", "The United States"], answer: "China" },
        { kind: "inference", q: "Why does Lin An say 不好意思 at the end?", choices: ["She has to leave", "She bumped into him", "She forgot his name"], answer: "She has to leave" },
      ],
    },
    { type: "truefalse", id: "meet-tf1", phrase: "myname", audio: L("我叫林安。你叫什么名字？", "Wǒ jiào Lín Ān. Nǐ jiào shénme míngzi?", "I'm Lin An. What's your name?"), statement: "The speaker gives her name and asks for yours.", answer: true, why: "She says 我叫林安, then asks 你叫什么名字." },
    { type: "reply", id: "meet-r1", phrase: "namequestion", prompt: L("你叫什么名字？", "Nǐ jiào shénme míngzi?", "What's your name?"), choices: ["我叫安娜。", "我是中国人。", "再见！"], answer: "我叫安娜。" },
    { type: "listenfill", id: "meet-f1", phrase: "namequestion", line: L("你叫【什么】名字？", "Nǐ jiào shénme míngzi?", "What's your name?"), blankPy: "shénme" },
    {
      type: "match", id: "meet-m", phrase: "namequestion", title: "Question and answer",
      pairs: [
        { left: L("你叫什么名字？", "Nǐ jiào shénme míngzi?", "What's your name?"), right: L("我叫安娜。", "Wǒ jiào Ānnà.", "") },
        { left: L("你是哪国人？", "Nǐ shì nǎ guó rén?", "Where are you from?"), right: L("我是美国人。", "Wǒ shì Měiguó rén.", "") },
        { left: L("不好意思！", "Bù hǎoyìsi!", "Sorry!"), right: L("没关系。", "Méi guānxi.", "") },
      ],
    },
  ],

  personal: [
    {
      type: "dialogue", id: "personal-d", phrase: "student", title: "Getting to know you",
      setting: "Chen Yu chats with Anna in the library café.",
      lines: [
        L("你是学生吗？", "Nǐ shì xuésheng ma?", "Are you a student?", "陈宇"),
        L("对，我是学生。", "Duì, wǒ shì xuésheng.", "Yes, I'm a student.", "安娜"),
        L("你在学什么？", "Nǐ zài xué shénme?", "What are you studying?", "陈宇"),
        L("我在学中文。", "Wǒ zài xué Zhōngwén.", "I'm learning Chinese.", "安娜"),
        L("你是哪国人？", "Nǐ shì nǎ guó rén?", "Where are you from?", "陈宇"),
        L("我是美国人。", "Wǒ shì Měiguó rén.", "I'm American.", "安娜"),
      ],
      questions: [
        { kind: "detail", q: "Is Anna a student?", choices: ["Yes", "No", "We aren't told"], answer: "Yes" },
        { kind: "detail", q: "What is she studying?", choices: ["Chinese", "English", "Vietnamese"], answer: "Chinese" },
        { kind: "detail", q: "Where is she from?", choices: ["The United States", "China", "Vietnam"], answer: "The United States" },
      ],
    },
    { type: "truefalse", id: "personal-tf1", phrase: "student", audio: L("我是学生。", "Wǒ shì xuésheng.", "I'm a student."), statement: "The speaker works at a company.", answer: false, why: "学生 is a student." },
    { type: "truefalse", id: "personal-tf2", phrase: "learning", audio: L("我在学中文。", "Wǒ zài xué Zhōngwén.", "I'm learning Chinese."), statement: "The speaker is learning Chinese.", answer: true, why: "在学中文 = is learning Chinese." },
    { type: "reply", id: "personal-r1", phrase: "student", prompt: L("你是学生吗？", "Nǐ shì xuésheng ma?", "Are you a student?"), choices: ["我叫林安。", "对，我是学生。", "没关系。"], answer: "对，我是学生。" },
    { type: "reply", id: "personal-r2", phrase: "learning", prompt: L("你在学什么？", "Nǐ zài xué shénme?", "What are you studying?"), choices: ["我在学中文。", "我是美国人。", "再见！"], answer: "我在学中文。" },
    { type: "listenfill", id: "personal-f1", phrase: "student", line: L("我是【学生】。", "Wǒ shì xuésheng.", "I'm a student."), blankPy: "xuésheng" },
    {
      type: "cloze", id: "personal-c", phrase: "student", title: "A profile",
      lines: [L("你好！我【叫】安娜。我是美国人，也是【学生】。我在学【中文】。", "Nǐ hǎo! Wǒ jiào Ānnà. Wǒ shì Měiguó rén, yě shì xuésheng. Wǒ zài xué Zhōngwén.", "Hi! I'm Anna. I'm American, and a student. I'm learning Chinese.")],
      bank: ["叫", "学生", "中文", "再见"],
    },
  ],

  friends: [
    {
      type: "dialogue", id: "friends-d", phrase: "brother", title: "Photos",
      setting: "Lin An shows Chen Yu photos on her phone.",
      lines: [
        L("这是我哥哥。", "Zhè shì wǒ gēge.", "This is my older brother.", "林安"),
        L("他也是学生吗？", "Tā yě shì xuésheng ma?", "Is he a student too?", "陈宇"),
        L("对，他在学英文。", "Duì, tā zài xué Yīngwén.", "Yes, he's learning English.", "林安"),
        L("这是你朋友吗？", "Zhè shì nǐ péngyou ma?", "Is this your friend?", "陈宇"),
        L("对，她叫安娜。你呢？你有哥哥吗？", "Duì, tā jiào Ānnà. Nǐ ne? Nǐ yǒu gēge ma?", "Yes, she's Anna. And you? Do you have an older brother?", "林安"),
        L("没有。", "Méiyǒu.", "No.", "陈宇"),
      ],
      questions: [
        { kind: "detail", q: "Who is in the first photo?", choices: ["Her older brother", "Her friend", "Chen Yu"], answer: "Her older brother" },
        { kind: "detail", q: "What is her brother studying?", choices: ["English", "Chinese", "Nothing, he works"], answer: "English" },
        { kind: "detail", q: "Does Chen Yu have an older brother?", choices: ["No", "Yes", "He doesn't say"], answer: "No" },
      ],
    },
    { type: "truefalse", id: "friends-tf1", phrase: "myfriend", audio: L("这是我朋友。", "Zhè shì wǒ péngyou.", "This is my friend."), statement: "This is the speaker's brother.", answer: false, why: "朋友 is a friend, not family." },
    { type: "reply", id: "friends-r1", phrase: "myfriend", prompt: L("这是你朋友吗？", "Zhè shì nǐ péngyou ma?", "Is this your friend?"), choices: ["没关系。", "对，她叫安娜。", "多少钱？"], answer: "对，她叫安娜。" },
    { type: "listenfill", id: "friends-f1", phrase: "brother", line: L("你有【哥哥】吗？", "Nǐ yǒu gēge ma?", "Do you have an older brother?"), blankPy: "gēge" },
    {
      type: "match", id: "friends-m", phrase: "family", title: "People in your life",
      pairs: [
        { left: "Friend", right: L("朋友", "péngyou", "") },
        { left: "Family", right: L("家人", "jiārén", "") },
        { left: "Older brother", right: L("哥哥", "gēge", "") },
      ],
    },
  ],

  plans: [
    {
      type: "dialogue", id: "plans-d", phrase: "tomorrow", title: "Study session",
      setting: "Chen Yu wants to study together.",
      lines: [
        L("明天你有空吗？", "Míngtiān nǐ yǒu kòng ma?", "Are you free tomorrow?", "陈宇"),
        L("有空。几点？", "Yǒu kòng. Jǐ diǎn?", "I am. What time?", "林安"),
        L("三点，可以吗？", "Sān diǎn, kěyǐ ma?", "Three o'clock, okay?", "陈宇"),
        L("可以。明天见！", "Kěyǐ. Míngtiān jiàn!", "Sure. See you tomorrow!", "林安"),
      ],
      questions: [
        { kind: "detail", q: "When will they meet?", choices: ["Tomorrow at three", "Today at three", "Tomorrow at ten"], answer: "Tomorrow at three" },
        { kind: "detail", q: "Is Lin An free?", choices: ["Yes", "No", "She doesn't know"], answer: "Yes" },
        { kind: "gist", q: "What are they doing?", choices: ["Making a plan", "Ordering food", "Saying sorry"], answer: "Making a plan" },
      ],
    },
    { type: "truefalse", id: "plans-tf1", phrase: "today", audio: L("今天三点。", "Jīntiān sān diǎn.", "Today at three."), statement: "The time is three o'clock tomorrow.", answer: false, why: "今天 is today; tomorrow is 明天." },
    { type: "truefalse", id: "plans-tf2", phrase: "tomorrowsee", audio: L("明天见！", "Míngtiān jiàn!", "See you tomorrow!"), statement: "See you tomorrow.", answer: true, why: "明天见 = see you tomorrow." },
    { type: "reply", id: "plans-r1", phrase: "when", prompt: L("几点？", "Jǐ diǎn?", "What time?"), choices: ["三点。", "明天见！", "对。"], answer: "三点。" },
    { type: "reply", id: "plans-r2", phrase: "three", prompt: L("三点，可以吗？", "Sān diǎn, kěyǐ ma?", "Three o'clock, okay?"), choices: ["几点？", "可以。", "我是学生。"], answer: "可以。" },
    { type: "listenfill", id: "plans-f1", phrase: "when", line: L("【几】点？", "Jǐ diǎn?", "What time?"), blankPy: "jǐ" },
    { type: "listenfill", id: "plans-f2", phrase: "tomorrowsee", line: L("【明天】见！", "Míngtiān jiàn!", "See you tomorrow!"), blankPy: "míngtiān" },
    {
      type: "cloze", id: "plans-c", phrase: "tomorrow", title: "Making the plan",
      lines: [
        L("【明天】你有空吗？", "Míngtiān nǐ yǒu kòng ma?", "Are you free tomorrow?", "陈宇"),
        L("有空。【几】点？", "Yǒu kòng. Jǐ diǎn?", "I am. What time?", "林安"),
        L("【三】点。", "Sān diǎn.", "Three.", "陈宇"),
      ],
      bank: ["明天", "几", "三", "再见"],
    },
  ],

  coffee: [
    {
      type: "dialogue", id: "coffee-d", phrase: "wanttea", title: "At the counter",
      setting: "Anna and Chen Yu order at a café.",
      lines: [
        L("你好！你想喝什么？", "Nǐ hǎo! Nǐ xiǎng hē shénme?", "Hi! What would you like to drink?", "服务员"),
        L("我想喝茶。", "Wǒ xiǎng hē chá.", "I'd like tea.", "安娜"),
        L("好。你呢？", "Hǎo. Nǐ ne?", "Okay. And you?", "服务员"),
        L("我想喝咖啡。", "Wǒ xiǎng hē kāfēi.", "I'd like coffee.", "陈宇"),
        L("还有一杯水，谢谢。", "Hái yǒu yì bēi shuǐ, xièxie.", "And a glass of water, thanks.", "安娜"),
      ],
      questions: [
        { kind: "detail", q: "What does Anna order first?", choices: ["Tea", "Coffee", "Water"], answer: "Tea" },
        { kind: "detail", q: "What does Chen Yu want?", choices: ["Coffee", "Tea", "Water"], answer: "Coffee" },
        { kind: "detail", q: "What else do they ask for?", choices: ["A glass of water", "A second tea", "Nothing"], answer: "A glass of water" },
      ],
    },
    { type: "truefalse", id: "coffee-tf1", phrase: "coffee", audio: L("我想喝咖啡。", "Wǒ xiǎng hē kāfēi.", "I'd like coffee."), statement: "The speaker wants tea.", answer: false, why: "咖啡 is coffee; tea is 茶." },
    { type: "truefalse", id: "coffee-tf2", phrase: "cup", audio: L("一杯水，谢谢。", "Yì bēi shuǐ, xièxie.", "A glass of water, thanks."), statement: "The speaker asks for water.", answer: true, why: "水 is water." },
    { type: "reply", id: "coffee-r1", phrase: "wanttea", prompt: L("你想喝什么？", "Nǐ xiǎng hē shénme?", "What would you like to drink?"), choices: ["我想喝茶。", "三点。", "没关系。"], answer: "我想喝茶。" },
    { type: "listenfill", id: "coffee-f1", phrase: "coffee", line: L("我想喝【咖啡】。", "Wǒ xiǎng hē kāfēi.", "I'd like coffee."), blankPy: "kāfēi" },
    { type: "listenfill", id: "coffee-f2", phrase: "water", line: L("一杯【水】。", "Yì bēi shuǐ.", "A glass of water."), blankPy: "shuǐ" },
    {
      type: "cloze", id: "coffee-c", phrase: "cup", title: "Your order",
      lines: [L("我想【喝】茶，还有一【杯】水。", "Wǒ xiǎng hē chá, hái yǒu yì bēi shuǐ.", "I'd like tea, and a glass of water.")],
      bank: ["喝", "杯", "吃", "个"],
    },
  ],

  food: [
    {
      type: "dialogue", id: "food-d", phrase: "bill", title: "Dinner",
      setting: "Lin An and Chen Yu have dinner at a small restaurant.",
      lines: [
        L("服务员，菜单，谢谢！", "Fúwùyuán, càidān, xièxie!", "Excuse me, the menu, please!", "林安"),
        L("好的。", "Hǎo de.", "Sure.", "服务员"),
        L("很好吃！", "Hěn hǎochī!", "This is really good!", "陈宇"),
        L("对！服务员，买单！", "Duì! Fúwùyuán, mǎidān!", "It is! Excuse me, the bill, please!", "林安"),
      ],
      questions: [
        { kind: "detail", q: "What does Lin An ask for first?", choices: ["The menu", "The bill", "Water"], answer: "The menu" },
        { kind: "detail", q: "What does Chen Yu think of the food?", choices: ["It's good", "It's bad", "It's too much"], answer: "It's good" },
        { kind: "gist", q: "What happens at the end?", choices: ["They ask for the bill", "They order more", "They leave without paying"], answer: "They ask for the bill" },
      ],
    },
    { type: "truefalse", id: "food-tf1", phrase: "bill", audio: L("买单！", "Mǎidān!", "The bill, please!"), statement: "The speaker wants to pay.", answer: true, why: "买单 asks for the bill." },
    { type: "truefalse", id: "food-tf2", phrase: "tasty", audio: L("很好吃！", "Hěn hǎochī!", "Really tasty!"), statement: "The speaker doesn't like the food.", answer: false, why: "好吃 means it tastes good." },
    { type: "reply", id: "food-r1", phrase: "tasty", prompt: L("好吃吗？", "Hǎochī ma?", "Is it good?"), choices: ["买单！", "很好吃！", "我想喝茶。"], answer: "很好吃！" },
    { type: "listenfill", id: "food-f1", phrase: "bill", line: L("服务员，【买单】！", "Fúwùyuán, mǎidān!", "Excuse me, the bill!"), blankPy: "mǎidān" },
    { type: "listenfill", id: "food-f2", phrase: "tasty", line: L("很【好吃】！", "Hěn hǎochī!", "Really tasty!"), blankPy: "hǎochī" },
    {
      type: "match", id: "food-m", phrase: "menu", title: "At the table",
      pairs: [
        { left: "The menu", right: L("菜单", "càidān", "") },
        { left: "The bill, please", right: L("买单", "mǎidān", "") },
        { left: "It tastes good", right: L("很好吃", "hěn hǎochī", "") },
      ],
    },
  ],

  directions: [
    {
      type: "dialogue", id: "directions-d", phrase: "where", title: "Which way?",
      setting: "Anna asks a passer-by for the metro.",
      lines: [
        L("不好意思，地铁站在哪儿？", "Bù hǎoyìsi, dìtiězhàn zài nǎr?", "Excuse me, where's the metro station?", "安娜"),
        L("一直走，然后在左边。", "Yìzhí zǒu, ránhòu zài zuǒbian.", "Go straight, then it's on the left.", "路人"),
        L("左边？", "Zuǒbian?", "On the left?", "安娜"),
        L("对，左边。", "Duì, zuǒbian.", "Yes, the left.", "路人"),
        L("谢谢！", "Xièxie!", "Thanks!", "安娜"),
      ],
      questions: [
        { kind: "gist", q: "What is Anna looking for?", choices: ["The metro station", "A café", "A restaurant"], answer: "The metro station" },
        { kind: "detail", q: "Which side is it on?", choices: ["Left", "Right", "Behind her"], answer: "Left" },
        { kind: "detail", q: "What should she do first?", choices: ["Go straight", "Turn right", "Go back"], answer: "Go straight" },
      ],
    },
    { type: "truefalse", id: "directions-tf1", phrase: "right", audio: L("在右边。", "Zài yòubian.", "It's on the right."), statement: "It's on the left.", answer: false, why: "右边 is right; left is 左边." },
    { type: "truefalse", id: "directions-tf2", phrase: "straight", audio: L("一直走。", "Yìzhí zǒu.", "Go straight."), statement: "Keep going straight.", answer: true, why: "一直走 = keep going straight." },
    { type: "reply", id: "directions-r1", phrase: "where", prompt: L("地铁站在哪儿？", "Dìtiězhàn zài nǎr?", "Where's the metro station?"), choices: ["很好吃！", "一直走。", "三点。"], answer: "一直走。" },
    { type: "listenfill", id: "directions-f1", phrase: "where", line: L("地铁站【在哪儿】？", "Dìtiězhàn zài nǎr?", "Where's the metro station?"), blankPy: "zài nǎr" },
    { type: "listenfill", id: "directions-f2", phrase: "left", line: L("在【左边】。", "Zài zuǒbian.", "On the left."), blankPy: "zuǒbian" },
    {
      type: "cloze", id: "directions-c", phrase: "station", title: "Directions",
      lines: [L("一直【走】，地铁站在【右边】。", "Yìzhí zǒu, dìtiězhàn zài yòubian.", "Go straight; the metro station is on the right.")],
      bank: ["走", "右边", "吃", "哪儿"],
    },
  ],

  hobbies: [
    {
      type: "dialogue", id: "hobbies-d", phrase: "whatlike", title: "Free time",
      setting: "Chen Yu and Anna talk about what they like.",
      lines: [
        L("你喜欢做什么？", "Nǐ xǐhuan zuò shénme?", "What do you like doing?", "陈宇"),
        L("我喜欢看电影。你呢？", "Wǒ xǐhuan kàn diànyǐng. Nǐ ne?", "I like watching films. You?", "安娜"),
        L("我喜欢打篮球，也喜欢音乐。", "Wǒ xǐhuan dǎ lánqiú, yě xǐhuan yīnyuè.", "I like basketball, and music too.", "陈宇"),
        L("真的假的？我也喜欢音乐！", "Zhēn de jiǎ de? Wǒ yě xǐhuan yīnyuè!", "Really? I like music too!", "安娜"),
      ],
      questions: [
        { kind: "detail", q: "What does Anna like?", choices: ["Films", "Basketball", "Cooking"], answer: "Films" },
        { kind: "inference", q: "What do they both like?", choices: ["Music", "Films", "Basketball"], answer: "Music" },
        { kind: "intent", q: "How does Anna feel at the end?", choices: ["Happily surprised", "Bored", "Annoyed"], answer: "Happily surprised" },
      ],
    },
    { type: "truefalse", id: "hobbies-tf1", phrase: "sport", audio: L("我喜欢打篮球。", "Wǒ xǐhuan dǎ lánqiú.", "I like playing basketball."), statement: "The speaker likes watching films.", answer: false, why: "打篮球 is playing basketball." },
    { type: "truefalse", id: "hobbies-tf2", phrase: "music", audio: L("我也喜欢音乐。", "Wǒ yě xǐhuan yīnyuè.", "I like music too."), statement: "The speaker likes music too.", answer: true, why: "也 = also; 音乐 = music." },
    { type: "reply", id: "hobbies-r1", phrase: "whatlike", prompt: L("你喜欢做什么？", "Nǐ xǐhuan zuò shénme?", "What do you like doing?"), choices: ["地铁站在左边。", "我喜欢看电影。", "买单！"], answer: "我喜欢看电影。" },
    { type: "listenfill", id: "hobbies-f1", phrase: "movies", line: L("我喜欢【看电影】。", "Wǒ xǐhuan kàn diànyǐng.", "I like watching films."), blankPy: "kàn diànyǐng" },
    { type: "listenfill", id: "hobbies-f2", phrase: "music", line: L("我也喜欢【音乐】。", "Wǒ yě xǐhuan yīnyuè.", "I like music too."), blankPy: "yīnyuè" },
    {
      type: "match", id: "hobbies-m", phrase: "like", title: "Hobbies",
      pairs: [
        { left: "Music", right: L("音乐", "yīnyuè", "") },
        { left: "Watch a film", right: L("看电影", "kàn diànyǐng", "") },
        { left: "Play basketball", right: L("打篮球", "dǎ lánqiú", "") },
      ],
    },
  ],

  routine: [
    {
      type: "dialogue", id: "routine-d", phrase: "busy", title: "After work",
      setting: "Lin An calls Chen Yu in the afternoon.",
      lines: [
        L("你在上班吗？", "Nǐ zài shàngbān ma?", "Are you at work?", "林安"),
        L("对，今天有点忙。", "Duì, jīntiān yǒudiǎn máng.", "Yes, it's a bit busy today.", "陈宇"),
        L("几点回家？", "Jǐ diǎn huí jiā?", "What time are you going home?", "林安"),
        L("我觉得……七点吧。", "Wǒ juéde… qī diǎn ba.", "I think… about seven.", "陈宇"),
        L("好，回家吃饭吧！", "Hǎo, huí jiā chīfàn ba!", "Okay, come home and eat!", "林安"),
      ],
      questions: [
        { kind: "detail", q: "Where is Chen Yu?", choices: ["At work", "At home", "At the metro"], answer: "At work" },
        { kind: "detail", q: "How is his day?", choices: ["A bit busy", "Relaxed", "Terrible"], answer: "A bit busy" },
        { kind: "detail", q: "When will he go home?", choices: ["Around seven", "At three", "Tomorrow"], answer: "Around seven" },
      ],
    },
    { type: "truefalse", id: "routine-tf1", phrase: "busy", audio: L("我有点忙。", "Wǒ yǒudiǎn máng.", "I'm a bit busy."), statement: "The speaker is free right now.", answer: false, why: "有点忙 = a bit busy." },
    { type: "truefalse", id: "routine-tf2", phrase: "home", audio: L("我回家吃饭。", "Wǒ huí jiā chīfàn.", "I'm going home to eat."), statement: "The speaker is going home to eat.", answer: true, why: "回家 = go home; 吃饭 = eat." },
    { type: "reply", id: "routine-r1", phrase: "busy", prompt: L("你忙吗？", "Nǐ máng ma?", "Are you busy?"), choices: ["很好吃！", "一直走。", "有点忙。"], answer: "有点忙。" },
    { type: "listenfill", id: "routine-f1", phrase: "busy", line: L("今天有点【忙】。", "Jīntiān yǒudiǎn máng.", "It's a bit busy today."), blankPy: "máng" },
    { type: "listenfill", id: "routine-f2", phrase: "home", line: L("几点【回家】？", "Jǐ diǎn huí jiā?", "What time are you going home?"), blankPy: "huí jiā" },
    {
      type: "cloze", id: "routine-c", phrase: "ithink", title: "My day",
      lines: [L("我今天【上班】，有点【忙】。我【觉得】七点回家。", "Wǒ jīntiān shàngbān, yǒudiǎn máng. Wǒ juéde qī diǎn huí jiā.", "I'm at work today, a bit busy. I think I'll be home at seven.")],
      bank: ["上班", "忙", "觉得", "好吃"],
    },
  ],

  weekend: [
    {
      type: "dialogue", id: "weekend-d", phrase: "letscoffee", title: "Weekend plans",
      setting: "Lin An messages Anna on Friday.",
      lines: [
        L("周末你有空吗？", "Zhōumò nǐ yǒu kòng ma?", "Are you free this weekend?", "林安"),
        L("有空！", "Yǒu kòng!", "I am!", "安娜"),
        L("一起喝咖啡吧？", "Yìqǐ hē kāfēi ba?", "Coffee together?", "林安"),
        L("好啊！几点？", "Hǎo a! Jǐ diǎn?", "Sure! What time?", "安娜"),
        L("三点，地铁站见。", "Sān diǎn, dìtiězhàn jiàn.", "Three, see you at the metro station.", "林安"),
      ],
      questions: [
        { kind: "detail", q: "When are they meeting?", choices: ["At the weekend, at three", "Tomorrow at ten", "Today"], answer: "At the weekend, at three" },
        { kind: "detail", q: "Where will they meet?", choices: ["At the metro station", "At a café", "At home"], answer: "At the metro station" },
        { kind: "intent", q: "How does Anna feel about the plan?", choices: ["Happy to go", "Unsure", "She says no"], answer: "Happy to go" },
      ],
    },
    { type: "truefalse", id: "weekend-tf1", phrase: "free", audio: L("周末我没空。", "Zhōumò wǒ méi kòng.", "I'm not free this weekend."), statement: "The speaker is free this weekend.", answer: false, why: "没空 = not free." },
    { type: "truefalse", id: "weekend-tf2", phrase: "letscoffee", audio: L("一起喝咖啡吧！", "Yìqǐ hē kāfēi ba!", "Let's have coffee together!"), statement: "The speaker suggests coffee together.", answer: true, why: "吧 makes it a suggestion." },
    { type: "reply", id: "weekend-r1", phrase: "okay", prompt: L("一起喝咖啡吧？", "Yìqǐ hē kāfēi ba?", "Coffee together?"), choices: ["好啊！", "不好意思！", "多少钱？"], answer: "好啊！" },
    { type: "reply", id: "weekend-r2", phrase: "free", prompt: L("周末你有空吗？", "Zhōumò nǐ yǒu kòng ma?", "Are you free this weekend?"), choices: ["很好吃！", "有空！", "三点。"], answer: "有空！" },
    { type: "listenfill", id: "weekend-f1", phrase: "weekend", line: L("【周末】你有空吗？", "Zhōumò nǐ yǒu kòng ma?", "Are you free this weekend?"), blankPy: "zhōumò" },
    { type: "listenfill", id: "weekend-f2", phrase: "together", line: L("【一起】喝咖啡吧！", "Yìqǐ hē kāfēi ba!", "Let's have coffee together!"), blankPy: "yìqǐ" },
    {
      type: "cloze", id: "weekend-c", phrase: "letscoffee", title: "The message",
      lines: [
        L("周末你【有空】吗？", "Zhōumò nǐ yǒu kòng ma?", "Are you free this weekend?", "林安"),
        L("有空！", "Yǒu kòng!", "I am!", "安娜"),
        L("【一起】喝咖啡【吧】？", "Yìqǐ hē kāfēi ba?", "Coffee together?", "林安"),
      ],
      bank: ["有空", "一起", "吧", "很"],
    },
  ],
};

/** Blanks marked with 【】 → their answers, in order. */
export const blanksOf = (zh: string) => [...zh.matchAll(/【([^】]+)】/g)].map((m) => m[1]);
/** The sentence with its blanks removed, as shown before answering. */
export const withGaps = (zh: string) => zh.replace(/【[^】]+】/g, "＿＿");
/** The full sentence for audio and the transcript. */
export const plain = (zh: string) => zh.replace(/[【】]/g, "");

/** Toneless, spaceless pinyin: "xiè xie", "xie4xie" and "xiexie" all compare equal. */
export const barePinyin = (s: string) =>
  s.normalize("NFD").toLowerCase().replace(/[̀-ͯ]/g, "").replace(/v/g, "u").replace(/[^a-z]/g, "");
/** A typed fill-in counts if it's the hanzi, or the pinyin with or without tones. */
export function fillMatches(input: string, blank: string, blankPy: string) {
  const typed = input.replace(/[\s，。！？、,.!?]/g, "");
  if (!typed) return false;
  if (typed === blank) return true;
  return /[a-z]/i.test(typed) && barePinyin(typed) === barePinyin(blankPy);
}
/** Speakers in order of first appearance; Sayo voices each with her own mood. */
export const speakersOf = (lines: TaskLine[]) => [...new Set(lines.map((l) => l.speaker ?? ""))];
/** Every Chinese line a task plays or shows, with the mood Sayo should voice it in. */
export function taskAudio(t: Task): { zh: string; py: string; en: string; mood: "clear" | "cool" | "playful" | "soft"; role: string }[] {
  const moods = ["cool", "playful", "soft"] as const;
  switch (t.type) {
    case "dialogue": {
      const who = speakersOf(t.lines);
      return t.lines.map((l) => ({ zh: plain(l.zh), py: l.py, en: l.en, mood: moods[who.indexOf(l.speaker ?? "") % 3], role: `dialogue:${l.speaker ?? ""}` }));
    }
    case "truefalse":
      return [{ ...t.audio, zh: plain(t.audio.zh), mood: "clear", role: "truefalse" }];
    case "reply":
      return [{ ...t.prompt, zh: plain(t.prompt.zh), mood: "clear", role: "reply-prompt" }, ...t.choices.map((c) => ({ zh: c, py: "", en: "", mood: "clear" as const, role: "reply-choice" }))];
    case "listenfill":
      return [{ ...t.line, zh: plain(t.line.zh), mood: "clear", role: "listenfill" }];
    case "cloze":
      return t.lines.map((l) => ({ zh: plain(l.zh), py: l.py, en: l.en, mood: "clear" as const, role: "cloze" }));
    case "match":
      return t.pairs.flatMap((p) => [...(typeof p.left === "string" ? [] : [p.left]), p.right]).map((l) => ({ zh: plain(l.zh), py: l.py, en: l.en, mood: "clear" as const, role: "match" }));
  }
}

/** Content gate for one task. Returns problems; empty means it passes. */
export function checkTask(t: Task, phraseIds?: Set<string>): string[] {
  const errs: string[] = [];
  const at = `task ${t.id}`;
  const line = (l: TaskLine, where: string) => {
    if (!l.zh?.trim()) errs.push(`${at}: ${where} has no Chinese.`);
    if (!l.py?.trim()) errs.push(`${at}: ${where} has no pinyin.`);
  };
  const unique = (xs: string[]) => new Set(xs).size === xs.length;
  if (phraseIds && !phraseIds.has(t.phrase)) errs.push(`${at}: phrase "${t.phrase}" is not taught in this lesson.`);
  switch (t.type) {
    case "dialogue":
      if (t.lines.length < 2) errs.push(`${at}: a conversation needs at least two lines.`);
      t.lines.forEach((l, i) => {
        line(l, `line ${i + 1}`);
        if (!l.speaker) errs.push(`${at}: line ${i + 1} has no speaker.`);
      });
      if (!t.questions.length) errs.push(`${at}: needs at least one question.`);
      t.questions.forEach((q, i) => {
        if (!q.choices.includes(q.answer)) errs.push(`${at}: question ${i + 1}'s answer is not one of its choices.`);
        if (q.choices.length < 3 || !unique(q.choices)) errs.push(`${at}: question ${i + 1} needs three different choices.`);
      });
      break;
    case "truefalse":
      line(t.audio, "audio");
      if (!t.statement.trim() || !t.why.trim()) errs.push(`${at}: statement and explanation are required.`);
      break;
    case "reply":
      line(t.prompt, "prompt");
      if (!t.choices.includes(t.answer)) errs.push(`${at}: the answer is not one of the choices.`);
      if (t.choices.length < 3 || !unique(t.choices)) errs.push(`${at}: needs three different replies.`);
      break;
    case "listenfill": {
      line(t.line, "line");
      const b = blanksOf(t.line.zh);
      if (b.length !== 1) errs.push(`${at}: mark exactly one 【blank】.`);
      if (!t.blankPy.trim()) errs.push(`${at}: blankPy is required.`);
      else if (b[0] && !barePinyin(t.line.py).includes(barePinyin(t.blankPy))) errs.push(`${at}: blankPy "${t.blankPy}" is not in the line's pinyin.`);
      break;
    }
    case "cloze": {
      t.lines.forEach((l, i) => line(l, `line ${i + 1}`));
      const b = t.lines.flatMap((l) => blanksOf(l.zh));
      if (!b.length) errs.push(`${at}: mark at least one 【blank】.`);
      if (!unique(t.bank)) errs.push(`${at}: the word bank has duplicates.`);
      if (!unique(b)) errs.push(`${at}: two blanks share an answer; make each blank unique.`);
      for (const x of b) if (!t.bank.includes(x)) errs.push(`${at}: "${x}" is missing from the word bank.`);
      if (t.bank.length <= b.length) errs.push(`${at}: add at least one distractor to the word bank.`);
      break;
    }
    case "match":
      if (t.pairs.length < 3) errs.push(`${at}: match needs at least three pairs.`);
      t.pairs.forEach((p, i) => line(p.right, `pair ${i + 1}`));
      if (!unique(t.pairs.map((p) => plain(p.right.zh)))) errs.push(`${at}: two pairs share the same right side.`);
      break;
  }
  return errs;
}
