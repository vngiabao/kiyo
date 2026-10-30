// Kiyo's Worker: Sayo's audio clips, and her daily note (Web Push).
import { serveAudio } from './audio';
import { handlePushApi, sendDueNotes, type PushEnvironment } from './push';

type Environment = { ASSETS: { fetch(request: Request): Promise<Response> } } & PushEnvironment;

export default {
  fetch(request: Request, env: Environment) {
    if (new URL(request.url).pathname.startsWith('/api/push/')) return handlePushApi(request, env);
    return serveAudio(request, env);
  },
  // Every 15 minutes: send each device its note once a day, at its chosen local time.
  async scheduled(_event: unknown, env: Environment) {
    await sendDueNotes(env);
  },
};
