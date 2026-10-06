import { useEffect, useState } from "react";
import { useLiveQuery } from "dexie-react-hooks";
import { ArrowLeft, Check, Clock, Flag } from "@phosphor-icons/react";
import { AudioButton, Pinyin } from "./components";
import { MoSays } from "./Mascot";
import { finishHskRun, hskDB, saveHskAnswer, markHskItemSeen } from "./hsk-db";
import {
  gradeRun,
  hskItemById,
  teacherLines,
  type HskRun,
  type HskAnswer,
} from "./hsk-model";

export default function HskExam({
  id,
  onExit,
}: {
  id: string;
  onExit: () => void;
}) {
  const run = useLiveQuery(() => hskDB.runs.get(id), [id]);
  const [index, setIndex] = useState(0),
    [now, setNow] = useState(Date.now()),
    [busy, setBusy] = useState(false),
    [error, setError] = useState("");
  const [optimistic, setOptimistic] = useState<Record<string, HskAnswer>>({});
  const visibleItem = run?.itemIds[index];
  useEffect(() => {
    if (visibleItem && run && !run.finishedAt)
      void markHskItemSeen(id, visibleItem).catch(() =>
        setError("Your question history could not be saved. Reload before continuing."));
  }, [id, visibleItem, run?.finishedAt]);
  useEffect(() => {
    const t = setInterval(() => setNow(Date.now()), 500);
    return () => clearInterval(t);
  }, []);
  const act = async (fn: () => Promise<unknown>) => {
    setBusy(true);
    setError("");
    try {
      await fn();
    } catch {
      setError("Your answer could not be saved. Try again before leaving.");
    } finally {
      setBusy(false);
    }
  };
  useEffect(() => {
    if (
      run &&
      !run.finishedAt &&
      run.deadline !== null &&
      now >= run.deadline &&
      !busy &&
      !error
    )
      void act(() => finishHskRun(id));
  }, [now, run, id, busy, error]);
  if (!run) return <p role="status">Opening your saved practice…</p>;
  if (run.finishedAt) return <Results run={run} onExit={onExit} />;
  const q = hskItemById[run.itemIds[index]],
    answer = optimistic[q.id] ?? run.answers[q.id];
  const choose = (value: string, supported: boolean) => {
    setOptimistic((old) => ({
      ...old,
      [q.id]: { value, supported: supported || !!answer?.supported },
    }));
    void act(async () => {
      try {
        await saveHskAnswer(id, q.id, value, supported);
      } catch (error) {
        setOptimistic((old) => {
          const copy = { ...old };
          delete copy[q.id];
          return copy;
        });
        throw error;
      }
    });
  };
  const expired = run.deadline !== null && now >= run.deadline;
  const seconds =
    run.deadline === null
      ? null
      : Math.max(0, Math.ceil((run.deadline - now) / 1000));
  // Stable rotation avoids teaching a fixed answer position across attempts.
  const offset = (q.id.charCodeAt(q.id.length - 1) + run.id.charCodeAt(0)) % 4;
  const choices = [...q.choices.slice(offset), ...q.choices.slice(0, offset)];
  const answered = Object.values(run.answers).filter((a) => a.value).length;
  return (
    <section className="hsk-exam" aria-label="HSK practice">
      <div className="hsk-exam-bar">
        <button className="text-button" disabled={busy} onClick={onExit}>
          <ArrowLeft /> Save & leave
        </button>
        <span>
          {run.unit === "sample"
            ? "Timed practice sample"
            : run.unit === "repair"
              ? "Mistake repair"
              : `Level ${run.level ?? 1} checkpoint`}
        </span>
        <span
          className="hsk-clock"
          aria-label={
            seconds === null
              ? "Untimed"
              : `${Math.floor(seconds / 60)} minutes ${seconds % 60} seconds remaining`
          }
        >
          <Clock />
          {seconds === null
            ? "Untimed"
            : `${Math.floor(seconds / 60)}:${String(seconds % 60).padStart(2, "0")}`}
        </span>
      </div>
      <p className="muted">
        {answered} of {run.itemIds.length} answered
        {busy ? " · Saving…" : " · Saved on this device"}
        {seconds !== null && " · The timer continues if you leave."}
      </p>
      <nav className="hsk-question-nav" aria-label="Questions">
        {run.itemIds.map((qid, i) => (
          <button
            key={qid}
            aria-label={`Question ${i + 1}${run.answers[qid]?.value ? ", answered" : ""}`}
            aria-current={i === index ? "step" : undefined}
            className={run.answers[qid]?.value ? "answered" : ""}
            onClick={() => setIndex(i)}
          >
            {i + 1}
          </button>
        ))}
      </nav>
      <h1>{q.format === "listening" ? "Listen, then choose." : q.format === "reading" ? "Read, then choose." : q.format === "ordering" ? "Choose the ordinary word order." : "Choose the missing word."}</h1>
      {q.format === "listening" && <>
        <AudioButton key={q.id} text={q.sentence} mood="clear" label="Play question" />
        {answer?.supported && <p className="hsk-question" lang="zh-CN">{q.sentence}</p>}
      </>}
      {q.format === "reading" && <p className="hsk-question" lang="zh-CN">{q.sentence}</p>}
      {q.format === "ordering" && <>
        <p className="muted">Use the ordinary order taught in the course to answer the question. Other marked or poetic orders are outside this exercise.</p>
        <p className="hsk-question" lang="zh-CN">{[...(q.segments ?? [])].reverse().map((c) => c.zh).join(" / ")}</p>
      </>}
      <p className="hsk-question" lang="zh-CN">{q.prompt.replace("___", "（　）")}</p>
      {answer?.supported && q.promptPy && <Pinyin text={q.promptPy} />}
      <fieldset className="hsk-choices" disabled={busy || expired}>
        <legend className="sr-only">Answer for question {index + 1}</legend>
        {choices.map((c, i) => (
          <label
            key={c.zh}
            className={answer?.value === c.zh ? "selected" : ""}
          >
            <input
              type="radio"
              name={q.id}
              value={c.zh}
              checked={answer?.value === c.zh}
              onChange={() => choose(c.zh, !!answer?.supported)}
            />
            <span className="hsk-choice-letter">
              {String.fromCharCode(65 + i)}
            </span>
            <span lang="zh-CN">{c.zh}</span>
            {answer?.supported && <Pinyin text={c.py} />}
          </label>
        ))}
      </fieldset>
      {run.unit !== "sample" && (
        <button
          className="text-button"
          disabled={busy || expired || answer?.supported}
          onClick={() => choose(answer?.value ?? "", true)}
        >
          {answer?.supported
            ? "Pinyin used · this attempt is supported"
            : q.format === "listening" ? "Show words and pinyin · marks this attempt as supported" : "Show option pinyin · marks this attempt as supported"}
        </button>
      )}
      {error && <p role="alert">{error}</p>}
      <div className="hsk-exam-actions">
        <button
          className="button secondary"
          disabled={index === 0 || busy}
          onClick={() => setIndex((i) => i - 1)}
        >
          Previous
        </button>
        {index < run.itemIds.length - 1 ? (
          <button
            className="button"
            disabled={busy}
            onClick={() => setIndex((i) => i + 1)}
          >
            Next question
          </button>
        ) : (
          <button
            className="button"
            disabled={busy}
            onClick={() => void act(() => finishHskRun(id))}
          >
            {busy
              ? "Saving…"
              : answered === run.itemIds.length
                ? "Submit answers"
                : `Submit · ${run.itemIds.length - answered} unanswered`}
          </button>
        )}
      </div>
      <p className="muted">
        Original Kiyo practice. Raw results only; this is not a full HSK
        paper or an official score.
      </p>
    </section>
  );
}

function Results({ run, onExit }: { run: HskRun; onExit: () => void }) {
  const result = gradeRun(run);
  return (
    <section className="hsk-results">
      <button className="text-button" onClick={onExit}>
        <ArrowLeft /> Back to HSK
      </button>
      <div className="hsk-result-head">
        <div>
          <h1>
            {result.passed
              ? "Checkpoint cleared."
              : "Keep the mistakes. Fix them."}
          </h1>
          <p className="hsk-result-score">
            {result.correct}
            <span> / {result.total} correct</span>
          </p>
          <p>
            {result.unaided} unaided · {result.supported} supported ·{" "}
            {run.itemIds.length -
              Object.values(run.answers).filter((a) => a.value).length}{" "}
            unanswered
          </p>
          <p className="muted">
            Kiyo’s progression rule: at least 80% correct, with no pinyin help.
            This result does not predict an HSK score.
          </p>
        </div>
        <MoSays
          state="teacher"
          say={result.passed ? teacherLines.pass : teacherLines.retry}
          autoSpeak
          size={180}
        />
      </div>
      <h2>Every answer, explained.</h2>
      <div className="hsk-answer-review">
        {run.itemIds.map((id, i) => {
          const q = hskItemById[id],
            a = run.answers[id],
            correct = a?.value === q.answer;
          return (
            <article key={id}>
              <p className={correct ? "hsk-good" : "hsk-repair"}>
                {correct ? <Check /> : <Flag />} Question {i + 1} ·{" "}
                {correct ? "Correct" : "Review"}
                {a?.supported && " · with help"}
              </p>
              <p className="hsk-review-sentence" lang="zh-CN">
                {q.sentence}
              </p>
              <Pinyin text={q.py} />
              <p>{q.en}</p>
              <p>
                Your answer:{" "}
                <span lang="zh-CN">{a?.value || "Unanswered"}</span> · Expected:{" "}
                <strong lang="zh-CN">{q.answer}</strong>
              </p>
              <p className="muted">{q.explanation}</p>
              <AudioButton
                text={q.sentence}
                mood="clear"
                label="Hear the corrected sentence"
              />
            </article>
          );
        })}
      </div>
      <button className="button" onClick={onExit}>
        Return to the pathway
      </button>
    </section>
  );
}
