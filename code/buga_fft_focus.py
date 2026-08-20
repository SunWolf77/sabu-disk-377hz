#!/usr/bin/env python3
"""
buga_fft_focus.py — SIMULATION / teaching only

Synthetic sum of sines at Fibonacci markers (233, 377, 610 Hz).
NOT a microphone recording of any physical sphere.

Buga is an **extension study** in this repo — separate from the Sabu
null-test path (docs/NULL_TEST.md, docs/ACOUSTIC_TEST.md).
"""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "data" / "buga_sphere"
OUT.mkdir(parents=True, exist_ok=True)

# Fibonacci markers (framework labels — not measured peaks)
PIVOTS = [233, 377, 610]
FS = 44100
DURATION = 1.0
t = np.linspace(0.0, DURATION, int(FS * DURATION), endpoint=False)

combined = np.sum([np.sin(2 * np.pi * f * t) for f in PIVOTS], axis=0)
N = len(combined)
yf = np.fft.rfft(combined)
xf = np.fft.rfftfreq(N, 1.0 / FS)
amp = (2.0 / N) * np.abs(yf)

df = pd.DataFrame({"Frequency_Hz": xf, "Amplitude": amp})
csv_path = OUT / "sim_buga_fft_focus.csv"
png_path = OUT / "sim_buga_fft_focus.png"
df.to_csv(csv_path, index=False)

fig, ax = plt.subplots(figsize=(10, 4))
ax.plot(xf, amp, color="darkorange", lw=0.8, label="SIM combined sines")
for p in PIVOTS:
    ax.axvline(p, color="crimson", ls="--", alpha=0.7)
    ax.text(p + 8, amp.max() * 0.85, f"{p} Hz", rotation=90, color="crimson", fontsize=8)
ax.set_xlim(0, 1000)
ax.set_title("SIM — Buga extension: synthetic FFT at Fibonacci markers (not mic data)")
ax.set_xlabel("Frequency (Hz)")
ax.set_ylabel("Amplitude (arb.)")
ax.grid(True, alpha=0.3)
ax.legend(loc="upper right")
fig.tight_layout()
fig.savefig(png_path, dpi=120)
plt.close(fig)

print(f"SIM CSV → {csv_path.relative_to(ROOT)}")
print(f"SIM PNG → {png_path.relative_to(ROOT)}")
print("Markers only. Not a physical sphere measurement.")
