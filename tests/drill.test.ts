import { describe, expect, it } from "vitest";
import { drillMaterial, meaningChoices, nextRate, showFor, MIN_SHOW, MAX_SHOW, START_RATE } from "../src/drill";
import { allLessons, phraseById } from "../src/content";

describe("reading drill", () => {
  it("keeps every line on screen between 5/6 s and 7 s", () => {
    expect(showFor("你好", 9)).toBe(MIN_SHOW);
    expect(showFor("我们明天一起去喝咖啡吧", 1.5)).toBe(MAX_SHOW);
    expect(showFor("我们明天一起去喝咖啡吧", 5)).toBeCloseTo(11 / 5);
  });
  it("speeds up after two correct answers and slows down after a miss", () => {
    let s = nextRate(START_RATE, 0, true);
    expect(s).toEqual({ rate: START_RATE, streak: 1 });
    s = nextRate(s.rate, s.streak, true);
    expect(s.rate).toBeGreaterThan(START_RATE);
    expect(s.streak).toBe(0);
    expect(nextRate(4, 1, false).rate).toBeLessThan(4);
    expect(nextRate(1.5, 0, false).rate).toBe(1.5);
  });
  it("only uses lines from finished lessons, built from taught characters", () => {
    expect(drillMaterial(new Set())).toEqual([]);
    const done = new Set(["first", "names", "identity", "language", "coffee", "plans", "s1-u01"]);
    const lines = drillMaterial(done);
    expect(lines.length).toBeGreaterThan(8);
    const taught = new Set(
      allLessons
        .filter((l) => done.has(l.id))
        .flatMap((l) => l.phrases.flatMap((id) => Array.from(phraseById[id]?.hanzi ?? ""))),
    );
    for (const l of lines) for (const ch of Array.from(l.zh)) if (/\p{Script=Han}/u.test(ch)) expect(taught.has(ch), `${ch} in ${l.zh}`).toBe(true);
    for (const l of lines) expect(Array.from(l.zh).filter((c) => /\p{Script=Han}/u.test(c)).length).toBeLessThanOrEqual(16);
  });
  it("offers three different meanings with the answer in varying positions", () => {
    const pool = [
      { zh: "我叫林安", en: "My name is Lin An" },
      { zh: "你是哪国人", en: "Where are you from?" },
      { zh: "我想喝茶", en: "I'd like tea" },
      { zh: "明天见", en: "See you tomorrow" },
    ];
    const positions = new Set<number>();
    for (let seed = 0; seed < 6; seed++) {
      const c = meaningChoices(pool[0], pool, seed);
      expect(new Set(c).size).toBe(3);
      positions.add(c.indexOf(pool[0].en));
    }
    expect(positions.size).toBeGreaterThan(1);
  });
});
