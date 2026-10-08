import { useEffect, useState } from "react";
import { useLiveQuery } from "dexie-react-hooks";
import {
  ArrowLeft,
  ArrowUpRight,
  Check,
  Lock,
  Timer,
  DownloadSimple,
} from "@phosphor-icons/react";
import { AudioButton, Pinyin } from "./components";
import { MoSays } from "./Mascot";
import HskExam from "./HskExam";
import { hskRoadmap, roadmapFor } from "./hsk-roadmap";
import { hskDB, changeHskSettings, exportHsk, importHsk } from "./hsk-db";
import {
  defaultHskSettings,
  gradeRun,
  hskSpeech,
  hskStudyWords,
  hskParticleContext,
  hskItems,
  hskItemById,
  hskSources,
  hskUnits,
  hskUnitsFor,
  hskEntryFor,
  makeRun,
  makeBankRun,
  hasHskBank,
  officialPaper,
  sourceSteps,
  sourceStepsFor,
  teacherLines,
  unitPassed,
  unitUnlocked,
  unresolvedItems,
  type HskEdition,
  type HskRun,
} from "./hsk-model";
import "./hsk.css";

const External = ({
  href,
  children,
}: {
  href: string;
  children: React.ReactNode;
}) => (
  <a href={href} target="_blank" rel="noreferrer">
    {children}
    <ArrowUpRight size={16} aria-label="opens in a new tab" />
  </a>
);

export default function Hsk({
  onLesson,
  onFocus,
}: {
  onLesson: (id: string) => void;
  onFocus: (focused: boolean) => void;
}) {
  const settings = useLiveQuery(() => hskDB.settings.get("learner"), []);
  const runs = useLiveQuery(
    () => hskDB.runs.orderBy("startedAt").reverse().toArray(),
    [],
  );
  const s = settings ?? defaultHskSettings;
  const bank = hasHskBank(s.level);
  const practiceAvailable = s.level === 1 || bank;
  const studyKey = (unit: string) => s.level === 1 ? unit : `${s.level}:${unit}`;
  const plan = roadmapFor(s.level);
  const units = hskUnitsFor(s.level);
  const levelSteps = sourceStepsFor(s.level);
  const selectLevel = (level: number) =>
    changeHskSettings({
      level,
      ...(level >= 7 ? { edition: "3.0" as const } : {}),
    });
  const [tab, setTab] = useState("path"),
    [study, setStudy] = useState<string | null>(null),
    [active, setActive] = useState<string | null>(null),
    [busy, setBusy] = useState(false),
    [error, setError] = useState(""),
    [message, setMessage] = useState("");
  useEffect(() => {
    onFocus(!!active);
    return () => onFocus(false);
  }, [active, onFocus]);
  useEffect(() => {
    window.scrollTo(0, 0);
  }, [active, study, tab]);
  const act = async (fn: () => Promise<unknown>) => {
    setBusy(true);
    setError("");
    try {
      await fn();
    } catch (e) {
      setError(
        e instanceof Error ? e.message : "Could not save. Please try again.",
      );
    } finally {
      setBusy(false);
    }
  };
  if (!runs) return <p role="status">Opening your HSK notebook…</p>;
  const start = (unit: HskRun["unit"], ids?: string[]) =>
    void act(async () => {
      const r = bank
        ? makeBankRun(unit, s.level as 1 | 2 | 3 | 4 | 5 | 6, runs, ids)
        : makeRun(unit, ids);
      await hskDB.runs.add(r);
      setActive(r.id);
    });
  if (active) return <HskExam id={active} onExit={() => setActive(null)} />;
  const completed = hskUnits.filter((u) => unitPassed(u.id, runs, s.level)).length;
  const unfinished = runs.find((r) => !r.finishedAt && (r.level ?? 1) === s.level);
  const mistakes = unresolvedItems(runs, s.level);
  const sourceKey = `${s.edition}:${s.level}:`;
  const sourceCount = sourceSteps.filter((t) =>
    s.sourceDone.includes(sourceKey + t.id),
  ).length;
  const next = units.find((u) => !unitPassed(u.id, runs, s.level));
  if (study) {
    const unit = units.find((u) => u.id === study)!;
    const items = hskItems.filter((q) => q.unit === study && q.level === s.level);
    const words = hskStudyWords(items);
    return (
      <section className="hsk-study">
        <button className="text-button" onClick={() => setStudy(null)}>
          <ArrowLeft /> Back to HSK
        </button>
        <h1>{unit.title}</h1>
        <p>
          {unit.description} Read the examples, then close the notes for your
          checkpoint.
        </p>
        {words.length > 0 && <><h2>Words in this checkpoint</h2>
        <dl className="hsk-word-bank">
          {words.map((w) => (
            <div key={w.zh}>
              <dt lang="zh-CN">{w.zh}</dt>
              <dd>
                <Pinyin text={w.py} />
                {w.en}
                <AudioButton
                  text={hskSpeech(w.zh)}
                  mood="clear"
                  label={`Hear ${hskSpeech(w.zh)}`}
                />
                {hskParticleContext[w.zh] && (
                  <p className="hsk-word-context muted">
                    <span>Neutral tone in a phrase:</span>
                    <span lang="zh-CN">{hskParticleContext[w.zh].zh}</span>
                    <Pinyin text={hskParticleContext[w.zh].py} />
                    <span>{hskParticleContext[w.zh].en}</span>
                  </p>
                )}
              </dd>
            </div>
          ))}
        </dl></>}
        <h2>Read in context</h2>
        <div className="hsk-study-lines">
          {items.map((q) => (
            <article key={q.id}>
              <p lang="zh-CN">{q.sentence}</p>
              <Pinyin text={q.py} />
              <p>{q.en}</p>
              <p className="muted">{q.explanation}</p>
              <AudioButton
                text={q.sentence}
                mood="clear"
                label="Hear sentence"
              />
            </article>
          ))}
        </div>
        {error && <p role="alert">{error}</p>}
        <button
          className="button"
          disabled={busy}
          onClick={() =>
            void act(async () => {
              await changeHskSettings({
                studied: [...new Set([...s.studied, studyKey(study)])],
              });
              setStudy(null);
            })
          }
        >
          I’ve studied these · unlock the checkpoint
        </button>
        <p className="muted">
          Studying is self-reported. Passing the checkpoint requires an unaided
          result.
        </p>
      </section>
    );
  }
  return (
    <section className="hsk-home">
      <header className="hsk-intro">
        <div>
          <h1>HSK study room.</h1>
          <p className="hsk-deck">Learn it. Prove it. Move on.</p>
          <p>
            A deliberate path through source material, skill checkpoints and
            timed practice.
          </p>
        </div>
        <MoSays state="teacher" say={teacherLines.start} size={220} />
        <button
          className="button hsk-quick-start"
          onClick={() =>
            unfinished
              ? setActive(unfinished.id)
              : practiceAvailable && next
                ? setStudy(next.id)
                : setTab("sources")
          }
        >
          {unfinished
            ? "Continue saved practice"
            : practiceAvailable && next
              ? `Begin: ${next.title}`
              : "Open your source checklist"}
        </button>
      </header>
      <div className="hsk-target">
        <label>
          Target level
          <select
            aria-label="Target level"
            value={s.level}
            disabled={busy}
            onChange={(e) =>
              void act(() => selectLevel(Number(e.target.value)))
            }
          >
            {hskRoadmap.map((p) => (
              <option key={p.level} value={p.level}>
                {p.label}
              </option>
            ))}
          </select>
        </label>
        <label>
          Exam version
          <select
            aria-label="Exam version"
            value={s.edition}
            disabled={busy || s.level >= 7}
            onChange={(e) =>
              void act(() =>
                changeHskSettings({ edition: e.target.value as HskEdition }),
              )
            }
          >
            <option value="2.0">HSK 2.0 · Standard Course track</option>
            <option value="3.0">HSK 3.0 · new syllabus</option>
          </select>
        </label>
        <p>
          {s.level >= 7
            ? "Levels 7, 8 and 9 are awarded through one combined advanced exam. This route prepares for that shared exam."
            : s.edition === "3.0"
              ? "Use the new official syllabus and samples. Older Standard Course books are supplementary."
              : "The classic six-level track. Confirm the version with your test centre before booking."}
        </p>
      </div>
      <nav className="hsk-tabs" aria-label="HSK sections">
        {[
          ["path", "Study path"],
          ["sources", "Source desk"],
          [
            "mistakes",
            `Mistakes${mistakes.length ? ` (${mistakes.length})` : ""}`,
          ],
        ].map(([id, title]) => (
          <button
            key={id}
            aria-current={tab === id ? "page" : undefined}
            onClick={() => setTab(id)}
          >
            {title}
          </button>
        ))}
      </nav>
      {error && <p role="alert">{error}</p>}
      {message && <p role="status">{message}</p>}
      {unfinished && (
        <div className="hsk-resume">
          <div>
            <strong>
              Unfinished{" "}
              {unfinished.unit === "sample" ? "timed sample" : "checkpoint"}
            </strong>
            <p>
              {unfinished.deadline
                ? "The clock keeps running. Returning after the deadline submits saved answers."
                : "Your saved answers are waiting."}
            </p>
          </div>
          <button
            className="button secondary"
            onClick={() => setActive(unfinished.id)}
          >
            Resume practice
          </button>
        </div>
      )}
      {tab === "path" && (
        <div className="hsk-path-layout">
          <div>
            <details className="hsk-roadmap">
              <summary>Full route · HSK 1–9</summary>
              <p className="muted">
                Choose your starting point. Each level follows study →
                correction → official sample → repair. Completion here records
                study, not a certified HSK level.
              </p>
              <ol>
                {hskRoadmap.map((p) => (
                  <li key={p.level}>
                    <button
                      className="text-button"
                      disabled={busy}
                      aria-current={s.level === p.level ? "step" : undefined}
                      onClick={() => void act(() => selectLevel(p.level))}
                    >
                      {p.label} · {p.title}
                    </button>
                    <p>{p.entry}</p>
                    <small>
                      {
                        sourceSteps.filter((t) =>
                          s.sourceDone.includes(
                            `${p.level >= 7 ? "3.0" : s.edition}:${p.level}:${t.id}`,
                          ),
                        ).length
                      }{" "}
                      / 5 source-study steps recorded
                    </small>
                  </li>
                ))}
              </ol>
            </details>
            <div className="hsk-section-heading">
              <h2>
                {practiceAvailable
                  ? `${plan.label} · skill checkpoints`
                  : `${plan.label} · ${plan.title}`}
              </h2>
              <span>
                {practiceAvailable
                  ? `${completed} / 3 checkpoints`
                  : `${sourceCount} / 5 study steps`}
              </span>
            </div>
            <details className="hsk-roadmap">
              <summary>Before {plan.label} · starting skills</summary>
              <p>{plan.entry}</p>
              <ul>{hskEntryFor(s.level).map((skill) => <li key={skill}>{skill}</li>)}</ul>
              <p className="muted">These are Kiyo study recommendations, not official exam eligibility requirements or a placement result. Choose a lower level when the starting skills feel unfamiliar.</p>
              <p>Study words and characters → grammar in context → reading and listening → mixed checkpoints → timed sample → repair. Use the Source desk for your chosen exam’s writing and speaking requirements.</p>
            </details>
            {practiceAvailable ? (
              <>
                <p className="muted">
                  {bank
                    ? `${hskItems.filter((q) => q.level === s.level).length} original questions: 60 checkpoint items and 30 sample items. Each attempt brings unseen items first, then those seen least often. Vocabulary follows the GF2021 inventory; this is adapted practice, not a complete official paper.`
                    : "36 original cloze questions: 24 checkpoint items and 12 sample items. This is foundation practice, not complete exam coverage."}
                </p>
                <ol className="hsk-path">
                  {units.map((u, i) => {
                    const passed = unitPassed(u.id, runs, s.level),
                      unlocked = unitUnlocked(i, runs, s.level),
                      studied = s.studied.includes(studyKey(u.id));
                    return (
                      <li key={u.id}>
                        <span
                          className="hsk-step-number"
                          aria-label={`Step ${i + 1}`}
                        >
                          {passed ? <Check /> : String(i + 1).padStart(2, "0")}
                        </span>
                        <div>
                          <div className="hsk-step-title">
                            <h3>{u.title}</h3>
                            <span className={passed ? "hsk-good" : "muted"}>
                              {passed
                                ? "Cleared"
                                : unlocked
                                  ? "Available"
                                  : "Locked"}
                            </span>
                          </div>
                          {!bank && <><p className="hsk-focus" lang="zh-CN">
                            {u.focus}
                          </p>
                          <Pinyin text={u.focusPy} />
                          <p>{u.description}</p>
                          <p className="muted">{u.book}</p></>}
                          {bank && <p>{u.description} Study the examples, then answer listening, reading, cloze and word-order questions without help.</p>}
                          {unlocked ? (
                            <div className="hsk-row-actions">
                              <button
                                className="button secondary"
                                onClick={() => setStudy(u.id)}
                              >
                                {studied ? "Revisit notes" : "Study the notes"}
                              </button>
                              <button
                                className="button"
                                disabled={!studied || busy || !!unfinished}
                                onClick={() => start(u.id)}
                              >
                                {passed
                                  ? "Retake checkpoint"
                                  : "Take checkpoint"}
                              </button>
                            </div>
                          ) : (
                            <p className="hsk-lock">
                              <Lock size={16} /> Clear the previous checkpoint
                              with at least 80% unaided.
                            </p>
                          )}
                          {unlocked && !studied && (
                            <small>
                              Study the notes first to unlock the {bank ? 10 : 8}-question
                              checkpoint.
                            </small>
                          )}
                        </div>
                      </li>
                    );
                  })}
                </ol>
                <div className="hsk-timed">
                  <Timer size={28} />
                  <div>
                    <h3>{bank ? "A fresh timed selection." : "Reading under pressure."}</h3>
                    <p>
                      {bank ? "12 questions · 12 minutes" : "12 questions · 6 minutes"} · no hints · auto-submit.
                    </p>
                    <p className="muted">
                      A short original sample, not a full official mock. All three
                      checkpoints must be cleared.
                    </p>
                    <button
                      className="button"
                      disabled={completed < 3 || busy || !!unfinished}
                      onClick={() => start("sample")}
                    >
                      Start timed sample
                    </button>
                  </div>
                </div>
                <p className="muted">
                  After the sample, work through the official paper on the
                  Source desk. Your real exam preparation includes the sections
                  required by your chosen level and version.
                </p>
              </>
            ) : (
              <>
                <p className="hsk-entry">
                  <strong>Before this level</strong>
                  <br />
                  {plan.entry}
                </p>
                <p>{plan.focus}</p>
                <p>
                  Higher-level study uses the published sources below. Kiyo does
                  not yet contain a graded {plan.label} question bank.
                </p>
                <SourceChecklist s={s} busy={busy} act={act} />
                <button
                  className="button secondary"
                  onClick={() => setTab("sources")}
                >
                  Open source desk
                </button>
              </>
            )}
          </div>
          <aside className="hsk-aside">
            <h2>Today’s assignment</h2>
            <p>
              {practiceAvailable
                ? next
                  ? `Study ${next.title.toLowerCase()}, then pass its checkpoint without notes.`
                  : "Take the timed reading sample, then review the official paper."
                : levelSteps[Math.min(sourceCount, 4)].detail}
            </p>
            <div className="hsk-aside-rule">
              <h3>The rule is simple.</h3>
              <p>
                80% unaided opens the next checkpoint. Pinyin help is saved as
                support. A book checkbox never becomes a test score.
              </p>
            </div>
            <h3>Study alongside</h3>
            <External
              href={
                s.level >= 7
                  ? hskSources.advanced
                  : s.level === 1
                    ? hskSources.book
                    : hskSources.books
              }
            >
              {s.level >= 7
                ? "CTI’s combined 7–9 guide"
                : `HSK Standard Course ${s.level}${s.level >= 4 ? " A + B" : ""}`}
            </External>
            <p className="muted">
              {s.level >= 7
                ? "Official advanced syllabus and sample tasks. Standard Course covers levels 1–6."
                : "Jiang Liping · BLCUP / CTI. Use your own textbook and workbook; their pages are not bundled here."}
            </p>
            <button className="text-button" onClick={() => setTab("sources")}>
              Syllabus, papers & source checklist <ArrowUpRight />
            </button>
            {s.level === 1 && (
              <button
                className="text-button"
                onClick={() => onLesson("read-1")}
              >
                Need character basics? Start with 一–十.
              </button>
            )}
          </aside>
        </div>
      )}
      {tab === "sources" && (
        <section className="hsk-source-desk">
          <h2>Know what you’re studying from.</h2>
          <p>
            Publisher and exam-provider sources, checked {hskSources.checked}.
            External material opens on its owner’s site and needs internet
            access.
          </p>
          <div className="hsk-source-list">
            <article>
              <h3>Chinese Testing International</h3>
              <p>
                Use the official syllabus for the level and version you will
                sit.
              </p>
              <External
                href={
                  s.level >= 7
                    ? hskSources.advanced
                    : s.edition === "3.0"
                      ? hskSources.syllabus
                      : `https://www.chinesetest.cn/HSK/${s.level}`
                }
              >
                Open syllabus & exam structure
              </External>
              <p className="muted">
                CTI announces the worldwide HSK 3.0 levels 1–6 launch for
                December 13, 2026. Check arrangements with your centre.
              </p>
              <External href={hskSources.announcement}>
                Read the version announcement
              </External>
            </article>
            <article>
              <h3>
                {s.level >= 7
                  ? "Advanced study sequence"
                  : `HSK Standard Course ${s.level}${s.level >= 4 ? " A + B" : ""}`}
              </h3>
              <p>
                {s.level >= 7 ? (
                  plan.work
                ) : (
                  <>
                    The BLCUP / CTI textbook and matching workbook give the
                    study sequence. Level 1 has 15 lessons. For HSK 3.0, use
                    these as a supplement and check syllabus gaps.
                  </>
                )}
              </p>
              <External
                href={
                  s.level >= 7
                    ? hskSources.advanced
                    : s.level === 1
                      ? hskSources.book
                      : hskSources.books
                }
              >
                {s.level >= 7
                  ? "Advanced exam tasks & requirements"
                  : "Publisher’s book & sample pages"}
              </External>
              {s.level === 1 && (
                <External href={hskSources.workbook}>
                  Matching workbook
                </External>
              )}
              <p className="muted">
                Book access may require a purchase. Nothing is purchased or
                connected by Kiyo.
              </p>
            </article>
            <article>
              <h3>
                {plan.label} ·{" "}
                {s.level >= 7
                  ? "combined advanced sample"
                  : s.edition === "3.0"
                    ? "new-version samples"
                    : "paper & answer key"}
              </h3>
              <p>
                {s.level >= 7
                  ? "The official combined sample contains reading, listening, writing, translation and speaking tasks. Some items are omitted; it is not a complete timed paper."
                  : s.edition === "3.0"
                    ? "Download CTI’s sample bundle or try the official demo. Choose your level and follow its instructions."
                    : "Open the official paper and answer key. You can start with its reading section; use the time printed on the paper."}
              </p>
              <External
                href={
                  s.level >= 7
                    ? hskSources.advancedSample
                    : s.edition === "3.0"
                      ? hskSources.samples3
                      : officialPaper(s.level)
                }
              >
                {s.level >= 7
                  ? "Open official 7–9 sample (PDF)"
                  : s.edition === "3.0"
                    ? "Download official sample bundle (ZIP)"
                    : "Open official sample paper (PDF)"}
              </External>
              <External
                href={
                  s.level >= 7
                    ? hskSources.downloads
                    : s.edition === "3.0"
                      ? hskSources.demo3
                      : hskSources.downloads
                }
              >
                {s.level >= 7
                  ? "Official audio & supporting files"
                  : s.edition === "3.0"
                    ? "Try the official HSK 3.0 demo"
                    : "Official audio & more sample papers"}
              </External>
            </article>
          </div>
          <h2>Your source-work checklist</h2>
          <p className="muted">
            Saved separately for {plan.label} · {s.edition}. These are your
            study notes, not verified exam results.
          </p>
          <SourceChecklist s={s} busy={busy} act={act} />
          <details>
            <summary>How Kiyo’s practice was made</summary>
            <p>
              The in-app questions are original AI-assisted Kiyo
              drafts, not copied exam or textbook questions. Mixed banks add listening, reading and adapted word-order practice; they do not reproduce every official section. Vocabulary and
              answer structure are checked by the content-pack pipeline against
              the imported MIT-licensed HSK list. Native-language review is
              still pending. The 2021 HSK vocabulary standard is not treated as
              the 2025/2026 exam syllabus.
            </p>
            <External href="https://github.com/drkameleon/complete-hsk-vocabulary">
              Vocabulary data source
            </External>
          </details>
        </section>
      )}
      {tab === "mistakes" && (
        <section>
          <div className="hsk-section-heading">
            <h2>Work on what missed.</h2>
            <span>{mistakes.length} to revisit</span>
          </div>
          <p>
            {mistakes.length
              ? "Wrong, unanswered and supported answers stay here until you answer them correctly without help in a later practice."
              : "No unresolved practice answers yet. Your checkpoints will put the useful work here."}
          </p>
          {mistakes.length > 0 && (
            <button
              className="button"
              disabled={busy || !!unfinished}
              onClick={() => start("repair", mistakes)}
            >
              Practise these again
            </button>
          )}
          <ul className="hsk-mistakes">
            {mistakes.map((id) => (
              <li key={id}>
                <p lang="zh-CN">{hskItemById[id].sentence}</p>
                <Pinyin text={hskItemById[id].py} />
                <p>{hskItemById[id].explanation}</p>
              </li>
            ))}
          </ul>
          <h2>Practice history</h2>
          {runs.filter((r) => r.finishedAt).length ? (
            <ul className="hsk-history">
              {runs
                .filter((r) => r.finishedAt)
                .map((r) => (
                  <li key={r.id}>
                    <div>
                      <strong>
                        Level {r.level ?? 1} · {r.unit === "sample"
                          ? "Timed reading sample"
                          : r.unit === "repair"
                            ? "Mistake repair"
                            : hskUnits.find((u) => u.id === r.unit)?.title}
                      </strong>
                      <p>
                        {new Date(r.finishedAt!).toLocaleString()} ·{" "}
                        {gradeRun(r).unaided}/{r.itemIds.length} unaided
                      </p>
                    </div>
                    <button
                      className="text-button"
                      onClick={() => setActive(r.id)}
                    >
                      Review answers
                    </button>
                  </li>
                ))}
            </ul>
          ) : (
            <p className="muted">No finished checkpoints yet.</p>
          )}
        </section>
      )}
      <footer className="hsk-footer">
        <p>
          HSK notebook · saved on this device and included in progress backups.
          Cloud sync does not include this notebook.
        </p>
        <div className="hsk-row-actions">
          <button
            className="text-button"
            disabled={busy}
            onClick={() =>
              void act(async () => {
                const blob = new Blob(
                  [JSON.stringify(await exportHsk(), null, 2)],
                  { type: "application/json" },
                );
                const url = URL.createObjectURL(blob),
                  a = document.createElement("a");
                a.href = url;
                a.download = `kiyo-hsk-${new Date().toISOString().slice(0, 10)}.json`;
                a.click();
                setTimeout(() => URL.revokeObjectURL(url), 1000);
              })
            }
          >
            <DownloadSimple /> Export HSK notebook
          </button>
          <label className="hsk-import">
            Restore HSK notebook
            <input
              type="file"
              accept="application/json,.json"
              disabled={busy}
              onChange={(e) => {
                const file = e.target.files?.[0];
                if (file)
                  void act(async () => {
                    if (file.size > 10_000_000)
                      throw new Error("This backup is too large.");
                    await importHsk(JSON.parse(await file.text()));
                    setMessage(
                      "HSK notebook restored. Existing attempts were preserved.",
                    );
                  });
                e.target.value = "";
              }}
            />
          </label>
        </div>
      </footer>
    </section>
  );
}

function SourceChecklist({
  s,
  busy,
  act,
}: {
  s: typeof defaultHskSettings;
  busy: boolean;
  act: (fn: () => Promise<unknown>) => Promise<void>;
}) {
  const prefix = `${s.edition}:${s.level}:`;
  const steps = sourceStepsFor(s.level);
  const [pending, setPending] = useState<Record<string, boolean>>({});
  return (
    <ol className="hsk-source-checklist">
      {steps.map((t, i) => {
        const done = s.sourceDone.includes(prefix + t.id),
          unlocked = steps
            .slice(0, i)
            .every((p) => s.sourceDone.includes(prefix + p.id));
        return (
          <li key={t.id}>
            <label>
              <input
                type="checkbox"
                checked={pending[prefix + t.id] ?? done}
                disabled={busy || !unlocked}
                onChange={(e) => {
                  const checked = e.target.checked;
                  setPending((old) => ({ ...old, [prefix + t.id]: checked }));
                  void act(() =>
                    changeHskSettings({
                      sourceDone: checked
                        ? [...new Set([...s.sourceDone, prefix + t.id])]
                        : s.sourceDone.filter(
                            (id) =>
                              !steps.slice(i).some((p) => id === prefix + p.id),
                          ),
                    }),
                  ).finally(() =>
                    setPending((old) => {
                      const copy = { ...old };
                      delete copy[prefix + t.id];
                      return copy;
                    }),
                  );
                }}
              />
              <span>
                <strong>{t.title}</strong>
                <span>{t.detail}</span>
                {!unlocked && <small>Complete the preceding step first.</small>}
              </span>
            </label>
          </li>
        );
      })}
    </ol>
  );
}
