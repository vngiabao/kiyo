import { beforeAll, describe, expect, it } from "vitest";
import { readFileSync } from "node:fs";
import { segment, setDictionaryLoader, toneMarks, lookup, tokenAt, type DictShard } from "../src/dictionary";

beforeAll(() => {
  setDictionaryLoader(async (i) => JSON.parse(readFileSync(`public/dict/${String(i).padStart(3, "0")}.json`, "utf8")) as DictShard);
});

describe("tone marks", () => {
  it("converts numbered pinyin, ü, neutral tone, erhua and proper nouns", () => {
    expect(toneMarks("ni3 hao3")).toBe("nǐhǎo");
    expect(toneMarks("lu:4 se4")).toBe("lǜsè");
    expect(toneMarks("xie4 xie5")).toBe("xièxie");
    expect(toneMarks("yi1 dian3 r5")).toBe("yīdiǎnr");
    expect(toneMarks("Bei3 jing1")).toBe("Běijīng");
    expect(toneMarks("gou3")).toBe("gǒu");
    expect(toneMarks("hui4")).toBe("huì");
    expect(toneMarks("liu2")).toBe("liú");
  });
});

describe("lookup", () => {
  it("finds simplified and traditional forms, everyday reading first", async () => {
    expect((await lookup("看"))[0].p).toBe("kàn");
    expect((await lookup("电视剧"))[0].m).toMatch(/TV/i);
    const trad = await lookup("電視");
    expect(trad[0].s).toBe("电视");
    expect((await lookup("学生"))[0].h).toBe(1);
  });
});

// Hand-segmented subtitle- and lyric-style lines ("/" between words). Original sentences.
const gold = `
你/在/看/什么/？
我/想/看/中国/电视剧/。
他们/说话/太/快/了/。
你/看懂/了/吗/？
今天/的/天气/怎么样/？
我/觉得/这/首/歌/很/好听/。
明天/我们/一起/去/唱歌/吧/！
不好意思/，/我/没/听懂/。
你/叫/什么/名字/？
我/是/美国人/。
这/件/衣服/太/贵/了/。
便宜/一点儿/吧/！
你/有/空/吗/？
我们/周末/见面/吧/。
你/怎么/又/忘/了/？
别/生气/，/我/请/你/吃饭/。
我/一直/在/等/你/。
你/为什么/不/给/我/打电话/？
我/喜欢/你/很/久/了/。
对不起/，/我/错/了/。
没关系/，/下次/注意/。
你/真的/要/走/吗/？
我/不/想/让/你/走/。
他/是/我/最/好/的/朋友/。
你/还/记得/我/吗/？
我们/以前/是/同学/。
这/是/我/第一/次/来/北京/。
我/每天/都/很/忙/。
你/吃饭/了/吗/？
我/已经/吃/过/了/。
你/想/喝/点儿/什么/？
给/我/一/杯/咖啡/。
他/在/医院/工作/。
她/的/妈妈/是/老师/。
我/明白/你/的/意思/。
你/说/得/对/。
我们/走/吧/，/快/下雨/了/。
外面/风/很/大/。
你/怎么/不/说话/？
我/有/一个/秘密/。
你/能/帮/我/一下/吗/？
当然/可以/。
谢谢/你/的/帮助/。
不/客气/。
这个/问题/很/难/。
我/不/知道/怎么/办/。
你/别/担心/。
一切/都/会/好/的/。
我/爱/你/。
你/爱/我/吗/？
我们/在/一起/吧/。
我/想/你/了/。
你/在/哪儿/？
我/马上/到/。
等/我/一下/。
你/今天/很/漂亮/。
我/的/手机/没/电/了/。
你/的/电话/号码/是/多少/？
我们/加/个/微信/吧/。
我/给/你/发/信息/。
他/开车/送/我/回家/。
从/这儿/到/机场/远/吗/？
坐/地铁/要/四十/分钟/。
你/看/，/那/是/什么/？
我/第一次/见到/你/的/时候/。
时间/过/得/真/快/。
我们/好久不见/了/。
你/最近/怎么样/？
还/可以/，/你/呢/？
我/要/去/上班/了/。
晚上/一起/吃饭/吧/。
我/请客/。
这/家/饭馆/的/菜/很/好吃/。
服务员/，/买单/！
你/喜欢/什么/样/的/音乐/？
我/最/喜欢/这/首/歌/。
你/会/唱/中文歌/吗/？
我/只/会/唱/一点儿/。
跟/我/一起/唱/吧/。
月亮/代表/我/的/心/。
你/问/我/爱/你/有/多/深/。
星期六/是/我/的/生日/。
生日/快乐/！
我们/给/她/买/了/一个/蛋糕/。
你/今年/多/大/？
我/二十五/岁/。
我/的/家/在/上海/。
你/是/哪国人/？
我/在/学/中文/。
汉字/有点儿/难/。
他/身体/不/舒服/。
你/应该/多/休息/。
医生/说/没/什么/大/问题/。
我/今天/不/能/去/上课/。
老师/，/我/病/了/。
我/会/努力/的/。
你/一定/可以/的/。
加油/！
`
  .trim()
  .split("\n");

describe("segmentation on subtitle and lyric lines", () => {
  it("matches the hand split on at least 95% of word boundaries", async () => {
    let right = 0,
      total = 0;
    const misses: string[] = [];
    for (const line of gold) {
      const want = line.split("/");
      const got = (await segment(want.join(""))).map((t) => t.text);
      // Boundary F1 on character offsets.
      const cuts = (ws: string[]) => {
        const s = new Set<number>();
        let at = 0;
        for (const w of ws) s.add((at += Array.from(w).length));
        return s;
      };
      const a = cuts(want),
        b = cuts(got);
      right += [...b].filter((x) => a.has(x)).length;
      total += Math.max(a.size, b.size);
      if (got.join("/") !== want.join("/")) misses.push(`${want.join("/")}  →  ${got.join("/")}`);
    }
    const accuracy = right / total;
    console.log(`segmentation: ${(accuracy * 100).toFixed(1)}% of boundaries on ${gold.length} lines; ${misses.length} lines differ`);
    if (misses.length) console.log(misses.slice(0, 30).join("\n"));
    expect(accuracy).toBeGreaterThanOrEqual(0.95);
  });
  it("gets the classic traps right", async () => {
    const split = async (s: string) => (await segment(s)).map((t) => t.text).join("/");
    expect(await split("我想看中国电视剧")).toContain("看/中国");
    expect(await split("不好意思")).toBe("不好意思");
    expect(await split("你看懂了吗")).toContain("看懂");
  });
  it("finds the word around a tapped character, keeping punctuation separate", async () => {
    const tokens = await segment("你看懂了吗？");
    expect(tokenAt(tokens, 2)?.text).toBe("看懂");
    expect(tokenAt(tokens, 5)?.entries).toEqual([]);
  });
});
