import { readFileSync } from "node:fs";
import { resolve } from "node:path";
import { createHash } from "node:crypto";

export function verifyReleasedAudio(root: string, ledger: { version: number; entries: { file: string; sha256: string; originCommit: string; retainThrough: string }[] }) {
  if (ledger.version !== 1 || !Array.isArray(ledger.entries)) throw new Error("Invalid released-audio ledger");
  const seen = new Set<string>();
  for (const entry of ledger.entries) {
    const expiry = Date.parse(entry.retainThrough);
    if (!/^public\/audio-v2\/[A-Za-z0-9_-]+\.mp3$/.test(entry.file) || !/^[a-f0-9]{64}$/.test(entry.sha256) || !/^[a-f0-9]{40}$/.test(entry.originCommit) || !/^\d{4}-\d{2}-\d{2}$/.test(entry.retainThrough) || !Number.isFinite(expiry) || new Date(expiry).toISOString().slice(0, 10) !== entry.retainThrough || seen.has(entry.file)) throw new Error("Invalid retained audio record");
    seen.add(entry.file);
    const actual = createHash("sha256").update(readFileSync(resolve(root, entry.file))).digest("hex");
    if (actual !== entry.sha256) throw new Error(`Changed retained audio: ${entry.file}`);
  }
  return seen.size;
}
