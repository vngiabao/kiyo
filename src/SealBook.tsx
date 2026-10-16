import { useRef, useState } from "react";
import { characters } from "./hanzi";
import { Pinyin } from "./components";
import { MoSays } from "./Mascot";
import type { CharStatus } from "./Characters";
import { browserSpeech, hasSayoClip } from "./audio";
import { gsap, reducedMotion, useGSAP } from "./motion";
import { sfx } from "./sfx";

const tierName: Record<Exclude<CharStatus, "new">, string> = {
  met: "Met",
  recognised: "Recognised",
  secure: "Secure",
};

/**
 * 印章簿: every character the learner has met, as a seal. The seal deepens with
 * evidence (met → recognised → secure, from unaided reading answers), never by
 * time spent. Tap a seal to hear Sayo say it.
 */
export function SealBook({ status, voiceURI }: { status: Record<string, CharStatus>; voiceURI?: string }) {
  const root = useRef<HTMLDivElement>(null);
  const [picked, setPicked] = useState<string | null>(null);
  const collected = characters.filter((c) => status[c.hanzi] && status[c.hanzi] !== "new");
  const next = characters.filter((c) => !status[c.hanzi] || status[c.hanzi] === "new").slice(0, 8);
  const count = (s: CharStatus) => collected.filter((c) => status[c.hanzi] === s).length;
  const pick = characters.find((c) => c.hanzi === picked);
  // The book opens with its seals stamping down in order.
  useGSAP(
    () => {
      if (reducedMotion()) return;
      const seals = root.current!.querySelectorAll(".seal-book-grid .seal");
      if (!seals.length) return;
      gsap.from(seals, {
        scale: 1.5, rotation: () => gsap.utils.random(-14, 14), opacity: 0, duration: 0.3, ease: "power4.in",
        stagger: Math.min(0.04, 0.9 / seals.length), clearProps: "transform,opacity",
      });
    },
    { scope: root },
  );
  return (
    <div className="seal-book" ref={root}>
      <header className="seal-book-head">
        <h2>
          <span lang="zh-CN">印章簿</span> Your seals
        </h2>
        <p className="muted">
          A seal marks a character you have met. It deepens as you read it
          without help: outline when met, tinted when recognised, solid when secure.
        </p>
        <dl className="seal-book-counts">
          <div><dt>Seals</dt><dd className="tabular">{collected.length}</dd></div>
          <div><dt>Secure</dt><dd className="tabular">{count("secure")}</dd></div>
          <div><dt>Recognised</dt><dd className="tabular">{count("recognised")}</dd></div>
          <div><dt>Met</dt><dd className="tabular">{count("met")}</dd></div>
        </dl>
      </header>
      {collected.length === 0 ? (
        <div className="seal-book-empty">
          <MoSays state="stamp" size={120} side="left" />
          <p>Your first seal arrives with your first character lesson.</p>
        </div>
      ) : (
        <ul className="seal-book-grid" aria-label="Characters you have met">
          {collected.map((c) => (
            <li key={c.id}>
              <button
                className={`seal tier-${status[c.hanzi]} ${picked === c.hanzi ? "is-picked" : ""}`}
                lang="zh-CN"
                aria-label={`${c.hanzi}, ${c.meaning}, ${tierName[status[c.hanzi] as Exclude<CharStatus, "new">]}`}
                aria-pressed={picked === c.hanzi}
                onClick={() => {
                  setPicked(c.hanzi);
                  const say = hasSayoClip(c.say) ? c.say : hasSayoClip(c.hanzi) ? c.hanzi : null;
                  if (say) void browserSpeech.speak(say, { voiceURI }).catch(() => {});
                  else sfx.stamp();
                }}
              >
                {c.hanzi}
              </button>
            </li>
          ))}
        </ul>
      )}
      {pick && (
        <p className="seal-book-detail" role="status">
          <span lang="zh-CN">{pick.hanzi}</span>
          <Pinyin text={pick.pinyin} />
          <span>{pick.meaning}</span>
          <small>{tierName[status[pick.hanzi] as Exclude<CharStatus, "new">]}</small>
        </p>
      )}
      {next.length > 0 && (
        <section className="seal-book-next" aria-labelledby="seal-next-title">
          <h3 id="seal-next-title">Next to collect</h3>
          <ul className="seal-book-grid is-next">
            {next.map((c) => (
              <li key={c.id}>
                <span className="seal tier-new" lang="zh-CN" aria-label={`${c.hanzi}, ${c.meaning}, not yet met`}>
                  {c.hanzi}
                </span>
              </li>
            ))}
          </ul>
        </section>
      )}
    </div>
  );
}
