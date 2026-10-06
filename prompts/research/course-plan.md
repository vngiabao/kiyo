# Kiyo course expansion — C1 review

Status: C1 outline approved on 5 October 2026 for all 96 units. Intermediate review stops are revoked. C2 runs four-unit batches through local audio and every acceptance gate; implementation evidence is recorded in course-log.md. Claude owns dictionary/reading-drill work and the five protected files in AGENTS.md section 6.

## Decision proposed

Build **96 additional social units**: 18 for the rest of GF2021 level 1 (`s1-u13`–`s1-u30`), 34 for level 2 (`s2-u01`–`s2-u34`), and 44 for level 3 (`s3-u01`–`s3-u44`). Together with the existing 12 packs, that is a proposed 108-pack course. This is a workload budget, not a duration estimate, HSK pass prediction or promise of fluent drama comprehension.

Prioritise conversation with friends, then transfer the same language to original scenes and lyrical reading. Keep the approved Sayo identity and Night Study v2 design. The last three level-3 units finish vocabulary and consolidate grammar rather than introducing another grammar family.

## Sources and version boundary

The learning baseline is **GF0025-2021**, not the old six-level test vocabulary. Sources checked:

- [Ministry of Education release](https://www.moe.gov.cn/jyb_xwfb/gzdt_gzdt/s5987/202103/t20210329_523304.html) and [original standard PDF](https://www.moe.gov.cn/jyb_xwfb/gzdt_gzdt/s5987/202103/W020210329527301787356.pdf). The scanned PDF was downloaded and pages visually inspected; the release webpage timed out. Printed pp. 1–4 contain benchmarks/topics/tasks, pp. 15–29 characters, pp. 36–169 words, Appendix A from p. 170 grammar. PDF viewer page numbers are six higher than printed pages.
- [CTI official GF2021 query system](https://admin.chinesetest.cn/newhsk/standardsAction.do?means=standardInfo). All level-1–3 word, character and grammar rows fetched, source row numbers retained. Research snapshot: `gf2021-inventory.json`. The source row number is a query identifier, not the Appendix A grammar code.
- [CTI current syllabus portal](https://www.chinesetest.cn/syllabus) and its [exam syllabus PDF](https://hsk.cn-bj.ufileos.com/3.0/%E6%96%B0%E7%89%88HSK%E8%80%83%E8%AF%95%E5%A4%A7%E7%BA%B21219.pdf). Cover: published November 2025, effective July 2026. Availability/version at a particular test centre still needs checking when booking.

GF2021 adds 500 / 772 / 973 vocabulary entries, 300 new characters at each level, and 48 / 81 / 81 grammar families. Thus the level-3 cumulative benchmark is **2,245 entries, 900 characters and 210 grammar families**. These are inventories; completing them does not establish proficiency.

The newer exam syllabus is different: its first 1,000 numbered vocabulary entries split **300 / 200 / 500** across levels 1 / 2 / 3 (cumulative 300 / 500 / 1,000). Recognition-character additions are **246 / 125 / 284**, cumulative 246 / 371 / 655. Digital extraction checked contiguous numbering; results and method are in `exam-syllabus-check.json`. Grammar placement also changes: 可以 is in the newer exam's level 1, while GF2021 places it at level 2. Keep separate alignment metadata; never relabel one inventory as the other. C2 will crosswalk authored packs to the chosen current exam inventory before describing any level as covered for exam preparation.

## Coverage audit

Run `npx tsx scripts/coverage-report.ts --write`. The report is `coverage-report.json`; it includes input hashes, introduced/remaining source rows, local-list differences, incidental candidates and grammar evidence. The seven focused tests cover alternative forms, repeated senses, supplementary character readings and unnumbered cross-references.

Current teaching data: **20 base phrase lessons, 8 character lessons, 12 packs, 66 explicit character entries, 24 grammar cards**. No learner's progress was read. “Introduced” means curriculum evidence, never learner mastery.

- **Level 1:** 189 / 500 word entries introduced; **311 left**. 63 / 300 characters explicitly introduced; **237 left**. Grammar: **8 introduced, 15 partial, 25 unmapped** out of 48.
- **Level 2:** 26 / 772 word entries introduced; **746 left**. 1 / 300 new characters introduced; **299 left**. Grammar: **2 introduced, 3 partial, 76 unmapped** out of 81.
- **Level 3:** 6 / 973 word entries introduced; **967 left**. 1 / 300 new characters introduced; **299 left**. Grammar: **0 introduced, 0 partial, 81 unmapped** out of 81.

That leaves **2,024 vocabulary entries**, **835 new characters**, and **200 grammar families needing some or all explicit treatment**. One of the existing 66 character entries lies outside the level-1–3 character inventories. Word counts are conservative and may fall after sense-level review; the plan must not teach already-covered senses as new vocabulary.

Method: exact base phrase and standalone character-word entries with meanings, plus declared pack vocabulary. A word appearing only in an example or dialogue does not earn full credit. Higher-level repeated spellings require explicit level-specific evidence; one level-1, seven level-2 and one level-3 repeated forms remain for semantic review. Character recognition does not prove mastery of every reading. Grammar coverage is a manual, conservative crosswalk to explicit cards in `grammar-crosswalk.json`; explanations/examples are evidence of introduction, not correctness certified by a native teacher.

Three source traps corrected:

1. Parent/younger-sibling variants occupy one official entry. The local import splits/folds variants and senses: it has 506 / 750 / 953 forms, which are not the official 500 / 772 / 973 entry counts. Do not sum surface forms as entries.
2. Character-query levels 2 and 3 each repeat nine earlier characters with additional readings. Deduplicating within a level alone gives 309; subtract earlier levels to recover the official **300 new characters**. Keep the additional readings as teaching obligations, not new-character counts.
3. Level 2's grammar query includes an unnumbered starred cross-reference before its final items. Exclude it before numbering; there are **81**, not 82. The printed Appendix A codes use 一01…一48, 二01…二81, 三01…三81. Spot checks included printed p. 185 (二42–二48) and p. 200 (三49–三54).

The report lists **3 / 24 / 25 form-or-level discrepancies** between the official query and the local lookup. These are discrepancies, not 52 proven errors: many reflect a minimum level for another sense/reading or suffix notation. Examples: 〇 is absent; 表示 needs review; 称1 and 面1/面2 carry homograph labels; 家（科学家） is a suffix rather than 家 meaning home. Before a affected batch, reconcile source row + reading + sense and propose a documented local lookup/metadata correction. Never guess a level or set a genuine official item to null just to bypass validation.

## Topic and task progression

GF2021 printed pp. 2–4 ground this sequence; situations below are our original adaptations.

- **Level 1:** personal information, daily routines, food, transport and hobbies. Exchange greetings, ask simple questions, understand short signs, and write simple personal details. Practise literal gist/detail and clean basic tones; short original chats/scenes.
- **Level 2:** basic social exchanges, family, study, shopping, meals and feelings. Exchange hobbies, use transport/shopping information, fill everyday forms and explain simple choices. Add reasons, sequence, comparisons, invitations/refusals and repair of misunderstandings.
- **Level 3:** travel, courses, activities, festivals, education and work. Discuss everyday matters, arrange trips, use simple notices/messages and respond to a basic invitation. Add purpose, conditions, indirect reference, polite complaints and supported inference.

The standard's reading descriptors are roughly 80 / 100 / 120 characters per minute at the three levels, within its text/difficulty conditions. These are **not subtitle-speed targets** and are not imported into Claude's timed-drill scoring. GF level 3 describes texts up to 300 characters; the brief's 300–500-character readings are a stretch. Proposed adjustment: a core reading at 200–300 characters, with optional later extended readings up to 500, rather than making 500 compulsory immediately.

## Sequencing, word slots and grammar evidence

The full ordered list follows. Vocabulary budgets sum exactly to the 2,024 remaining official entries: 17–18 per new level-1 unit, 21–22 per level-2 unit and 21–22 per level-3 unit. They are **planning slots**, not finished word lists. Exact word-to-unit assignments (including senses, required grammar words and possible extra social chunks) are finalized against the remaining source rows before each four-unit batch. Retain 15–25 genuinely new entries after moving awkward words to a better situation. Unit counts can change if semantic review or prerequisite allocation demands it; no filler words to meet a number.

The plan does not alphabetically dump leftover words into social scenarios. Each batch starts by selecting collocations and useful lexical fields, allocating its source rows, checking they are not re-taught, and placing displaced items in later thematic buckets. Additional chunks outside GF2021 are marked honestly and must not replace inventory obligations. The current audit deliberately leaves exact item-to-unit lexical and character allocations unfinished; those are C2 pre-writing checks, not evidence that the entire inventory is already covered.

Every official grammar family has one canonical owner (existing explicit card or planned unit) and two later retrieval locations in `course-plan.json`. The 18 partial families retain their existing evidence and are completed in their owner unit. Family-level recycling slots must expand into concrete, manageable tasks before batch acceptance. Existing fully introduced families are reviewed rather than relabelled as new.

**Proposed interpretation needing approval:** some official codes combine many patterns—for example 三19 lists a large set of discourse adverbs—while other codes describe the same construction from different grammatical perspectives. “Teach exactly once” means one canonical inventory owner, then tracked subpattern introduction and deliberate reuse. It cannot mean one 70-word card completely teaches an entire broad family. Split broad families into short cards/micro-lessons and record all subpoints; do not stamp complete based on one example. Units below name two or three official families; depth may require more than two or three small cards.

Prerequisites form a chain starting at `s1-u12`, with earlier grammar/character dependencies checked during batch allocation. GF levels 1 and 2 both use `unit.stage: 1`; GF level 3 uses stage 2, consistent with the app's three-stage standard. Global pack orders continue at 13; unit IDs use s1/s2/s3 for level-specific naming. Higher-level IDs must not accidentally change the stage heuristic. New character entries are spread across the words/readings that need them, with recurring recognition checks; no enormous isolated character dump.

Media alternates: first new unit = original drama scene, second = original verse, then repeat. A verse is an original language-learning text, not borrowed lyrics. Sayo reads it rhythmically in her clear voice; singing is not promised. Dialogue characters are written roles, all spoken by the same Sayo identity (cool / playful / soft by appearance order).

## Full proposed unit list

“[review]” indicates an already-introduced family. Codes and content labels refer to the GF2021 inventory; all dialogue and exercise text will be newly authored.

- **s1-u13 — A friend of a friend** (18 new entries). Introduce people without sounding like a form. Grammar: 一05 我、你、您、他、她、我们、你们、他们、她们; 一24 名词、代词或名词性短语作主语
- **s1-u14 — Want to come along?** (18 new entries). Invite someone and accept or decline gently. Grammar: 一03 想、要; 一13 还1、也
- **s1-u15 — Wait, which one?** (18 new entries). Ask follow-up questions in a group chat. Grammar: 一04 多、多少、几、哪、哪儿、哪里、哪些、什么、谁、怎么; 一46 用“多、多少、几、哪、哪儿、哪里、哪些、什么、谁、怎么”提问
- **s1-u16 — This one or that one?** (18 new entries). Point out items and describe the one you mean. Grammar: 一06 这、那、这儿、那儿、这里、那里、这些、那些、别的、有的; 一27 名词性词语、形容词性词语、数量短语作定语
- **s1-u17 — Cooking for the group** (18 new entries). Count portions and share a simple recipe. Grammar: 一07 一、二/两、三、四、五、六、七、八、九、零；十、百；半; 一23 数量短语
- **s1-u18 — Our shared kitchen** (17 new entries). Explain what the flat has and count household things. Grammar: 一08 杯、本、个、家、间、口、块、页; 一37 “有”字句1：（1）表示领有；（2）表示存在
- **s1-u19 — Whose charger is this?** (17 new entries). Return belongings and state who needs what. Grammar: 一20 的1、地; 一26 名词、代词或名词性短语作宾语
- **s1-u20 — What are you doing now?** (17 new entries). Send a voice message without interrupting. Grammar: 一11 马上、先、有时、在、正、正在; 一42 （1）……在/正在+动词 （2）……在/正/正在+动词……+呢 （3）……呢
- **s1-u21 — Our weekday routines** (17 new entries). Describe habits and fit study around daily life. Grammar: 一12 常、常常、再1; 一28 副词、形容词作状语； 表示时间、处所的词语作状语
- **s1-u22 — No, I meant tomorrow** (17 new entries). Check and correct plans politely. Grammar: 一14 别、不、没、没有; 一48 用正反疑问形式提问
- **s1-u23 — Meet me outside** (17 new entries). Set a meeting place and a precise time. Grammar: 一16 在; 一29 主谓句1：动词谓语句; 一44 （1）年、月、日、星期表示法（2）钟点表示法
- **s1-u24 — Bring your friends too** (17 new entries). Connect people and coordinate who is coming. Grammar: 一17 跟1、和1; 一19 跟2、还是、和2
- **s1-u25 — That looks great on you** (17 new entries). Give specific, natural compliments. Grammar: 一09 非常、很、太、真、最; 一30 主谓句2：形容词谓语句; 一35 感叹句
- **s1-u26 — Which place is quieter?** (17 new entries). Compare two places and choose together. Grammar: 一18 比; 一38 比较句1：（1）A比B +形容词（2）A没有B +形容词
- **s1-u27 — Walk and talk** (17 new entries). Plan two activities together. Grammar: 一10 都1、一块儿、一起; 一39 （1）不用关联词语 （2）用关联词语：一边……，一边……；……，也……
- **s1-u28 — Are we still on?** (17 new entries). Confirm plans in a chat and ask real questions. Grammar: 一22 吧1、了2、吗、呢; 一33 （1）是非问句（2）特指问句（3）选择问句（4）正反问句; 一45 用“吗”提问
- **s1-u29 — Find us at the entrance** (17 new entries). Read short signs and send directions. Grammar: 一01 上、下、里、外、前、后、左、右、东、南、西、北；上边、下边、 里边、外边、前边、后边、左边、右边、东边、南边、西边、北边; 一31 非主谓句
- **s1-u30 — My first month here** (17 new entries). Introduce a neighbourhood and write a short recap. Grammar: 一25 动词或动词性短语、形容词或形容词性短语作谓语; 一32 陈述句; 一36 （1）表示等同或类属；（2）表示说明或特征；（3）表示存在
- **s2-u01 — Joining the friend group** (22 new entries). Refer to people and link ideas naturally. Grammar: 二06 别人、大家、它、它们、咱、咱们、自己; 二37 基本结构类型：（1）联合短语（2）偏正短语（3）动宾短语（4）动补短语（5）主谓短语; 二01 （1）可能；（2）可以；（3）会
- **s2-u02 — What should I bring?** (22 new entries). Ask for advice before visiting someone. Grammar: 二02 该、应该; 二75 用“好吗/可以吗/行吗/怎么样”提问
- **s2-u03 — Maybe another night** (22 new entries). Decline warmly and suggest another plan. Grammar: 二03 愿意; 二45 还是……吧
- **s2-u04 — Why that restaurant?** (22 new entries). Ask about preferences and reasons. Grammar: 二05 多久、为什么、怎么样、怎样; 二76 用“什么时候、什么样、为什么、怎么样、怎样”提问
- **s2-u05 — One more practice round** (22 new entries). Arrange practice and count repetitions. Grammar: 二04 动词重叠：AA、A一A、A了A、ABAB; 二11 遍、次、场、回、下; 二52 数量补语1：动词+动量补语
- **s2-u06 — That post you sent me** (22 new entries). Refer back to a post without repeating everything. Grammar: 二07 那么、那样、这么、这样; 二38 其他结构类型1：（1）“的”字短语（2）连谓短语
- **s2-u07 — Dress code? Sort of** (22 new entries). Describe styles without judging the person. Grammar: 二08 AA、AABB; 二41 形容词性短语; 二46 又……又……
- **s2-u08 — Our weekend budget** (22 new entries). Agree spending limits and approximate numbers. Grammar: 二09 千、万、亿; 二73 概数表示法1： （1）数词+多+量词（2）数词+量词+多
- **s2-u09 — A little gift for you** (22 new entries). Give and send gifts politely. Grammar: 二10 层、封、件、条、位; 二61 （1）主语+动词+宾语1+宾语2 （2）主语+动词+给+宾语1+宾语2
- **s2-u10 — Before the show starts** (22 new entries). Plan time before and after an event. Grammar: 二12 分钟、年、天、周; 二47 （在）……以前/以后/前/后; 二81 要/快要/就要……了
- **s2-u11 — A bit too loud for me** (22 new entries). Compare venues and explain your comfort. Grammar: 二13 多、多么、好、更、十分、特别、挺、有（一）点儿; 二58 比较句2： （1）A比B +形容词+数量补语（2）A比B +更/还+形容词（3）A不如B（+形容词）（4）A有B（+这么/那么）+形容词
- **s2-u12 — Ordering for everyone** (22 new entries). Count the whole order and check preferences. Grammar: 二14 全、一共、只; 二39 名词性短语
- **s2-u13 — Sorry, I'm running late** (22 new entries). Update friends and decide when to leave. Grammar: 二15 刚、刚刚、还2、忽然、一直、已经; 二20 才1、都2、就2、正好; 二80 该……了
- **s2-u14 — Message me when you arrive** (22 new entries). Coordinate a sequence and repeated plans. Grammar: 二16 重新、经常、老、老是、又; 二62 （1）不用关联词语（2）用关联词语：先……，再/然后……; 二69 一……就……
- **s2-u15 — That is exactly what I meant** (22 new entries). Use emphasis without sounding annoyed. Grammar: 二17 就1; 二74 用“就”表示强调
- **s2-u16 — You did that on purpose?** (22 new entries). Tease lightly and check your interpretation. Grammar: 二18 故意; 二79 用“吧”提问; 二78 用“是不是”提问
- **s2-u17 — If it rains, plan B** (22 new entries). Make a backup plan with clear conditions. Grammar: 二19 必须、差不多、好像、也许; 二66 （1）不用关联词语（2）用关联词语：如果……，就……；……的话，就……; 二67 只要……，就……
- **s2-u18 — Taking turns as host** (22 new entries). Discuss roles and explain activities. Grammar: 二21 当; 二40 动词性短语
- **s2-u19 — Getting across town** (22 new entries). Explain a route and direction of travel. Grammar: 二22 往; 二23 向1
- **s2-u20 — How did you meet?** (22 new entries). Explain a first meeting and its circumstances. Grammar: 二24 从2; 二60 “是……的”句1：强调时间、地点、方式、动作者
- **s2-u21 — We feel the same way** (22 new entries). React to a friend and compare experiences. Grammar: 二25 对; 二59 比较句3：（1）A跟B一样/相同（2）A跟B一样+形容词
- **s2-u22 — Close enough to walk?** (22 new entries). Compare distance and measurable differences. Grammar: 二27 离; 二53 数量补语2：形容词+数量补语
- **s2-u23 — Doing a friend a favour** (22 new entries). Explain whom an action benefits. Grammar: 二28 为1; 二55 “有”字句2：（1）表示评价、达到； （2）表示比较（见“比较句 2-（4）”）
- **s2-u24 — Rice or noodles tonight?** (22 new entries). Discuss alternatives and reach one choice. Grammar: 二29 或、或者; 二64 （1）不用关联词语（2）用关联词语：（是）……，还是……
- **s2-u25 — A complaint, gently** (22 new entries). Mention a problem while acknowledging the good. Grammar: 二30 不过、但、但是、而且、那、如果、虽然、只要; 二65 （1）不用关联词语（2）用关联词语：虽然……，但是/可是……；……，不过……
- **s2-u26 — How was my singing?** (22 new entries). Describe performance instead of guessing scores. Grammar: 二31 得; 二51 状态补语1：动词+得+形容词性词语
- **s2-u27 — Have you tried this before?** (22 new entries). Swap experiences before trying something new. Grammar: 二32 过; 二71 用动态助词“过”表示
- **s2-u28 — A room full of friends** (22 new entries). Describe the scene and ongoing actions. Grammar: 二33 着; 二56 存现句1：表示存在（1）处所+是（+数量短语）+名词（见“‘是’字句（3）”）（2）处所+有+数量短语+名词（见“‘有’字句1-（2）”）（3）处所+动词+着（+数量短语）+名词; 二70 动词+着 （1）表示状态的持续（2）表示动作的持续
- **s2-u29 — You, me, and all that** (22 new entries). Understand omitted words and casual chat endings. Grammar: 二34 啊1、吧2、的2; 二43 什么的; 二77 用“呢”构成的省略式疑问句“代词/名词+呢？”提问
- **s2-u30 — Dropping by briefly** (22 new entries). Understand conditional phrasing and short waits. Grammar: 二35 的话、等; 二42 不一会儿; 二36 喂
- **s2-u31 — Getting better together** (22 new entries). Describe progress and add a stronger point. Grammar: 二44 越来越; 二63 （1）不用关联词语（2）用关联词语：……，更/还……；不但……，而且……
- **s2-u32 — Not everyone has the same story** (22 new entries). Give background and short nominal statements. Grammar: 二48 名词、代词、数词、数量短语、名词性短语作谓语; 二54 主谓句3：名词谓语句
- **s2-u33 — Let's finish cooking first** (21 new entries). Complete a task and move on to the next one. Grammar: 二49 结果补语1：动词+错/懂/干净/好/会/清楚/完; 二50 趋向补语1 简单趋向补语的趋向意义用法： （1）动词+来/去（2）动词+上/下/进/出/起/过/回/开; 二57 连动句1：表示前后动作先后发生
- **s2-u34 — Why the evening worked** (21 new entries). Explain causes, thank recipients, and recap order. Grammar: 二68 （1）不用关联词语（2）用关联词语：因为……，所以……; 二26 [review] 给; 二72 [review] 序数表示法
- **s3-u01 — Nicknames in the group** (22 new entries). Understand affectionate names and word endings. Grammar: 三01 第-、老-、小-; 三02 -儿、-家、-们、-头、-子
- **s3-u02 — Anyone can join** (22 new entries). Invite freely and express courage without pressure. Grammar: 三03 敢; 三07 疑问代词的非疑问用法 （1）任指用法 ①疑问代词+都……②疑问代词……疑问代词……（2）不定指用法
- **s3-u03 — We need volunteers** (22 new entries). Assign responsibilities and address a whole group. Grammar: 三04 需要; 三08 各、各位、各种、每、任何
- **s3-u04 — Could you ask them for me?** (22 new entries). Ask for help and pass a request along. Grammar: 三05 动宾式离合词：帮忙、点头、放假、干杯、见面、结婚、看病、睡觉、洗澡、理发、说话; 三57 兼语句1 表使令：主语+叫/派/请/让……+宾语1 +动词+宾语2
- **s3-u05 — Found it at last** (22 new entries). Report finding something and completing an action. Grammar: 三06 动补式离合词：打开、看见、离开、完成; 三46 结果补语2：动词+到/住/走
- **s3-u06 — Dinner for a big group** (22 new entries). Count objects and portions in a busy restaurant. Grammar: 三09 把、行、架、群、束、双、台、张、支、只、种; 三10 顿、口、眼
- **s3-u07 — A little for each person** (22 new entries). Share food and distribute tasks evenly. Grammar: 三11 量词重叠：AA; 三33 数量重叠：数词+量词+数词+量词
- **s3-u08 — Our karaoke practice** (22 new entries). Compare performance and improvements tactfully. Grammar: 三12 比较、更加、还3、相当; 三58 比较句4： （1）A比B +动词+得+形容词 （2）A不比B +形容词 （3）A +动词+得+比+ B +形容词 （4）A比B +多/少/早/晚+动词+数量短语
- **s3-u09 — Only a few places left** (22 new entries). Discuss limited availability and plentiful supplies. Grammar: 三13 光、仅、仅仅、就3、至少; 三37 有的是
- **s3-u10 — An old friend's surprise visit** (22 new entries). Relate events and changes since a past time. Grammar: 三14 本来、才2、曾经、从来、赶紧、赶快、立刻、连忙、始终、已、早已; 三21 自从
- **s3-u11 — The habits we keep** (22 new entries). Talk about typical behaviour and duration. Grammar: 三15 通常、往往、总、总是; 三51 数量补语4（动词+时量补语）：表示动作持续的时间
- **s3-u12 — Let's give it another go** (22 new entries). Coordinate another attempt and mutual help. Grammar: 三16 再2; 三17 互相、尽量、亲自、相互
- **s3-u13 — Tentative plans, honest answers** (22 new entries). Offer a possibility without overpromising. Grammar: 三18 大概、恐怕; 三69 要是……，就……
- **s3-u14 — Is that really what happened?** (22 new entries). Separate guesses from facts and question a claim. Grammar: 三19 白、并1、当然、到底、反正、根本、果然、简直、绝对、难道、其实、千万、确实、只好、终于; 三76 用反问句表示强调 反问句1：不是……吗？/难道……吗？
- **s3-u15 — Who is organising the event?** (22 new entries). Explain responsibility and agreed instructions. Grammar: 三20 由1; 三29 按、按照
- **s3-u16 — Bring it over here** (22 new entries). Give precise directions while moving things. Grammar: 三22 朝; 三47 趋向补语2 复合趋向补语的趋向意义用法：动词+出来/出去/过来/过去/回来/回去/进来/进去/ 起来/上来/上去/下来/下去
- **s3-u17 — What matters to you?** (22 new entries). Explain a choice from someone's perspective. Grammar: 三23 为2; 三40 对……来说
- **s3-u18 — Explaining an unfamiliar custom** (22 new entries). Explain whom an action is directed toward and use comparisons. Grammar: 三24 向2; 三41 像……一样
- **s3-u19 — A proper apology** (22 new entries). Explain causes without using them as excuses. Grammar: 三25 由于1、因为; 三71 （由于）……，所以/因此……
- **s3-u20 — A gift with a reason** (22 new entries). Explain the purpose of a plan or gift. Grammar: 三26 为了; 三72 为了……，……
- **s3-u21 — Please put it by the door** (22 new entries). Coordinate a delivery and its result. Grammar: 三27 把、被、叫、让; 三54 “把”字句1：表处置 （1）主语+把+宾语+动词+在/到+处所（2）主语+把+宾语1 +动词（+给）+宾语2（3）主语+把+宾语+动词+结果补语/趋向补语/状态补语
- **s3-u22 — Everyone except me?** (22 new entries). Discuss exceptions without losing the group's meaning. Grammar: 三28 除了; 三38 除了……（以外），……还/也/都……
- **s3-u23 — Only if everyone agrees** (22 new entries). Set conditions and add connected reasons. Grammar: 三30 并且、不光、不仅、另外、要是、因此、由于2、只有; 三70 只有……，才……
- **s3-u24 — The joke in the chat** (22 new entries). Hear a question tone and understand a laugh in context. Grammar: 三31 哈哈; 三78 用疑问语调表示疑问
- **s3-u25 — The friend I mentioned** (22 new entries). Build descriptions and whole-sentence predicates. Grammar: 三32 其他结构类型2：（1）介宾短语（2）方位短语（3）兼语短语（4）同位短语; 三53 主谓句4：主谓谓语句
- **s3-u26 — It's good, but not perfect** (22 new entries). Give balanced criticism and compact descriptions. Grammar: 三34 不A不B; 三68 ……X是X，就是/不过……
- **s3-u27 — How does this photo look?** (22 new entries). Distinguish appearance from certainty. Grammar: 三35 看起来; 三36 看上去
- **s3-u28 — Starting next week** (22 new entries). Describe a starting point and elapsed time. Grammar: 三39 从……起; 三52 数量补语5（动词+时量补语）：表示动作结束后到某个时间点的间隔时间
- **s3-u29 — Practice makes it easier** (22 new entries). Link gradual changes and describe repeated performance. Grammar: 三42 越……越……; 三59 主语+动词+宾语+动词+补语
- **s3-u30 — Learning with a purpose** (22 new entries). Use activities as subjects and discuss plans. Grammar: 三43 动词或动词性短语、形容词或形容词性短语作主语; 三44 动词或动词性短语、形容词或形容词性短语和主谓短语作宾语
- **s3-u31 — Different ways to get there** (22 new entries). Describe a chosen method and the item it identifies. Grammar: 三45 动词或动词性短语、主谓短语作定语; 三56 连动句2： （1）前一动作是后一动作的方式（2）后一动作是前一动作的目的
- **s3-u32 — Can we follow this scene?** (22 new entries). Discuss ability, difficulty and repetitions with an object. Grammar: 三48 可能补语1：动词+得/不+动词/形容词；动词+得/不+了; 三50 数量补语 3（动词+动量补语）：宾语和动量补语共现
- **s3-u33 — That was seriously funny** (22 new entries). React with emphasis and express a strong negative. Grammar: 三49 程度补语1：形容词/心理动词+得很/极了/死了; 三75 用“一点儿也不……”表示强调
- **s3-u34 — The parcel was moved** (22 new entries). Describe what happened without blaming someone unfairly. Grammar: 三55 被动句1：主语+被/叫/让+宾语+动词+其他成分; 三77 用“是”表示强调
- **s3-u35 — Two hobbies, one evening** (22 new entries). Add parallel ideas without collapsing them. Grammar: 三60 （也）……，也……; 三63 又……，又……
- **s3-u36 — Part of me wants to go** (22 new entries). Describe changing choices and two sides of a decision. Grammar: 三61 一会儿……，一会儿……; 三62 一方面……，另一方面……
- **s3-u37 — Planning something together** (22 new entries). Explain steps and add connected information. Grammar: 三64 首先……，然后……; 三65 ……，并且……
- **s3-u38 — More than one good option** (22 new entries). Expand a reason and discuss mutually exclusive possibilities. Grammar: 三66 不仅/不光……，还/而且……; 三67 不是……，就是……
- **s3-u39 — Splitting the trip costs** (22 new entries). Estimate amounts and link completed actions. Grammar: 三73 ……了……（就）……; 三74 概数表示法2： （1）用“大概、大约、几”表示概数（2）相邻数词连用表示概数（3）用“左右、前后”表示概数
- **s3-u40 — The party is already over** (22 new entries). React to a late situation and accept a small compromise. Grammar: 三79 都……了; 三80 X就X（点儿）吧
- **s3-u41 — Come on, I'm only joking** (22 new entries). Use friendly retorts and recognise when they are too blunt. Grammar: 三81 X什么（啊）; 三19 [review] 白、并1、当然、到底、反正、根本、果然、简直、绝对、难道、其实、千万、确实、只好、终于
- **s3-u42 — Drama night without peeking** (22 new entries). Transfer open reference and possibility complements to a scene. Grammar: 三07 [review] 疑问代词的非疑问用法 （1）任指用法 ①疑问代词+都……②疑问代词……疑问代词……（2）不定指用法; 三48 [review] 可能补语1：动词+得/不+动词/形容词；动词+得/不+了
- **s3-u43 — A song that tells a story** (22 new entries). Transfer emotion and comparisons to original lyrical reading. Grammar: 三49 [review] 程度补语1：形容词/心理动词+得很/极了/死了; 三58 [review] 比较句4： （1）A比B +动词+得+形容词 （2）A不比B +形容词 （3）A +动词+得+比+ B +形容词 （4）A比B +多/少/早/晚+动词+数量短语
- **s3-u44 — Resolve it in the group chat** (21 new entries). Combine disposal and passive structures in a social problem. Grammar: 三54 [review] “把”字句1：表处置 （1）主语+把+宾语+动词+在/到+处所（2）主语+把+宾语1 +动词（+给）+宾语2（3）主语+把+宾语+动词+结果补语/趋向补语/状态补语; 三55 [review] 被动句1：主语+被/叫/让+宾语+动词+其他成分

## Schema and handoff decisions before C2

1. **Second reading:** current `ContentPack` accepts one `reading`; the compiler/validator/audio manifest do not process a second media reading. Propose additive `extraReadings?: PackText[]` with matching compilation, reader routing, pinyin/content checks and audio manifest coverage. Preserve old packs unchanged. Never put extra fields into JSON and pretend they work. Claude needs to coordinate this reader-facing seam; no Watch/dictionary/drill changes are included here.
2. **Inventory alignment:** keep GF2021 source-row/sense evidence separately from the current minimum-level lookup. Propose additive sense-specific reference metadata rather than changing a shared word's level indiscriminately. Reconcile any required correction before the affected packs are generated.
3. **Grammar and reading length:** approve family/subpoint tracking and the level-3 core/stretch distinction above. Final level-3 units consolidate grammar rather than adding artificial points.
4. **Characters/known words:** the existing validator's 95% coverage message uses a character proxy and allows 85–95% as a warning. That is not a proven 95% known-word rule. Each new batch must separately segment/review connected text and enforce the brief's ≥95% lexical coverage, with glosses accounted for and explicit new-character handling. Coordinate segmentation evidence with Claude's dictionary work; do not claim the old gate already proves this.
5. **Read-only baseline:** this pass does not enable live sync, merge device progress, deploy, push, change the voice base, or introduce dependencies.

## C2 batch acceptance and native-quality review

For each four-unit batch:

- Allocate source vocabulary rows, character prerequisites, grammar subpoints and retrievals first. Keep a ledger of missing/introduced/recycled items and senses. Do not equate completion with learner mastery.
- Author mainland, neutral/casual Chinese from the communicative goal. Then review it independently for unnatural literal translation, collocations, pronoun reference, register, real-world plausibility and tone. Self-review is not a native-speaker sign-off: all packs remain **AI-assisted draft** until reviewed. Avoid time-sensitive etiquette claims presented as universal norms.
- Review Vietnamese meanings for natural language; include Sino-Vietnamese readings only where they help, separate from the actual meaning. Verify pinyin using the existing dictionary checker, including polyphones, neutral tones, 一/不 sandhi and erhua.
- Require each new word twice in connected context, with ≥95% lexical readability and appropriate glosses. Start listening questions without transcript/pinyin. Gist, detail and intent questions must be answerable from that dialogue; do not label obvious word matching as inference.
- Check exactly one defensible answer, varied answer positions, plausible distractors and varied true/false outcomes. Inspect accept regexes against positive and near-miss negative replies. Supported answers remain supported.
- Keep the approved B-half timbre. Vocabulary/examples/media = clear; conversation roles use cool, playful, soft in order. Preserve context `say` for particles and polyphones. Generate all required clips locally and verify mapping, existence, decoding, duration, loudness and hashes. Structural audio checks do not prove tone accuracy: listen to new single-syllable clips, uncertain pronunciations and representative lines before declaring audio reviewed. No device fallback counted as Sayo coverage.
- Run types, all unit tests, packs/pinyin, content/audio validation, browser tests and production build. Inspect listening/reader/extra-media screenshots at required sizes. Fix failures before another batch. Check audio grows on demand and research files are not precached.
- Record changes and unverified native quality in `course-log.md`. The owner revoked batch review stops; continue once every gate passes. Source datasets are reference-only and no copyrighted lyrics/scenes or textbook exercises are added.

## Validation of C1 itself

Automated plan checks: 96 unique units in a continuous prerequisite chain; budgets sum to the audited remaining rows; all 210 grammar families have canonical owners, and every owner has two later retrieval slots. Seven focused audit tests cover the traps above. No new units, speech clips or UI have been produced at C1.

The whole-app check results are recorded in `c1-validation.md`. Claude is changing A/B in the same checkout, so shared runtime failures must be distinguished from these research files. No screenshots are claimed for a changed UI in this pass.

The existing twelve packs build without errors but each emits a warning, mostly for vocabulary used fewer than twice in context; one flags a large set of glossed characters. They do not yet meet every stronger C2 quality requirement. Carry these into the first batch's review/repair ledger rather than treating a successful build as proof of full linguistic quality.

**C2 authorization:** the owner approved the outline and adjustments, confirmed Claude's extraReadings and lexical-readability implementation, and requested completion through s3-u44 without intermediate review stops. Deployment is authorized after the run passes its checks.
