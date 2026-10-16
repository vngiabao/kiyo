// Kiyo's motion vocabulary (GSAP). Transforms and opacity only; everything is
// skipped when the device asks for reduced motion. Frequent motion stays short
// (page entrances, trails); rare moments (level up, a lit streak) may be bigger.
import gsap from "gsap";
import { useGSAP } from "@gsap/react";

gsap.registerPlugin(useGSAP);
gsap.defaults({ ease: "power3.out", duration: 0.4 });

export { gsap, useGSAP };

export const reducedMotion = () =>
  typeof matchMedia === "function" &&
  matchMedia("(prefers-reduced-motion: reduce)").matches;

/** Sayo's palette for celebrations: peony blue, sound amber, hair violet, brooch teal. */
export const sayoColours = ["#86a8ff", "#f2c47e", "#b8a6ff", "#72d9b9"];

/** Rise-and-fade a set of elements in order. Returns the tween (or null when motion is off). */
export function rise(targets: gsap.TweenTarget, vars: gsap.TweenVars = {}) {
  if (reducedMotion()) return null;
  const els = quiet(targets);
  if (!els.length) return null;
  return gsap.from(els, {
    y: 14,
    opacity: 0,
    duration: 0.38,
    stagger: 0.05,
    clearProps: "transform,opacity,visibility,transition",
    ...vars,
  });
}

/**
 * Pause CSS transitions on elements GSAP is about to move; a CSS transform
 * transition fights the tween and stutters. Pair with clearProps "transition".
 */
export function quiet(targets: gsap.TweenTarget) {
  const els = gsap.utils.toArray<HTMLElement>(targets);
  gsap.set(els, { transition: "none" });
  return els;
}

/**
 * A short burst of small dots from the centre of `host`, for rare celebrations.
 * The dots are decorative, absolutely positioned and removed when done.
 */
export function burst(host: HTMLElement, count = 14) {
  if (reducedMotion()) return null;
  const dots = Array.from({ length: count }, (_, i) => {
    const d = document.createElement("span");
    d.className = "burst-dot";
    d.setAttribute("aria-hidden", "true");
    d.style.background = sayoColours[i % sayoColours.length];
    host.appendChild(d);
    return d;
  });
  const tl = gsap.timeline({ onComplete: () => dots.forEach((d) => d.remove()) });
  dots.forEach((d, i) => {
    const angle = (i / count) * Math.PI * 2 + gsap.utils.random(-0.2, 0.2);
    const distance = gsap.utils.random(70, 120);
    tl.fromTo(
      d,
      { x: 0, y: 0, scale: gsap.utils.random(0.6, 1.1), opacity: 1 },
      {
        x: Math.cos(angle) * distance,
        y: Math.sin(angle) * distance,
        scale: 0.2,
        opacity: 0,
        duration: gsap.utils.random(0.7, 1),
        ease: "power2.out",
      },
      0,
    );
  });
  return tl;
}
