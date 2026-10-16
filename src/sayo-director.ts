// Sayo's little state machine (in the spirit of Rive's "Teddy" login): she reacts to what
// the learner is doing, using her approved poses as states. Anything can cue her;
// every visible Sayo with `follow` listens and returns to her own pose when the cue ends.
import type { MascotState, MoLine } from "./sayo-lines";

export type Cue = { state: MascotState; until: number; reason: string; say?: MoLine } | null;
type Listener = (cue: Cue) => void;

const listeners = new Set<Listener>();
let current: Cue = null;
let timer: ReturnType<typeof setTimeout> | undefined;

export function onSayoCue(listener: Listener) {
  listeners.add(listener);
  listener(current);
  return () => void listeners.delete(listener);
}

/** Show `state` for `ms` (Infinity = until cleared). A newer cue replaces an older one. */
export function cueSayo(state: MascotState, ms: number, reason: string, say?: MoLine) {
  clearTimeout(timer);
  current = { state, until: performance.now() + ms, reason, say };
  listeners.forEach((l) => l(current));
  if (Number.isFinite(ms)) timer = setTimeout(() => clearSayo(reason), ms);
}

/** End the cue, but only if it is still the one this caller started. */
export function clearSayo(reason?: string) {
  if (reason && current?.reason !== reason) return;
  clearTimeout(timer);
  current = null;
  listeners.forEach((l) => l(null));
}

/**
 * App-wide triggers, attached once. The learner's actions become Sayo's states:
 *  - peeking at pinyin, words or a transcript → she closes her eyes ("I didn't see that");
 *  - hovering a hint control → a raised finger;
 *  - typing an answer → she looks thoughtful;
 *  - 45 s without input → she dozes; any movement wakes her.
 */
export function startSayoDirector() {
  const peek = /^(Show (pinyin|the words|transcript|romaji)|Reveal|Peek|Show hint)/i;
  const onClick = (e: MouseEvent) => {
    const b = (e.target as Element | null)?.closest("button");
    if (b && peek.test(b.textContent?.trim() ?? "")) cueSayo("rest", 1600, "peek");
  };
  const onOver = (e: PointerEvent) => {
    const b = (e.target as Element | null)?.closest("button");
    if (b && peek.test(b.textContent?.trim() ?? "")) cueSayo("hint", 1200, "hover-hint");
  };
  const onFocus = (e: FocusEvent) => {
    const el = e.target as Element | null;
    if (el?.matches("input[type=text], input:not([type]), textarea, .fill-slot input")) cueSayo("think", Infinity, "typing");
  };
  const onBlur = () => clearSayo("typing");
  let idle: ReturnType<typeof setTimeout> | undefined;
  const wake = () => {
    clearSayo("idle");
    clearTimeout(idle);
    idle = setTimeout(() => cueSayo("rest", Infinity, "idle"), 45_000);
  };
  wake();
  document.addEventListener("click", onClick, true);
  document.addEventListener("pointerover", onOver, true);
  document.addEventListener("focusin", onFocus);
  document.addEventListener("focusout", onBlur);
  for (const type of ["pointermove", "keydown", "scroll", "touchstart"] as const)
    window.addEventListener(type, wake, { passive: true });
  return () => {
    clearTimeout(idle);
    document.removeEventListener("click", onClick, true);
    document.removeEventListener("pointerover", onOver, true);
    document.removeEventListener("focusin", onFocus);
    document.removeEventListener("focusout", onBlur);
    for (const type of ["pointermove", "keydown", "scroll", "touchstart"] as const)
      window.removeEventListener(type, wake);
  };
}
