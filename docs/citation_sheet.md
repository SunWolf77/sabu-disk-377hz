# Citation sheet — Sabu disk replication

## Museum / archaeology (primary)

- **Inventory:** Egyptian Museum, Cairo — **JE 71295**  
- **Excavation:** Walter B. Emery, 19 January 1936, mastaba **S3111**, Saqqara (Room E, beside burial)  
- **Emery, W. B. (1949).** *Great Tombs of the First Dynasty*, Vol. 1. Cairo: Government Press. Especially Fig. 58 (plan and section).  
- **El-Khouli, A. (1978).** *Egyptian Stone Vessels: Predynastic Period to Dynasty III*. Mainz: Philipp von Zabern. Vol. 2, p. 730, no. 5586; Vol. 3, pls. 135 (drawing), 158 (photo).

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

## This repo’s experimental layer

- Simulated FFT / PIV scripts = teaching tools (labelled in code).  
- Physical claims require mic data + null twin + pre-registered metric (`docs/NULL_TEST.md`).  
- SUPT probe (Sheppard) is a separate instrument for ordered series — not proof of disk function.

## Buga extension (out of Sabu L1)

Scripts under `code/buga_*.py` and files in `data/buga_sphere/` are **synthetic teaching plots** only (`docs/BUGA_EXTENSION.md`).  
They do **not** document or validate public media claims about a metallic sphere reported from Buga, Colombia (2025–). Those claims are external; this repo does not host their primary data.

## Optional cultural / framework notes (L3 only)

- 377 ≈ F14; free-space impedance Z₀ ≈ 376.73 Ω — a **numeric rhyme**, not a measured carving tone on the artifact.  
- Keep framework notes out of the results table until a transducer and null test exist.

### 377 Hz as a test target (L3)

- **Newton, Emily.** *Tesla Towers 377* (working paper). Treats **377 Hz** as the 15th Fibonacci number (F14 = 377) and as a correction of Tesla’s 3-6-9 cycle as an incomplete 2D loop. That framing is why 377 Hz is a **drive target** in this project. It is not a museum label, and it does not by itself identify 377 Ω (Z₀).  
- **Sheppard, Paul.** SUPT (proxy / remeasurement). Ordered-series instrument — not a disk oracle.  
- Holonomy discriminator: [BERRY_377.md](BERRY_377.md).
