/* Sayo's evening note (imported into the generated service worker; see vite.config.ts).
 * The push itself carries no learning data. This worker reads the learner's own progress
 * from the app's local database (tingjian-v1) and picks what Sayo says:
 *   studied today            → "done"   (tomorrow's note is sealed)
 *   last night's note opened → "note"   (names the character inside)
 *   reviews due              → "review" (how many)
 *   otherwise                → "evening"
 * Lines drafted with GPT, edited for Sayo's voice; Chinese at HSK 1-2. */
const SAYO = {
  evening: [
    ["我在这里等你。", "Wǒ zài zhèlǐ děng nǐ.", "Your next lesson is ready. Two minutes is enough to start."],
    ["今天学一点吧。", "Jīntiān xué yìdiǎn ba.", "A little today beats a lot on Sunday."],
    ["来学两分钟。", "Lái xué liǎng fēnzhōng.", "Two minutes. I'll keep it short."],
    ["现在开始吧。", "Xiànzài kāishǐ ba.", "Your next lesson is waiting. Start small."],
    ["学一点就好。", "Xué yìdiǎn jiù hǎo.", "Just a little. That counts."],
  ],
  note: [
    ["现在可以看了。", "Xiànzài kěyǐ kàn le.", "Last night's note is open. {char} is inside."],
    ["这是给你的。", "Zhè shì gěi nǐ de.", "I sealed {char} for you yesterday. Come meet it."],
    ["给你看个字。", "Gěi nǐ kàn ge zì.", "One character, sealed last night: {char}."],
    ["看看这个字吧。", "Kànkan zhège zì ba.", "Your note opened this morning. Meet {char}."],
  ],
  review: [
    ["再看看这些字。", "Zài kànkan zhèxiē zì.", "{n} reviews are due. Two minutes clears a few."],
    ["这些字你会的。", "Zhèxiē zì nǐ huì de.", "{n} reviews are waiting. You know these."],
    ["再看一次吧。", "Zài kàn yí cì ba.", "{n} things are fading. One more look keeps them."],
  ],
  done: [
    ["今天学得很好。", "Jīntiān xué de hěn hǎo.", "You studied today. Tomorrow's note is already sealed."],
    ["今天就到这里。", "Jīntiān jiù dào zhèlǐ.", "That's enough for today. Your next seal opens tomorrow."],
    ["不错嘛。", "Bú cuò ma.", "Already done today. I noticed."],
  ],
  test: [["收到了吗？", "Shōu dào le ma?", "This is how my evening note will look."]],
};

const dayKey = (t) => {
  const d = new Date(t);
  return `${d.getFullYear()}-${String(d.getMonth() + 1).padStart(2, "0")}-${String(d.getDate()).padStart(2, "0")}`;
};

function readProgress() {
  return new Promise((resolve) => {
    const empty = { profile: null, studiedToday: false, due: 0 };
    let req;
    try { req = indexedDB.open("tingjian-v1"); } catch { return resolve(empty); }
    req.onerror = () => resolve(empty);
    req.onsuccess = () => {
      const db = req.result;
      try {
        const stores = ["profiles", "sessions", "attempts", "memories"].filter((s) => db.objectStoreNames.contains(s));
        const tx = db.transaction(stores, "readonly");
        const out = { profile: null, studiedToday: false, due: 0 };
        const start = new Date(); start.setHours(0, 0, 0, 0);
        const since = IDBKeyRange.lowerBound(start.getTime());
        if (stores.includes("profiles")) tx.objectStore("profiles").get("learner").onsuccess = (e) => { out.profile = e.target.result ?? null; };
        if (stores.includes("sessions")) tx.objectStore("sessions").index("completedAt").count(since).onsuccess = (e) => { if (e.target.result) out.studiedToday = true; };
        if (stores.includes("attempts")) tx.objectStore("attempts").index("at").count(since).onsuccess = (e) => { if (e.target.result) out.studiedToday = true; };
        if (stores.includes("memories")) {
          const skip = new Set(["conversation", "speaking", "recall", "media"]);
          tx.objectStore("memories").index("due").openCursor(IDBKeyRange.upperBound(Date.now())).onsuccess = (e) => {
            const c = e.target.result;
            if (!c) return;
            if (!skip.has(c.value.modality)) out.due++;
            c.continue();
          };
        }
        tx.oncomplete = () => { db.close(); resolve(out); };
        tx.onerror = () => { db.close(); resolve(out); };
      } catch { db.close(); resolve(empty); }
    };
  });
}

function pick(list, seed) {
  return list[Math.abs(seed) % list.length];
}

async function sayoNote(kind) {
  const p = await readProgress();
  const today = dayKey(Date.now());
  const seed = Number(today.replace(/-/g, ""));
  const note = p.profile && p.profile.sealedNote;
  let group = "evening", fill = {};
  if (kind === "test") group = "test";
  else if (p.studiedToday) group = "done";
  else if (note && note.sealedOn < today && note.hanzi) { group = "note"; fill = { char: note.hanzi }; }
  else if (p.due > 0) { group = "review"; fill = { n: String(p.due) }; }
  const [zh, py, en] = pick(SAYO[group], seed);
  const body = `${py}\n${en.replace("{char}", fill.char ?? "").replace("{n}", fill.n ?? "")}`;
  return {
    title: `小夜 · ${zh}`,
    options: {
      body,
      lang: "zh-CN",
      icon: "/brand/app-icon-93e5cbf04055-192.png",
      tag: "sayo-daily",
      renotify: true,
      data: { url: "/?from=note#today" },
    },
  };
}

self.addEventListener("push", (event) => {
  let kind = "daily";
  try { kind = (event.data && event.data.json().kind) || "daily"; } catch { /* plain push */ }
  event.waitUntil(sayoNote(kind).then(({ title, options }) => self.registration.showNotification(title, options)));
});

self.addEventListener("notificationclick", (event) => {
  event.notification.close();
  const url = (event.notification.data && event.notification.data.url) || "/#today";
  event.waitUntil(
    self.clients.matchAll({ type: "window", includeUncontrolled: true }).then((wins) => {
      const open = wins.find((w) => new URL(w.url).origin === self.location.origin);
      if (open) return open.focus().then((w) => w && w.navigate(url));
      return self.clients.openWindow(url);
    }),
  );
});
