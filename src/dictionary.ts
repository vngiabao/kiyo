/**
 * Offline Chinese dictionary (CC-CEDICT, CC BY-SA 4.0), built by scripts/build-dictionary.ts
 * into public/dict/NNN.json shards. Shards load on demand and are cached by the service
 * worker ("kiyo-dict"), so the install stays small and lookups work offline once used.
 *
 * Subtitles have no spaces, so a tapped character is resolved to the WORD around it:
 * forward and backward longest-match segmentation, keeping the split with fewer words
 * (then fewer single characters, then the backward one, which handles 看中国 → 看 + 中国).
 */
export interface DictEntry {
  /** Pinyin with tone marks, syllables joined (dictionary form, no tone sandhi). */
  p: string;
  /** Up to three senses, "; "-separated. */
  m: string;
  /** Measure words, e.g. "个 gè · 只 zhī". */
  c?: string;
  /** HSK 3.0 level (7 = levels 7–9). */
  h?: number;
  /** Set on traditional-form keys: the simplified word. */
  s?: string;
}
export type DictShard = Record<string, DictEntry[]>;
export const SHARDS = 256;
export const shardOf = (key: string) => (key.codePointAt(0) ?? 0) % SHARDS;
const MAX_WORD = 8;
const isHan = (ch: string) => /\p{Script=Han}/u.test(ch);

// ---------- Pinyin ----------
const marks: Record<string, string> = { a: "āáǎà", e: "ēéěè", i: "īíǐì", o: "ōóǒò", u: "ūúǔù", ü: "ǖǘǚǜ" };
function markSyllable(s: string): string {
  const m = s.match(/^([A-Za-zü:]+?)([1-5])?$/);
  if (!m) return s;
  let base = m[1].replace(/u:|v/g, "ü").replace(/U:|V/g, "Ü");
  const tone = Number(m[2] ?? 5);
  if (tone === 5) return base;
  const lower = base.toLowerCase();
  let at = lower.search(/[ae]/);
  if (at < 0) at = lower.indexOf("ou");
  if (at < 0) {
    for (let i = lower.length - 1; i >= 0; i--)
      if ("aeiouü".includes(lower[i])) {
        at = i;
        break;
      }
  }
  if (at < 0) return base;
  const ch = lower[at];
  const marked = marks[ch][tone - 1];
  base = base.slice(0, at) + (base[at] === ch ? marked : marked.toUpperCase()) + base.slice(at + 1);
  return base;
}
/** "ni3 hao3" → "nǐhǎo"; "yi1 dian3 r5" → "yīdiǎnr"; "Bei3 jing1" → "Běijīng". */
export function toneMarks(numbered: string): string {
  const out: string[] = [];
  for (const tok of numbered.trim().split(/\s+/)) {
    if (/^r5?$/i.test(tok) && out.length) out[out.length - 1] += "r";
    else if (/^[A-Za-zü:]+[1-5]?$/.test(tok)) out.push(markSyllable(tok));
    else out.push(` ${tok} `);
  }
  return out.join("").replace(/\s+/g, " ").trim();
}

// ---------- Loading ----------
type Loader = (shard: number) => Promise<DictShard>;
const defaultLoader: Loader = async (i) => {
  const res = await fetch(`/dict/${String(i).padStart(3, "0")}.json`);
  if (!res.ok || !/json/i.test(res.headers.get("content-type") ?? "")) throw new Error("The dictionary couldn't load. Try again when you're online.");
  return (await res.json()) as DictShard;
};
let loader: Loader = defaultLoader;
const shards = new Map<number, Promise<DictShard>>();
/** Tests (and Node scripts) load shards from disk. */
export function setDictionaryLoader(next: Loader) {
  loader = next;
  shards.clear();
}
function shard(i: number) {
  let p = shards.get(i);
  if (!p) {
    p = loader(i).catch((e) => {
      shards.delete(i);
      throw e;
    });
    shards.set(i, p);
  }
  return p;
}
/** Load every shard a line could need (one per distinct character). */
async function prepare(text: string) {
  const idx = [...new Set(Array.from(text).filter(isHan).map(shardOf))];
  const loaded = await Promise.all(idx.map(shard));
  const map = new Map<number, DictShard>(idx.map((s, k) => [s, loaded[k]]));
  return (word: string) => map.get(shardOf(word))?.[word];
}
export async function lookup(word: string): Promise<DictEntry[]> {
  return (await shard(shardOf(word)))[word] ?? [];
}

// ---------- Segmentation ----------
export interface Token {
  text: string;
  start: number;
  end: number;
  /** Dictionary entries for this word (empty for punctuation or unknown). */
  entries: DictEntry[];
}
type Has = (w: string) => DictEntry[] | undefined;
function forward(run: string[], has: Has): string[] {
  const out: string[] = [];
  for (let i = 0; i < run.length; ) {
    let n = Math.min(MAX_WORD, run.length - i);
    while (n > 1 && !has(run.slice(i, i + n).join(""))) n--;
    out.push(run.slice(i, i + n).join(""));
    i += n;
  }
  return out;
}
function backward(run: string[], has: Has): string[] {
  const out: string[] = [];
  for (let j = run.length; j > 0; ) {
    let n = Math.min(MAX_WORD, j);
    while (n > 1 && !has(run.slice(j - n, j).join(""))) n--;
    out.unshift(run.slice(j - n, j).join(""));
    j -= n;
  }
  return out;
}
const singles = (ws: string[]) => ws.filter((w) => Array.from(w).length === 1).length;
const longest = (ws: string[]) => Math.max(...ws.map((w) => Array.from(w).length));
export function splitRun(run: string[], has: Has): string[] {
  const f = forward(run, has),
    b = backward(run, has);
  if (f.length !== b.length) return f.length < b.length ? f : b;
  // Same number of words: prefer the split with more everyday (HSK-listed) words
  // (欢迎/来 over 欢/迎来), then the rules below.
  const everyday = (ws: string[]) => ws.filter((w) => has(w)?.some((e) => e.h)).length;
  if (everyday(f) !== everyday(b)) return everyday(f) > everyday(b) ? f : b;
  // Same number of words: prefer the split containing the longer word (好久不见/了 over
  // 好久/不见了), then fewer single characters, then backward (看/中国 over 看中/国).
  if (longest(f) !== longest(b)) return longest(f) > longest(b) ? f : b;
  if (singles(f) !== singles(b)) return singles(f) < singles(b) ? f : b;
  return b;
}

// ---------- Numbers ----------
const DIGITS = "零一二三四五六七八九";
const NUMERAL = /^[零一二两三四五六七八九十百千万亿]+$/;
const numeralPy: Record<string, string> = { 零: "líng", 一: "yī", 二: "èr", 两: "liǎng", 三: "sān", 四: "sì", 五: "wǔ", 六: "liù", 七: "qī", 八: "bā", 九: "jiǔ", 十: "shí", 百: "bǎi", 千: "qiān", 万: "wàn", 亿: "yì" };
/** 二十五 → 25; 一百二十 → 120; 两千 → 2000. Null if it isn't a number word. */
export function numberValue(s: string): number | null {
  if (!NUMERAL.test(s)) return null;
  let total = 0,
    section = 0,
    digit = 0;
  for (const ch of s) {
    const d = ch === "两" ? 2 : DIGITS.indexOf(ch);
    if (d >= 0) digit = d;
    else if (ch === "十" || ch === "百" || ch === "千") {
      section += (digit || 1) * (ch === "十" ? 10 : ch === "百" ? 100 : 1000);
      digit = 0;
    } else {
      total += (section + digit) * (ch === "万" ? 1e4 : 1e8);
      section = 0;
      digit = 0;
    }
  }
  return total + section + digit;
}
/** Join neighbouring numeral words (二 + 十五 → 二十五). */
function mergeNumbers(words: string[]): string[] {
  const out: string[] = [];
  for (const w of words) {
    const prev = out[out.length - 1];
    if (prev && NUMERAL.test(prev) && NUMERAL.test(w)) out[out.length - 1] = prev + w;
    else out.push(w);
  }
  return out;
}
const numberEntry = (w: string): DictEntry[] => {
  const v = numberValue(w);
  return v === null || Array.from(w).length < 2 ? [] : [{ p: Array.from(w).map((c) => numeralPy[c]).join(""), m: String(v) }];
};
/** Split a subtitle or lyric line into words, with dictionary entries attached. */
export async function segment(line: string): Promise<Token[]> {
  const has = await prepare(line);
  const chars = Array.from(line);
  const tokens: Token[] = [];
  for (let i = 0; i < chars.length; ) {
    if (!isHan(chars[i])) {
      tokens.push({ text: chars[i], start: i, end: i + 1, entries: [] });
      i++;
      continue;
    }
    let j = i;
    while (j < chars.length && isHan(chars[j])) j++;
    let at = i;
    for (const w of mergeNumbers(splitRun(chars.slice(i, j), has))) {
      const n = Array.from(w).length;
      tokens.push({ text: w, start: at, end: at + n, entries: has(w) ?? numberEntry(w) });
      at += n;
    }
    i = j;
  }
  return tokens;
}
/** Synchronous split for scripts that already hold the dictionary in memory: Han words only. */
export function wordsOf(line: string, has: (w: string) => DictEntry[] | undefined): string[] {
  const out: string[] = [];
  const chars = Array.from(line);
  for (let i = 0; i < chars.length; ) {
    if (!isHan(chars[i])) {
      i++;
      continue;
    }
    let j = i;
    while (j < chars.length && isHan(chars[j])) j++;
    out.push(...mergeNumbers(splitRun(chars.slice(i, j), has)));
    i = j;
  }
  return out;
}
export const isNumberWord = (w: string) => numberValue(w) !== null;
/** The word containing character index i (in Array.from(line) positions). */
export const tokenAt = (tokens: Token[], i: number) => tokens.find((t) => i >= t.start && i < t.end);
