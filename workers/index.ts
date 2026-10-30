// Kiyo's Worker: Sayo's audio clips, and her daily note (Web Push).
import { serveAudio } from './audio';
import { handlePushApi, sendDueNotes, type PushEnvironment } from './push';

type Environment = { ASSETS: { fetch(request: Request): Promise<Response> } } & PushEnvironment;

export default {
  fetch(request: Request, env: Environment) {
    const { pathname } = new URL(request.url);
    // Reached only after Cloudflare Access lets the request through: a fresh sign-in.
    if (pathname === '/api/signin') return Response.redirect(new URL('/#today', request.url).href, 302);
    if (pathname.startsWith('/api/push/')) return handlePushApi(request, env);
    return serveAudio(request, env);
  },
  // Every 15 minutes: send each device its note once a day, at its chosen local time.
  async scheduled(_event: unknown, env: Environment) {
    await sendDueNotes(env);
  },
};
