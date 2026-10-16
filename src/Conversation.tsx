import { useRef, useState } from "react";
import { sfx } from "./sfx";
import {
  ChatCircle,
  ArrowCounterClockwise,
  Check,
} from "@phosphor-icons/react";
import { AudioButton, Arrow, Recorder } from "./components";
import { db, saveAttempt } from "./db";
import { normalize } from "./learning";
import { packScenarios, packUnits } from "./content";
import type { Profile } from "./types";
import { baseScenarios } from "./dialogue-data";
import { useLiveQuery } from "dexie-react-hooks";
/** Built-in rehearsals first, then one role-play per content pack. */
const scenarios = [...baseScenarios, ...packScenarios];
// Role-plays sit under their unit's course level; the built-in ones are "Foundation".
const levelOfScenario = new Map<string, string>();
for (const u of packUnits)
  if (u.scenario) levelOfScenario.set(u.scenario.id, u.hskTarget ? String(u.hskTarget.level) : "foundation");
const scenarioLevel = (id: string) => levelOfScenario.get(id) ?? "foundation";
const scenarioLevels = ["foundation", "1", "2", "3", "4", "5", "6"].filter((l) =>
  scenarios.some((s) => scenarioLevel(s.id) === l),
);
const levelName = (l: string) => (l === "foundation" ? "Foundation" : `HSK ${l}`);
export default function Conversation({
  profile,
  initialScenario,
}: {
  profile: Profile;
  initialScenario?: string;
}) {
  const [scenarioId, setScenarioId] = useState(
    scenarios.some((s) => s.id === initialScenario) ? initialScenario! : "meet",
  ),
    [active, setActive] = useState(false),
    [turn, setTurn] = useState(0),
    [answer, setAnswer] = useState(""),
    [history, setHistory] = useState<{ text: string; who: "you" | "lin" }[]>(
      [],
    ),
    [help, setHelp] = useState(false),
    [supportUsed, setSupportUsed] = useState(false),
    [feedback, setFeedback] = useState(""),
    [done, setDone] = useState(false),
    [busy, setBusy] = useState(false),
    [error, setError] = useState(""),
    [level, setLevel] = useState<string | null>(null);
  const finished = new Set(
    (useLiveQuery(() => db.sessions.toArray()) ?? [])
      .filter((s) => s.kind === "conversation")
      .map((s) => s.lessonId),
  );
  const shownLevel = level ?? scenarioLevel(scenarioId);
  const start = useRef(Date.now()),
    turnStart = useRef(Date.now());
  const scenario = scenarios.find((s) => s.id === scenarioId)!,
    current = scenario.turns[turn];
  function reset(id = scenarioId) {
    setScenarioId(id);
    setActive(false);
    setTurn(0);
    setAnswer("");
    setHistory([]);
    setHelp(false);
    setSupportUsed(false);
    setFeedback("");
    setDone(false);
    setError("");
  }
  async function respond() {
    if (!answer.trim() || busy) return;
    setBusy(true);
    setError("");
    const valid = current.test(normalize(answer));
    if (valid) sfx.correct();
    try {
      await saveAttempt({
        phraseId: current.phrase,
        modality: "conversation",
        correct: valid,
        answer,
        expected: current.examples[0],
        latencyMs: Date.now() - turnStart.current,
        support: supportUsed ? "transcript" : "none",
        context: `scenario:${scenario.id}:${turn}`,
      });
      if (!valid) {
        setFeedback(
          `This rehearsal recognizes a few patterns. Try: ${current.examples[0]}. Other replies may be valid; this is not an AI language judgment.`,
        );
        setHelp(true);
        setSupportUsed(true);
        return;
      }
      setHistory((h) => [
        ...h,
        { text: current.text, who: "lin" },
        { text: answer, who: "you" },
      ]);
      setAnswer("");
      setFeedback("");
      setHelp(false);
      setSupportUsed(false);
      if (turn === scenario.turns.length - 1) {
        await db.sessions.add({
          id: crypto.randomUUID(),
          lessonId: `conversation:${scenario.id}`,
          completedAt: Date.now(),
          attempts: scenario.turns.length,
          seconds: Math.round((Date.now() - start.current) / 1000),
          kind: "conversation",
        });
        setDone(true);
      } else {
        setTurn((t) => t + 1);
        turnStart.current = Date.now();
      }
    } catch {
      setError("Your reply could not be saved. Please try again.");
    } finally {
      setBusy(false);
    }
  }
  return (
    <div className="conversation-page">
      <div className="page-head">
        <p className="eyebrow"><span lang="zh-CN">说</span> Speak</p>
        <h1>Find a moment to use the words.</h1>
        <p>Guided role-plays. Hear the line, then answer in Chinese.</p>
      </div>
      <div className="conversation-grid">
        <aside className="scenario-panel">
          <MoSays state="speak" size={110} side="top" />
          <ChatCircle size={34} weight="light" />
          <h2>Your next conversation</h2>
          <div className="level-strip" role="group" aria-label="Course level">
            {scenarioLevels.map((l) => (
              <button key={l} aria-pressed={shownLevel === l} onClick={() => setLevel(l)}>
                {levelName(l)}
              </button>
            ))}
          </div>
          <div className="scenario-options" aria-label={`${levelName(shownLevel)} role-plays`}>
            {scenarios
              .filter((s) => scenarioLevel(s.id) === shownLevel)
              .map((s) => (
                <button
                  disabled={busy}
                  key={s.id}
                  aria-pressed={scenarioId === s.id}
                  className={finished.has(`conversation:${s.id}`) ? "is-done" : ""}
                  onClick={() => reset(s.id)}
                >
                  <strong>{s.title}</strong>
                  <span>{s.place}</span>
                  {finished.has(`conversation:${s.id}`) && (
                    <Check size={14} weight="bold" className="scenario-done" aria-label="Finished" />
                  )}
                </button>
              ))}
          </div>
          <p>{scenario.context}</p>
          <div className="mission-note">
            <span>Your intention</span>
            <p>{scenario.goal}</p>
          </div>
          <p className="small">
            Guided rehearsal · original script
            <br />
            Responses checked against limited patterns. Open-ended AI
            conversation is not connected.
          </p>
        </aside>
        <section className="conversation-space">
          {!active ? (
            <div className="conversation-welcome">
              <div className="person-monogram" lang="zh-CN">
                {Array.from(scenario.partner).slice(-1)[0]}
              </div>
              <h2>
                {scenario.partner === "林安" ? "Meet Lin An." : <span lang="zh-CN">{scenario.partner}</span>}
              </h2>
              <p>{scenario.place}</p>
              <button
                className="button"
                onClick={() => {
                  setActive(true);
                  start.current = Date.now();
                  turnStart.current = Date.now();
                }}
              >
                Begin conversation <Arrow />
              </button>
            </div>
          ) : done ? (
            <div className="conversation-welcome">
              <Check size={40} />
              <h2>You kept it going.</h2>
              <MoSays autoSpeak state="celebrate" size={140} side="top" />
              <p>
                You completed {scenario.turns.length} guided turns. Try the same
                intentions with someone new to test real-world transfer.
              </p>
              <details>
                <summary>Read your conversation</summary>
                {history.map((h, i) => (
                  <p key={i}>
                    <strong>{h.who === "you" ? "You" : scenario.partner}:</strong>{" "}
                    <span lang="zh-CN">{h.text}</span>
                  </p>
                ))}
              </details>
              <button className="button secondary" onClick={() => reset()}>
                <ArrowCounterClockwise /> Rehearse again
              </button>
            </div>
          ) : (
            <>
              <div className="conversation-top">
                <span className="avatar" lang="zh-CN">
                  {Array.from(scenario.partner).slice(-1)[0]}
                </span>
                <div>
                  <strong lang="zh-CN">{scenario.partner}</strong>
                  <span>{scenario.place}</span>
                </div>
                <span className="turn-count">
                  {turn + 1} / {scenario.turns.length}
                </span>
              </div>
              <div className="chat-history">
                {history.slice(-4).map((h, i) => (
                  <div key={i} className={`bubble ${h.who}`} lang="zh-CN">
                    {h.text}
                  </div>
                ))}
              </div>
              <div className="current-turn">
                <AudioButton
                  text={current.text}
                  mood="playful"
                  voiceURI={profile.voiceURI}
                  large
                />
                <button
                  className="text-button"
                  onClick={() => {
                    setHelp(!help);
                    setSupportUsed(true);
                  }}
                >
                  {help ? "Hide support" : "Show transcript & help"}
                </button>
                {help && (
                  <>
                    <p className="chinese" lang="zh-CN">
                      {current.text}
                    </p>
                    <p className="pinyin">{current.pinyin}</p>
                    <p>{current.meaning}</p>
                  </>
                )}
              </div>
              <div className="reply-area">
                <label htmlFor="reply">{current.intent}</label>
                {!profile.quiet && (
                  <details>
                    <summary>Practice your reply aloud</summary>
                    <Recorder />
                  </details>
                )}
                <form
                  onSubmit={(e) => {
                    e.preventDefault();
                    void respond();
                  }}
                >
                  <input
                    id="reply"
                    disabled={busy}
                    lang="zh-CN"
                    value={answer}
                    maxLength={200}
                    onChange={(e) => setAnswer(e.target.value)}
                    placeholder="用中文回复…"
                    autoComplete="off"
                  />
                  <button className="button" disabled={!answer.trim() || busy}>
                    {busy ? "Saving…" : "Reply"} <Arrow />
                  </button>
                </form>
                {help && (
                  <div className="suggestions">
                    {current.examples.map((v) => (
                      <button key={v} onClick={() => setAnswer(v)} lang="zh-CN">
                        {v}
                      </button>
                    ))}
                  </div>
                )}
                {feedback && (
                  <p className="feedback-text" role="status">
                    {feedback}
                  </p>
                )}
                {error && (
                  <p className="inline-error" role="alert">
                    {error}
                  </p>
                )}
                <p className="small">
                  Type after speaking, or use text alone. This rehearsal does
                  not score your voice.
                </p>
              </div>
            </>
          )}
        </section>
      </div>
    </div>
  );
}
import { MoSays } from "./Mascot";
