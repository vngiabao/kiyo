// Research audit only: explicit teaching is separate from incidental text exposure.
// npx tsx scripts/coverage-report.ts [--write]
import { createHash } from "node:crypto";
import { existsSync, readFileSync, readdirSync, writeFileSync } from "node:fs";
import { resolve } from "node:path";
import { fileURLToPath } from "node:url";
import { basePhrases, lessons } from "../src/content";
import { baseCharacters, baseReadings } from "../src/hanzi";
import type { ContentPack } from "../src/packs";

export interface Inventory {
  standard: string;
  source: string;
  levels: Record<
    string,
    { words: string[][]; characters: string[][]; grammar: string[][] }
  >;
}
export interface GrammarEvidence {
  code: string;
  cards: string[];
  status: "introduced" | "partial";
  note: string;
}
export const alternatives = (word: string) => {
  const annotated: Record<string, string[]> = {
    "第（第二）": ["第"],
    "有（一）些": ["有些", "有一些"],
    "们（朋友们）": ["们"],
    "子（桌子）": ["子"],
  };
  return (
    annotated[word] ??
    word
      .split(/[∣|｜]/u)
      .map((s) => s.trim())
      .filter(Boolean)
  );
};

export function auditCoverage(
  inventory: Inventory,
  input: {
    baseWords: string[];
    characters: string[];
    packs: ContentPack[];
    text: string;
    grammar: GrammarEvidence[];
  },
  lookup: Record<string, { hsk3?: number }>,
) {
  const taught = new Set([
    ...input.baseWords,
    ...input.packs.flatMap((p) => p.vocabulary.map((w) => w.hanzi)),
  ]);
  const characters = new Set([
    ...input.characters,
    ...input.packs.flatMap((p) => (p.characters ?? []).map((c) => c.hanzi)),
  ]);
  const cards = new Set(
    input.packs.flatMap((p) => (p.grammar ?? []).map((g) => g.id)),
  );
  const seenEvidence = new Set<string>();
  for (const e of input.grammar) {
    if (seenEvidence.has(e.code))
      throw new Error(`Duplicate grammar crosswalk: ${e.code}`);
    seenEvidence.add(e.code);
    if (!e.cards.length || e.cards.some((id) => !cards.has(id)))
      throw new Error(`Unknown grammar card: ${e.code}`);
  }
  const earlierCharacters = new Set<string>();
  const earlierWords = new Set<string>();
  const levels = [1, 2, 3].map((level) => {
    const data = inventory.levels[String(level)];
    const rows = data.words.map((r) => ({
      sourceNo: r[0],
      entry: r[2],
      forms: alternatives(r[2]),
      pinyin: r[3],
      partOfSpeech: r[4],
    }));
    const sameLevelDuplicates = new Set(
      rows
        .flatMap((r) => r.forms)
        .filter((w, _, all) => all.filter((s) => s === w).length > 1),
    );
    const normalizePinyin = (s: string) =>
      s.toLowerCase().replace(/[\s'’]/gu, "");
    const pos: Record<string, string> = {
      noun: "名",
      verb: "动",
      adjective: "形",
      adverb: "副",
      pronoun: "代",
      "measure word": "量",
      particle: "助",
      preposition: "介",
      conjunction: "连",
      suffix: "后缀",
    };
    const hasSenseEvidence = (w: string, r: (typeof rows)[number]) =>
      input.packs.some((p) =>
        p.vocabulary.some(
          (v) =>
            v.hanzi === w &&
            normalizePinyin(v.pinyin) === normalizePinyin(r.pinyin) &&
            !!pos[v.pos ?? ""] &&
            r.partOfSpeech.includes(pos[v.pos ?? ""]),
        ),
      );
    const sourceAliases: Record<string, string[]> = {
      "有（一）点儿": ["有点儿", "有一点儿"], "家（科学家）": ["家"],
      "老（老王）": ["老"], "小（小王）": ["小"], "头（里头）": ["头"],
      "面1": ["面"], "面2": ["面"],
    };
    const sourceReadings = (r: (typeof rows)[number], word: string) => {
      if (r.entry === "有（一）点儿") return word === "有点儿" ? ["yǒudiǎnr"] : ["yǒuyìdiǎnr"];
      const readings = r.pinyin.split(/[∣|｜]/u);
      return readings.length === r.forms.length && readings.length > 1
        ? [readings[r.forms.indexOf(word)]] : [r.pinyin.split(/[（(]/u)[0].trim()];
    };
    const hasSourceRowEvidence = (r: (typeof rows)[number]) =>
      input.packs.some((p) => p.vocabulary.some((v) =>
        [...r.forms, ...(sourceAliases[r.entry] ?? [])].includes(v.hanzi) &&
        v.usageNote?.includes(`[GF2021:L${level}:${r.sourceNo}]`) &&
        sourceReadings(r, v.hanzi).some((py) => normalizePinyin(v.pinyin) === normalizePinyin(py)) &&
        !!pos[v.pos ?? ""] && (!r.partOfSpeech || r.partOfSpeech.includes(pos[v.pos ?? ""])) &&
        (!r.partOfSpeech.includes("后缀") || (v.pos === "suffix" && !!v.usageNote.includes(r.entry))),
      ));
    // Repeated forms may introduce another reading or sense: exact spelling alone is insufficient.
    const suffixEvidence = (w: string, r: (typeof rows)[number]) =>
      input.packs.some((p) => p.vocabulary.some((v) =>
        v.hanzi === w && v.pos === "suffix" &&
        normalizePinyin(v.pinyin) === normalizePinyin(r.pinyin.split(/[（(]/u)[0]) &&
        !!v.usageNote?.includes(r.entry),
      ));
    const isIntroduced = (r: (typeof rows)[number]) =>
      r.forms.some(
        (w) =>
          taught.has(w) &&
          (!r.partOfSpeech.includes("后缀") || suffixEvidence(w, r)) &&
          (!sameLevelDuplicates.has(w) || hasSenseEvidence(w, r)) &&
          (!earlierWords.has(w) ||
            input.packs.some((p) =>
              p.vocabulary.some((v) => v.hanzi === w && v.hskLevel === level),
            )),
      ) || hasSourceRowEvidence(r);
    const introduced = rows.filter(isIntroduced);
    const remaining = rows.filter((r) => !isIntroduced(r));
    const repeatedFormNeedsReview = remaining.filter((r) =>
      r.forms.some(
        (w) =>
          taught.has(w) && (earlierWords.has(w) || sameLevelDuplicates.has(w)),
      ),
    );
    const allChars = [...new Set(data.characters.map((r) => r[2]))];
    const supplementaryReadings = data.characters.filter((r) =>
      earlierCharacters.has(r[2]),
    );
    const charList = allChars.filter((c) => !earlierCharacters.has(c));
    allChars.forEach((c) => earlierCharacters.add(c));
    rows.flatMap((r) => r.forms).forEach((w) => earlierWords.add(w));
    const grammar = data.grammar
      .filter((r) => !r[5].startsWith("※"))
      .map((r, i) => {
        // 【一01】 etc. are the printed Appendix A codes. Query No. is retained separately.
        const code = `${["", "一", "二", "三"][level]}${String(i + 1).padStart(2, "0")}`;
        const evidence = input.grammar.find((e) => e.code === code);
        return {
          code,
          sourceNo: r[0],
          category: r.slice(2, 5),
          content: r[5],
          status: evidence?.status ?? "unmapped",
          cards: evidence?.cards ?? [],
          note:
            evidence?.note ??
            "No explicit grammar-card crosswalk; occurrence does not prove instruction.",
        };
      });
    const differences = rows.flatMap((r) =>
      r.forms
        .filter((w) => lookup[w]?.hsk3 !== level)
        .map((word) => ({
          word,
          officialLevel: level,
          localLevel: lookup[word]?.hsk3 ?? null,
          sourceNo: r.sourceNo,
        })),
    );
    return {
      level,
      words: {
        officialEntries: rows.length,
        localLookupForms: Object.values(lookup).filter((w) => w.hsk3 === level)
          .length,
        introduced: introduced.length,
        remaining: remaining.length,
        introducedEntries: introduced,
        remainingEntries: remaining,
        repeatedFormNeedsReview,
        incidentalOnlyCandidates: remaining.filter((r) =>
          r.forms.some((w) => input.text.includes(w)),
        ),
        differences,
      },
      characters: {
        officialUnique: charList.length,
        sourceRows: data.characters.length,
        supplementaryReadings,
        introduced: charList.filter((c) => characters.has(c)).length,
        remaining: charList.filter((c) => !characters.has(c)),
      },
      grammar: {
        officialItems: grammar.length,
        crossReferences: data.grammar.filter((r) => r[5].startsWith("※")),
        introduced: grammar.filter((g) => g.status === "introduced").length,
        partial: grammar.filter((g) => g.status === "partial").length,
        unmapped: grammar.filter((g) => g.status === "unmapped").length,
        items: grammar,
      },
    };
  });
  const validCodes = new Set(
    levels.flatMap((l) => l.grammar.items.map((g) => g.code)),
  );
  if (input.grammar.some((e) => !validCodes.has(e.code)))
    throw new Error("Unknown official grammar code");
  return {
    standard: inventory.standard,
    source: inventory.source,
    method:
      "Exact base phrases and standalone character entries with meanings + declared pack vocabulary; explicit character entries; manually reviewed grammar-card crosswalk. Repeated higher-level senses require level-specific pack evidence. Incidental example words and substring matches are candidates only, not segmented coverage or learner mastery.",
    explicitWords: taught.size,
    explicitCharacters: characters.size,
    grammarCards: cards.size,
    levels,
  };
}

export function runCoverage() {
  const reference = "prompts/research/gf2021-inventory.json";
  if (!existsSync(reference))
    throw new Error(`Missing researched inventory: ${reference}`);
  const inventory: Inventory = JSON.parse(readFileSync(reference, "utf8"));
  const lookup = JSON.parse(
    readFileSync("content/hsk/levels.json", "utf8"),
  ).words;
  const files = readdirSync("content/packs")
    .filter(
      (f) =>
        f.endsWith(".json") && !f.startsWith("_") && !f.endsWith(".hsk.json"),
    )
    .sort();
  const packs: ContentPack[] = files
    .map((f) => JSON.parse(readFileSync(`content/packs/${f}`, "utf8")))
    .sort((a, b) => a.unit.stage - b.unit.stage || a.unit.order - b.unit.order);
  const grammar: GrammarEvidence[] = JSON.parse(
    readFileSync("prompts/research/grammar-crosswalk.json", "utf8"),
  ).evidence;
  const result = auditCoverage(
    inventory,
    {
      baseWords: [
        ...basePhrases.filter((p) => p.topic !== "sounds").map((p) => p.hanzi),
        ...baseCharacters.map((c) => c.hanzi),
      ],
      characters: baseCharacters.map((c) => c.hanzi),
      packs,
      grammar,
      text: JSON.stringify([...basePhrases, ...baseReadings, ...packs]),
    },
    lookup,
  );
  const report = {
    ...result,
    generatedAt: new Date().toISOString(),
    baseLessons: lessons.length,
    packUnits: packs.length,
    inputs: [
      reference,
      "content/hsk/levels.json",
      "prompts/research/grammar-crosswalk.json",
      "src/content.ts",
      "src/hanzi.ts",
      ...files.map((f) => `content/packs/${f}`),
    ].map((path) => ({
      path,
      sha256: createHash("sha256").update(readFileSync(path)).digest("hex"),
    })),
    currentUnits: packs.map((p) => ({
      id: p.unit.id,
      title: p.unit.title,
      vocabulary: p.vocabulary.length,
      grammar: (p.grammar ?? []).map((g) => ({ id: g.id, pattern: g.pattern })),
    })),
  };
  console.log(
    `${report.baseLessons} base phrase lessons; ${report.packUnits} packs; ${report.explicitCharacters} explicit characters; ${report.grammarCards} grammar cards.`,
  );
  for (const l of report.levels)
    console.log(
      `GF2021 L${l.level}: words ${l.words.introduced}/${l.words.officialEntries} introduced, ${l.words.remaining} left; characters ${l.characters.introduced}/${l.characters.officialUnique}; grammar ${l.grammar.introduced} introduced, ${l.grammar.partial} partial, ${l.grammar.unmapped} unmapped of ${l.grammar.officialItems}; ${l.words.differences.length} local form/level differences.`,
    );
  if (process.argv.includes("--write"))
    writeFileSync(
      "prompts/research/coverage-report.json",
      JSON.stringify(report, null, 2) + "\n",
    );
  return report;
}

if (
  process.argv[1] &&
  resolve(process.argv[1]) === fileURLToPath(import.meta.url)
)
  runCoverage();
