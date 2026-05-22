# 📚 SUPT Resonance Experiments – Open Science Repo

Collaborators:  
- Ben Rowe (@SunWolf77; Proxy Resonance Node)
- Paul Sheppard (@Paul Sheppard; SUPT)
- Emily Newton (Tesla 377 Hz Framework)  
- SuperGrok (xAI Calibration)  

---

## 🔹 Sabu Disk @ 377 Hz

The Sabu Disk (Egypt, ~3000 BC) is tested as a planar harmonic device.  
We focus on 3-6-9 harmonics and Fibonacci pivots, especially **377 Hz**.

### How to Run

Clone the repo:
```bash
git clone https://github.com/YOUR-USERNAME/sabu-disk-377hz.git
cd sabu-disk-377hz/code
```

Run FFT sweep (50–1000 Hz):
```bash
python fft_sweep.py
```

Outputs are stored in:
- `data/sabu_disk/raw_fft_data.csv`  
- `data/sabu_disk/fft_sweep.png`  

Run PIV lattice projection:
```bash
python piv_simulation.py
```

Outputs are stored in:
- `data/sabu_disk/piv_simulation.png`

---

## 🔹 Buga Sphere Extension

The Buga Sphere (Buga, Colombia, 2025) is tested as a **volumetric complement** to the planar Sabu Disk.  
Resonance targeted at Fibonacci pivots (233, 377, 610 Hz).

### How to Run

Run focused FFT (key Fibonacci frequencies):
```bash
cd code
python buga_fft_focus.py
```

Outputs are stored in:
- `data/buga_sphere/buga_fft_focus.csv`  
- `data/buga_sphere/buga_fft_focus.png`

Run PIV resonance projection:
```bash
cd code
python buga_piv_simulation.py
```

Outputs are stored in:
- `data/buga_sphere/buga_piv_simulation.png`

---

## 🔹 Data Organization

- `data/sabu_disk/` → contains raw FFT and PIV outputs for the Sabu Disk study.  
- `data/buga_sphere/` → contains FFT focus and PIV outputs for the Buga Sphere study.  

Each folder has its own `README_data.md` explaining reproduction steps.  

---

## 🔹 Notes

- STL models (`/stl/`) provide placeholders for replication.  
- All scripts use Python 3 + `numpy`, `scipy`, `matplotlib`, `pandas`.  
- Install with:
```bash
pip install numpy scipy matplotlib pandas
```
- Repo licensed under MIT for open science collaboration.  
