// Builds the offline dictionary used by the Watch player and the reader.
// Source: CC-CEDICT (https://www.mdbg.net/chinese/dictionary?page=cc-cedict), licensed CC BY-SA 4.0.
// The derived files in public/dict/ are CC BY-SA 4.0 too (see THIRD_PARTY_NOTICES.md).
//   npx tsx scripts/build-dictionary.ts            download (cached in .dict-cache/) and build
//   npx tsx scripts/build-dictionary.ts --offline  build from the cached download only
import { gunzipSync, gzipSync } from "node:zlib";
import { createHash } from "node:crypto";
import { existsSync, mkdirSync, readFileSync, rmSync, writeFileSync } from "node:fs";
import { SHARDS, shardOf, toneMarks, type DictEntry, type DictShard } from "../src/dictionary";

const SOURCE = "https://www.mdbg.net/chinese/export/cedict/cedict_1_0_ts_utf-8_mdbg.txt.gz";
const cacheFile = ".dict-cache/cedict.txt.gz";
mkdirSync(".dict-cache", { recursive: true });
if (!process.argv.includes("--offline") || !existsSync(cacheFile)) {
  const res = await fetch(SOURCE);
  if (!res.ok) throw new Error(`Dictionary download failed: ${res.status}`);
  writeFileSync(cacheFile, Buffer.from(await res.arrayBuffer()));
}
const raw = gunzipSync(readFileSync(cacheFile)).toString("utf8");
const sourceDate = raw.match(/#! date=(\S+)/)?.[1] ?? "unknown";

const hsk = JSON.parse(readFileSync("content/hsk/levels.json", "utf8")).words as Record<string, { hsk3?: number }>;

// "個|个[ge4],隻|只[zhi1]" → "个 gè · 只 zhī"
const classifiers = (s: string) =>
  s
    .split(",")
    .map((c) => {
      const m = c.match(/(?:[^|[\]]+\|)?([^|[\]]+)\[([^\]]+)\]/);
      return m ? `${m[1]} ${toneMarks(m[2])}` : "";
    })
    .filter(Boolean)
    .join(" · ");

const isNoise = (d: string) => /^(old |archaic |)variant of |^see [^ ]+$|^used in |^erhua variant of /i.test(d);
const shards: DictShard[] = Array.from({ length: SHARDS }, () => ({}));
let entries = 0,
  dropped = 0;
// Erhua forms (一点儿, 点儿, 这儿) are only "erhua variant of X" in the source; give them X's meaning.
const meaningOf = new Map<string, string>();
for (const line of raw.split("\n")) {
  const m = line.match(/^\S+ (\S+) \[[^\]]*\] \/(.*)\/\s*$/);
  if (!m || meaningOf.has(m[1])) continue;
  const senses = m[2].split("/").filter((d) => d && !d.startsWith("CL:") && !isNoise(d) && !/^surname /i.test(d));
  if (senses.length) meaningOf.set(m[1], senses.slice(0, 3).join("; "));
}
for (const line of raw.split("\n")) {
  if (!line || line.startsWith("#")) continue;
  const m = line.match(/^(\S+) (\S+) \[([^\]]*)\] \/(.*)\/\s*$/);
  if (!m) continue;
  const [, trad, simp, py, defsRaw] = m;
  const defs = defsRaw.split("/").filter(Boolean);
  const cl = defs.filter((d) => d.startsWith("CL:")).map((d) => classifiers(d.slice(3))).join(" · ");
  const senses = defs.filter((d) => !d.startsWith("CL:") && !isNoise(d));
  // Keep "surname X" only when it's all the entry says.
  const useful = senses.filter((d) => !/^surname /i.test(d));
  let meanings = (useful.length ? useful : senses).slice(0, 3);
  if (!meanings.length) {
    const base = defs.map((d) => d.match(/^erhua variant of (?:[^|[\]]+\|)?([^|[\]]+)\[/)?.[1]).find(Boolean);
    if (base && meaningOf.has(base)) meanings = [`${meaningOf.get(base)} (erhua form of ${base})`];
  }
  if (!meanings.length) {
    dropped++;
    continue;
  }
  const entry: DictEntry = { p: toneMarks(py), m: meanings.join("; ") };
  if (cl) entry.c = cl;
  const level = hsk[simp]?.hsk3;
  if (level) entry.h = level;
  for (const key of new Set([simp, trad])) {
    const shard = shards[shardOf(key)];
    const list = (shard[key] ??= []);
    if (key !== simp) {
      // Traditional form: point at the simplified word, but still searchable.
      if (!list.some((e) => e.s === simp && e.p === entry.p)) list.push({ ...entry, s: simp });
    } else if (!list.some((e) => e.p === entry.p && e.m === entry.m)) list.push(entry);
  }
  entries++;
}
// Everyday reading first for common multi-reading characters (the dictionary's own order
// is arbitrary: 看 lists kān before kàn). Words resolve most cases; this orders single characters.
const primary: Record<string, string> = {
  了: "le", 的: "de", 地: "de", 得: "de", 着: "zhe", 看: "kàn", 行: "xíng", 长: "cháng", 还: "hái", 都: "dōu",
  重: "zhòng", 好: "hǎo", 觉: "jué", 乐: "lè", 只: "zhǐ", 为: "wèi", 数: "shù", 调: "diào", 便: "biàn", 和: "hé",
  要: "yào", 会: "huì", 种: "zhǒng", 少: "shǎo", 发: "fā", 当: "dāng", 相: "xiāng", 大: "dà", 么: "me", 哪: "nǎ",
  那: "nà", 差: "chà", 教: "jiāo", 背: "bèi", 空: "kōng", 正: "zhèng", 难: "nán", 中: "zhōng", 一: "yī", 不: "bù",
  传: "chuán", 场: "chǎng", 解: "jiě", 量: "liàng", 应: "yīng", 处: "chù", 结: "jié", 系: "xì", 角: "jiǎo", 给: "gěi",
  没: "méi", 干: "gàn", 分: "fēn", 假: "jiǎ", 转: "zhuǎn", 弹: "tán", 难过: "nánguò",
};
const rank = (key: string, e: DictEntry) =>
  (primary[key] && e.p.toLowerCase() === primary[key] ? 0 : 1) * 4 + Number(/^[A-Z]/.test(e.p)) * 2;
for (const shard of shards)
  for (const [key, list] of Object.entries(shard)) list.sort((a, b) => rank(key, a) - rank(key, b) || (a.h ?? 9) - (b.h ?? 9));

rmSync("public/dict", { recursive: true, force: true });
mkdirSync("public/dict", { recursive: true });
let bytes = 0,
  gz = 0;
const hash = createHash("sha256");
shards.forEach((shard, i) => {
  const json = JSON.stringify(shard);
  hash.update(json);
  bytes += Buffer.byteLength(json);
  gz += gzipSync(json).length;
  writeFileSync(`public/dict/${String(i).padStart(3, "0")}.json`, json);
});
const manifest = {
  source: "CC-CEDICT",
  sourceUrl: "https://www.mdbg.net/chinese/dictionary?page=cc-cedict",
  sourceDate,
  license: "CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)",
  attribution: "CC-CEDICT, MDBG and contributors. Adapted for Kiyo: tone marks, first three senses, HSK 3.0 levels.",
  shards: SHARDS,
  entries,
  version: hash.digest("hex").slice(0, 12),
  bytes,
  gzipBytes: gz,
};
writeFileSync("public/dict/manifest.json", JSON.stringify(manifest, null, 2));
console.log(`${entries} entries (${dropped} variant-only dropped) · ${SHARDS} shards · ${(bytes / 1e6).toFixed(1)} MB raw, ${(gz / 1e6).toFixed(1)} MB gzipped · source ${sourceDate}`);
