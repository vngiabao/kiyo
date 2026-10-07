import { readFile, rename, unlink, writeFile } from "node:fs/promises";
import { setTimeout } from "node:timers/promises";
import { randomUUID } from "node:crypto";

// OneDrive and Windows scanners can briefly lock generated files. Readers must
// keep seeing the previous complete catalog until the replacement is ready.
export async function publishGenerated(path: string, text: string) {
  try {
    if (await readFile(path, "utf8") === text) return;
  } catch (error) {
    if ((error as NodeJS.ErrnoException).code !== "ENOENT") throw error;
  }
  const temporary = `${path}.${randomUUID()}.tmp`;
  await writeFile(temporary, text, { encoding: "utf8", flag: "wx" });
  try {
    for (let attempt = 0; ; attempt++) {
      try {
        await rename(temporary, path);
        return;
      } catch (error) {
        const code = (error as NodeJS.ErrnoException).code;
        if (attempt >= 6 || !["EPERM", "EBUSY", "EACCES", "UNKNOWN"].includes(code ?? "")) throw error;
        await setTimeout(100 * 2 ** attempt);
      }
    }
  } finally {
    await unlink(temporary).catch((error: NodeJS.ErrnoException) => {
      if (error.code !== "ENOENT") throw error;
    });
  }
}
