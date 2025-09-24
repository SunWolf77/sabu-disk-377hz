# sabu_check.py
# Quick validation of Sabu Disk FFT data (377 Hz resonance check)

import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file
data = pd.read_csv("../data/sabu_disk/raw_fft_data.csv")

# Plot FFT sweep
plt.figure(figsize=(10, 5))
plt.plot(data['Frequency'], data['Amplitude'], label="FFT Spectrum", color='blue')
plt.axvline(377, color='r', linestyle='--', label="377 Hz")
plt.title("Sabu Disk FFT Sweep (50–1000 Hz)")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Amplitude")
plt.legend()
plt.grid()
plt.show()

# Print amplitude near 377 Hz
amp_377 = data.loc[(data['Frequency']-377).abs().idxmin(), 'Amplitude']
print(f"Amplitude at ~377 Hz: {amp_377:.6e}")
