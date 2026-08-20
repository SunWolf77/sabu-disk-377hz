# Buga extension (optional)

**Role in this repo:** teaching / volumetric sketch lane — **not** the Sabu disk null-test.

## What exists

| Item | Purpose |
| --- | --- |
| `code/buga_fft_focus.py` | Synthetic sines at 233 / 377 / 610 Hz → SIM CSV + plot |
| `code/buga_piv_simulation.py` | Synthetic 3-fold quiver sketch |
| `code/buga_check.py` | Inspect SIM CSV marker bins |
| `data/buga_sphere/` | SIM outputs only (see folder README) |

```bash
python code/buga_fft_focus.py
python code/buga_piv_simulation.py
python code/buga_check.py   # optional interactive check
```

## Claim hygiene

- Fibonacci lines are **markers**, not measured peaks on a physical sphere.
- Public media claims about a “Buga Sphere” (Colombia, 2025–) are **outside** this repository’s L1 data.
- No ferrofluid, CT, or alloy result in this repo is tied to those scripts.
- Real acoustic work on any sphere-shaped object would need its own pre-register, null control, and `mic_` files — same standard as Sabu (`docs/NULL_TEST.md`).

## Relation to Sabu

| Sabu path | Buga path |
| --- | --- |
| JE 71295 form + null twin | Optional sim sketches |
| Mode A / Mode B protocols | No physical protocol in-repo |
| Primary open-science bench | Extension folder only |

Keep results tables separate.
