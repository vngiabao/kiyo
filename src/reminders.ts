// Sayo's daily note on this device: Web Push through the Worker (workers/push.ts), with a
// calendar file as the fallback where push is unavailable (iPhone before "Add to Home Screen").
import { db } from "./db";
import type { Profile } from "./types";

export const localDay = (t = Date.now()) => {
  const d = new Date(t);
  return `${d.getFullYear()}-${String(d.getMonth() + 1).padStart(2, "0")}-${String(d.getDate()).padStart(2, "0")}`;
};

export type ReminderSupport = "push" | "install-first" | "none";
export function reminderSupport(): ReminderSupport {
  if (typeof window === "undefined") return "none";
  const ios = /iPhone|iPad|iPod/.test(navigator.userAgent) || (navigator.platform === "MacIntel" && navigator.maxTouchPoints > 1);
  const standalone = matchMedia("(display-mode: standalone)").matches || (navigator as Navigator & { standalone?: boolean }).standalone === true;
  if ("serviceWorker" in navigator && "PushManager" in window && "Notification" in window) return "push";
  return ios && !standalone ? "install-first" : "none";
}

const fromB64url = (s: string) => {
  const raw = atob(s.replace(/-/g, "+").replace(/_/g, "/") + "===".slice((s.length + 3) % 4));
  return Uint8Array.from(raw, (c) => c.charCodeAt(0));
};
async function api(path: string, body?: object) {
  const res = await fetch(path, body ? { method: "POST", headers: { "Content-Type": "application/json" }, body: JSON.stringify(body), credentials: "same-origin" } : { credentials: "same-origin" });
  const data = (await res.json().catch(() => ({}))) as { error?: string; key?: string | null };
  if (!res.ok) throw new Error(data.error ?? `The server answered ${res.status}.`);
  return data;
}

/** Ask permission, subscribe this device and register the time with the Worker. */
export async function enableReminder(profile: Profile, time: string) {
  if (reminderSupport() !== "push") throw new Error("This browser can't receive notifications. Use “Add to calendar” instead.");
  const permission = await Notification.requestPermission();
  if (permission !== "granted") throw new Error("Notifications are blocked for Kiyo. Allow them in your browser's site settings, then try again.");
  const { key } = await api("/api/push/key");
  if (!key) throw new Error("Reminders aren't set up on the server yet.");
  const reg = await navigator.serviceWorker.ready;
  const sub = (await reg.pushManager.getSubscription()) ?? (await reg.pushManager.subscribe({ userVisibleOnly: true, applicationServerKey: fromB64url(key) }));
  const tz = Intl.DateTimeFormat().resolvedOptions().timeZone;
  await api("/api/push/subscribe", { subscription: sub.toJSON(), time, tz });
  await db.profiles.put({ ...profile, reminder: { enabled: true, time, endpoint: sub.endpoint }, reminderAskedAt: Date.now() });
}

export async function disableReminder(profile: Profile) {
  const reg = await navigator.serviceWorker?.ready.catch(() => null);
  const sub = await reg?.pushManager.getSubscription();
  const endpoint = sub?.endpoint ?? profile.reminder?.endpoint;
  if (endpoint) await api("/api/push/unsubscribe", { endpoint }).catch(() => undefined);
  await sub?.unsubscribe().catch(() => undefined);
  await db.profiles.put({ ...profile, reminder: { enabled: false, time: profile.reminder?.time ?? "20:00" } });
}

/** Ask the Worker to send this device a note right now. */
export async function sendTestNote(profile: Profile) {
  const reg = await navigator.serviceWorker.ready;
  const endpoint = (await reg.pushManager.getSubscription())?.endpoint ?? profile.reminder?.endpoint;
  if (!endpoint) throw new Error("Turn the daily note on first.");
  await api("/api/push/test", { endpoint });
}

/** A daily calendar event with an alert: the fallback that works on every phone. */
export function downloadCalendar(time: string) {
  const [h, m] = time.split(":");
  const start = new Date();
  start.setHours(Number(h), Number(m), 0, 0);
  const stamp = (d: Date) => `${d.getFullYear()}${String(d.getMonth() + 1).padStart(2, "0")}${String(d.getDate()).padStart(2, "0")}T${String(d.getHours()).padStart(2, "0")}${String(d.getMinutes()).padStart(2, "0")}00`;
  const end = new Date(start.getTime() + 10 * 60_000);
  const ics = [
    "BEGIN:VCALENDAR", "VERSION:2.0", "PRODID:-//Kiyo//Sayo's note//EN", "CALSCALE:GREGORIAN",
    "BEGIN:VEVENT",
    `UID:kiyo-sayo-note-${Date.now()}@kiyo.gbaonvo.com`,
    `DTSTAMP:${stamp(new Date())}`,
    `DTSTART:${stamp(start)}`,
    `DTEND:${stamp(end)}`,
    "RRULE:FREQ=DAILY",
    "SUMMARY:小夜 · Two minutes of Mandarin",
    "DESCRIPTION:Sayo's note is waiting. https://kiyo.gbaonvo.com/#today",
    "URL:https://kiyo.gbaonvo.com/#today",
    "BEGIN:VALARM", "ACTION:DISPLAY", "DESCRIPTION:Sayo's note is waiting", "TRIGGER:PT0M", "END:VALARM",
    "END:VEVENT", "END:VCALENDAR",
  ].join("\r\n");
  const url = URL.createObjectURL(new Blob([ics], { type: "text/calendar" }));
  const a = Object.assign(document.createElement("a"), { href: url, download: "kiyo-sayo-note.ics" });
  a.click();
  setTimeout(() => URL.revokeObjectURL(url), 1000);
}
