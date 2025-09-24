# buga_check.py
# Quick validation of Buga Sphere FFT data (Fibonacci pivot checks)

import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file
data = pd.read_csv("../data/buga_sphere/buga_fft_focus.csv")

# Define Fibonacci pivot frequencies of interest
fib_pivots = [233, 377, 610]

# Plot FFT sweep
plt.figure(figsize=(10, 5))
plt.plot(data['Frequency'], data['Amplitude'], label="FFT Spectrum", color='orange')

# Add markers for pivot frequencies
for f in fib_pivots:
    plt.axvline(f, color='r', linestyle='--')
    amp = data.loc[(data['Frequency']-f).abs().idxmin(), 'Amplitude']
    plt.text(f+5, amp, f"{f} Hz ~ {amp:.4f}", rotation=90, color='red')

plt.title("Buga Sphere FFT Sweep (50–1000 Hz)")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Amplitude")
plt.legend()
plt.grid()
plt.show()

# Print amplitudes at pivot points
print("Fibonacci Pivot Amplitudes:")
for f in fib_pivots:
    amp = data.loc[(data['Frequency']-f).abs().idxmin(), 'Amplitude']
    print(f"  {f} Hz → {amp:.6e}")
