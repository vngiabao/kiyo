"""Create genuine path-only vector drafts from the preserved generated concepts.

Uses the already-installed vtracer; no model, app, or audio files are modified.
"""
from pathlib import Path
import json
import tempfile
import xml.etree.ElementTree as ET

from PIL import Image
import vtracer

root = Path(__file__).resolve().parent
report = []
for name in ("peek", "stamp", "watch"):
    source = root / f"{name}.png"
    target = root / f"{name}.svg"
    with Image.open(source) as im:
        rgba = im.convert("RGBA")
        width, height = im.size
        alpha = rgba.getchannel("A")
        assert alpha.getextrema() == (0, 255), f"{name}: missing transparency"
        # The generator leaves isolated alpha 1–8 dust outside the visible figure.
        # Preserve the PNG and report its raw bounds separately; test the visible
        # figure (above 3% opacity) for cropping, rather than invisible dust.
        raw_bounds = alpha.getbbox()
        bounds = alpha.point(lambda value: 255 if value > 8 else 0).getbbox()
        assert bounds and bounds[0] > 0 and bounds[1] > 0
        assert bounds[2] < width and bounds[3] < height, f"{name}: clipped figure"
        # Tracing treats even alpha=1 dust as opaque shapes. Drop only that
        # invisible dust in the conversion input; the original PNG stays intact.
        rgba.putalpha(alpha.point(lambda value: value if value > 8 else 0))
        with tempfile.TemporaryDirectory(prefix="sayo-svg-") as temporary:
            trace_input = Path(temporary) / "source.png"
            rgba.save(trace_input)
            vtracer.convert_image_to_svg_py(str(trace_input), str(target))
    text = target.read_text(encoding="utf-8")
    # Keep the original coordinate system while presenting a consistent canvas.
    text = text.replace(f'width="{width}" height="{height}"',
                        f'width="1254" height="1254" viewBox="0 0 {width} {height}"', 1)
    target.write_text(text, encoding="utf-8")
    svg = ET.fromstring(text)
    tags = [e.tag.rsplit("}", 1)[-1] for e in svg.iter()]
    assert "path" in tags and not {"image", "script", "foreignObject", "text"}.intersection(tags)
    assert "data:image" not in text and "href=" not in text
    report.append(dict(pose=name, sourceSize=[width, height], sourceAlphaBounds=raw_bounds,
                       visibleAlphaBounds=bounds, framingAlphaThreshold=8,
                       svgCanvas=[1254, 1254], paths=tags.count("path"), bytes=target.stat().st_size,
                       embeddedRaster=False, status="design draft; not installed"))
(root / "validation.json").write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
print(json.dumps(report, indent=2))
