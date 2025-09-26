import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft, fftfreq
import pandas as pd

# Sampling rate and duration
fs = 44100  # Hz
duration = 0.1  # seconds per frequency
t = np.linspace(0, duration, int(fs * duration), endpoint=False)

# Frequencies to sweep (50-1000 Hz, 1 Hz steps)
frequencies = np.arange(50, 1001, 1)
signals = [np.sin(2 * np.pi * f * t) for f in frequencies]  # Sine waves

# Concatenate for full sweep signal
sweep_signal = np.concatenate(signals)

# FFT analysis
N = len(sweep_signal)
yf = fft(sweep_signal)
xf = fftfreq(N, 1 / fs)[:N//2]

# Save raw FFT data to CSV
df = pd.DataFrame({'Frequency (Hz)': xf, 'Amplitude': 2.0 / N * np.abs(yf[:N//2])})
df.to_csv('../data/sabu_disk/raw_fft_data.csv', index=False)
print("Raw FFT data saved to ../data/sabu_disk/raw_fft_data.csv")

# Plot FFT
plt.figure()
plt.plot(xf, 2.0 / N * np.abs(yf[:N//2]))
plt.title('Simulated FFT of Acoustic Sweep (Focus 377 Hz)')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Amplitude')
plt.axvline(377, color='r', linestyle='--', label='377 Hz Peak')
plt.legend()
plt.grid()
plt.savefig('../data/sabu_disk/fft_sweep.png')
plt.close()
print("FFT plot saved to ../data/sabu_disk/fft_sweep.png")
