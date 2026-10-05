"""Measured loudness correction, including clips shorter than a standard LUFS window."""
import subprocess
from pathlib import Path
import imageio_ffmpeg
import numpy as np
import pyloudnorm as pyln
import soundfile as sf

def levels(path):
    audio, sr = sf.read(path)
    if sr != 24000 or audio.ndim != 1 or len(audio) < sr*.23 or not np.isfinite(audio).all():
        raise ValueError(f'Invalid audio: {path}')
    block = .4 if len(audio) >= sr*.4 else len(audio)/sr/2
    loudness = pyln.Meter(sr,block_size=block).integrated_loudness(audio)
    if not np.isfinite(loudness) or max(abs(audio)) >= 1 or max(abs(audio)) < .005:
        raise ValueError(f'Invalid level: {path}')
    return audio, sr, float(loudness), block

def normalize_clip(path: Path, cache: Path):
    audio, sr, loudness, block = levels(path)
    before = loudness
    corrections = 0
    gain = -16-loudness
    for attempt in range(8):
        if abs(loudness+16) <= 1:
            break
        # Always correct from the original decode, avoiding repeated lossy transcodes.
        wav = cache/(path.stem+'-level.wav')
        tmp = cache/(path.stem+'-level.mp3')
        sf.write(wav,audio*10**(gain/20),sr,subtype='FLOAT')
        proc = subprocess.run([imageio_ffmpeg.get_ffmpeg_exe(),'-hide_banner','-loglevel','error','-y','-i',str(wav),
            '-af','alimiter=limit=0.84:level=false:latency=true','-ar','24000','-ac','1','-codec:a','libmp3lame','-b:a','64k',str(tmp)],capture_output=True)
        wav.unlink(missing_ok=True)
        if proc.returncode:
            raise RuntimeError(proc.stderr.decode(errors='replace'))
        _, _, loudness, _ = levels(tmp)
        gain += -16-loudness
        corrections = attempt+1
    if abs(loudness+16) > 1:
        raise ValueError(f'Cannot meet loudness target for {path}: {loudness}')
    if corrections:
        tmp.replace(path)
    final, _, loudness, _ = levels(path)
    return dict(lufs=round(loudness,2),originalLufs=round(before,2),loudnessWindowSeconds=block,peak=round(float(max(abs(final))),5),loudnessPass=1,corrected=bool(corrections))
