# Data directory

| Path | Status |
| --- | --- |
| `sabu_disk/*.csv`, `*.png` (legacy names) | **SIMULATION / teaching** — not microphone data |
| `buga_sphere/*` | **SIMULATION / teaching** unless a file is explicitly prefixed `mic_` |
| Future `mic_*.wav` / `mic_*.csv` | Real recordings only |

## Naming rule

| Prefix | Meaning |
| --- | --- |
| `sim_` | Synthetic or teaching output |
| `mic_` | Real sensor recording |
| `null_` | Null-twin run (after unblinding, or in private notes) |

If a legacy file has no prefix, treat it as **sim** until proven otherwise.

Do not publish a 377 Hz “result” from files in this folder without a matching pre-register sheet and null twin metric (`docs/ACOUSTIC_TEST.md`, `docs/NULL_TEST.md`).
