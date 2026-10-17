import { afterEach, beforeAll, expect, it, vi } from "vitest";
import { browserSpeech } from "../src/audio";
import { loadAudioCatalog } from "../src/audio-catalog";

// The catalogue loads lazily in the app; load it up front so playback is synchronous.
beforeAll(() => loadAudioCatalog());
import { welcomeGreeting } from "../src/sayo-lines";

class TestAudio {
  static clips: TestAudio[] = [];
  playbackRate = 1;
  preservesPitch = true;
  onended?: () => void;
  onplaying?: () => void;
  onerror?: () => void;
  pause = vi.fn();
  play = vi.fn(async () => {
    this.onplaying?.();
  });
  constructor(public src: string) {
    TestAudio.clips.push(this);
  }
}
afterEach(() => {
  browserSpeech.stop();
  vi.unstubAllGlobals();
  TestAudio.clips = [];
});

it("welcome uses Sayo's bundled playful recording", async () => {
  vi.stubGlobal("Audio", TestAudio);
  const fallback = vi.fn();
  const pending = browserSpeech.speak(welcomeGreeting.zh, {
    mood: "playful",
    onFallback: fallback,
  });
  expect(TestAudio.clips[0].src).toMatch(/^\/audio-v2\//);
  TestAudio.clips[0].onended?.();
  await pending;
  expect(fallback).not.toHaveBeenCalled();
});

it("rapid taps cancel earlier audio without awarding completed listening", async () => {
  vi.stubGlobal("Audio", TestAudio);
  const complete = vi.fn();
  const old = browserSpeech.speak("你好", { onComplete: complete });
  const next = browserSpeech.speak("太棒了！");
  await old;
  expect(TestAudio.clips[0].pause).toHaveBeenCalled();
  expect(complete).not.toHaveBeenCalled();
  expect(TestAudio.clips[1].src).toMatch(/^\/audio-v2\//);
  TestAudio.clips[1].onended?.();
  await next;
});

it("saved legacy choices resolve to Sayo clear; explicit moods select one identity", async () => {
  vi.stubGlobal("Audio", TestAudio);
  for (const voiceURI of ["", "local:zf_001", "local:zm_010"]) {
    const done = browserSpeech.speak("你好", { voiceURI });
    expect(TestAudio.clips.at(-1)?.src).toContain("-clear-");
    TestAudio.clips.at(-1)?.onended?.();
    await done;
  }
  const done = browserSpeech.speak("你好", {
    voiceURI: "local:playful",
    mood: "clear",
  });
  expect(TestAudio.clips.at(-1)?.src).toContain("-clear-");
  TestAudio.clips.at(-1)?.onended?.();
  await done;
});

it("a failed bundled clip falls back once and credits only completed device speech", async () => {
  vi.stubGlobal("Audio", TestAudio);
  class Utterance {
    onend?: () => void;
    onstart?: () => void;
    constructor(public text: string) {}
  }
  let spoken: Utterance | undefined;
  vi.stubGlobal("SpeechSynthesisUtterance", Utterance);
  const speak = vi.fn((u: Utterance) => {
    spoken = u;
  });
  vi.stubGlobal("speechSynthesis", {
    getVoices: () => [
      { lang: "zh-CN", voiceURI: "device", localService: true },
    ],
    cancel: vi.fn(),
    speak,
  });
  const onComplete = vi.fn(),
    onFallback = vi.fn();
  const done = browserSpeech.speak("你好", { onComplete, onFallback });
  TestAudio.clips[0].onerror?.();
  TestAudio.clips[0].onerror?.();
  TestAudio.clips[0].onended?.();
  expect(speak).toHaveBeenCalledTimes(1);
  expect(onFallback).toHaveBeenCalledTimes(1);
  expect(onComplete).not.toHaveBeenCalled();
  spoken?.onend?.();
  await done;
  expect(onComplete).toHaveBeenCalledTimes(1);
});

it("answer-only playback never switches to a device voice on a failed recording", async () => {
  vi.stubGlobal("Audio", TestAudio);
  const device = vi.fn();
  vi.stubGlobal("speechSynthesis", {
    getVoices: () => [
      { lang: "zh-CN", voiceURI: "device", localService: true },
    ],
    cancel: vi.fn(),
    speak: device,
  });
  const pending = browserSpeech.speak("你好", { allowDeviceFallback: false });
  const rejected = expect(pending).rejects.toThrow("This audio could not load");
  TestAudio.clips[0].onerror?.();
  await rejected;
  expect(TestAudio.clips[0].pause).toHaveBeenCalled();
  expect(device).not.toHaveBeenCalled();
});

it("unmounting an old control cannot stop newer playback", async () => {
  vi.stubGlobal("Audio", TestAudio);
  const owner = new AbortController();
  const old = browserSpeech.speak("你好", { signal: owner.signal });
  const complete = vi.fn();
  const next = browserSpeech.speak("太棒了！", { onComplete: complete });
  owner.abort();
  expect(TestAudio.clips[1].pause).not.toHaveBeenCalled();
  TestAudio.clips[1].onended?.();
  await Promise.all([old, next]);
  expect(complete).toHaveBeenCalledTimes(1);
});

it("aborting its own playback stops sound; failed clips reject", async () => {
  vi.stubGlobal("Audio", TestAudio);
  const owner = new AbortController();
  const first = browserSpeech.speak("你好", { signal: owner.signal });
  owner.abort();
  await first;
  expect(TestAudio.clips[0].pause).toHaveBeenCalled();
  const failed = browserSpeech.speak("你好");
  TestAudio.clips[1].onerror?.();
  await expect(failed).rejects.toThrow("could not load");
});
