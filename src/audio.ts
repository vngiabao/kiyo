import assets from "./audio-assets.json";
import deliveryRates from "../content/voices/playback-rates.json";
import { sayoVoiceURI, voiceKey as key, type SayoMood } from "./sayo-voice";
type Options = {
  signal?: AbortSignal;
  rate?: number;
  voiceURI?: string;
  mood?: SayoMood;
  onFallback?: () => void;
  onStart?: () => void;
  onEnd?: () => void;
  onComplete?: () => void;
};
export interface SpeechProvider {
  speak(text: string, options?: Options): Promise<void>;
  stop(): void;
}
export interface TranscriptionProvider {
  transcribe(
    audio: Blob,
    consent: boolean,
  ): Promise<{ text: string; confidence: number | null }>;
}
export interface PronunciationProvider {
  assess(
    audio: Blob,
    target: string,
    consent: boolean,
  ): Promise<{ intelligibility: string; toneEvidence: null | string }>;
}
export const mandarinVoices = () =>
  typeof speechSynthesis === "undefined"
    ? []
    : speechSynthesis
        .getVoices()
        .filter((v) => /^zh(-|_)(CN|Hans)/i.test(v.lang) || v.lang === "zh");
const index = Object.fromEntries(
  Object.entries(assets).map(([text, voices]) => [
    key(text),
    voices as Record<string, string>,
  ]),
);
let active: HTMLAudioElement | null = null,
  finishActive: (() => void) | null = null;
function stop() {
  active?.pause();
  active = null;
  finishActive?.();
  finishActive = null;
  if (typeof speechSynthesis !== "undefined") speechSynthesis.cancel();
}
export const browserSpeech: SpeechProvider = {
  speak(text, options = {}) {
    if (options.signal?.aborted) return Promise.resolve();
    stop();
    return new Promise((resolve, reject) => {
      let finished = false;
      const cancel = () => {
        if (finishActive === ownedFinish) stop();
      };
      const ownedFinish = () => finish();
      const finish = (complete = false, error?: Error) => {
        if (finished) return;
        finished = true;
        options.signal?.removeEventListener("abort", cancel);
        if (finishActive === ownedFinish) {
          finishActive = null;
          active = null;
        }
        options.onEnd?.();
        if (complete) options.onComplete?.();
        if (error) reject(error);
        else resolve();
      };
      finishActive = ownedFinish;
      options.signal?.addEventListener("abort", cancel, { once: true });
      const uri = sayoVoiceURI(options.voiceURI);
      // Punctuation-normalized file lookup shares words; preserve authored slow delivery.
      const rate =
        (options.rate ?? 1) *
        ((deliveryRates as Record<string, number>)[text] ?? 1);
      const local = uri.startsWith("local:");
      const voice = options.mood ?? uri.split(":")[1];
      const src = local
        ? (index[key(text)]?.[voice] ??
          index[key(text)]?.clear ??
          Object.values(index[key(text)] ?? {})[0])
        : undefined;
      let deviceStarted = false;
      const deviceSpeech = (loadError?: Error) => {
        if (finished || deviceStarted) return;
        deviceStarted = true;
        active?.pause();
        active = null;
        const voices = mandarinVoices();
        if (typeof speechSynthesis === "undefined" || !voices.length) {
          finish(
            false,
            loadError ??
              new Error(
                "No device Mandarin voice is available for this text. Use transcript support to continue.",
              ),
          );
          return;
        }
        if (local) options.onFallback?.();
        const u = new SpeechSynthesisUtterance(text);
        u.lang = "zh-CN";
        u.rate = rate;
        u.voice =
          voices.find((v) => v.voiceURI === uri) ??
          voices.find((v) => v.localService) ??
          voices[0];
        u.onstart = () => {
          if (!finished) options.onStart?.();
        };
        u.onend = () => finish(true);
        u.onerror = (e) =>
          e.error === "canceled" || e.error === "interrupted"
            ? finish()
            : finish(
                false,
                new Error(
                  "The device voice could not play. Tap play again or use the transcript.",
                ),
              );
        speechSynthesis.speak(u);
      };
      if (src) {
        const audio = new Audio(src);
        active = audio;
        audio.playbackRate = rate;
        audio.preservesPitch = true;
        audio.onended = () => {
          if (!deviceStarted) finish(true);
        };
        audio.onerror = () =>
          deviceSpeech(
            new Error(
              "This audio could not load. Replay when connected, or use the transcript.",
            ),
          );
        audio.onplaying = () => {
          if (!finished && !deviceStarted) options.onStart?.();
        };
        void audio
          .play()
          .catch(() =>
            deviceSpeech(
              new Error(
                "Audio playback was interrupted. Tap play again, or use the transcript.",
              ),
            ),
          );
        return;
      }
      deviceSpeech();
    });
  },
  stop,
};
