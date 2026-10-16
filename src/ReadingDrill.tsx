import { useEffect, useMemo, useRef, useState } from "react";
import { sfx } from "./sfx";
import { Lightning } from "@phosphor-icons/react";
import { useLiveQuery } from "dexie-react-hooks";
import { db } from "./db";
import { Arrow } from "./components";
import {
  SUBTITLE_RATE,
  START_RATE,
  drillMaterial,
  hanLength,
  meaningChoices,
  nextRate,
  showFor,
  type DrillLine,
} from "./drill";

const LINES = 12;
type Stage = { kind: "idle" } | { kind: "show"; i: number } | { kind: "ask"; i: number } | { kind: "told"; i: number; correct: boolean; from: number } | { kind: "done" };

/** Practice → Reading speed: lines you know, flashed at subtitle pace. */
export function ReadingDrill() {
  const sessions = useLiveQuery(() => db.sessions.toArray()) ?? [];
  const history = useLiveQuery(() => db.readingSpeed.orderBy("at").toArray()) ?? [];
  const done = useMemo(() => new Set(sessions.map((s) => s.lessonId)), [sessions]);
  const pool = useMemo(() => drillMaterial(done), [done]);
  const last = history[history.length - 1];
  const [stage, setStage] = useState<Stage>({ kind: "idle" }),
    [lines, setLines] = useState<DrillLine[]>([]),
    [rate, setRate] = useState(START_RATE),
    [streak, setStreak] = useState(0),
    [correct, setCorrect] = useState(0),
    [pick, setPick] = useState(""),
    [startRate, setStartRate] = useState(START_RATE);
  const seed = useRef(1);

  function start() {
    const r = last?.endRate ?? START_RATE;
    seed.current = Math.floor(Math.random() * 1000) + 1;
    const shuffled = [...pool].sort((a, b) => ((hash(a.zh) ^ seed.current) % 997) - ((hash(b.zh) ^ seed.current) % 997));
    setLines(shuffled.slice(0, Math.min(LINES, shuffled.length)));
    setRate(r);
    setStartRate(r);
    setStreak(0);
    setCorrect(0);
    setStage({ kind: "show", i: 0 });
  }
  // A line stays up exactly as long as it would at the current rate, then disappears.
  useEffect(() => {
    if (stage.kind !== "show") return;
    setPick("");
    const t = setTimeout(() => setStage({ kind: "ask", i: stage.i }), showFor(lines[stage.i].zh, rate) * 1000);
    return () => clearTimeout(t);
  }, [stage, lines, rate]);

  const line = stage.kind === "show" || stage.kind === "ask" || stage.kind === "told" ? lines[stage.i] : undefined;
  const choices = useMemo(() => (line ? meaningChoices(line, pool, seed.current + (stage.kind === "done" || stage.kind === "idle" ? 0 : stage.i)) : []), [line, pool, stage]);

  function answer(choice: string) {
    if (stage.kind !== "ask" || !line) return;
    setPick(choice);
    const ok = choice === line.en;
    if (ok) sfx.correct();
    else sfx.wrong();
    const next = nextRate(rate, streak, ok);
    if (ok) setCorrect((n) => n + 1);
    setStage({ kind: "told", i: stage.i, correct: ok, from: rate });
    setRate(next.rate);
    setStreak(next.streak);
  }
  async function advance() {
    if (stage.kind !== "told") return;
    if (stage.i + 1 < lines.length) setStage({ kind: "show", i: stage.i + 1 });
    else {
      await db.readingSpeed.add({ id: crypto.randomUUID(), at: Date.now(), startRate, endRate: rate, lines: lines.length, correct: correct });
      setStage({ kind: "done" });
    }
  }
  // Keyboard: 1–3 answer, Enter continues.
  useEffect(() => {
    const onKey = (e: KeyboardEvent) => {
      if (stage.kind === "ask" && /^[1-3]$/.test(e.key)) answer(choices[+e.key - 1]);
      else if (stage.kind === "told" && e.key === "Enter") void advance();
    };
    window.addEventListener("keydown", onKey);
    return () => window.removeEventListener("keydown", onKey);
  });

  if (pool.length < 8)
    return (
      <section className="drill">
        <h2>Read at subtitle speed</h2>
        <p className="muted">
          The drill only uses lines you've studied, so it unlocks after a few lessons ({pool.length} of 8 lines so far). Finish a couple more and come back.
        </p>
      </section>
    );

  return (
    <section className="drill" aria-labelledby="drill-title">
      <div className="drill-head">
        <div>
          <h2 id="drill-title">Read at subtitle speed</h2>
          <p>
            A line you've learned appears for as long as a subtitle would at your pace, then disappears. Pick what it meant. Two right in a row and
            lines get faster; a miss slows them down.
          </p>
        </div>
        <dl className="drill-rates">
          <div>
            <dt>Your pace</dt>
            <dd className="tabular">{(stage.kind === "idle" ? last?.endRate ?? START_RATE : rate).toFixed(1)} /s</dd>
          </div>
          <div>
            <dt>Adult subtitles</dt>
            <dd className="tabular">{SUBTITLE_RATE.adult} /s</dd>
          </div>
        </dl>
      </div>

      {stage.kind === "idle" && (
        <div className="drill-start">
          <button className="button" onClick={start}>
            <Lightning size={18} /> Start · {Math.min(LINES, pool.length)} lines
          </button>
          <p className="small muted">Characters per second. Netflix's Chinese subtitles go up to {SUBTITLE_RATE.adult}/s for adults and {SUBTITLE_RATE.children}/s for children's shows.</p>
        </div>
      )}

      {line && (
        <div className="drill-screen" aria-live="polite">
          {stage.kind === "show" ? (
            <>
              <p className="drill-line" lang="zh-CN">
                {line.zh}
              </p>
              <span className="drill-timer" style={{ animationDuration: `${showFor(line.zh, rate)}s` }} aria-hidden />
            </>
          ) : stage.kind === "told" ? (
            <p className="drill-line revealed" lang="zh-CN">
              {line.zh}
            </p>
          ) : (
            <p className="drill-line gone">What did it say?</p>
          )}
          <span className="drill-count small tabular">
            {stage.kind === "done" || stage.kind === "idle" ? "" : `${stage.i + 1} / ${lines.length} · ${hanLength(line.zh)} characters`}
          </span>
        </div>
      )}

      {(stage.kind === "ask" || stage.kind === "told") && (
        <div className="choices drill-choices" role="radiogroup" aria-label="What did it mean?">
          {choices.map((c, k) => {
            const state = stage.kind === "told" ? (c === line!.en ? "correct" : c === pick ? "incorrect" : "dim") : "";
            return (
              <button key={c} role="radio" aria-checked={pick === c} disabled={stage.kind === "told"} className={`choice ${state}`} onClick={() => answer(c)}>
                <span className="choice-key" aria-hidden>
                  {k + 1}
                </span>
                <span className="choice-text">{c}</span>
              </button>
            );
          })}
        </div>
      )}

      {stage.kind === "told" && (
        <div className="drill-feedback" role="status">
          <span>
            {stage.correct ? "Right." : "Not quite."}{" "}
            {rate > stage.from ? `Faster now: ${rate.toFixed(1)}/s.` : rate < stage.from ? `Slower now: ${rate.toFixed(1)}/s.` : stage.correct ? "One more right and it speeds up." : ""}
          </span>
          <button className="button" onClick={() => void advance()}>
            {stage.i + 1 < lines.length ? "Next line" : "Finish"} <Arrow />
          </button>
        </div>
      )}

      {stage.kind === "done" && (
        <div className="drill-summary" role="status">
          <h3>
            {startRate.toFixed(1)} → {rate.toFixed(1)} characters per second
          </h3>
          <p>
            {correct} of {lines.length} meanings right, read once with no help. Your next session starts at {rate.toFixed(1)}/s.
          </p>
          <button className="button secondary" onClick={() => setStage({ kind: "idle" })}>
            Done
          </button>
        </div>
      )}

      {history.length > 1 && <PaceChart rates={history.slice(-20).map((h) => h.endRate)} />}
    </section>
  );
}

const hash = (s: string) => Array.from(s).reduce((h, c) => (h * 31 + c.charCodeAt(0)) >>> 0, 7);

/** Pace at the end of each session, with the two subtitle reference lines. */
function PaceChart({ rates }: { rates: number[] }) {
  const W = 560,
    H = 140,
    pad = 28;
  const top = Math.max(10, ...rates);
  const x = (i: number) => pad + (i * (W - pad * 2)) / Math.max(1, rates.length - 1);
  const y = (r: number) => H - pad - (r / top) * (H - pad * 1.5);
  return (
    <figure className="pace-chart">
      <figcaption>Your pace after each session (characters per second)</figcaption>
      <svg viewBox={`0 0 ${W} ${H}`} role="img" aria-label={`Pace over the last ${rates.length} sessions: from ${rates[0].toFixed(1)} to ${rates[rates.length - 1].toFixed(1)} characters per second`}>
        {[SUBTITLE_RATE.children, SUBTITLE_RATE.adult].map((r) => (
          <g key={r}>
            <line x1={pad} x2={W - pad} y1={y(r)} y2={y(r)} className="pc-ref" />
            <text x={W - pad} y={y(r) - 4} textAnchor="end" className="pc-label">
              {r === SUBTITLE_RATE.adult ? "adult subtitles 9/s" : "children's 7/s"}
            </text>
          </g>
        ))}
        <polyline points={rates.map((r, i) => `${x(i)},${y(r)}`).join(" ")} className="pc-line" />
        {rates.map((r, i) => (
          <circle key={i} cx={x(i)} cy={y(r)} r={3} className="pc-dot" />
        ))}
        <text x={x(rates.length - 1)} y={y(rates[rates.length - 1]) - 8} textAnchor="end" className="pc-value">
          {rates[rates.length - 1].toFixed(1)}/s
        </text>
      </svg>
    </figure>
  );
}
