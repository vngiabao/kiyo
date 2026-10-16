import { voiceDelay } from "./sfx";
import {
  createContext,
  useContext,
  useState,
  useEffect,
  type CSSProperties,
  type PropsWithChildren,
} from "react";
import { useLiveQuery } from "dexie-react-hooks";
import {
  ArrowLeft,
  ArrowClockwise,
  DownloadSimple,
  Pause,
  Play,
} from "@phosphor-icons/react";
import { db } from "./db";
import { AudioButton, Pinyin } from "./components";
import { brand } from "./brand";
import "./mascot.css";
import { useSpeech } from "./useSpeech";
import { reactionMood } from "./sayo-voice";

import { mascotScenes, sceneById, type MascotState, type MoLine } from "./sayo-lines";
export { mascotScenes, moLines, pickLine, type MascotState, type MoLine } from "./sayo-lines";

const Preferences = createContext({ visible: true, motion: true, quiet: false, ready: false });
export function MascotProvider({ children }: PropsWithChildren) {
  const profile = useLiveQuery(() => db.profiles.get("learner"), [], null);
  return (
    <Preferences.Provider
      value={{
        visible: profile?.mascotEnabled !== false,
        motion: profile !== null && profile?.mascotMotion !== false,
        quiet: profile?.quiet ?? false,
        ready: profile !== null,
      }}
    >
      {children}
    </Preferences.Provider>
  );
}
export const useMascotVisible = () => useContext(Preferences).visible;

/** Decorative: the adjacent learning text remains the source of meaning. */
export function Mascot({
  state = "welcome",
  size = 112,
  active = false,
  still = false,
  showcase = false,
  className = "",
}: {
  state?: MascotState;
  size?: number;
  active?: boolean;
  still?: boolean;
  showcase?: boolean;
  className?: string;
}) {
  const preferences = useContext(Preferences);
  if (!showcase && !preferences.visible) return null;
  const motion = !still && preferences.motion;
  return (
    <span
      className={`mascot ${className}`}
      data-state={state}
      data-motion={motion}
      data-active={active}
      style={{ "--mascot-size": `${size}px` } as CSSProperties}
      aria-hidden="true"
    >
      <img
        key={`${state}-${active}`}
        src={`/mascot/web/${state}.webp`}
        width="480"
        height="480"
        alt=""
        draggable={false}
        decoding="async"
      />
    </span>
  );
}

/**
 * Sayo with a speech bubble. The bubble is real teaching text (Chinese, pinyin,
 * English) and stays readable even when the artwork is hidden in Settings.
 */
export function MoSays({
  state,
  say,
  size = 96,
  side = "right",
  className = "",
  showcase = false,
  autoSpeak = false,
  interactive = true,
  collapsible = false,
}: {
  state: MascotState;
  say?: MoLine;
  size?: number;
  side?: "right" | "left" | "top";
  className?: string;
  showcase?: boolean;
  autoSpeak?: boolean;
  interactive?: boolean;
  /** Show only the Chinese line on narrow screens until tapped. */
  collapsible?: boolean;
}) {
  const [expanded, setExpanded] = useState(false);
  const preferences = useContext(Preferences);
  const visible = preferences.visible || showcase;
  const words = say ?? sceneById[state].say;
  const { speak, stop, playing, error } = useSpeech();
  const Bubble = interactive ? "button" : "p";
  useEffect(() => {
    if (!autoSpeak || preferences.quiet || !preferences.ready) return;
    // Defer one tick so React's development effect replay cannot speak twice.
    // Starts after any interface sound (sfx.ts) so the chime never talks over her.
    const timer = setTimeout(() => speak(words.zh, { voiceURI: `local:${reactionMood(words.zh)}` }), voiceDelay());
    return () => { clearTimeout(timer); stop(); };
  }, [autoSpeak, preferences.quiet, preferences.ready, words.zh, speak, stop]);
  return (
    <div className={`mo-says side-${side} ${visible ? "" : "no-art"} ${collapsible ? "is-collapsible" : ""} ${expanded ? "is-expanded" : ""} ${className}`}>
      <Mascot state={state} size={size} showcase={showcase} active={playing} />
      <Bubble type={interactive ? "button" : undefined} className={`mo-bubble ${interactive ? "mo-voice" : ""}`} key={words.zh}
        aria-label={interactive ? playing ? "Stop Sayo’s voice" : `Hear Sayo: ${words.zh}` : undefined}
        aria-expanded={collapsible ? expanded : undefined}
        onClick={interactive ? () => { setExpanded(true); if (playing) stop(); else speak(words.zh, { voiceURI: `local:${reactionMood(words.zh)}` }); } : undefined}>
        <span className="mo-zh" lang="zh-CN">
          {words.zh}
        </span>
        <Pinyin text={words.py} className="mo-py" />
        <span className="mo-en">{words.en}</span>
        {interactive && <span className="mo-voice-hint">{playing ? "Speaking · stop" : "Hear Sayo"}</span>}
        {error && <span className="inline-error" role="alert">{error}</span>}
      </Bubble>
    </div>
  );
}

export function MascotGallery({ onBack }: { onBack: () => void }) {
  const preferences = useContext(Preferences);
  const [selected, setSelected] = useState<MascotState>("welcome");
  const [replay, setReplay] = useState(0);
  const [previewMotion, setMotion] = useState(true);
  const motion = previewMotion && preferences.motion;
  const scene = sceneById[selected];
  return (
    <main className="mascot-gallery">
      <header className="mascot-gallery-nav">
        <button className="text-button" onClick={onBack}>
          <ArrowLeft size={18} /> Back to {brand.name}
        </button>
        <span>小夜 Sayo · your study mentor</span>
      </header>
      <section className="mascot-feature" aria-labelledby="mascot-title">
        <div className="mascot-feature-copy">
          <p className="eyebrow">
            <span lang="zh-CN">小夜</span> Sayo
          </p>
          <h1 id="mascot-title">
            Few words.
            <br />
            All of them Chinese.
          </h1>
          <p>
            Sayo is a little shy, a little goofy, and quick to tease you with a
            grin. Her short Mandarin lines turn a welcome, a nudge, or a tiny
            victory into something you can learn and say back.
          </p>
          <p className="mascot-count">{mascotScenes.length} moods, each with a phrase to learn.</p>
          <div className="mascot-controls">
            <button
              className="button secondary"
              disabled={!preferences.motion}
              onClick={() => {
                setMotion(true);
                setReplay((n) => n + 1);
              }}
            >
              <ArrowClockwise size={18} /> Replay motion
            </button>
            <button
              className="text-button"
              disabled={!preferences.motion}
              aria-pressed={!motion}
              onClick={() => setMotion((m) => !m)}
            >
              {motion ? <Pause size={18} /> : <Play size={18} />}
              {!preferences.motion ? "Motion off in Settings" : motion ? "Pause motion" : "Enable motion"}
            </button>
          </div>
          <p className="small">
            Motion follows your device’s reduced-motion setting. You can hide Sayo or
            her motion in Settings; her phrases stay.
          </p>
        </div>
        <figure className="mascot-feature-art">
          <Mascot key={`${selected}-${replay}`} state={selected} size={360} active showcase still={!motion} />
          <figcaption aria-live="polite">
            <p className="mo-bubble is-large">
              <span className="mo-zh" lang="zh-CN">
                {scene.say.zh}
              </span>
              <Pinyin text={scene.say.py} className="mo-py" />
              <span className="mo-en">{scene.say.en}</span>
            </p>
            <AudioButton text={scene.say.zh} voiceURI={`local:${reactionMood(scene.say.zh)}`} label="Hear this line" />
          </figcaption>
        </figure>
      </section>
      <section className="mascot-collection" aria-labelledby="collection-title">
        <div className="mascot-collection-head">
          <h2 id="collection-title">Her moods</h2>
            <a className="text-button" href={`/mascot/quiet/${selected}.png`} download={`mo-${selected}.png`}>
              <DownloadSimple size={18} /> Download this pose
            </a>
        </div>
        <p className="mascot-scene-description" aria-live="polite">
          <strong>{scene.name}.</strong> {scene.use}
        </p>
        <div className="mascot-pose-grid">
          {mascotScenes.map((s) => (
            <button
              key={s.id}
              aria-pressed={selected === s.id}
              onClick={() => {
                setSelected(s.id);
                setReplay((n) => n + 1);
              }}
            >
              <Mascot state={s.id} size={112} still showcase />
              <span lang="zh-CN" className="pose-zh">
                {s.say.zh}
              </span>
              <span>{s.name}</span>
            </button>
          ))}
        </div>
      </section>
    </main>
  );
}
