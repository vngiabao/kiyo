import { indexShard, type AudioIndex } from './audio-index';

type Assets = { fetch(request: Request): Promise<Response> };
type Environment = { ASSETS: Assets };

// The assets binding can ignore Range. Read only as far as this clip instead of
// buffering an entire 8 MiB chunk for every play on the free Worker budget.
function clipStream(body: ReadableStream<Uint8Array>, start: number, length: number) {
  const reader = body.getReader();
  let position = 0, sent = 0;
  return new ReadableStream<Uint8Array>({
    async pull(controller) {
      try {
        while (sent < length) {
          const { value, done } = await reader.read();
          if (done) throw new Error('Audio chunk ended before the requested clip');
          const begin = Math.max(0, start - position);
          position += value.byteLength;
          if (begin >= value.byteLength) continue;
          const count = Math.min(length - sent, value.byteLength - begin);
          controller.enqueue(value.slice(begin, begin + count));
          sent += count;
          if (sent === length) {
            controller.close();
            await reader.cancel().catch(() => {});
          }
          return;
        }
      } catch (error) {
        controller.error(error);
        await reader.cancel(error).catch(() => {});
      }
    },
    cancel: reason => reader.cancel(reason),
  });
}

// Return null for an invalid range, and undefined when no range was requested.
export function byteRange(value: string | null, length: number) {
  if (!value) return undefined;
  const match = /^bytes=(\d*)-(\d*)$/.exec(value);
  if (!match || (!match[1] && !match[2])) return null;
  const start = match[1] ? Number(match[1]) : Math.max(0, length - Number(match[2]));
  const end = match[1] ? (match[2] ? Math.min(Number(match[2]), length - 1) : length - 1) : length - 1;
  if (!Number.isSafeInteger(start) || !Number.isSafeInteger(end) || start < 0 || start > end || start >= length) return null;
  return { start, end };
}

export async function serveAudio(request: Request, env: Environment): Promise<Response> {
  const url = new URL(request.url);
  const match = /^\/audio-v2\/([a-zA-Z0-9_-]+\.mp3)$/.exec(url.pathname);
  if (!match) return env.ASSETS.fetch(request);
  if (request.method !== 'GET' && request.method !== 'HEAD') return new Response(null, { status: 405, headers: { Allow: 'GET, HEAD' } });
  const filename = match[1];
  const indexUrl = new URL(`/audio-store/index-${indexShard(filename)}.json`, url);
  const response = await env.ASSETS.fetch(new Request(indexUrl));
  if (!response.ok || !/json/i.test(response.headers.get('content-type') ?? '')) {
    console.warn('Audio index unavailable', filename, response.status, response.headers.get('content-type'));
    return new Response('Audio index unavailable', { status: 503 });
  }
  const index = await response.json() as AudioIndex;
  const entry = index.version === 1 ? index.files?.[filename] : undefined;
  if (!entry) {
    console.warn('Audio not found', filename);
    return new Response('Audio not found', { status: 404 });
  }
  if (!/^chunk-[a-f0-9]{64}\.bin$/.test(entry.chunk) || !Number.isSafeInteger(entry.offset) || entry.offset < 0 || !Number.isSafeInteger(entry.length) || entry.length < 1 || !/^[a-f0-9]{64}$/.test(entry.sha256)) return new Response('Invalid audio index', { status: 503 });
  const etag = `"${entry.sha256}"`;
  const headers = new Headers({ 'Content-Type': 'audio/mpeg', 'Cache-Control': 'private, max-age=31536000, immutable', 'ETag': etag, 'Accept-Ranges': 'bytes', 'X-Content-Type-Options': 'nosniff' });
  if (request.headers.get('if-none-match')?.split(',').map(v => v.trim()).includes(etag)) return new Response(null, { status: 304, headers });
  const ifRange = request.headers.get('if-range');
  const range = byteRange(ifRange && ifRange !== etag ? null : request.headers.get('range'), entry.length);
  if (range === null) {
    headers.set('Content-Range', `bytes */${entry.length}`);
    return new Response(null, { status: 416, headers });
  }
  const start = range?.start ?? 0;
  const end = range?.end ?? entry.length - 1;
  headers.set('Content-Length', String(end - start + 1));
  if (range) headers.set('Content-Range', `bytes ${start}-${end}/${entry.length}`);
  const status = range ? 206 : 200;
  if (request.method === 'HEAD') return new Response(null, { status, headers });
  const chunkUrl = new URL(`/audio-store/${entry.chunk}`, url);
  const from = entry.offset + start;
  const to = entry.offset + end;
  const chunk = await env.ASSETS.fetch(new Request(chunkUrl, { headers: { Range: `bytes=${from}-${to}` } }));
  if (chunk.status === 206 && chunk.headers.get('content-range')?.startsWith(`bytes ${from}-${to}/`)) return new Response(chunk.body, { status, headers });
  // Some local asset adapters ignore Range. Never return a whole chunk as a clip.
  if (chunk.status === 200 && chunk.body && !/html|json/i.test(chunk.headers.get('content-type') ?? '')) {
    const declaredLength = chunk.headers.get('content-length');
    if (declaredLength && Number(declaredLength) <= to) return new Response('Audio data unavailable', { status: 502 });
    return new Response(clipStream(chunk.body, from, end - start + 1), { status, headers });
  }
  console.warn('Audio data unavailable', filename, chunk.status, chunk.headers.get('content-type'));
  return new Response('Audio data unavailable', { status: 502 });
}

export default { fetch: serveAudio };
