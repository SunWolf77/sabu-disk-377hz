# Data Folder — SUPT Resonance Tests

This folder contains raw simulation data and figures for both the **Sabu Disk** and the **Buga Sphere** resonance studies.

---

## Sabu Disk (377 Hz)
- **raw_fft_data.csv** — Frequencies (50–1000 Hz) and amplitudes from acoustic FFT sweep.
- Use `fft_quickcheck.py` in `/code` to confirm the resonance peak at 377 Hz.

---

## Buga Sphere
- **buga_piv_simulation.png** — Vortex lattice from hybrid 3D simulation.
- Outputs generated with `buga_fft_focus.py` and `buga_piv_simulation.py` in `/code`.

---

## How to Use
- Run `fft_quickcheck.py` → validates Sabu Disk’s 377 Hz resonance.
- Run `buga_fft_focus.py` → quick FFT check for Buga Sphere.
- Run `buga_piv_simulation.py` → visualize 3D vortex lattice nodes.
