// Kiyo's interactive layer: small, physical responses to the pointer and to clicks.
//  - Sayo leans and turns toward the pointer (any .mascot[data-follow]).
//  - Cards catch a soft light where the pointer is (.spot-host).
//  - Primary buttons lean toward the pointer (magnetic).
//  - Today's big character floats against its practice grid (parallax).
//  - Clicking empty space stamps a seal (印章) with a character you have learned.
//  - Poke Sayo three times and she pouts, with one of her recorded lines.
// Fine pointers only for hover effects; everything visual is skipped under reduced motion.
import { gsap, reducedMotion } from "./motion";
import { sfx } from "./sfx";
import { browserSpeech, hasSayoClip } from "./audio";
import { reactionMood } from "./sayo-voice";
import { cueSayo, onSayoCue } from "./sayo-director";

const SPOT = ".unit-card, .path-stop, .sayo-card, .choice, .hsk-choices label, .lead-glyph, .scenario-options button";
const MAGNET = ".button:not(.secondary):not(:disabled)";
const INTERACTIVE = "button, a, input, select, textarea, label, summary, [role=button], [role=radio], [role=tab], [contenteditable], dialog, .word-card, .stamp";
// Her recorded lines that fit being poked (zh, pinyin, English).
const pokeLines = [
  { zh: "嗯，我看见了。", py: "Ńg, wǒ kàn jiàn le.", en: "Hmm. I saw that." },
  { zh: "别笑，下一题。", py: "Bié xiào, xià yì tí.", en: "Don’t grin. Next question." },
  { zh: "嗯？再瞧瞧。", py: "Ńg? Zài qiáoqiao.", en: "Hmm? Look again." },
];

let known: string[] = [];
/** App keeps this list current: characters from finished reading lessons. */
export function setKnownCharacters(chars: string[]) {
  known = chars;
}

const clamp = gsap.utils.clamp;
const lerp = (a: number, b: number, t: number) => a + (b - a) * t;
type Lean = { r: number; x: number; y: number };

export function startInteractions(opts: { voiceURI: () => string | undefined; quiet: () => boolean }) {
  const fine = matchMedia("(hover: hover) and (pointer: fine)");
  let px = -1, py = -1, raf = 0, idleFrames = 0;
  const leans = new WeakMap<HTMLElement, Lean>();
  const magnets = new Set<HTMLElement>();
  let lit: HTMLElement | null = null;

  const frame = () => {
    raf = 0;
    let moving = false;
    // Sayo leans toward the pointer, a few degrees at most.
    for (const el of document.querySelectorAll<HTMLElement>(".mascot[data-follow]")) {
      const box = el.getBoundingClientRect();
      if (!box.width || box.bottom < 0 || box.top > innerHeight) continue;
      const dx = px - (box.left + box.width / 2), dy = py - (box.top + box.height * 0.3);
      const target: Lean = px < 0 ? { r: 0, x: 0, y: 0 } : { r: clamp(-5, 5, dx / 90), x: clamp(-6, 6, dx / 70), y: clamp(-3, 3, dy / 120) };
      const now = leans.get(el) ?? { r: 0, x: 0, y: 0 };
      const next = { r: lerp(now.r, target.r, 0.12), x: lerp(now.x, target.x, 0.12), y: lerp(now.y, target.y, 0.12) };
      leans.set(el, next);
      // Lean the artwork, not the frame, so her halo and card stay upright.
      const img = el.querySelector("img");
      if (img) {
        img.style.rotate = `${next.r.toFixed(2)}deg`;
        img.style.translate = `${next.x.toFixed(2)}px ${next.y.toFixed(2)}px`;
      }
      if (Math.abs(next.r - target.r) > 0.02 || Math.abs(next.x - target.x) > 0.05) moving = true;
    }
    // Magnetic primary buttons: drift a few pixels toward the pointer, ease home when it leaves.
    for (const el of magnets) {
      const box = el.getBoundingClientRect();
      const dx = px - (box.left + box.width / 2), dy = py - (box.top + box.height / 2);
      const inside = Math.abs(dx) < box.width / 2 + 24 && Math.abs(dy) < box.height / 2 + 24;
      const [cx, cy] = (el.style.translate || "0px 0px").split(" ").map(parseFloat);
      const tx = inside ? clamp(-6, 6, dx * 0.15) : 0, ty = inside ? clamp(-4, 4, dy * 0.2) : 0;
      const nx = lerp(cx || 0, tx, 0.2), ny = lerp(cy || 0, ty, 0.2);
      el.style.translate = `${nx.toFixed(2)}px ${ny.toFixed(2)}px`;
      if (Math.abs(nx - tx) > 0.05 || Math.abs(ny - ty) > 0.05) moving = true;
      else if (!inside) { el.style.translate = ""; magnets.delete(el); }
    }
    if (moving || idleFrames++ < 2) raf = requestAnimationFrame(frame);
  };
  const kick = () => { idleFrames = 0; if (!raf) raf = requestAnimationFrame(frame); };

  const onMove = (e: PointerEvent) => {
    if (e.pointerType !== "mouse" || reducedMotion()) return;
    px = e.clientX; py = e.clientY;
    const target = e.target as Element | null;
    // Light on the card under the pointer.
    const host = fine.matches ? target?.closest<HTMLElement>(SPOT) ?? null : null;
    if (host !== lit) { lit?.classList.remove("is-lit-spot"); lit = host; host?.classList.add("spot-host", "is-lit-spot"); }
    if (host) {
      const b = host.getBoundingClientRect();
      host.style.setProperty("--mx", `${px - b.left}px`);
      host.style.setProperty("--my", `${py - b.top}px`);
      if (host.matches(".lead-glyph")) {
        host.style.setProperty("--px", ((px - b.left) / b.width - 0.5).toFixed(3));
        host.style.setProperty("--py", ((py - b.top) / b.height - 0.5).toFixed(3));
      }
    }
    const magnet = fine.matches ? target?.closest<HTMLElement>(MAGNET) : null;
    if (magnet) magnets.add(magnet);
    kick();
  };
  const onLeave = () => { px = -1; py = -1; lit?.classList.remove("is-lit-spot"); lit = null; kick(); };

  // Poke counting: three taps on her within 1.6 s.
  let pokes: number[] = [];
  const mascotAt = (x: number, y: number) =>
    [...document.querySelectorAll<HTMLElement>(".mascot[data-follow]")].find((m) => {
      const b = m.getBoundingClientRect();
      // Her art is a square frame; the figure sits in the middle half.
      return x > b.left + b.width * 0.25 && x < b.right - b.width * 0.25 && y > b.top + b.height * 0.08 && y < b.bottom - b.height * 0.04;
    });
  const poke = (m: HTMLElement) => {
    const now = performance.now();
    pokes = [...pokes.filter((t) => now - t < 1600), now];
    if (!reducedMotion()) gsap.fromTo(m.querySelector("img"), { scaleY: 0.92, scaleX: 1.05 }, { scaleY: 1, scaleX: 1, duration: 0.45, ease: "elastic.out(1, 0.4)", transformOrigin: "50% 100%", clearProps: "transform" });
    if (pokes.length >= 3) {
      pokes = [];
      const line = pokeLines[Math.floor(Math.random() * pokeLines.length)];
      cueSayo("grumpy", 2400, "poke", line);
      if (!opts.quiet() && hasSayoClip(line.zh)) void browserSpeech.speak(line.zh, { voiceURI: `local:${reactionMood(line.zh)}` }).catch(() => {});
    } else sfx.tap();
  };

  const onClick = (e: MouseEvent) => {
    const m = mascotAt(e.clientX, e.clientY);
    if (m) return poke(m);
    const target = e.target as Element | null;
    if (!target || target.closest(INTERACTIVE) || document.querySelector(".focus-layout")) return;
    // Only stamp on open space, not on text the learner may be selecting.
    if (getSelection()?.toString()) return;
    if ([...target.childNodes].some((n) => n.nodeType === 3 && n.textContent?.trim())) return;
    stamp(e.pageX, e.pageY);
  };

  // A pose change swaps her image; re-apply the current lean to the new one.
  const stopCues = onSayoCue(() => requestAnimationFrame(kick));
  document.addEventListener("pointermove", onMove, { passive: true });
  document.documentElement.addEventListener("pointerleave", onLeave);
  document.addEventListener("click", onClick);
  return () => {
    stopCues();
    cancelAnimationFrame(raf);
    document.removeEventListener("pointermove", onMove);
    document.documentElement.removeEventListener("pointerleave", onLeave);
    document.removeEventListener("click", onClick);
  };
}

/** A seal (印章) stamps down where you clicked, carrying a character you know. */
function stamp(x: number, y: number) {
  const layer = document.querySelector(".stamp-layer") ?? document.body.appendChild(Object.assign(document.createElement("div"), { className: "stamp-layer" }));
  const old = layer.querySelectorAll(".stamp");
  if (old.length >= 8) old[0].remove();
  const pool = known.length ? known : ["清", "学", "夜"];
  const s = document.createElement("span");
  s.className = "stamp";
  s.setAttribute("aria-hidden", "true");
  s.lang = "zh-CN";
  s.textContent = pool[Math.floor(Math.random() * pool.length)];
  s.style.left = `${x}px`;
  s.style.top = `${y}px`;
  layer.appendChild(s);
  sfx.stamp();
  // She stamps it with you.
  cueSayo("stamp", 1100, "stamp");
  const tilt = gsap.utils.random(-14, 14);
  if (reducedMotion()) {
    gsap.set(s, { rotation: tilt, xPercent: -50, yPercent: -50 });
    gsap.to(s, { opacity: 0, delay: 1.6, duration: 0.4, onComplete: () => s.remove() });
    return;
  }
  gsap.timeline({ onComplete: () => s.remove() })
    .fromTo(s, { xPercent: -50, yPercent: -50, scale: 1.7, rotation: tilt - 10, opacity: 0 },
      { scale: 1, rotation: tilt, opacity: 1, duration: 0.22, ease: "power4.in" })
    .to(s, { scale: 1.06, duration: 0.08, yoyo: true, repeat: 1, ease: "power1.out" })
    .to(s, { opacity: 0, y: -10, duration: 0.6, ease: "power1.in" }, "+=1.6");
}
