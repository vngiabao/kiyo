import { useEffect, useMemo, useRef, useState } from "react";
import { ArrowLeft, Check, Eye, X } from "@phosphor-icons/react";
import { lessonById, lessons, exercisesFor, phraseById, charByHanzi, grammarById } from "./content";
import type { CompiledGrammar } from "./packs";
import { db, saveAttempt } from "./db";
import {
  AudioButton,
  Arrow,
  PhraseText,
  Pinyin,
  Recorder,
  ToneCurve,
  Speakable,
} from "./components";
import { CharacterAnatomy, HanziStage } from "./Characters";
import type { Exercise, Profile } from "./types";
import { normalize } from "./learning";
import { Mascot, MoSays, moLines, pickLine, type MascotState, type MoLine } from "./Mascot";
import { levelOf, streakOf } from "./progression";
import { TaskView, type TaskAnswer } from "./TaskView";

const quizKinds = ["choice", "glyph", "pick", "count", "dialogue", "truefalse", "reply", "listenfill"];
const listeningTasks = ["dialogue", "truefalse", "reply", "listenfill"];
export default function LessonPlayer({
  lessonId,
  profile,
  onExit,
  mode = "lesson",
}: {
  lessonId: string;
  profile: Profile;
  onExit: () => void;
  mode?: "lesson" | "listening" | "assessment";
}) {
  const lesson = lessonById[lessonId] ?? lessons[0];
  const steps = useMemo(
    () =>
      mode === "lesson"
        ? exercisesFor(lesson)
        : exercisesFor(lesson).filter((e) => quizKinds.includes(e.kind)),
    [lesson, mode],
  );
  const [step, setStep] = useState(0),
    [ready, setReady] = useState(false),
    [done, setDone] = useState(false),
    [levelUp, setLevelUp] = useState<{ level: number; streak: number; newDay: boolean } | null>(null),
    [error, setError] = useState("");
  const advancing = useRef(false);
  const started = useRef(Date.now()),
    draftKey = `${mode}:${lessonId}`;
  useEffect(() => {
    let alive = true;
    db.drafts
      .get(draftKey)
      .then((d) => {
        if (alive) {
          setStep(Math.min(d?.step ?? 0, steps.length - 1));
          setReady(true);
        }
      })
      .catch(() => {
        if (alive)
          setError(
            "Your saved position could not be loaded. Reload before continuing.",
          );
      });
    return () => {
      alive = false;
    };
  }, [draftKey, steps.length]);
  async function next() {
    if (advancing.current) return;
    advancing.current = true;
    setError("");
    try {
      if (step + 1 >= steps.length) {
        // A first finish of a lesson is a level-up; a repeat is just practice.
        const before = await db.sessions.toArray();
        const attemptTimes = await db.attempts.toArray();
        const firstFinish =
          mode === "lesson" && !before.some((s) => s.lessonId === lessonId && s.kind === "lesson");
        const hadToday = streakOf(before, []).studiedToday;
        await db.transaction("rw", db.sessions, db.drafts, async () => {
          await db.sessions.add({
            id: crypto.randomUUID(),
            lessonId: mode === "listening" ? `listening:${lessonId}` : lessonId,
            kind: mode === "assessment" ? "assessment" : "lesson",
            completedAt: Date.now(),
            attempts: steps.filter((e) =>
              ["choice", "reorder", "read", "recall", "glyph", "pick", "spot", "count", "dialogue", "truefalse", "reply", "listenfill", "cloze", "match"].includes(e.kind),
            ).length,
            seconds: Math.round((Date.now() - started.current) / 1000),
          });
          await db.drafts.delete(draftKey);
        });
        if (firstFinish) {
          const after = await db.sessions.toArray();
          const run = streakOf(after, attemptTimes);
          setLevelUp({ level: levelOf(after).level, streak: run.days, newDay: !hadToday });
        }
        setDone(true);
      } else {
        await db.drafts.put({ id: draftKey, step: step + 1, updatedAt: Date.now() });
        setStep((s) => s + 1);
      }
    } catch {
      setError("Your progress could not be saved. Keep this tab open and try again.");
    } finally {
      advancing.current = false;
    }
  }
  const isRead = lesson.track === "read";
  return (
    <main className={`focus-layout ${isRead ? "track-read" : "track-speak"}`}>
      <header className="focus-header">
        <button className="text-button" onClick={onExit} aria-label="Save and exit">
          <ArrowLeft size={18} /> <span className="hide-sm">Save &amp; exit</span>
        </button>
        <span className="focus-title">
          <span className="hide-sm">{isRead ? "Characters" : lesson.unit} · </span>
          {lesson.title}
        </span>
        <span className="focus-count">
          {done ? "Done" : `${step + 1} / ${steps.length}`}
        </span>
      </header>
      <div
        className="lesson-progress"
        role="progressbar"
        aria-label="Lesson progress"
        aria-valuemin={0}
        aria-valuemax={steps.length}
        aria-valuenow={done ? steps.length : step}
      >
        <div style={{ transform: `scaleX(${done ? 1 : step / steps.length})` }} />
      </div>
      {error && (
        <p role="alert" className="inline-error">
          {error}
        </p>
      )}
      {done && levelUp ? (
        <LevelUp
          level={levelUp.level}
          streak={profile.showStreak === false ? 0 : levelUp.streak}
          newDay={levelUp.newDay}
          mission={lesson.mission}
          glyphs={isRead ? lesson.phrases.map((p) => p.slice(2)) : []}
          onExit={onExit}
        />
      ) : done ? (
        <div className="lesson-done">
          <MoSays autoSpeak state="celebrate" say={moLines.done} size={150} side="top" />
          {isRead ? (
            <p className="done-glyphs" lang="zh-CN">
              {lesson.phrases.map((p) => (
                <span key={p}>{p.slice(2)}</span>
              ))}
            </p>
          ) : (
            <div className="complete-mark">
              <Check size={30} weight="bold" />
            </div>
          )}
          <h1>{isRead ? "Eight more characters you can read." : "A little more Mandarin in your world."}</h1>
          <p>{lesson.mission}</p>
          <p className="muted">
            Unaided answers now have their own review schedule. Come back in a
            day or two and see which ones stayed.
          </p>
          <button className="button" onClick={onExit}>
            Back to your day <Arrow />
          </button>
        </div>
      ) : ready ? (
        <ExerciseView
          key={`${draftKey}-${step}`}
          exercise={steps[step]}
          lessonNotice={lesson.notice}
          context={lesson.context}
          profile={profile}
          onNext={next}
        />
      ) : (
        <div className="loading-state"><Mascot state="think" size={100} />Opening your saved lesson…</div>
      )}
    </main>
  );
}

const kindLabel: Record<string, string> = {
  hear: "Listen",
  notice: "Notice",
  record: "Speak",
  recall: "Recall",
  read: "Read",
  choice: "Understand",
  reorder: "Build",
  dictation: "Write what you hear",
  meet: "New character",
  glyph: "Read",
  pick: "Find",
  spot: "Spot the part",
  grammar: "Pattern",
  register: "Say it naturally",
  count: "Count",
  dialogue: "Listen to the conversation",
  truefalse: "True or false",
  reply: "Choose the reply",
  listenfill: "Fill in what you hear",
  cloze: "Fill the gaps",
  match: "Match",
};

export function ExerciseView({
  exercise: e,
  lessonNotice = "",
  context = "",
  profile,
  onNext,
}: {
  exercise: Exercise;
  lessonNotice?: string;
  context?: string;
  profile: Profile;
  onNext: () => void | Promise<void>;
}) {
  const p = phraseById[e.phraseId];
  const char = charByHanzi[p.hanzi];
  const [revealed, setRevealed] = useState(false),
    [answer, setAnswer] = useState(""),
    [selected, setSelected] = useState<number[]>([]),
    [result, setResult] = useState<boolean | null>(null),
    [submitted, setSubmitted] = useState(false),
    [busy, setBusy] = useState(false),
    [error, setError] = useState(""),
    [heard, setHeard] = useState(false),
    [recorded, setRecorded] = useState(false),
    [taskAnswer, setTaskAnswer] = useState<TaskAnswer | null>(null);
  const start = useRef(Date.now()),
    id = useRef(crypto.randomUUID()),
    audioRef = useRef<HTMLDivElement>(null),
    primary = useRef<HTMLButtonElement>(null),
    footerRef = useRef<HTMLElement>(null),
    moRef = useRef<HTMLDivElement>(null);
  const isChoice = ["choice", "read", "glyph", "pick", "spot", "count", "register"].includes(e.kind),
    isTask = !!e.task,
    listeningTask = listeningTasks.includes(e.kind),
    testing = isChoice || isTask || e.kind === "reorder" || e.kind === "dictation",
    glyphChoices = ["pick", "spot", "count"].includes(e.kind),
    needsAudio = e.kind === "choice" && !heard && !revealed;
  const supportKind = ["glyph", "read", "cloze", "match"].includes(e.kind) ? "pinyin" : "transcript";
  async function submit(
    correct: boolean | null,
    value: string,
    support: "none" | "self-report" | "transcript" | "pinyin" = "none",
  ) {
    if (busy || submitted) return;
    setBusy(true);
    setError("");
    try {
      await saveAttempt({
        id: id.current,
        phraseId: p.id,
        modality: e.modality,
        correct,
        answer: value,
        expected: e.correct ?? p.hanzi,
        latencyMs: Date.now() - start.current,
        support: revealed && support === "none" ? supportKind : support,
        context: e.id,
      });
      setResult(correct);
      setSubmitted(true);
    } catch {
      setError("That answer hasn’t been saved. Please try again.");
    } finally {
      setBusy(false);
    }
  }
  const check = () => {
    if (isTask) {
      if (taskAnswer) void submit(taskAnswer.correct, taskAnswer.value);
      return;
    }
    const value =
      e.kind === "reorder" ? selected.map((i) => e.tokens?.[i]).join("") : answer;
    void submit(normalize(value) === normalize(e.correct ?? p.hanzi), value);
  };
  const advance = async () => {
    if (e.kind === "meet" && !submitted) await submit(null, "Met the character");
    await onNext();
  };
  const canContinue = !(
    busy ||
    (["recall", "record"].includes(e.kind) && !submitted) ||
    (e.kind === "hear" && !heard && !revealed)
  );
  const canCheck =
    !busy &&
    (isTask ? !!taskAnswer?.complete : e.kind === "reorder" ? selected.length === e.tokens?.length : !!answer);
  // Keyboard: Space replays, 1–4 choose, Enter checks or continues.
  useEffect(() => {
    const handler = (event: KeyboardEvent) => {
      const tag = (event.target as HTMLElement)?.tagName;
      if (["INPUT", "TEXTAREA", "SELECT"].includes(tag)) return;
      if (event.code === "Space" && tag !== "BUTTON") {
        event.preventDefault();
        (audioRef.current?.querySelector<HTMLButtonElement>("[data-audio] button") ?? audioRef.current?.querySelector("button"))?.click();
      } else if (isChoice && !submitted && /^[1-9]$/.test(event.key)) {
        const c = e.choices?.[+event.key - 1];
        if (c && !needsAudio) setAnswer(c);
      } else if (
        event.key === "Enter" &&
        (tag !== "BUTTON" || (event.target as HTMLElement).classList.contains("choice"))
      ) {
        event.preventDefault();
        primary.current?.click();
      }
    };
    window.addEventListener("keydown", handler);
    return () => window.removeEventListener("keydown", handler);
  }, [isChoice, submitted, e.choices, needsAudio]);
  // Sayo stands just above the verdict bar, whose height changes with its content.
  useEffect(() => {
    const el = footerRef.current;
    if (!el || typeof ResizeObserver === "undefined") return;
    const root = document.documentElement;
    const ro = new ResizeObserver(() => root.style.setProperty("--verdict-h", `${el.offsetHeight}px`));
    ro.observe(el);
    return () => ro.disconnect();
  }, []);
  // Below 1280px Sayo sits in the flow after the task; bring her reaction into view.
  useEffect(() => {
    if (!submitted || e.kind === "meet" || window.innerWidth >= 1280) return;
    const reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
    // Wait for the verdict bar to grow and report its height, or the page can't scroll far enough yet.
    const timer = setTimeout(() => moRef.current?.scrollIntoView({ block: "nearest", behavior: reduce ? "auto" : "smooth" }), 120);
    return () => clearTimeout(timer);
  }, [submitted, e.kind]);
  return (
    <section className={`exercise kind-${e.kind}`} aria-labelledby="exercise-title">
      <div className="exercise-head">
        <p className="eyebrow">{kindLabel[e.kind]}</p>
        <h1 id="exercise-title">{e.prompt}</h1>
        {e.kind === "hear" && <p className="exercise-context">{context}</p>}
        {e.task?.type === "dialogue" && <p className="exercise-context">{e.task.setting}</p>}
        {(e.kind === "spot" || e.kind === "register") && <p className="exercise-context">{e.cue}</p>}
      </div>

      <div className="exercise-stage" ref={isTask ? audioRef : undefined}>
        {e.task && (
          <TaskView
            task={e.task}
            profile={profile}
            submitted={submitted}
            revealed={revealed}
            heard={heard}
            onHeard={() => setHeard(true)}
            onAnswer={setTaskAnswer}
          />
        )}
        {e.kind === "meet" && char && (
          <div className="meet">
            <HanziStage char={char.hanzi} size={260} autoplay />
            <CharacterAnatomy entry={char} profile={profile} />
          </div>
        )}
        {e.kind === "glyph" && (
          <div className="big-glyph" lang="zh-CN">
            <Speakable text={char?.say ?? p.audio.text ?? p.hanzi} onHear={() => { if (!submitted) setRevealed(true); }}>{p.hanzi}</Speakable>
            {revealed && <Pinyin text={p.pinyin} className="glyph-pinyin" />}
          </div>
        )}
        {e.kind === "grammar" && grammarById[e.cue ?? ""] && (
          <GrammarCard g={grammarById[e.cue ?? ""]} voiceURI={profile.voiceURI} />
        )}
        {e.kind === "count" && (
          <div className="count-dots" role="img" aria-label={`${e.cue} dots`}>
            {Array.from({ length: Number(e.cue) }, (_, i) => (
              <i key={i} />
            ))}
          </div>
        )}
        {e.kind === "spot" && (
          <div className="spot-cue" lang="zh-CN">
            {e.prompt.match(/contains (.+)\?/)?.[1]}
          </div>
        )}
        {["hear", "choice", "notice", "record", "dictation"].includes(e.kind) && (
          <div ref={audioRef} className="stage-audio">
            <AudioButton
              text={p.audio.text}
              mood={e.modality === "tone" || p.topic === "sounds" ? "clear" : undefined}
              companion={!submitted && !revealed && !error}
              voiceURI={profile.voiceURI}
              large={["hear", "choice", "dictation"].includes(e.kind)}
              onPlayed={() => setHeard(true)}
            />
          </div>
        )}
        {e.kind === "hear" && revealed && <PhraseText phrase={p} />}
        {e.kind === "notice" && (
          <>
            <PhraseText phrase={p} />
            {p.example && (
              <div className="example-line">
                <span className="gx-text">
                  <span className="gx-zh" lang="zh-CN">
                    {p.example.zh}
                  </span>
                  <Pinyin text={p.example.py} />
                  <span className="gx-en">{p.example.en}</span>
                </span>
                <AudioButton text={p.example.zh} voiceURI={profile.voiceURI} />
              </div>
            )}
            {(p.usage || lessonNotice) && (
              <div className="teaching-note">
                {p.usage && <p>{p.usage}</p>}
                {lessonNotice && lessonNotice !== p.usage && (
                  <details>
                    <summary>How the pieces fit</summary>
                    <p>{lessonNotice}</p>
                  </details>
                )}
              </div>
            )}
            {e.phraseId === "hello" && (
              <div className="tone-pair">
                <ToneCurve tone={2} />
                <ToneCurve tone={3} />
                <span className="small">ní + hǎo · how it is actually said</span>
              </div>
            )}
          </>
        )}
        {e.kind === "read" && <PhraseText phrase={p} pinyin={revealed} meaning={false} onHear={() => { if (!submitted) setRevealed(true); }} />}
        {e.kind === "choice" && revealed && <PhraseText phrase={p} meaning={false} />}
        {e.kind === "recall" && (
          <>
            <p className="recall-meaning">{p.meaning}</p>
            {revealed ? (
              <>
                <PhraseText phrase={p} meaning={false} />
                <AudioButton text={p.hanzi} voiceURI={profile.voiceURI} />
              </>
            ) : (
              <p className="muted">Say it aloud from memory, then reveal it to compare.</p>
            )}
          </>
        )}
        {e.kind === "reorder" && (
          <>
            <p className="recall-meaning">{p.meaning}</p>
            <div className="assembly" aria-label="Your sentence" lang="zh-CN">
              {selected.map((index, i) => (
                <button
                  key={`${index}-${i}`}
                  disabled={submitted}
                  onClick={() => setSelected((s) => s.filter((_, j) => j !== i))}
                >
                  {e.tokens?.[index]}
                </button>
              ))}
              {!selected.length && <span>Tap the characters in order</span>}
            </div>
            <div className="token-bank" lang="zh-CN">
              {e.tokens?.map((token, i) => (
                <button
                  key={i}
                  disabled={selected.includes(i) || submitted}
                  onClick={() => setSelected((s) => [...s, i])}
                >
                  {token}
                </button>
              ))}
            </div>
          </>
        )}
        {e.kind === "dictation" && (
          <label className="field">
            Type what you hear
            <input
              value={answer}
              onChange={(v) => setAnswer(v.target.value)}
              onKeyDown={(k) => k.key === "Enter" && canCheck && !submitted && check()}
              lang="zh-CN"
              placeholder="输入中文"
            />
          </label>
        )}
        {e.kind === "record" && (
          <>
            <PhraseText phrase={p} />
            <p className="muted">Listen, repeat, then compare your recording with the model.</p>
            {!profile.quiet && <Recorder onAttempt={() => setRecorded(true)} />}
          </>
        )}
      </div>

      {isChoice && (
        <div className={`choices ${glyphChoices ? "glyph-choices" : ""} ${e.kind === "register" ? "zh-choices" : ""}`} role="radiogroup" aria-label="Answers">
          {e.choices?.map((choice, i) => {
            const state = submitted
              ? choice === e.correct
                ? "correct"
                : answer === choice
                  ? "incorrect"
                  : "dim"
              : answer === choice
                ? "selected"
                : "";
            return (
              <button
                key={choice}
                role="radio"
                aria-checked={answer === choice}
                disabled={submitted || busy || needsAudio}
                className={`choice ${state}`}
                onClick={() => setAnswer(choice)}
                lang={glyphChoices || e.kind === "register" ? "zh-CN" : undefined}
              >
                <span className="choice-key" aria-hidden>
                  {i + 1}
                </span>
                <span className="choice-text">{choice}</span>
                {submitted && choice === e.correct && <Check size={18} weight="bold" className="choice-mark" />}
              </button>
            );
          })}
        </div>
      )}

      <div className="exercise-support">
        {e.kind === "hear" && (
          <button className="text-button" onClick={() => setRevealed(!revealed)}>
            <Eye size={17} /> {revealed ? "Hide the words" : "Show the words"}
          </button>
        )}
        {["choice", "read", "glyph"].includes(e.kind) && !submitted && !revealed && (
          <button className="text-button" onClick={() => setRevealed(true)}>
            <Eye size={17} />
            {e.kind === "choice" ? "Show the words" : "Show pinyin"}
          </button>
        )}
        {isTask && !submitted && !revealed && (
          <button className="text-button" onClick={() => setRevealed(true)}>
            <Eye size={17} />
            {listeningTask ? "Show the words" : "Show pinyin"}
          </button>
        )}
        {e.kind === "recall" && !revealed && (
          <button className="button secondary" onClick={() => setRevealed(true)}>
            Reveal phrase
          </button>
        )}
        {e.kind === "recall" && revealed && !submitted && (
          <div className="rating-row">
            <button className="button secondary" disabled={busy} onClick={() => submit(false, "Needed a reminder", "self-report")}>
              Needed a reminder
            </button>
            <button className="button secondary" disabled={busy} onClick={() => submit(true, "Recalled aloud", "self-report")}>
              I had it
            </button>
          </div>
        )}
        {e.kind === "record" && !submitted && (
          <button
            className="text-button"
            disabled={busy}
            onClick={() =>
              submit(
                null,
                recorded ? "Recorded local speaking practice" : profile.quiet ? "Quiet-mode alternative" : "Practiced without recording",
                "self-report",
              )
            }
          >
            {recorded ? "Save this speaking attempt" : profile.quiet ? "I rehearsed it silently" : "I said it aloud"}
          </button>
        )}
        {error && (
          <p role="alert" className="inline-error">
            {error}
          </p>
        )}
      </div>

      {/* Sayo lives in one place beside the task: idle pose while you work, a reaction with her line after you check. */}
      <div ref={moRef} className={`lesson-mo ${submitted && e.kind !== "meet" ? "is-reacting" : ""}`}>
        {submitted && e.kind !== "meet" ? (
          <MoSays autoSpeak collapsible side="top" size={132} {...reaction(e, p.topic, result, revealed)} />
        ) : (
          <Mascot
            size={132}
            still
            state={
              error
                ? "error"
                : revealed
                  ? "hint"
                  : e.kind === "meet"
                    ? "read"
                    : e.kind === "record"
                      ? "speak"
                      : ["hear", "choice", "dictation", ...listeningTasks].includes(e.kind)
                        ? "listen"
                        : "think"
            }
          />
        )}
      </div>
      <footer
        ref={footerRef}
        className={`exercise-footer ${submitted && e.kind !== "meet" ? (result === false ? "is-wrong" : "is-right") : ""}`}
      >
        <div className="verdict" role="status" aria-live="polite">
          {submitted && e.kind !== "meet" ? (
            <>
              <span className="verdict-icon">
                {result === false ? <X size={18} weight="bold" /> : <Check size={18} weight="bold" />}
              </span>
              <span className="verdict-text">
                <strong>{result === true ? "Right." : result === false ? "Not quite." : "Saved."}</strong>
                {result === false && isTask ? (
                  <span className="verdict-answer">
                    {taskAnswer && taskAnswer.total > 1 ? `${taskAnswer.right} of ${taskAnswer.total} right. ` : ""}The answers are marked above.
                  </span>
                ) : result === false ? (
                  <span className="verdict-answer">
                    <span lang="zh-CN" className="verdict-zh">{p.hanzi}</span>
                    <Pinyin text={p.pinyin} />
                    <span>“{p.meaning}”</span>
                    <AudioButton text={p.hanzi} voiceURI={profile.voiceURI} />
                  </span>
                ) : null}
                <span className="verdict-evidence">
                  {result === false
                    ? "Goes back into review soon."
                    : revealed
                      ? `${e.kind === "choice" || listeningTask ? "The words were" : "Pinyin was"} shown, so this counts as supported.`
                      : e.kind === "record"
                        ? "Practice saved. Your recording stays in this tab."
                        : result === null
                          ? "Practice saved."
                          : "Recalled without help."}
                </span>
              </span>
            </>
          ) : (
            <span className="footer-hint">
              {needsAudio
                ? "Play the audio first · Space"
                : isChoice
                  ? "1–4 to choose · Enter to check"
                  : listeningTask && !heard && !revealed
                    ? "Play the audio first · Space"
                    : isTask
                      ? "Enter to check"
                  : e.kind === "meet"
                    ? "Enter to continue"
                    : ""}
            </span>
          )}
        </div>
        {testing && !submitted ? (
          <button ref={primary} className="button" disabled={!canCheck} onClick={check}>
            {busy ? "Saving…" : "Check"}
          </button>
        ) : (
          <button ref={primary} className="button" disabled={!canContinue} onClick={() => void advance()}>
            Continue <Arrow />
          </button>
        )}
      </footer>
    </section>
  );
}

/** Sayo's reaction to a checked answer: brief, specific, always in Mandarin. */
function reaction(
  e: Exercise,
  topic: string,
  result: boolean | null,
  supported: boolean,
): { state: MascotState; say: MoLine } {
  if (result === null) return { state: "celebrate", say: moLines.right[2] };
  if (result && supported) return { state: "hint", say: moLines.supported };
  if (result) {
    const seed = e.id.length + e.id.charCodeAt(e.id.length - 1);
    return { state: "celebrate", say: seed % 4 === 0 ? moLines.cool : pickLine(moLines.right, e.id) };
  }
  if (topic === "sounds" || e.modality === "tone") return { state: "grumpy", say: moLines.tone };
  return { state: "encourage", say: pickLine(moLines.wrong, e.id) };
}

/** First finish of a lesson: a level that names what you can now do. */
function LevelUp({
  level,
  streak,
  newDay,
  mission,
  glyphs,
  onExit,
}: {
  level: number;
  streak: number;
  newDay: boolean;
  mission: string;
  glyphs: string[];
  onExit: () => void;
}) {
  return (
    <div className="level-up" role="status">
      <MoSays autoSpeak state="thumbsup" say={moLines.levelUp} size={156} side="top" />
      <div className="level-badge" aria-label={`Level ${level}`}>
        <span className="level-word">Level</span>
        <span className="level-number tabular">{level}</span>
      </div>
      <h1>Now you can</h1>
      <p className="level-mission">{mission}</p>
      {glyphs.length > 0 && (
        <p className="done-glyphs" lang="zh-CN" aria-label={`New characters: ${glyphs.join(" ")}`}>
          {glyphs.map((g) => (
            <span key={g}>{g}</span>
          ))}
        </p>
      )}
      {streak > 0 && (
        <p className="level-streak">
          <Mascot state="run" size={44} still />
          <span>
            <strong className="tabular">{streak}</strong> {streak === 1 ? "day" : "days in a row"}
            {newDay && streak > 1 ? " · one more today" : ""}
          </span>
        </p>
      )}
      <p className="muted">
        Unaided answers now have their own review schedule. Come back in a day
        or two and see which ones stayed.
      </p>
      <button className="button" onClick={onExit} ref={(b) => b?.focus({ preventScroll: true })}>
        Continue <Arrow />
      </button>
    </div>
  );
}

/** A grammar pattern: what it's for, how it works, real examples, and the usual traps. */
function GrammarCard({ g, voiceURI }: { g: CompiledGrammar; voiceURI: string }) {
  return (
    <div className="grammar-card">
      <p className="grammar-pattern" lang="zh-CN">
        {g.pattern}
      </p>
      <p className="grammar-explain">{g.explanation}</p>
      <ul className="grammar-examples">
        {g.examples.map((ex) => (
          <li key={ex.zh}>
            <span className="gx-text">
              <span className="gx-zh" lang="zh-CN">
                {ex.zh}
              </span>
              <Pinyin text={ex.py} />
              <span className="gx-en">{ex.en}</span>
            </span>
            <AudioButton text={ex.zh} voiceURI={voiceURI} />
          </li>
        ))}
      </ul>
      {!!g.commonMistakes?.length && (
        <div className="grammar-mistakes">
          <p className="eyebrow">Watch out</p>
          {g.commonMistakes.map((m) => (
            <p key={m.wrong} className="gm-row">
              <s lang="zh-CN">{m.wrong}</s>
              <span aria-hidden> → </span>
              <span lang="zh-CN" className="gm-right">
                {m.right}
              </span>
              <span className="gm-why">{m.why}</span>
            </p>
          ))}
        </div>
      )}
      {g.contrastWith && <p className="small">Compare: {g.contrastWith}</p>}
    </div>
  );
}
