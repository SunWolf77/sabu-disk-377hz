#!/usr/bin/env python3
"""
buga_check.py — inspect SIM Buga FFT CSV (Fibonacci markers)

Reads sim_buga_fft_focus.csv (or legacy buga_fft_focus.csv).
Does not claim physical measurement.
"""
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "buga_sphere"

candidates = [
    DATA / "sim_buga_fft_focus.csv",
    DATA / "buga_fft_focus.csv",  # legacy name
]
path = next((p for p in candidates if p.exists()), None)
if path is None:
    raise SystemExit(
        "No Buga FFT CSV found. Run: python code/buga_fft_focus.py"
    )

df = pd.read_csv(path)
# tolerate legacy column names
freq_col = "Frequency_Hz" if "Frequency_Hz" in df.columns else (
    "Frequency (Hz)" if "Frequency (Hz)" in df.columns else "Frequency"
)
amp_col = "Amplitude"
if freq_col not in df.columns or amp_col not in df.columns:
    raise SystemExit(f"Unexpected columns in {path.name}: {list(df.columns)}")

pivots = [233, 377, 610]
print(f"Loaded SIM file: {path.relative_to(ROOT)}")
print("Fibonacci marker amplitudes (nearest bins):")
for f in pivots:
    idx = (df[freq_col] - f).abs().idxmin()
    amp = float(df.loc[idx, amp_col])
    fbin = float(df.loc[idx, freq_col])
    print(f"  target {f} Hz → bin {fbin:.2f} Hz → amp {amp:.6e}")

fig, ax = plt.subplots(figsize=(10, 4))
ax.plot(df[freq_col], df[amp_col], color="darkorange", lw=0.8, label="SIM spectrum")
for f in pivots:
    ax.axvline(f, color="crimson", ls="--", alpha=0.7)
ax.set_xlim(0, 1000)
ax.set_title("SIM — Buga FFT check (markers only; not mic data)")
ax.set_xlabel("Frequency (Hz)")
ax.set_ylabel("Amplitude (arb.)")
ax.grid(True, alpha=0.3)
ax.legend()
fig.tight_layout()
plt.show()
