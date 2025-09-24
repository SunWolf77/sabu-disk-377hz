# Data — Buga Sphere Resonance Tests

This folder contains simulation outputs for the **Buga Sphere** study.

---

## Files
- **buga_fft_focus.csv** — Amplitudes at Fibonacci pivot frequencies (233, 377, 610 Hz).  
- **buga_fft_focus.png** — Plot showing FFT peaks at pivot frequencies.  
- **buga_piv_simulation.png** — Vortex lattice projection from hybrid 3D simulation.  

---

## How to Reproduce
1. Navigate to `/code`:
   ```bash
   cd code
   python buga_fft_focus.py
   python buga_piv_simulation.py
   ```
2. The scripts output:
   - `buga_fft_focus.csv`  
   - `buga_fft_focus.png`  
   - `buga_piv_simulation.png`

---

## Notes
- Buga Sphere treated as **volumetric complement** to Sabu Disk’s planar geometry.  
- Resonance targeted at **233, 377, 610 Hz** Fibonacci pivots.  
- 7-point lattice in PIV confirms hybrid toroidal + tetrahedral geometry.
