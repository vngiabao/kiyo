import { audioCatalog, loadAudioCatalog } from "./audio-catalog";
import deliveryRates from "../content/voices/playback-rates.json";
import { sayoVoiceURI, voiceKey as key, type SayoMood } from "./sayo-voice";
type Options = {
  signal?: AbortSignal;
  rate?: number;
  voiceURI?: string;
  mood?: SayoMood;
  /** Answer taps must stay in Sayo's voice, even when a recording fails to load. */
  allowDeviceFallback?: boolean;
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
let builtIndex: Record<string, Record<string, string>> | null = null;
/** Clip lookup by normalised text; null until the catalogue has loaded. */
function clipIndex() {
  const catalog = audioCatalog();
  if (!builtIndex && catalog)
    builtIndex = Object.fromEntries(
      Object.entries(catalog).map(([text, voices]) => [key(text), voices]),
    );
  return builtIndex;
}
/** True when Sayo has a recorded clip for this exact text (no device-voice fallback needed). */
export const hasSayoClip = (text: string) => !!clipIndex()?.[key(text)];
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
  speak(text, options = {}): Promise<void> {
    if (options.signal?.aborted) return Promise.resolve();
    // First sound of the session may arrive before the catalogue: wait for it once.
    const index = clipIndex();
    if (!index)
      return loadAudioCatalog().then(
        () => browserSpeech.speak(text, options),
        () => speakWith({}, text, options),
      );
    return speakWith(index, text, options);
  },
  stop,
};

function speakWith(
  index: Record<string, Record<string, string>>,
  text: string,
  options: Options,
): Promise<void> {
  {
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
        if (options.allowDeviceFallback === false) {
          active?.pause();
          finish(
            false,
            loadError ??
              new Error("No Sayo recording is available for this answer."),
          );
          return;
        }
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
  }
}
