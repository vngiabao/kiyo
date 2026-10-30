import { useEffect, useState } from "react";

/**
 * kiyo.gbaonvo.com sits behind Cloudflare Access. The service worker keeps opening the
 * app from its cache after that sign-in expires, but every network request (Sayo's
 * recordings not saved yet, sync, reminders) is then redirected to the sign-in page and
 * fails, so audio would quietly fall back to the device voice. This notices that case.
 */
let expired = false;
const listeners = new Set<(value: boolean) => void>();
let checking: Promise<boolean> | null = null;

/** True when the network answered with the sign-in redirect (never true offline). */
export function checkSignIn(): Promise<boolean> {
  if (typeof fetch === "undefined" || !navigator.onLine) return Promise.resolve(expired);
  checking ??= fetch("/api/push/key", { redirect: "manual", cache: "no-store", credentials: "same-origin" })
    .then((res) => res.type === "opaqueredirect" || res.status === 401 || res.status === 403)
    .catch(() => false)
    .then((value) => {
      checking = null;
      if (value !== expired) {
        expired = value;
        listeners.forEach((l) => l(value));
      }
      return value;
    });
  return checking;
}

/** Goes through the sign-in page, then back to Today (the Worker answers /api/signin). */
export const signInAgain = () => location.assign("/api/signin");

export function useSignInExpired() {
  const [value, setValue] = useState(expired);
  useEffect(() => {
    listeners.add(setValue);
    const check = () => {
      if (document.visibilityState === "visible") void checkSignIn();
    };
    check();
    document.addEventListener("visibilitychange", check);
    window.addEventListener("online", check);
    return () => {
      listeners.delete(setValue);
      document.removeEventListener("visibilitychange", check);
      window.removeEventListener("online", check);
    };
  }, []);
  return value;
}
