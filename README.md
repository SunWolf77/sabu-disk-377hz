# Sabu Disk — open replication & resonance tests

**Artifact:** Egyptian Museum, Cairo · **JE 71295**  
**Find:** Mastaba S3111, Saqqara · 19 January 1936 · Walter B. Emery  
**Date:** First Dynasty, c. 3000–2800 BC  

This repo supports **open replication** of the Sabu disk form and **honest acoustic / flow experiments**.  
It is not a certificate of ancient “resonance technology.” Function of the original remains unknown.

---

## What this object is (museum facts)

| Property | Value | Source |
| --- | --- | --- |
| Outer diameter | **61 cm** | Emery 1949; Egypt Museum summaries |
| Maximum height | **10.6 cm** | Emery 1949; Wikipedia (Sabu disk) |
| Central hole (approx.) | **~8 cm** diameter | Consensus museum descriptions |
| Material | Weakly metamorphic **siltstone** (historically called schist) | Emery / modern catalogues |
| Form | Shallow bowl; three lobes folded **inward** toward a central socket; outer rim remains as narrow arches between lobes | Emery 1949 Fig. 58 |

Primary drawing: **Emery, W. B. (1949).** *Great Tombs of the First Dynasty*, Vol. 1, Cairo: Government Press, Fig. 58 (p. 101).  
Catalogue note: El-Khouli, A. (1978). *Egyptian Stone Vessels*, Vol. 2 no. 5586; Vol. 3 pls. 135, 158.

**Form in plain words:** not a gear, not a toothed hubcap. A thin-walled stone *bowl* with three curved wings bent toward a tubular centre.

---

## Claim hygiene (read this)

| Layer | What lives here |
| --- | --- |
| **L1 — instrument** | Mic / logger traces, printed dimensions, blinded null comparisons |
| **L2 — literature physics** | FFT as a tool; PIV as a flow-visualisation idea |
| **L3 — framework** | 377 Hz as F14, Z₀ rhyme, “modulator,” ancient intent |

- Scripts under `code/fft_sweep.py` and `code/piv_simulation.py` are **simulations / teaching plots**. They are **not** microphone recordings of a physical disk.
- A real 377 Hz claim requires: physical replica → fixed drive → **null twin** → blinded score sheet (see `docs/NULL_TEST.md` and `docs/ACOUSTIC_TEST.md`).
- Printing the shape proves **form is reproducible**. It does not prove resonance or purpose.

---

## Repo layout

```
STL/                 # printables (approximate until laser-scan exists)
code/
  fft_sweep.py       # SIMULATED frequency sweep (labelled)
  piv_simulation.py  # SIMULATED flow field (labelled)
  acoustic_logger.ino
  openscad/
    sabu_disk_approx.scad   # parametric approx from published dims
data/
  sabu_disk/         # outputs (sim or real — label in filename)
  buga_sphere/       # separate extension study
docs/
  REPLICA.md         # 3D-print instructions + supports + sourced measurements
  NULL_TEST.md       # blind / kill-rule protocol
  ACOUSTIC_TEST.md   # Mode A forced response + Mode B eigenmodes
  citation_sheet.md
  README_docs.md
```

---

## Quick start

```bash
git clone https://github.com/SunWolf77/sabu-disk-377hz.git
cd sabu-disk-377hz
pip install numpy scipy matplotlib pandas

# Teaching simulations only (not physical data)
cd code
python fft_sweep.py
python piv_simulation.py
```

For a **physical** test:

1. Print from [`docs/REPLICA.md`](docs/REPLICA.md) (Sabu-form + null twin).  
2. Run acoustics per [`docs/ACOUSTIC_TEST.md`](docs/ACOUSTIC_TEST.md).  
3. Blind and score per [`docs/NULL_TEST.md`](docs/NULL_TEST.md).

---

## 3D printing

See **[docs/REPLICA.md](docs/REPLICA.md)** for:

- Sourced full-scale dimensions (61 cm Ø)
- Recommended scale factors (1:2, 1:4, 1:10)
- OpenSCAD approximate model + support recommendations
- Material notes (PLA ≠ siltstone)
- What a print can and cannot claim

---

## Acoustic testing

See **[docs/ACOUSTIC_TEST.md](docs/ACOUSTIC_TEST.md)** for:

- **Mode A** — forced response vs null (default null-test path)
- **Mode B** — structural eigenmodes of the print
- Instrumentation floor and logger limits
- Pre-register template and allowed claims

---

## Collaborators / lineage

- Ben Rowe (@SunWolf77) — replication / open science  
- Paul Sheppard — SUPT instrument context (probe is a separate ruler; not a disk oracle)  
- Museum & excavation record — Emery 1949; Egyptian Museum JE 71295  

---

## License

MIT — open science. Cite the museum inventory and Emery when publishing replicas or acoustic results.
