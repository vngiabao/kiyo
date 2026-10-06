import type { Lesson, Phrase, Provenance } from "./types";
import { compiledPacks } from "./pack-content";

// Characters-first reading track. Original teaching text; decompositions follow
// standard modern descriptions. "origin" notes describe widely accepted early
// forms; "memory aid" and "traditional explanation" are labelled as such so a
// learner never mistakes a mnemonic for etymology. Awaiting educator review.
const provenance: Provenance = {
  status: "AI-assisted draft",
  author: "Tingjian original seed",
  reviewer: null,
  version: 1,
  sources: ["Unicode Unihan", "CC-CEDICT (reference)", "Make Me a Hanzi (stroke data)"],
  lastReviewed: null,
};

export type ComponentRole = "whole" | "meaning" | "sound" | "shape";
export interface CharPart {
  form: string;
  role: ComponentRole;
  gloss: string;
}
export interface CharWord {
  w: string;
  p: string;
  m: string;
}
export interface HanziEntry extends Phrase {
  strokes: number;
  parts: CharPart[];
  note: string;
  noteKind: "origin" | "memory aid" | "traditional explanation" | "usage";
  words: CharWord[];
  /** Text spoken for audio; particles are voiced inside a word. */
  say: string;
}

type Row = [
  hanzi: string,
  pinyin: string,
  tone: number,
  meaning: string,
  vi: string,
  strokes: number,
  parts: CharPart[],
  noteKind: HanziEntry["noteKind"],
  note: string,
  words: CharWord[],
  traditional?: string,
  say?: string,
];
const whole = (gloss: string): CharPart[] => [{ form: "", role: "whole", gloss }];
const m = (form: string, gloss: string): CharPart => ({ form, role: "meaning", gloss });
const s = (form: string, gloss: string): CharPart => ({ form, role: "sound", gloss });
const sh = (form: string, gloss: string): CharPart => ({ form, role: "shape", gloss });
const w = (word: string, p: string, meaning: string): CharWord => ({ w: word, p, m: meaning });

const rows: Row[] = [
  // r1 · pictures
  ["人", "rén", 2, "person", "người", 2, whole("a person, seen from the side"), "origin", "Early forms show a standing figure in profile. Two strokes, leaning on each other.", [w("中国人", "Zhōngguó rén", "Chinese person"), w("美国人", "Měiguó rén", "American")]],
  ["口", "kǒu", 3, "mouth; opening", "miệng", 3, whole("an open mouth"), "origin", "A mouth, squared off over centuries of writing. As a part, it often signals speaking, eating, or a spoken particle.", [w("门口", "ménkǒu", "doorway"), w("人口", "rénkǒu", "population")]],
  ["日", "rì", 4, "sun; day", "mặt trời; ngày", 4, whole("the sun"), "origin", "The sun was first drawn round with a dot in the centre. Brushes made the circle square.", [w("生日", "shēngrì", "birthday"), w("日本", "Rìběn", "Japan")]],
  ["月", "yuè", 4, "moon; month", "mặt trăng; tháng", 4, whole("a crescent moon"), "origin", "A crescent moon. On the left of other characters, the same shape often stands for flesh or the body instead.", [w("一月", "yīyuè", "January"), w("月饼", "yuèbǐng", "mooncake")]],
  ["山", "shān", 1, "mountain", "núi", 3, whole("three peaks"), "origin", "Three peaks rising from one base.", [w("火山", "huǒshān", "volcano"), w("山上", "shān shang", "on the mountain")]],
  ["木", "mù", 4, "tree; wood", "cây; gỗ", 4, whole("a tree with branches and roots"), "origin", "A trunk, branches above, roots below. In modern speech the word for tree is 树; 木 lives on as a part meaning wood or trees.", [w("木头", "mùtou", "wood"), w("木门", "mù mén", "wooden door")]],
  ["水", "shuǐ", 3, "water", "nước", 4, whole("a stream with splashes"), "origin", "A central current with water spilling either side. On the left of a character it shrinks to three dots: 氵.", [w("喝水", "hē shuǐ", "drink water"), w("水果", "shuǐguǒ", "fruit")]],
  ["火", "huǒ", 3, "fire", "lửa", 4, whole("flames rising"), "origin", "Flames with sparks either side. At the bottom of a character it can become four dots: 灬.", [w("火车", "huǒchē", "train"), w("火山", "huǒshān", "volcano")]],
  // r2 · pointing at ideas
  ["一", "yī", 1, "one", "một", 1, whole("a single line"), "origin", "One stroke for one. Its tone shifts in connected speech: 一起 yìqǐ, 一下 yíxià.", [w("一起", "yìqǐ", "together"), w("一点", "yìdiǎn", "a little")]],
  ["二", "èr", 4, "two", "hai", 2, whole("two lines"), "origin", "Two lines, the lower one longer. When counting things, Mandarin usually says 两 liǎng instead.", [w("二月", "èryuè", "February"), w("十二", "shí'èr", "twelve")]],
  ["三", "sān", 1, "three", "ba", 3, whole("three lines"), "origin", "Three lines. After three, the pattern stops: four is 四.", [w("三点", "sān diǎn", "three o’clock"), w("三月", "sānyuè", "March")]],
  ["上", "shàng", 4, "up; on; above", "trên", 3, whole("a mark above a line"), "origin", "A short mark above a base line points upward.", [w("山上", "shān shang", "on the mountain"), w("上午", "shàngwǔ", "morning")]],
  ["下", "xià", 4, "down; below", "dưới", 3, whole("a mark below a line"), "origin", "The mirror of 上: a mark hanging below the line.", [w("一下", "yíxià", "a moment"), w("下午", "xiàwǔ", "afternoon")]],
  ["大", "dà", 4, "big", "to; lớn", 3, whole("a person, arms and legs spread wide"), "origin", "A person stretching out as wide as possible. Compare 人.", [w("大学", "dàxué", "university"), w("大小", "dàxiǎo", "size")]],
  ["小", "xiǎo", 3, "small", "nhỏ", 3, whole("tiny grains"), "origin", "Early forms show small dots, like grains of sand.", [w("小学", "xiǎoxué", "primary school"), w("小心", "xiǎoxīn", "be careful")]],
  ["中", "zhōng", 1, "middle; centre", "giữa", 4, whole("a line through the centre"), "memory aid", "A vertical stroke straight through the middle of a box.", [w("中国", "Zhōngguó", "China"), w("中文", "Zhōngwén", "Chinese language")]],
  // r3 · two pictures, one idea
  ["女", "nǚ", 3, "woman; female", "nữ", 3, whole("a kneeling woman"), "origin", "Early forms show a kneeling figure with crossed arms. As a part, it appears in many family and women’s words.", [w("女儿", "nǚ'ér", "daughter"), w("女生", "nǚshēng", "girl; female student")]],
  ["子", "zǐ", 3, "child", "con", 3, whole("a baby with arms out"), "origin", "A swaddled baby with arms reaching out. Also a very common word ending, as in 儿子 son.", [w("儿子", "érzi", "son"), w("孩子", "háizi", "child")]],
  ["好", "hǎo", 3, "good; well", "tốt; khỏe", 6, [m("女", "woman"), m("子", "child")], "traditional explanation", "A woman and a child: the classic picture of “good.” Scholars debate the original sense, but the structure is a reliable memory hook.", [w("你好", "nǐ hǎo", "hello"), w("好吃", "hǎochī", "tasty")]],
  ["明", "míng", 2, "bright; clear", "sáng", 8, [m("日", "sun"), m("月", "moon")], "memory aid", "Sun and moon side by side: as bright as it gets.", [w("明天", "míngtiān", "tomorrow"), w("明白", "míngbai", "to understand")]],
  ["休", "xiū", 1, "rest", "nghỉ", 6, [m("亻", "person"), m("木", "tree")], "origin", "A person leaning against a tree. 亻 is how 人 looks on the left side of a character.", [w("休息", "xiūxi", "to rest"), w("休假", "xiūjià", "time off")]],
  ["林", "lín", 2, "woods; Lin (surname)", "rừng; họ Lâm", 8, [m("木", "tree"), m("木", "tree")], "origin", "Two trees make woods; three make 森, a forest. It is also a common surname, as in 林安.", [w("森林", "sēnlín", "forest"), w("林安", "Lín Ān", "Lin An (a name)")]],
  ["目", "mù", 4, "eye", "mắt", 5, whole("an eye turned upright"), "origin", "An eye, rotated to stand upright. Everyday speech uses 眼睛 for eye; 目 lives on inside other characters.", [w("目的", "mùdì", "purpose"), w("节目", "jiémù", "programme; show")]],
  ["看", "kàn", 4, "look; watch; read", "nhìn; xem", 9, [m("手", "hand (reshaped on top)"), m("目", "eye")], "origin", "A hand held over the eye, shading it to look into the distance.", [w("看书", "kàn shū", "read a book"), w("好看", "hǎokàn", "good-looking")]],
  // r4 · meaning + sound
  ["马", "mǎ", 3, "horse", "ngựa", 3, whole("a horse: mane, body, legs"), "origin", "Simplified from 馬, which still shows the mane and four legs. As a part, it often gives the sound “ma.”", [w("马上", "mǎshàng", "right away"), w("骑马", "qí mǎ", "ride a horse")], "馬"],
  ["妈", "mā", 1, "mum", "mẹ", 6, [m("女", "woman"), s("马", "mǎ")], "origin", "Woman for the meaning, horse for the sound. Most characters are built this way.", [w("妈妈", "māma", "mum")], "媽"],
  ["吗", "ma", 5, "question particle (yes/no)", "trợ từ nghi vấn", 6, [m("口", "a spoken word"), s("马", "mǎ")], "usage", "Mouth marks a spoken particle; horse gives the sound. Put 吗 at the end of a statement to make a yes-or-no question.", [w("你好吗", "nǐ hǎo ma", "how are you?"), w("是吗", "shì ma", "really?")], "嗎", "你好吗"],
  ["门", "mén", 2, "door; gate", "cửa", 3, whole("a door"), "origin", "Simplified from 門, a pair of swinging doors.", [w("门口", "ménkǒu", "doorway"), w("开门", "kāi mén", "open the door")], "門"],
  ["们", "men", 5, "plural for people", "(số nhiều)", 5, [m("亻", "person"), s("门", "mén")], "origin", "Person for the meaning, door for the sound. Added to pronouns to make them plural.", [w("我们", "wǒmen", "we"), w("你们", "nǐmen", "you (plural)")], "們", "我们"],
  ["你", "nǐ", 3, "you", "bạn", 7, [m("亻", "person"), sh("尔", "an old word for “you”")], "origin", "Person, plus 尔, which meant “you” in Classical Chinese.", [w("你好", "nǐ hǎo", "hello"), w("你们", "nǐmen", "you (plural)")]],
  ["他", "tā", 1, "he; him", "anh ấy", 5, [m("亻", "person"), sh("也", "")], "usage", "Compare 她: same sound, same right side. Only the meaning part changes.", [w("他们", "tāmen", "they"), w("他的", "tā de", "his")]],
  ["她", "tā", 1, "she; her", "cô ấy", 6, [m("女", "woman"), sh("也", "")], "usage", "Sounds exactly like 他. Reading can tell them apart; listening can’t, so context does the work in speech.", [w("她们", "tāmen", "they (women)"), w("她的", "tā de", "her")]],
  // r5 · small words
  ["我", "wǒ", 3, "I; me", "tôi", 7, whole("a pronged weapon"), "origin", "Originally a drawing of a weapon. The word for “I” borrowed the character for its sound.", [w("我们", "wǒmen", "we"), w("我的", "wǒ de", "my")]],
  ["是", "shì", 4, "to be (am, is, are)", "là", 9, [sh("日", "sun"), sh("正", "straight (reshaped)")], "memory aid", "Under the sun, it’s straight: that’s how it is. Links two nouns: 我是学生.", [w("是的", "shì de", "yes, that’s right"), w("不是", "bú shì", "is not")]],
  ["不", "bù", 4, "not; no", "không", 4, whole("one unit"), "usage", "Negates verbs and adjectives. Before a fourth tone it becomes bú: 不是 bú shì, 不对 bú duì.", [w("不对", "bú duì", "not right"), w("不好", "bù hǎo", "not good")]],
  ["的", "de", 5, "’s; linking particle", "của", 8, [sh("白", "white"), sh("勺", "ladle")], "usage", "The most frequent character in written Chinese. It links a describer to a noun: 我的 mine, 好的 okay.", [w("我的", "wǒ de", "my; mine"), w("好的", "hǎo de", "okay")], undefined, "我的"],
  ["了", "le", 5, "change / completion particle", "rồi", 2, whole("two strokes"), "usage", "Signals that something has happened or changed. One of the most useful small words, and one of the subtlest.", [w("好了", "hǎo le", "done; that’s it"), w("太好了", "tài hǎo le", "great!")], undefined, "好了"],
  ["有", "yǒu", 3, "to have; there is", "có", 6, [m("手", "a hand (reshaped)"), m("月", "meat (old form)")], "origin", "A hand holding a piece of meat: to have. The 月 here was once 肉, flesh.", [w("有空", "yǒu kòng", "to be free"), w("没有", "méiyǒu", "don’t have")]],
  ["这", "zhè", 4, "this", "này", 7, [m("辶", "movement"), sh("文", "")], "usage", "辶 is the walking component; it appears in many words about movement and direction.", [w("这是", "zhè shì", "this is"), w("这儿", "zhèr", "here")], "這"],
  ["在", "zài", 4, "at; in; (be) doing", "ở; đang", 6, [sh("才", "a reshaped 才"), m("土", "earth")], "usage", "Marks location (在家 at home) or an action in progress (我在学中文).", [w("在家", "zài jiā", "at home"), w("现在", "xiànzài", "now")]],
  // r6 · mouth and speech
  ["说", "shuō", 1, "say; speak", "nói", 9, [m("讠", "speech"), sh("兑", "")], "origin", "讠 is the simplified speech component, from 言. Look for it in words about language.", [w("说话", "shuōhuà", "to talk"), w("说中文", "shuō Zhōngwén", "speak Chinese")], "說"],
  ["话", "huà", 4, "words; speech", "lời nói", 8, [m("讠", "speech"), m("舌", "tongue")], "memory aid", "Speech plus tongue: words.", [w("说话", "shuōhuà", "to talk"), w("电话", "diànhuà", "phone")], "話"],
  ["听", "tīng", 1, "listen; hear", "nghe", 7, [m("口", "mouth"), s("斤", "jīn")], "origin", "The traditional form 聽 contains 耳, ear. The simplified form is smaller but the word is the same.", [w("听见", "tīngjiàn", "to hear"), w("听懂", "tīngdǒng", "understand by listening")], "聽"],
  ["叫", "jiào", 4, "call; be called", "gọi; tên là", 5, [m("口", "mouth"), s("丩", "jiū")], "usage", "我叫… is the everyday way to say your name.", [w("我叫", "wǒ jiào", "my name is"), w("叫车", "jiào chē", "call a car")]],
  ["吃", "chī", 1, "eat", "ăn", 6, [m("口", "mouth"), s("乞", "qǐ")], "usage", "Mouth marks the meaning. 好吃 means tasty.", [w("吃饭", "chīfàn", "have a meal"), w("好吃", "hǎochī", "tasty")]],
  ["喝", "hē", 1, "drink", "uống", 12, [m("口", "mouth"), s("曷", "hé")], "usage", "Mouth plus a sound part. Twelve strokes, but you only need to recognise its shape.", [w("喝水", "hē shuǐ", "drink water"), w("喝茶", "hē chá", "drink tea")]],
  ["问", "wèn", 4, "ask", "hỏi", 6, [s("门", "mén"), m("口", "mouth")], "memory aid", "A mouth at the door, asking. 门 also hints at the sound.", [w("问题", "wèntí", "question; problem"), w("请问", "qǐngwèn", "excuse me, may I ask")], "問"],
  ["名", "míng", 2, "name", "tên", 6, [m("夕", "evening"), m("口", "mouth")], "traditional explanation", "In the evening dark you can’t be seen, so you call out your name.", [w("名字", "míngzi", "name"), w("有名", "yǒumíng", "famous")]],
  // r7 · people and places
  ["国", "guó", 2, "country", "nước; quốc", 8, [m("囗", "border"), m("玉", "jade")], "memory aid", "Treasure inside a border. The traditional 國 used a different inner part.", [w("中国", "Zhōngguó", "China"), w("美国", "Měiguó", "United States")], "國"],
  ["学", "xué", 2, "study; learn", "học", 8, [sh("⺍冖", "a roof (simplified top)"), m("子", "child")], "memory aid", "A child under a roof: learning.", [w("学生", "xuésheng", "student"), w("学中文", "xué Zhōngwén", "learn Chinese")], "學"],
  ["生", "shēng", 1, "be born; grow; life", "sinh", 5, whole("a sprout rising from the ground"), "origin", "A plant pushing up out of the soil.", [w("学生", "xuésheng", "student"), w("生日", "shēngrì", "birthday")]],
  ["朋", "péng", 2, "companion (朋友 = friend)", "bạn", 8, [sh("月", ""), sh("月", "")], "origin", "Originally two strings of shells hung together; today it looks like two moons side by side.", [w("朋友", "péngyou", "friend")]],
  ["友", "yǒu", 3, "friend; friendly", "hữu", 4, [m("手", "a hand (reshaped)"), m("又", "a hand")], "origin", "Two hands: help offered and taken.", [w("朋友", "péngyou", "friend"), w("好友", "hǎoyǒu", "close friend")]],
  ["天", "tiān", 1, "sky; day", "trời; ngày", 4, [m("一", "what’s above"), m("大", "a person")], "origin", "A person with what is above their head: the sky, and by extension a day.", [w("今天", "jīntiān", "today"), w("明天", "míngtiān", "tomorrow")]],
  ["见", "jiàn", 4, "see; meet", "gặp; thấy", 4, [m("目", "eye (reduced)"), m("儿", "legs")], "origin", "Simplified from 見: an eye on legs, a person looking.", [w("再见", "zàijiàn", "goodbye"), w("听见", "tīngjiàn", "hear")], "見"],
  ["文", "wén", 2, "writing; language", "văn; chữ", 4, whole("a figure with a pattern on the chest"), "origin", "First a patterned body; then pattern; then writing and culture.", [w("中文", "Zhōngwén", "Chinese language"), w("英文", "Yīngwén", "English")]],
  // counting
  ["四", "sì", 4, "four", "bốn", 5, whole("a box with two marks inside"), "usage", "Four. Some buildings skip a fourth floor, because 四 sì sounds like 死 sǐ, death.", [w("四月", "sìyuè", "April"), w("四个", "sì ge", "four (of something)")]],
  ["五", "wǔ", 3, "five", "năm", 4, whole("lines crossing between a top and a base"), "usage", "Five: one whole hand. You’ll hear it in prices, phone numbers and times.", [w("五月", "wǔyuè", "May"), w("五点", "wǔ diǎn", "five o’clock")]],
  ["六", "liù", 4, "six", "sáu", 4, whole("a dot, a line and two legs"), "usage", "Six is a lucky number: 六六大顺 means “everything goes smoothly.”", [w("六月", "liùyuè", "June"), w("六点", "liù diǎn", "six o’clock")]],
  ["七", "qī", 1, "seven", "bảy", 2, whole("a line crossed by a hook"), "usage", "Seven is only two strokes. A week is 七天, seven days.", [w("七天", "qī tiān", "seven days"), w("七月", "qīyuè", "July")]],
  ["八", "bā", 1, "eight", "tám", 2, whole("two strokes parting"), "usage", "Eight is a favourite number: 八 bā sounds a little like 发 fā, to prosper.", [w("八月", "bāyuè", "August"), w("八点", "bā diǎn", "eight o’clock")]],
  ["九", "jiǔ", 3, "nine", "chín", 2, whole("a hook and a bend"), "usage", "Nine sounds like 久 jiǔ, “long-lasting,” so it appears in wishes for a long friendship.", [w("九月", "jiǔyuè", "September"), w("九点", "jiǔ diǎn", "nine o’clock")]],
  ["十", "shí", 2, "ten", "mười", 2, whole("a simple cross"), "usage", "Ten. Bigger numbers are built from it: 十一 (10 + 1) is eleven, 二十 (2 × 10) is twenty.", [w("十一", "shíyī", "eleven"), w("二十", "èrshí", "twenty")]],
  // home, coming and going
  ["家", "jiā", 1, "home; family", "nhà", 10, [m("宀", "roof"), m("豕", "pig")], "origin", "A pig under a roof: in early farming life, that was a household.", [w("我家", "wǒ jiā", "my home"), w("大家", "dàjiā", "everyone")]],
  ["来", "lái", 2, "come", "đến", 7, whole("a stalk of wheat"), "origin", "First a picture of wheat; the word for “come” borrowed it for its sound.", [w("来了", "lái le", "coming!"), w("回来", "huílai", "come back")], "來"],
  ["去", "qù", 4, "go", "đi", 5, [sh("土", ""), sh("厶", "")], "usage", "The opposite of 来. 我去 means “I’m going.”", [w("去哪儿", "qù nǎr", "where to?"), w("回去", "huíqu", "go back")]],
];

export const baseCharacters: HanziEntry[] = rows.map(
  ([hanzi, pinyin, tone, meaning, vi, strokes, parts, noteKind, note, words, traditional, say]) => ({
    id: `c:${hanzi}`,
    hanzi,
    traditional: traditional ?? hanzi,
    pinyin,
    meaning,
    vi,
    tones: [tone],
    register: "neutral",
    usage: note,
    utilityScore: 80,
    topic: "characters",
    audio: { provider: "local", text: say ?? hanzi },
    provenance,
    hskAlignment: [],
    strokes,
    parts,
    note,
    noteKind,
    words,
    say: say ?? hanzi,
  }),
);
// Characters introduced by content packs (first definition wins; the base course is never overridden).
const characterContexts: Record<string, string> = {
  空: "有空", 吧: "好吧", 啊: "好啊", 什: "什么", 么: "什么", 以: "可以",
  息: "休息", 儿: "儿子", 孩: "孩子", 弟: "弟弟", 干: "干净", 地: "地上",
  得: "得到", 识: "知识", 候: "时候", 视: "电视机", 准: "准备", 备: "准备",
  脑: "电脑", 够: "够用", 习: "学习", 觉: "睡觉", 汉: "汉语", 师: "老师",
  同: "同学", 星: "星期", 昨: "昨天", 今: "今天", 汽: "汽车", 介: "介绍",
  绍: "介绍", 京: "北京", 服: "衣服", 欢: "喜欢", 喜: "喜欢", 兴: "高兴",
  爸: "爸爸", 谢: "谢谢", 体: "身体", 方: "地方",
  非: "非常", 医: "医生", 馆: "图书馆", 商: "商店", 饭: "米饭",
  桌: "桌子", 唱: "唱歌", 歌: "唱歌", 告: "告诉", 诉: "告诉",
  考: "考试", 哥: "哥哥", 道: "知道", 气: "生气", 系: "没关系",
  样: "一样", 怎: "怎么",
  着: "门开着，请进。", 场: "机场", 右: "右边", 后: "后边",
};
const packCharacters: HanziEntry[] = [];
for (const pack of compiledPacks)
  for (const c of pack.characters) {
    if (baseCharacters.some((b) => b.hanzi === c.hanzi) || packCharacters.some((b) => b.hanzi === c.hanzi)) continue;
    // Bound syllables must keep their word context when packs add explicit glyphs.
    const say = characterContexts[c.hanzi] ?? c.hanzi;
    packCharacters.push({
      id: `c:${c.hanzi}`,
      hanzi: c.hanzi,
      traditional: c.hanzi,
      pinyin: c.pinyin,
      meaning: c.meaning,
      vi: "",
      tones: [0],
      register: "neutral",
      usage: c.note,
      utilityScore: 70,
      topic: "characters",
      audio: { provider: "local", text: say },
      provenance: { ...provenance, author: "Content pack (AI-assisted)" },
      hskAlignment: [],
      strokes: c.strokes,
      parts: c.parts,
      note: c.note,
      noteKind: c.noteKind,
      words: c.words,
      say,
    });
  }
export const characters: HanziEntry[] = [...baseCharacters, ...packCharacters];
export const charByHanzi: Record<string, HanziEntry> = Object.fromEntries(
  characters.map((c) => [c.hanzi, c]),
);

const readRows: [string, string, string, string, string[]][] = [
  ["read-1", "Count to ten", "Ten simple characters for counting fingers, prices and days.", "Read the numbers one to ten.", ["一", "二", "三", "四", "五", "六", "七", "八", "九", "十"]],
  ["read-2", "Your first words", "Eight tiny words for your first sentences, like 你好 and 我是….", "Read the words for I, you, good, not, is, big, small and person.", ["人", "大", "小", "你", "我", "好", "不", "是"]],
  ["read-3", "Little pictures", "Mouth, sun, moon, mountain: characters that began as drawings.", "Recognise eight picture-characters by their shape.", ["口", "日", "月", "山", "水", "火", "木", "目"]],
  ["read-4", "Family and a horse", "One part shows the meaning, another part gives the sound.", "Use meaning parts and sound parts to read new characters.", ["女", "子", "马", "妈", "吗", "他", "她", "们"]],
  ["read-5", "Two pictures, one new idea", "Sun + moon = bright. Put pictures together and a new meaning appears.", "Read characters built from parts you already know.", ["明", "休", "林", "看", "门", "问", "听", "见"]],
  ["read-6", "Little helper words", "The small words that hold every sentence together.", "Recognise the most frequent helper words.", ["的", "了", "有", "这", "在", "上", "下", "中"]],
  ["read-7", "Talking and eating", "口 and 讠 mark mouths, speech and asking.", "Spot the mouth and speech parts in new characters.", ["说", "话", "叫", "吃", "喝", "名", "学", "生"]],
  ["read-8", "Friends, home and the world", "Enough characters to read a note from a friend.", "Read words about friends, home, coming and going.", ["国", "朋", "友", "天", "文", "家", "来", "去"]],
];
export const readingLessons: Lesson[] = readRows.map(
  ([id, title, description, mission, chars], i) => ({
    id,
    unit: "Characters",
    title,
    description,
    minutes: 10,
    phrases: chars.map((c) => `c:${c}`),
    prerequisites: i ? [readRows[i - 1][0]] : [],
    notice: description,
    mission,
    context: description,
    track: "read",
    provenance,
  }),
);

/** Glosses for characters that appear in readings before they are taught. */
export const extraGloss: Record<string, { p: string; m: string }> = {
  安: { p: "ān", m: "peace; An (in a name)" },
  它: { p: "tā", m: "it" },
  很: { p: "hěn", m: "very" },
  息: { p: "xī", m: "breath (休息 = rest)" },
  空: { p: "kòng", m: "free time (also kōng, empty)" },
  做: { p: "zuò", m: "do; make" },
  吧: { p: "ba", m: "suggestion particle: let’s…" },
  啊: { p: "a", m: "particle that softens or brightens" },
  茶: { p: "chá", m: "tea" },
  也: { p: "yě", m: "also; too" },
  快: { p: "kuài", m: "fast" },
  懂: { p: "dǒng", m: "understand" },
  可: { p: "kě", m: "can (可以 = may, can)" },
  以: { p: "yǐ", m: "(in 可以 = may, can)" },
  慢: { p: "màn", m: "slow" },
  点: { p: "diǎn", m: "a little; o’clock" },
  谁: { p: "shéi", m: "who" },
  起: { p: "qǐ", m: "rise (一起 = together)" },
  饭: { p: "fàn", m: "meal; cooked rice" },
  和: { p: "hé", m: "and" },
  想: { p: "xiǎng", m: "want to; think" },
  什: { p: "shén", m: "(in 什么 = what)" },
  么: { p: "me", m: "(in 什么 = what)" },
  美: { p: "měi", m: "beautiful (美国 = USA)" },
};

export interface ReadingLine {
  zh: string;
  py: string;
  en: string;
  speaker?: string;
}
export interface Reading {
  id: string;
  title: string;
  titleZh: string;
  after: string;
  blurb: string;
  lines: ReadingLine[];
  questions: { q: string; choices: string[]; answer: string; kind?: "gist" | "detail" | "inference" }[];
  /** What the text is in real life: shapes how it is laid out. */
  format?: "chat" | "post" | "note" | "story";
  /** Read with a goal, as in an exam: shown before the text. */
  purpose?: string;
  /** Lock it in: key words gapped out of the text, refilled from a word bank with the text hidden. */
  cloze?: { lines: ReadingLine[]; bank: string[] };
  /** Word glosses for words not taught yet (content packs). */
  glosses?: { hanzi: string; pinyin: string; meaning: string }[];
}
export const baseReadings: Reading[] = [
  {
    id: "p-horse",
    title: "My horse",
    titleZh: "我的马",
    after: "read-6",
    blurb: "Lin An introduces two members of the family.",
    format: "post",
    purpose: "Lin An posted two photos. Read to find out who (and what) is in them.",
    lines: [
      { zh: "你好！我是林安。", py: "Nǐ hǎo! Wǒ shì Lín Ān.", en: "Hello! I’m Lin An." },
      { zh: "这是我妈妈。", py: "Zhè shì wǒ māma.", en: "This is my mum." },
      { zh: "这是我的马。", py: "Zhè shì wǒ de mǎ.", en: "This is my horse." },
      { zh: "我的马不大，它很小。", py: "Wǒ de mǎ bú dà, tā hěn xiǎo.", en: "My horse isn’t big. It’s very small." },
      { zh: "你有马吗？", py: "Nǐ yǒu mǎ ma?", en: "Do you have a horse?" },
    ],
    questions: [
      { kind: "gist", q: "What is in the two photos?", choices: ["Her mum and her horse", "Her mum and her friend", "Two horses"], answer: "Her mum and her horse" },
      { kind: "detail", q: "What is the horse like?", choices: ["Small", "Big", "Fast"], answer: "Small" },
      { kind: "inference", q: "How does the post end?", choices: ["With a question to her readers", "With a goodbye", "With a price"], answer: "With a question to her readers" },
    ],
    cloze: {
      lines: [
        { zh: "这是我【妈】妈。", py: "Zhè shì wǒ māma.", en: "This is my mum." },
        { zh: "我的【马】不大，它很【小】。", py: "Wǒ de mǎ bú dà, tā hěn xiǎo.", en: "My horse isn’t big. It’s very small." },
      ],
      bank: ["妈", "马", "小", "大", "人"],
    },
  },
  {
    id: "p-mountain",
    title: "On the mountain",
    titleZh: "山上",
    after: "read-6",
    blurb: "A postcard from a weekend away.",
    format: "note",
    purpose: "A friend sent you a postcard. Read to find out where they are and what they’re doing.",
    lines: [
      { zh: "山上有人。", py: "Shān shang yǒu rén.", en: "There are people on the mountain." },
      { zh: "山下有水。", py: "Shān xià yǒu shuǐ.", en: "There is water below the mountain." },
      { zh: "我看山，山很大。", py: "Wǒ kàn shān, shān hěn dà.", en: "I look at the mountain. It is big." },
      { zh: "他们在山上休息。", py: "Tāmen zài shān shang xiūxi.", en: "They are resting on the mountain." },
    ],
    questions: [
      { kind: "gist", q: "Where is your friend?", choices: ["In the mountains", "At the sea", "In the city"], answer: "In the mountains" },
      { kind: "detail", q: "What is below the mountain?", choices: ["Water", "People", "Fire"], answer: "Water" },
      { kind: "detail", q: "What are the people on the mountain doing?", choices: ["Resting", "Eating", "Talking"], answer: "Resting" },
    ],
    cloze: {
      lines: [
        { zh: "【山】上有人。", py: "Shān shang yǒu rén.", en: "There are people on the mountain." },
        { zh: "山下有【水】。", py: "Shān xià yǒu shuǐ.", en: "There is water below the mountain." },
        { zh: "我看山，山很【大】。", py: "Wǒ kàn shān, shān hěn dà.", en: "I look at the mountain. It is big." },
      ],
      bank: ["山", "水", "大", "火", "小"],
    },
  },
  {
    id: "p-he-she",
    title: "He and she",
    titleZh: "他和她",
    after: "read-8",
    blurb: "Meeting a friend’s mum, who speaks a little too fast.",
    format: "note",
    purpose: "A page from a learner’s diary. Read to find out what went wrong, and what they did about it.",
    lines: [
      { zh: "他是我朋友，他叫大明。", py: "Tā shì wǒ péngyou, tā jiào Dàmíng.", en: "He’s my friend. His name is Daming." },
      { zh: "她是大明的妈妈。", py: "Tā shì Dàmíng de māma.", en: "She is Daming’s mum." },
      { zh: "大明说中文，他妈妈也说中文。", py: "Dàmíng shuō Zhōngwén, tā māma yě shuō Zhōngwén.", en: "Daming speaks Chinese, and so does his mum." },
      { zh: "她说话很快，我听不懂。", py: "Tā shuōhuà hěn kuài, wǒ tīng bu dǒng.", en: "She talks fast. I can’t follow." },
      { zh: "我问她：“可以说慢一点吗？”", py: "Wǒ wèn tā: “Kěyǐ shuō màn yìdiǎn ma?”", en: "I ask her, “Could you speak a little slower?”" },
    ],
    questions: [
      { kind: "detail", q: "Who is 她 in this diary?", choices: ["Daming’s mum", "Daming", "The writer"], answer: "Daming’s mum" },
      { kind: "gist", q: "What went wrong?", choices: ["She spoke too fast to follow", "She didn’t speak Chinese", "Daming forgot the writer’s name"], answer: "She spoke too fast to follow" },
      { kind: "inference", q: "What does the writer do about it?", choices: ["Politely asks her to slow down", "Leaves", "Asks Daming to translate"], answer: "Politely asks her to slow down" },
    ],
    cloze: {
      lines: [
        { zh: "她说话很【快】，我听不懂。", py: "Tā shuōhuà hěn kuài, wǒ tīng bu dǒng.", en: "She talks fast. I can’t follow." },
        { zh: "我问她：“可以说【慢】一点吗？”", py: "Wǒ wèn tā: “Kěyǐ shuō màn yìdiǎn ma?”", en: "I ask her, “Could you speak a little slower?”" },
      ],
      bank: ["快", "慢", "大", "好"],
    },
  },
  {
    id: "p-tomorrow",
    title: "See you tomorrow",
    titleZh: "明天见",
    after: "read-8",
    blurb: "A chat on WeChat: Daming wants to meet up.",
    format: "chat",
    purpose: "Daming messaged Lin An. Read to find out what they agree to do, and when.",
    lines: [
      { speaker: "大明", zh: "林安，你明天有空吗？", py: "Lín Ān, nǐ míngtiān yǒu kòng ma?", en: "Lin An, are you free tomorrow?" },
      { speaker: "林安", zh: "有空。你想做什么？", py: "Yǒu kòng. Nǐ xiǎng zuò shénme?", en: "I am. What do you want to do?" },
      { speaker: "大明", zh: "我们去喝茶吧。", py: "Wǒmen qù hē chá ba.", en: "Let’s go for tea." },
      { speaker: "林安", zh: "好啊！明天见。", py: "Hǎo a! Míngtiān jiàn.", en: "Sure! See you tomorrow." },
    ],
    questions: [
      { kind: "detail", q: "When will they meet?", choices: ["Tomorrow", "Today", "At the weekend"], answer: "Tomorrow" },
      { kind: "detail", q: "What will they do?", choices: ["Drink tea", "Eat a meal", "Climb a mountain"], answer: "Drink tea" },
      { kind: "inference", q: "How does Lin An feel about the plan?", choices: ["Happy to go", "Not sure", "She says no"], answer: "Happy to go" },
    ],
    cloze: {
      lines: [
        { speaker: "大明", zh: "林安，你【明天】有空吗？", py: "Lín Ān, nǐ míngtiān yǒu kòng ma?", en: "Lin An, are you free tomorrow?" },
        { speaker: "大明", zh: "我们去喝【茶】吧。", py: "Wǒmen qù hē chá ba.", en: "Let’s go for tea." },
        { speaker: "林安", zh: "【好】啊！明天见。", py: "Hǎo a! Míngtiān jiàn.", en: "Sure! See you tomorrow." },
      ],
      bank: ["明天", "茶", "好", "水", "今天"],
    },
  },
  {
    id: "p-door",
    title: "At the door",
    titleZh: "在门口",
    after: "read-8",
    blurb: "Someone knocks. A tiny story with a question, a reply and an ending.",
    format: "story",
    purpose: "Read to find out who is at the door, and how the evening ends.",
    lines: [
      { zh: "有人在门口。", py: "Yǒu rén zài ménkǒu.", en: "Someone is at the door." },
      { zh: "我问：“你是谁？”", py: "Wǒ wèn: “Nǐ shì shéi?”", en: "I ask, “Who are you?”" },
      { zh: "他说：“我是你的朋友大明！”", py: "Tā shuō: “Wǒ shì nǐ de péngyou Dàmíng!”", en: "He says, “I’m your friend Daming!”" },
      { zh: "我看了看，是大明。", py: "Wǒ kàn le kàn, shì Dàmíng.", en: "I take a look. It is Daming." },
      { zh: "我们一起去吃饭了。", py: "Wǒmen yìqǐ qù chīfàn le.", en: "We went to eat together." },
    ],
    questions: [
      { kind: "detail", q: "Who was at the door?", choices: ["Daming", "Lin An", "A stranger"], answer: "Daming" },
      { kind: "inference", q: "Why does the narrator ask 你是谁？", choices: ["They can’t see who it is", "They forgot Daming’s name", "They are angry"], answer: "They can’t see who it is" },
      { kind: "detail", q: "What did they do next?", choices: ["Went to eat", "Watched a film", "Went to sleep"], answer: "Went to eat" },
    ],
    cloze: {
      lines: [
        { zh: "有人在【门】口。", py: "Yǒu rén zài ménkǒu.", en: "Someone is at the door." },
        { zh: "我问：“你是【谁】？”", py: "Wǒ wèn: “Nǐ shì shéi?”", en: "I ask, “Who are you?”" },
        { zh: "我们一起去【吃】饭了。", py: "Wǒmen yìqǐ qù chīfàn le.", en: "We went to eat together." },
      ],
      bank: ["门", "谁", "吃", "喝", "山"],
    },
  },
];

/** Pack dialogues and readings appear after the curated readings. */
export const readings: Reading[] = [...baseReadings, ...compiledPacks.flatMap((p) => p.texts)];

// Word-level help for characters that only appear inside pack words or glosses.
const wordHelp = new Map<string, { p: string; m: string; say: string }>();
for (const pack of compiledPacks) {
  for (const g of pack.texts.flatMap((t) => t.glosses))
    for (const ch of Array.from(g.hanzi)) if (!wordHelp.has(ch)) wordHelp.set(ch, { say: g.hanzi, p: g.pinyin, m: g.hanzi.length > 1 ? `in ${g.hanzi}: ${g.meaning}` : g.meaning });
  for (const w of pack.phrases.filter((x) => x.topic.startsWith("stage-")))
    for (const ch of Array.from(w.hanzi))
      if (!wordHelp.has(ch) || w.hanzi === ch) wordHelp.set(ch, { say: w.hanzi, p: w.pinyin, m: w.hanzi === ch ? w.meaning : `in ${w.hanzi} (${w.pinyin}): ${w.meaning}` });
}
/** Called by content.ts once all phrases exist: lets the reader explain a character through a known word. */
export function registerWordHelp(words: { hanzi: string; pinyin: string; meaning: string }[]) {
  for (const w of words)
    for (const ch of Array.from(w.hanzi))
      if (isHan(ch) && (!wordHelp.has(ch) || w.hanzi === ch))
        wordHelp.set(ch, { say: w.hanzi, p: w.pinyin, m: w.hanzi === ch ? w.meaning : `in ${w.hanzi} (${w.pinyin}): ${w.meaning}` });
}
export const glossFor = (ch: string) => {
  const c = charByHanzi[ch];
  if (c) return { p: c.pinyin, m: c.meaning, taught: true as const };
  const e = extraGloss[ch] ?? wordHelp.get(ch);
  return e ? { ...e, taught: false as const } : null;
};
export const isHan = (ch: string) => /\p{Script=Han}/u.test(ch);

/** Keep neutral particles and ambiguous syllables inside a familiar word. */
export function characterSpeech(ch: string) {
  return charByHanzi[ch]?.say ?? characterContexts[ch] ?? (extraGloss[ch] ? ch : wordHelp.get(ch)?.say ?? ch);
}
