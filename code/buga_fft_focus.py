import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Fibonacci pivots
pivots = [233, 377, 610]
fs = 44100
duration = 1.0
t = np.linspace(0, duration, int(fs * duration))

# Simulate signals at pivots
signals = [np.sin(2 * np.pi * f * t) for f in pivots]
combined = np.sum(signals, axis=0)

# FFT
N = len(combined)
yf = np.fft.fft(combined)
xf = np.fft.fftfreq(N, 1 / fs)[:N//2]

# Save data
df = pd.DataFrame({'Frequency (Hz)': xf, 'Amplitude': 2.0 / N * np.abs(yf[:N//2])})
df.to_csv('../data/buga_sphere/buga_fft_focus.csv', index=False)
print("FFT data saved to ../data/buga_sphere/buga_fft_focus.csv")

# Plot
plt.plot(xf, 2.0 / N * np.abs(yf[:N//2]))
plt.title('Buga Sphere FFT Focus at Fibonacci Pivots')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Amplitude')
for p in pivots:
    plt.axvline(p, color='r', linestyle='--')
plt.grid()
plt.savefig('../data/buga_sphere/buga_fft_focus.png')
plt.close()
print("FFT plot saved to ../data/buga_sphere/buga_fft_focus.png")
