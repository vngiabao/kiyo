import { useEffect, useState } from "react";

export function UpdateNotice() {
  const [waiting, setWaiting] = useState<ServiceWorker | null>(null);
  const [changed, setChanged] = useState(false);

  useEffect(() => {
    if (!import.meta.env.PROD || !("serviceWorker" in navigator)) return;
    let active = true;
    let previousController = navigator.serviceWorker.controller;
    const controllerChanged = () => {
      const next = navigator.serviceWorker.controller;
      if (active && previousController && next !== previousController) setChanged(true);
      previousController = next;
    };
    navigator.serviceWorker.addEventListener("controllerchange", controllerChanged);
    let removeListeners = () => {};
    void navigator.serviceWorker.ready.then((registration) => {
      if (!active) return;
      const check = () => {
        if (active && registration.waiting && navigator.serviceWorker.controller)
          setWaiting(registration.waiting);
      };
      const found = () => {
        const installing = registration.installing;
        installing?.addEventListener("statechange", check);
        removeListeners = () => {
          registration.removeEventListener("updatefound", found);
          installing?.removeEventListener("statechange", check);
        };
      };
      registration.addEventListener("updatefound", found);
      removeListeners = () => registration.removeEventListener("updatefound", found);
      found();
      check();
      // Check on opening the app; never replace the running lesson automatically.
      void registration.update().catch(() => {});
    });
    return () => {
      active = false;
      navigator.serviceWorker.removeEventListener("controllerchange", controllerChanged);
      removeListeners();
    };
  }, []);

  if (!waiting && !changed) return null;
  const refresh = () => {
    if (changed || waiting?.state === "activated" || waiting?.state === "redundant") {
      location.reload();
      return;
    }
    navigator.serviceWorker.addEventListener(
      "controllerchange",
      () => location.reload(),
      { once: true },
    );
    waiting?.postMessage({ type: "SKIP_WAITING" });
  };
  return (
    <aside className="update-notice" aria-label="App update">
      <p role="status">An update is ready. Refresh when you’re ready.</p>
      <button className="button ghost" onClick={refresh}>Refresh</button>
    </aside>
  );
}
