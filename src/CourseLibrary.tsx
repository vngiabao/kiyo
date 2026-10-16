import { useRef, useState } from "react";
import { gsap, quiet, reducedMotion, useGSAP } from "./motion";
import { useLiveQuery } from "dexie-react-hooks";
import { CaretRight, Check } from "@phosphor-icons/react";
import { db } from "./db";
import { lessons, packUnits, readingLessons } from "./content";
import { Arrow } from "./components";

type Kind = "words" | "grammar" | "read" | "speak";
type Entry = { id: string; kind: Kind; title: string; detail: string; meta: string; open: () => void };
type Unit = { id: string; level: string; title: string; titleZh?: string; detail: string; preparation: string; entries: Entry[] };

const levels = ["foundation", "1", "2", "3", "4", "5", "6"];
const levelNames: Record<string, [string, string]> = {
  foundation: ["Foundation", "Characters, first readings and first conversations."],
  "1": ["HSK 1", "Hello, names, numbers and friends."],
  "2": ["HSK 2", "Everyday life: plans, food, places."],
  "3": ["HSK 3", "Tell your story and follow a longer one."],
  "4": ["HSK 4", "Media and social life at real pace."],
  "5": ["HSK 5", "Opinions, nuance and longer reading."],
  "6": ["HSK 6", "Native pace: drama, songs and group chat."],
};
const shortName = (l: string) => (l === "foundation" ? "Foundation" : `HSK ${l}`);
const action: Record<Kind, string> = { words: "Open", grammar: "Open", read: "Read", speak: "Speak" };

export default function CourseLibrary({ onLesson, onReading, onSpeak }: {
  onLesson: (id: string) => void;
  onReading: (id: string) => void;
  onSpeak: (id: string) => void;
}) {
  const sessions = useLiveQuery(() => db.sessions.toArray()) ?? [];
  const done = new Set(sessions.map((s) => s.lessonId));
  const [filter, setFilter] = useState("all");
  const [query, setQuery] = useState("");
  // Sections the learner opened or closed by hand; the rest follow progress.
  const [toggled, setToggled] = useState<Record<string, boolean>>({});
  const foundation: Unit[] = [readingLessons, lessons].map((rows, i) => ({
    id: `foundation-${i}`, level: "foundation", title: i ? "First conversations" : "Characters & first readings",
    detail: "Start here, or return for review.", preparation: "", entries: rows.map((l): Entry => ({
      id: l.id, kind: "words", title: l.title, detail: "", meta: `${l.minutes} min suggested pace`, open: () => onLesson(l.id),
    })),
  }));
  const units: Unit[] = [...foundation, ...packUnits.map((u): Unit => ({
    id: u.id, level: u.hskTarget ? String(u.hskTarget.level) : "foundation", title: u.title, titleZh: u.titleZh,
    detail: u.canDo.join(" · "),
    preparation: [...new Set((u.prerequisites ?? []).map((id) => packUnits.find((p) => p.id === id || p.lessons.some((l) => l.id === id))?.title).filter(Boolean))].join(" · "),
    entries: [
      ...u.lessons.map((l): Entry => ({
        id: l.id, kind: l.packPart === "words" ? "words" : "grammar", title: l.packPart === "words" ? "New words" : "Grammar & usage",
        detail: "", meta: `${l.phrases.length} items · ${l.minutes} min suggested pace`, open: () => onLesson(l.id),
      })),
      ...u.texts.map((t): Entry => ({
        id: `read:${t.id}`, kind: "read", title: t.id.endsWith("-d") ? `Dialogue: ${t.title}` : `Read: ${t.title}`,
        detail: t.titleZh, meta: "", open: () => onReading(t.id),
      })),
      ...(u.scenario ? [{ id: `conversation:${u.scenario.id}`, kind: "speak" as Kind, title: `Role-play: ${u.scenario.title}`,
        detail: u.scenario.place, meta: "", open: () => onSpeak(u.scenario!.id) }] : []),
    ],
  }))];
  const currentLevel = units.find((u) => u.entries.some((e) => !done.has(e.id)))?.level ?? "foundation";
  const needle = query.trim().toLocaleLowerCase();
  const shows = (u: Unit, e: Entry) =>
    (filter === "all" || levels.includes(filter) || filter === e.kind || (filter === "unfinished" && !done.has(e.id))) &&
    (!needle || `${u.title} ${u.titleZh ?? ""} ${u.detail} ${e.title} ${e.detail}`.toLocaleLowerCase().includes(needle));
  const visible = units
    .filter((u) => !levels.includes(filter) || u.level === filter)
    .map((u) => ({ ...u, entries: u.entries.filter((e) => shows(u, e)) }))
    .filter((u) => u.entries.length);
  const count = units.reduce((n, u) => n + u.entries.length, 0);
  const completed = units.reduce((n, u) => n + u.entries.filter((e) => done.has(e.id)).length, 0);
  const isOpen = (level: string) =>
    toggled[level] ?? (level === "foundation" || level === currentLevel || filter === level || Boolean(needle));
  const root = useRef<HTMLDivElement>(null);
  // The path board fills in like a progress report: stops rise, then each bar draws to its value.
  useGSAP(
    () => {
      if (reducedMotion()) return;
      gsap.timeline()
        .from(quiet(root.current!.querySelectorAll(".path-stop")), { y: 12, opacity: 0, stagger: 0.05, duration: 0.35, clearProps: "transform,opacity,visibility,transition" })
        .from(".path-bar > span", { scaleX: 0, transformOrigin: "left center", stagger: 0.05, duration: 0.6, ease: "power2.out", clearProps: "transform" }, "-=0.2");
    },
    { scope: root },
  );
  const goTo = (level: string) => {
    setFilter(level);
    setToggled((t) => ({ ...t, [level]: true }));
    requestAnimationFrame(() =>
      document.getElementById(`level-${level}`)?.scrollIntoView({
        behavior: matchMedia("(prefers-reduced-motion: reduce)").matches ? "auto" : "smooth",
        block: "start",
      }),
    );
  };
  return <div className="course-library" ref={root}>
    <header className="page-head">
      <h1>Course library.</h1>
      <p className="lede">Characters, everyday exchanges, songs and drama scenes. Choose a level, then open a lesson.</p>
    </header>
    {/* The path at a glance: one stop per level, progress under each, the current one marked. */}
    <nav className="path-board" aria-label="Your path through the course">
      {levels.filter((l) => units.some((u) => u.level === l)).map((level) => {
        const all = units.filter((u) => u.level === level).flatMap((u) => u.entries);
        const n = all.filter((e) => done.has(e.id)).length;
        const complete = all.length > 0 && n === all.length;
        return (
          <button
            key={level}
            className={`path-stop ${level === currentLevel ? "is-current" : ""} ${complete ? "is-done" : ""}`}
            aria-current={level === currentLevel ? "step" : undefined}
            onClick={() => goTo(level)}
          >
            <span className="path-label">
              {shortName(level)}
              {complete && <Check size={14} weight="bold" aria-label="complete" />}
            </span>
            <span className="path-bar" aria-hidden>
              <span style={{ width: `${all.length ? (n / all.length) * 100 : 0}%` }} />
            </span>
            <small className="tabular">{n} / {all.length}</small>
          </button>
        );
      })}
    </nav>
    <div className="library-summary">
      <p>
        <strong>{packUnits.length}</strong> course units · <strong>{count}</strong> lessons and activities · {completed} finished
      </p>
      <p className="small muted">Levels describe the material, not your HSK readiness. The order is a guide; revisit anything.</p>
    </div>
    <div className="library-filters">
      <div className="field">
        <label htmlFor="library-filter">Show lessons</label>
        <select id="library-filter" value={filter} onChange={(e) => setFilter(e.target.value)}>
          <option value="all">All lessons</option>
          <option value="unfinished">Not finished yet</option>
          <option value="words">New words</option>
          <option value="grammar">Grammar & usage</option>
          <option value="read">Readings & dialogues</option>
          <option value="speak">Role-plays</option>
          {levels.filter((l) => units.some((u) => u.level === l)).map((l) => (
            <option key={l} value={l}>{shortName(l)}{l === "foundation" ? "" : " course"}</option>
          ))}
        </select>
      </div>
      <div className="field">
        <label htmlFor="library-search">Find a lesson</label>
        <input id="library-search" type="search" value={query} onChange={(e) => setQuery(e.target.value)} placeholder="Topic, title or 中文" />
      </div>
    </div>
    {visible.length === 0 && <p role="status">No lessons match. Try another level or a shorter search.</p>}
    {levels.filter((l) => visible.some((u) => u.level === l)).map((level) => {
      const own = visible.filter((u) => u.level === level);
      const all = units.filter((u) => u.level === level).flatMap((u) => u.entries);
      const n = all.filter((e) => done.has(e.id)).length;
      return (
        <details
          className="course-level"
          id={`level-${level}`}
          key={`${level}-${filter}-${needle ? "search" : "browse"}`}
          open={isOpen(level)}
          onToggle={(e) => {
            const open = e.currentTarget.open;
            setToggled((t) => (t[level] === open ? t : { ...t, [level]: open }));
          }}
        >
          <summary>
            <CaretRight size={16} weight="bold" className="level-caret" aria-hidden />
            <h2>{levelNames[level][0]}</h2>
            <span className="level-summary">
              <span>{levelNames[level][1]}</span>
              <small className="tabular">
                {units.filter((u) => u.level === level).length} units · {all.length} lessons · {n} finished
              </small>
            </span>
          </summary>
          {own.map((u) => {
            const finished = u.entries.filter((e) => done.has(e.id)).length;
            return (
              <section className="course-unit" key={u.id}>
                <div className="section-title">
                  <h3>
                    {u.title}
                    {u.titleZh && <span className="unit-zh" lang="zh-CN">{u.titleZh}</span>}
                  </h3>
                  {finished > 0 && (
                    <small className="unit-status tabular">
                      {finished === u.entries.length && <Check size={14} weight="bold" aria-hidden />}
                      {finished} / {u.entries.length} finished
                    </small>
                  )}
                </div>
                <p className="small muted">{u.detail}</p>
                {u.preparation && <p className="small muted">Suggested preparation: {u.preparation}.</p>}
                <div className="course-lessons">
                  {u.entries.map((e) => (
                    <div key={e.id}>
                      <div>
                        <h4>
                          {e.title}
                          {done.has(e.id) && <Check size={16} weight="bold" className="lesson-done" aria-label="finished" />}
                        </h4>
                        {e.detail && <p lang={e.kind === "read" ? "zh-CN" : undefined}>{e.detail}</p>}
                        {e.meta && <small>{e.meta}</small>}
                      </div>
                      <div className="actions">
                        <button className="text-button" aria-label={`${action[e.kind]} ${e.title}`} onClick={e.open}>
                          {action[e.kind]} <Arrow />
                        </button>
                      </div>
                    </div>
                  ))}
                </div>
              </section>
            );
          })}
        </details>
      );
    })}
    <p className="small content-note">Original course drafts · native educator review pending.</p>
  </div>;
}
