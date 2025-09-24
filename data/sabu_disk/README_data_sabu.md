# Data — Sabu Disk Resonance Tests

This folder contains raw simulation data for the **Sabu Disk** acoustic resonance study.

---

## Files
- **raw_fft_data.csv** — Frequencies (50–1000 Hz) and amplitudes from acoustic FFT sweep.  
- Generated using `fft_sweep.py` in `/code`.

---

## How to Reproduce
1. Navigate to `/code`:
   ```bash
   cd code
   python fft_sweep.py
   ```
2. The script outputs:
   - `raw_fft_data.csv` → this data file
   - `fft_sweep.png` → resonance plot (optional, store in this folder if desired)

---

## Notes
- Key resonance observed at **377 Hz** (15th Fibonacci number).  
- This aligns with SUPT’s hypothesis that the Sabu Disk acts as a planar harmonic device tuned to Fibonacci pivots.
