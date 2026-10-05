/** Study targets are Kiyo's suggested sequence, not claims of exam readiness. */
export const hskRoadmap = [
  {
    level: 1,
    label: "HSK 1",
    title: "Build a reading base",
    entry:
      "Start here, or use an official sample to confirm your starting point.",
    focus:
      "Recognise common words, identify people and objects, and read numbers and short statements.",
    work: "Complete Standard Course 1 and its workbook. Read each dialogue without its pinyin before replaying the audio.",
  },
  {
    level: 2,
    label: "HSK 2",
    title: "Connect everyday meaning",
    entry:
      "First repair the questions missed on a Level 1 sample, or confirm equivalent prior study.",
    focus:
      "Follow short exchanges, time and location details, comparisons and everyday plans.",
    work: "Complete Standard Course 2 and its workbook. Keep a contrast list for similar words and connect each grammar point to a sentence you can explain.",
  },
  {
    level: 3,
    label: "HSK 3",
    title: "Read connected passages",
    entry:
      "Finish the Level 2 study loop and explain your sample-paper errors without notes.",
    focus:
      "Track who did what and why across sentences; build accurate sentences as well as recognising them.",
    work: "Complete Standard Course 3 and its workbook. Retell each dialogue, reconstruct sentences, and review the language that changes a passage’s meaning.",
  },
  {
    level: 4,
    label: "HSK 4",
    title: "Follow structure and intent",
    entry:
      "Complete the Level 3 loop, including the writing tasks required by your chosen exam version.",
    focus:
      "Follow paragraph order, causes and contrasts; distinguish a speaker’s intention from individual keywords.",
    work: "Work through Standard Course 4 A, then B, with both workbooks. Summarise each passage and explain why each rejected answer is wrong.",
  },
  {
    level: 5,
    label: "HSK 5",
    title: "Read for argument and register",
    entry:
      "Repair Level 4 reading and writing weaknesses before beginning longer timed passages.",
    focus:
      "Extract claims and evidence, infer meaning in context, and choose language that fits the situation.",
    work: "Complete Standard Course 5 A and B with their workbooks. Build a collocation notebook, summarise passages, and revise written responses with qualified feedback.",
  },
  {
    level: 6,
    label: "HSK 6",
    title: "Handle dense material",
    entry:
      "Finish the Level 5 study loop and practise sustained reading without sentence-by-sentence translation.",
    focus:
      "Track complex reasoning, detect language problems, and produce faithful summaries under time pressure.",
    work: "Complete Standard Course 6 A and B with their workbooks. Audit gaps against the official syllabus, then practise long passages and summaries with error explanations.",
  },
  {
    level: 7,
    label: "HSK 7–9",
    title: "Work at advanced depth",
    entry:
      "Build a strong Level 6 foundation, then diagnose your gaps with the official combined 7–9 sample.",
    focus:
      "Academic and professional reading, extended argument, precise register, translation and sustained spoken responses.",
    work: "Use CTI’s combined 7–9 syllabus and sample materials. Work on news, academic and specialist passages, then obtain qualified feedback on writing, translation and speaking. Standard Course ends at 6.",
  },
] as const;
export const roadmapFor = (level: number) =>
  hskRoadmap.find((p) => p.level === level) ?? hskRoadmap[0];
export const hskLevelLabel = (level: number) => roadmapFor(level).label;
