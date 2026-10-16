// Ask the production Worker for every clip the app (or an older cached install) can request.
// Usage: npx wrangler dev --local --port 8788 (after npm run build), then
//        npx tsx scripts/audit-audio-routes.ts [http://127.0.0.1:8788]
// Every clip: HEAD → 200, audio/mpeg, exact byte length. A random sample: full GET + sha256.
import { createHash } from "node:crypto";
import { readFileSync, statSync } from "node:fs";
import http from "node:http";

// Reuse connections: tens of thousands of one-off requests exhaust local ports on Windows.
const agent = new http.Agent({ keepAlive: true, maxSockets: 24 });
// A refused local connection is the machine, not the route: retry before calling it a failure.
async function request(url: string, method: "HEAD" | "GET", tries = 4): Promise<{ status: number; headers: http.IncomingHttpHeaders; body: Buffer }> {
  try {
    return await once(url, method);
  } catch (e) {
    if (tries <= 1 || !/EADDRINUSE|ECONNRESET|ECONNREFUSED/.test(String((e as Error).message))) throw e;
    await new Promise((r) => setTimeout(r, 250));
    return request(url, method, tries - 1);
  }
}
function once(url: string, method: "HEAD" | "GET") {
  return new Promise<{ status: number; headers: http.IncomingHttpHeaders; body: Buffer }>((resolve, reject) => {
    const req = http.request(url, { method, agent }, (res) => {
      const chunks: Buffer[] = [];
      res.on("data", (c: Buffer) => chunks.push(c));
      res.on("end", () => resolve({ status: res.statusCode ?? 0, headers: res.headers, body: Buffer.concat(chunks) }));
      res.on("error", reject);
    });
    req.on("error", reject);
    req.end();
  });
}

const base = process.argv[2] ?? "http://127.0.0.1:8788";
const read = (p: string) => JSON.parse(readFileSync(p, "utf8"));
const current = new Set<string>(
  Object.values(read("src/audio-assets.json") as Record<string, Record<string, string>>).flatMap((v) => Object.values(v)),
);
const retained = (read("content/voices/released-audio-compatibility.json").entries as { file: string; sha256: string }[])
  .map((e) => ({ url: "/" + e.file.replace(/^public\//, ""), sha256: e.sha256 }));
const proof = new Map<string, string>(
  (read("content/voices/sayo-library-provenance.json").clips as { file: string; sha256: string }[]).map((c) => [
    "/" + c.file.replace(/^public\//, ""),
    c.sha256,
  ]),
);
for (const r of retained) proof.set(r.url, r.sha256);
const urls = [...new Set([...current, ...retained.map((r) => r.url)])];

const failures: string[] = [];
let done = 0;
async function head(url: string) {
  const res = await request(base + url, "HEAD");
  const size = statSync("public" + url).size;
  const type = String(res.headers["content-type"] ?? "");
  const length = Number(res.headers["content-length"]);
  if (res.status !== 200 || !type.startsWith("audio/mpeg") || length !== size)
    failures.push(`${url}: ${res.status} ${type} ${length} (expected ${size})`);
  if (++done % 5000 === 0) console.log(`${done}/${urls.length}`);
}
async function full(url: string) {
  const res = await request(base + url, "GET");
  const bytes = res.body;
  const sha = createHash("sha256").update(bytes).digest("hex");
  if (res.status !== 200 || sha !== proof.get(url)) failures.push(`${url}: body hash mismatch (${res.status})`);
}
async function pool<T>(items: T[], size: number, fn: (x: T) => Promise<void>) {
  let i = 0;
  await Promise.all(Array.from({ length: size }, async () => {
    while (i < items.length) {
      const x = items[i++];
      try { await fn(x); } catch (e) { failures.push(`${String(x)}: ${(e as Error).message}`); }
    }
  }));
}

await pool(urls, 24, head);
const sample = [...urls].sort(() => Math.random() - 0.5).slice(0, 400);
await pool(sample, 12, full);
// A missing clip must be a clean 404, never the app's HTML shell.
const missing = await request(base + "/audio-v2/sayo-not-a-real-clip.mp3", "GET");
if (missing.status !== 404) failures.push(`missing clip returned ${missing.status}, expected 404`);

console.log(`${urls.length} clip routes checked (${current.size} current, ${retained.length} retained for cached installs); ${sample.length} bodies hash-verified.`);
if (failures.length) {
  console.error(failures.slice(0, 20).join("\n"));
  console.error(`${failures.length} failures`);
  process.exit(1);
}
console.log("All audio routes OK.");
agent.destroy();
