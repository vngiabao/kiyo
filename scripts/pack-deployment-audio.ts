import { cpSync, existsSync, mkdirSync, readdirSync, readFileSync, rmSync, writeFileSync } from 'node:fs';
import { resolve, join, dirname, basename } from 'node:path';
import { createHash } from 'node:crypto';
import { fileURLToPath } from 'node:url';
import { indexShard, type AudioIndex } from '../workers/audio-index';

const sha = (bytes: Uint8Array) => createHash('sha256').update(bytes).digest('hex');

export function packAudio(source: string, destination: string, chunkLimit = 8 * 1024 * 1024) {
  source = resolve(source);
  destination = resolve(destination);
  if (source === destination || !existsSync(source)) throw new Error('Deployment must have a separate existing build source');
  // Only the explicitly named generated sibling directory can be replaced.
  if (dirname(destination) !== dirname(source) || !['.deploy-dist', 'stage'].includes(basename(destination))) throw new Error('Unsafe deployment staging path');
  if (existsSync(destination)) rmSync(destination, { recursive: true });
  cpSync(source, destination, { recursive: true, filter: path => path !== join(source, 'audio-v2') });
  const store = join(destination, 'audio-store');
  mkdirSync(store, { recursive: true });
  const indices = new Map<string, AudioIndex>();
  const queue: { filename: string; bytes: Buffer; sha256: string }[] = [];
  let queuedBytes = 0, clips = 0, chunks = 0, audioBytes = 0;
  const flush = () => {
    if (!queue.length) return;
    const bytes = Buffer.concat(queue.map(q => q.bytes));
    const chunk = `chunk-${sha(bytes)}.bin`;
    writeFileSync(join(store, chunk), bytes);
    let offset = 0;
    for (const q of queue) {
      const shard = indexShard(q.filename);
      let index = indices.get(shard);
      if (!index) { index = { version: 1, files: {} }; indices.set(shard, index); }
      index.files[q.filename] = { chunk, offset, length: q.bytes.length, sha256: q.sha256 };
      offset += q.bytes.length;
    }
    queue.length = 0; queuedBytes = 0; chunks++;
  };
  for (const filename of readdirSync(join(source, 'audio-v2')).sort()) {
    if (filename === 'assets.json') {
      mkdirSync(join(destination, 'audio-v2'), { recursive: true });
      cpSync(join(source, 'audio-v2', filename), join(destination, 'audio-v2', filename));
      continue;
    }
    if (!/^[a-zA-Z0-9_-]+\.mp3$/.test(filename)) throw new Error(`Unexpected audio asset: ${filename}`);
    const bytes = readFileSync(join(source, 'audio-v2', filename));
    if (!bytes.length || bytes.length > chunkLimit) throw new Error(`Invalid clip size: ${filename}`);
    if (queuedBytes + bytes.length > chunkLimit) flush();
    queue.push({ filename, bytes, sha256: sha(bytes) });
    queuedBytes += bytes.length; audioBytes += bytes.length; clips++;
  }
  flush();
  // Empty shards also return JSON, preventing missing-file SPA fallback responses.
  for (let i = 0; i < 256; i++) {
    const shard = i.toString(16).padStart(2, '0');
    writeFileSync(join(store, `index-${shard}.json`), JSON.stringify(indices.get(shard) ?? { version: 1, files: {} }));
  }
  const assetCount = readdirSync(destination, { recursive: true, withFileTypes: true }).filter(entry => entry.isFile()).length;
  if (assetCount > 20000) throw new Error(`Free static asset count exceeded: ${assetCount}`);
  const report = { clips, chunks, audioBytes, assetCount };
  console.log(`Deployment audio: ${clips} clips, ${chunks} chunks, ${(audioBytes / 1048576).toFixed(1)} MiB; ${assetCount}/20000 static files. Local MP3s unchanged.`);
  return report;
}

if (process.argv[1] && resolve(process.argv[1]) === fileURLToPath(import.meta.url)) packAudio('dist', '.deploy-dist');
