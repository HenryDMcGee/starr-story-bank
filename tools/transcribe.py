"""Transcribe a STARR practice recording (video or audio) to plain text.

Uses a Whisper model run locally through sherpa-onnx, so nothing is sent to a
third-party service.

Setup (once per machine):
    pip install sherpa-onnx numpy
    # ffmpeg must be on PATH
    curl -L -o base.en.tar.bz2 \
      https://github.com/k2-fsa/sherpa-onnx/releases/download/asr-models/sherpa-onnx-whisper-base.en.tar.bz2
    tar xjf base.en.tar.bz2

Usage:
    python tools/transcribe.py recording.webm --model-dir sherpa-onnx-whisper-base.en

Prints the transcript to stdout and the duration to stderr.
"""

import argparse
import os
import subprocess
import sys

import numpy as np
import sherpa_onnx

SAMPLE_RATE = 16000
CHUNK_SECONDS = 25  # Whisper handles up to 30 s per pass


def load_audio(path):
    pcm = subprocess.run(
        ["ffmpeg", "-v", "error", "-i", path, "-ac", "1", "-ar", str(SAMPLE_RATE), "-f", "s16le", "-"],
        capture_output=True,
        check=True,
    ).stdout
    return np.frombuffer(pcm, np.int16).astype(np.float32) / 32768


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("recording")
    ap.add_argument("--model-dir", default="sherpa-onnx-whisper-base.en")
    args = ap.parse_args()

    name = os.path.basename(os.path.normpath(args.model_dir)).replace("sherpa-onnx-whisper-", "")
    prefix = os.path.join(args.model_dir, name + "-")
    rec = sherpa_onnx.OfflineRecognizer.from_whisper(
        encoder=prefix + "encoder.int8.onnx",
        decoder=prefix + "decoder.int8.onnx",
        tokens=prefix + "tokens.txt",
        num_threads=4,
    )

    audio = load_audio(args.recording)
    step = SAMPLE_RATE * CHUNK_SECONDS
    parts = []
    for start in range(0, len(audio), step):
        stream = rec.create_stream()
        stream.accept_waveform(SAMPLE_RATE, audio[start:start + step])
        rec.decode_stream(stream)
        text = stream.result.text.strip()
        if text:
            parts.append(text)

    print(" ".join(parts))
    print(f"duration {len(audio) / SAMPLE_RATE:.1f}s", file=sys.stderr)


if __name__ == "__main__":
    main()
