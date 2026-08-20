# Data directory

> **Everything here is SIMULATION / teaching unless the filename starts with `mic_`.**

| Path | Status |
| --- | --- |
| `sabu_disk/*` | SIM — synthetic FFT / PIV teaching outputs |
| `buga_sphere/*` | SIM — **extension only** (not Sabu null-test); see [buga_sphere/README_data_buga.md](buga_sphere/README_data_buga.md) |
| Future `mic_*.wav` / `mic_*.csv` | Real recordings only |

## Naming rule

| Prefix | Meaning |
| --- | --- |
| `sim_` | Synthetic or teaching output |
| `mic_` | Real sensor recording |
| `null_` | Null-twin run (after unblinding, or in private notes) |

Legacy names without a prefix → treat as **sim**.

Do not publish a 377 Hz “result” from this folder without a pre-register sheet and a null-twin metric ([docs/ACOUSTIC_TEST.md](../docs/ACOUSTIC_TEST.md), [docs/NULL_TEST.md](../docs/NULL_TEST.md)).
