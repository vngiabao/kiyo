import glyph from "hanzi-writer-data/清.json";
import assets from "./brand-assets.json";

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

/** The owner's selected website signature; preserves the original approved art. */
export function BrandSignature({ className = "" }: { className?: string }) {
  return (
    <img
      className={`brand-signature ${className}`}
      src={assets.signature.src}
      width={assets.signature.width}
      height={assets.signature.height}
      alt="Kiyo — Sayo leaning over the wordmark"
      decoding="async"
    />
  );
}

/**
 * The tile uses approved Sayo art. The legacy 清 glyph remains available
 * to callers that explicitly request it; installed icons use the waving portrait.
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
        <img src={assets.icon512.src} alt="" aria-hidden />
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
