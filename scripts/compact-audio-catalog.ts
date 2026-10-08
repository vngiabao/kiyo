/** Build-only encoding: the exported catalog and every recording URL stay exact. */
export function compactAudioCatalog(input: Record<string, Record<string, string>>) {
  const moods = [...new Set(Object.values(input).flatMap((voices) => Object.keys(voices)))];
  const prefixFor = (url: string) => url.match(/^\/audio-v2\/sayo-b-half-[a-z]+-/)?.[0] ?? url.slice(0, url.lastIndexOf("/") + 1);
  const prefixes = [...new Set(Object.values(input).flatMap((voices) => Object.values(voices).map(prefixFor)))];
  const rows = Object.entries(input).map(([text, voices]) => [text,
    Object.entries(voices).map(([mood, url]) => {
      const index = moods.indexOf(mood);
      const prefix = prefixes.indexOf(prefixFor(url));
      return [index, prefix, url.slice(prefixes[prefix].length)];
    }),
  ]);
  // JSON escaping keeps lesson text as data, never executable source.
  return `const moods=${JSON.stringify(moods)},prefixes=${JSON.stringify(prefixes)},rows=${JSON.stringify(rows)};\nexport default Object.fromEntries(rows.map(([text,voices])=>[text,Object.fromEntries(voices.map(([mood,prefix,suffix])=>[moods[mood],prefixes[prefix]+suffix]))]));`;
}
