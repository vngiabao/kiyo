import { useState } from "react";
import {
  Headphones,
  Microphone,
  BookOpen,
  Waveform,
  ArrowLeft,
  Check,
} from "@phosphor-icons/react";
import { useLiveQuery } from "dexie-react-hooks";
import { db } from "./db";
import { phraseById, lessons, reviewTaskFor } from "./content";
import { ExerciseView } from "./LessonPlayer";
import { AudioButton, Arrow, ToneCurve, Recorder } from "./components";
import type { Profile, Exercise, Memory } from "./types";
import { MoSays } from "./Mascot";
export function Review({
  profile,
  onLearn,
}: {
  profile: Profile;
  onLearn: () => void;
}) {
  const [queue, setQueue] = useState<Memory[] | null>(null),
    [position, setPosition] = useState(0);
  const memories = useLiveQuery(() => db.memories.toArray()) ?? [];
  const mistakes = useLiveQuery(() => db.mistakes.toArray()) ?? [];
  const due = memories.filter(
    (m) =>
      m.due <= Date.now() &&
      !["conversation", "speaking", "recall", "media"].includes(m.modality),
  );
  if (queue && position < queue.length) {
    const m = queue[position],
      p = phraseById[m.phraseId];
    const alternatives = Object.values(phraseById)
      .filter((v) => v.id !== p.id && v.topic === p.topic)
      .slice(0, 2);
    if (alternatives.length < 2)
      alternatives.push(phraseById.good, phraseById.bye);
    const choices = [
      ...new Set([...alternatives.map((v) => v.meaning), p.meaning]),
    ];
    // Bring back a real task (the one you missed, or a fresh sentence with the same phrase).
    const task = reviewTaskFor(m, mistakes.find((x) => x.id === m.id)?.context);
    const e: Exercise = task ? { ...task, id: `review:${task.id}:${m.due}` } : {
      id: `review:${m.id}:${m.due}`,
      kind: ["listening", "media", "tone"].includes(m.modality)
        ? "choice"
        : m.modality === "typing"
          ? "dictation"
          : "read",
      phraseId: p.id,
      prompt:
        m.modality === "typing"
          ? "Type what you hear."
          : ["listening", "media", "tone"].includes(m.modality)
            ? "What do you hear?"
            : "What does this mean?",
      modality: m.modality,
      choices,
      correct: m.modality === "typing" ? p.hanzi : p.meaning,
    };
    return (
      <div>
        <div className="section-heading">
          <button className="text-button" onClick={() => setQueue(null)}>
            <ArrowLeft /> Back to review
          </button>
          <span>
            {position + 1} / {queue.length}
          </span>
        </div>
        <ExerciseView
          key={e.id}
          exercise={e}
          profile={profile}
          onNext={() => setPosition((n) => n + 1)}
        />
      </div>
    );
  }
  if (queue)
    return (
      <div className="empty-state">
        <Check size={40} />
        <h1>You brought it back.</h1>
        <MoSays autoSpeak state="celebrate" size={150} side="top" />
        <p>
          {queue.length} memories revisited. Your next review dates follow your
          answers.
        </p>
        <button
          className="button"
          onClick={() => {
            setQueue(null);
            setPosition(0);
          }}
        >
          Back to review <Arrow />
        </button>
      </div>
    );
  return (
    <>
      <div className="page-head">
        <p className="eyebrow"><span lang="zh-CN">复习</span> Review</p>
        <h1>Bring it back.</h1>
        <p>Remember the sound. Retrieve the meaning. Give it time to stay.</p>
      </div>
      <section className="review-summary">
        <MoSays state={due.length ? "review" : "rest"} size={120} side="left" />
        <span className="review-number">{due.length}</span>
        <div>
          <h2>
            {due.length
              ? "memories ready today"
              : "A little space helps memory."}
          </h2>
          <p>
            {due.length
              ? "Each listening, reading, and typing memory has its own schedule."
              : "New phrases join your review after an unaided exercise. Come back when they’re due."}
          </p>
          <button
            className="button"
            onClick={() =>
              due.length
                ? (setQueue(due.slice(0, 20)), setPosition(0))
                : onLearn()
            }
          >
            {due.length ? "Begin review" : "Continue learning"} <Arrow />
          </button>
        </div>
      </section>
      {memories.length > 0 && (
        <section className="upcoming">
          <h2>Coming back into view</h2>
          {memories
            .slice()
            .sort((a, b) => a.due - b.due)
            .slice(0, 8)
            .map((m) => (
              <div className="review-row" key={m.id}>
                <span lang="zh-CN">{phraseById[m.phraseId].hanzi}</span>
                <span>{m.modality}</span>
                <span>
                  {m.due <= Date.now()
                    ? "Ready now"
                    : new Date(m.due).toLocaleDateString(undefined, {
                        month: "short",
                        day: "numeric",
                      })}
                </span>
              </div>
            ))}
        </section>
      )}
    </>
  );
}
export default function Practice({
  profile,
  onLesson,
  onReview,
}: {
  profile: Profile;
  onLesson: (id: string, mode: "lesson" | "listening" | "assessment") => void;
  onReview: () => void;
}) {
  const [tab, setTab] = useState("listening"),
    [tone, setTone] = useState(1),
    [unit, setUnit] = useState("first");
  const tabs = [
    { id: "listening", label: "Listening", icon: Headphones },
    { id: "pronunciation", label: "Pronunciation", icon: Waveform },
    { id: "speaking", label: "Speaking", icon: Microphone },
    { id: "reading", label: "Words & structure", icon: BookOpen },
  ];
  return (
    <>
      <div className="page-head">
        <p className="eyebrow"><span lang="zh-CN">练</span> Practice</p>
        <h1>A little more deliberate.</h1>
        <p>Give one part of your Mandarin some undivided attention.</p>
      </div>
      <div className="practice-tabs" role="tablist" aria-label="Practice area">
        {tabs.map((t) => (
          <button
            role="tab"
            aria-selected={tab === t.id}
            key={t.id}
            onClick={() => setTab(t.id)}
          >
            <t.icon size={20} />
            {t.label}
          </button>
        ))}
      </div>
      {tab === "pronunciation" ? (
        <div className="pronunciation-layout">
          <div>
            <h2>Follow the pitch.</h2>
            <p>The syllable stays the same. Its tone changes the word.</p>
            <div className="tone-selector">
              {[1, 2, 3, 4].map((n) => (
                <button
                  aria-pressed={n === tone}
                  onClick={() => setTone(n)}
                  key={n}
                >
                  Tone {n}
                </button>
              ))}
            </div>
            <ToneCurve tone={tone} />
            <div className="tone-word">
              <span lang="zh-CN">{["妈", "麻", "马", "骂"][tone - 1]}</span>
              <span>{["mā", "má", "mǎ", "mà"][tone - 1]}</span>
              <AudioButton
                text={["妈", "麻", "马", "骂"][tone - 1]}
                mood="clear"
                voiceURI={profile.voiceURI}
              />
            </div>
          </div>
          <aside className="teaching-note">
            <h2>
              {
                [
                  "High and level",
                  "Rise from the middle",
                  "Keep it low",
                  "A clear fall",
                ][tone - 1]
              }
            </h2>
            <p>
              {
                [
                  "Hold a comfortable high pitch. It should stay level, rather than drift down.",
                  "Begin in the middle of your range and rise. Listen before trying to imitate.",
                  "A full dip is a useful isolated model. In everyday connected speech, this tone is usually low and may not rise.",
                  "Start high and move down decisively. Keep the syllable controlled; louder is not necessarily better.",
                ][tone - 1]
              }
            </p>
            <p className="small">
              Schematic contours only. No voice analysis is performed.
            </p>
            {!profile.quiet && <Recorder />}
            <button
              className="button"
              onClick={() => onLesson("tones", "listening")}
            >
              Try tone listening <Arrow />
            </button>
          </aside>
        </div>
      ) : (
        <div className="practice-intro">
          <div>
            <h2>
              {tab === "listening"
                ? "Let your ears lead."
                : tab === "speaking"
                  ? "Move from recognition to response."
                  : "Find the patterns in useful words."}
            </h2>
            <p>
              {tab === "listening"
                ? "Audio first, with no transcript on screen. Listen for meaning before reaching for support."
                : tab === "speaking"
                  ? "Choose a lesson, listen to a model, and record a response. A quiet alternative is always available."
                  : "Use sentence assembly and character recognition in a real lesson. Pinyin remains a support you can reveal."}
            </p>
            <label className="field">
              Choose your context
              <select value={unit} onChange={(e) => setUnit(e.target.value)}>
                {lessons.map((l) => (
                  <option value={l.id} key={l.id}>
                    {l.title}
                  </option>
                ))}
              </select>
            </label>
            <button
              className="button"
              onClick={() =>
                onLesson(unit, tab === "listening" ? "listening" : "lesson")
              }
            >
              Start practice <Arrow />
            </button>
          </div>
          <aside>
            <div className="practice-type" lang="zh-CN">
              {tab === "listening" ? "听" : tab === "speaking" ? "说" : "读"}
            </div>
            <p>Attention is a kind of progress.</p>
          </aside>
        </div>
      )}
      <section className="review-invitation">
        <div>
          <h2>The things you almost remembered.</h2>
          <p>Your review queue follows your own attempts.</p>
        </div>
        <button className="text-button" onClick={onReview}>
          Open review <Arrow />
        </button>
      </section>
    </>
  );
}
