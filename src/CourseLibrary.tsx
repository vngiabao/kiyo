import { useState } from "react";
import { useLiveQuery } from "dexie-react-hooks";
import { db } from "./db";
import { lessons, packUnits, readingLessons } from "./content";
import { Arrow } from "./components";

type Entry = { id: string; title: string; detail: string; open: () => void };
export default function CourseLibrary({ onLesson, onReading, onSpeak }: {
  onLesson: (id: string) => void;
  onReading: (id: string) => void;
  onSpeak: (id: string) => void;
}) {
  const sessions = useLiveQuery(() => db.sessions.toArray()) ?? [];
  const done = new Set(sessions.map((s) => s.lessonId));
  const [level, setLevel] = useState("all");
  const [status, setStatus] = useState("all");
  const [query, setQuery] = useState("");
  const foundation = [readingLessons, lessons].map((rows, i) => ({
    id: `foundation-${i}`, level: "foundation", title: i ? "First conversations" : "Characters & first readings",
    detail: "Start here, or return for review.", preparation: "", entries: rows.map((l): Entry => ({
      id: l.id, title: l.title, detail: `${l.minutes} min suggested pace`, open: () => onLesson(l.id),
    })),
  }));
  const units = [...foundation, ...packUnits.map((u) => ({
    id: u.id, level: u.hskTarget ? String(u.hskTarget.level) : "foundation", title: u.title,
    detail: `${u.titleZh} · ${u.canDo.join(" · ")}`,
    preparation: [...new Set((u.prerequisites ?? []).map((id) => packUnits.find((p) => p.id === id || p.lessons.some((l) => l.id === id))?.title).filter(Boolean))].join(" · "),
    entries: [
      ...u.lessons.map((l): Entry => ({ id: l.id, title: l.packPart === "words" ? "New words" : "Grammar & usage",
        detail: `${l.phrases.length} items · ${l.minutes} min suggested pace`, open: () => onLesson(l.id) })),
      ...u.texts.map((t): Entry => ({ id: `read:${t.id}`, title: `Read: ${t.title}`, detail: t.titleZh, open: () => onReading(t.id) })),
      ...(u.scenario ? [{ id: `conversation:${u.scenario.id}`, title: `Role-play: ${u.scenario.title}`,
        detail: u.scenario.place, open: () => onSpeak(u.scenario!.id) }] : []),
    ],
  }))];
  const needle = query.trim().toLocaleLowerCase();
  const visible = units.filter((u) => level === "all" || u.level === level).map((u) => ({ ...u,
    entries: u.entries.filter((e) => (status === "all" || (status === "finished") === done.has(e.id)) &&
      (!needle || `${u.title} ${u.detail} ${e.title} ${e.detail}`.toLocaleLowerCase().includes(needle))),
  })).filter((u) => u.entries.length);
  const count = units.reduce((n, u) => n + u.entries.length, 0);
  const completed = units.reduce((n, u) => n + u.entries.filter((e) => done.has(e.id)).length, 0);
  return <div className="course-library">
    <header className="page-head">
      <h1>Course library.</h1>
      <p className="lede">Characters, everyday exchanges, songs and drama scenes. Choose a level, then open a lesson.</p>
      <p className="small">{packUnits.length} course units · {count} lessons and activities · {completed} finished</p>
      <p className="small muted">Course levels describe the material, not your HSK readiness. The suggested order is a guide; you can revisit any lesson.</p>
    </header>
    <div className="library-filters">
      <div className="field"><label htmlFor="library-level">Level</label><select id="library-level" value={level} onChange={(e) => setLevel(e.target.value)}>
        <option value="all">All levels</option><option value="foundation">Foundation</option>
        {[1, 2, 3, 4, 5, 6].filter((n) => packUnits.some((u) => u.hskTarget?.level === n)).map((n) => <option key={n} value={n}>HSK {n}</option>)}
      </select></div>
      <div className="field"><label htmlFor="library-status">Show activities</label><select id="library-status" value={status} onChange={(e) => setStatus(e.target.value)}>
        <option value="all">All activities</option><option value="unfinished">Not finished</option><option value="finished">Finished</option>
      </select></div>
      <div className="field"><label htmlFor="library-search">Find a lesson</label><input id="library-search" type="search" value={query} onChange={(e) => setQuery(e.target.value)} placeholder="Topic or title" /></div>
    </div>
    <p className="small" role="status">{visible.length} matching units or foundation groups</p>
    {visible.length === 0 && <p>No activities match these filters. Try another level or search.</p>}
    {["foundation", "1", "2", "3", "4", "5", "6"].filter((n) => visible.some((u) => u.level === n)).map((n) => <details
      className="library-level" key={`${n}-${level}-${needle ? "search" : "browse"}`} open={n === "foundation" || level === n || Boolean(needle)}>
      <summary><h2>{n === "foundation" ? "Foundation" : `HSK ${n}`}</h2></summary>
      {visible.filter((u) => u.level === n).map((u) => <details className="library-unit" key={u.id} open={needle ? true : undefined}>
      <summary><span>{u.title}</span><small>{u.level === "foundation" ? "Foundation" : `HSK ${u.level}`} · {u.entries.length} activities</small></summary>
      <p className="small muted">{u.detail}</p>
      {u.preparation && <p className="small">Suggested preparation: {u.preparation}.</p>}
      <ul className="library-entries">{u.entries.map((e) => <li key={e.id}>
        <div><h3>{e.title}</h3><p className="small muted">{e.detail}</p>{done.has(e.id) && <span className="small">Finished</span>}</div>
        <button className="text-button" aria-label={`Open ${e.title}`} onClick={e.open}>Open <Arrow /></button>
      </li>)}</ul>
    </details>)}
    </details>)}
    <p className="small content-note">Original course drafts · native educator review pending.</p>
  </div>;
}
