// Fail the build if the approved exports are missing or were replaced accidentally.
import { readFileSync } from "node:fs";
import { createHash } from "node:crypto";
import assets from "../src/brand-assets.json";

for (const asset of Object.values(assets)) {
  const bytes = readFileSync(`public${asset.src}`);
  if (createHash("sha256").update(bytes).digest("hex") !== asset.sha256)
    throw new Error(`Approved brand asset changed: ${asset.src}. Re-export with scripts/export-brand-icons.ts.`);
}
await import("./make-icon");
console.log("Verified approved website logo and app-icon exports.");
