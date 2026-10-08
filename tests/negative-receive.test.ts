import { readFileSync, readdirSync } from 'node:fs';
import { expect, test } from 'vitest';

test('not yet received uses méi rather than the overlapping confiscate reading', () => {
  const lines: { zh: string; py: string }[] = [];
  const walk = (value: unknown) => {
    if (Array.isArray(value)) value.forEach(walk);
    else if (value && typeof value === 'object') {
      const row = value as Record<string, unknown>;
      if (typeof row.zh === 'string' && typeof row.py === 'string' && row.zh.includes('没收到')) {
        lines.push({ zh: row.zh, py: row.py });
      }
      Object.values(row).forEach(walk);
    }
  };
  for (const name of readdirSync('content/packs').filter((name) => /^s\d-u.*\.json$/.test(name))) {
    walk(JSON.parse(readFileSync(`content/packs/${name}`, 'utf8')));
  }
  expect(lines.length).toBeGreaterThan(0);
  for (const line of lines) {
    expect(line.py, line.zh).not.toMatch(/mò\s+shōu\s+dào/);
    expect(line.py, line.zh).toMatch(/méi\s+shōu\s+dào/);
  }
});
