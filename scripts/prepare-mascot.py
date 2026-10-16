"""Turn full-size mascot PNGs into the small WebP files the app loads.

Usage: python scripts/prepare-mascot.py [source_dir] [--all]   (default: public/mascot/quiet)
Requires Pillow. Every pose uses ONE fixed square frame, so swapping poses never
changes her size or position. The frame is pinned to the one the approved poses
were made with (measured from public/mascot/web, 16 Oct 2026); re-deriving it from
the PNGs would silently re-crop the approved set.

By default only poses without a WebP are converted, so approved files are never
re-encoded. Pass --all to rebuild every pose (only after a deliberate art change).
New poses must already be drawn to the standard scale: feet on y≈1154, centred
on x≈655, head the size of welcome.png's (see prompts/sayo-new-poses.md).
Output: public/mascot/web/<id>.webp at 480 x 480.
"""
import glob
import os
import sys

from PIL import Image

FRAME = (116, 154, 1137, 1175)
args = [a for a in sys.argv[1:] if not a.startswith("--")]
rebuild = "--all" in sys.argv
src = args[0] if args else "public/mascot/quiet"
out_dir = "public/mascot/web"
files = sorted(glob.glob(os.path.join(src, "*.png")))
if not files:
    sys.exit(f"No PNG files in {src}")

os.makedirs(out_dir, exist_ok=True)
written = []
for f in files:
    target = os.path.join(out_dir, os.path.basename(f)[:-4] + ".webp")
    if os.path.exists(target) and not rebuild:
        continue
    im = Image.open(f).convert("RGBA")
    box = im.split()[-1].point(lambda v: 255 if v > 40 else 0).getbbox()
    if box and not (box[0] >= FRAME[0] and box[1] >= FRAME[1] and box[2] <= FRAME[2] and box[3] <= FRAME[3]):
        sys.exit(f"{f} extends outside the shared frame {FRAME} (visible {box}); scale it to the standard size first")
    im.crop(FRAME).resize((480, 480), Image.LANCZOS).save(target, "WEBP", quality=86, method=6)
    written.append(os.path.basename(target))
print(f"Wrote {len(written)} pose(s) to {out_dir}: {', '.join(written) or 'none (all up to date)'}; frame {FRAME}")
