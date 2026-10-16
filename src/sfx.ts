// Interface sound effects, synthesised with Web Audio: original, tiny, offline.
// They never touch Sayo's clips. When an effect plays, Sayo's automatic reaction
// waits until it has finished (voiceDelay) so the two never talk over each other.

import { preferPlaybackSession } from "./audio-session";

let ctx: AudioContext | null = null;
let master: GainNode | null = null;
let enabled = true;
let quietUntil = 0;

/** App calls this whenever the profile changes: Settings → Sound effects, and quiet mode. */
export function setSfxEnabled(on: boolean) {
  enabled = on;
}

/** How long Sayo's automatic line should wait so it starts after the current effect. */
export function voiceDelay() {
  return Math.max(0, quietUntil - performance.now());
}

function audio() {
  if (!enabled || typeof window === "undefined" || !("AudioContext" in window)) return null;
  if (!ctx) {
    preferPlaybackSession();
    ctx = new AudioContext();
    const comp = ctx.createDynamicsCompressor();
    comp.threshold.value = -18;
    comp.ratio.value = 4;
    master = ctx.createGain();
    master.gain.value = 0.22;
    master.connect(comp).connect(ctx.destination);
  }
  // Effects only play from taps and key presses, so resuming here is allowed on iOS too.
  if (ctx.state === "suspended") void ctx.resume();
  return ctx;
}

type Voice = { type?: OscillatorType; gain?: number; ratio?: number };

/** One struck note with a few partials and an exponential decay, like a small bell. */
function note(freq: number, at: number, length: number, voices: Voice[], filter?: number) {
  const c = audio();
  if (!c || !master) return;
  const t = c.currentTime + at;
  const out = c.createGain();
  out.gain.setValueAtTime(0.0001, t);
  out.gain.exponentialRampToValueAtTime(1, t + 0.006);
  out.gain.exponentialRampToValueAtTime(0.0001, t + length);
  let tail: AudioNode = out;
  if (filter) {
    const lp = c.createBiquadFilter();
    lp.type = "lowpass";
    lp.frequency.value = filter;
    out.connect(lp);
    tail = lp;
  }
  tail.connect(master);
  for (const v of voices) {
    const o = c.createOscillator();
    const g = c.createGain();
    o.type = v.type ?? "sine";
    o.frequency.setValueAtTime(freq * (v.ratio ?? 1), t);
    g.gain.value = v.gain ?? 1;
    o.connect(g).connect(out);
    o.start(t);
    o.stop(t + length + 0.05);
  }
}

/** A light haptic tap on phones that allow it (Android); iOS ignores web vibration. */
function buzz(pattern: number | number[]) {
  if (!enabled || typeof navigator === "undefined" || !("vibrate" in navigator)) return;
  if (!matchMedia("(pointer: coarse)").matches) return;
  try {
    navigator.vibrate(pattern);
  } catch {
    /* Blocked without a user gesture; nothing to do. */
  }
}

function hold(seconds: number) {
  quietUntil = Math.max(quietUntil, performance.now() + seconds * 1000);
}

const bell: Voice[] = [
  { type: "sine", gain: 0.8 },
  { type: "sine", gain: 0.25, ratio: 2 },
  { type: "triangle", gain: 0.08, ratio: 3 },
];
const C5 = 523.25, E5 = 659.25, G5 = 783.99, C6 = 1046.5, E6 = 1318.5, G6 = 1568;

export const sfx = {
  /** Picking an answer, a token or a card: a soft pop. */
  tap() {
    const c = audio();
    if (!c || !master) return;
    const t = c.currentTime;
    const o = c.createOscillator();
    const g = c.createGain();
    o.type = "sine";
    o.frequency.setValueAtTime(1150, t);
    o.frequency.exponentialRampToValueAtTime(620, t + 0.06);
    g.gain.setValueAtTime(0.0001, t);
    g.gain.exponentialRampToValueAtTime(0.45, t + 0.004);
    g.gain.exponentialRampToValueAtTime(0.0001, t + 0.08);
    o.connect(g).connect(master);
    o.start(t);
    o.stop(t + 0.1);
  },
  /** A seal stamping down: a soft, low thud with a paper tick. */
  stamp() {
    const c = audio();
    if (!c || !master) return;
    const t = c.currentTime;
    const o = c.createOscillator();
    const g = c.createGain();
    o.type = "sine";
    o.frequency.setValueAtTime(170, t);
    o.frequency.exponentialRampToValueAtTime(70, t + 0.12);
    g.gain.setValueAtTime(0.0001, t);
    g.gain.exponentialRampToValueAtTime(0.9, t + 0.005);
    g.gain.exponentialRampToValueAtTime(0.0001, t + 0.16);
    o.connect(g).connect(master);
    o.start(t);
    o.stop(t + 0.2);
    note(2400, 0.004, 0.03, [{ type: "triangle", gain: 0.12 }]);
    buzz(12);
  },
  /** A right answer: two bright rising bell notes. */
  correct() {
    if (!audio()) return;
    note(C6, 0, 0.4, bell);
    note(G6, 0.085, 0.55, bell);
    buzz(18);
    hold(0.32);
  },
  /** A wrong answer: two low, soft falling notes. Information, not punishment. */
  wrong() {
    if (!audio()) return;
    const soft: Voice[] = [{ type: "triangle", gain: 0.7 }, { type: "sine", gain: 0.3, ratio: 2 }];
    note(349.23, 0, 0.22, soft, 1400);
    note(293.66, 0.12, 0.32, soft, 1200);
    buzz([28, 60, 28]);
    hold(0.36);
  },
  /** A finished lesson: a rising arpeggio. */
  complete() {
    if (!audio()) return;
    [C5, E5, G5, C6].forEach((f, i) => note(f, i * 0.075, i === 3 ? 0.8 : 0.35, bell));
    buzz([16, 60, 16, 60, 40]);
    hold(0.55);
  },
  /** A level up: the arpeggio climbs higher and lands on a chord. */
  levelUp() {
    if (!audio()) return;
    [C5, E5, G5, C6, E6].forEach((f, i) => note(f, i * 0.07, 0.4, bell));
    [C6, E6, G6].forEach((f) => note(f, 0.42, 1.1, bell));
    buzz([16, 50, 16, 50, 16, 80, 60]);
    hold(0.9);
  },
};
