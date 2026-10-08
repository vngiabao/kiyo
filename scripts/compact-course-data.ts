/** Lossless build encoding; authored packs and all runtime fields stay intact. */
export function compactCourseData(input: unknown) {
  const counts = new Map<string, number>();
  const visit = (value: unknown) => {
    if (typeof value === "string") counts.set(value, (counts.get(value) ?? 0) + 1);
    else if (Array.isArray(value)) value.forEach(visit);
    else if (value && typeof value === "object") Object.values(value).forEach(visit);
  };
  visit(input);
  const strings = [...counts].filter(([s, n]) => s.length >= 14 && n >= 2).map(([s]) => s);
  const stringIndex = new Map(strings.map((s, i) => [s, i]));
  const shapes: string[][] = [], shapeIndex = new Map<string, number>();
  const encode = (value: unknown): unknown => {
    if (typeof value === "string") {
      const index = stringIndex.get(value);
      return index === undefined ? value : [2, index];
    }
    if (Array.isArray(value)) return [1, ...value.map(encode)];
    if (value && typeof value === "object") {
      const keys = Object.keys(value), signature = JSON.stringify(keys);
      let index = shapeIndex.get(signature);
      if (index === undefined) { index = shapes.length; shapes.push(keys); shapeIndex.set(signature, index); }
      return [0, index, ...Object.values(value).map(encode)];
    }
    return value;
  };
  const data = encode(input);
  // All strings are JSON escaped. Markers only appear in encoded arrays.
  return `const shapes=${JSON.stringify(shapes)},strings=${JSON.stringify(strings)},data=${JSON.stringify(data)};\nfunction decode(v){if(!Array.isArray(v))return v;if(v[0]===2)return strings[v[1]];if(v[0]===1)return v.slice(1).map(decode);return Object.fromEntries(shapes[v[1]].map((k,i)=>[k,decode(v[i+2])]));}\nexport default decode(data);`;
}

/** Keep each installed course chunk small as later levels are added. */
export function courseDataPages(packs: unknown[], maxBytes = 1_500_000) {
  const pages: unknown[][] = [];
  let page: unknown[] = [], bytes = 2;
  for (const pack of packs) {
    const size = Buffer.byteLength(JSON.stringify(pack)) + 1;
    if (page.length && bytes + size > maxBytes) { pages.push(page); page = []; bytes = 2; }
    page.push(pack); bytes += size;
  }
  if (page.length || !pages.length) pages.push(page);
  return pages;
}
