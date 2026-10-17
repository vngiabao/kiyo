import { characterSpeech } from "./hanzi";

/** English explanations mentioning hanzi are labels, not Mandarin to read aloud. */
export function answerSpeechText(raw: string): string | null {
  const text = raw.trim();
  if (!/\p{Script=Han}/u.test(text) || /[a-z]/i.test(text)) return null;
  return Array.from(text).length === 1 ? characterSpeech(text) : text;
}
