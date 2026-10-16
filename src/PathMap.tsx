import { useRef, type CSSProperties, type ReactNode } from "react";
import { gsap, quiet, reducedMotion, useGSAP } from "./motion";
import { BookOpen, ChatCircle, Check, Lightning } from "@phosphor-icons/react";
import { Mascot, MoSays, moLines } from "./Mascot";

export type PathNode = {
  id: string;
  /** What sits inside the stepping stone: a character, or an icon. */
  face: ReactNode;
  title: string;
  detail: string;
  status: "done" | "next" | "open";
  kind?: "learn" | "check" | "read";
  onOpen: () => void;
};
export type PathUnit = {
  id: string;
  number: number;
  title: string;
  subtitle: string;
  preview?: string;
  nodes: PathNode[];
};

// A gentle S-curve, in units of --swing.
const curve = [0, 1, 1.5, 1, 0, -1, -1.5, -1];

/**
 * A winding trail of stepping stones, grouped into numbered units.
 * Nothing is locked; the trail only suggests an order.
 */
export function PathMap({ units, label }: { units: PathUnit[]; label: string }) {
  let index = 0;
  const root = useRef<HTMLOListElement>(null);
  // Stones drop onto the trail one after another, following its curve.
  useGSAP(
    () => {
      if (reducedMotion()) return;
      gsap.from(".unit-banner", { y: 12, opacity: 0, duration: 0.35, clearProps: "all" });
      // Long trails (the Read path) keep the whole cascade under ~0.7 s.
      const each = Math.min(0.045, 0.7 / Math.max(1, gsap.utils.toArray(".stone", root.current).length));
      gsap.from(quiet(root.current!.querySelectorAll(".stone")), {
        scale: 0.5, y: -10, opacity: 0, duration: 0.45, ease: "back.out(1.8)",
        stagger: each, delay: 0.08, clearProps: "transform,opacity,visibility,transition",
      });
      gsap.from(".stone-label", {
        x: -8, opacity: 0, duration: 0.3, stagger: each, delay: 0.16, clearProps: "transform,opacity,visibility",
      });
    },
    { dependencies: [units.map((u) => u.id).join()], scope: root, revertOnUpdate: true },
  );
  return (
    <ol className="path-map" aria-label={label} ref={root}>
      {units.map((unit) => {
        const done = unit.nodes.filter((n) => n.status === "done").length;
        const complete = done > 0 && done === unit.nodes.length;
        return (
          <li key={unit.id} className={`path-unit ${complete ? "is-complete" : ""}`}>
            <header className="unit-banner">
              <span className="unit-number">Unit {unit.number}</span>
              <h3>{unit.title}</h3>
              <p>{unit.subtitle}</p>
              {unit.preview && (
                <p className="unit-preview" lang="zh-CN">
                  {unit.preview}
                </p>
              )}
              <span className="unit-count tabular">
                {complete ? (
                  <>
                    <Check size={14} weight="bold" aria-hidden /> Done
                  </>
                ) : (
                  `${done} / ${unit.nodes.length}`
                )}
              </span>
              {complete && (
                <span className="unit-complete-buddy">
                  <MoSays state="celebrate" say={moLines.done} size={84} side="left" className="is-compact" />
                </span>
              )}
            </header>
            <ol className="path-stones">
              {unit.nodes.map((node) => {
                const x = curve[index++ % curve.length];
                return (
                  <li
                    key={node.id}
                    className={`stone-row is-${node.status} side-${x > 0 ? "right" : x < 0 ? "left" : "mid"}`}
                    style={{ "--x": x } as CSSProperties}
                  >
                    <button
                      className={`stone kind-${node.kind ?? "learn"}`}
                      onClick={node.onOpen}
                      aria-label={`${node.title}. ${node.detail}${node.status === "done" ? ". Done" : node.status === "next" ? ". Start here" : ""}`}
                    >
                      <span className="stone-face" aria-hidden>
                        {node.face}
                      </span>
                      {node.status === "done" && (
                        <span className="stone-check" aria-hidden>
                          <Check size={14} weight="bold" />
                        </span>
                      )}
                    </button>
                    <span className="stone-label" aria-hidden>
                      <strong>{node.title}</strong>
                      <span>{node.detail}</span>
                    </span>
                    {node.status === "next" && (
                      <span className="stone-buddy">
                        <MoSays state="welcome" say={moLines.start} size={84} side="left" className="is-compact" follow />
                      </span>
                    )}
                  </li>
                );
              })}
            </ol>
          </li>
        );
      })}
    </ol>
  );
}

export const stoneIcon = {
  check: <Lightning size={26} weight="fill" />,
  read: <BookOpen size={26} weight="fill" />,
  speak: <ChatCircle size={26} weight="fill" />,
};

/** Plain-language stages of the whole journey, for complete beginners. */
export const journey = [
  { zh: "你好", title: "Hello and numbers", can: "Count to ten, say hello and read your first characters." },
  { zh: "认识", title: "Meeting people", can: "Say your name, where you’re from, and ask simple questions." },
  { zh: "生活", title: "Everyday life", can: "Food, time, places and making plans." },
  { zh: "故事", title: "Telling little stories", can: "Talk about your day and what you like." },
  { zh: "视频", title: "Easy videos", can: "Follow short videos with Chinese captions." },
  { zh: "聊天", title: "Real-speed chatting", can: "Understand people talking at normal speed." },
  { zh: "朋友", title: "Hanging out", can: "Joke, chat in a group and make friends." },
  { zh: "工作", title: "School and work", can: "Talk about projects, ideas and plans." },
  { zh: "得体", title: "Polished speaking", can: "Sound natural and kind in any setting." },
  { zh: "一辈子", title: "Lifelong Chinese", can: "Keep growing with the things you love." },
];

export function Journey({ current = 0 }: { current?: number }) {
  return (
    <section className="journey" aria-labelledby="journey-title">
      <h2 id="journey-title">Your whole journey</h2>
      <p className="muted">
        Ten big steps from your first 你好 to chatting with friends. The course
        runs through HSK 6; your place on it moves as you finish units.
      </p>
      <ol className="journey-steps">
        {journey.map((step, i) => (
          <li key={step.title} className={i < current ? "is-done" : i === current ? "is-here" : ""}>
            <span className="journey-dot tabular" aria-hidden>
              {i + 1}
            </span>
            <span className="journey-zh" lang="zh-CN">
              {step.zh}
            </span>
            <strong>{step.title}</strong>
            <span className="journey-can">{step.can}</span>
            {i === current && (
              <span className="journey-here">
                <Mascot state="read" size={56} still /> You are here
              </span>
            )}
          </li>
        ))}
      </ol>
    </section>
  );
}
