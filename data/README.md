# Data directory

> **Everything here is SIMULATION / teaching unless the filename starts with `mic_`.**

| Path | Status |
| --- | --- |
| `sabu_disk/*` | SIM — synthetic FFT / PIV teaching outputs |
| `buga_sphere/*` | SIM — extension study only (not the Sabu null-test path) |
| Future `mic_*.wav` / `mic_*.csv` | Real recordings only |

## Naming rule

| Prefix | Meaning |
| --- | --- |
| `sim_` | Synthetic or teaching output |
| `mic_` | Real sensor recording |
| `null_` | Null-twin run (after unblinding, or in private notes) |

Legacy names without a prefix → treat as **sim**.

Do not publish a 377 Hz “result” from this folder without a pre-register sheet and a null-twin metric ([docs/ACOUSTIC_TEST.md](../docs/ACOUSTIC_TEST.md), [docs/NULL_TEST.md](../docs/NULL_TEST.md)).
