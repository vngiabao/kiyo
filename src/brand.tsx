import glyph from "hanzi-writer-data/清.json";

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
 * The mark: 清 drawn from stroke data. The flat top bar of 青 (stroke 4)
 * is lit in pale blue: it doubles as the first-tone mark in qīng.
 */
export function BrandMark({ size = 40, tile = true }: { size?: number; tile?: boolean }) {
  return (
    <svg
      className="brand-mark-svg"
      width={size}
      height={size}
      viewBox="0 0 1024 1024"
      role="img"
      aria-label={`${brand.name} logo`}
    >
      {tile && <rect width="1024" height="1024" rx="232" className="bm-tile" />}
      <g transform="translate(112 112) scale(0.78)">
        <g transform="scale(1,-1) translate(0,-900)">
          {glyph.strokes.map((d: string, i: number) => (
            <path key={i} d={d} className={i === TONE_STROKE ? "bm-tone" : "bm-ink"} />
          ))}
        </g>
      </g>
    </svg>
  );
}

/** Wordmark: KIYO, with a blue bar over the I echoing the tone mark in qīng. */
export function Wordmark({ className = "" }: { className?: string }) {
  return (
    <span className={`wordmark ${className}`}>
      <span className="sr-only">{brand.name}</span>
      <span aria-hidden>
        K<span className="wm-e">I<span className="wm-macron" /></span>YO
      </span>
    </span>
  );
}
