// What a picked answer sounds like: Sayo reads a Chinese answer (her recorded clip
// only, never the device voice); anything else gets the interface pop.
import { browserSpeech, hasSayoClip } from "./audio";
import { characterSpeech } from "./hanzi";
import { sfx } from "./sfx";
import type { Profile } from "./types";

export function answerFeedback(say: string | undefined, profile: Pick<Profile, "readChoices" | "quiet" | "voiceURI">) {
  const raw = say?.trim();
  // A single character is read with its taught pronunciation, like its own sound button.
  const text = raw && Array.from(raw).length === 1 ? characterSpeech(raw) : raw;
  const clip = text && hasSayoClip(text) ? text : raw && hasSayoClip(raw) ? raw : null;
  if (clip && profile.readChoices !== false && !profile.quiet) {
    void browserSpeech.speak(clip, { voiceURI: profile.voiceURI }).catch(() => {});
    return;
  }
  sfx.tap();
}
