// iOS mutes Web Audio (the answer chime) under the silent switch unless the page
// asks for "playback". Lesson audio is something the learner chose to start, so ask.
type AudioSessionNavigator = Navigator & { audioSession?: { type: string } };
export function preferPlaybackSession() {
  const nav = navigator as AudioSessionNavigator;
  try {
    if (nav.audioSession) nav.audioSession.type = "playback";
  } catch {
    /* Older Safari or other browsers: nothing to do. */
  }
}
