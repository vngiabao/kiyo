import { useEffect, useMemo, useRef, useState } from "react";
import HanziWriter from "hanzi-writer";
import { useLiveQuery } from "dexie-react-hooks";
import { ArrowLeft, Check, PencilSimple, Play, X } from "@phosphor-icons/react";
import { db } from "./db";
import { characters, charByHanzi, readingLessons } from "./content";
import {
  glossFor,
  characterSpeech,
  isHan,
  readings,
  type HanziEntry,
  type Reading,
} from "./hanzi";
import { AudioButton, Arrow, Pinyin } from "./components";
import { Journey, PathMap, stoneIcon, type PathNode, type PathUnit } from "./PathMap";
import type { Memory, Profile } from "./types";
import { useSpeech } from "./useSpeech";

const reduceMotion = () =>
  typeof matchMedia !== "undefined" &&
  matchMedia("(prefers-reduced-motion: reduce)").matches;
const token = (name: string, fallback: string) =>
  typeof document === "undefined"
    ? fallback
    : getComputedStyle(document.documentElement)
        .getPropertyValue(name)
        .trim() || fallback;

/**
 * A character drawn from stroke data. Animates once when asked to, and falls
 * back to the font glyph if stroke data is unavailable.
 */
export function HanziStage({
  char,
  size = 240,
  autoplay = false,
  radical = true,
  practice = false,
  controls = true,
  label,
}: {
  char: string;
  size?: number;
  autoplay?: boolean;
  radical?: boolean;
  practice?: boolean;
  controls?: boolean;
  label?: string;
}) {
  const host = useRef<HTMLDivElement>(null),
    writer = useRef<HanziWriter | null>(null),
    [failed, setFailed] = useState(false),
    [playing, setPlaying] = useState(false),
    [traced, setTraced] = useState(false);
  const speech = useSpeech();
  useEffect(() => {
    if (!host.current) return;
    host.current.innerHTML = "";
    setFailed(false);
    setTraced(false);
    const w = HanziWriter.create(host.current, char, {
      width: size,
      height: size,
      padding: Math.round(size * 0.06),
      showOutline: practice,
      showCharacter: !practice && !(autoplay && !reduceMotion()),
      strokeColor: token("--ink", "#1d1c1a"),
      radicalColor: radical ? token("--accent", "#22406a") : null,
      // hanzi-writer only parses hex/rgb() colours, so it gets its own solid token.
      outlineColor: token("--writer-outline", "#34435f"),
      highlightColor: token("--accent", "#22406a"),
      drawingColor: token("--ink", "#1d1c1a"),
      strokeAnimationSpeed: 1.4,
      delayBetweenStrokes: 140,
      renderer: "svg",
      charDataLoader: (c, onLoad, onError) => {
        fetch(`/hanzi/${encodeURIComponent(c)}.json`)
          .then((r) => (r.ok ? r.json() : Promise.reject(r.status)))
          .then(onLoad)
          .catch(onError);
      },
      onLoadCharDataError: () => setFailed(true),
    });
    writer.current = w;
    if (practice)
      void w.quiz({ onComplete: () => setTraced(true), showHintAfterMisses: 2 });
    else if (autoplay && !reduceMotion()) {
      setPlaying(true);
      void w.animateCharacter({ onComplete: () => setPlaying(false) });
    }
    return () => {
      writer.current = null;
    };
  }, [char, size, autoplay, radical, practice]);
  const play = () => {
    const w = writer.current;
    if (!w || playing) return;
    if (reduceMotion()) {
      void w.showCharacter();
      return;
    }
    setPlaying(true);
    void w.animateCharacter({ onComplete: () => setPlaying(false) });
  };
  return (
    <figure className="hanzi-stage" style={{ width: size }}>
      <div className="hanzi-grid" style={{ width: size, height: size }}
        role={practice ? undefined : "button"} tabIndex={practice ? undefined : 0}
        aria-label={practice ? undefined : `Hear ${char}`}
        onClick={practice ? undefined : () => speech.speak(characterSpeech(char))}
        onKeyDown={practice ? undefined : (event) => {
          if (event.key === "Enter" || event.key === " ") {
            event.preventDefault(); event.stopPropagation(); speech.speak(characterSpeech(char));
          }
        }}>
        <svg className="grid-lines" viewBox="0 0 100 100" aria-hidden>
          <path d="M50 0V100M0 50H100" />
          <path className="diag" d="M0 0L100 100M100 0L0 100" />
        </svg>
        {failed ? (
          <span className="hanzi-fallback" lang="zh-CN" style={{ fontSize: size * 0.72 }}>
            {char}
          </span>
        ) : (
          <div
            ref={host}
            className="hanzi-writer"
            role="img"
            aria-label={label ?? `The character ${char}`}
            lang="zh-CN"
          />
        )}
      </div>
      {speech.error && <p className="inline-error" role="alert">{speech.error}</p>}
      {!failed && !practice && controls && (
        <button className="stage-action" onClick={play} disabled={playing}>
          <Play size={14} weight="fill" />
          {playing ? "Writing…" : "Watch the strokes"}
        </button>
      )}
      {practice && (
        <figcaption className="small" role="status">
          {traced ? "Traced. Handwriting is optional practice and isn’t scored." : "Trace each stroke in order. Hints appear after two misses."}
        </figcaption>
      )}
    </figure>
  );
}

const roleLabel = {
  whole: "picture",
  meaning: "meaning",
  sound: "sound",
  shape: "shape",
} as const;

/** The anatomy of one character: parts, origin note and words. */
export function CharacterAnatomy({
  entry,
  profile,
}: {
  entry: HanziEntry;
  profile: Profile;
}) {
  // Every new character arrives with its romanisation (pinyin) and sound.
  const parts = entry.parts.filter((p) => p.role !== "whole");
  return (
    <div className="anatomy">
      <div className="anatomy-head">
        <div className="anatomy-sound">
          <Pinyin text={entry.pinyin} className="anatomy-pinyin" />
          <AudioButton text={entry.say} voiceURI={profile.voiceURI} label="Say it" />
        </div>
        <p className="anatomy-meaning">{entry.meaning}</p>
        {entry.say !== entry.hanzi && (
          <span className="small">You’ll hear it inside {entry.say}.</span>
        )}
      </div>
      {parts.length > 0 ? (
        <div className="parts" aria-label="Parts of this character">
          {parts.map((p, i) => (
            <div key={i} className={`part role-${p.role}`}>
              <span className="part-glyph" lang="zh-CN">
                {p.form}
              </span>
              <span className="part-role">{roleLabel[p.role]}</span>
              {p.gloss && <span className="part-gloss">{p.gloss}</span>}
            </div>
          ))}
        </div>
      ) : (
        <p className="anatomy-whole">
          <span>One picture</span> {entry.parts[0]?.gloss}
        </p>
      )}
      <p className="anatomy-note">
        <span className="note-kind">{entry.noteKind}</span>
        {entry.note}
      </p>
      <dl className="anatomy-words">
        {entry.words.map((w) => (
          <div key={w.w}>
            <dt lang="zh-CN">{w.w}</dt>
            <dd>
              <Pinyin text={w.p} />
              <span>{w.m}</span>
            </dd>
          </div>
        ))}
      </dl>
      <p className="anatomy-meta">
        {entry.strokes} {entry.strokes === 1 ? "stroke" : "strokes"}
        {entry.traditional !== entry.hanzi && (
          <>
            {" · "}traditional <span lang="zh-Hant">{entry.traditional}</span>
          </>
        )}
      </p>
    </div>
  );
}

export type CharStatus = "new" | "met" | "recognised" | "secure";
export function charStatus(memory: Memory | undefined, met: boolean): CharStatus {
  if (memory && memory.successes > 0 && memory.card.state !== 3)
    return memory.card.reps >= 3 && memory.card.stability >= 3
      ? "secure"
      : "recognised";
  return met || memory ? "met" : "new";
}
export function useCharacterStatus() {
  const memories = useLiveQuery(() => db.memories.where("modality").equals("reading").toArray()) ?? [];
  const met = useLiveQuery(async () => {
    const ids = new Set<string>();
    await db.attempts
      .where("phraseId")
      .startsWith("c:")
      .each((a) => {
        ids.add(a.phraseId);
      });
    return ids;
  }) ?? new Set<string>();
  return useMemo(() => {
    const byId = new Map(memories.map((m) => [m.phraseId, m]));
    return Object.fromEntries(
      characters.map((c) => [c.hanzi, charStatus(byId.get(c.id), met.has(c.id))]),
    ) as Record<string, CharStatus>;
  }, [memories, met]);
}
export const knownSet = (status: Record<string, CharStatus>) =>
  new Set(
    Object.entries(status)
      .filter(([, s]) => s === "recognised" || s === "secure")
      .map(([c]) => c),
  );
export function coverage(reading: Reading, known: Set<string>) {
  const han = new Set(reading.lines.flatMap((l) => Array.from(l.zh).filter(isHan)));
  const k = [...han].filter((c) => known.has(c)).length;
  return { known: k, total: han.size, pct: han.size ? Math.round((100 * k) / han.size) : 0 };
}

/** The Read section: a path of character lessons, graded readings, and the full set. */
export function ReadHome({
  profile,
  onLesson,
  onReading,
}: {
  profile: Profile;
  onLesson: (id: string, mode?: "lesson" | "listening") => void;
  onReading: (id: string) => void;
}) {
  const speech = useSpeech();
  const [tab, setTab] = useState<"path" | "texts" | "all">("path"),
    [open, setOpen] = useState<string | null>(null);
  const status = useCharacterStatus(),
    known = knownSet(status);
  const sessions = useLiveQuery(() => db.sessions.toArray()) ?? [];
  const done = new Set(sessions.map((s) => s.lessonId));
  // Each unit: meet the characters, a quick check, then any reading it unlocks.
  const readUnits: PathUnit[] = readingLessons.map((l, i) => ({
    id: l.id,
    number: i + 1,
    title: l.title,
    subtitle: l.description,
    preview: l.phrases.map((p) => p.slice(2)).join(" "),
    nodes: [
      {
        id: l.id,
        // 一 alone reads like a dash, so the counting unit shows 十.
        face: <span lang="zh-CN">{l.phrases[0] === "c:一" ? "十" : l.phrases[0].slice(2)}</span>,
        title: "Meet the characters",
        detail: `${l.phrases.length} new · about ${l.minutes} min`,
        status: done.has(l.id) ? "done" : "open",
        kind: "learn",
        onOpen: () => onLesson(l.id),
      },
      {
        id: `listening:${l.id}`,
        face: stoneIcon.check,
        title: "Quick check",
        detail: "Can you still read them?",
        status: done.has(`listening:${l.id}`) ? "done" : "open",
        kind: "check",
        onOpen: () => onLesson(l.id, "listening"),
      },
      ...readings
        .filter((r) => r.after === l.id)
        .map(
          (r): PathNode => ({
            id: `read:${r.id}`,
            face: stoneIcon.read,
            title: `Read: ${r.title}`,
            detail: r.titleZh,
            status: done.has(`read:${r.id}`) ? "done" : "open",
            kind: "read",
            onOpen: () => onReading(r.id),
          }),
        ),
    ],
  }));
  const firstOpen = readUnits.flatMap((u) => u.nodes).find((n) => n.status !== "done");
  if (firstOpen) firstOpen.status = "next";
  const counts = { met: 0, recognised: 0, secure: 0 };
  for (const s of Object.values(status)) if (s !== "new") counts[s]++;
  return (
    <div className="read-home">
      <header className="page-head">
        <p className="eyebrow">
          <span lang="zh-CN">读</span> Read
        </p>
        <h1>Start from zero. Read a little every day.</h1>
        <p className="lede">
          We begin by counting to ten, then easy words like 你好. Every new
          character comes with its pinyin and its sound, and you can watch it
          being written.
        </p>
        <div className="read-tally" aria-label="Character progress">
          <span>
            <strong>{counts.recognised + counts.secure}</strong> recognised
          </span>
          <span>
            <strong>{counts.secure}</strong> secure
          </span>
          <span>
            <strong>{characters.length}</strong> in this course
          </span>
        </div>
      </header>
      <div className="tabs" role="tablist" aria-label="Reading sections">
        {(
          [
            ["path", "Character path"],
            ["texts", "Readings"],
            ["all", "All characters"],
          ] as const
        ).map(([id, label]) => (
          <button
            key={id}
            role="tab"
            aria-selected={tab === id}
            onClick={() => setTab(id)}
          >
            {label}
          </button>
        ))}
      </div>
      {tab === "path" && (
        <>
          <PathMap label="Character path" units={readUnits} />
          <Journey current={0} />
        </>
      )}
      {tab === "texts" && (
        <div className="reading-list">
          {readings.map((r) => {
            const c = coverage(r, known);
            return (
              <button key={r.id} className="reading-row" onClick={() => onReading(r.id)}>
                <span className="reading-title" lang="zh-CN">
                  {r.titleZh}
                </span>
                <span className="reading-body">
                  <strong>{r.title}</strong>
                  <span>{r.blurb}</span>
                </span>
                <span className="reading-cover">
                  <span className="cover-bar" aria-hidden>
                    <i style={{ transform: `scaleX(${c.pct / 100})` }} />
                  </span>
                  <span>
                    {c.known} of {c.total} characters recognised
                  </span>
                </span>
              </button>
            );
          })}
          <p className="small">
            Characters you haven’t studied are glossed when you tap them. Coverage
            counts only characters you have recognised without help.
          </p>
        </div>
      )}
      {tab === "all" && (
        <div className="char-wall-layout">
          {speech.error && <p className="inline-error" role="alert">{speech.error}</p>}
          <div className="char-wall" lang="zh-CN">
            {characters.map((c) => (
              <button
                key={c.id}
                className={`wall-cell s-${status[c.hanzi]} ${open === c.hanzi ? "is-open" : ""}`}
                onClick={() => { setOpen(c.hanzi); speech.speak(characterSpeech(c.hanzi)); }}
                aria-label={`${c.hanzi}, ${c.meaning}, ${status[c.hanzi]}`}
              >
                {c.hanzi}
              </button>
            ))}
          </div>
          <div className="wall-legend small">
            <span className="s-new">Not met</span>
            <span className="s-met">Met</span>
            <span className="s-recognised">Recognised</span>
            <span className="s-secure">Secure</span>
          </div>
          {open && (
            <CharacterSheet
              entry={charByHanzi[open]}
              profile={profile}
              onClose={() => setOpen(null)}
            />
          )}
        </div>
      )}
    </div>
  );
}

/** A modal sheet: bottom sheet on phones, side panel on wide screens. */
export function CharacterSheet({
  entry,
  profile,
  onClose,
}: {
  entry: HanziEntry;
  profile: Profile;
  onClose: () => void;
}) {
  const [trace, setTrace] = useState(false);
  const ref = useRef<HTMLDivElement>(null);
  useEffect(() => {
    setTrace(false);
    ref.current?.focus();
  }, [entry.id]);
  useEffect(() => {
    const esc = (e: KeyboardEvent) => e.key === "Escape" && onClose();
    window.addEventListener("keydown", esc);
    return () => window.removeEventListener("keydown", esc);
  }, [onClose]);
  return (
    <div className="sheet-scrim" onClick={onClose}>
      <div
        className="sheet"
        role="dialog"
        aria-modal="true"
        aria-label={`Character ${entry.hanzi}`}
        tabIndex={-1}
        ref={ref}
        onClick={(e) => e.stopPropagation()}
      >
        <div className="sheet-top">
          <button className="text-button" onClick={() => setTrace(!trace)}>
            <PencilSimple size={17} /> {trace ? "Stop tracing" : "Trace it (optional)"}
          </button>
          <button className="icon-button" aria-label="Close" onClick={onClose}>
            <X size={20} />
          </button>
        </div>
        <HanziStage key={`${entry.id}-${trace}`} char={entry.hanzi} size={200} practice={trace} autoplay={!trace} />
        {trace && <Mascot state="write" size={90} className="mascot-center" />}
        <CharacterAnatomy entry={entry} profile={profile} />
      </div>
    </div>
  );
}

/** Focused, full-screen reading of one graded text. */
export function Reader({
  readingId,
  profile,
  onExit,
}: {
  readingId: string;
  profile: Profile;
  onExit: () => void;
}) {
  const reading = readings.find((r) => r.id === readingId) ?? readings[0];
  const speech = useSpeech();
  const status = useCharacterStatus(),
    known = knownSet(status);
  const [pinyin, setPinyin] = useState(profile.path !== "characters"),
    [english, setEnglish] = useState<Set<number>>(new Set()),
    [tapped, setTapped] = useState<{ ch: string; line: number; at: number } | null>(null),
    [stage, setStage] = useState<"read" | "check" | "lock" | "done">("read"),
    [lock, setLock] = useState<TaskAnswer | null>(null),
    [locked, setLocked] = useState(false),
    [answers, setAnswers] = useState<Record<number, string>>({}),
    [lookups, setLookups] = useState(0);
  const started = useRef(Date.now());
  const c = coverage(reading, known);
  const gloss = tapped ? glossFor(tapped.ch) : null;
  // Characters the course hasn't taught fall back to the full dictionary (the whole word).
  const words = useWords(tapped && !gloss?.taught ? reading.lines[tapped.line]?.zh : undefined);
  const word = tapped && words.tokens ? tokenAt(words.tokens, tapped.at) : undefined;
  async function finish() {
    await db.sessions.add({
      id: crypto.randomUUID(),
      lessonId: `read:${reading.id}`,
      kind: "lesson",
      completedAt: Date.now(),
      attempts: reading.questions.length,
      seconds: Math.round((Date.now() - started.current) / 1000),
    });
    setStage("done");
  }
  return (
    <main className="focus-layout reader-layout">
      <header className="focus-header">
        <button className="text-button" onClick={onExit}>
          <ArrowLeft size={18} /> Back
        </button>
        <span className="focus-title">
          <span lang="zh-CN">{reading.titleZh}</span> · {reading.title}
        </span>
        <span className="focus-count">{c.pct}% known</span>
      </header>
      <div className="reader">
        {stage === "read" && (
          <>
            <div className="reader-tools" role="group" aria-label="Reading support">
              <button aria-pressed={pinyin} onClick={() => setPinyin(!pinyin)}>
                Pinyin
              </button>
              <button
                aria-pressed={english.size === reading.lines.length}
                onClick={() =>
                  setEnglish(
                    english.size === reading.lines.length
                      ? new Set()
                      : new Set(reading.lines.map((_, i) => i)),
                  )
                }
              >
                English
              </button>
              <AudioButton
                text={reading.lines.map((l) => l.zh).join("")}
                voiceURI={profile.voiceURI}
                label="Read aloud"
              />
            </div>
            {reading.purpose && <p className="reader-purpose">{reading.purpose}</p>}
            <p className="reader-hint small">
              Tap any character to hear it and see its meaning. Faded characters are ones you
              haven’t studied yet.
            </p>
            <article className={`reader-text format-${reading.format ?? "story"}`} lang="zh-CN">
              {reading.lines.map((line, li) => (
                <div
                  className={`reader-line ${reading.format === "chat" && line.speaker && line.speaker !== reading.lines[0].speaker ? "is-reply" : ""}`}
                  key={li}
                >
                  {line.speaker && <span className="speaker">{line.speaker}</span>}
                  <p className="line-zh">
                    {Array.from(line.zh).map((ch, ci) =>
                      isHan(ch) ? (
                        <button
                          key={ci}
                          className={`rch ${known.has(ch) ? "k" : charByHanzi[ch] ? "t" : "u"} ${tapped?.ch === ch && tapped.line === li ? "on" : ""}`}
                          onClick={() => {
                            setTapped({ ch, line: li, at: ci });
                            setLookups((n) => n + 1);
                            speech.speak(characterSpeech(ch));
                          }}
                        >
                          {ch}
                        </button>
                      ) : (
                        <span key={ci} className="punct">
                          {ch}
                        </span>
                      ),
                    )}
                  </p>
                  {pinyin && <Pinyin text={line.py} className="line-py" />}
                  {english.has(li) ? (
                    <p className="line-en" lang="en">
                      {line.en}
                    </p>
                  ) : (
                    <button
                      className="line-reveal"
                      lang="en"
                      onClick={() => setEnglish(new Set(english).add(li))}
                    >
                      Meaning
                    </button>
                  )}
                </div>
              ))}
            </article>
            {speech.error && <p className="inline-error" role="alert">{speech.error}</p>}
            {tapped && !gloss?.taught && word && (
              <div className="reader-word">
                <WordCard
                  token={word}
                  line={reading.lines[tapped.line].zh}
                  source={reading.title}
                  voiceURI={profile.voiceURI}
                  onClose={() => setTapped(null)}
                />
              </div>
            )}
            {tapped && gloss?.taught && (
              <aside className="gloss" role="status" lang="en">
                <span className="gloss-char" lang="zh-CN">
                  {tapped.ch}
                </span>
                <span className="gloss-body">
                  <Pinyin text={gloss.p} />
                  <span>{gloss.m}</span>
                </span>
                <button className="icon-button" aria-label="Close gloss" onClick={() => setTapped(null)}>
                  <X size={18} />
                </button>
              </aside>
            )}
            <footer className="reader-footer">
              <span className="small">
                {lookups ? `${lookups} ${lookups === 1 ? "look-up" : "look-ups"}` : "No look-ups yet"}
              </span>
              <button className="button" onClick={() => setStage("check")}>
                Check understanding <Arrow />
              </button>
            </footer>
          </>
        )}
        {stage === "check" && (
          <div className="reader-check">
            <h1>What did you read?</h1>
            {reading.purpose && <p className="reader-purpose">{reading.purpose}</p>}
            {reading.questions.map((q, qi) => (
              <fieldset key={qi} className="question">
                <legend>
                  {q.kind && <span className="q-kind">{q.kind === "gist" ? "Main idea" : q.kind === "inference" ? "Read between the lines" : "Detail"}</span>}
                  {q.q}
                </legend>
                <div className="choices">
                  {q.choices.map((ch) => {
                    const picked = answers[qi] === ch,
                      answered = answers[qi] !== undefined;
                    return (
                      <button
                        key={ch}
                        className={`choice ${picked ? "selected" : ""} ${answered && ch === q.answer ? "correct" : ""} ${picked && ch !== q.answer ? "incorrect" : ""}`}
                        disabled={answered}
                        onClick={() => setAnswers({ ...answers, [qi]: ch })}
                      >
                        {ch}
                        {answered && ch === q.answer && <Check size={18} />}
                      </button>
                    );
                  })}
                </div>
              </fieldset>
            ))}
            <footer className="reader-footer">
              <button className="text-button" onClick={() => setStage("read")}>
                <ArrowLeft size={17} /> Reread the text
              </button>
              <button
                className="button"
                disabled={Object.keys(answers).length < reading.questions.length}
                onClick={() => (reading.cloze ? setStage("lock") : void finish())}
              >
                {reading.cloze ? "Next: lock it in" : "Finish"} <Arrow />
              </button>
            </footer>
          </div>
        )}
        {stage === "lock" && reading.cloze && (
          <div className="reader-check reader-lock">
            <p className="eyebrow">Lock it in</p>
            <h1>Put the words back.</h1>
            <p className="muted">The text is hidden. Fill each gap from memory, then check.</p>
            <TaskView
              task={{ type: "cloze", id: `${reading.id}-lock`, phrase: "", title: reading.title, lines: reading.cloze.lines, bank: reading.cloze.bank }}
              profile={profile}
              submitted={locked}
              revealed={false}
              heard
              onHeard={() => undefined}
              onAnswer={setLock}
            />
            <footer className="reader-footer">
              {locked ? (
                <>
                  <span className="small">{lock ? `${lock.right} of ${lock.total} back in place.` : ""}</span>
                  <button className="button" onClick={() => void finish()}>
                    Finish <Arrow />
                  </button>
                </>
              ) : (
                <>
                  <button className="text-button" onClick={() => void finish()}>
                    Skip
                  </button>
                  <button className="button" disabled={!lock?.complete} onClick={() => setLocked(true)}>
                    Check <Arrow />
                  </button>
                </>
              )}
            </footer>
          </div>
        )}
        {stage === "done" && (
          <div className="lesson-done">
            <p className="done-glyph" lang="zh-CN">
              {reading.titleZh}
            </p>
            <h1>You read a whole text in Chinese.</h1>
            <MoSays autoSpeak state="celebrate" size={150} side="top" />
            <p>
              {reading.questions.filter((q, i) => answers[i] === q.answer).length} of{" "}
              {reading.questions.length} questions answered as the text says, with{" "}
              {lookups} {lookups === 1 ? "look-up" : "look-ups"}. Come back in a
              few days and try it with fewer.
            </p>
            <button className="button" onClick={onExit}>
              Back to reading <Arrow />
            </button>
          </div>
        )}
      </div>
    </main>
  );
}
import { Mascot, MoSays } from "./Mascot";
import { TaskView, type TaskAnswer } from "./TaskView";
import { WordCard, useWords } from "./WordCard";
import { tokenAt } from "./dictionary";
