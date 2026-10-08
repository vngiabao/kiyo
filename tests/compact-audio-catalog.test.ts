import { expect, it } from "vitest";
import assets from "../src/audio-assets.json";
import { compactAudioCatalog } from "../scripts/compact-audio-catalog";

const decode = (input: Record<string, Record<string, string>>) => {
  const source = compactAudioCatalog(input);
  return new Function(source.replace("export default", "return"))();
};
it("preserves every installed Mandarin key, mood and exact audio URL", () => {
  expect(decode(assets)).toEqual(assets);
  expect(Buffer.byteLength(compactAudioCatalog(assets))).toBeLessThan(Buffer.byteLength(JSON.stringify(assets)) * .8);
});
it("handles irregular paths, punctuation, escaping, empty catalogs and one-off moods", () => {
  const unusual = { '你说“好”？\\': { clear: '/audio/one.mp3', soft: '/else/two.mp3' }, second: { clear: '/different/three.mp3' } };
  expect(decode(unusual)).toEqual(unusual);
  expect(decode({})).toEqual({});
});
