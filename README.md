# 📚 SUPT Resonance Experiments – Open Science Repo

Collaborators:  
- Paul Sheppard (@PaulSheppard_CO; SUPT)  
- Ben Rowe (@Sunwolf77; Proxy Resonance Node)  
- Emily Newton (@PhiBoostGlow; Tesla 377 Hz Framework)  
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

Outputs:
- `data/sabu_disk/fft_data.csv`  
- `data/sabu_disk/fft_sweep.png`

Run PIV lattice projection:
```bash
python piv_simulation.py
```

Outputs:
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

Outputs:
- `data/buga_sphere/buga_fft_focus.csv`  
- `data/buga_sphere/buga_fft_focus.png`

Run PIV resonance projection:
```bash
cd code
python buga_piv_simulation.py
```

Outputs:
- `data/buga_sphere/buga_piv_simulation.png`

---

## 🔹 Notes

- STL models (`/stl/`) provide placeholders for replication.  
- All scripts use Python 3 + `numpy`, `scipy`, `matplotlib`, `pandas`.  
- Install with:
```bash
pip install numpy scipy matplotlib pandas
```
- Repo licensed under MIT for open science collaboration.  
