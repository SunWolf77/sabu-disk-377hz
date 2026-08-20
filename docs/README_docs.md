# Docs map

| File | What it is |
| --- | --- |
| [REPLICA.md](REPLICA.md) | Museum dimensions, print scales, supports, allowed claims |
| [ACOUSTIC_TEST.md](ACOUSTIC_TEST.md) | Mode A (forced response vs null) · Mode B (eigenmodes) |
| [NULL_TEST.md](NULL_TEST.md) | Blinding steps + pre-registered kill rule |
| [REPLICATION.md](REPLICATION.md) | How to add STL commits or mic runs without breaking hygiene |
| [citation_sheet.md](citation_sheet.md) | Emery, El-Khouli, JE 71295, and related citations |
| [BUGA_EXTENSION.md](BUGA_EXTENSION.md) | Optional Buga sim lane — **not** Sabu null-test |

Root overview: [../README.md](../README.md)  
Mesh workflow: [../STL/README.md](../STL/README.md)

---

## Terms in plain language

**FFT** — splits a waveform into frequencies.  
`fft_sweep.py` / `buga_fft_focus.py` are **synthetic** teaching data. Real tests need `mic_` recordings.

**PIV** — lab method for fluid motion imaging.  
`piv_simulation.py` / `buga_piv_simulation.py` are **synthetic** quiver plots, not lab runs.

**STL** — triangle mesh for printing.  
Generate with `code/export_stl_approx.py` or OpenSCAD. Approximate geometry only.

**Null twin** — control object with the same outer envelope but **no** three-lobe openings. Required for Mode A.

**Buga extension** — optional sphere-themed sims in `data/buga_sphere/`. Separate from Sabu L1.

**L1 / L2 / L3** — instrument data / standard tools / interpretive framework. Keep them separate.
