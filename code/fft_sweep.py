import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft, fftfreq

# Parameters
fs = 44100  # Sampling rate
duration = 0.1  # seconds per frequency
frequencies = np.arange(50, 1001, 1)

# Generate sweep signal
t = np.linspace(0, duration, int(fs * duration), endpoint=False)
signals = [np.sin(2 * np.pi * f * t) for f in frequencies]
sweep_signal = np.concatenate(signals)

# FFT
N = len(sweep_signal)
yf = fft(sweep_signal)
xf = fftfreq(N, 1 / fs)[:N//2]

# Plot
plt.figure()
plt.plot(xf, 2.0 / N * np.abs(yf[:N//2]))
plt.title('FFT Sweep of Acoustic Signal')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Amplitude')
plt.axvline(377, color='r', linestyle='--', label='377 Hz')
plt.legend()
plt.grid()
plt.show()