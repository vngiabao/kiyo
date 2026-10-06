// Cross-checks the pinyin of every Chinese line in the content packs against a dictionary.
// Lines are split into words (longest match against the HSK 3.0 list, the base phrases
// and each pack's own vocabulary and glosses); each word's authored syllables must match
// one of its dictionary readings, allowing spoken tone changes of 一/不 and neutral tones.
//   npx tsx scripts/check-pinyin.ts            all packs
//   npx tsx scripts/check-pinyin.ts s1-u03     one unit
import { readFileSync, readdirSync } from "node:fs";
import { isHan, pinyinMatches, syllables, type ContentPack } from "../src/packs";
import { phrases as basePhrases } from "../src/content";
import { taskAudio, plain } from "../src/tasks";

const hsk = JSON.parse(readFileSync("content/hsk/levels.json", "utf8")).words as Record<string, { pinyin: string[] }>;
const dict = new Map<string, Set<string>>();
const addWord = (w: string, py: string) => {
  if (!w || !py) return;
  (dict.get(w) ?? dict.set(w, new Set()).get(w)!).add(py);
};
for (const [w, v] of Object.entries(hsk)) for (const py of v.pinyin) addWord(w, py);
// In phone and room numbers 一 is read yāo, so it can't be confused with 七.
addWord("一", "yāo");
for (const p of basePhrases) if (p.topic !== "sounds") addWord(p.hanzi.replace(/[，。！？、]/g, ""), p.pinyin.replace(/[,.!?]/g, ""));

const only = process.argv[2];
const files = readdirSync("content/packs").filter((f) => f.endsWith(".json") && !f.startsWith("_") && !f.endsWith(".hsk.json"));
let checked = 0,
  unverified = 0,
  problems = 0;
for (const file of files) {
  const pack = JSON.parse(readFileSync(`content/packs/${file}`, "utf8")) as ContentPack;
  if (only && pack.unit.id !== only) continue;
  for (const v of pack.vocabulary) addWord(v.hanzi, v.pinyin);
  for (const t of [pack.dialogue, pack.reading, ...(pack.extraReadings ?? [])]) for (const g of t?.glosses ?? []) addWord(g.hanzi, g.pinyin);
  const lines: { where: string; zh: string; py: string }[] = [];
  const push = (where: string, l?: { zh?: string; py?: string }) => l?.zh && l.py && lines.push({ where, zh: plain(l.zh), py: l.py });
  pack.vocabulary.forEach((v) => push(`word ${v.hanzi} example`, v.example));
  (pack.grammar ?? []).forEach((g) => g.examples.forEach((e, i) => push(`grammar ${g.pattern} ex ${i + 1}`, e)));
  for (const [name, t] of [["dialogue", pack.dialogue], ["reading", pack.reading], ...(pack.extraReadings ?? []).map((r, k) => [`extra reading ${k + 1}`, r] as const)] as const)
    t?.lines.forEach((l, i) => push(`${name} line ${i + 1}`, l));
  (pack.pragmatics ?? []).forEach((x, i) => {
    push(`usage ${i + 1} natural`, x.natural);
    push(`usage ${i + 1} too formal`, x.tooFormal);
    push(`usage ${i + 1} too blunt`, x.tooBlunt);
  });
  pack.conversation?.turns.forEach((t, i) => push(`conversation turn ${i + 1}`, { zh: t.text, py: t.pinyin }));
  for (const task of pack.tasks ?? []) taskAudio(task).forEach((l, i) => l.py && push(`task ${task.id} line ${i + 1}`, l));

  for (const line of lines) {
    const chars = Array.from(line.zh).filter(isHan);
    const sylls = syllables(line.py.replace(/\s+r\b/g, "r"));
    let si = 0;
    const issues: string[] = [];
    // Try each word split at this position, longest first; take the first whose dictionary
    // reading matches what was written (看中国 is 看 + 中国, not 看中 + 国).
    const attempt = (ci: number, len: number) => {
      const word = chars.slice(ci, ci + len).join("");
      const readings = dict.get(word);
      if (!readings) return null;
      const take = syllables([...readings][0]).length || len;
      let chunk = sylls.slice(si, si + take).join(" ");
      let used = len;
      // Erhua after a known word (一点 + 儿 → yìdiǎnr): the -r carries the 儿.
      if (chars[ci + len] === "儿" && /[^e]r$/i.test(chunk) && ![...readings].some((r) => /r$/i.test(r))) {
        chunk = chunk.slice(0, -1);
        used = len + 1;
      }
      return { word, readings, take, chunk, used, ok: [...readings].some((r) => pinyinMatches(word, chunk, r)) };
    };
    for (let ci = 0; ci < chars.length; ) {
      const tries = [5, 4, 3, 2, 1].filter((n) => n <= chars.length - ci).map((n) => attempt(ci, n)).filter((x) => x !== null);
      // A shorter split only counts if what follows is also a dictionary word,
      // so an error can't hide behind an unchecked leftover character.
      const startsWord = (at: number) => at >= chars.length || [1, 2, 3, 4].some((n) => dict.has(chars.slice(at, at + n).join("")));
      const pick = tries.find((x, i) => x.ok && (i === 0 || startsWord(ci + x.used))) ?? tries[0];
      if (!pick) {
        unverified++;
        si++;
        ci++;
        continue;
      }
      if (pick.ok) checked++;
      else issues.push(`${pick.word}: wrote "${pick.chunk}", dictionary has ${[...pick.readings].join(" / ")}`);
      si += pick.take;
      ci += pick.used;
    }
    if (si !== sylls.length) issues.push(`syllable count: text needs ${si}, pinyin has ${sylls.length}`);
    if (issues.length) {
      problems++;
      console.log(`✗ ${pack.unit.id} ${line.where}: ${line.zh}\n    ${line.py}\n    ${issues.join("\n    ")}`);
    }
  }
}
console.log(`\n${checked} words matched the dictionary, ${unverified} characters had no entry (names etc.), ${problems} line(s) to fix.`);
if (problems) process.exitCode = 1;
