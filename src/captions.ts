/**
 * Timed text for the Watch player: drama subtitles (.srt, .vtt) and song lyrics (.lrc).
 * Every format becomes the same list of cues, sorted by start time.
 */
export interface Cue {
  start: number;
  end: number;
  text: string;
}

const clean = (s: string) => s.replace(/<[^>]+>/g, "").replace(/\{[^}]*\}/g, "").trim();

/** 00:01:02,500 · 00:01:02.500 · 01:02.500 (WebVTT allows no hours) */
function clock(s: string): number {
  const m = s.trim().match(/^(?:(\d+):)?(\d{1,2}):(\d{2})[,.](\d{1,3})/);
  if (!m) return NaN;
  return (m[1] ? +m[1] * 3600 : 0) + +m[2] * 60 + +m[3] + +m[4].padEnd(3, "0") / 1000;
}

/** SRT and WebVTT share the "start --> end" block shape. */
function parseBlocks(input: string): Cue[] {
  return input
    .replace(/^﻿/, "")
    .trim()
    .split(/\r?\n\s*\r?\n/)
    .flatMap((block) => {
      const lines = block.split(/\r?\n/);
      const i = lines.findIndex((l) => l.includes("-->"));
      if (i < 0) return [];
      const [a, b] = lines[i].split("-->");
      const start = clock(a),
        end = clock(b.trim().split(/\s+/)[0] ?? "");
      const text = clean(lines.slice(i + 1).join(" "));
      return Number.isFinite(start) && end > start && text ? [{ start, end, text }] : [];
    });
}
export const parseSrt = parseBlocks;
export const parseVtt = parseBlocks;

/** LRC lyrics: [mm:ss.xx] line. A line ends when the next begins (or 5 s for the last). */
export function parseLrc(input: string): Cue[] {
  const stamped: { start: number; text: string }[] = [];
  for (const line of input.replace(/^﻿/, "").split(/\r?\n/)) {
    const stamps = [...line.matchAll(/\[(\d{1,3}):(\d{2})(?:[.:](\d{1,3}))?\]/g)];
    if (!stamps.length) continue;
    const text = clean(line.replace(/\[[^\]]*\]/g, ""));
    for (const s of stamps) stamped.push({ start: +s[1] * 60 + +s[2] + (s[3] ? +s[3].padEnd(3, "0") / 1000 : 0), text });
  }
  stamped.sort((a, b) => a.start - b.start);
  return stamped
    .map((s, i) => ({ start: s.start, end: stamped[i + 1]?.start ?? s.start + 5, text: s.text }))
    .filter((c) => c.text && c.end > c.start);
}

/** Pick the parser from the file name, falling back to the content. */
export function parseCaptions(fileName: string, text: string): Cue[] {
  const lower = fileName.toLowerCase();
  const cues = lower.endsWith(".lrc") || /^\s*\[\d{1,3}:\d{2}/m.test(text) && !text.includes("-->") ? parseLrc(text) : parseBlocks(text);
  return cues.sort((a, b) => a.start - b.start);
}

/** The cue playing at time t, or -1. */
export const cueAt = (cues: Cue[], t: number) => cues.findIndex((c) => t >= c.start && t < c.end);
