import { mkdtempSync, mkdirSync, readFileSync, readdirSync, writeFileSync } from "node:fs";
import { tmpdir } from "node:os";
import { join } from "node:path";
import { describe, expect, it } from "vitest";
import { writeGeneratedText } from "../scripts/write-generated-text";

describe("generated report replacement", () => {
  it("replaces a longer previous report with exact Unicode bytes", () => {
    const root = mkdtempSync(join(tmpdir(), "kiyo-report-replacement-"));
    const target = join(root, "report.json");
    writeFileSync(target, "previous report with a long obsolete tail");
    const content = '{"line":"你好，开始吧。"}\n';
    writeGeneratedText(target, content);
    expect(readFileSync(target)).toEqual(Buffer.from(content, "utf8"));
    expect(readdirSync(root)).toEqual(["report.json"]);
  });

  it("keeps existing contents and reports an unsuccessful replacement", () => {
    const root = mkdtempSync(join(tmpdir(), "kiyo-report-failure-"));
    const target = join(root, "report.json");
    mkdirSync(target);
    writeFileSync(join(target, "keep.txt"), "previous contents");
    expect(() => writeGeneratedText(target, "new report\n")).toThrow();
    expect(readFileSync(join(target, "keep.txt"), "utf8")).toBe("previous contents");
    const retained = readdirSync(root).find((name) => name.endsWith(".tmp"));
    expect(retained).toBeDefined();
    expect(readFileSync(join(root, retained!), "utf8")).toBe("new report\n");
  });
});
