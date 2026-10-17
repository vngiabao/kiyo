import { useEffect, useMemo, useRef, useState } from "react";
import { Check, Play, Stop, X } from "@phosphor-icons/react";
import { browserSpeech } from "./audio";
import { answerSpeechText } from "./answer-text";
import { AudioButton, Pinyin } from "./components";
import { dialogueMood, type SayoMood } from "./sayo-voice";
import type { Profile, Task, TaskLine } from "./types";
import { blanksOf, fillMatches, plain, speakersOf, withGaps } from "./tasks";

/** What the task reports to the exercise shell after every change. */
export interface TaskAnswer {
  complete: boolean;
  correct: boolean;
  /** Human-readable summary for the attempt log, e.g. "2/3: A | B | C". */
  value: string;
  right: number;
  total: number;
}

const rotate = <T,>(xs: T[], by: number) => xs.map((_, i) => xs[(i + by) % xs.length]);

/** Plays lines one after another, each in its speaker's mood. */
function useLinePlayer(voiceURI: string) {
  const [current, setCurrent] = useState(-1);
  const [playing, setPlaying] = useState(false);
  const [error, setError] = useState("");
  const owner = useRef<AbortController | null>(null);
  useEffect(() => () => owner.current?.abort(), []);
  const stop = () => {
    owner.current?.abort();
    owner.current = null;
    setPlaying(false);
    setCurrent(-1);
  };
  async function play(lines: { zh: string; mood?: SayoMood }[], from = 0, rate = 1, onDone?: () => void) {
    owner.current?.abort();
    const c = new AbortController();
    owner.current = c;
    setPlaying(true);
    setError("");
    try {
      for (let i = from; i < lines.length; i++) {
        if (c.signal.aborted) return;
        setCurrent(i);
        await browserSpeech.speak(lines[i].zh, { voiceURI, mood: lines[i].mood, rate, signal: c.signal });
        if (c.signal.aborted) return;
        await new Promise((r) => setTimeout(r, 380));
      }
      if (!c.signal.aborted) onDone?.();
    } catch (reason) {
      if (!c.signal.aborted) setError(reason instanceof Error ? reason.message : "Audio could not play.");
    } finally {
      if (owner.current === c) {
        setPlaying(false);
        setCurrent(-1);
      }
    }
  }
  return { play, stop, playing, current, error };
}

export function TaskView({
  task: t,
  profile,
  submitted,
  revealed,
  onAnswer,
  onHeard,
  heard,
}: {
  task: Task;
  profile: Profile;
  submitted: boolean;
  revealed: boolean;
  heard: boolean;
  onAnswer: (a: TaskAnswer) => void;
  onHeard: () => void;
}) {
  switch (t.type) {
    case "dialogue":
      return <DialogueTask t={t} {...{ profile, submitted, revealed, onAnswer, onHeard, heard }} />;
    case "truefalse":
      return <TrueFalseTask t={t} {...{ profile, submitted, revealed, onAnswer, onHeard, heard }} />;
    case "reply":
      return <ReplyTask t={t} {...{ profile, submitted, revealed, onAnswer, onHeard, heard }} />;
    case "listenfill":
      return <FillTask t={t} {...{ profile, submitted, revealed, onAnswer, onHeard }} />;
    case "cloze":
      return <ClozeTask t={t} {...{ profile, submitted, revealed, onAnswer }} />;
    case "match":
      return <MatchTask t={t} {...{ profile, submitted, revealed, onAnswer }} />;
  }
}

type Of<K extends Task["type"]> = Extract<Task, { type: K }>;
interface Shared {
  profile: Profile;
  submitted: boolean;
  revealed: boolean;
  onAnswer: (a: TaskAnswer) => void;
}

/** A line of transcript: who, the Chinese, pinyin, English, and a replay. */
function TranscriptLine({ line, voiceURI, mood, active = false }: { line: TaskLine; voiceURI: string; mood?: SayoMood; active?: boolean }) {
  return (
    <li className={`tx-line ${active ? "is-active" : ""}`}>
      {line.speaker && <span className="tx-who" lang="zh-CN">{line.speaker}</span>}
      <span className="tx-text">
        <span className="tx-zh" lang="zh-CN">{plain(line.zh)}</span>
        <Pinyin text={line.py} />
        {line.en && <span className="tx-en">{line.en}</span>}
      </span>
      <AudioButton text={plain(line.zh)} voiceURI={voiceURI} mood={mood} />
    </li>
  );
}

/** A radio group of answers that marks itself after checking. */
function Choices({
  name,
  choices,
  value,
  answer,
  submitted,
  disabled,
  zh = false,
  pinyin,
  onPick,
}: {
  name: string;
  choices: string[];
  value: string;
  answer: string;
  submitted: boolean;
  disabled: boolean;
  zh?: boolean;
  pinyin?: Record<string, string>;
  onPick: (c: string) => void;
}) {
  return (
    <div className={`choices ${zh ? "zh-choices" : ""}`} role="radiogroup" aria-label={name}>
      {choices.map((c, i) => {
        const state = submitted ? (c === answer ? "correct" : value === c ? "incorrect" : "dim") : value === c ? "selected" : "";
        return (
          <button
            key={c}
            role="radio"
            aria-checked={value === c}
            disabled={submitted || disabled}
            className={`choice ${state}`}
            onClick={() => onPick(c)}
            lang={zh ? "zh-CN" : undefined}
            data-say={answerSpeechText(c) ? c : undefined}
          >
            <span className="choice-key" aria-hidden>{i + 1}</span>
            <span className="choice-text">
              {c}
              {pinyin?.[c] && <Pinyin text={pinyin[c]} />}
            </span>
            {submitted && c === answer && <Check size={18} weight="bold" className="choice-mark" />}
            {submitted && c !== answer && value === c && <X size={18} weight="bold" className="choice-mark" />}
          </button>
        );
      })}
    </div>
  );
}

function DialogueTask({ t, profile, submitted, revealed, onAnswer, onHeard, heard }: Shared & { t: Of<"dialogue">; heard: boolean; onHeard: () => void }) {
  const who = useMemo(() => speakersOf(t.lines), [t.lines]);
  const voiced = useMemo(() => t.lines.map((l) => ({ zh: plain(l.zh), mood: dialogueMood(who.indexOf(l.speaker ?? "")) })), [t.lines, who]);
  const player = useLinePlayer(profile.voiceURI);
  const [picks, setPicks] = useState<string[]>(() => t.questions.map(() => ""));
  useEffect(() => {
    const right = t.questions.filter((q, i) => picks[i] === q.answer).length;
    onAnswer({
      complete: picks.every(Boolean),
      correct: right === t.questions.length,
      right,
      total: t.questions.length,
      value: `${right}/${t.questions.length}: ${picks.join(" | ")}`,
    });
  }, [picks]); // eslint-disable-line react-hooks/exhaustive-deps
  const speaking = player.playing ? t.lines[player.current]?.speaker : undefined;
  return (
    <div className="task task-dialogue">
      <div className="convo-player">
        <ul className="convo-cast" aria-label="Speakers">
          {who.map((name, i) => (
            <li key={name} className={`cast-chip tone-${i % 3} ${speaking === name ? "is-speaking" : ""}`} lang="zh-CN">
              <span className="cast-dot" aria-hidden />
              {name}
            </li>
          ))}
        </ul>
        <div className="convo-controls" data-audio>
          <button
            className={`audio-disc ${player.playing ? "is-playing" : ""}`}
            onClick={() => (player.playing ? player.stop() : void player.play(voiced, 0, 1, onHeard))}
            aria-label={player.playing ? "Stop the conversation" : heard ? "Play the conversation again" : "Play the conversation"}
          >
            {player.playing ? <Stop size={26} weight="fill" /> : <Play size={28} weight="fill" />}
          </button>
          <span className="audio-caption">
            {player.playing ? `Line ${player.current + 1} of ${t.lines.length}` : heard ? "Play again · Space" : "Play the conversation · Space"}
          </span>
          <ol className="convo-dots" aria-hidden>
            {t.lines.map((_, i) => (
              <li key={i} className={i === player.current ? "is-now" : i < player.current || (heard && !player.playing) ? "is-done" : ""} />
            ))}
          </ol>
        </div>
        {!heard && !revealed && <p className="task-gate muted">Listen once through, then answer. Replays are free.</p>}
        {player.error && <p className="inline-error" role="alert">{player.error}</p>}
      </div>

      <ol className="task-questions">
        {t.questions.map((q, qi) => (
          <li key={q.q} className="task-question">
            <p className="tq-prompt">
              <span className="tq-num tabular">{qi + 1}</span>
              {q.q}
            </p>
            <Choices
              name={q.q}
              choices={q.choices}
              value={picks[qi]}
              answer={q.answer}
              submitted={submitted}
              disabled={!heard && !revealed}
              onPick={(c) => setPicks((p) => p.map((x, j) => (j === qi ? c : x)))}
            />
          </li>
        ))}
      </ol>

      {(submitted || revealed) && (
        <details className="transcript" open={submitted}>
          <summary>Transcript</summary>
          <ol>
            {t.lines.map((l, i) => (
              <TranscriptLine key={i} line={l} voiceURI={profile.voiceURI} mood={voiced[i].mood} active={player.current === i} />
            ))}
          </ol>
        </details>
      )}
    </div>
  );
}

function TrueFalseTask({ t, profile, submitted, revealed, onAnswer, onHeard, heard }: Shared & { t: Of<"truefalse">; heard: boolean; onHeard: () => void }) {
  const [pick, setPick] = useState("");
  const yes = "True · 对",
    no = "False · 错";
  useEffect(() => {
    const ok = pick === (t.answer ? yes : no);
    onAnswer({ complete: !!pick, correct: ok, right: ok ? 1 : 0, total: 1, value: pick });
  }, [pick]); // eslint-disable-line react-hooks/exhaustive-deps
  return (
    <div className="task task-tf">
      <div className="stage-audio" data-audio>
        <AudioButton text={plain(t.audio.zh)} mood="clear" voiceURI={profile.voiceURI} large companion={false} onPlayed={onHeard} />
      </div>
      <p className="tf-statement">{t.statement}</p>
      <Choices name="True or false" choices={[yes, no]} value={pick} answer={t.answer ? yes : no} submitted={submitted} disabled={!heard && !revealed} onPick={setPick} />
      {(submitted || revealed) && (
        <ul className="transcript-inline">
          <TranscriptLine line={t.audio} voiceURI={profile.voiceURI} mood="clear" />
        </ul>
      )}
      {submitted && <p className="task-why">{t.why}</p>}
    </div>
  );
}

function ReplyTask({ t, profile, submitted, revealed, onAnswer, onHeard, heard }: Shared & { t: Of<"reply">; heard: boolean; onHeard: () => void }) {
  const [pick, setPick] = useState("");
  useEffect(() => {
    const ok = pick === t.answer;
    onAnswer({ complete: !!pick, correct: ok, right: ok ? 1 : 0, total: 1, value: pick });
  }, [pick]); // eslint-disable-line react-hooks/exhaustive-deps
  return (
    <div className="task task-reply">
      <div className="stage-audio" data-audio>
        <AudioButton text={plain(t.prompt.zh)} mood="clear" voiceURI={profile.voiceURI} large companion={false} onPlayed={onHeard} />
      </div>
      {(submitted || revealed) && (
        <ul className="transcript-inline">
          <TranscriptLine line={t.prompt} voiceURI={profile.voiceURI} mood="clear" />
        </ul>
      )}
      <Choices name="Replies" zh choices={t.choices} value={pick} answer={t.answer} submitted={submitted} disabled={!heard && !revealed} onPick={setPick} />
      {submitted && t.why && <p className="task-why">{t.why}</p>}
    </div>
  );
}

function FillTask({ t, profile, submitted, revealed, onAnswer, onHeard }: Omit<Shared, "heard"> & { t: Of<"listenfill">; onHeard: () => void }) {
  const [text, setText] = useState("");
  const blank = blanksOf(t.line.zh)[0] ?? "";
  useEffect(() => {
    const ok = fillMatches(text, blank, t.blankPy);
    onAnswer({ complete: !!text.trim(), correct: ok, right: ok ? 1 : 0, total: 1, value: text.trim() });
  }, [text]); // eslint-disable-line react-hooks/exhaustive-deps
  const [before, after] = withGaps(t.line.zh).split("＿＿");
  return (
    <div className="task task-fill">
      <div className="fill-audio" data-audio>
        <AudioButton text={plain(t.line.zh)} mood="clear" voiceURI={profile.voiceURI} large companion={false} onPlayed={onHeard} />
        <AudioButton text={plain(t.line.zh)} mood="clear" voiceURI={profile.voiceURI} rate={0.75} label="Slower" />
      </div>
      <p className="fill-line" lang="zh-CN">
        <span>{before}</span>
        <label className={`fill-slot ${submitted ? (fillMatches(text, blank, t.blankPy) ? "is-right" : "is-wrong") : ""}`}>
          <span className="sr-only">The missing word</span>
          <input
            value={text}
            size={Math.max(3, blank.length * 2 + 1)}
            disabled={submitted}
            onChange={(ev) => setText(ev.target.value)}
            autoComplete="off"
            autoCapitalize="off"
            spellCheck={false}
            placeholder="汉字 / pinyin"
          />
        </label>
        <span>{after}</span>
      </p>
      {revealed && !submitted && <Pinyin text={t.line.py} className="fill-py" />}
      <p className="small muted">Type the characters, or pinyin with or without tone marks.</p>
      {submitted && (
        <ul className="transcript-inline">
          <TranscriptLine line={t.line} voiceURI={profile.voiceURI} mood="clear" />
        </ul>
      )}
    </div>
  );
}

function ClozeTask({ t, profile, submitted, revealed, onAnswer }: Omit<Shared, "heard"> & { t: Of<"cloze"> }) {
  const answers = useMemo(() => t.lines.flatMap((l) => blanksOf(l.zh)), [t.lines]);
  const bank = useMemo(() => rotate(t.bank, Math.ceil(t.bank.length / 2)), [t.bank]);
  const [fills, setFills] = useState<string[]>(() => answers.map(() => ""));
  const [active, setActive] = useState(0);
  useEffect(() => {
    const right = fills.filter((f, i) => f === answers[i]).length;
    onAnswer({ complete: fills.every(Boolean), correct: right === answers.length, right, total: answers.length, value: `${right}/${answers.length}: ${fills.join(" | ")}` });
  }, [fills]); // eslint-disable-line react-hooks/exhaustive-deps
  const place = (word: string) => {
    const target = fills[active] === "" ? active : fills.indexOf("");
    if (target < 0) return;
    const next = fills.map((f, i) => (i === target ? word : f));
    setFills(next);
    const empty = next.indexOf("");
    if (empty >= 0) setActive(empty);
  };
  let slot = -1;
  return (
    <div className="task task-cloze">
      <div className="cloze-text" lang="zh-CN">
        {t.lines.map((l, li) => (
          <div key={li} className="cloze-line">
            {l.speaker && <span className="tx-who">{l.speaker}</span>}
            <span className="cloze-zh">
              {l.zh.split(/(【[^】]+】)/).map((part, pi) => {
                if (!part.startsWith("【")) return <span key={pi}>{part}</span>;
                const i = ++slot;
                const state = submitted ? (fills[i] === answers[i] ? "is-right" : "is-wrong") : i === active ? "is-active" : "";
                return (
                  <button
                    key={pi}
                    className={`cloze-slot ${state} ${fills[i] ? "is-filled" : ""}`}
                    disabled={submitted}
                    aria-label={fills[i] ? `Blank ${i + 1}: ${fills[i]}. Tap to clear.` : `Blank ${i + 1}, empty`}
                    onClick={() => {
                      setFills((f) => f.map((x, j) => (j === i ? "" : x)));
                      setActive(i);
                    }}
                  >
                    {fills[i] || "　　"}
                    {submitted && fills[i] !== answers[i] && <span className="cloze-fix">{answers[i]}</span>}
                  </button>
                );
              })}
            </span>
            {(revealed || submitted) && <Pinyin text={l.py} />}
            {submitted && l.en && <span className="tx-en">{l.en}</span>}
            {submitted && <AudioButton text={plain(l.zh)} mood="clear" voiceURI={profile.voiceURI} />}
          </div>
        ))}
      </div>
      {!submitted && (
        <div className="token-bank" lang="zh-CN" aria-label="Word bank">
          {bank.map((w) => (
            <button key={w} disabled={fills.includes(w)} onClick={() => place(w)} data-say={w}>
              {w}
            </button>
          ))}
        </div>
      )}
    </div>
  );
}

function MatchTask({ t, submitted, revealed, onAnswer }: Omit<Shared, "heard"> & { t: Of<"match"> }) {
  const order = useMemo(() => rotate(t.pairs.map((_, i) => i), 1 + (t.id.length % Math.max(1, t.pairs.length - 1))), [t]);
  const [links, setLinks] = useState<(number | null)[]>(() => t.pairs.map(() => null));
  const [active, setActive] = useState(0);
  useEffect(() => {
    const right = links.filter((r, i) => r === i).length;
    onAnswer({
      complete: links.every((x) => x !== null),
      correct: right === t.pairs.length,
      right,
      total: t.pairs.length,
      value: `${right}/${t.pairs.length}`,
    });
  }, [links]); // eslint-disable-line react-hooks/exhaustive-deps
  const link = (right: number) => {
    const next = links.map((r, i) => (i === active ? right : r === right ? null : r));
    setLinks(next);
    const open = next.indexOf(null);
    if (open >= 0) setActive(open);
  };
  return (
    <div className="task task-match">
      <ol className="match-left">
        {t.pairs.map((p, i) => {
          const state = submitted ? (links[i] === i ? "is-right" : "is-wrong") : i === active ? "is-active" : "";
          return (
            <li key={i}>
              <button className={`match-item ${state}`} disabled={submitted} onClick={() => setActive(i)} aria-pressed={i === active}>
                <span className="match-key tabular" aria-hidden>{i + 1}</span>
                {typeof p.left === "string" ? (
                  <span>{p.left}</span>
                ) : (
                  <span className="match-zh" lang="zh-CN">
                    {plain(p.left.zh)}
                    {(revealed || submitted) && <Pinyin text={p.left.py} />}
                  </span>
                )}
                {links[i] !== null && <span className="match-link" lang="zh-CN">→ {plain(t.pairs[links[i]!].right.zh)}</span>}
              </button>
              {submitted && links[i] !== i && (
                <p className="match-fix" lang="zh-CN">
                  {plain(p.right.zh)} <Pinyin text={p.right.py} />
                </p>
              )}
            </li>
          );
        })}
      </ol>
      <div className="match-right" role="group" aria-label={`Answers for item ${active + 1}`}>
        {order.map((ri) => {
          const owner = links.indexOf(ri);
          return (
            <button key={ri} className={`match-option ${owner >= 0 ? "is-used" : ""}`} disabled={submitted} onClick={() => link(ri)} lang="zh-CN" data-say={plain(t.pairs[ri].right.zh)}>
              {owner >= 0 && <span className="match-key tabular" aria-hidden>{owner + 1}</span>}
              <span className="match-zh">
                {plain(t.pairs[ri].right.zh)}
                {(revealed || submitted) && <Pinyin text={t.pairs[ri].right.py} />}
              </span>
            </button>
          );
        })}
      </div>
    </div>
  );
}
