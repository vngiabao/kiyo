import { useEffect, useState } from "react";
import { BookmarkSimple, Check, X } from "@phosphor-icons/react";
import { useLiveQuery } from "dexie-react-hooks";
import { db } from "./db";
import { segment, tokenAt, type Token } from "./dictionary";
import { phrases } from "./content";
import { AudioButton, Pinyin } from "./components";
import assets from "./audio-assets.json";
import { voiceKey } from "./sayo-voice";
import { wordSpeech } from "./word-speech";

const taught = new Set(phrases.map((p) => p.hanzi.replace(/[，。！？、,.!?]/g, "")));
const clips = assets as Record<string, Record<string, string>>;

/** Words of a line, from the offline dictionary. Null while the dictionary loads. */
export function useWords(line: string | undefined) {
  const [state, setState] = useState<{ line: string; tokens: Token[] | null; error: string }>({ line: "", tokens: null, error: "" });
  useEffect(() => {
    if (!line) return;
    let alive = true;
    setState({ line, tokens: null, error: "" });
    segment(line)
      .then((tokens) => alive && setState({ line, tokens, error: "" }))
      .catch((e: Error) => alive && setState({ line, tokens: null, error: e.message }));
    return () => {
      alive = false;
    };
  }, [line]);
  return state.line === line ? state : { line: line ?? "", tokens: null, error: "" };
}

/** The tapped word: pinyin, meanings, measure words, HSK level, course status, save. */
export function WordCard({
  token,
  line,
  source,
  voiceURI,
  onClose,
}: {
  token: Token;
  line: string;
  source: string;
  voiceURI: string;
  onClose: () => void;
}) {
  const saved = useLiveQuery(() => db.personalWords.get(token.text), [token.text]);
  const main = token.entries[0];
  const spoken = wordSpeech(token.text, main?.p ?? "");
  const hasClip = !!clips[voiceKey(spoken)];
  const simplified = main?.s;
  return (
    <aside className="word-card" role="status" aria-label={`Dictionary: ${token.text}`}>
      <div className="wc-head">
        <span className="wc-word" lang="zh-CN">
          {token.text}
          {simplified && <span className="wc-simp">{simplified}</span>}
        </span>
        {main && <Pinyin text={main.p} />}
        {hasClip && <AudioButton text={spoken} voiceURI={voiceURI} label={spoken === token.text ? "Hear" : `Hear ${spoken}`} />}
        <button className="icon-button wc-close" aria-label="Close" onClick={onClose}>
          <X size={16} />
        </button>
      </div>
      {token.entries.length ? (
        <ul className="wc-senses">
          {token.entries.slice(0, 3).map((e, i) => (
            <li key={i}>
              {token.entries.length > 1 && <Pinyin text={e.p} />} {e.m}
              {e.c && <span className="wc-cl"> · measure word {e.c}</span>}
            </li>
          ))}
        </ul>
      ) : (
        <p className="muted">Not in the dictionary (often a name or a rare form).</p>
      )}
      <div className="wc-meta">
        {main?.h && <span className="wc-tag">{main.h === 7 ? "HSK 7–9" : `HSK ${main.h}`}</span>}
        {taught.has(token.text) && <span className="wc-tag good">In your course</span>}
        <button
          className="chip-toggle"
          aria-pressed={!!saved}
          disabled={!main}
          onClick={() =>
            void (saved
              ? db.personalWords.delete(token.text)
              : db.personalWords.put({ id: token.text, pinyin: main!.p, meaning: main!.m, line, source, at: Date.now() }))
          }
        >
          {saved ? <Check size={16} /> : <BookmarkSimple size={16} />} {saved ? "Saved" : "Save word"}
        </button>
      </div>
    </aside>
  );
}

/** A line whose characters can be tapped; the whole word around the tap lights up. */
export function TappableLine({
  line,
  tokens,
  active,
  onTap,
  className = "",
}: {
  line: string;
  tokens: Token[] | null;
  active: Token | null;
  onTap: (t: Token) => void;
  className?: string;
}) {
  const chars = Array.from(line);
  return (
    <p className={className} lang="zh-CN">
      {chars.map((ch, i) => {
        const t = tokens ? tokenAt(tokens, i) : undefined;
        const on = !!active && !!t && t.start === active.start && t.end === active.end;
        const word = t && t.entries.length > 0;
        return word || (t && /\p{Script=Han}/u.test(ch)) ? (
          <button key={i} className={`wch ${on ? "on" : ""} ${on && i === t!.start ? "first" : ""} ${on && i === t!.end - 1 ? "last" : ""}`} onClick={() => onTap(t!)}>
            {ch}
          </button>
        ) : (
          <span key={i}>{ch}</span>
        );
      })}
    </p>
  );
}
