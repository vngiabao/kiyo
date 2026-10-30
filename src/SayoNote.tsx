import { useEffect, useRef, useState } from "react";
import { db } from "./db";
import { charByHanzi, type HanziEntry } from "./hanzi";
import type { Profile } from "./types";
import { AudioButton, Arrow, Pinyin } from "./components";
import { MoSays, moLines } from "./Mascot";
import { sceneById } from "./sayo-lines";
import { gsap, reducedMotion, useGSAP } from "./motion";
import { sfx } from "./sfx";
import {
  disableReminder,
  downloadCalendar,
  enableReminder,
  localDay,
  reminderSupport,
  sendTestNote,
} from "./reminders";

// The seal flips once a day, not every time you come back to Today.
const FLIP_KEY = "kiyo-note-flipped";
const flippedToday = (day: string) => { try { return sessionStorage.getItem(FLIP_KEY) === day; } catch { return false; } };
const markFlipped = (day: string) => { try { sessionStorage.setItem(FLIP_KEY, day); } catch { /* private mode */ } };

const clock = (time: string) =>
  new Date(`2000-01-01T${time}:00`).toLocaleTimeString([], { hour: "numeric", minute: "2-digit" });

/**
 * Sayo's note: the reason to come back tomorrow.
 * After a study day she seals tomorrow's character; the next day, before you study,
 * the seal opens on Today with the character, her voice and a two-minute start.
 */
export function SayoNote({
  profile, featured, lessonId, studiedToday, due, onLesson, onReview,
}: {
  profile: Profile;
  featured?: HanziEntry;
  lessonId: string;
  studiedToday: boolean;
  due: number;
  onLesson: (id: string) => void;
  onReview: () => void;
}) {
  const today = localDay();
  const note = profile.sealedNote;
  // Seal tomorrow's character once today counts (and keep it current while you study).
  useEffect(() => {
    if (!studiedToday || !featured) return;
    if (note?.sealedOn === today && note.hanzi === featured.hanzi && note.lessonId === lessonId) return;
    void db.profiles.update("learner", { sealedNote: { hanzi: featured.hanzi, lessonId, sealedOn: today } });
  }, [studiedToday, featured, lessonId, note, today]);
  const open = !!note && note.sealedOn < today && !studiedToday;
  const sealed = studiedToday && note?.sealedOn === today;
  // When the sealed character is also today's lead lesson, the lead card above already
  // shows it, its sound and Continue; the note only names it.
  const inLead = open && featured?.hanzi === note!.hanzi;
  const entry = note ? charByHanzi[note.hanzi] : undefined;
  const root = useRef<HTMLElement>(null);
  useGSAP(
    () => {
      if (!open || reducedMotion() || flippedToday(today)) return;
      markFlipped(today);
      // Starts after the page's own rise() so the two motions don't stack.
      gsap.timeline({ delay: 0.2 })
        .from(".note-seal", { rotateY: 90, transformPerspective: 700, scale: 0.8, opacity: 0, duration: 0.55, ease: "back.out(1.6)", clearProps: "transform,opacity" })
        .from(".note-copy > *", { y: 10, opacity: 0, stagger: 0.06, duration: 0.35, clearProps: "transform,opacity" }, "-=0.25");
    },
    { scope: root, dependencies: [open, today] },
  );
  if (!open && !sealed) return null;
  return (
    <section ref={root} className={`sayo-note ${open ? "is-open" : "is-sealed"}`} aria-labelledby="note-title">
      <div className="note-seal" aria-hidden>
        <span lang="zh-CN">{open ? note!.hanzi : "?"}</span>
      </div>
      <div className="note-copy">
        {open ? (
          <>
            <h2 id="note-title">
              She sealed <span lang="zh-CN">{note!.hanzi}</span> for you.
            </h2>
            {inLead ? (
              <p className="note-line">It’s waiting in today’s lesson.</p>
            ) : (
              entry && (
                <p className="note-gloss">
                  <Pinyin text={entry.pinyin} /> <span>{entry.meaning}</span>
                </p>
              )
            )}
            {(!inLead || due > 0) && (
              <div className="note-actions">
                {!inLead && (
                  <button className="button" onClick={() => onLesson(note!.lessonId)}>
                    Meet <span lang="zh-CN">{note!.hanzi}</span> <Arrow />
                  </button>
                )}
                {!inLead && entry && <AudioButton text={entry.say} voiceURI={profile.voiceURI} label="Hear it" />}
                {due > 0 && (
                  <button className={`button${inLead ? "" : " secondary"}`} onClick={onReview}>
                    Two-minute review · {due}
                  </button>
                )}
              </div>
            )}
          </>
        ) : (
          <>
            <h2 id="note-title">Sayo picked tomorrow’s character.</h2>
            <p className="note-line">It opens in the morning. No peeking.</p>
            <ReminderOffer profile={profile} />
          </>
        )}
      </div>
      {/* Recorded lines only: her voice stays the approved set. */}
      <div className="note-mo">
        <MoSays state={open ? "stamp" : "peek"} say={open ? moLines.start : sceneById.run.say} size={96} side="left" />
      </div>
    </section>
  );
}

/** One question at the right moment: would you like her to message you? */
function ReminderOffer({ profile }: { profile: Profile }) {
  const [time, setTime] = useState(profile.reminder?.time ?? "20:00");
  const [busy, setBusy] = useState(false);
  const [note, setNote] = useState("");
  const [saved, setSaved] = useState(false);
  const support = reminderSupport();
  if (saved) return <p className="note-line note-ok" role="status">Saved. Open the file to add her daily alert.</p>;
  if (profile.reminder?.enabled)
    return <p className="note-line">She’ll message you at {clock(profile.reminder.time)}.</p>;
  if (profile.reminderAskedAt) return null;
  const turnOn = async () => {
    setBusy(true);
    setNote("");
    try {
      await enableReminder(profile, time);
      sfx.correct();
    } catch (e) {
      setNote((e as Error).message);
    } finally {
      setBusy(false);
    }
  };
  return (
    <div className="note-offer">
      <p className="note-line">Want a note from her tomorrow?</p>
      <div className="note-actions">
        <label className="note-time">
          <span>at</span>
          <input type="time" value={time} onChange={(e) => setTime(e.target.value || "20:00")} />
        </label>
        {support === "push" ? (
          <button className="button" disabled={busy} onClick={() => void turnOn()}>
            {busy ? "Asking…" : "Message me"}
          </button>
        ) : (
          <button className="button" onClick={() => { downloadCalendar(time); setSaved(true); void db.profiles.update("learner", { reminderAskedAt: Date.now() }); }}>
            Add a daily calendar alert
          </button>
        )}
        <button className="text-button" onClick={() => void db.profiles.update("learner", { reminderAskedAt: Date.now() })}>
          Not now
        </button>
      </div>
      {support === "install-first" && (
        <p className="note-hint">On iPhone, add Kiyo to your Home Screen (Share, then Add to Home Screen) to get her messages.</p>
      )}
      {note && <p className="note-hint is-error" role="alert">{note}</p>}
    </div>
  );
}

/** Settings → Sayo's daily note. */
export function ReminderSettings({ profile }: { profile: Profile }) {
  const [time, setTime] = useState(profile.reminder?.time ?? "20:00");
  const [busy, setBusy] = useState(false);
  const [status, setStatus] = useState<{ text: string; error?: boolean } | null>(null);
  const on = !!profile.reminder?.enabled;
  const support = reminderSupport();
  const run = async (task: () => Promise<void>, done: string) => {
    setBusy(true);
    setStatus(null);
    try {
      await task();
      setStatus({ text: done });
    } catch (e) {
      setStatus({ text: (e as Error).message, error: true });
    } finally {
      setBusy(false);
    }
  };
  return (
    <section className="reminder-settings" aria-labelledby="reminder-title">
      <h3 id="reminder-title">Sayo’s daily note</h3>
      <p className="muted">
        One short message a day at your time, from Sayo: tomorrow’s sealed character, reviews
        that are due, or a quiet “already done today”. Nothing about your progress leaves this
        device. The app picks her words locally.
      </p>
      <div className="reminder-row">
        <label className="field reminder-time">
          <span>Time</span>
          <input type="time" value={time} onChange={(e) => setTime(e.target.value || "20:00")} />
        </label>
        {support === "push" &&
          (on ? (
            <>
              <button className="button" disabled={busy} onClick={() => void run(() => enableReminder(profile, time), `Updated. She’ll message you at ${clock(time)}.`)}>
                {busy ? "Saving…" : "Save time"}
              </button>
              <button className="button secondary" disabled={busy} onClick={() => void run(() => sendTestNote(profile), "Sent. It should arrive in a few seconds.")}>
                Send a test
              </button>
              <button className="text-button" disabled={busy} onClick={() => void run(() => disableReminder(profile), "Turned off on this device.")}>
                Turn off
              </button>
            </>
          ) : (
            <button className="button" disabled={busy} onClick={() => void run(() => enableReminder(profile, time), `On. She’ll message you at ${clock(time)}.`)}>
              {busy ? "Asking…" : "Turn on"}
            </button>
          ))}
        <button className="button secondary" onClick={() => { downloadCalendar(time); setStatus({ text: "Saved. Open the file to add her daily alert." }); }}>
          {support === "push" ? "Add to calendar instead" : "Add a calendar alert"}
        </button>
      </div>
      {support === "install-first" && (
        <p className="muted">On iPhone, add Kiyo to your Home Screen first (Share, then Add to Home Screen); messages work from there.</p>
      )}
      {support === "none" && <p className="muted">This browser can’t show notifications. The calendar alert works everywhere.</p>}
      {status && (
        <p className={`reminder-status${status.error ? " is-error" : ""}`} role={status.error ? "alert" : "status"}>
          {status.text}
        </p>
      )}
    </section>
  );
}
