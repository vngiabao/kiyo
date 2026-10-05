import { gunzipSync } from "node:zlib";
import { writeFileSync, mkdirSync } from "node:fs";
import { phrases } from "../src/content";
const source =
  "https://www.mdbg.net/chinese/export/cedict/cedict_1_0_ts_utf-8_mdbg.txt.gz";
const response = await fetch(source);
if (!response.ok)
  throw new Error(`Dictionary download failed: ${response.status}`);
const lines = gunzipSync(Buffer.from(await response.arrayBuffer()))
  .toString("utf8")
  .split("\n");
const entries = new Map<
  string,
  { traditional: string; pinyin: string; definitions: string[] }[]
>();
for (const line of lines) {
  const m = line.trim().match(/^(\S+) (\S+) \[([^\]]+)\] \/(.+)\/$/);
  if (m)
    entries.set(m[2], [
      ...(entries.get(m[2]) ?? []),
      { traditional: m[1], pinyin: m[3], definitions: m[4].split("/") },
    ]);
}
const report = phrases.map((p) => ({
  id: p.id,
  hanzi: p.hanzi,
  authoredPinyin: p.pinyin,
  exactDictionaryEntries: entries.get(p.hanzi) ?? [],
  status: entries.has(p.hanzi)
    ? "dictionary-entry-found; human comparison required"
    : "composed phrase; constituent review required",
}));
mkdirSync("content", { recursive: true });
writeFileSync(
  "content/reference-check.json",
  JSON.stringify(
    {
      source,
      license: "CC BY-SA 4.0",
      attribution: "CC-CEDICT contributors, via MDBG",
      checkedOn: "2026-10-04",
      note: "Dictionary presence is not a naturalness or pedagogical approval. Extracted dictionary data retains CC BY-SA 4.0.",
      entries: report,
    },
    null,
    2,
  ),
);
console.log(
  `${report.filter((r) => r.exactDictionaryEntries.length).length}/${phrases.length} phrases have exact CC-CEDICT entries. Saved evidence; no automatic publication approval.`,
);
