import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.fft import fft, fftfreq

fs = 44100
duration = 1.0
t = np.linspace(0, duration, int(fs * duration), endpoint=False)

target_freqs = [233, 377, 610]
results = []

plt.figure(figsize=(10, 5))
for f in target_freqs:
    signal = np.sin(2 * np.pi * f * t)
    N = len(signal)
    yf = fft(signal)
    xf = fftfreq(N, 1 / fs)[:N//2]
    amplitude = 2.0/N * np.abs(yf[:N//2])
    idx = np.argmin(np.abs(xf - f))
    results.append((f, xf[idx], amplitude[idx]))
    plt.plot(xf, amplitude, label=f"{f} Hz")

df = pd.DataFrame(results, columns=["Target_Freq", "Closest_Freq", "Amplitude"])
df.to_csv("../data/buga_sphere/buga_fft_focus.csv", index=False)

plt.title("Buga Sphere FFT Focused Simulation (233, 377, 610 Hz)")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Amplitude")
plt.xlim(0, 1000)
plt.legend()
plt.grid()
plt.tight_layout()
plt.savefig("../data/buga_sphere/buga_fft_focus.png")
