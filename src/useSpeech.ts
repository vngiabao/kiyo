import { useCallback, useEffect, useRef, useState } from "react";
import { browserSpeech } from "./audio";
import { useLiveQuery } from "dexie-react-hooks";
import { db } from "./db";
import { checkSignIn } from "./session";

/** Cancels only this control's playback when it leaves the screen. */
export function useSpeech() {
  const voiceURI = useLiveQuery(
    () => db.profiles.get("learner").then((p) => p?.voiceURI ?? ""),
    [],
    "",
  );
  const owner = useRef<AbortController | null>(null);
  const [playing, setPlaying] = useState(false);
  const [error, setError] = useState("");
  const stop = useCallback(() => owner.current?.abort(), []);
  useEffect(() => stop, [stop]);
  const speak = useCallback(
    (text: string, options: Parameters<typeof browserSpeech.speak>[1] = {}) => {
      owner.current?.abort();
      const controller = new AbortController();
      owner.current = controller;
      setError("");
      setPlaying(true);
      // An expired sign-in blocks every recording not saved yet; say that instead.
      const explain = (message: string) => {
        setError(message);
        void checkSignIn().then((expired) => {
          if (expired && owner.current === controller)
            setError("Your Kiyo sign-in expired, so Sayo’s recording couldn’t load. Sign in again from the banner at the top.");
        });
      };
      void browserSpeech
        .speak(text, {
          ...options,
          voiceURI: options.voiceURI ?? voiceURI,
          signal: controller.signal,
          onFallback: () => {
            explain("Using your device’s Mandarin voice for this line.");
            options.onFallback?.();
          },
          onEnd: () => {
            if (owner.current === controller) setPlaying(false);
            options.onEnd?.();
          },
        })
        .catch((reason: unknown) => {
          if (!controller.signal.aborted && owner.current === controller) {
            explain(
              reason instanceof Error
                ? reason.message
                : "Audio could not play. Tap to try again.",
            );
            setPlaying(false);
          }
        });
    },
    [voiceURI],
  );
  return { speak, stop, playing, error };
}
