import { lazy, Suspense, useEffect, useRef, useState, type CSSProperties, type MouseEvent } from "react";
import { useLiveQuery } from "dexie-react-hooks";
import {
  ArrowUpRight,
  Check,
  DotsThree,
  DownloadSimple,
  Flame,
  GearSix,
  MagnifyingGlass,
  X,
  ArrowLeft,
  ArrowCounterClockwise,
} from "@phosphor-icons/react";
import { db, defaultProfile, importRecord } from "./db";
import {
  characters,
  charByHanzi,
  lessons,
  phrases,
  phraseById,
  readingLessons,
  standards,
  packUnits,
  packLessons,
} from "./content";
import { readings, characterSpeech } from "./hanzi";
import {
  dailyPlan,
  searchNormalize,
  skillEvidence,
  type PlanItem,
} from "./learning";
import { AudioButton, Arrow, PhraseText, Pinyin } from "./components";
import { useSpeech } from "./useSpeech";
import {
  CharacterAnatomy,
  HanziStage,
  ReadHome,
  Reader,
  coverage,
  knownSet,
  useCharacterStatus,
} from "./Characters";
import { mandarinVoices } from "./audio";
import { backupDue, downloadBackup } from "./backup";
import { OfflinePanel } from "./OfflinePanel";
import { sayoVoiceURI } from "./sayo-voice";
import {
  Journey,
  PathMap,
  stoneIcon,
  type PathNode,
  type PathUnit,
} from "./PathMap";
import type { Profile, Modality, LearningPath } from "./types";
import LessonPlayer from "./LessonPlayer";
import Welcome from "./Welcome";
import { authConfigured, oauthConfigured, signInWith, signOut } from "./auth";
import { acceptAccount, detachSync, startSync, syncNow } from "./sync";
import { SyncConsent, SyncPanel, useSyncStatus } from "./SyncPanel";
import { BrandSignature, brand } from "./brand";
import { Mascot, MascotGallery, MoSays, moLines } from "./Mascot";
import { levelOf, streakOf } from "./progression";
const Conversation = lazy(() => import("./Conversation"));
const MediaLab = lazy(() => import("./MediaLab"));
const Practice = lazy(() => import("./Practice"));
const Hsk = lazy(() => import("./Hsk"));
const CourseLibrary = lazy(() => import("./CourseLibrary"));
const Review = lazy(() =>
  import("./Practice").then((m) => ({ default: m.Review })),
);

type Route =
  | "today"
  | "library"
  | "read"
  | "learn"
  | "practice"
  | "speak"
  | "media"
  | "progress"
  | "dictionary"
  | "settings"
  | "review"
  | "mascot"
  | "hsk";
type LessonMode = "lesson" | "listening" | "assessment";
const nav: { id: Route; label: string; zh: string; mobile?: boolean }[] = [
  { id: "today", label: "Today", zh: "今天", mobile: true },
  { id: "library", label: "Course library", zh: "课程" },
  { id: "read", label: "Read", zh: "读", mobile: true },
  { id: "learn", label: "Listen", zh: "听", mobile: true },
  { id: "speak", label: "Speak", zh: "说", mobile: true },
  { id: "hsk", label: "HSK", zh: "考" },
  { id: "practice", label: "Practice", zh: "练" },
  { id: "media", label: "Media", zh: "看" },
  { id: "progress", label: "Progress", zh: "进步" },
];
const pathOf = (p: Profile): LearningPath => p.path ?? "characters";
const routes: Route[] = [
  ...nav.map((n) => n.id),
  "dictionary",
  "settings",
  "review",
  "mascot",
];
function routeFromHash(): Route {
  const hash = location.hash.slice(1);
  if (hash === "companion") return "mascot";
  if (hash === "listen") return "learn";
  return routes.includes(hash as Route) ? (hash as Route) : "today";
}

/** Days in a row, always in view. It never blocks or punishes; it only counts. */
function StreakChip({ profile, onOpen }: { profile: Profile; onOpen: () => void }) {
  const sessions = useLiveQuery(() => db.sessions.toArray()) ?? [];
  const attempts = useLiveQuery(() => db.attempts.toArray()) ?? [];
  const { days, studiedToday } = streakOf(sessions, attempts);
  if (profile.showStreak === false || !days) return null;
  return (
    <button
      className={`streak-chip ${studiedToday ? "is-lit" : ""}`}
      onClick={onOpen}
      aria-label={`${days} ${days === 1 ? "day" : "days"} in a row${studiedToday ? ", today counts" : ", study today to keep it"}`}
      title={studiedToday ? "Today counts" : "Study today to keep it"}
    >
      <Flame size={16} weight={studiedToday ? "fill" : "regular"} aria-hidden />
      <span className="tabular">{days}</span>
    </button>
  );
}

export default function App() {
  const syncStatus = useSyncStatus();
  useEffect(startSync, []);
  const profileData = useLiveQuery(() => db.profiles.get("learner"), [], null);
  const profile = profileData ?? defaultProfile;
  const [route, setRoute] = useState<Route>(routeFromHash),
    [hskFocus, setHskFocus] = useState(false),
    [speakScenario, setSpeakScenario] = useState<string | undefined>(undefined),
    [lesson, setLesson] = useState<{ id: string; mode: LessonMode } | null>(
      null,
    ),
    [reading, setReading] = useState<string | null>(null),
    [more, setMore] = useState(false),
    [online, setOnline] = useState(navigator.onLine),
    [storageError, setStorageError] = useState("");
  const menu = useRef<HTMLDialogElement>(null);
  const moreTrigger = useRef<HTMLButtonElement | null>(null);
  const openMore = (event: MouseEvent<HTMLButtonElement>) => {
    moreTrigger.current = event.currentTarget;
    setMore(true);
  };
  useEffect(() => {
    if (more && menu.current && !menu.current.open) menu.current.showModal();
    if (!more && menu.current?.open) {
      menu.current.close();
      moreTrigger.current?.focus();
    }
  }, [more]);
  useEffect(() => {
    const sync = () => {
      if (location.hash === "#main") return;
      setLesson(null);
      setReading(null);
      setRoute(routeFromHash());
    };
    window.addEventListener("hashchange", sync);
    return () => window.removeEventListener("hashchange", sync);
  }, []);
  useEffect(() => {
    const yes = () => setOnline(true),
      no = () => setOnline(false);
    window.addEventListener("online", yes);
    window.addEventListener("offline", no);
    return () => {
      window.removeEventListener("online", yes);
      window.removeEventListener("offline", no);
    };
  }, []);
  useEffect(() => {
    db.open().catch(() =>
      setStorageError(
        "Local storage could not open. Check that your browser allows site data, then reload.",
      ),
    );
  }, []);
  useEffect(() => {
    document.documentElement.dataset.tones =
      profile.toneColors === false ? "off" : "on";
  }, [profile.toneColors]);
  useEffect(() => {
    window.scrollTo(0, 0);
  }, [route, lesson, reading]);
  const navigate = (r: Route) => {
    setLesson(null);
    setReading(null);
    setMore(false);
    setRoute(r);
    location.hash = r === "mascot" ? "companion" : r === "learn" ? "listen" : r;
  };
  const openLesson = (id: string, mode: LessonMode = "lesson") =>
    setLesson({ id, mode });
  if (syncStatus.phase === "consent") return <SyncConsent />;
  if (route === "mascot")
    return <MascotGallery onBack={() => navigate("today")} />;
  if (storageError)
    return (
      <main className="recovery">
        <Mascot state="error" size={140} />
        <h1>Your learning needs a safe place to stay.</h1>
        <p>{storageError}</p>
        <button className="button" onClick={() => location.reload()}>
          Try again
        </button>
      </main>
    );
  if (profileData === null)
    return (
      <div className="loading-state">
        <Mascot state="think" size={100} />
        <BrandSignature className="brand-loading" />
      </div>
    );
  if (!profile.onboarded && !profile.entry)
    return (
      <Welcome
        onGuest={async () => {
          await db.profiles.put({ ...profile, entry: "guest" });
        }}
        onAccount={async (account) => {
          await acceptAccount(account);
          await syncNow();
        }}
      />
    );
  if (!profile.onboarded)
    return (
      <Onboarding
        base={profile}
        onComplete={async (p) => {
          await db.profiles.put(p);
          openLesson(p.path === "sound" ? "first" : "read-1");
        }}
      />
    );
  if (lesson)
    return (
      <LessonPlayer
        lessonId={lesson.id}
        profile={profile}
        mode={lesson.mode}
        onExit={() => setLesson(null)}
      />
    );
  if (reading)
    return (
      <Reader
        readingId={reading}
        profile={profile}
        onExit={() => setReading(null)}
      />
    );
  const current = nav.find((n) => n.id === route);
  return (
    <div
      className={`app-shell${route === "hsk" && hskFocus ? " hsk-focused" : ""}`}
    >
      <a
        className="skip-link"
        href="#main"
        onClick={(e) => {
          e.preventDefault();
          const main = document.getElementById("main");
          main?.focus();
          main?.scrollIntoView();
        }}
      >
        Skip to content
      </a>
      <header className="masthead">
        <button
          className="brand"
          onClick={() => navigate("today")}
          aria-label={`${brand.name}, today`}
        >
          <BrandSignature />
        </button>
        <nav aria-label="Main navigation" className="main-nav">
          {nav.map((n) => (
            <button
              key={n.id}
              className={route === n.id ? "active" : ""}
              aria-current={route === n.id ? "page" : undefined}
              onClick={() => navigate(n.id)}
            >
              {n.label}
            </button>
          ))}
        </nav>
        <div className="masthead-tools">
          <button className="text-button desktop-more" aria-controls="study-menu" aria-haspopup="dialog" aria-expanded={more} onClick={openMore}>
            More <DotsThree size={20} />
          </button>
          {!online && (
            <span className="offline-note">
              Offline · local learning available
            </span>
          )}
          <StreakChip profile={profile} onOpen={() => navigate("today")} />
          <button
            className={`icon-button ${route === "dictionary" ? "active" : ""}`}
            aria-label="Dictionary"
            onClick={() => navigate("dictionary")}
          >
            <MagnifyingGlass size={20} />
          </button>
          <button
            className={`icon-button ${route === "settings" ? "active" : ""}`}
            aria-label="Settings"
            onClick={() => navigate("settings")}
          >
            <GearSix size={20} />
          </button>
        </div>
      </header>
      <main id="main" className="main-content" tabIndex={-1}>
        <Suspense
          fallback={
            <div className="loading-state">
              <Mascot state="think" size={100} />
              Opening…
            </div>
          }
        >
          {route === "today" && (
            <Today
              profile={profile}
              onNavigate={navigate}
              onLesson={openLesson}
              onReading={setReading}
            />
          )}
          {route === "read" && (
            <ReadHome
              profile={profile}
              onLesson={(id, mode) => openLesson(id, mode ?? "lesson")}
              onReading={setReading}
            />
          )}
          {route === "library" && <CourseLibrary onLesson={openLesson} onReading={setReading} onSpeak={(id) => {
            navigate("speak");
            setSpeakScenario(id);
          }} />}
          {route === "learn" && (
            <Learn
              onLesson={openLesson}
              onReading={setReading}
              onSpeak={(id) => {
                navigate("speak");
                setSpeakScenario(id);
              }}
            />
          )}
          {route === "practice" && (
            <Practice
              profile={profile}
              onLesson={openLesson}
              onReview={() => navigate("review")}
            />
          )}
          {route === "speak" && (
            <Conversation
              key={speakScenario ?? "default"}
              profile={profile}
              initialScenario={speakScenario}
            />
          )}
          {route === "media" && <MediaLab profile={profile} />}
          {route === "hsk" && (
            <Hsk onLesson={openLesson} onFocus={setHskFocus} />
          )}
          {route === "progress" && <Progress onLesson={openLesson} />}
          {route === "dictionary" && <Dictionary profile={profile} />}
          {route === "settings" && (
            <Settings profile={profile} onMascot={() => navigate("mascot")} />
          )}
          {route === "review" && (
            <Review profile={profile} onLearn={() => navigate("read")} />
          )}
        </Suspense>
      </main>
      <nav className="tabbar" aria-label="Main navigation">
        {nav
          .filter((n) => n.mobile)
          .map((n) => (
            <button
              key={n.id}
              className={route === n.id ? "active" : ""}
              aria-current={route === n.id ? "page" : undefined}
              onClick={() => navigate(n.id)}
            >
              <span className="tab-zh" lang="zh-CN" aria-hidden>
                {n.zh}
              </span>
              <span>{n.label}</span>
            </button>
          ))}
        <button
          className={!current?.mobile && route !== "today" ? "active" : ""}
          aria-expanded={more}
          aria-controls="study-menu"
          aria-haspopup="dialog"
          onClick={openMore}
        >
          <span className="tab-zh" aria-hidden>
            <DotsThree size={22} weight="bold" />
          </span>
          <span>More</span>
        </button>
      </nav>
      <dialog ref={menu} id="study-menu" className="study-menu" aria-labelledby="study-menu-title"
        onClose={() => setMore(false)} onClick={(e) => { if (e.target === e.currentTarget) setMore(false); }}>
        <header><h2 id="study-menu-title">Your study desk</h2><button className="icon-button" aria-label="Close study desk" onClick={() => setMore(false)}><X size={20} /></button></header>
        <nav aria-label="More navigation">
          {(
            [
              ["library", "Course library", "课程"],
              ["practice", "Practice", "练"],
              ["hsk", "HSK", "考"],
              ["media", "Media", "看"],
              ["review", "Review", "复习"],
              ["progress", "Progress", "进步"],
              ["dictionary", "Dictionary", "词典"],
              ["settings", "Settings", "设置"],
              ["mascot", "Sayo & her voice", "小夜"],
            ] as [Route, string, string][]
          ).map(([id, label, zh]) => (
            <button
              key={id}
              onClick={() => navigate(id)}
            >
              <span lang="zh-CN" aria-hidden>
                {zh}
              </span>
              {label}
            </button>
          ))}
        </nav>
      </dialog>
    </div>
  );
}

const goalsList = [
  "Reading",
  "Conversation",
  "Friends & socializing",
  "Films & videos",
  "Travel & everyday life",
  "Work & ideas",
];
const paths: {
  id: LearningPath;
  title: string;
  zh: string;
  body: string;
  sample: string;
}[] = [
  {
    id: "characters",
    title: "Characters first",
    zh: "先认字",
    body: "Start by counting 一 to 十, then easy words. Every character comes with its pinyin and sound, then short texts to read.",
    sample: "一 二 三",
  },
  {
    id: "together",
    title: "Side by side",
    zh: "读和听",
    body: "A few characters and a few phrases every day, so what you read and what you hear grow together.",
    sample: "好 · hǎo",
  },
  {
    id: "sound",
    title: "Sound first",
    zh: "先听说",
    body: "Start with listening, tones and useful phrases. Characters arrive once the sounds are familiar.",
    sample: "nǐ hǎo",
  },
];
function Onboarding({
  base,
  onComplete,
}: {
  base: Profile;
  onComplete: (p: Profile) => Promise<void>;
}) {
  const [stage, setStage] = useState(0),
    [name, setName] = useState(base.name),
    [minutes, setMinutes] = useState(30),
    [goals, setGoals] = useState([
      "Reading",
      ...defaultProfile.goals.slice(0, 2),
    ]),
    [path, setPath] = useState<LearningPath>("characters"),
    [quiet, setQuiet] = useState(false),
    [busy, setBusy] = useState(false),
    [error, setError] = useState("");
  async function finish() {
    setBusy(true);
    try {
      await onComplete({
        ...base,
        name: name.trim(),
        minutes,
        goals,
        quiet,
        path,
        pinyin: path !== "characters",
        onboarded: true,
      });
    } catch {
      setError(
        "Your preferences could not be saved. Check browser storage and try again.",
      );
      setBusy(false);
    }
  }
  const titles = [
    "Mandarin, read and spoken.",
    "Where would you like to begin?",
    "Make a little room for it.",
  ];
  return (
    <main className="onboarding">
      <header className="onboarding-top">
        <BrandSignature className="brand-onboarding" />
        <ol className="steps" aria-label={`Step ${stage + 1} of 3`}>
          {[0, 1, 2].map((i) => (
            <li key={i} className={i <= stage ? "on" : ""} />
          ))}
        </ol>
      </header>
      <div className="onboarding-body">
        <section className="onboarding-form" key={stage}>
          <p className="eyebrow">Step {stage + 1} of 3</p>
          <h1>{titles[stage]}</h1>
          {stage === 0 && (
            <>
              <p className="lede">
                Characters you can read. Speech you can follow. Replies that
                come without translating in your head.
              </p>
              <label className="field">
                <span>
                  What should we call you?{" "}
                  <span className="muted">Optional</span>
                </span>
                <input
                  value={name}
                  maxLength={40}
                  onChange={(e) => setName(e.target.value)}
                  placeholder="Your first name"
                  autoComplete="given-name"
                />
              </label>
              <fieldset className="chip-picker">
                <legend>What matters most to you?</legend>
                {goalsList.map((g) => (
                  <button
                    type="button"
                    aria-pressed={goals.includes(g)}
                    key={g}
                    onClick={() =>
                      setGoals((v) =>
                        v.includes(g) ? v.filter((x) => x !== g) : [...v, g],
                      )
                    }
                  >
                    {goals.includes(g) && <Check size={14} weight="bold" />}
                    {g}
                  </button>
                ))}
              </fieldset>
              <div className="onboarding-actions">
                <span />
                <button className="button" onClick={() => setStage(1)}>
                  Continue <Arrow />
                </button>
              </div>
            </>
          )}
          {stage === 1 && (
            <>
              <p className="lede">
                You can change this any time. Every path ends up in the same
                place: reading, listening and speaking.
              </p>
              <div
                className="path-picker"
                role="radiogroup"
                aria-label="Learning path"
              >
                {paths.map((p) => (
                  <button
                    key={p.id}
                    role="radio"
                    aria-checked={path === p.id}
                    className={path === p.id ? "on" : ""}
                    onClick={() => setPath(p.id)}
                  >
                    <span
                      className="path-sample"
                      lang={p.id === "sound" ? "zh-Latn-pinyin" : "zh-CN"}
                    >
                      {p.sample}
                    </span>
                    <span className="path-copy">
                      <strong>
                        {p.title} <span lang="zh-CN">{p.zh}</span>
                      </strong>
                      <span>{p.body}</span>
                    </span>
                    <span className="radio" aria-hidden />
                  </button>
                ))}
              </div>
              <div className="onboarding-actions">
                <button className="text-button" onClick={() => setStage(0)}>
                  <ArrowLeft size={17} /> Back
                </button>
                <button className="button" onClick={() => setStage(2)}>
                  Continue <Arrow />
                </button>
              </div>
            </>
          )}
          {stage === 2 && (
            <>
              <fieldset className="duration-picker">
                <legend>Minutes a day</legend>
                {[10, 20, 30, 45, 60].map((n) => (
                  <button
                    key={n}
                    aria-pressed={minutes === n}
                    onClick={() => setMinutes(n)}
                  >
                    {n}
                  </button>
                ))}
              </fieldset>
              <label className="check-field">
                <input
                  type="checkbox"
                  checked={quiet}
                  onChange={(e) => setQuiet(e.target.checked)}
                />
                <span>
                  Start in quiet mode
                  <small>
                    Text alternatives to speaking. Change this any time.
                  </small>
                </span>
              </label>
              <p className="privacy-note">
                Progress is saved in this browser. Bundled voices work offline.
                Recordings stay in the current tab.
              </p>
              <div className="onboarding-actions">
                <button className="text-button" onClick={() => setStage(1)}>
                  <ArrowLeft size={17} /> Back
                </button>
                <button
                  className="button"
                  disabled={busy}
                  onClick={() => void finish()}
                >
                  {busy
                    ? "Preparing…"
                    : path === "sound"
                      ? "Hear your first words"
                      : "Meet your first characters"}{" "}
                  <Arrow />
                </button>
              </div>
              {error && (
                <p role="alert" className="inline-error">
                  {error}
                </p>
              )}
            </>
          )}
        </section>
        <aside className="onboarding-specimen">
          <Mascot
            state={
              stage === 0
                ? "welcome"
                : stage === 1
                  ? path === "sound"
                    ? "listen"
                    : "read"
                  : "encourage"
            }
            size={360}
          />
          <p className="mascot-caption">
            {stage === 0
              ? "A little Mandarin, together."
              : stage === 1
                ? "We’ll find your way into the language."
                : "Small steps. Plenty of room to grow."}
          </p>
          <a className="text-button" href="#companion">
            Meet Sayo
          </a>
        </aside>
      </div>
    </main>
  );
}

const zhNum = (n: number) => {
  const d = "〇一二三四五六七八九";
  if (n <= 10) return n === 10 ? "十" : d[n];
  if (n < 20) return "十" + d[n - 10];
  return d[Math.floor(n / 10)] + "十" + (n % 10 ? d[n % 10] : "");
};
function chineseDate(date: Date) {
  return `${zhNum(date.getMonth() + 1)}月${zhNum(date.getDate())}日 星期${"日一二三四五六"[date.getDay()]}`;
}
function greeting(date: Date) {
  const h = date.getHours();
  return h < 5
    ? "Still up"
    : h < 12
      ? "Good morning"
      : h < 18
        ? "Good afternoon"
        : "Good evening";
}

function Today({
  profile,
  onNavigate,
  onLesson,
  onReading,
}: {
  profile: Profile;
  onNavigate: (r: Route) => void;
  onLesson: (id: string, mode?: LessonMode) => void;
  onReading: (id: string) => void;
}) {
  const sessions = useLiveQuery(() => db.sessions.toArray()) ?? [],
    attempts = useLiveQuery(() => db.attempts.toArray()) ?? [],
    memories = useLiveQuery(() => db.memories.toArray()) ?? [];
  const status = useCharacterStatus(),
    known = knownSet(status);
  const path = pathOf(profile);
  const complete = new Set(
    sessions
      .filter(
        (s) =>
          (s.kind === "lesson" || s.kind === "assessment") &&
          !s.lessonId.startsWith("listening:"),
      )
      .map((s) => s.lessonId),
  );
  // The speaking course: the base lessons, then the HSK units in order.
  const course = [...lessons, ...packLessons];
  const nextSpeak = course.find((l) => !complete.has(l.id)) ?? lessons[0];
  const nextRead =
    readingLessons.find((l) => !complete.has(l.id)) ?? readingLessons[0];
  const nextText =
    readings.find(
      (r) => !complete.has(`read:${r.id}`) && coverage(r, known).pct >= 50,
    ) ??
    readings.find((r) => !complete.has(`read:${r.id}`)) ??
    readings[0];
  const due = memories.filter(
    (m) =>
      m.due <= Date.now() &&
      !["conversation", "speaking", "recall", "media"].includes(m.modality),
  ).length;
  const plan = dailyPlan(profile.minutes, attempts, due, path);
  const { level, finished } = levelOf(sessions);
  const { days: streak, studiedToday } = streakOf(sessions, attempts);
  const now = new Date();
  const date = now.toLocaleDateString("en-US", {
    weekday: "long",
    month: "long",
    day: "numeric",
  });
  const readFirst = path !== "sound";
  const featured =
    charByHanzi[
      (
        nextRead.phrases.find((p) => status[p.slice(2)] === "new") ??
        nextRead.phrases[0]
      ).slice(2)
    ];
  const go = (item: PlanItem) => {
    if (item.route === "review") onNavigate("review");
    else if (item.route === "speak") onNavigate("speak");
    else if (item.route === "characters") onLesson(nextRead.id);
    else if (item.route === "reading") onReading(nextText.id);
    else
      onLesson(
        nextSpeak.id,
        item.route === "listening" ? "listening" : "lesson",
      );
  };
  const recognised = Object.values(status).filter(
    (s) => s === "recognised" || s === "secure",
  ).length;
  const textCover = coverage(nextText, known);
  const syncState = useLiveQuery(() => db.syncState.get("local"));
  const [backupNote, setBackupNote] = useState("");
  const showBackup = backupDue({
    now: Date.now(),
    firstStudyAt: sessions.length
      ? Math.min(...sessions.map((s) => s.completedAt))
      : undefined,
    lastBackupAt: profile.lastBackupAt,
    snoozedAt: profile.backupSnoozedAt,
    lastSyncAt: syncState?.enabled ? syncState.lastSync : undefined,
  });
  async function backupNow() {
    try {
      await downloadBackup();
      await db.profiles.put({ ...profile, lastBackupAt: Date.now() });
      setBackupNote(
        "Backup saved. Keep the file somewhere safe, like a cloud drive.",
      );
    } catch {
      setBackupNote("The backup couldn’t be created. Try again from Settings.");
    }
  }
  return (
    <div className="today">
      <header className="today-head">
        <div>
          <p className="dateline">
            {date}
            <span lang="zh-CN">{chineseDate(now)}</span>
          </p>
          <h1>
            {greeting(now)}
            {profile.name ? `, ${profile.name}` : ""}.
          </h1>
        </div>
        <div className="today-mo">
          <MoSays
            state={due ? "review" : "welcome"}
            say={due ? undefined : studiedToday ? moLines.done : undefined}
            size={200}
            side="left"
          />
        </div>
      </header>
      <section className="lead" aria-labelledby="lead-title">
        {readFirst ? (
          <button
            className="lead-glyph"
            onClick={() => onLesson(nextRead.id)}
            aria-label={`Start lesson: ${nextRead.title}`}
          >
            <span lang="zh-CN">{featured.hanzi}</span>
            <span className="lead-glyph-gloss">{featured.meaning}</span>
          </button>
        ) : (
          <button
            className="lead-glyph lead-phrase"
            onClick={() => onLesson(nextSpeak.id)}
            aria-label={`Start lesson: ${nextSpeak.title}`}
          >
            <span lang="zh-CN">{phraseById[nextSpeak.phrases[0]].hanzi}</span>
            <Pinyin text={phraseById[nextSpeak.phrases[0]].pinyin} />
          </button>
        )}
        <div className="lead-copy">
          <p className="eyebrow">
            {readFirst
              ? `Characters · lesson ${readingLessons.indexOf(nextRead) + 1} of ${readingLessons.length}`
              : `${nextSpeak.unit} · lesson ${course.indexOf(nextSpeak) + 1}`}
          </p>
          <h2 id="lead-title">
            {readFirst ? nextRead.title : nextSpeak.title}
          </h2>
          <p>{readFirst ? nextRead.description : nextSpeak.description}</p>
          {readFirst && (
            <p
              className="lead-chars"
              lang="zh-CN"
              aria-label="Characters in this lesson"
            >
              {nextRead.phrases.map((p) => (
                <span key={p} className={`s-${status[p.slice(2)]}`}>
                  {p.slice(2)}
                </span>
              ))}
            </p>
          )}
          <div className="lead-actions">
            <button
              className="button"
              onClick={() =>
                readFirst ? onLesson(nextRead.id) : onLesson(nextSpeak.id)
              }
            >
              Continue <Arrow />
            </button>
            <AudioButton
              text={
                readFirst
                  ? featured.say
                  : phraseById[nextSpeak.phrases[0]].audio.text
              }
              voiceURI={profile.voiceURI}
              label="Hear it"
            />
          </div>
        </div>
      </section>

      {(showBackup || backupNote) && (
        <aside className="backup-nudge" role="status">
          {backupNote ? (
            <p>{backupNote}</p>
          ) : (
            <>
              <p>
                <strong>Back up your progress.</strong> It lives only in this
                browser until sync is on; clearing site data would erase it.
              </p>
              <div className="backup-actions">
                <button
                  className="button secondary"
                  onClick={() => void backupNow()}
                >
                  <DownloadSimple size={18} /> Export backup
                </button>
                <button
                  className="text-button"
                  onClick={() =>
                    void db.profiles.put({
                      ...profile,
                      backupSnoozedAt: Date.now(),
                    })
                  }
                >
                  Later
                </button>
              </div>
            </>
          )}
        </aside>
      )}

      <div className="today-columns">
        <section className="plan" aria-labelledby="plan-title">
          <div className="section-head">
            <h2 id="plan-title">Today’s session</h2>
            <div
              className="minutes-picker"
              role="radiogroup"
              aria-label="Minutes today"
            >
              {[10, 20, 30, 45, 60].map((n) => (
                <button
                  key={n}
                  role="radio"
                  aria-checked={profile.minutes === n}
                  className="tabular"
                  onClick={() =>
                    void db.profiles.put({ ...profile, minutes: n })
                  }
                >
                  {n}
                </button>
              ))}
              <span aria-hidden>min</span>
            </div>
          </div>
          <p className="plan-reason">{plan.reason}</p>
          <ol>
            {plan.items.map((item, i) => (
              <li key={item.route}>
                <button onClick={() => go(item)}>
                  <span className="plan-index tabular">{i + 1}</span>
                  <span className="plan-text">
                    <strong>{item.label}</strong>
                    <span>{item.detail}</span>
                  </span>
                  <span className="plan-time tabular">{item.minutes} min</span>
                  <span className="plan-go" aria-hidden>
                    <Arrow />
                  </span>
                </button>
              </li>
            ))}
          </ol>
        </section>

        <section className="today-text" aria-labelledby="text-title">
          <div className="section-head">
            <h2 id="text-title">Something to read</h2>
            <button className="text-button" onClick={() => onNavigate("read")}>
              All readings <ArrowUpRight size={16} />
            </button>
          </div>
          <button
            className="text-teaser"
            onClick={() => onReading(nextText.id)}
          >
            <span className="teaser-title" lang="zh-CN">
              {nextText.titleZh}
            </span>
            <span className="teaser-line" lang="zh-CN">
              {Array.from(nextText.lines[0].zh).map((ch, i) => (
                <span key={i} className={known.has(ch) ? "k" : ""}>
                  {ch}
                </span>
              ))}
            </span>
            <span className="teaser-meta">
              {nextText.title} · you recognise {textCover.known} of{" "}
              {textCover.total} characters
            </span>
          </button>
          <dl className="today-facts">
            <div>
              <dt>Milestone</dt>
              <dd>
                {readFirst
                  ? "First note: read a short message from a friend."
                  : "First contact: greet someone and introduce yourself."}
              </dd>
            </div>
            <div>
              <dt>Level</dt>
              <dd>
                <span className="tabular">{level}</span>
                <span className="muted">
                  {" · "}
                  {finished.size
                    ? `${finished.size} ${finished.size === 1 ? "lesson" : "lessons"} finished`
                    : "finish a lesson to reach 2"}
                </span>
              </dd>
            </div>
            {profile.showStreak !== false && (
              <div>
                <dt>Days in a row</dt>
                <dd>
                  <span className="tabular">{streak}</span>
                  <span className="muted">
                    {studiedToday
                      ? " · today counts"
                      : streak
                        ? " · study today to keep it"
                        : " · start today"}
                  </span>
                </dd>
              </div>
            )}
            <div>
              <dt>Review</dt>
              <dd>
                {due ? (
                  <button
                    className="text-button"
                    onClick={() => onNavigate("review")}
                  >
                    {due} ready now <Arrow />
                  </button>
                ) : (
                  "Nothing due. Memories return when they’re ready."
                )}
              </dd>
            </div>
            <div>
              <dt>Characters</dt>
              <dd>
                <span className="tabular">{recognised}</span> of{" "}
                {characters.length} recognised without help
              </dd>
            </div>
          </dl>
        </section>
      </div>
    </div>
  );
}

function Learn({
  onLesson,
  onReading,
  onSpeak,
}: {
  onLesson: (id: string) => void;
  onReading: (id: string) => void;
  onSpeak: (scenarioId: string) => void;
}) {
  const sessions = useLiveQuery(() => db.sessions.toArray()) ?? [],
    done = new Set(sessions.map((s) => s.lessonId));
  const groups = [
    {
      id: "foundation",
      title: "First conversations",
      subtitle: "Hello, your name, yes and no, numbers and friends.",
      match: (u: string) => u === "Sound & survival",
    },
    {
      id: "everyday",
      title: "Everyday moments",
      subtitle: "Cafés, plans, directions, hobbies and your day.",
      match: (u: string) => u !== "Sound & survival",
    },
  ];
  // Units are numbered within their level so HSK 2 starts at unit 1 again.
  const levelOf = new Map<string, string>();
  const units: PathUnit[] = groups.map((g, gi) => ({
    id: g.id,
    number: gi + 1,
    title: g.title,
    subtitle: g.subtitle,
    nodes: lessons
      .filter((l) => g.match(l.unit))
      .map((l) => {
        const sample = phraseById[l.phrases[0]].hanzi;
        return {
          id: l.id,
          face: (
            <span lang="zh-CN">{Array.from(sample).slice(0, 2).join("")}</span>
          ),
          title: l.title,
          detail: `${phraseById[l.phrases[0]].pinyin} · ${l.minutes} min`,
          status: done.has(l.id) ? "done" : "open",
          onOpen: () => onLesson(l.id),
        } satisfies PathNode;
      }),
  }));
  for (const g of groups) levelOf.set(g.id, "foundation");
  // Content-pack units: words, grammar & usage, dialogue, reading, role-play.
  const perLevel = new Map<string, number>();
  for (const u of packUnits) {
    const level = u.hskTarget ? String(u.hskTarget.level) : "foundation";
    levelOf.set(u.id, level);
    perLevel.set(level, (perLevel.get(level) ?? 0) + 1);
    const number = level === "foundation" ? groups.length + perLevel.get(level)! : perLevel.get(level)!;
    const nodes: PathNode[] = u.lessons.map((l) => ({
      id: l.id,
      face:
        l.packPart === "words" ? (
          <span lang="zh-CN">
            {Array.from(phraseById[l.phrases[0]]?.hanzi ?? "词")
              .slice(0, 2)
              .join("")}
          </span>
        ) : (
          stoneIcon.check
        ),
      title: l.packPart === "words" ? "New words" : "Grammar & usage",
      detail: `${l.phrases.length} ${l.packPart === "words" ? "words" : "items"} · ${l.minutes} min`,
      status: done.has(l.id) ? "done" : "open",
      kind: l.packPart === "words" ? "learn" : "check",
      onOpen: () => onLesson(l.id),
    }));
    for (const t of u.texts)
      nodes.push({
        id: `read:${t.id}`,
        face: stoneIcon.read,
        title: t.id.endsWith("-d")
          ? `Dialogue: ${t.title}`
          : `Read: ${t.title}`,
        detail: t.titleZh,
        status: done.has(`read:${t.id}`) ? "done" : "open",
        kind: "read",
        onOpen: () => onReading(t.id),
      });
    if (u.scenario)
      nodes.push({
        id: `conversation:${u.scenario.id}`,
        face: stoneIcon.speak,
        title: `Role-play: ${u.scenario.title}`,
        detail: u.scenario.place,
        status: done.has(`conversation:${u.scenario.id}`) ? "done" : "open",
        kind: "read",
        onOpen: () => onSpeak(u.scenario!.id),
      });
    units.push({
      id: u.id,
      number,
      title: u.title,
      subtitle: u.canDo.join(" · "),
      preview: u.titleZh,
      nodes,
    });
  }
  const firstOpen = units
    .flatMap((u) => u.nodes)
    .find((n) => n.status !== "done");
  if (firstOpen) firstOpen.status = "next";
  const currentUnit =
    units.find((u) => u.nodes.some((n) => n.status === "next")) ?? units[0];
  // One unit on the trail at a time: the whole course is 150 units long.
  const [picked, setPicked] = useState<string | null>(null);
  const [level, setLevel] = useState<string | null>(null);
  const focus = units.find((u) => u.id === picked) ?? currentUnit;
  const levels = ["foundation", "1", "2", "3", "4", "5", "6"].filter((l) =>
    units.some((u) => levelOf.get(u.id) === l),
  );
  const shownLevel = level ?? levelOf.get(focus.id) ?? "foundation";
  const levelName = (l: string) => (l === "foundation" ? "Foundation" : `HSK ${l}`);
  const stage = levels.indexOf(levelOf.get(currentUnit.id) ?? "foundation");
  return (
    <div className="listen-page">
      <header className="page-head">
        <p className="eyebrow">
          <span lang="zh-CN">听</span> Listen
        </p>
        <h1>Hear it first. Then say it back.</h1>
        <p className="lede">
          Short lessons that start with sound: say hello, count, order a drink.
          Every new phrase shows its pinyin so you always know how to say it.
        </p>
      </header>
      <section className="listen-focus" id="listen-focus" aria-labelledby="listen-focus-title">
        <div className="section-head">
          <h2 id="listen-focus-title">
            {focus.id === currentUnit.id ? "Where you are" : focus.title}
          </h2>
          <p className="muted">
            {levelName(levelOf.get(focus.id) ?? "foundation")} · unit {focus.number}
            {focus.id !== currentUnit.id && (
              <>
                {" · "}
                <button className="text-button" onClick={() => setPicked(null)}>
                  Back to where you are
                </button>
              </>
            )}
          </p>
        </div>
        <PathMap label="Listening path" units={[focus]} />
      </section>
      <section className="listen-units" aria-labelledby="listen-units-title">
        <div className="section-head">
          <h2 id="listen-units-title">Every unit</h2>
          <p className="muted">
            {units.length} units from your first 你好 to HSK 6. Pick one to put it on the trail.
          </p>
        </div>
        <div className="level-strip" role="group" aria-label="Course level">
          {levels.map((l) => (
            <button
              key={l}
              aria-pressed={shownLevel === l}
              onClick={() => setLevel(l)}
            >
              {levelName(l)}
            </button>
          ))}
        </div>
        <ul className="unit-grid" aria-label={`${levelName(shownLevel)} units`}>
          {units
            .filter((u) => levelOf.get(u.id) === shownLevel)
            .map((u) => {
              const done = u.nodes.filter((n) => n.status === "done").length;
              const state = [
                u.id === focus.id ? "is-focus" : "",
                done === u.nodes.length ? "is-done" : done ? "is-started" : "",
              ].join(" ");
              return (
                <li key={u.id}>
                  <button
                    className={`unit-card ${state}`}
                    aria-pressed={u.id === focus.id}
                    style={{ "--p": done / u.nodes.length } as CSSProperties}
                    onClick={() => {
                      setPicked(u.id);
                      document.getElementById("listen-focus")?.scrollIntoView({
                        behavior: matchMedia("(prefers-reduced-motion: reduce)").matches ? "auto" : "smooth",
                        block: "start",
                      });
                    }}
                  >
                    <span className="unit-card-top">
                      <span className="unit-card-number">Unit {u.number}</span>
                      <span className="unit-card-count tabular">
                        {done}/{u.nodes.length}
                      </span>
                    </span>
                    <strong>{u.title}</strong>
                    {u.preview && (
                      <span className="unit-card-zh" lang="zh-CN">
                        {u.preview}
                      </span>
                    )}
                    <span className="unit-card-meter" aria-hidden />
                  </button>
                </li>
              );
            })}
        </ul>
      </section>
      <Journey current={Math.max(0, stage)} />
      <p className="small content-note">
        Original drafts · awaiting native educator and audio review.
      </p>
    </div>
  );
}

function Progress({
  onLesson,
}: {
  onLesson: (id: string, mode: "assessment") => void;
}) {
  const attempts = useLiveQuery(() => db.attempts.toArray()) ?? [],
    sessions = useLiveQuery(() => db.sessions.toArray()) ?? [],
    mistakes = useLiveQuery(() => db.mistakes.toArray()) ?? [];
  const status = useCharacterStatus();
  const [section, setSection] = useState("Capabilities");
  const dimensions: [Modality, string, string][] = [
    ["reading", "Reading", "Characters and words understood without pinyin"],
    ["listening", "Listening", "Meaning recognised from audio alone"],
    ["typing", "Typing & structure", "Phrases assembled or typed"],
    [
      "conversation",
      "Conversation rehearsal",
      "Limited scripted patterns, typed responses",
    ],
    ["media", "Media listening", "Gist and detail in the original scene"],
    ["speaking", "Speaking", "Practice attempts; no automatic scoring"],
  ];
  const counts = { new: 0, met: 0, recognised: 0, secure: 0 };
  for (const s of Object.values(status)) counts[s]++;
  return (
    <div className="progress-page">
      <header className="page-head">
        <p className="eyebrow">Progress</p>
        <h1>What’s becoming possible.</h1>
        <p className="lede">
          Evidence, one skill at a time. No single fluency score.
        </p>
      </header>
      <div className="tabs" role="tablist" aria-label="Progress sections">
        {["Capabilities", "Mistakes", "HSK alignment"].map((s) => (
          <button
            key={s}
            role="tab"
            aria-selected={section === s}
            onClick={() => setSection(s)}
          >
            {s}
          </button>
        ))}
      </div>
      {section === "Capabilities" ? (
        <>
          <p className="progress-summary">
            {sessions.length || attempts.length
              ? `${sessions.length} completed study sessions · ${attempts.length} saved attempts`
              : "Nothing measured yet. Your first lesson gives you something real to build on."}
          </p>
          <section className="char-meter" aria-label="Character recognition">
            <div className="meter" aria-hidden>
              {(["secure", "recognised", "met", "new"] as const).map((k) => (
                <i
                  key={k}
                  className={`s-${k}`}
                  style={{ flexGrow: counts[k] }}
                />
              ))}
            </div>
            <dl>
              <div>
                <dt>Secure</dt>
                <dd className="tabular">{counts.secure}</dd>
              </div>
              <div>
                <dt>Recognised</dt>
                <dd className="tabular">{counts.recognised}</dd>
              </div>
              <div>
                <dt>Met</dt>
                <dd className="tabular">{counts.met}</dd>
              </div>
              <div>
                <dt>Not met</dt>
                <dd className="tabular">{counts.new}</dd>
              </div>
            </dl>
          </section>
          <table className="capability-table">
            <thead>
              <tr>
                <th scope="col">Skill</th>
                <th scope="col">Evidence</th>
              </tr>
            </thead>
            <tbody>
              {dimensions.map(([id, name, description]) => {
                const e = skillEvidence(attempts, id);
                return (
                  <tr key={id} className="capability-row">
                    <th scope="row">
                      <strong>{name}</strong>
                      <span>{description}</span>
                    </th>
                    <td>
                      {id === "speaking" ? (
                        <strong className="tabular">
                          {attempts.filter((a) => a.modality === id).length}{" "}
                          attempts
                        </strong>
                      ) : e.count ? (
                        <>
                          <strong className="tabular">
                            {e.correct} / {e.count}
                          </strong>
                          <span>unaided answers correct</span>
                        </>
                      ) : (
                        <span className="muted">Not measured yet</span>
                      )}
                    </td>
                  </tr>
                );
              })}
            </tbody>
          </table>
          <section className="assessment-invite">
            <div>
              <h2>First contact: a listening checkpoint</h2>
              <p>
                Recognise the first useful expressions without a transcript. A
                product exercise with familiar material, not an official rating.
              </p>
            </div>
            <button
              className="button secondary"
              onClick={() => onLesson("first", "assessment")}
            >
              Try the checkpoint <Arrow />
            </button>
          </section>
        </>
      ) : section === "Mistakes" ? (
        <>
          <p className="muted">
            A place to notice, not a list to be perfect at.
          </p>
          {mistakes.length ? (
            <ul className="mistake-list">
              {mistakes
                .sort((a, b) => b.at - a.at)
                .map((m) => (
                  <li className="mistake-row" key={m.id}>
                    <span className="mistake-zh" lang="zh-CN">
                      {phraseById[m.phraseId]?.hanzi}
                    </span>
                    <div>
                      <strong>
                        {m.modality} · missed {m.count}{" "}
                        {m.count === 1 ? "time" : "times"}
                      </strong>
                      <p>
                        You chose “{m.answer}”. Expected “{m.expected}”.
                      </p>
                    </div>
                    <AudioButton
                      text={phraseById[m.phraseId]?.audio.text ?? ""}
                    />
                  </li>
                ))}
            </ul>
          ) : (
            <div className="empty-state">
              <h2>Nothing here yet.</h2>
              <p>
                When an exercise reveals a gap, it is saved here and used in
                review.
              </p>
            </div>
          )}
        </>
      ) : (
        <div className="standards-page">
          <h2>Communication first. Standards alongside.</h2>
          <p>
            Formal mappings are not yet verified. We don’t turn a small seed
            curriculum into an exam-readiness percentage.
          </p>
          {standards.map((s) => (
            <article key={s.id}>
              <h3>{s.name}</h3>
              <p>{s.note}</p>
              <a href={s.source} target="_blank" rel="noreferrer">
                Official source <ArrowUpRight size={16} />
              </a>
            </article>
          ))}
          <ol className="hsk-levels">
            {Array.from({ length: 9 }, (_, i) => (
              <li key={i}>
                <span className="tabular">{i + 1}</span>
                <strong>
                  {i < 3 ? "Elementary" : i < 6 ? "Intermediate" : "Advanced"}
                </strong>
                <small>Mapping pending</small>
              </li>
            ))}
          </ol>
          <p className="small">No certificate is issued by this app.</p>
        </div>
      )}
    </div>
  );
}

const PAGE = 60;
function Dictionary({ profile }: { profile: Profile }) {
  const speech = useSpeech();
  const [query, setQuery] = useState(""),
    [selected, setSelected] = useState<string | null>(null),
    [limit, setLimit] = useState(PAGE);
  const q = searchNormalize(query);
  const items = [
    ...characters,
    ...phrases.filter((p) => p.topic !== "sounds" || !charByHanzi[p.hanzi]),
  ];
  const matches = items.filter((p) =>
    searchNormalize([p.hanzi, p.pinyin, p.meaning].join(" ")).includes(q),
  );
  // The course holds thousands of entries; page the list instead of painting them all.
  const filtered = matches.slice(0, limit);
  const more = matches.length - filtered.length;
  const pick = selected ? phraseById[selected] : null,
    pickChar = pick ? charByHanzi[pick.hanzi] : null;
  return (
    <div className="dictionary-page">
      <header className="page-head">
        <p className="eyebrow">Dictionary</p>
        <h1>Every character and phrase in your course.</h1>
      </header>
      <label className="search">
        <MagnifyingGlass size={22} />
        <span className="sr-only">Search the course</span>
        <input
          value={query}
          onChange={(e) => {
            setQuery(e.target.value);
            setLimit(PAGE);
          }}
          placeholder="Try 你好, ni hao, or hello…"
        />
        {query && (
          <button
            className="icon-button"
            aria-label="Clear search"
            onClick={() => setQuery("")}
          >
            <X size={18} />
          </button>
        )}
      </label>
      {speech.error && (
        <p className="inline-error" role="alert">
          {speech.error}
        </p>
      )}
      <div className={`dictionary-layout ${pick ? "has-detail" : ""}`}>
        <ul className="word-list">
          {filtered.map((p) => (
            <li key={p.id}>
              <button
                className={selected === p.id ? "selected" : ""}
                onClick={() => {
                  setSelected(p.id);
                  speech.speak(
                    p.audio.text ?? charByHanzi[p.hanzi]?.say ?? p.hanzi,
                  );
                }}
              >
                <span className="wl-zh" lang="zh-CN">
                  {p.hanzi}
                </span>
                <Pinyin text={p.pinyin} />
                <span className="wl-en">{p.meaning}</span>
              </button>
            </li>
          ))}
          {!filtered.length && (
            <li className="empty-state">
              <h2>No match in this course.</h2>
              <p>Try a shorter phrase or its English meaning.</p>
            </li>
          )}
          {more > 0 && (
            <li className="word-list-more">
              <p className="small muted" role="status">
                Showing {filtered.length} of {matches.length}. Type to narrow the list.
              </p>
              <button className="button secondary" onClick={() => setLimit((n) => n + PAGE)}>
                Show {Math.min(more, PAGE)} more
              </button>
            </li>
          )}
        </ul>
        {pick && (
          <aside className="word-detail">
            <button className="text-button" onClick={() => setSelected(null)}>
              <X size={16} /> Close
            </button>
            {pickChar ? (
              <>
                <HanziStage char={pickChar.hanzi} size={180} />
                <CharacterAnatomy entry={pickChar} profile={profile} />
              </>
            ) : (
              <>
                <PhraseText phrase={pick} />
                <AudioButton
                  text={pick.audio.text || pick.hanzi}
                  voiceURI={profile.voiceURI}
                  label="Hear it"
                />
                <h3>In real life</h3>
                <p>{pick.usage}</p>
                <dl className="detail-facts">
                  <dt>Register</dt>
                  <dd>{pick.register}</dd>
                  <dt>Traditional</dt>
                  <dd lang="zh-Hant">{pick.traditional}</dd>
                  <dt>Characters</dt>
                  <dd lang="zh-CN" className="detail-chars">
                    {Array.from(pick.hanzi).map((c, i) =>
                      charByHanzi[c] ? (
                        <button
                          key={i}
                          className="text-button"
                          onClick={() => {
                            setSelected(`c:${c}`);
                            speech.speak(characterSpeech(c));
                          }}
                        >
                          {c}
                        </button>
                      ) : (
                        <span key={i}>{c}</span>
                      ),
                    )}
                  </dd>
                </dl>
              </>
            )}
            <p className="small">
              Original draft · awaiting native educator review.
            </p>
          </aside>
        )}
      </div>
    </div>
  );
}

function Settings({
  profile,
  onMascot,
}: {
  profile: Profile;
  onMascot: () => void;
}) {
  const [message, setMessage] = useState(""),
    [error, setError] = useState(""),
    [voices, setVoices] = useState(mandarinVoices()),
    [reset, setReset] = useState(false),
    [restoreFile, setRestoreFile] = useState<File | null>(null);
  useEffect(() => {
    const load = () => setVoices(mandarinVoices());
    globalThis.speechSynthesis?.addEventListener("voiceschanged", load);
    return () =>
      globalThis.speechSynthesis?.removeEventListener("voiceschanged", load);
  }, []);
  useEffect(() => {
    if (!message) return;
    const t = setTimeout(() => setMessage(""), 2600);
    return () => clearTimeout(t);
  }, [message]);
  async function update(p: Partial<Profile>) {
    try {
      await db.profiles.put({ ...profile, ...p });
      setMessage("Saved.");
      setError("");
    } catch {
      setError("Preferences could not be saved. Please try again.");
    }
  }
  async function backup() {
    try {
      await downloadBackup();
      await db.profiles.put({ ...profile, lastBackupAt: Date.now() });
      setMessage("Your backup is ready. Keep it somewhere safe.");
    } catch {
      setError("The backup could not be created. Please try again.");
    }
  }
  async function restore() {
    if (!restoreFile) return;
    try {
      if (restoreFile.size > 20000000)
        throw new Error("Choose a backup smaller than 20 MB.");
      await importRecord(JSON.parse(await restoreFile.text()));
      setMessage(
        "Backup restored. Matching records were updated; other records were kept.",
      );
      setRestoreFile(null);
    } catch (e) {
      setError((e as Error).message);
    }
  }
  return (
    <div className="settings-page">
      <header className="page-head">
        <p className="eyebrow">Settings</p>
        <h1>Your study room.</h1>
      </header>
      <div className="settings-layout">
        <section>
          <h2>Learning</h2>
          <label className="check-field">
            <input
              type="checkbox"
              checked={profile.mascotEnabled !== false}
              onChange={(e) => void update({ mascotEnabled: e.target.checked })}
            />
            <span>
              Show Sayo
              <small>A companion for learning, practice, and feedback.</small>
            </span>
          </label>
          <label className="check-field">
            <input
              type="checkbox"
              checked={profile.mascotMotion !== false}
              onChange={(e) => void update({ mascotMotion: e.target.checked })}
            />
            <span>
              Animate Sayo
              <small>
                Your device’s reduced-motion setting always takes priority.
              </small>
            </span>
          </label>
          <label className="check-field">
            <input
              type="checkbox"
              checked={profile.showStreak !== false}
              onChange={(e) => void update({ showStreak: e.target.checked })}
            />
            <span>
              Show days in a row
              <small>
                A gentle count of study days. It never blocks or punishes
                anything.
              </small>
            </span>
          </label>
          <button className="text-button" onClick={onMascot}>
            Meet Sayo · her moods and phrases <Arrow />
          </button>
          <fieldset className="segmented">
            <legend>Where to begin each day</legend>
            {paths.map((p) => (
              <button
                key={p.id}
                aria-pressed={pathOf(profile) === p.id}
                onClick={() => void update({ path: p.id })}
              >
                {p.title}
              </button>
            ))}
          </fieldset>
          <label className="field">
            Daily time
            <select
              value={profile.minutes}
              onChange={(e) => void update({ minutes: +e.target.value })}
            >
              {[10, 20, 30, 45, 60].map((n) => (
                <option key={n} value={n}>
                  {n} minutes
                </option>
              ))}
            </select>
          </label>
          <label className="check-field">
            <input
              type="checkbox"
              checked={profile.pinyin}
              onChange={(e) => void update({ pinyin: e.target.checked })}
            />
            <span>
              Show pinyin in phrase lessons
              <small>Recognition checks always begin without pinyin.</small>
            </span>
          </label>
          <label className="check-field">
            <input
              type="checkbox"
              checked={profile.toneColors !== false}
              onChange={(e) => void update({ toneColors: e.target.checked })}
            />
            <span>
              Colour pinyin by tone
              <small>
                <Pinyin text="mā má mǎ mà ma" /> · a visual cue for each tone.
              </small>
            </span>
          </label>
          <label className="check-field">
            <input
              type="checkbox"
              checked={profile.quiet}
              onChange={(e) => void update({ quiet: e.target.checked })}
            />
            <span>
              Quiet mode
              <small>
                Mute automatic Sayo comments and use text alternatives.
                Tap-to-hear still works.
              </small>
            </span>
          </label>
          <label className="field">
            Sayo’s voice
            <select
              value={sayoVoiceURI(profile.voiceURI)}
              onChange={(e) => void update({ voiceURI: e.target.value })}
            >
              <option value="local:clear">Clear · precise and calm</option>
              <option value="local:cool">Cool · low and unhurried</option>
              <option value="local:playful">Playful · a little smile</option>
              {voices.map((v) => (
                <option value={v.voiceURI} key={v.voiceURI}>
                  {v.name}
                  {v.localService ? " · on device" : " · online service"}
                </option>
              ))}
            </select>
          </label>
          <AudioButton
            text="你好，很高兴认识你。"
            voiceURI={profile.voiceURI}
            label="Preview voice"
          />
          <p className="small">
            One Sayo voice, three reading styles. Her reactions choose their own
            mood. Device voices are a fallback; online device voices may send
            text to your operating system’s speech service.
          </p>
        </section>
        <section>
          <h2>Account</h2>
          <AccountPanel onChange={update} />
          <SyncPanel />
          <h2>Your data</h2>
          <p>
            Learning records always stay available in this browser. Cloud sync
            is optional. Keep an exported backup before clearing browser data.
          </p>
          <button className="button secondary" onClick={() => void backup()}>
            <DownloadSimple size={18} /> Export learning record
          </button>
          <label className="field">
            Restore a backup
            <input
              type="file"
              accept="application/json,.json"
              onChange={(e) => {
                setRestoreFile(e.target.files?.[0] ?? null);
                setError("");
              }}
            />
          </label>
          {restoreFile && (
            <div className="confirm-box">
              <p>
                Restore <strong>{restoreFile.name}</strong>? Matching records
                will be replaced by this backup. Other records stay.
              </p>
              <button
                className="button secondary"
                onClick={() => void restore()}
              >
                Restore this backup
              </button>
            </div>
          )}
          <OfflinePanel />
          <h3>Voice privacy</h3>
          <p>
            No recording leaves the tab. Recordings are temporary and not
            included in backups.
          </p>
          <h3>Start again</h3>
          {reset ? (
            <div className="confirm-box danger">
              <p>
                This removes all learning records and preferences from this
                browser. It also signs you out. Cloud data is not deleted.
                Export first if you want to keep a local copy.
              </p>
              <button
                className="button danger"
                onClick={async () => {
                  try {
                    await detachSync();
                    await signOut();
                    await db.transaction("rw", db.tables, async () => {
                      for (const table of db.tables) await table.clear();
                    });
                  } catch {
                    setError(
                      "The reset could not be completed. Please try again.",
                    );
                  }
                }}
              >
                Delete my local learning data
              </button>
              <button className="text-button" onClick={() => setReset(false)}>
                Cancel
              </button>
            </div>
          ) : (
            <button className="text-button" onClick={() => setReset(true)}>
              <ArrowCounterClockwise size={17} /> Reset learning data
            </button>
          )}
          <p className="small about-note">
            {brand.name} {brand.zh} · early learning release. Original
            curriculum drafts. No official certification, validated fluency
            estimate, or automated pronunciation assessment. Stroke data from
            Make Me a Hanzi (Arphic Public License).
          </p>
        </section>
      </div>
      <p
        className={`toast ${message ? "show" : ""}`}
        role="status"
        aria-live="polite"
      >
        {message}
      </p>
      {error && (
        <p className="inline-error" role="alert">
          {error}
        </p>
      )}
    </div>
  );
}

function AccountPanel({
  onChange,
}: {
  onChange: (p: Partial<Profile>) => Promise<void>;
}) {
  const [error, setError] = useState("");
  const a = useSyncStatus().account;
  if (a)
    return (
      <div className="account-card">
        <span className="account-avatar" aria-hidden>
          {(a.name || a.email || "?").charAt(0).toUpperCase()}
        </span>
        <span className="account-body">
          <strong>{a.name || a.email}</strong>
          <span className="small">
            Signed in with{" "}
            {a.provider === "email"
              ? "email"
              : a.provider === "google"
                ? "Google"
                : "Apple"}
            {a.name && a.email ? ` · ${a.email}` : ""}
          </span>
        </span>
        <button
          className="text-button"
          onClick={async () => {
            try {
              await detachSync();
              await signOut();
              await onChange({ account: null, entry: "guest" });
            } catch {
              setError("Sign-out didn’t finish. Try again.");
            }
          }}
        >
          Sign out
        </button>
        {error && (
          <p className="inline-error" role="alert">
            {error}
          </p>
        )}
      </div>
    );
  return (
    <div className="account-card is-guest">
      <span className="account-body">
        <strong>Studying without an account</strong>
        <span className="small">
          {authConfigured
            ? "Sign in so we know it’s you. Your progress here is kept."
            : "Accounts aren’t switched on yet. Everything is saved in this browser."}
        </span>
      </span>
      {authConfigured && (
        <span className="account-actions">
          <button
            className="button secondary"
            disabled={!oauthConfigured("google")}
            onClick={() =>
              void signInWith("google").catch((e) =>
                setError((e as Error).message),
              )
            }
          >
            Google
          </button>
          {oauthConfigured("apple") && (
            <button
              className="button secondary"
              onClick={() =>
                void signInWith("apple").catch((e) =>
                  setError((e as Error).message),
                )
              }
            >
              Apple
            </button>
          )}
        </span>
      )}
      {error && (
        <p className="inline-error" role="alert">
          {error}
        </p>
      )}
    </div>
  );
}
