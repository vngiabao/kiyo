// What a picked answer sounds like: Sayo reads a Chinese answer (her recorded clip
// only, never the device voice); anything else gets the interface pop.
import { browserSpeech, hasSayoClip } from "./audio";
import { answerSpeechText } from "./answer-text";
import { audioCatalog, loadAudioCatalog } from "./audio-catalog";
import { sfx } from "./sfx";
import { sayoVoiceURI } from "./sayo-voice";
import type { Profile } from "./types";

let lastAnswer = 0;
export function answerFeedback(
  say: string | undefined,
  profile: Pick<Profile, "readChoices" | "quiet" | "voiceURI">,
) {
  const request = ++lastAnswer;
  const raw = say?.trim();
  // A single character is read with its taught pronunciation, like its own sound button.
  const text = raw && answerSpeechText(raw);
  if (!text || profile.readChoices === false || profile.quiet) {
    sfx.tap();
    return;
  }
  // First interaction can precede the lazy catalogue. Wait for it instead of
  // incorrectly treating every recorded answer as absent on a cold page.
  if (!audioCatalog()) {
    void loadAudioCatalog()
      .then(() => {
        if (request === lastAnswer) answerFeedback(say, profile);
      })
      .catch(() => {
        if (request === lastAnswer) sfx.tap();
      });
    return;
  }
  // A bare polyphonic glyph is not a safe substitute for its taught reading.
  const clip = hasSayoClip(text) ? text : null;
  if (clip) {
    const preferred = sayoVoiceURI(profile.voiceURI);
    void browserSpeech
      .speak(clip, {
        voiceURI: preferred.startsWith("local:") ? preferred : "local:clear",
        allowDeviceFallback: false,
      })
      .catch(() => {
        if (request === lastAnswer) sfx.tap();
      });
    return;
  }
  sfx.tap();
}
