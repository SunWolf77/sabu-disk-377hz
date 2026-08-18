#!/usr/bin/env python3
"""Mode A: WAV/CSV -> in-band metric. Usage: python analyze_mic.py run.wav --f0 377 --half 2"""
from __future__ import annotations
import argparse
from pathlib import Path
import numpy as np

def load_mono(path: Path):
    path = Path(path)
    if path.suffix.lower() == ".wav":
        import wave
        with wave.open(str(path), "rb") as w:
            nch, sw, rate, n = w.getnchannels(), w.getsampwidth(), w.getframerate(), w.getnframes()
            raw = w.readframes(n)
        data = np.frombuffer(raw, dtype=np.int16 if sw == 2 else np.int32).astype(np.float64)
        if nch > 1:
            data = data.reshape(-1, nch).mean(axis=1)
        data /= np.max(np.abs(data)) + 1e-12
        return data, float(rate)
    arr = np.loadtxt(path, delimiter=",", ndmin=1)
    return (arr[:, 0] if arr.ndim > 1 else arr).astype(np.float64), 44100.0

def band_metric(x, rate, f0, half):
    n = len(x)
    win = np.hanning(n)
    amp = np.abs(np.fft.rfft(x * win)) * 2.0 / (np.sum(win) + 1e-12)
    freqs = np.fft.rfftfreq(n, 1.0 / rate)
    band = (freqs >= f0 - half) & (freqs <= f0 + half)
    in_band = float(amp[band].mean()) if band.any() else float("nan")
    lo = (freqs >= f0 - 30) & (freqs <= f0 - 15)
    hi = (freqs >= f0 + 15) & (freqs <= f0 + 30)
    side = list(amp[lo]) + list(amp[hi])
    baseline = float(np.mean(side)) if len(side) else float("nan")
    snr = in_band / baseline if baseline and baseline > 0 else float("nan")
    i = int(np.argmin(np.abs(freqs - f0)))
    return in_band, baseline, snr, float(amp[i]), float(freqs[i]), n, rate

def main():
    p = argparse.ArgumentParser()
    p.add_argument("files", nargs="+")
    p.add_argument("--f0", type=float, default=377.0)
    p.add_argument("--half", type=float, default=2.0)
    p.add_argument("--compare", action="store_true")
    args = p.parse_args()
    rows = []
    for f in args.files:
        x, rate = load_mono(Path(f))
        ib, base, snr, a0, fbin, n, rate = band_metric(x, rate, args.f0, args.half)
        rows.append((ib, snr))
        print(f"--- {f}")
        print(f"  nearest {fbin:.3f} Hz amp={a0:.6e}  in_band={ib:.6e}  snr={snr:.4f}")
    if args.compare and len(rows) >= 2:
        print(f"--- d_in_band={rows[0][0]-rows[1][0]:.6e}  d_snr={rows[0][1]-rows[1][1]:.4f}")

if __name__ == "__main__":
    main()
