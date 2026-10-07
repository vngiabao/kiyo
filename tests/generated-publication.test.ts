import { mkdtemp, readFile, readdir, rm, stat, writeFile } from "node:fs/promises";
import { join } from "node:path";
import { tmpdir } from "node:os";
import { expect, it } from "vitest";
import { publishGenerated } from "../scripts/publish-generated";

it("publishes complete catalogs and leaves identical files untouched", async () => {
  const directory = await mkdtemp(join(tmpdir(), "kiyo-publication-"));
  try {
    const path = join(directory, "catalog.json");
    await publishGenerated(path, '[{"id":"first"}]');
    const initial = await stat(path);
    await publishGenerated(path, '[{"id":"first"}]');
    expect((await stat(path)).mtimeMs).toBe(initial.mtimeMs);
    await publishGenerated(path, '[{"id":"replacement"}]');
    expect(JSON.parse(await readFile(path, "utf8"))).toEqual([{ id: "replacement" }]);
    expect(await readdir(directory)).toEqual(["catalog.json"]);
  } finally {
    await rm(directory, { recursive: true, force: true });
  }
});

it("fails on an invalid destination without silently accepting old data", async () => {
  const directory = await mkdtemp(join(tmpdir(), "kiyo-publication-"));
  try {
    await writeFile(join(directory, "existing.json"), "[]");
    await expect(publishGenerated(join(directory, "absent", "catalog.json"), "[]")).rejects.toThrow();
    expect(await readdir(directory)).toEqual(["existing.json"]);
  } finally {
    await rm(directory, { recursive: true, force: true });
  }
});
