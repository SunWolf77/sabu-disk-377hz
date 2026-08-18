"""
SIMULATED FFT teaching sweep — NOT a microphone recording of a Sabu replica.

This script concatenates pure sines and plots an FFT so collaborators can
see how a sweep display looks. It does not prove a 377 Hz physical resonance.

For a real test: record WAV/CSV from acoustic_logger (or equivalent), then
FFT the recording. Compare Sabu-form vs null twin under docs/NULL_TEST.md.
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft, fftfreq
import pandas as pd
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / "data" / "sabu_disk"
OUT.mkdir(parents=True, exist_ok=True)

fs = 44100  # Hz
duration = 0.1  # seconds per dwell tone
t = np.linspace(0, duration, int(fs * duration), endpoint=False)

# Synthetic dwell tones (teaching only)
frequencies = np.arange(50, 1001, 1)
signals = [np.sin(2 * np.pi * f * t) for f in frequencies]
sweep_signal = np.concatenate(signals)

N = len(sweep_signal)
yf = fft(sweep_signal)
xf = fftfreq(N, 1 / fs)[: N // 2]
amp = 2.0 / N * np.abs(yf[: N // 2])

df = pd.DataFrame({"Frequency_Hz": xf, "Amplitude": amp, "source": "SIMULATED_SINE_SWEEP"})
df.to_csv(OUT / "sim_fft_sweep.csv", index=False)
print(f"Simulated FFT data -> {OUT / 'sim_fft_sweep.csv'}")

plt.figure(figsize=(10, 4))
plt.plot(xf, amp, lw=0.8)
plt.axvline(377, color="r", ls="--", label="377 Hz marker (not a measured peak)")
plt.xlim(50, 1000)
plt.title("SIMULATION — synthetic sine sweep FFT (not mic data)")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Amplitude")
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig(OUT / "sim_fft_sweep.png", dpi=150)
plt.close()
print(f"Simulated FFT plot -> {OUT / 'sim_fft_sweep.png'}")
