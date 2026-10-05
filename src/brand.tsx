import glyph from "hanzi-writer-data/清.json";
import { toneBarPath, wordmarkPaths } from "./brand-paths";

/**
 * One place for the product's name. Change these and the logo, wordmark,
 * page title and copy follow. (Storage keys stay "tingjian-*" on purpose:
 * renaming them would orphan existing learners' data.)
 */
/** Index of the stroke lit as the tone mark. */
export const TONE_STROKE = 3;

export const brand = {
  name: "Kiyo",
  plain: "Kiyo",
  zh: "清",
  meaning: "clear · pure (Japanese kiyo, Chinese qīng)",
  tagline: "Mandarin, crystal clear.",
};

/**
 * The main tile uses approved Sayo art. The compact 清 mark remains available
 * for tiny favicons, where the portrait's face cannot be read.
 */
export function BrandMark({
  size = 40,
  tile = true,
}: {
  size?: number;
  tile?: boolean;
}) {
  if (tile)
    return (
      <span
        className="brand-portrait"
        style={{ width: size, height: size }}
        role="img"
        aria-label={`${brand.name} logo`}
      >
        <img src="/mascot/web/welcome.webp" alt="" aria-hidden />
      </span>
    );
  return (
    <svg
      className="brand-mark-svg"
      width={size}
      height={size}
      viewBox="0 0 1024 1024"
      role="img"
      aria-label={`${brand.name} logo`}
    >
      <g transform="translate(112 112) scale(0.78)">
        <g transform="scale(1,-1) translate(0,-900)">
          {glyph.strokes.map((d: string, i: number) => (
            <path
              key={i}
              d={d}
              className={i === TONE_STROKE ? "bm-tone" : "bm-ink"}
            />
          ))}
        </g>
      </g>
    </svg>
  );
}

/** Wordmark: KIYO, with a blue bar over the I echoing the tone mark in qīng. */
export function Wordmark({ className = "" }: { className?: string }) {
  return (
    <svg
      className={`wordmark wordmark-vector ${className}`}
      viewBox="0 0 259 94"
      role="img"
      aria-label={brand.name}
    >
      <path d={toneBarPath} fill="var(--accent)" />
      {wordmarkPaths.map((d, i) => (
        <path key={i} d={d} fill="currentColor" fillRule="evenodd" />
      ))}
    </svg>
  );
}
