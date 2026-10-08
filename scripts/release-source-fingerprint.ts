import { execFileSync } from "node:child_process";
import { createHash } from "node:crypto";
import { existsSync, readFileSync } from "node:fs";

// Clip bytes have their own exact-hash build gate. This stamp guards source,
// curriculum and visual assets against concurrent edits after the test receipt.
const paths = new Set(
  execFileSync(
    "git",
    ["ls-files", "-z", "--cached", "--others", "--exclude-standard"],
    { encoding: "utf8", maxBuffer: 16 * 1024 * 1024 },
  )
    .split("\0")
    .filter(Boolean),
);
const included = [...paths]
  .filter(
    (p) =>
      (/^(src|scripts|content|public|tests|e2e)\//.test(p) &&
        /\.(tsx?|css|json|html|py|ps1|svg|png|webp|ico)$/.test(p)) ||
      (!p.includes("/") && /\.(tsx?|json|jsonc|html)$/.test(p)),
  )
  .sort();
const hash = createHash("sha256");
for (const path of included) {
  hash
    .update(path)
    .update("\0")
    .update(existsSync(path) ? readFileSync(path) : "deleted")
    .update("\0");
}
process.stdout.write(hash.digest("hex") + "\n");
