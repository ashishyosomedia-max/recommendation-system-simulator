"""Transcribe an audio file with faster-whisper to cross-check subtitles.

Usage: python3 -I transcribe.py <audio> <model_dir> [lang]
Audio is decoded with ffmpeg (16 kHz mono). Model: a CTranslate2 Whisper
model directory (e.g. Whisper small).
"""
import subprocess, sys
import numpy as np
from faster_whisper import WhisperModel

audio, model_dir = sys.argv[1], sys.argv[2]
lang = sys.argv[3] if len(sys.argv) > 3 else "en"
raw = subprocess.run(["ffmpeg", "-loglevel", "error", "-i", audio, "-ac", "1",
                      "-ar", "16000", "-f", "f32le", "-"], capture_output=True, check=True).stdout
m = WhisperModel(model_dir, device="cpu", compute_type="int8")
segs, _ = m.transcribe(np.frombuffer(raw, dtype=np.float32), language=lang, beam_size=5)
for s in segs:
    print(f"[{s.start:.2f}-{s.end:.2f}] {s.text}")
