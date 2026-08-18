# data/sabu_disk — simulation outputs (not mic)

All current files in this folder are **teaching / simulation** artifacts.

| File | Status |
| --- | --- |
| `raw_fft_data.csv` | SIM — synthetic sweep product (legacy name) |
| `sabu_fft_spectrum.png` | SIM plot |
| `sabu_piv_simulation.png` | SIM quiver |

Real Mode A recordings should be added as `mic_*.wav` (or mono CSV) and analyzed with:

```bash
python code/analyze_mic.py path/to/mic_run.wav --f0 377 --half 2
```

See `docs/ACOUSTIC_TEST.md`.
