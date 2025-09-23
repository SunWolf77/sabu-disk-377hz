import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft, fftfreq
import pandas as pd

# Parameters
fs = 44100  # sample rate
duration = 0.1  # seconds per frequency
frequencies = np.arange(50, 1001, 1)  # sweep range

# Time vector
t = np.linspace(0, duration, int(fs * duration), endpoint=False)

# Generate spherical sweep signal (proxy: sum of sine waves scaled by spherical volume factor)
signals = [np.sin(2 * np.pi * f * t) * (4/3 * np.pi * (1.0**3)) for f in frequencies]  # volume factor constant
sweep_signal = np.concatenate(signals)

# FFT
N = len(sweep_signal)
yf = fft(sweep_signal)
xf = fftfreq(N, 1 / fs)[:N//2]

# Focus on Fibonacci pivots: 233, 377, 610 Hz
target_freqs = [233, 377, 610]
results = {}
for f in target_freqs:
    idx = np.argmin(np.abs(xf - f))
    results[f] = np.abs(yf[idx]) * 2.0 / N

# Print results
for f, amp in results.items():
    print(f"Closest to {f} Hz: Amplitude {amp:.6f}")

# Plot FFT
plt.figure(figsize=(10, 5))
plt.plot(xf, 2.0/N * np.abs(yf[:N//2]), label="FFT Spectrum")
for f, amp in results.items():
    plt.axvline(f, color='r', linestyle='--', label=f'{f} Hz ~ {amp:.4f}')
plt.title("Buga Sphere FFT Sweep Simulation (50–1000 Hz)")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Amplitude")
plt.legend()
plt.grid()
plt.tight_layout()
plt.savefig("buga_fft_sweep.png")

# Save FFT data to CSV
fft_data = pd.DataFrame({"Frequency": xf, "Amplitude": 2.0/N * np.abs(yf[:N//2])})
fft_data.to_csv("buga_fft_data.csv", index=False)
