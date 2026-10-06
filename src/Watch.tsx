import { useEffect, useMemo, useRef, useState } from "react";
import {
  ArrowCounterClockwise,
  CaretLeft,
  CaretRight,
  DownloadSimple,
  Eye,
  FilmStrip,
  MusicNotes,
  Repeat,
  Star,
  Trash,
  UploadSimple,
} from "@phosphor-icons/react";
import { useLiveQuery } from "dexie-react-hooks";
import { db } from "./db";
import { packUnits } from "./content";
import { cueAt, parseCaptions, type Cue } from "./captions";
import { TappableLine, WordCard, useWords } from "./WordCard";
import type { Token } from "./dictionary";
import type { Profile, WatchLog } from "./types";

type Rung = WatchLog["rung"];
const rungs: { id: Rung; title: string; hint: string }[] = [
  {
    id: "subtitles",
    title: "Chinese subtitles",
    hint: "Read every line as it plays. Tap a character to look it up.",
  },
  {
    id: "peek",
    title: "Peek when stuck",
    hint: "Lines stay hidden. Peek only when you're lost; every peek is counted.",
  },
  {
    id: "none",
    title: "No subtitles",
    hint: "Ears only. See the lines you heard when you finish.",
  },
];
const mmss = (s: number) =>
  `${Math.floor(s / 60)}:${String(Math.floor(s % 60)).padStart(2, "0")}`;

/**
 * Watch and sing: your own video or song with its .srt / .vtt subtitles or .lrc lyrics.
 * Three rungs from reading every line to none; peeks and look-ups are counted honestly.
 * Files never leave the device.
 */
export function WatchPlayer({ profile }: { profile: Profile }) {
  const [media, setMedia] = useState<{
      url: string;
      name: string;
      kind: "video" | "audio";
    } | null>(null),
    [cues, setCues] = useState<Cue[]>([]),
    [capName, setCapName] = useState(""),
    [rung, setRung] = useState<Rung>("subtitles"),
    [time, setTime] = useState(0),
    [slow, setSlow] = useState(false),
    [loopLine, setLoopLine] = useState(false),
    [peeked, setPeeked] = useState<Set<number>>(new Set()),
    [heardLines, setHeardLines] = useState<Set<number>>(new Set()),
    [lookups, setLookups] = useState(0),
    [tapped, setTapped] = useState<{ token: Token; line: string } | null>(null),
    [noteFor, setNoteFor] = useState<string | null>(null),
    [summary, setSummary] = useState<WatchLog | null>(null),
    [error, setError] = useState("");
  const el = useRef<HTMLVideoElement & HTMLAudioElement>(null),
    played = useRef(0),
    lastT = useRef(0),
    lastIdx = useRef(-1);
  const saved =
    useLiveQuery(() => db.savedLines.orderBy("at").reverse().toArray()) ?? [];
  const history =
    useLiveQuery(() =>
      db.watchLog.orderBy("at").reverse().limit(6).toArray(),
    ) ?? [];

  useEffect(
    () => () => void (media && URL.revokeObjectURL(media.url)),
    [media],
  );
  useEffect(() => {
    if (el.current) el.current.playbackRate = slow ? 0.75 : 1;
  }, [slow, media]);

  const now = cueAt(cues, time);
  if (now >= 0) lastIdx.current = now;
  const focus = now >= 0 ? now : lastIdx.current;
  const isLyrics = capName.toLowerCase().endsWith(".lrc");

  const seek = (i: number) => {
    const c = cues[i];
    if (!c || !el.current) return;
    el.current.currentTime = c.start + 0.01;
    void el.current.play().catch(() => undefined);
  };
  const peek = () => {
    if (focus < 0 || rung !== "peek") return;
    setPeeked((s) => new Set(s).add(focus));
  };
  async function saveLine() {
    const c = cues[focus];
    if (!c || !media) return;
    const id = crypto.randomUUID();
    await db.savedLines.add({
      id,
      text: c.text,
      note: "",
      source: media.name,
      start: c.start,
      at: Date.now(),
    });
    setNoteFor(id);
  }
  async function finish() {
    if (!media) return;
    const log: WatchLog = {
      id: crypto.randomUUID(),
      source: media.name,
      media: media.kind,
      rung,
      seconds: Math.round(played.current),
      peeks: peeked.size,
      lookups,
      lines: heardLines.size,
      at: Date.now(),
    };
    if (log.seconds >= 10) await db.watchLog.add(log);
    setSummary(log);
    el.current?.pause();
  }
  function restart() {
    setSummary(null);
    setPeeked(new Set());
    setHeardLines(new Set());
    setLookups(0);
    played.current = 0;
  }
  // Keyboard: R replay line · P peek · S save · ← → previous / next line.
  useEffect(() => {
    const onKey = (e: KeyboardEvent) => {
      const tag = (e.target as HTMLElement)?.tagName;
      if (
        ["INPUT", "TEXTAREA", "SELECT", "VIDEO", "AUDIO"].includes(tag) ||
        !cues.length
      )
        return;
      if (e.key === "r") seek(focus);
      else if (e.key === "p") peek();
      else if (e.key === "s") void saveLine();
      else if (e.key === "ArrowLeft") seek(Math.max(0, focus - 1));
      else if (e.key === "ArrowRight")
        seek(Math.min(cues.length - 1, focus + 1));
      else return;
      e.preventDefault();
    };
    window.addEventListener("keydown", onKey);
    return () => window.removeEventListener("keydown", onKey);
  });

  const line = (i: number, role: "prev" | "next") => {
    const c = cues[i];
    return (
      <p className={`watch-line ${role}`} lang="zh-CN" aria-hidden={!c}>
        {c?.text}
      </p>
    );
  };
  const showNow =
    rung === "subtitles" || (rung === "peek" && peeked.has(focus));
  // The current line, split into dictionary words (loaded on demand, then offline).
  const nowText = showNow && focus >= 0 ? cues[focus]?.text : undefined;
  const words = useWords(nowText);

  return (
    <section className="watch" aria-labelledby="watch-title">
      <div className="section-heading">
        <div>
          <h2 id="watch-title">Watch and sing</h2>
          <p>
            Your own episode or song, with its Chinese subtitles (.srt, .vtt) or
            lyrics (.lrc). Files stay on this device.
          </p>
        </div>
        <div className="watch-files">
          <label className="button secondary file-button">
            <UploadSimple />{" "}
            {media ? "Change video or song" : "Open a video or song"}
            <input
              type="file"
              accept="video/*,audio/*"
              onChange={(e) => {
                const f = e.target.files?.[0];
                if (!f) return;
                setMedia({
                  url: URL.createObjectURL(f),
                  name: f.name,
                  kind: f.type.startsWith("audio") ? "audio" : "video",
                });
                setCues([]);
                setCapName("");
                setTime(0);
                setTapped(null);
                lastT.current = 0;
                lastIdx.current = -1;
                setError("");
                restart();
              }}
            />
          </label>
          <label className="button secondary file-button">
            {capName ? "Change subtitles" : "Add subtitles or lyrics"}
            <input
              type="file"
              accept=".srt,.vtt,.lrc,.txt"
              onChange={async (e) => {
                const f = e.target.files?.[0];
                if (!f) return;
                try {
                  const parsed = parseCaptions(f.name, await f.text());
                  setCues(parsed);
                  lastIdx.current = -1;
                  setTapped(null);
                  setCapName(f.name);
                  setError(
                    parsed.length
                      ? ""
                      : "No timed lines found. Use an .srt, .vtt or .lrc file with timings.",
                  );
                  restart();
                } catch {
                  setError("That file couldn't be read.");
                }
              }}
            />
          </label>
        </div>
      </div>

      <div className="watch-rungs" role="radiogroup" aria-label="How much help">
        {rungs.map((r, i) => (
          <button
            key={r.id}
            role="radio"
            aria-checked={rung === r.id}
            className={rung === r.id ? "is-on" : ""}
            onClick={() => setRung(r.id)}
          >
            <span className="rung-step tabular">{i + 1}</span>
            <span>
              <strong>{r.title}</strong>
              <small>{r.hint}</small>
            </span>
          </button>
        ))}
      </div>

      {error && (
        <p className="inline-error" role="alert">
          {error}
        </p>
      )}

      {media ? (
        <div className={`watch-stage ${media.kind}`}>
          {media.kind === "video" ? (
            <video
              ref={el}
              src={media.url}
              controls
              playsInline
              onTimeUpdate={(e) => onTime(e.currentTarget)}
            />
          ) : (
            <div className="watch-audio">
              <MusicNotes size={28} />
              <span>{media.name}</span>
              <audio
                ref={el}
                src={media.url}
                controls
                onTimeUpdate={(e) => onTime(e.currentTarget)}
              />
            </div>
          )}

          {cues.length > 0 && (
            <div className={`watch-text rung-${rung}`} aria-live="off">
              {rung === "subtitles" && line(focus - 1, "prev")}
              {showNow && nowText ? (
                <TappableLine
                  className="watch-line now"
                  line={nowText}
                  tokens={words.tokens}
                  active={tapped?.line === nowText ? tapped.token : null}
                  onTap={(token) => {
                    // Looking a word up pauses the scene so you can read the card.
                    el.current?.pause();
                    setTapped({ token, line: nowText });
                    setLookups((n) => n + 1);
                  }}
                />
              ) : rung === "peek" ? (
                <button
                  className="watch-peek"
                  onClick={peek}
                  disabled={focus < 0}
                >
                  <Eye size={18} /> Peek at this line <kbd>P</kbd>
                </button>
              ) : (
                <p className="watch-line hidden">
                  Line {Math.max(focus + 1, 0)} of {cues.length}
                </p>
              )}
              {rung === "subtitles" && line(focus + 1, "next")}
              {words.error && <p className="small muted">{words.error}</p>}
              {tapped && (
                <WordCard
                  token={tapped.token}
                  line={tapped.line}
                  source={media.name}
                  voiceURI={profile.voiceURI}
                  onClose={() => setTapped(null)}
                />
              )}
            </div>
          )}

          <div className="watch-controls">
            <button
              className="icon-button"
              aria-label="Previous line"
              disabled={!cues.length}
              onClick={() => seek(Math.max(0, focus - 1))}
            >
              <CaretLeft size={20} />
            </button>
            <button
              className="button secondary"
              disabled={!cues.length || focus < 0}
              onClick={() => seek(focus)}
            >
              <ArrowCounterClockwise size={18} /> Replay line
            </button>
            <button
              className="icon-button"
              aria-label="Next line"
              disabled={!cues.length}
              onClick={() => seek(Math.min(cues.length - 1, focus + 1))}
            >
              <CaretRight size={20} />
            </button>
            <button
              className="chip-toggle"
              aria-pressed={loopLine}
              disabled={!cues.length}
              onClick={() => setLoopLine(!loopLine)}
            >
              <Repeat size={16} /> Loop line
            </button>
            <button
              className="chip-toggle"
              aria-pressed={slow}
              onClick={() => setSlow(!slow)}
            >
              0.75×
            </button>
            <button
              className="chip-toggle"
              disabled={!cues.length || focus < 0}
              onClick={() => void saveLine()}
            >
              <Star size={16} /> Save line
            </button>
            <span className="watch-keys small">
              R replay · P peek · S save · ← →
            </span>
          </div>

          {noteFor && (
            <label className="field watch-note">
              Note for the saved line (optional)
              <input
                autoFocus
                placeholder="What it means, or why you saved it"
                onKeyDown={(e) => e.key === "Enter" && setNoteFor(null)}
                onChange={(e) =>
                  void db.savedLines.update(noteFor, { note: e.target.value })
                }
                onBlur={() => setNoteFor(null)}
              />
            </label>
          )}

          <div className="watch-footer">
            <span className="small tabular">
              {mmss(played.current)} played · {peeked.size}{" "}
              {peeked.size === 1 ? "peek" : "peeks"} · {lookups}{" "}
              {lookups === 1 ? "look-up" : "look-ups"}
            </span>
            {!summary && (
              <button className="button" onClick={() => void finish()}>
                End session
              </button>
            )}
          </div>
          {summary && (
            <div className="watch-summary" role="status">
              <h3>
                {summary.seconds < 10
                  ? "Session finished."
                  : isLyrics
                    ? "Song done."
                    : "Session saved."}
              </h3>
              <p>
                {mmss(summary.seconds)} on “
                {rungs.find((r) => r.id === summary.rung)?.title}”,{" "}
                {summary.lines} lines, {summary.peeks}{" "}
                {summary.peeks === 1 ? "peek" : "peeks"} and {summary.lookups}{" "}
                {summary.lookups === 1 ? "look-up" : "look-ups"}
                {summary.seconds >= 60 &&
                  ` (${((summary.peeks * 600) / summary.seconds).toFixed(1)} peeks per 10 minutes)`}
                .
              </p>
              <p className="small">
                Peeks and look-ups show how much help you needed. They aren't a
                score: you can miss a scene without peeking.
              </p>
              {summary.rung !== "subtitles" && heardLines.size > 0 && (
                <details>
                  <summary>See the lines you heard</summary>
                  <ol className="watch-heard" lang="zh-CN">
                    {[...heardLines]
                      .sort((a, b) => a - b)
                      .map((i) => (
                        <li key={i}>
                          <span className="tabular small">
                            {mmss(cues[i].start)}
                          </span>{" "}
                          {cues[i].text}
                        </li>
                      ))}
                  </ol>
                </details>
              )}
              <button className="text-button" onClick={restart}>
                Start another session
              </button>
            </div>
          )}
        </div>
      ) : (
        <div className="watch-empty">
          <FilmStrip size={28} />
          <p>
            Open an episode or a song you own, then add its Chinese subtitle or
            lyric file. Lyrics (.lrc) turn this into karaoke: the current line
            lights up so you can read ahead and sing.
          </p>
        </div>
      )}

      {history.length > 0 && (
        <div className="watch-history">
          <h3>Recent sessions</h3>
          <table>
            <thead>
              <tr>
                <th scope="col">When</th>
                <th scope="col">What</th>
                <th scope="col">Rung</th>
                <th scope="col">Time</th>
                <th scope="col">Peeks / 10 min</th>
              </tr>
            </thead>
            <tbody>
              {history.map((h) => (
                <tr key={h.id}>
                  <td>
                    {new Date(h.at).toLocaleDateString(undefined, {
                      month: "short",
                      day: "numeric",
                    })}
                  </td>
                  <td className="watch-src">{h.source}</td>
                  <td>{rungs.find((r) => r.id === h.rung)?.title}</td>
                  <td className="tabular">{mmss(h.seconds)}</td>
                  <td className="tabular">
                    {h.rung === "peek" && h.seconds >= 60
                      ? ((h.peeks * 600) / h.seconds).toFixed(1)
                      : "–"}
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      )}

      {saved.length > 0 && <SavedLines lines={saved} />}
      <SavedWords />
    </section>
  );

  function onTime(m: HTMLMediaElement) {
    const t = m.currentTime;
    const dt = t - lastT.current;
    if (dt > 0 && dt < 1.5 && !m.paused) played.current += dt;
    lastT.current = t;
    const i = cueAt(cues, t);
    if (i >= 0 && !heardLines.has(i)) setHeardLines((s) => new Set(s).add(i));
    if (loopLine && focus >= 0 && t >= cues[focus].end - 0.05)
      m.currentTime = cues[focus].start + 0.01;
    setTime(t);
  }
}

/** Words saved from the dictionary card, with an Anki export. */
function SavedWords() {
  const words = useLiveQuery(() => db.personalWords.orderBy("at").reverse().toArray()) ?? [];
  if (!words.length) return null;
  const exportAnki = () => {
    // Front: word. Back: pinyin · meaning · the line it came from.
    const tsv = words
      .map((w) => [w.id, `${w.pinyin} · ${w.meaning}${w.line ? ` · ${w.line}` : ""}`].map((f) => f.replace(/[\t\n]/g, " ")).join("\t"))
      .join("\n");
    const url = URL.createObjectURL(new Blob([tsv], { type: "text/tab-separated-values" }));
    const a = document.createElement("a");
    a.href = url;
    a.download = `kiyo-saved-words-${new Date().toISOString().slice(0, 10)}.txt`;
    a.click();
    setTimeout(() => URL.revokeObjectURL(url), 1000);
  };
  return (
    <div className="watch-saved">
      <div className="section-heading">
        <h3>Saved words</h3>
        <button className="button secondary" onClick={exportAnki}>
          <DownloadSimple size={18} /> Export for Anki
        </button>
      </div>
      <ul>
        {words.map((w) => (
          <li key={w.id}>
            <span className="saved-text" lang="zh-CN">
              {w.id} <span className="saved-py">{w.pinyin}</span>
            </span>
            <span className="saved-note">{w.meaning}</span>
            {w.line && (
              <span className="saved-src small" lang="zh-CN">
                {w.line}
              </span>
            )}
            <button className="icon-button" aria-label={`Delete saved word ${w.id}`} onClick={() => void db.personalWords.delete(w.id)}>
              <Trash size={16} />
            </button>
          </li>
        ))}
      </ul>
    </div>
  );
}

function SavedLines({
  lines,
}: {
  lines: {
    id: string;
    text: string;
    note: string;
    source: string;
    start: number;
  }[];
}) {
  const exportAnki = () => {
    // Tab-separated: Front, Back. In Anki: File → Import, "Fields separated by: Tab".
    const tsv = lines
      .map((l) =>
        [
          l.text,
          [l.note, `${l.source} ${mmss(l.start)}`].filter(Boolean).join(" · "),
        ]
          .map((f) => f.replace(/[\t\n]/g, " "))
          .join("\t"),
      )
      .join("\n");
    const url = URL.createObjectURL(
      new Blob([tsv], { type: "text/tab-separated-values" }),
    );
    const a = document.createElement("a");
    a.href = url;
    a.download = `kiyo-saved-lines-${new Date().toISOString().slice(0, 10)}.txt`;
    a.click();
    setTimeout(() => URL.revokeObjectURL(url), 1000);
  };
  return (
    <div className="watch-saved">
      <div className="section-heading">
        <h3>Saved lines</h3>
        <button className="button secondary" onClick={exportAnki}>
          <DownloadSimple size={18} /> Export for Anki
        </button>
      </div>
      <ul>
        {lines.map((l) => (
          <li key={l.id}>
            <span className="saved-text" lang="zh-CN">
              {l.text}
            </span>
            {l.note && <span className="saved-note">{l.note}</span>}
            <span className="saved-src small">
              {l.source} · {mmss(l.start)}
            </span>
            <button
              className="icon-button"
              aria-label={`Delete saved line ${l.text}`}
              onClick={() => void db.savedLines.delete(l.id)}
            >
              <Trash size={16} />
            </button>
          </li>
        ))}
      </ul>
    </div>
  );
}

/** The honest route from the course to watching and singing without help. */
export function ReadingRoute() {
  const sessions = useLiveQuery(() => db.sessions.toArray()) ?? [];
  // HSK 1 units are whatever packs target HSK level 1; the count grows as units are added.
  const hsk1 = useMemo(() => packUnits.filter((u) => u.hskTarget?.level === 1).map((u) => u.id), []);
  const units = useMemo(() => {
    const done = new Set(sessions.map((s) => s.lessonId));
    return hsk1.filter((id) => done.has(id)).length;
  }, [sessions, hsk1]);
  const here = hsk1.length && units >= hsk1.length ? 1 : 0;
  const stages = [
    {
      name: "Foundation",
      level: "HSK 1 · 500 words, 300 characters",
      watch:
        "Short clips you already know, Chinese subtitles on, 0.75×. Slow songs with lyrics.",
      how: "One line at a time: hear it, read it, replay it.",
      next: `Finish the ${hsk1.length} HSK 1 units (${units} of ${hsk1.length} so far).`,
    },
    {
      name: "Subtitle reader",
      level: "HSK 2 · about 1,270 words, 600 characters",
      watch:
        "Slice-of-life dramas and vlogs with Chinese subtitles at normal speed.",
      how: "Pause less. Look up only words that keep coming back; save those lines.",
      next: "A whole episode with fewer than 10 look-ups.",
    },
    {
      name: "Reading at speed",
      level: "HSK 3 · about 2,250 words, 900 characters",
      watch:
        "The same kind of shows, subtitles on, no pausing. Sing familiar songs from the hanzi lyrics.",
      how: "Let the line go when it goes; catch the next one.",
      next: "Three episodes in a row without pausing to read, and one full song from hanzi.",
    },
    {
      name: "Ears first",
      level: "HSK 4 · about 3,250 words, 1,200 characters",
      watch: "Rewatch scenes on “Peek when stuck”, then check with subtitles.",
      how: "Guess from sound and context before you peek.",
      next: "Under 10 peeks per 10 minutes on a show you know, checked afterwards.",
    },
    {
      name: "Without subtitles",
      level: "HSK 5–6 · about 4,300–5,450 words",
      watch:
        "New episodes in a genre you know, no subtitles; check the lines you missed after.",
      how: "Follow the story; let unknown words pass.",
      next: "Explain a new episode's plot, then confirm it with the subtitles.",
    },
    {
      name: "Native ease",
      level: "HSK 7–9 · about 11,000 words, 3,000 characters",
      watch: "Variety shows, fast talk, period dramas; new songs by ear.",
      how: "Daily, for years. This is the long part.",
      next: "",
    },
  ];
  return (
    <section className="route" aria-labelledby="route-title">
      <h2 id="route-title">The route to watching and singing without help</h2>
      <p className="route-honest">
        Most Chinese shows and karaoke screens have Chinese text on them, so
        reading fast comes first and pays off early. Following shows with no
        text at all is HSK 5–6 territory: years of daily study, not weeks.
      </p>
      <ol className="route-stages">
        {stages.map((s, i) => (
          <li
            key={s.name}
            className={i === here ? "is-here" : i < here ? "is-done" : ""}
          >
            <span className="route-num tabular">{i + 1}</span>
            <div>
              <p className="route-name">
                {s.name}{" "}
                {i === here && <span className="route-here">You are here</span>}
              </p>
              <p className="small">{s.level}</p>
              {i === here && (
                <dl className="route-detail">
                  <div>
                    <dt>Watch</dt>
                    <dd>{s.watch}</dd>
                  </div>
                  <div>
                    <dt>How</dt>
                    <dd>{s.how}</dd>
                  </div>
                  {s.next && (
                    <div>
                      <dt>Move on when</dt>
                      <dd>{s.next}</dd>
                    </div>
                  )}
                </dl>
              )}
            </div>
          </li>
        ))}
      </ol>
      <p className="small muted">
        Word and character counts are the cumulative HSK 3.0 targets. Kiyo's own
        course currently reaches HSK 1; the later stages lean on your own shows
        and songs until more units are written.
      </p>
    </section>
  );
}
