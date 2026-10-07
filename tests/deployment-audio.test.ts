import { afterEach, describe, expect, it } from 'vitest';
import { mkdtempSync, mkdirSync, readFileSync, writeFileSync, rmSync } from 'node:fs';
import { tmpdir } from 'node:os';
import { join } from 'node:path';
import { createHash } from 'node:crypto';
import { packAudio } from '../scripts/pack-deployment-audio';
import { serveAudio, byteRange } from '../workers/audio';
import { indexShard, type AudioIndex } from '../workers/audio-index';

const roots: string[] = [];
afterEach(() => { for (const root of roots.splice(0)) rmSync(root, { recursive: true }); });
const sha = (bytes: Uint8Array) => createHash('sha256').update(bytes).digest('hex');

function fixture(ignoreRange = false) {
  const root = mkdtempSync(join(tmpdir(), 'kiyo-audio-test-')); roots.push(root);
  const source = join(root, 'dist'), stage = join(root, 'stage');
  mkdirSync(join(source, 'audio-v2'), { recursive: true });
  writeFileSync(join(source, 'index.html'), 'application shell');
  const clips = { 'first.mp3': Buffer.from('ID3first audio'), 'second.mp3': Buffer.from('ID3second audio'), 'third.mp3': Buffer.from('ID3third audio') };
  for (const [name, bytes] of Object.entries(clips)) writeFileSync(join(source, 'audio-v2', name), bytes);
  const report = packAudio(source, stage, 30);
  const assets = { async fetch(request: Request) {
    const path = new URL(request.url).pathname;
    try {
      const bytes = readFileSync(join(stage, path));
      const headers = { 'Content-Type': path.endsWith('.json') ? 'application/json' : 'application/octet-stream' };
      const range = byteRange(request.headers.get('range'), bytes.length);
      if (range && !ignoreRange) return new Response(bytes.subarray(range.start, range.end + 1), { status: 206, headers: { ...headers, 'Content-Range': `bytes ${range.start}-${range.end}/${bytes.length}` } });
      return new Response(bytes, { headers });
    } catch { return new Response('application shell', { headers: { 'Content-Type': 'text/html' } }); }
  } };
  const request = (name: string, init?: RequestInit) => serveAudio(new Request(`https://kiyo.test/audio-v2/${name}`, init), { ASSETS: assets });
  return { source, stage, clips, report, request, assets };
}

describe('deployment audio preserves individually addressable clips', () => {
  it('packs exact bytes and hashes without changing source audio or the app shell', async () => {
    const f = fixture();
    expect(f.report.clips).toBe(3); expect(f.report.chunks).toBe(2);
    expect(readFileSync(join(f.stage, 'index.html'), 'utf8')).toBe('application shell');
    for (const [name, bytes] of Object.entries(f.clips)) {
      expect(readFileSync(join(f.source, 'audio-v2', name))).toEqual(bytes);
      const index = JSON.parse(readFileSync(join(f.stage, 'audio-store', `index-${indexShard(name)}.json`), 'utf8')) as AudioIndex;
      const entry = index.files[name];
      expect(readFileSync(join(f.stage, 'audio-store', entry.chunk)).subarray(entry.offset, entry.offset + entry.length)).toEqual(bytes);
      const response = await f.request(name);
      expect(response.status).toBe(200); expect(response.headers.get('content-type')).toBe('audio/mpeg');
      expect(response.headers.get('etag')).toBe(`"${sha(bytes)}"`);
      expect(Buffer.from(await response.arrayBuffer())).toEqual(bytes);
    }
  });
  it('serves clip-relative ranges, suffixes, HEAD and conditional requests', async () => {
    const f = fixture();
    const name = 'second.mp3', bytes = f.clips[name];
    for (const [range, start, end] of [['bytes=3-7', 3, 7], ['bytes=3-', 3, bytes.length - 1], ['bytes=-4', bytes.length - 4, bytes.length - 1]] as const) {
      const response = await f.request(name, { headers: { Range: range } });
      expect(response.status).toBe(206);
      expect(response.headers.get('content-range')).toBe(`bytes ${start}-${end}/${bytes.length}`);
      expect(Buffer.from(await response.arrayBuffer())).toEqual(bytes.subarray(start, end + 1));
    }
    const head = await f.request(name, { method: 'HEAD' });
    expect(head.headers.get('content-length')).toBe(String(bytes.length)); expect(await head.text()).toBe('');
    expect((await f.request(name, { headers: { 'If-None-Match': `"${sha(bytes)}"` } })).status).toBe(304);
    expect((await f.request(name, { headers: { Range: 'bytes=1-3', 'If-Range': 'old' } })).status).toBe(200);
    expect((await f.request(name, { headers: { Range: 'bytes=9999-' } })).status).toBe(416);
  });
  it('does not return neighbouring clips when the asset adapter ignores ranges', async () => {
    const f = fixture(true);
    expect(Buffer.from(await (await f.request('second.mp3')).arrayBuffer())).toEqual(f.clips['second.mp3']);
  });
  it('rejects missing clips and an HTML login/fallback masquerading as index or audio', async () => {
    const f = fixture();
    expect((await f.request('missing.mp3')).status).toBe(404);
    const request = new Request('https://kiyo.test/audio-v2/first.mp3');
    const htmlAssets = { fetch: async () => new Response('login', { headers: { 'Content-Type': 'text/html' } }) };
    expect((await serveAudio(request, { ASSETS: htmlAssets })).status).toBe(503);
    const badChunk = { fetch: async (r: Request) => new URL(r.url).pathname.endsWith('.json') ? f.assets.fetch(r) : htmlAssets.fetch() };
    expect((await serveAudio(request, { ASSETS: badChunk })).status).toBe(502);
    expect((await f.request('first.mp3', { method: 'POST' })).status).toBe(405);
  });
  it('refuses unsafe staging paths and empty clips', () => {
    const f = fixture();
    expect(() => packAudio(f.source, f.source)).toThrow();
    expect(() => packAudio(f.source, join(f.source, 'stage'))).toThrow('Unsafe');
    writeFileSync(join(f.source, 'audio-v2', 'empty.mp3'), '');
    expect(() => packAudio(f.source, f.stage)).toThrow('Invalid clip size');
  });
  it('rejects ambiguous or impossible ranges', () => {
    for (const range of ['bytes=-0', 'bytes=4-2', 'bytes=0-1,4-5', 'bytes=-', 'bytes=1e3-']) expect(byteRange(range, 12)).toBeNull();
  });
});
