import { beforeEach, expect, it, vi } from "vitest";

const state = vi.hoisted(() => ({
  ready: true,
  clips: new Set<string>(),
  pending: Promise.resolve({}) as Promise<object>,
  resolve: () => {},
  reject: (_reason: Error) => {},
  speak: vi.fn(() => Promise.resolve()),
  tap: vi.fn(),
}));
vi.mock("../src/audio", () => ({
  hasSayoClip: (text: string) => state.clips.has(text),
  browserSpeech: { speak: state.speak },
}));
vi.mock("../src/audio-catalog", () => ({
  audioCatalog: () => (state.ready ? {} : null),
  loadAudioCatalog: () => state.pending,
}));
vi.mock("../src/hanzi", () => ({
  characterSpeech: (text: string) => (text === "行" ? "银行" : text),
}));
vi.mock("../src/sfx", () => ({ sfx: { tap: state.tap } }));
import { answerFeedback } from "../src/answer-voice";

const profile = { quiet: false, readChoices: true, voiceURI: "local:clear" };
beforeEach(() => {
  vi.clearAllMocks();
  state.ready = true;
  state.clips = new Set(["你好", "二十五", "银行"]);
  state.pending = new Promise((resolve, reject) => {
    state.resolve = () => {
      state.ready = true;
      resolve({});
    };
    state.reject = reject;
  });
});

it("the first answer waits for the catalogue and plays its recording", async () => {
  state.ready = false;
  answerFeedback("二十五", profile);
  expect(state.speak).not.toHaveBeenCalled();
  expect(state.tap).not.toHaveBeenCalled();
  state.resolve();
  await state.pending;
  expect(state.speak).toHaveBeenCalledExactlyOnceWith("二十五", {
    voiceURI: "local:clear",
    allowDeviceFallback: false,
  });
});

it("rapid choices while loading play only the latest answer", async () => {
  state.ready = false;
  answerFeedback("你好", profile);
  answerFeedback("二十五", profile);
  state.resolve();
  await state.pending;
  expect(state.speak).toHaveBeenCalledExactlyOnceWith("二十五", {
    voiceURI: "local:clear",
    allowDeviceFallback: false,
  });
});

it("quiet or unvoiced later taps cancel a waiting answer", async () => {
  state.ready = false;
  answerFeedback("你好", profile);
  answerFeedback(undefined, { ...profile, quiet: true });
  state.resolve();
  await state.pending;
  expect(state.speak).not.toHaveBeenCalled();
  expect(state.tap).toHaveBeenCalledOnce();
});

it("English explanations mentioning Chinese keep the interface sound", () => {
  state.clips.add("companion (朋友 = friend)");
  answerFeedback("companion (朋友 = friend)", profile);
  expect(state.speak).not.toHaveBeenCalled();
  expect(state.tap).toHaveBeenCalledOnce();
});

it("a single character uses its taught pronunciation", () => {
  answerFeedback("行", profile);
  expect(state.speak).toHaveBeenCalledExactlyOnceWith("银行", {
    voiceURI: "local:clear",
    allowDeviceFallback: false,
  });
});

it("a missing contextual reading cannot fall back to a different bare-character reading", () => {
  state.clips.delete("银行");
  state.clips.add("行");
  answerFeedback("行", profile);
  expect(state.speak).not.toHaveBeenCalled();
  expect(state.tap).toHaveBeenCalledOnce();
});

it("a saved device-voice preference cannot change the answer narrator", () => {
  answerFeedback("你好", { ...profile, voiceURI: "device:mandarin" });
  expect(state.speak).toHaveBeenCalledExactlyOnceWith("你好", {
    voiceURI: "local:clear",
    allowDeviceFallback: false,
  });
});

it("missing clips and disabled answer speech do not invoke a device voice", () => {
  answerFeedback("没有录音", profile);
  answerFeedback("你好", { ...profile, readChoices: false });
  expect(state.speak).not.toHaveBeenCalled();
  expect(state.tap).toHaveBeenCalledTimes(2);
});

it("a failed lazy catalogue keeps the interface usable", async () => {
  state.ready = false;
  answerFeedback("你好", profile);
  state.reject(new Error("offline"));
  await state.pending.catch(() => {});
  await Promise.resolve();
  expect(state.speak).not.toHaveBeenCalled();
  expect(state.tap).toHaveBeenCalledOnce();
});
