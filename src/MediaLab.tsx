import { useRef, useState } from "react";
import { ArrowCounterClockwise, Check, FilmStrip } from "@phosphor-icons/react";
import { AudioButton, Arrow, Recorder } from "./components";
import { db, saveAttempt } from "./db";
import type { Profile } from "./types";
import { segments } from "./dialogue-data";
import { dialogueMood } from "./sayo-voice";
import { ReadingRoute, WatchPlayer } from "./Watch";
/** Kept for callers of the old export; the parser lives in captions.ts. */
export { parseSrt } from "./captions";
export default function MediaLab({ profile }: { profile: Profile }) {
  const [pass, setPass] = useState(0),
    [support, setSupport] = useState(false),
    [supportUsed, setSupportUsed] = useState(false),
    [answer, setAnswer] = useState(""),
    [result, setResult] = useState<boolean | null>(null),
    [speed, setSpeed] = useState(1),
    [done, setDone] = useState(false),
    [heard, setHeard] = useState(false),
    [error, setError] = useState(""),
    [busy, setBusy] = useState(false);
  const start = useRef(Date.now());
  const choices =
    pass === 0
      ? ["Making a plan to meet", "Ordering lunch", "Asking for directions"]
      : ["Tomorrow at three", "Today at three", "Tomorrow at ten"];
  async function check() {
    if (busy) return;
    setBusy(true);
    try {
      const correct = answer === choices[0];
      await saveAttempt({
        phraseId: pass === 0 ? "letscoffee" : "three",
        modality: "media",
        correct,
        answer,
        expected: choices[0],
        latencyMs: Date.now() - start.current,
        support: supportUsed ? "transcript" : "none",
        context: `media:coffee:pass${pass}`,
      });
      setResult(correct);
    } catch {
      setError("Your answer could not be saved. Try again.");
    } finally {
      setBusy(false);
    }
  }
  async function complete() {
    setBusy(true);
    try {
      await db.sessions.add({
        id: crypto.randomUUID(),
        lessonId: "media:coffee",
        kind: "media",
        completedAt: Date.now(),
        attempts: 2,
        seconds: Math.round((Date.now() - start.current) / 1000),
      });
      setDone(true);
    } catch {
      setError("Your session could not be saved. Try again.");
    } finally {
      setBusy(false);
    }
  }
  function next() {
    setPass((p) => p + 1);
    setSupport(false);
    setSupportUsed(false);
    setAnswer("");
    setResult(null);
    setHeard(false);
  }
  return (
    <div>
      <div className="page-head">
        <p className="eyebrow"><span lang="zh-CN">看</span> Media</p>
        <h1>Watch, listen, sing. Then let the text go.</h1>
        <p>Your own shows and songs, with less help each time, and a practice scene to warm up.</p>
      </div>
      <ReadingRoute />
      <WatchPlayer profile={profile} />
      <h2 className="media-practice-title">A practice scene</h2>
      <div className="media-layout">
        <section>
          <div className="scene-player">
            <div className="scene-header">
              <FilmStrip size={20} />
              <span>An original audio scene</span>
              <span>Foundation</span>
            </div>
            <div className="scene-body">
              <span className="scene-hanzi" lang="zh-CN">
                聊一聊。
              </span>
              <h2>Before they leave.</h2>
              <p>Two acquaintances, at a neighborhood café.</p>
              <div className="scene-people">
                <span>林安</span>
                <span>陈宇</span>
              </div>
              <AudioButton
                text={segments.map((s) => s.text).join(" ")}
                voiceURI={profile.voiceURI}
                rate={speed}
                large
                onPlayed={() => setHeard(true)}
              />
            </div>
            <div className="scene-controls">
              <span>Sayo voices both parts · original script</span>
              <label>
                Speed{" "}
                <select
                  value={speed}
                  onChange={(e) => setSpeed(+e.target.value)}
                >
                  <option value={1}>1×</option>
                  <option value={0.85}>0.85×</option>
                  <option value={0.7}>0.7×</option>
                </select>
              </label>
            </div>
          </div>
          <p className="small">
            A controlled listening bridge. Native-speaker video and
            unfamiliar-speaker assessments require licensed, reviewed
            recordings.
          </p>
          <div className="media-transcript">
            <div className="section-heading">
              <h2>Inside the exchange</h2>
              <button
                className="text-button"
                onClick={() => {
                  setSupport(!support);
                  setSupportUsed(true);
                }}
              >
                {support ? "Hide transcript" : "Reveal transcript"}
              </button>
            </div>
            {support ? (
              segments.map((s, i) => (
                <div className="segment" key={s.text}>
                  <span className="segment-index">
                    {String(i + 1).padStart(2, "0")}
                  </span>
                  <div>
                    <span className="small">{s.speaker}</span>
                    <p lang="zh-CN">{s.text}</p>
                    {profile.pinyin && (
                      <span className="pinyin">{s.pinyin}</span>
                    )}
                    <p className="small">{s.meaning}</p>
                  </div>
                  <AudioButton
                    text={s.text}
                    mood={dialogueMood(segments.findIndex(line => line.speaker === s.speaker))}
                    voiceURI={profile.voiceURI}
                    rate={speed}
                  />
                </div>
              ))
            ) : (
              <p className="transcript-hidden">
                Give your ears a turn first. Reveal the transcript whenever you
                need support.
              </p>
            )}
          </div>
        </section>
        <aside className="media-task">
          {(error || done || result !== null || support) && <Mascot state={error ? "error" : done ? "celebrate" : result === false ? "encourage" : result === true ? "celebrate" : "hint"} size={96} />}
          <div className="pass-track">
            {["Catch the gist", "Listen closely", "Return without text"].map(
              (s, i) => (
                <div
                  key={s}
                  className={
                    i === pass ? "current" : i < pass ? "complete" : ""
                  }
                >
                  <span>{i < pass ? <Check size={16} /> : i + 1}</span>
                  {s}
                </div>
              ),
            )}
          </div>
          {done ? (
            <>
              <h2>You heard it again.</h2>
              <p>
                Your listening attempts are saved separately from supported
                practice. Revisit this scene to practice again.
              </p>
              <button
                className="button secondary"
                onClick={() => {
                  setPass(0);
                  setDone(false);
                  setAnswer("");
                  setResult(null);
                  setHeard(false);
                  setSupport(false);
                  setSupportUsed(false);
                }}
              >
                <ArrowCounterClockwise /> Try again
              </button>
            </>
          ) : pass < 2 ? (
            <>
              <h2>
                {pass === 0 ? "What’s happening?" : "When will they meet?"}
              </h2>
              <p>
                {pass === 0
                  ? "Listen for the overall situation. You don’t need every word."
                  : "Replay the scene. This time, listen for the day and time."}
              </p>
              <div className="choices compact">
                {choices.map((c) => (
                  <button
                    className={`choice ${answer === c ? "selected" : ""}`}
                    disabled={result !== null || busy || (!heard && !support)}
                    key={c}
                    onClick={() => setAnswer(c)}
                  >
                    {c}
                  </button>
                ))}
              </div>
              {result === null ? (
                <button
                  className="button"
                  disabled={!answer || busy}
                  onClick={() => void check()}
                >
                  Check understanding <Arrow />
                </button>
              ) : (
                <>
                  <p className="feedback-text" role="status">
                    {result
                      ? "That’s it."
                      : "Listen once more: " + choices[0] + "."}{" "}
                    {supportUsed
                      ? "Saved as supported practice."
                      : "Saved as an unaided attempt."}
                  </p>
                  <button className="button" onClick={next}>
                    Next pass <Arrow />
                  </button>
                </>
              )}
            </>
          ) : (
            <>
              <h2>Let the words disappear.</h2>
              <p>
                Listen once more with the transcript hidden. Then answer aloud:
                你明天有空吗？
              </p>
              {!profile.quiet && <Recorder />}
              <button
                className="button"
                disabled={busy || support || !heard}
                onClick={() => void complete()}
              >
                Finish this scene <Arrow />
              </button>
            </>
          )}
          {error && (
            <p role="alert" className="inline-error">
              {error}
            </p>
          )}
        </aside>
      </div>
    </div>
  );
}
import { Mascot } from "./Mascot";
