import React, { useEffect, useRef, useState } from "react";
import {
  Play,
  Stop,
  Microphone,
  ArrowRight,
  SpeakerHigh,
  Trash,
} from "@phosphor-icons/react";
import { browserSpeech } from "./audio";
import type { Phrase } from "./types";
import { Mascot } from "./Mascot";
import { useSpeech } from "./useSpeech";
import type { SayoMood } from "./sayo-voice";
export function Arrow() {
  return <ArrowRight size={19} aria-hidden />;
}
export function AudioButton({
  text,
  voiceURI,
  mood,
  large = false,
  rate = 1,
  label,
  onPlayed,
  companion = true,
}: {
  text: string;
  voiceURI?: string;
  mood?: SayoMood;
  large?: boolean;
  rate?: number;
  label?: string;
  onPlayed?: () => void;
  companion?: boolean;
}) {
  const { playing, error, speak, stop } = useSpeech();
  const play = () => {
    if (playing) {
      stop();
      return;
    }
    speak(text, {
        voiceURI,
        mood,
        rate,
        onComplete: onPlayed,
      });
  };
  return (
    <div className={`audio-control ${large ? "large" : ""}`}>
      {large && companion && <Mascot state={error ? "error" : "listen"} size={96} active={playing} still={!playing && !error} />}
      <button
        className={`${large ? "audio-disc" : "audio-chip"} ${playing ? "is-playing" : ""} ${label ? "has-label" : ""}`}
        onClick={play}
        aria-label={playing ? "Stop audio" : (label ?? "Play Mandarin audio")}
      >
        {playing ? (
          <span className="eq" aria-hidden>
            <i />
            <i />
            <i />
          </span>
        ) : large ? (
          <Play size={28} weight="fill" />
        ) : (
          <SpeakerHigh size={18} weight="bold" />
        )}
        {label && !large && <span>{label}</span>}
      </button>
      {large && (
        <span className="audio-caption">
          {playing ? "Listening…" : "Play · Space"}
        </span>
      )}
      {error && (
        <p className="inline-error" role="alert">
          {error}
        </p>
      )}
    </div>
  );
}
const toneMarks = [
  "āēīōūǖĀĒĪŌŪǕ",
  "áéíóúǘÁÉÍÓÚǗ",
  "ǎěǐǒǔǚǍĚǏǑǓǙ",
  "àèìòùǜÀÈÌÒÙǛ",
];
const V = "aeiouüvāáǎàēéěèīíǐìōóǒòūúǔùǖǘǚǜAEIOUÜĀÁǍÀĒÉĚÈĪÍǏÌŌÓǑÒŪÚǓÙǕǗǙǛ";
const syllable = new RegExp(
  `(zh|ch|sh|[bpmfdtnlgkhjqxrzcsyw])?[${V}]+(?:ng(?![${V}])|n(?![${V}]))?(?:r(?![${V}]))?`,
  "gi",
);
export function toneOf(s: string) {
  for (let t = 0; t < 4; t++)
    if ([...s].some((ch) => toneMarks[t].includes(ch))) return t + 1;
  return 5;
}
/** Pinyin split into syllables, each carrying its tone for optional colour. */
export function Pinyin({
  text,
  className = "",
}: {
  text: string;
  className?: string;
}) {
  const out: React.ReactNode[] = [];
  let last = 0;
  for (const m of text.matchAll(syllable)) {
    if (m.index! > last) out.push(text.slice(last, m.index));
    out.push(
      <span key={m.index} className={`t${toneOf(m[0])}`}>
        {m[0]}
      </span>,
    );
    last = m.index! + m[0].length;
  }
  out.push(text.slice(last));
  return (
    <span className={`pinyin ${className}`} lang="zh-Latn-pinyin">
      {out}
    </span>
  );
}
export function PhraseText({
  phrase,
  pinyin = true,
  meaning = true,
  onHear,
}: {
  phrase: Phrase;
  pinyin?: boolean;
  meaning?: boolean;
  onHear?: () => void;
}) {
  return (
    <div className="phrase">
      <Speakable className="hanzi" text={phrase.audio.text || phrase.hanzi} onHear={onHear}>
        {phrase.hanzi}
      </Speakable>
      {pinyin && <Pinyin text={phrase.pinyin} />}
      {meaning && <div className="translation">{phrase.meaning}</div>}
    </div>
  );
}
export function Speakable({ text, children, className = "", onHear }: {
  text: string; children: React.ReactNode; className?: string; onHear?: () => void;
}) {
  const { speak, playing, error } = useSpeech();
  return <>
    <button type="button" className={`speakable ${className}`} lang="zh-CN"
      aria-label={`Hear ${text}`} data-speaking={playing}
      onClick={() => { onHear?.(); speak(text); }}>{children}</button>
    {error && <p className="inline-error" role="alert">{error}</p>}
  </>;
}
export function ToneCurve({ tone = 3 }: { tone?: number }) {
  const paths: Record<number, string> = {
    1: "M 20 35 L 210 35",
    2: "M 20 115 Q 115 90 210 25",
    3: "M 20 90 Q 90 155 130 140 Q 175 120 210 60",
    4: "M 20 25 L 210 145",
    5: "M 80 85 L 140 85",
  };
  return (
    <svg
      className="tone-curve"
      viewBox="0 0 240 180"
      role="img"
      aria-label={`Schematic tone ${tone} pitch contour`}
    >
      <path className="tone-guide" d="M20 35H220 M20 90H220 M20 145H220" />
      <path className="tone-line" d={paths[tone]} />
      <circle
        cx="20"
        cy={tone === 1 ? 35 : tone === 2 ? 115 : tone === 3 ? 90 : 25}
        r="5"
      />
    </svg>
  );
}
export function Recorder({ onAttempt }: { onAttempt?: () => void }) {
  const [recording, setRecording] = useState(false),
    [url, setUrl] = useState(""),
    [error, setError] = useState("");
  const rec = useRef<MediaRecorder | null>(null),
    stream = useRef<MediaStream | null>(null),
    mounted = useRef(true),
    timer = useRef<ReturnType<typeof setTimeout> | null>(null);
  const stop = () => {
    if (rec.current?.state === "recording") rec.current.stop();
    stream.current?.getTracks().forEach((t) => t.stop());
    if (timer.current) clearTimeout(timer.current);
    setRecording(false);
  };
  useEffect(() => {
    mounted.current = true;
    return () => {
      mounted.current = false;
      rec.current?.state === "recording" && rec.current.stop();
      stream.current?.getTracks().forEach((t) => t.stop());
      if (timer.current) clearTimeout(timer.current);
    };
  }, []);
  useEffect(
    () => () => {
      if (url) URL.revokeObjectURL(url);
    },
    [url],
  );
  async function start() {
    browserSpeech.stop();
    setError("");
    try {
      if (!navigator.mediaDevices?.getUserMedia || !window.MediaRecorder)
        throw new Error(
          "Recording is not supported here. Say the phrase aloud or use the text alternative.",
        );
      const s = await navigator.mediaDevices.getUserMedia({ audio: true });
      if (!mounted.current) {
        s.getTracks().forEach((t) => t.stop());
        return;
      }
      stream.current = s;
      const r = new MediaRecorder(s);
      rec.current = r;
      const chunks: BlobPart[] = [];
      r.ondataavailable = (e) => {
        if (e.data.size) chunks.push(e.data);
      };
      r.onstop = () => {
        s.getTracks().forEach((t) => t.stop());
        if (mounted.current) {
          setUrl(URL.createObjectURL(new Blob(chunks, { type: r.mimeType })));
          setRecording(false);
          onAttempt?.();
        }
      };
      r.start();
      setRecording(true);
      timer.current = setTimeout(stop, 60000);
    } catch (e) {
      stream.current?.getTracks().forEach((t) => t.stop());
      setError(
        e instanceof DOMException
          ? "Microphone access wasn’t available. Allow it in your browser, or practice aloud without recording."
          : (e as Error).message,
      );
    }
  }
  return (
    <div className="recorder">
      <Mascot state={error ? "error" : "speak"} size={90} active={recording} still={!recording && !error} />
      <p className="small">
        Record to listen back. Audio stays in this tab and is discarded when you
        leave. No automatic pronunciation score.
      </p>
      <button
        className={recording ? "button recording" : "button secondary"}
        onClick={recording ? stop : start}
      >
        {recording ? <Stop weight="fill" /> : <Microphone size={20} />}{" "}
        {recording ? "Stop recording" : "Record yourself"}
      </button>
      {recording && (
        <p role="status">Recording · stops automatically after one minute</p>
      )}
      {url && (
        <div className="recording-result">
          <audio controls src={url} />
          <button
            className="icon-button"
            aria-label="Delete recording"
            onClick={() => setUrl("")}
          >
            <Trash size={20} />
          </button>
        </div>
      )}
      {error && (
        <p role="alert" className="inline-error">
          {error}
        </p>
      )}
    </div>
  );
}
