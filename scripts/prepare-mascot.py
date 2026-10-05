"""Turn full-size mascot PNGs into the small WebP files the app loads.

Usage: python scripts/prepare-mascot.py [source_dir]   (default: public/mascot/quiet)
Requires Pillow. All poses are cropped to ONE shared square frame (the union
of their visible pixels), so swapping poses never changes her size or position.
Output: public/mascot/web/<id>.webp at 480 x 480.
"""
import glob
import os
import sys

from PIL import Image

src = sys.argv[1] if len(sys.argv) > 1 else "public/mascot/quiet"
out_dir = "public/mascot/web"
files = sorted(glob.glob(os.path.join(src, "*.png")))
if not files:
    sys.exit(f"No PNG files in {src}")

box = None
for f in files:
    alpha = Image.open(f).convert("RGBA").split()[-1].point(lambda v: 255 if v > 40 else 0)
    b = alpha.getbbox()
    if b:
        box = b if box is None else (min(box[0], b[0]), min(box[1], b[1]), max(box[2], b[2]), max(box[3], b[3]))

side = max(box[2] - box[0], box[3] - box[1]) + 24
cx, cy = (box[0] + box[2]) // 2, (box[1] + box[3]) // 2
crop = (cx - side // 2, cy - side // 2, cx - side // 2 + side, cy - side // 2 + side)
os.makedirs(out_dir, exist_ok=True)
total = 0
for f in files:
    im = Image.open(f).convert("RGBA").crop(crop).resize((480, 480), Image.LANCZOS)
    target = os.path.join(out_dir, os.path.basename(f)[:-4] + ".webp")
    im.save(target, "WEBP", quality=86, method=6)
    total += os.path.getsize(target)
print(f"Wrote {len(files)} poses to {out_dir} ({total // 1024} KB), shared frame {crop}")
