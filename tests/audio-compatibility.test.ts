import { afterEach, describe, expect, it } from 'vitest';
import { mkdtempSync, mkdirSync, writeFileSync, rmSync } from 'node:fs';
import { tmpdir } from 'node:os';
import { join } from 'node:path';
import { createHash } from 'node:crypto';
import { verifyReleasedAudio } from '../scripts/audio-compatibility';

const roots: string[] = [];
afterEach(() => { for (const root of roots.splice(0)) rmSync(root, { recursive: true }); });
function fixture() {
  const root = mkdtempSync(join(tmpdir(), 'kiyo-retained-test-')); roots.push(root);
  const file = 'public/audio-v2/released.mp3';
  const bytes = Buffer.from('ID3 exact released audio');
  mkdirSync(join(root, 'public/audio-v2'), { recursive: true });
  writeFileSync(join(root, file), bytes);
  return { root, ledger: { version: 1, entries: [{ file, sha256: createHash('sha256').update(bytes).digest('hex'), originCommit: 'a'.repeat(40), retainThrough: '2027-01-06' }] } };
}
describe('previously released audio verification', () => {
  it('accepts exact committed bytes independently of current catalog coverage', () => {
    const f = fixture();
    expect(verifyReleasedAudio(f.root, f.ledger)).toBe(1);
  });
  it('rejects tampered or missing audio', () => {
    const f = fixture();
    writeFileSync(join(f.root, f.ledger.entries[0].file), 'changed');
    expect(() => verifyReleasedAudio(f.root, f.ledger)).toThrow('Changed retained audio');
    f.ledger.entries[0].file = 'public/audio-v2/missing.mp3';
    expect(() => verifyReleasedAudio(f.root, f.ledger)).toThrow();
  });
  it('rejects path escapes and duplicate receipts', () => {
    const f = fixture();
    f.ledger.entries.push({ ...f.ledger.entries[0] });
    expect(() => verifyReleasedAudio(f.root, f.ledger)).toThrow('Invalid retained audio record');
    f.ledger.entries = [{ ...f.ledger.entries[0], file: 'public/audio-v2/../escape.mp3' }];
    expect(() => verifyReleasedAudio(f.root, f.ledger)).toThrow('Invalid retained audio record');
  });
  it('rejects invalid hashes, origins, dates and ledger versions', () => {
    for (const change of [{ sha256: '0' }, { originCommit: 'HEAD' }, { retainThrough: '2027-02-30' }]) {
      const f = fixture(); Object.assign(f.ledger.entries[0], change);
      expect(() => verifyReleasedAudio(f.root, f.ledger)).toThrow('Invalid retained audio record');
    }
    const f = fixture(); f.ledger.version = 2;
    expect(() => verifyReleasedAudio(f.root, f.ledger)).toThrow('Invalid released-audio ledger');
  });
});
