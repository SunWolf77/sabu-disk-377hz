# Docs map

| File | What it is |
| --- | --- |
| [BERRY_377.md](BERRY_377.md) | 377 Hz / Z₀ holonomy 2×2 · Möbius ±2π/3. Cites Paterson et al. PRA + Moreno 1948 for 377 Ω. |
| [citation_sheet.md](citation_sheet.md) | Who owns what · Emery, Newton, Sheppard, Moreno, Paterson/UWA, TORUS, this repo |
| [REPLICA.md](REPLICA.md) | Museum dimensions, print scales, supports, allowed claims |
| [ACOUSTIC_TEST.md](ACOUSTIC_TEST.md) | Mode A (forced response vs null) · Mode B (eigenmodes) |
| [NULL_TEST.md](NULL_TEST.md) | Blinding steps + pre-registered kill rule (replica lane) |
| [REPLICATION.md](REPLICATION.md) | How to add STL commits or mic runs without breaking hygiene |
| [BUGA_EXTENSION.md](BUGA_EXTENSION.md) | Volumetric cousins (Buga sims, dodecahedron note) — **not** Sabu L1 |

Holonomy pre-register: [../templates/pre_register_holonomy.txt](../templates/pre_register_holonomy.txt)  
Extractor stub: `python code/wilson_extract.py`  
d/λ stub: `python code/scale_d_lambda.py`

Root overview: [../README.md](../README.md)  
Mesh workflow: [../STL/README.md](../STL/README.md)

---

## Terms in plain language

**FFT** — splits a waveform into frequencies.  
`fft_sweep.py` / `buga_fft_focus.py` are **synthetic** teaching data. Real tests need `mic_` recordings.

**PIV** — lab method for fluid motion imaging.  
`piv_simulation.py` / `buga_piv_simulation.py` are **synthetic** quiver plots, not lab runs.

**STL** — triangle mesh for printing.  
Generate with `bash code/generate_stls.sh` or OpenSCAD. Approximate geometry only.

**Null twin** — control object with the same outer envelope but **no** three-lobe openings. Required for Mode A.

**Planar vs volumetric** — hypothesis that Sabu is a disk/bowl (surface modes) and a sphere or dodecahedron would be a cavity (volume modes). Same *question type*, separate objects. See root README and [BUGA_EXTENSION.md](BUGA_EXTENSION.md).

**Buga extension** — optional sphere-themed sims in `data/buga_sphere/`. Separate from Sabu L1.

**L1 / L2 / L3** — instrument data / standard tools / interpretive framework. Keep them separate.

**Paterson et al.** — UWA microwave Möbius ±2π/3. Literature null. Not a Sabu measurement.

**Moreno 1948** — handbook source for 377 Ω as free-space wave impedance. Not 377 Hz, not the disk.

**Newton vs this repo** — Newton is cited for an optional 377 Hz drive. Z₀ / holonomy 2×2 is this repo. See [citation_sheet.md](citation_sheet.md).
