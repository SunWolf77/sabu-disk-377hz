import pandas as pd

# Load FFT data
df = pd.read_csv("data/raw_fft_data.csv")

# Find 377 Hz row
row = df.iloc[(df['Frequency'] - 377).abs().argmin()]
print(f"Closest to 377 Hz: {row['Frequency']} Hz, Amplitude: {row['Amplitude']:.4f}")
