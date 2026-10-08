import { readFileSync } from "node:fs";
import { expect, it } from "vitest";
import { compactCourseData, courseDataPages } from "../scripts/compact-course-data";

const decode = (source: string) => new Function(source.replace("export default decode(data);", "return decode(data);"))();
it("preserves every authored course field while reducing installed data", () => {
  const packs = JSON.parse(readFileSync("src/generated/packs.json", "utf8"));
  const source = compactCourseData(packs);
  expect(decode(source)).toEqual(packs);
  expect(Buffer.byteLength(source)).toBeLessThan(Buffer.byteLength(JSON.stringify(packs)) * 0.85);
});
it("splits growing courses into bounded chunks without losing or reordering units", () => {
  const packs = JSON.parse(readFileSync("src/generated/packs.json", "utf8"));
  const pages = courseDataPages(packs);
  expect(pages.length).toBeGreaterThan(1);
  expect(pages.flatMap((p) => decode(compactCourseData(p)))).toEqual(packs);
  for (const page of pages) expect(Buffer.byteLength(compactCourseData(page))).toBeLessThan(1_500_000);
  expect(courseDataPages([])).toEqual([[]]);
});
it("keeps numbers, nulls, arrays, escapes and different object shapes distinct", () => {
  const input = [0, 1, 2, -1, null, true, false, "A quote: \"; not executable", [], {},
    { a: "long repeated string", b: [2, 0] }, { b: "long repeated string", a: false },
    { "a\u0001b": "x" }, { a: "x", b: "y" }];
  expect(decode(compactCourseData(input))).toEqual(input);
});
