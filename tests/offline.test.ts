import { afterEach, expect, it, vi } from "vitest";
import { clipUrls, saveAllAudio } from "../src/offline";

afterEach(() => vi.unstubAllGlobals());

it("does not save a successful HTML login response as offline audio", async () => {
  vi.stubGlobal("location", { origin: "https://kiyo.example" });
  const urls = clipUrls();
  const put = vi.fn();
  vi.stubGlobal("caches", {
    open: async () => ({
      keys: async () => urls.slice(1).map((url) => ({ url })),
      put,
    }),
  });
  vi.stubGlobal(
    "fetch",
    vi.fn(
      async () =>
        new Response("Sign in", {
          status: 200,
          headers: { "content-type": "text/html" },
        }),
    ),
  );
  const result = await saveAllAudio(() => undefined);
  expect(result.failed).toBe(1);
  expect(put).not.toHaveBeenCalled();
});

it("saves a complete audio response in the resumable cache", async () => {
  vi.stubGlobal("location", { origin: "https://kiyo.example" });
  const urls = clipUrls();
  const put = vi.fn();
  vi.stubGlobal("caches", {
    open: async () => ({
      keys: async () => urls.slice(1).map((url) => ({ url })),
      put,
    }),
  });
  vi.stubGlobal(
    "fetch",
    vi.fn(
      async () =>
        new Response(new Uint8Array([73, 68, 51]), {
          status: 200,
          headers: { "content-type": "audio/mpeg" },
        }),
    ),
  );
  expect((await saveAllAudio(() => undefined)).failed).toBe(0);
  expect(put).toHaveBeenCalledOnce();
});
