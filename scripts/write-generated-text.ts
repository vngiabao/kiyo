import { randomUUID } from "node:crypto";
import { renameSync, writeFileSync } from "node:fs";
import { resolve } from "node:path";

export function writeGeneratedText(path: string, content: string) {
  const target = resolve(path);
  const temporary = `${target}.${process.pid}.${randomUUID()}.tmp`;
  // Finish a new sibling file before replacing the old report. Directly opening
  // an existing file for truncation can fail in this Windows synced workspace.
  writeFileSync(temporary, content, { encoding: "utf8", flag: "wx", flush: true });
  // A failed replacement remains an error; retain the temporary for inspection.
  renameSync(temporary, target);
}
