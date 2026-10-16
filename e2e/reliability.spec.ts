import { test, expect, type Page } from "@playwright/test";
import AxeBuilder from "@axe-core/playwright";

test("a waiting app update requires an explicit refresh", async ({ page }) => {
  test.skip(!process.env.APP_URL, "Update notice is production-only.");
  await page.addInitScript(() => {
    const registration = Object.assign(new EventTarget(), {
      waiting: { postMessage: (message: unknown) => {
        localStorage.setItem("test-update-message", JSON.stringify(message));
      } },
      installing: null,
      update: async () => {},
    });
    const worker = Object.assign(new EventTarget(), {
      controller: {},
      ready: Promise.resolve(registration),
      register: async () => registration,
    });
    Object.defineProperty(navigator, "serviceWorker", { value: worker });
  });
  await page.goto("/");
  await expect(page.getByRole("status")).toHaveText(
    "An update is ready. Refresh when you’re ready.",
  );
  expect(await page.evaluate(() => localStorage.getItem("test-update-message"))).toBeNull();
  await page.getByRole("button", { name: "Refresh", exact: true }).click();
  expect(await page.evaluate(() => localStorage.getItem("test-update-message"))).toBe(
    JSON.stringify({ type: "SKIP_WAITING" }),
  );
  await expect(page.getByRole("heading", { name: "Mandarin, crystal clear." })).toBeVisible();
});
/** First screen is sign-in; tests study as a guest. */
async function enter(page: Page) {
  const guest = page.getByRole("button", { name: /Start without an account/ });
  await guest.waitFor({ timeout: 4000 }).catch(() => undefined);
  if (await guest.isVisible()) await guest.click();
}

async function start(page: Page, quiet = true) {
  await page.goto("/");
  await enter(page);
  await page.getByRole("button", { name: "Continue", exact: true }).click();
  await page.getByRole("radio", { name: /Sound first/ }).click();
  await page.getByRole("button", { name: "Continue", exact: true }).click();
  if (quiet)
    await page.getByRole("checkbox", { name: "Start in quiet mode" }).check();
  await page.getByRole("button", { name: "Hear your first words" }).click();
  await expect(
    page.getByRole("heading", { name: "First, just listen." }),
  ).toBeVisible();
}
async function attempts(page: Page) {
  return page.evaluate(
    () =>
      new Promise<any[]>((resolve, reject) => {
        const request = indexedDB.open("tingjian-v1");
        request.onsuccess = () => {
          const database = request.result;
          const get = database
            .transaction("attempts")
            .objectStore("attempts")
            .getAll();
          get.onsuccess = () => {
            resolve(get.result);
            database.close();
          };
          get.onerror = () => reject(get.error);
        };
        request.onerror = () => reject(request.error);
      }),
  );
}

test("audio must finish, interrupted playback does not count, unaided answers persist", async ({
  page,
}) => {
  await start(page);
  const next = page.getByRole("button", { name: "Continue", exact: true });
  await expect(next).toBeDisabled();
  await page.getByRole("button", { name: "Play Mandarin audio" }).click();
  await page.getByRole("button", { name: "Stop audio" }).click();
  await expect(next).toBeDisabled();
  await page.getByRole("button", { name: "Play Mandarin audio" }).click();
  await expect(next).toBeEnabled({ timeout: 12000 });
  await next.click();
  await next.click();
  // The second phrase arrives before the first one is checked.
  await page.getByRole("button", { name: "Play Mandarin audio" }).click();
  await expect(next).toBeEnabled({ timeout: 12000 });
  await next.click();
  await next.click();
  await expect(page.locator(".choice").first()).toBeDisabled();
  await page.getByRole("button", { name: "Play Mandarin audio" }).click();
  await expect(page.locator(".choice").first()).toBeEnabled({ timeout: 12000 });
  await page.locator(".choice").filter({ hasText: "Hello" }).click();
  await page.getByRole("button", { name: "Check", exact: true }).click();
  await expect(page.getByText("Right.", { exact: true })).toBeVisible();
  expect(await attempts(page)).toMatchObject([
    { modality: "listening", support: "none", correct: true },
  ]);
  await page.reload();
  expect(await attempts(page)).toHaveLength(1);
});

test("conversation help remains supported after hiding it", async ({
  page,
}) => {
  await start(page);
  await page.getByRole("button", { name: "Save and exit" }).click();
  await page.locator(".main-nav").getByRole("button", { name: "Speak", exact: true }).click();
  await page.getByRole("button", { name: "Begin conversation" }).click();
  await page.getByRole("button", { name: "Show transcript & help" }).click();
  await page.getByRole("button", { name: "Hide support" }).click();
  await page.getByRole("textbox").fill("你好");
  await page.getByRole("button", { name: "Reply", exact: true }).click();
  await expect(page.locator(".turn-count")).toHaveText("2 / 4");
  expect(await attempts(page)).toMatchObject([
    { modality: "conversation", support: "transcript" },
  ]);
});

test("microphone refusal offers a usable alternative", async ({ page }) => {
  await page.addInitScript(() => {
    Object.defineProperty(navigator.mediaDevices, "getUserMedia", {
      value: () =>
        Promise.reject(new DOMException("denied", "NotAllowedError")),
    });
  });
  await start(page, false);
  await page.getByRole("button", { name: "Save and exit" }).click();
  await page.locator(".main-nav").getByRole("button", { name: "Practice", exact: true }).click();
  await page.getByRole("tab", { name: "Pronunciation" }).click();
  await page.getByRole("button", { name: "Record yourself" }).click();
  await expect(page.getByRole("alert")).toContainText(
    "practice aloud without recording",
  );
  await expect(
    page.getByRole("button", { name: "Try tone listening" }),
  ).toBeEnabled();
});

test("primary desktop and mobile surfaces meet automated WCAG AA checks", async ({
  page,
}) => {
  // Ten full-page axe scans over the HSK 1–6 course need more than the default 40 s.
  test.setTimeout(120_000);
  // Audit settled colours, not frames of a fade-in.
  await page.emulateMedia({ reducedMotion: "reduce" });
  await page.goto("/");
  await enter(page);
  expect(
    (
      await new AxeBuilder({ page })
        .withTags(["wcag2a", "wcag2aa", "wcag21aa"])
        .analyze()
    ).violations,
  ).toEqual([]);
  await start(page);
  expect(
    (
      await new AxeBuilder({ page })
        .withTags(["wcag2a", "wcag2aa", "wcag21aa"])
        .analyze()
    ).violations,
  ).toEqual([]);
  await page.getByRole("button", { name: "Save and exit" }).click();
  for (const width of [1440, 375]) {
    await page.setViewportSize({ width, height: 1000 });
    for (const name of ["Today", "Read", "Listen", "Speak"]) {
      await page.getByRole("navigation").getByRole("button", { name, exact: true }).first().click();
      await page.locator("main h1").waitFor();
      await page.mouse.move(0, 0);
      expect(
        (
          await new AxeBuilder({ page })
            .withTags(["wcag2a", "wcag2aa", "wcag21aa"])
            .analyze()
        ).violations,
        `${name} at ${width}`,
      ).toEqual([]);
    }
  }
});

test("installed production shell, routes and bundled audio work offline", async ({
  page,
  context,
}) => {
  test.skip(
    !process.env.APP_URL,
    "Run against the production preview with APP_URL.",
  );
  await start(page);
  await page.getByRole("button", { name: "Save and exit" }).click();
  await page.evaluate(() => navigator.serviceWorker.ready);
  await page.reload();
  await expect(
    page.getByRole("heading", { level: 1, name: /Good (morning|afternoon|evening)|Still up/ }),
  ).toBeVisible();
  await page.locator(".lead").getByRole("button", { name: "Continue" }).click();
  const firstPlay = page.waitForResponse(
    (r) => r.url().includes("/audio-v2/") && r.ok(),
  );
  await page.getByRole("button", { name: "Play Mandarin audio" }).click();
  const audioUrl = (await firstPlay).url();
  await expect.poll(() => page.evaluate(async (url) =>
    Boolean(await caches.match(url)), audioUrl)).toBe(true);
  await page.getByRole("button", { name: "Save and exit" }).click();
  await context.setOffline(true);
  await page.reload();
  await expect(
    page.getByText("Offline · local learning available"),
  ).toBeVisible();
  await page.locator(".lead").getByRole("button", { name: "Continue" }).click();
  const offlinePlay = page.waitForResponse(
    (r) => r.url() === audioUrl && r.ok(),
  );
  await page.getByRole("button", { name: "Play Mandarin audio" }).click();
  await offlinePlay;
  await expect(
    page.getByRole("button", { name: "Continue", exact: true }),
  ).toBeEnabled({ timeout: 12000 });
  await page.getByRole("button", { name: "Save and exit" }).click();
  await page.locator(".main-nav").getByRole("button", { name: "Media", exact: true }).click();
  await expect(
    page.getByRole("heading", { name: "Before they leave." }),
  ).toBeVisible();
  await context.setOffline(false);
  const callbackPath = "/cdn-cgi/access/authorized?kiyo-test";
  await page.route(`**${callbackPath}`, async (route) => route.fulfill({
    status: 200,
    contentType: "text/html",
    body: "<h1>Access callback reached the network</h1>",
  }));
  const callback = await page.goto(callbackPath);
  await expect(page.getByRole("heading", { name: "Access callback reached the network" })).toBeVisible();
  expect(callback?.fromServiceWorker()).toBe(false);
});

test("complete beginner lesson saves a session and starts the next lesson", async ({
  page,
}) => {
  await start(page);
  // Walk every step with support shown (audio is covered by its own test).
  // Picking visible options exercises save and feedback; correctness is tested in unit tests.
  const seen = new Set<string>();
  const button = (name: string | RegExp) => page.getByRole("button", { name, exact: typeof name === "string" });
  const check = async () => {
    await button("Check").click();
    await expect(page.locator(".verdict strong")).toBeVisible();
  };
  // The finish screen animates in, so test for it being mounted rather than already visible.
  for (let guard = 0; guard < 40 && !(await page.locator(".level-up, .lesson-done").count()); guard++) {
    const kind = ((await page.locator(".exercise").getAttribute("class")) ?? "").match(/kind-(\w+)/)?.[1] ?? "";
    seen.add(kind);
    const show = page.getByRole("button", { name: /^(Show the words|Show pinyin)$/ });
    if (await show.isVisible()) await show.click();
    if (kind === "recall") {
      await button("Reveal phrase").click();
      await button("I had it").click();
    } else if (kind === "record") {
      await button("I rehearsed it silently").click();
    } else if (["choice", "read", "truefalse", "reply"].includes(kind)) {
      await page.locator(".choice").first().click();
      await check();
    } else if (kind === "dialogue") {
      for (const group of await page.locator(".task-question .choices").all()) await group.locator(".choice").first().click();
      await check();
      await expect(page.locator(".transcript")).toBeVisible();
    } else if (kind === "listenfill") {
      await page.locator(".fill-slot input").fill("xiexie");
      await check();
    } else if (kind === "cloze") {
      while (await button("Check").isDisabled()) await page.locator(".token-bank button:enabled").first().click();
      await check();
    } else if (kind === "reorder") {
      while (await button("Check").isDisabled()) await page.locator(".token-bank button:enabled").first().click();
      await check();
    }
    const count = await page.locator(".focus-count").textContent();
    await button("Continue").click();
    await expect(page.locator(".focus-count")).not.toHaveText(count ?? "");
  }
  expect([...seen]).toEqual(expect.arrayContaining(["hear", "notice", "choice", "dialogue", "truefalse", "reply", "listenfill", "cloze", "recall", "record", "read"]));
  // Shown words make listening tasks supported, never unaided.
  expect((await attempts(page)).filter((a) => /first-(d|tf1|r1|f1)$/.test(a.context))).toEqual(
    expect.arrayContaining([expect.objectContaining({ modality: "listening", support: "transcript" })]),
  );
  // A first finish is a level-up that names what you can now do.
  await expect(page.getByText("Now you can")).toBeVisible();
  await expect(page.locator(".level-number")).toHaveText("2");
  await page.getByRole("button", { name: "Continue", exact: true }).click();
  await page.reload();
  await expect(page.locator(".lead")).toContainText("One syllable, four meanings");
});

test("welcome sign-in screen is accessible and never blocks starting", async ({ page }) => {
  await page.emulateMedia({ reducedMotion: "reduce" });
  for (const width of [1440, 375]) {
    await page.setViewportSize({ width, height: 900 });
    await page.goto("/");
    await expect(page.getByRole("heading", { name: "Mandarin, crystal clear." })).toBeVisible();
    await expect(page.getByText("你好！我是小夜。")).toBeVisible();
    expect(
      (await new AxeBuilder({ page }).withTags(["wcag2a", "wcag2aa", "wcag21aa"]).analyze()).violations,
      `welcome at ${width}`,
    ).toEqual([]);
  }
  await page.getByRole("button", { name: /Start without an account/ }).click();
  await expect(page.getByPlaceholder("Your first name")).toBeVisible();
  await page.reload();
  // The choice is remembered: no second welcome.
  await expect(page.getByPlaceholder("Your first name")).toBeVisible();
});
