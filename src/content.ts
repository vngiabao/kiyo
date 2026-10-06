import type { Phrase, Lesson, Provenance, Exercise, Task } from "./types";
import { lessonTasks } from "./tasks";
import { characters, readingLessons, charByHanzi, isHan, registerWordHelp } from "./hanzi";
import { wordSpeech } from "./word-speech";
import { compiledPacks } from "./pack-content";
import type { CompiledGrammar, CompiledScenario, PackPragmatics } from "./packs";
export { characters, readingLessons, charByHanzi } from "./hanzi";
export const provenance: Provenance = {
  status: "AI-assisted draft",
  author: "Tingjian original seed",
  reviewer: null,
  version: 1,
  sources: [],
  lastReviewed: null,
};
// Original teaching language. Reference checking does not imply native educator review.
const rows: [string, string, string, string, string, string, string][] = [
  [
    "hello",
    "你好",
    "nǐ hǎo",
    "Hello",
    "Xin chào",
    "greetings",
    "A neutral greeting for meeting someone. With two third tones, the first is pronounced like a rising tone.",
  ],
  [
    "thanks",
    "谢谢",
    "xièxie",
    "Thank you",
    "Cảm ơn",
    "greetings",
    "The second syllable is light and short.",
  ],
  [
    "good",
    "好",
    "hǎo",
    "Good / okay",
    "Tốt / được",
    "greetings",
    "A short, useful response when you accept a suggestion.",
  ],
  [
    "bye",
    "再见",
    "zàijiàn",
    "Goodbye",
    "Tạm biệt",
    "greetings",
    "Use when taking leave. Between friends, 拜拜 is also common.",
  ],
  [
    "you",
    "你",
    "nǐ",
    "You",
    "Bạn",
    "names",
    "Use with peers. 您 is a respectful alternative in some contexts.",
  ],
  [
    "me",
    "我",
    "wǒ",
    "I / me",
    "Tôi",
    "names",
    "Mandarin does not change this pronoun between subject and object.",
  ],
  [
    "myname",
    "我叫林安",
    "wǒ jiào Lín Ān",
    "My name is Lin An",
    "Tôi tên là Lâm An",
    "names",
    "叫 introduces a name. Replace 林安 with your own name.",
  ],
  [
    "youquestion",
    "你呢",
    "nǐ ne",
    "And you?",
    "Còn bạn?",
    "names",
    "A compact way to return the same question.",
  ],
  [
    "namequestion",
    "你叫什么名字",
    "nǐ jiào shénme míngzi",
    "What is your name?",
    "Bạn tên là gì?",
    "names",
    "Use with a peer in a friendly introduction.",
  ],
  [
    "yes",
    "对",
    "duì",
    "Right / correct",
    "Đúng",
    "reactions",
    "Confirm that what someone said is correct. It is not a universal yes.",
  ],
  [
    "notright",
    "不对",
    "bú duì",
    "Not right",
    "Không đúng",
    "reactions",
    "不 changes to a rising tone before another fourth tone.",
  ],
  [
    "can",
    "可以",
    "kěyǐ",
    "Can / may / okay",
    "Có thể / được",
    "reactions",
    "Useful for permission or accepting a proposal.",
  ],
  [
    "cant",
    "不可以",
    "bù kěyǐ",
    "Not allowed",
    "Không được",
    "reactions",
    "This usually refuses permission, rather than describing lack of skill.",
  ],
  [
    "slow",
    "慢一点",
    "màn yìdiǎn",
    "A little slower",
    "Chậm một chút",
    "repair",
    "Add 请 for a more polite request: 请慢一点。",
  ],
  [
    "again",
    "可以再说一次吗",
    "kěyǐ zài shuō yí cì ma",
    "Could you say that again?",
    "Bạn có thể nói lại một lần không?",
    "repair",
    "A complete rescue phrase; learn it as one reusable chunk.",
  ],
  [
    "notunderstand",
    "我没听懂",
    "wǒ méi tīng dǒng",
    "I didn’t understand what I heard",
    "Tôi chưa nghe hiểu",
    "repair",
    "听懂 combines hearing with understanding.",
  ],
  [
    "meaning",
    "什么意思",
    "shénme yìsi",
    "What does it mean?",
    "Nghĩa là gì?",
    "repair",
    "Ask about meaning. In a tense context this can sound challenging; keep a curious tone.",
  ],
  [
    "wait",
    "等一下",
    "děng yíxià",
    "Wait a moment",
    "Đợi một chút",
    "repair",
    "Useful for buying a little processing time.",
  ],
  [
    "china",
    "中国",
    "Zhōngguó",
    "China",
    "Trung Quốc",
    "identity",
    "国 is often used in country names.",
  ],
  [
    "us",
    "美国",
    "Měiguó",
    "United States",
    "Hoa Kỳ",
    "identity",
    "A country name; add 人 to describe nationality.",
  ],
  [
    "vietnam",
    "越南",
    "Yuènán",
    "Vietnam",
    "Việt Nam",
    "identity",
    "我来自越南 means I come from Vietnam.",
  ],
  [
    "from",
    "你是哪国人",
    "nǐ shì nǎ guó rén",
    "What country are you from?",
    "Bạn là người nước nào?",
    "identity",
    "A country-level question. 你是哪里人 asks more generally where someone is from.",
  ],
  [
    "american",
    "我是美国人",
    "wǒ shì Měiguó rén",
    "I’m American",
    "Tôi là người Mỹ",
    "identity",
    "是 links a person to an identity or category.",
  ],
  [
    "student",
    "我是学生",
    "wǒ shì xuésheng",
    "I’m a student",
    "Tôi là sinh viên",
    "identity",
    "Use 是 for identity. Do not add 是 before every adjective.",
  ],
  [
    "mandarin",
    "中文",
    "Zhōngwén",
    "Chinese language",
    "Tiếng Trung",
    "language",
    "In this course we use Standard Mandarin. 中文 can refer more broadly to Chinese language.",
  ],
  [
    "learning",
    "我在学中文",
    "wǒ zài xué Zhōngwén",
    "I’m learning Chinese",
    "Tôi đang học tiếng Trung",
    "language",
    "在 before a verb can mark an activity in progress.",
  ],
  [
    "little",
    "一点",
    "yìdiǎn",
    "A little",
    "Một chút",
    "language",
    "Use for a small amount; in 慢一点 it softens a request.",
  ],
  [
    "know",
    "我不知道",
    "wǒ bù zhīdào",
    "I don’t know",
    "Tôi không biết",
    "language",
    "知道 concerns knowing information.",
  ],
  [
    "friend",
    "朋友",
    "péngyou",
    "Friend",
    "Bạn bè",
    "people",
    "The second syllable is normally light.",
  ],
  [
    "myfriend",
    "这是我朋友",
    "zhè shì wǒ péngyou",
    "This is my friend",
    "Đây là bạn tôi",
    "people",
    "的 is often omitted with close relationships.",
  ],
  [
    "family",
    "家人",
    "jiārén",
    "Family members",
    "Người nhà",
    "people",
    "Refers to people in the family.",
  ],
  [
    "brother",
    "哥哥",
    "gēge",
    "Older brother",
    "Anh trai",
    "people",
    "Mandarin distinguishes older and younger siblings.",
  ],
  [
    "tea",
    "茶",
    "chá",
    "Tea",
    "Trà",
    "food",
    "The rising tone distinguishes this syllable from other tonal possibilities.",
  ],
  [
    "water",
    "水",
    "shuǐ",
    "Water",
    "Nước",
    "food",
    "A useful third-tone word. In connected speech third tones are often low, not full dips.",
  ],
  [
    "coffee",
    "咖啡",
    "kāfēi",
    "Coffee",
    "Cà phê",
    "food",
    "Both syllables have a high, level tone.",
  ],
  [
    "wanttea",
    "我想喝茶",
    "wǒ xiǎng hē chá",
    "I’d like to drink tea",
    "Tôi muốn uống trà",
    "food",
    "想 is a useful way to express a wish.",
  ],
  [
    "cup",
    "一杯水",
    "yì bēi shuǐ",
    "A glass of water",
    "Một cốc nước",
    "food",
    "杯 measures drinks in a cup or glass.",
  ],
  [
    "menu",
    "菜单",
    "càidān",
    "Menu",
    "Thực đơn",
    "food",
    "可以看一下菜单吗 asks to see a menu.",
  ],
  [
    "tasty",
    "很好吃",
    "hěn hǎochī",
    "It tastes good",
    "Ngon",
    "food",
    "好吃 describes food; 好喝 describes drinks.",
  ],
  [
    "bill",
    "买单",
    "mǎidān",
    "Pay the bill",
    "Thanh toán",
    "food",
    "A common restaurant expression. 请 adds politeness.",
  ],
  [
    "today",
    "今天",
    "jīntiān",
    "Today",
    "Hôm nay",
    "time",
    "Time expressions often come before the verb.",
  ],
  [
    "tomorrow",
    "明天",
    "míngtiān",
    "Tomorrow",
    "Ngày mai",
    "time",
    "Place it before the activity: 明天见。",
  ],
  [
    "when",
    "几点",
    "jǐ diǎn",
    "What time?",
    "Mấy giờ?",
    "time",
    "Ask for a clock time. 什么时候 asks more broadly when.",
  ],
  [
    "three",
    "三点",
    "sān diǎn",
    "Three o’clock",
    "Ba giờ",
    "time",
    "点 marks the hour.",
  ],
  [
    "tomorrowsee",
    "明天见",
    "míngtiān jiàn",
    "See you tomorrow",
    "Hẹn gặp ngày mai",
    "time",
    "A natural short goodbye once a plan is made.",
  ],
  [
    "weekend",
    "周末",
    "zhōumò",
    "Weekend",
    "Cuối tuần",
    "plans",
    "A useful anchor for social plans.",
  ],
  [
    "free",
    "你有空吗",
    "nǐ yǒu kòng ma",
    "Are you free?",
    "Bạn có rảnh không?",
    "plans",
    "空 is kòng when it means free time.",
  ],
  [
    "together",
    "一起",
    "yìqǐ",
    "Together",
    "Cùng nhau",
    "plans",
    "Put it before the shared activity.",
  ],
  [
    "letscoffee",
    "一起喝咖啡吧",
    "yìqǐ hē kāfēi ba",
    "Let’s have coffee together",
    "Cùng uống cà phê nhé",
    "plans",
    "吧 makes this a suggestion.",
  ],
  [
    "okay",
    "好啊",
    "hǎo a",
    "Sure!",
    "Được chứ!",
    "plans",
    "A warm acceptance; delivery matters.",
  ],
  [
    "where",
    "在哪儿",
    "zài nǎr",
    "Where is it?",
    "Ở đâu?",
    "places",
    "在 locates something. 哪里 is another common way to say where.",
  ],
  [
    "station",
    "地铁站",
    "dìtiězhàn",
    "Metro station",
    "Ga tàu điện ngầm",
    "places",
    "A practical compound: metro + station.",
  ],
  [
    "left",
    "左边",
    "zuǒbian",
    "Left side",
    "Bên trái",
    "places",
    "边 can be a light syllable in everyday speech.",
  ],
  [
    "right",
    "右边",
    "yòubian",
    "Right side",
    "Bên phải",
    "places",
    "Use with 在 to locate something.",
  ],
  [
    "straight",
    "一直走",
    "yìzhí zǒu",
    "Go straight / keep going",
    "Đi thẳng",
    "places",
    "Usually accompanied by directional context.",
  ],
  [
    "like",
    "喜欢",
    "xǐhuan",
    "Like",
    "Thích",
    "hobbies",
    "Use before a noun or an activity.",
  ],
  [
    "music",
    "音乐",
    "yīnyuè",
    "Music",
    "Âm nhạc",
    "hobbies",
    "乐 is yuè in 音乐.",
  ],
  [
    "movies",
    "看电影",
    "kàn diànyǐng",
    "Watch a film",
    "Xem phim",
    "hobbies",
    "An activity chunk, useful after 喜欢 or 想.",
  ],
  [
    "sport",
    "打篮球",
    "dǎ lánqiú",
    "Play basketball",
    "Chơi bóng rổ",
    "hobbies",
    "Ball sports use different verbs; learn 打篮球 as a chunk.",
  ],
  [
    "whatlike",
    "你喜欢做什么",
    "nǐ xǐhuan zuò shénme",
    "What do you like doing?",
    "Bạn thích làm gì?",
    "hobbies",
    "The question word stays in the position of the missing information.",
  ],
  [
    "work",
    "上班",
    "shàngbān",
    "Go to work / be at work",
    "Đi làm",
    "routine",
    "A routine activity rather than a job title.",
  ],
  [
    "eat",
    "吃饭",
    "chīfàn",
    "Eat / have a meal",
    "Ăn cơm",
    "routine",
    "Often means eating a meal, not literally only eating rice.",
  ],
  [
    "home",
    "回家",
    "huí jiā",
    "Go home",
    "Về nhà",
    "routine",
    "回 expresses return.",
  ],
  [
    "busy",
    "有点忙",
    "yǒudiǎn máng",
    "A little busy",
    "Hơi bận",
    "routine",
    "有点 often introduces a less-than-ideal quality.",
  ],
  [
    "sorry",
    "不好意思",
    "bù hǎoyìsi",
    "Sorry / excuse me",
    "Xin lỗi / làm phiền",
    "social",
    "Often used for small impositions or awkwardness.",
  ],
  [
    "noproblem",
    "没关系",
    "méi guānxi",
    "No problem / it’s okay",
    "Không sao",
    "social",
    "A reassuring response to an apology.",
  ],
  [
    "really",
    "真的假的",
    "zhēn de jiǎ de",
    "Really? / Are you serious?",
    "Thật hay đùa vậy?",
    "social",
    "Casual surprise with friends; not a formal response.",
  ],
  [
    "ithink",
    "我觉得",
    "wǒ juéde",
    "I think / I feel",
    "Tôi nghĩ / tôi cảm thấy",
    "social",
    "Introduce an impression or opinion.",
  ],
  [
    "then",
    "然后呢",
    "ránhòu ne",
    "And then?",
    "Rồi sao nữa?",
    "social",
    "Invite someone to continue a story.",
  ],
  ["mother", "妈", "mā", "Mum", "Mẹ", "sounds", "Tone 1: high and level."],
  [
    "hemp",
    "麻",
    "má",
    "Hemp / numb",
    "Gai / tê",
    "sounds",
    "Tone 2: rises. Used here only to hear a sound contrast.",
  ],
  [
    "horse",
    "马",
    "mǎ",
    "Horse",
    "Ngựa",
    "sounds",
    "Tone 3: low; its full dip is most audible in isolation.",
  ],
  ["scold", "骂", "mà", "Scold", "Mắng", "sounds", "Tone 4: falls sharply."],
  [
    "one",
    "一",
    "yī",
    "One",
    "Một",
    "numbers",
    "The citation tone changes in connected speech: yí before fourth tone; yì before first, second or third.",
  ],
  [
    "two",
    "二",
    "èr",
    "Two",
    "Hai",
    "numbers",
    "Use 两 before many measure words: 两杯水。",
  ],
  ["threeNum", "三", "sān", "Three", "Ba", "numbers", "A high, level tone."],
  [
    "howmuch",
    "多少钱",
    "duōshao qián",
    "How much does it cost?",
    "Bao nhiêu tiền?",
    "numbers",
    "A useful pricing question; 少 is light here.",
  ],
  [
    "ten",
    "十",
    "shí",
    "Ten",
    "Mười",
    "numbers",
    "Keep it distinct from 四 sì (four).",
  ],
];
const trad: Record<string, string> = {
  谢谢: "謝謝",
  再见: "再見",
  你叫什么名字: "你叫什麼名字",
  可以再说一次吗: "可以再說一次嗎",
  我没听懂: "我沒聽懂",
  什么意思: "什麼意思",
  中国: "中國",
  美国: "美國",
  你是哪国人: "你是哪國人",
  我是美国人: "我是美國人",
  我是学生: "我是學生",
  我在学中文: "我在學中文",
  这是我朋友: "這是我朋友",
  菜单: "菜單",
  买单: "買單",
  几点: "幾點",
  三点: "三點",
  明天见: "明天見",
  周末: "週末",
  你有空吗: "你有空嗎",
  一起喝咖啡吧: "一起喝咖啡吧",
  在哪儿: "在哪兒",
  地铁站: "地鐵站",
  左边: "左邊",
  右边: "右邊",
  音乐: "音樂",
  看电影: "看電影",
  打篮球: "打籃球",
  你喜欢做什么: "你喜歡做什麼",
  喜欢: "喜歡",
  吃饭: "吃飯",
  有点忙: "有點忙",
  没关系: "沒關係",
  我觉得: "我覺得",
  妈: "媽",
  马: "馬",
  骂: "罵",
  多少钱: "多少錢",
};
// One tone per spoken syllable, including neutral 5. These match the pedagogical
// pinyin (explicit yi/bu changes); connected third-tone changes are explained separately.
const tones: Record<string, number[]> = {
  hello: [3, 3],
  thanks: [4, 5],
  good: [3],
  bye: [4, 4],
  you: [3],
  me: [3],
  myname: [3, 4, 2, 1],
  youquestion: [3, 5],
  namequestion: [3, 4, 2, 5, 2, 5],
  yes: [4],
  notright: [2, 4],
  can: [3, 3],
  cant: [4, 3, 3],
  slow: [4, 4, 3],
  again: [3, 3, 4, 1, 2, 4, 5],
  notunderstand: [3, 2, 1, 3],
  meaning: [2, 5, 4, 5],
  wait: [3, 2, 4],
  china: [1, 2],
  us: [3, 2],
  vietnam: [4, 2],
  from: [3, 4, 3, 2, 2],
  american: [3, 4, 3, 2, 2],
  student: [3, 4, 2, 5],
  mandarin: [1, 2],
  learning: [3, 4, 2, 1, 2],
  little: [4, 3],
  know: [3, 4, 1, 4],
  friend: [2, 5],
  myfriend: [4, 4, 3, 2, 5],
  family: [1, 2],
  brother: [1, 5],
  tea: [2],
  water: [3],
  coffee: [1, 1],
  wanttea: [3, 3, 1, 2],
  cup: [4, 1, 3],
  menu: [4, 1],
  tasty: [3, 3, 1],
  bill: [3, 1],
  today: [1, 1],
  tomorrow: [2, 1],
  when: [3, 3],
  three: [1, 3],
  tomorrowsee: [2, 1, 4],
  weekend: [1, 4],
  free: [3, 3, 4, 5],
  together: [4, 3],
  letscoffee: [4, 3, 1, 1, 1, 5],
  okay: [3, 5],
  where: [4, 3],
  station: [4, 3, 4],
  left: [3, 5],
  right: [4, 5],
  straight: [4, 2, 3],
  like: [3, 5],
  music: [1, 4],
  movies: [4, 4, 3],
  sport: [3, 2, 2],
  whatlike: [3, 3, 5, 4, 2, 5],
  work: [4, 1],
  eat: [1, 4],
  home: [2, 1],
  busy: [3, 3, 2],
  sorry: [4, 3, 4, 5],
  noproblem: [2, 1, 5],
  really: [1, 5, 3, 5],
  ithink: [3, 2, 5],
  then: [2, 4, 5],
  mother: [1],
  hemp: [2],
  horse: [3],
  scold: [4],
  one: [1],
  two: [4],
  threeNum: [1],
  howmuch: [1, 5, 2],
  ten: [2],
};
export const basePhrases: Phrase[] = rows.map(
  ([id, hanzi, pinyin, meaning, vi, topic, usage]) => ({
    id,
    hanzi,
    traditional: trad[hanzi] ?? hanzi,
    pinyin,
    meaning,
    vi,
    topic,
    usage,
    tones: tones[id],
    register: ["really", "then"].includes(id) ? "casual" : "neutral",
    utilityScore: topic === "sounds" ? 35 : topic === "repair" ? 98 : 90,
    audio: { provider: "local", text: hanzi },
    provenance,
    hskAlignment: [],
  }),
);
/** Phrases and characters share one lookup so attempts, memories and review treat them alike. */
/** Base course phrases plus words, grammar examples and natural phrasings from content packs. */
export const phrases: Phrase[] = [
  ...basePhrases,
  ...compiledPacks.flatMap((p) => p.phrases).filter((p) => !basePhrases.some((b) => b.id === p.id)).map((p) => ({
    ...p, audio: { ...p.audio, text: wordSpeech(p.audio.text, p.pinyin) },
  })),
];
registerWordHelp(phrases.filter((p) => p.topic !== "sounds"));
export const phraseById: Record<string, Phrase> = Object.fromEntries(
  [...phrases, ...characters].map((p) => [p.id, p]),
);
const lessonRows: [
  string,
  string,
  string,
  string[],
  string,
  string,
  string,
  number?,
][] = [
  [
    "first",
    "Sound & survival",
    "Your first exchange",
    ["hello", "thanks", "good", "bye"],
    "Mandarin is a sound system first. Pitch changes meaning. In 你好, nǐ becomes rising before hǎo; the spelling keeps the original tones.",
    "Greet someone, acknowledge them, and say goodbye.",
    "You arrive at a small language exchange. Lin An turns to welcome you.",
    3,
  ],
  [
    "tones",
    "Sound & survival",
    "One syllable, four meanings",
    ["mother", "hemp", "horse", "scold"],
    "Listen to the same syllable four ways. First high and level, then rising, then low, then falling. The curves are teaching models, not measurements of your voice.",
    "Hear the difference between mā, má, mǎ, and mà.",
    "An invitation to slow down and notice pitch.",
    2,
  ],
  [
    "names",
    "Sound & survival",
    "A name opens a conversation",
    ["me", "you", "myname", "youquestion", "namequestion"],
    "我叫… introduces a name. 你呢？ sends the same question back, keeping the conversation moving.",
    "Introduce yourself and ask for a name.",
    "You and Lin An find a seat before the conversation group begins.",
  ],
  [
    "yesno",
    "Sound & survival",
    "Say yes. Say no.",
    ["yes", "notright", "can", "cant"],
    "Mandarin has no single answer that works for every yes/no question. 对 confirms correctness; 可以 answers permission or a suggestion.",
    "Confirm a detail and accept or refuse permission.",
    "Lin An checks that you are in the right group.",
  ],
  [
    "rescue",
    "Sound & survival",
    "Keep the conversation alive",
    ["slow", "again", "notunderstand", "wait"],
    "Not understanding is normal. A short repair phrase lets your partner help. Use the whole chunk before analyzing every word.",
    "Ask for repetition and slower speech.",
    "Your new friend says something you miss. You can still keep talking.",
  ],
  [
    "identity",
    "Sound & survival",
    "Where are you from?",
    ["china", "us", "vietnam", "from", "american"],
    "Country + 人 describes nationality. 是 links someone to a category. Choose an identity that is true for you when speaking freely.",
    "Ask about someone’s country and give your own.",
    "People introduce themselves at the language exchange.",
  ],
  [
    "language",
    "Sound & survival",
    "I’m learning, too",
    ["mandarin", "learning", "little", "know", "meaning"],
    "在 + activity can show what you are doing. 我在学中文 gives your partner useful context about your Mandarin.",
    "Tell someone you are learning and ask what a phrase means.",
    "Lin An notices you are learning Mandarin and offers to help.",
  ],
  [
    "numbers",
    "Sound & survival",
    "Numbers you can use",
    ["one", "two", "threeNum", "ten", "howmuch"],
    "Start with useful numbers, not a long counting test. 一 changes tone in connected speech; number names in isolation use citation tones.",
    "Ask a price and recognize a few numbers.",
    "You stop to buy a drink after the language exchange.",
  ],
  [
    "people",
    "Sound & survival",
    "Bring a friend into the story",
    ["friend", "myfriend", "family", "brother"],
    "这是… means this is…. With close relationships, 我朋友 often works without 的.",
    "Introduce a friend and recognize family words.",
    "Lin An’s friend joins you at the café.",
  ],
  [
    "reactions",
    "Sound & survival",
    "Small replies, real connection",
    ["sorry", "noproblem", "really", "then"],
    "Short reactions do social work: reassure, show surprise, or invite a story to continue. 真的假的 is casual.",
    "React warmly and invite someone to keep talking.",
    "A friend arrives late, apologizes, and starts explaining.",
  ],
  [
    "meet",
    "Meeting people",
    "From hello to a real exchange",
    ["hello", "myname", "namequestion", "youquestion", "bye"],
    "Link familiar chunks into a short exchange. Ask one question back rather than letting the conversation stop.",
    "Greet, introduce yourself, ask a name, and leave naturally.",
    "You meet someone new at a campus event.",
  ],
  [
    "personal",
    "Personal information",
    "Tell me a little about yourself",
    ["student", "american", "learning", "from"],
    "Keep identities and current activities distinct: 我是学生; 我在学中文.",
    "Share two details about yourself and ask a follow-up.",
    "A classmate asks what you do and where you are from.",
  ],
  [
    "friends",
    "Friends & family",
    "People in your life",
    ["friend", "myfriend", "family", "brother", "youquestion"],
    "Use 这是 to introduce someone nearby. Use 你呢 to return a familiar question.",
    "Introduce one person in your life.",
    "You bring a friend to meet Lin An.",
  ],
  [
    "plans",
    "Time & plans",
    "Make a small plan",
    ["today", "tomorrow", "when", "three", "tomorrowsee"],
    "Time usually comes before the activity. 明天三点见 means see you tomorrow at three.",
    "Agree on a day and a time.",
    "You want to meet again after class.",
  ],
  [
    "coffee",
    "Food & drinks",
    "Something to drink",
    ["tea", "water", "coffee", "wanttea", "cup"],
    "想 + verb expresses what you would like to do. A drink often needs a measure word: 一杯水.",
    "Say what you want and understand a drink choice.",
    "You are ordering at a neighborhood café.",
  ],
  [
    "food",
    "Food & drinks",
    "At the table",
    ["menu", "eat", "tasty", "bill"],
    "Learn a few complete acts: ask for a menu, enjoy the food, and ask to pay. 好吃 is for food; 好喝 is for drinks.",
    "Handle a simple restaurant exchange.",
    "You and Lin An stop for lunch.",
  ],
  [
    "directions",
    "Places & directions",
    "Find your way",
    ["where", "station", "left", "right", "straight"],
    "在 tells you where something is. Listen for the destination, then a direction. Ask for repetition if you miss either.",
    "Ask where the metro is and follow a simple direction.",
    "You are leaving the café and looking for the metro.",
  ],
  [
    "hobbies",
    "Hobbies",
    "Find something in common",
    ["like", "music", "movies", "sport", "whatlike"],
    "喜欢 can take a thing or an activity. A question word stays where the missing answer belongs.",
    "Share an interest and ask about theirs.",
    "The conversation turns to what you do outside work.",
  ],
  [
    "routine",
    "Daily routine",
    "A day in your life",
    ["work", "eat", "home", "busy", "ithink"],
    "Learn activities as chunks. Time + activity lets you build a simple account of your day.",
    "Name everyday activities and say when you are busy.",
    "Lin An asks about your usual day.",
  ],
  [
    "weekend",
    "Time & plans",
    "See you this weekend?",
    ["weekend", "free", "together", "letscoffee", "okay"],
    "吧 softens a suggestion. If you cannot accept, 不好意思，我有点忙 is a gentle starting point.",
    "Invite a friend for coffee and respond warmly.",
    "You want to turn an acquaintance into a friend.",
  ],
];
export const lessons: Lesson[] = lessonRows.map(
  ([id, unit, title, ids, notice, mission, context, tone], i) => ({
    id,
    unit,
    title,
    description: mission,
    minutes: i < 10 ? 12 : 18,
    phrases: ids,
    prerequisites: i ? [lessonRows[i - 1][0]] : [],
    notice,
    mission,
    context,
    tone,
    track: "speak",
    provenance,
  }),
);
/** Lessons generated from content packs: a words lesson and a grammar-and-usage lesson per unit. */
export const packLessons: Lesson[] = compiledPacks.flatMap((p) => p.lessons);
export const packUnits = compiledPacks.map((p) => ({
  ...p.unit,
  lessons: p.lessons,
  texts: p.texts,
  scenario: p.scenario,
}));
export const grammarById: Record<string, CompiledGrammar> = Object.fromEntries(
  compiledPacks.flatMap((p) => p.grammar).map((g) => [g.id, g]),
);
export const usageById: Record<string, PackPragmatics & { id: string }> = Object.fromEntries(
  compiledPacks.flatMap((p) => p.usage).map((u) => [u.id, u]),
);
export const packScenarios: CompiledScenario[] = compiledPacks
  .map((p) => p.scenario)
  .filter((s): s is CompiledScenario => !!s);
export const allLessons: Lesson[] = [...readingLessons, ...lessons, ...packLessons];
export const lessonById: Record<string, Lesson> = Object.fromEntries(
  allLessons.map((l) => [l.id, l]),
);
export const roadmap = [
  "Sound & survival",
  "Social survival",
  "Everyday conversation",
  "Social independence",
  "Media bridge",
  "Native-content independence",
  "Advanced social Mandarin",
  "Professional Mandarin",
  "Polished communication",
  "Lifelong refinement",
];
const taskKind: Record<Task["type"], Exercise["kind"]> = {
  dialogue: "dialogue",
  truefalse: "truefalse",
  reply: "reply",
  listenfill: "listenfill",
  cloze: "cloze",
  match: "match",
};
const taskPrompt: Record<Task["type"], (t: Task) => string> = {
  dialogue: (t) => (t.type === "dialogue" ? t.title : ""),
  truefalse: () => "Is the statement true?",
  reply: () => "What's the best reply?",
  listenfill: () => "Type the missing word.",
  cloze: (t) => (t.type === "cloze" ? t.title : "Fill the gaps."),
  match: (t) => (t.type === "match" ? t.title : "Match them up."),
};
/** A small stable hash, so the same task always shows the same order. */
const seedOf = (s: string) => Array.from(s).reduce((h, c) => (h * 31 + c.charCodeAt(0)) >>> 0, 7);
/**
 * Authors tend to write the right answer first. Place it at a position that
 * varies by task and question, so the key's position never gives it away.
 */
export function placeAnswer(choices: string[], answer: string, seed: number): string[] {
  const others = choices.filter((c) => c !== answer);
  const at = seed % choices.length;
  return [...others.slice(0, at), answer, ...others.slice(at)];
}
const arranged = (task: Task): Task =>
  task.type === "dialogue"
    ? { ...task, questions: task.questions.map((q, i) => ({ ...q, choices: placeAnswer(q.choices, q.answer, seedOf(`${task.id}:${i}`)) })) }
    : task.type === "reply"
      ? { ...task, choices: placeAnswer(task.choices, task.answer, seedOf(task.id)) }
      : task;
/** A practice task as a lesson step. */
export function taskExercise(lessonId: string, raw: Task): Exercise {
  const task = arranged(raw);
  return {
    id: `${lessonId}-${task.id}`,
    kind: taskKind[task.type],
    phraseId: task.phrase,
    prompt: taskPrompt[task.type](task),
    modality: task.type === "cloze" || task.type === "match" ? "reading" : "listening",
    task,
  };
}
/** Deterministic shuffle that never leaves the tiles in order or simply reversed. */
export function scramble<T>(tiles: T[]): T[] {
  if (tiles.length < 2) return tiles;
  const out = [...tiles.filter((_, i) => i % 2 === 1), ...tiles.filter((_, i) => i % 2 === 0)];
  const same = (xs: T[]) => xs.every((x, i) => x === tiles[i]);
  const reversed = (xs: T[]) => xs.every((x, i) => x === tiles[tiles.length - 1 - i]);
  return same(out) || (tiles.length > 2 && reversed(out)) ? rotate(tiles, 1) : out;
}
/** Take one from each list in turn: a, b, c, a, b, c… */
const roundRobin = <T,>(...lists: T[][]) =>
  Array.from({ length: Math.max(0, ...lists.map((l) => l.length)) }, (_, i) => lists.map((l) => l[i])).flat().filter((x): x is T => x !== undefined);

/**
 * Phrase lessons, built like a good textbook unit:
 * 1. Meet each phrase (hear it, see how it works). Each comprehension check comes
 *    one phrase later, so you hold it in memory instead of echoing it back.
 * 2. A short conversation using the phrases: listen with no text, answer gist,
 *    detail and intent questions, then read the transcript.
 * 3. Mixed practice in exam formats (true/false, choose the reply, fill in what you
 *    hear), interleaved so no two steps in a row test the same thing.
 * 4. Reading in context (gap-fill with a word bank, or matching), then build,
 *    speak and read without pinyin.
 */
export function exercisesFor(lesson: Lesson): Exercise[] {
  if (lesson.track === "read") return characterExercisesFor(lesson);
  if (lesson.track === "pack") return packExercisesFor(lesson);
  const steps: Exercise[] = [];
  const ids = lesson.phrases;
  const tasks = (lessonTasks[lesson.id] ?? []).map((x) => taskExercise(lesson.id, x));
  const ofType = (k: Exercise["kind"]) => tasks.filter((x) => x.kind === k);
  const choice = (i: number): Exercise => {
    const id = ids[i];
    const p = phraseById[id];
    const wrong = rotate(ids.filter((x) => x !== id), i)
      .map((x) => phraseById[x].meaning)
      .filter((m) => m !== p.meaning)
      .slice(0, 2);
    const choices = [...wrong];
    choices.splice(i % (wrong.length + 1), 0, p.meaning);
    return { id: `${lesson.id}-${id}-choice`, kind: "choice", phraseId: id, prompt: "What did you hear?", modality: "listening", choices, correct: p.meaning };
  };
  ids.forEach((id, i) => {
    steps.push(
      { id: `${lesson.id}-${id}-hear`, kind: "hear", phraseId: id, prompt: "First, just listen.", modality: "listening" },
      { id: `${lesson.id}-${id}-notice`, kind: "notice", phraseId: id, prompt: "Connect the sound to meaning.", modality: "reading" },
    );
    if (i >= 1) steps.push(choice(i - 1));
  });
  steps.push(...ofType("dialogue"));
  steps.push(choice(ids.length - 1));
  const mixed = roundRobin(ofType("truefalse"), ofType("reply"), ofType("listenfill"));
  const target = ids[0];
  steps.push(...mixed.slice(0, 3), {
    id: `${lesson.id}-recall`,
    kind: "recall",
    phraseId: target,
    prompt: "Bring it back from memory.",
    modality: "recall",
  });
  steps.push(...mixed.slice(3), ...ofType("cloze"), ...ofType("match"));
  const sentence = ids.find((id) => phraseById[id].hanzi.length >= 4);
  if (sentence) {
    const p = phraseById[sentence];
    const words = wordTiles(p.hanzi, p.pinyin);
    const tiles = words.length >= 3 ? words : Array.from(p.hanzi).filter(isHan);
    steps.push({
      id: `${lesson.id}-order`,
      kind: "reorder",
      phraseId: sentence,
      prompt: "Build the phrase.",
      modality: "typing",
      tokens: scramble(tiles),
      correct: tiles.join(""),
    });
  }
  steps.push({
    id: `${lesson.id}-record`,
    kind: "record",
    phraseId: ids[Math.min(1, ids.length - 1)],
    prompt: "Make the words your own.",
    modality: "speaking",
  });
  steps.push({
    id: `${lesson.id}-read`,
    kind: "read",
    phraseId: target,
    prompt: "Recognize it without pinyin.",
    modality: "reading",
    choices: rotate(ids.slice(0, 3), 1).map((id) => phraseById[id].meaning),
    correct: phraseById[target].meaning,
  });
  return steps;
}
let taskSteps: Exercise[] | null = null;
/** Every practice-task step in the course (built once, on first use). */
export function allTaskSteps(): Exercise[] {
  taskSteps ??= allLessons.flatMap((l) => exercisesFor(l)).filter((e) => e.task);
  return taskSteps;
}
/** The lesson step an attempt came from, whether answered in a lesson or in review. */
export const stepOf = (context: string) => context.replace(/^review:/, "").replace(/:\d+$/, "");
/**
 * What review should bring back for a due memory: the task you missed, if any;
 * otherwise another task that uses the same phrase in a new sentence, rotating
 * so you don't meet the same one every time. Null means no task uses it yet.
 */
export function reviewTaskFor(
  memory: { phraseId: string; modality: string; due: number },
  lastMistakeContext?: string,
): Exercise | null {
  const options = allTaskSteps().filter((e) => e.phraseId === memory.phraseId && e.modality === memory.modality);
  if (!options.length) return null;
  const missed = lastMistakeContext && options.find((e) => e.id === stepOf(lastMistakeContext));
  return missed || options[Math.floor(memory.due / 86_400_000) % options.length];
}

export const standards = [
  {
    id: "GF0025-2021",
    name: "Chinese Proficiency Grading Standards (2021)",
    levels: 9,
    source:
      "https://www.moe.gov.cn/srcsite/A19/s229/202104/t20210401_523904.html",
    effectiveDate: "2021-07-01",
    note: "Three stages, nine levels. This proficiency standard is distinct from any particular exam delivery format.",
  },
  {
    id: "HSK-current",
    name: "HSK examination syllabus",
    levels: null,
    source: "https://www.chinesetest.cn/HSK",
    effectiveDate: null,
    note: "Verify the current official syllabus and local exam arrangements before planning an examination.",
  },
];

/** Every character taught up to and including this reading lesson. */
export function charactersThrough(lessonId: string) {
  const end = readingLessons.findIndex((l) => l.id === lessonId);
  return new Set(
    readingLessons
      .slice(0, end + 1)
      .flatMap((l) => l.phrases.map((id) => id.slice(2))),
  );
}
const rotate = <T,>(list: T[], by: number) =>
  list.map((_, i) => list[(i + by) % list.length]);
/**
 * Meet each character, then check it soon after (char → meaning), with
 * reverse recognition (meaning → char) and component spotting interleaved.
 * Closes on real words built only from characters already met.
 */
function characterExercisesFor(lesson: Lesson): Exercise[] {
  const ids = lesson.phrases,
    steps: Exercise[] = [];
  const glyph = (i: number): Exercise => {
    const id = ids[i],
      others = rotate(
        ids.filter((x) => x !== id),
        i,
      ).slice(0, 3);
    const choices = others.map((x) => phraseById[x].meaning);
    choices.splice(i % 4, 0, phraseById[id].meaning);
    return {
      id: `${lesson.id}-${id}-glyph`,
      kind: "glyph",
      phraseId: id,
      prompt: "What does this mean?",
      modality: "reading",
      choices,
      correct: phraseById[id].meaning,
    };
  };
  const pick = (i: number): Exercise => {
    const id = ids[i],
      others = rotate(
        ids.filter((x) => x !== id),
        i + 2,
      ).slice(0, 3);
    const choices = others.map((x) => phraseById[x].hanzi);
    choices.splice((i + 1) % 4, 0, phraseById[id].hanzi);
    return {
      id: `${lesson.id}-${id}-pick`,
      kind: "pick",
      phraseId: id,
      prompt: `Which one means “${phraseById[id].meaning}”?`,
      modality: "reading",
      choices,
      correct: phraseById[id].hanzi,
    };
  };
  const spot = (upTo: number): Exercise | null => {
    for (const id of ids.slice(0, upTo + 1)) {
      const c = charByHanzi[id.slice(2)];
      for (const part of c.parts.filter(
        (p) => p.role === "meaning" && !p.gloss.includes("reshaped"),
      )) {
        const without = ids.filter(
          (x) =>
            !charByHanzi[x.slice(2)].parts.some((p) => p.form === part.form) &&
            x.slice(2) !== part.form,
        );
        if (without.length < 3) continue;
        const choices = without.slice(0, 3).map((x) => x.slice(2));
        choices.splice(1, 0, c.hanzi);
        return {
          id: `${lesson.id}-${id}-spot`,
          kind: "spot",
          phraseId: id,
          prompt: `Which character contains ${part.form}?`,
          cue: part.gloss,
          modality: "reading",
          choices,
          correct: c.hanzi,
        };
      }
    }
    return null;
  };
  const meet = (i: number): Exercise => ({
    id: `${lesson.id}-${ids[i]}-meet`,
    kind: "meet",
    phraseId: ids[i],
    prompt: "A new character",
    modality: "reading",
  });
  // "How many?" — dots to numeral, for the counting lesson.
  const numerals = "一二三四五六七八九十";
  const isCounting = ids.every((id) => numerals.includes(id.slice(2)));
  const count = (i: number): Exercise => {
    const n = numerals.indexOf(ids[i].slice(2)) + 1;
    const choices = rotate(
      ids.filter((x) => x !== ids[i]).slice(Math.max(0, i - 3), i + 3),
      i,
    )
      .slice(0, 3)
      .map((x) => x.slice(2));
    choices.splice(i % 4, 0, ids[i].slice(2));
    return {
      id: `${lesson.id}-${ids[i]}-count`,
      kind: "count",
      phraseId: ids[i],
      prompt: "How many dots?",
      cue: String(n),
      modality: "reading",
      choices,
      correct: ids[i].slice(2),
    };
  };
  // Each check comes two characters after its introduction, so you read it from
  // memory rather than from the screen you just saw.
  const n = ids.length,
    middle = Math.floor(n / 2);
  for (let i = 0; i < n; i++) {
    steps.push(meet(i));
    if (i >= 2) steps.push(glyph(i - 2));
    if (i >= 3 && i % 3 === 0) steps.push(isCounting ? count(i - 2) : pick(i - 3));
    if (i === middle) steps.push((!isCounting && spot(i - 1)) || pick(Math.max(0, i - 2)));
  }
  if (n >= 2) steps.push(glyph(n - 2));
  if (n >= 3) steps.push(isCounting ? count(n - 3) : pick(n - 3));
  steps.push(glyph(n - 1));
  if (n >= 2) steps.push(isCounting ? count(n - 1) : pick(n - 2));
  if (isCounting && n >= 3) steps.push(pick(n - 3));
  // Words the learner can now read in full, sourced from the phrase lexicon.
  const known = charactersThrough(lesson.id),
    fresh = new Set(ids.map((x) => x.slice(2)));
  const readable = phrases.filter((p) => {
    const han = Array.from(p.hanzi).filter(isHan);
    return (
      han.length > 1 &&
      han.every((c) => known.has(c)) &&
      han.some((c) => fresh.has(c))
    );
  });
  readable.slice(0, 2).forEach((p, i) => {
    const distractors = rotate(
      phrases.filter((x) => x.id !== p.id && x.topic !== "sounds"),
      7 * (i + 1),
    )
      .slice(0, 2)
      .map((x) => x.meaning);
    const choices = [...distractors];
    choices.splice(i % 3, 0, p.meaning);
    steps.push({
      id: `${lesson.id}-${p.id}-word`,
      kind: "read",
      phraseId: p.id,
      prompt: "You can read this word now.",
      modality: "reading",
      choices,
      correct: p.meaning,
    });
  });
  return steps.filter((s, i) => steps.findIndex((x) => x.id === s.id) === i);
}

/** Split a sentence into word tiles using the word spacing in its pinyin. */
export function wordTiles(zh: string, py: string): string[] {
  const chars = Array.from(zh).filter(isHan);
  const words = py
    .replace(/[,.!?;:，。！？、“”"]/g, " ")
    .split(/\s+/)
    .filter(Boolean);
  const tiles: string[] = [];
  let i = 0;
  for (const w of words) {
    const n = (w.match(/[aeiouüāáǎàēéěèīíǐìōóǒòūúǔùǖǘǚǜ]+/gi) ?? []).length;
    if (!n) continue;
    tiles.push(chars.slice(i, i + n).join(""));
    i += n;
  }
  return i === chars.length && tiles.every(Boolean) ? tiles : chars;
}

/**
 * Pack lessons. Words: notice each word, then hear it and pick its meaning,
 * then read a few without pinyin. Usage: a grammar card, then build its example
 * from word tiles; then choose the natural phrasing for each social situation.
 */
function packExercisesFor(lesson: Lesson): Exercise[] {
  const steps: Exercise[] = [];
  const ids = lesson.phrases;
  if (lesson.packPart === "words") {
    const choice = (i: number): Exercise => {
      const id = ids[i];
      const p = phraseById[id];
      const others = rotate(ids.filter((x) => x !== id), i).map((x) => phraseById[x].meaning).filter((m) => m !== p.meaning).slice(0, 2);
      const choices = [...new Set(others)];
      choices.splice(i % (choices.length + 1), 0, p.meaning);
      return { id: `${lesson.id}-${id}-choice`, kind: "choice", phraseId: id, prompt: "What did you hear?", modality: "listening", choices, correct: p.meaning };
    };
    const tasks = (compiledPacks.find((c) => c.unit.id === lesson.id)?.tasks ?? []).map((x) => taskExercise(lesson.id, x));
    // Most practice happens in sentences (the tasks). Single-word checks are only for
    // words no task covers, at most six, so a lesson stays one sitting long.
    const inTasks = new Set(tasks.map((x) => x.phraseId));
    const untested = ids.filter((id) => !inTasks.has(id));
    const checked = new Set([...untested, ...ids.filter((id) => inTasks.has(id))].slice(0, 6));
    // Each word's listening check comes after the next word, not straight away.
    ids.forEach((id, i) => {
      steps.push({ id: `${lesson.id}-${id}-notice`, kind: "notice", phraseId: id, prompt: "A new word.", modality: "reading" });
      if (i >= 1 && checked.has(ids[i - 1])) steps.push(choice(i - 1));
    });
    const dialogue = tasks.filter((x) => x.kind === "dialogue");
    const rest = tasks.filter((x) => x.kind !== "dialogue");
    steps.push(...dialogue.slice(0, 1));
    if (checked.has(ids[ids.length - 1])) steps.push(choice(ids.length - 1));
    steps.push(...dialogue.slice(1));
    const mixed = roundRobin(
      rest.filter((x) => x.kind === "truefalse"),
      rest.filter((x) => x.kind === "reply"),
      rest.filter((x) => x.kind === "listenfill"),
    );
    // With a grammar & usage lesson, the mixed practice moves there, after the patterns.
    const hasUsage = allLessons.some((l) => l.id === `${lesson.id}-usage`);
    if (!hasUsage) steps.push(...mixed, ...rest.filter((x) => x.kind === "cloze" || x.kind === "match"));
    ids.slice(0, 3).forEach((id, i) => {
      const p = phraseById[id];
      const others = rotate(ids.filter((x) => x !== id), i + 2).map((x) => phraseById[x].meaning).filter((m) => m !== p.meaning).slice(0, 2);
      const choices = [...new Set(others)];
      choices.splice((i + 1) % (choices.length + 1), 0, p.meaning);
      steps.push({ id: `${lesson.id}-${id}-read`, kind: "read", phraseId: id, prompt: "Read it without pinyin.", modality: "reading", choices, correct: p.meaning });
    });
    return steps;
  }
  for (const id of ids) {
    const p = phraseById[id];
    if (id.endsWith("-ex")) {
      const grammarId = id.slice(0, -3);
      steps.push({ id: `${lesson.id}-${grammarId}-card`, kind: "grammar", phraseId: id, prompt: grammarById[grammarId]?.purpose ?? "A pattern", cue: grammarId, modality: "reading" });
      const tiles = wordTiles(p.hanzi, p.pinyin);
      if (tiles.length > 1 && tiles.length <= 10)
        steps.push({
          id: `${lesson.id}-${grammarId}-build`,
          kind: "reorder",
          phraseId: id,
          prompt: "Build the sentence.",
          modality: "typing",
          tokens: rotate(tiles, Math.ceil(tiles.length / 2)),
          correct: tiles.join(""),
        });
    } else {
      const u = usageById[id];
      const options = [u?.natural.zh, u?.tooFormal?.zh, u?.tooBlunt?.zh].filter((x): x is string => !!x);
      if (options.length > 1)
        steps.push({
          id: `${lesson.id}-${id}-register`,
          kind: "register",
          phraseId: id,
          prompt: "Which sounds natural here?",
          cue: u.situation,
          modality: "reading",
          choices: rotate(options, id.length % options.length),
          correct: u.natural.zh,
        });
      else steps.push({ id: `${lesson.id}-${id}-notice`, kind: "notice", phraseId: id, prompt: u?.situation ?? "Say it naturally.", modality: "reading" });
    }
  }
  // Then practice in exam formats, now that the patterns are fresh.
  const unitTasks = (compiledPacks.find((c) => `${c.unit.id}-usage` === lesson.id)?.tasks ?? [])
    .filter((x) => x.type !== "dialogue")
    .map((x) => taskExercise(lesson.id, x));
  steps.push(
    ...roundRobin(
      unitTasks.filter((x) => x.kind === "truefalse"),
      unitTasks.filter((x) => x.kind === "reply"),
      unitTasks.filter((x) => x.kind === "listenfill"),
    ),
    ...unitTasks.filter((x) => x.kind === "cloze" || x.kind === "match"),
  );
  return steps;
}
