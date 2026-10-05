import { test, expect, type Page } from "@playwright/test";
import { readFileSync } from "node:fs";
import { voiceKey } from "../src/sayo-voice";

// Generated with scripts/voice-task-review.ts so Node need not load app JSON modules.
const fixtures = JSON.parse(
  readFileSync("output/approved-voice-rollout/tasks.json", "utf8"),
).spotChecks as {
  id: string;
  type: string;
  lessonId: string;
  lessonTitle: string;
  step: number;
  lines: { zh: string; mood: string }[];
}[];

const assets = new Map(
  Object.entries(JSON.parse(readFileSync("src/audio-assets.json", "utf8"))).map(
    ([text, voices]) => [voiceKey(text), voices as Record<string, string>],
  ),
);

async function openTask(page: Page, taskId: string) {
  const task = fixtures.find((t) => t.id === taskId)!;
  const { lessonId, step } = task;
  expect(step).toBeGreaterThanOrEqual(0);
  await page.goto("/");
  await page.getByRole("button", { name: /Start without an account/ }).click();
  await page.getByRole("button", { name: "Continue", exact: true }).click();
  await page.getByRole("button", { name: "Continue", exact: true }).click();
  await page.getByRole("checkbox", { name: "Start in quiet mode" }).check();
  await page
    .getByRole("button", { name: "Meet your first characters" })
    .click();
  await page.getByRole("button", { name: "Save and exit" }).click();
  // Seed only this disposable browser context's saved position; do not rely on fixed Continue counts.
  await page.evaluate(
    ({ lessonId, step }) =>
      new Promise<void>((resolve, reject) => {
        const request = indexedDB.open("tingjian-v1");
        request.onerror = () => reject(request.error);
        request.onsuccess = () => {
          const db = request.result;
          const tx = db.transaction("drafts", "readwrite");
          tx.objectStore("drafts").put({
            id: `lesson:${lessonId}`,
            step,
            updatedAt: Date.now(),
          });
          tx.oncomplete = () => {
            db.close();
            resolve();
          };
          tx.onerror = () => reject(tx.error);
        };
      }),
    { lessonId, step },
  );
  await page.goto("/");
  await page
    .locator(".main-nav")
    .getByRole("button", { name: "Listen", exact: true })
    .click();
  await page
    .getByRole("button", {
      name: new RegExp(
        `^${task.lessonTitle.replace(/[.*+?^${}()|[\]\\]/g, "\\$&")}\\.`,
      ),
    })
    .click();
  return task;
}

for (const id of ["names-d", "rescue-d", "meet-d"]) {
  test(`new conversation ${id} plays every line in its mapped Sayo mood without fallback`, async ({
    page,
  }) => {
    test.setTimeout(90000);
    await page.addInitScript(() => {
      Object.assign(window, {
        taskPlayback: [] as string[],
        taskRates: [] as number[],
        deviceFallbacks: 0,
      });
      const play = HTMLMediaElement.prototype.play;
      HTMLMediaElement.prototype.play = function () {
        this.addEventListener(
          "playing",
          () => {
            (window as unknown as { taskPlayback: string[] }).taskPlayback.push(
              new URL(this.currentSrc).pathname,
            );
            (window as unknown as { taskRates: number[] }).taskRates.push(
              this.playbackRate,
            );
          },
          { once: true },
        );
        return play.call(this);
      };
      speechSynthesis.speak = () => {
        (window as unknown as { deviceFallbacks: number }).deviceFallbacks++;
      };
    });
    const task = await openTask(page, id);
    const expected = task.lines.map(
      (line) => assets.get(voiceKey(line.zh))![line.mood],
    );
    await page
      .getByRole("button", { name: "Play the conversation", exact: true })
      .click();
    await expect(
      page.getByRole("button", {
        name: "Play the conversation again",
        exact: true,
      }),
    ).toBeVisible({ timeout: 60000 });
    const playback = await page.evaluate(() => ({
      clips: (window as unknown as { taskPlayback: string[] }).taskPlayback,
      fallbacks: (window as unknown as { deviceFallbacks: number })
        .deviceFallbacks,
      rates: (window as unknown as { taskRates: number[] }).taskRates,
    }));
    expect(playback.clips.slice(-expected.length)).toEqual(expected);
    expect(playback.fallbacks).toBe(0);
    if (id === "rescue-d")
      expect(playback.rates.slice(-4)).toEqual([1, 1, 0.75, 1]);
  });
}

test("a new listen-fill reuses its clear clip at slower speed with pitch preservation", async ({
  page,
}) => {
  await page.addInitScript(() => {
    Object.assign(window, { playedSettings: [] as unknown[] });
    const play = HTMLMediaElement.prototype.play;
    HTMLMediaElement.prototype.play = function () {
      this.addEventListener(
        "playing",
        () => {
          const audio = this;
          (
            window as unknown as { playedSettings: unknown[] }
          ).playedSettings.push({
            url: new URL(audio.currentSrc).pathname,
            rate: audio.playbackRate,
            preservesPitch: audio.preservesPitch,
          });
        },
        { once: true },
      );
      return play.call(this);
    };
  });
  const taskId = fixtures.find((t) => t.type === "listenfill")!.id;
  const task = await openTask(page, taskId);
  const line = task.lines[0];
  await page.getByRole("button", { name: "Slower", exact: true }).click();
  await expect
    .poll(() =>
      page.evaluate(() =>
        (window as unknown as { playedSettings: unknown[] }).playedSettings.at(
          -1,
        ),
      ),
    )
    .toEqual({
      url: assets.get(voiceKey(line.zh))!.clear,
      rate: 0.75,
      preservesPitch: true,
    });
});
