# Sabu Disk — open replication & acoustic tests

**Artifact:** Egyptian Museum, Cairo · **JE 71295**  
**Find:** Mastaba S3111, Saqqara · 19 January 1936 · Walter B. Emery  
**Date:** First Dynasty, c. 3000–2800 BC

Open tools to **replicate the published form** and run **honest acoustic comparisons**.  
This is not a certificate of ancient “resonance technology.” The original’s function remains unknown.

---

## Museum facts

| Property | Value | Source |
| --- | --- | --- |
| Outer diameter | **61 cm** | Emery 1949 |
| Maximum height | **10.6 cm** | Emery 1949 |
| Central hole | **~8 cm** | Museum descriptions |
| Material | Weakly metamorphic **siltstone** (historically “schist”) | Emery / catalogues |
| Form | Shallow bowl; three lobes folded **inward** toward a central socket; outer rim as narrow arches between lobes | Emery 1949 Fig. 58 |

**Plain form:** not a gear. A thin-walled stone *bowl* with three curved wings bent toward a tubular centre.

Primary drawing: Emery, W. B. (1949). *Great Tombs of the First Dynasty*, Vol. 1. Cairo: Government Press, Fig. 58.  
Catalogue: El-Khouli, A. (1978). *Egyptian Stone Vessels*, Vol. 2 no. 5586; Vol. 3 pls. 135, 158.

---

## Claim hygiene

| Layer | What belongs here |
| --- | --- |
| **L1 — instrument** | Mic traces, measured print dimensions, blinded null scores |
| **L2 — literature tools** | FFT, PIV ideas, standard acoustics |
| **L3 — framework** | 377 Hz as F14, Z₀ rhyme, “modulator,” ancient intent |

- `code/fft_sweep.py`, `code/piv_simulation.py`, and files under `data/` **without** a `mic_` prefix are **simulations / teaching** — not microphone data.
- A real band claim needs: print → fixed drive → **null twin** → `analyze_mic.py` → blinded score (`docs/NULL_TEST.md`).
- Printing proves **form is reproducible**. It does not prove resonance or purpose.

---

## Quick start

```bash
git clone https://github.com/SunWolf77/sabu-disk-377hz.git
cd sabu-disk-377hz
pip install -r requirements.txt

# Teaching simulations only (not physical data)
python code/fft_sweep.py
python code/piv_simulation.py

# After a real recording
python code/analyze_mic.py path/to/mic_run.wav --f0 377 --half 2
python code/analyze_mic.py mic_a.wav mic_b.wav --compare
```

### Physical path (one pass)

1. **Print** — [docs/REPLICA.md](docs/REPLICA.md) (Sabu-form + null twin; OpenSCAD approx in `code/openscad/`).  
2. **Log the print** — [templates/print_log.csv](templates/print_log.csv).  
3. **Pre-register** — [templates/pre_register.txt](templates/pre_register.txt).  
4. **Run acoustics** — [docs/ACOUSTIC_TEST.md](docs/ACOUSTIC_TEST.md) (Mode A vs null).  
5. **Blind & score** — [docs/NULL_TEST.md](docs/NULL_TEST.md).  
6. **Commit cleanly** — [docs/REPLICATION.md](docs/REPLICATION.md).

---

## Repo layout

```
code/
  analyze_mic.py              # Mode A metric from WAV / mono CSV
  openscad/sabu_disk_approx.scad   # parametric approx + null_twin()
  acoustic_logger.ino         # relative multi-mic stream (not calibrated SPL)
  fft_sweep.py                # SIM only
  piv_simulation.py           # SIM only
STL/                          # placeholders deprecated — prefer OpenSCAD export
docs/
  REPLICA.md                  # dimensions, supports, print scales
  ACOUSTIC_TEST.md            # Mode A forced response + Mode B eigenmodes
  NULL_TEST.md                # blind protocol + kill rule
  REPLICATION.md              # how to add a run without breaking hygiene
templates/
  print_log.csv
  pre_register.txt
data/                         # treat as SIM unless filename is mic_*
requirements.txt
```

---

## 3D printing

See **[docs/REPLICA.md](docs/REPLICA.md)** for sourced dimensions, scale factors (1:2, 1:4, 1:10), support rules, and what a print may claim.

- Preferred model: `code/openscad/sabu_disk_approx.scad` (kidney openings, inward lobe fold, `null_twin()`).
- STL placeholders under `STL/` are **legacy / wrong geometry** — do not print those for a serious null test.
- PLA ≠ siltstone. Log mass, walls, and measured Ø with every acoustic run.

---

## Acoustic testing

See **[docs/ACOUSTIC_TEST.md](docs/ACOUSTIC_TEST.md)**.

| Mode | Question |
| --- | --- |
| **A — forced response** | Under the same drive, does Sabu-form differ from the null twin in a chosen band? |
| **B — eigenmodes** | What does *this print* ring at when struck? |

377 Hz is a **test target**, not a museum label. Publish Sabu and null numbers together.

---

## Highest-leverage next step

Print **1:4** Sabu + null → one blinded Mode A session → commit `mic_` files + filled templates.  
Until that exists, this repo is a **protocol + teaching sims**. After that, it is a **bench**.

---

## Collaborators / lineage

- Ben Rowe (@SunWolf77) — replication / open science  
- Paul Sheppard — SUPT instrument context (separate ruler; not a disk oracle)  
- Museum record — Emery 1949; Egyptian Museum JE 71295

## License

MIT. Cite **JE 71295** and **Emery 1949** when publishing replicas or acoustic results.
