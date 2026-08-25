# Citation sheet — Sabu disk replication

## Who owns what

| Name | What we take from them | What we do **not** attribute to them |
| --- | --- | --- |
| **Emery 1949 · JE 71295** | Find, form, dimensions, siltstone | Any resonance, 377 Hz, or function |
| **Newton, *Tesla Towers 377*** | 377 Hz as a Fibonacci (F14) **drive-target proposal**; 3-6-9 as an incomplete 2D loop | Z₀ / 377 Ω, the holonomy test, replica protocol, disk function |
| **Sheppard, SUPT** | Proxy / remeasurement stance: same digits in two maps is a reason to check the maps | Disk function, identity of Hz with Ω |
| **Paterson, Tobar, Goryachev, Bourhill (UWA)** | Measured ±2π/3 on a triangular Möbius microwave cavity vs twin | Sabu, 377 Hz, Z₀ identity |
| **This repo (Rowe)** | STL + null twin + mic protocol; 2×2 on that holonomy null vs Z₀ | Newton’s paper; SUPT as proof; Paterson as a 377 result |

Cited sources are **not** repo collaborators. Citing them does not imply endorsement of the Z₀ test or of disk function.

---

## Museum / archaeology (primary)

- **Inventory:** Egyptian Museum, Cairo — **JE 71295**  
- **Excavation:** Walter B. Emery, 19 January 1936, mastaba **S3111**, Saqqara (Room E, beside burial)  
- **Emery, W. B. (1949).** *Great Tombs of the First Dynasty*, Vol. 1. Cairo: Government Press. Especially Fig. 58 (plan and section).  
- **El-Khouli, A. (1978).** *Egyptian Stone Vessels: Predynastic Period to Dynasty III*. Mainz: Philipp von Zabern. Vol. 2, p. 730, no. 5586; Vol. 3, pls. 135, 158.

## Dimensions used in this repo

| Qty | Value |
| --- | --- |
| Diameter | 61 cm |
| Height | 10.6 cm |
| Central hole | ~8 cm |

Sources: Emery 1949; museum/catalogue summaries as collated on [Wikipedia: Sabu disk](https://en.wikipedia.org/wiki/Sabu_disk) and [Egypt Museum](https://egypt-museum.com/sabu-disk/).

## Material

Weakly metamorphic siltstone (older literature often says “schist”). Fragile; not equivalent to PLA.

## Function

**Unknown.** Emery suggested ceremonial vessel / stand-mounted container; no consensus. Modern mechanical or acoustic readings are **hypotheses**, not museum labels.

## Literature (holonomy null)

- **Paterson, E. C. I., Tobar, M. E., Goryachev, M. & Bourhill, J.** *Distinct Berry phases in a single triangular Möbius microwave resonator.* Phys. Rev. A **113**, 04350 (2026). [doi:10.1103/qnym-rzrs](https://doi.org/10.1103/qnym-rzrs). Also [arXiv:2506.07320](https://arxiv.org/abs/2506.07320). Quantum Technologies and Dark Matter Labs, University of Western Australia. TE₁,₀,n ±2π/3 vs mirror twin.

## This repo’s experimental layer

- Simulated FFT / PIV scripts = teaching tools (labelled in code).  
- `code/wilson_extract.py` = Pancharatnam pipeline check + four-cell pre-register. **Not FEM.**  
- `code/scale_d_lambda.py` = d/λ scaling. **Not a frequency identity.**  
- Physical claims require mic data + null twin + pre-registered metric (`docs/NULL_TEST.md`). Holonomy claims require [templates/pre_register_holonomy.txt](../templates/pre_register_holonomy.txt).

## Buga extension (out of Sabu L1)

Scripts under `code/buga_*.py` and files in `data/buga_sphere/` are **synthetic teaching plots** only (`docs/BUGA_EXTENSION.md`).  
They do **not** document or validate public media claims about a metallic sphere reported from Buga, Colombia (2025–). Those claims are external; this repo does not host their primary data.

## L3 notes (keep out of the results table)

- **Newton:** optional acoustic drive at 377 Hz (Fibonacci 377).  
- **This repo:** 377 also appears as Z₀ ≈ 376.73 Ω. That is a **numeric rhyme we are testing**, not Newton’s claim.  
- Holonomy discriminator: [BERRY_377.md](BERRY_377.md).
