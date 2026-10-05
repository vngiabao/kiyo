import { expect, it } from "vitest";
import { cueAt, parseCaptions, parseLrc, parseVtt } from "../src/captions";
import { parseSrt } from "../src/MediaLab";

it("still parses SRT through the Media page export", () => {
  expect(parseSrt("1\n00:00:01,500 --> 00:00:03,000\n你好")).toEqual([{ start: 1.5, end: 3, text: "你好" }]);
});
it("parses WebVTT, with or without hours, and strips styling tags", () => {
  const vtt = "WEBVTT\n\n00:01.000 --> 00:02.500 align:start\n<i>你好</i>\n\n01:00:00.000 --> 01:00:01.000\n再见";
  expect(parseVtt(vtt)).toEqual([
    { start: 1, end: 2.5, text: "你好" },
    { start: 3600, end: 3601, text: "再见" },
  ]);
});
it("parses LRC lyrics; each line lasts until the next", () => {
  const lrc = "[ti:Song]\n[00:12.30]第一句\n[00:15.00]第二句\n[00:15.00][00:40.5]副歌";
  expect(parseLrc(lrc)).toEqual([
    { start: 12.3, end: 15, text: "第一句" },
    { start: 15, end: 15, text: "第二句" },
    { start: 15, end: 40.5, text: "副歌" },
    { start: 40.5, end: 45.5, text: "副歌" },
  ].filter((c) => c.end > c.start));
});
it("picks the format from the file and finds the current line", () => {
  const cues = parseCaptions("song.lrc", "[00:01.00]一\n[00:03.00]二");
  expect(cues.map((c) => c.text)).toEqual(["一", "二"]);
  expect(cueAt(cues, 2)).toBe(0);
  expect(cueAt(cues, 3.5)).toBe(1);
  expect(cueAt(cues, 0.5)).toBe(-1);
  expect(parseCaptions("ep1.srt", "1\n00:00:01,000 --> 00:00:02,000\n好")).toHaveLength(1);
});
