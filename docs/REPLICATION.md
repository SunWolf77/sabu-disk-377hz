# How to add a run without breaking hygiene

## Generate STLs (before any print)

```bash
git pull origin main
bash code/generate_stls.sh
# → STL/sabu_approx_1to4.stl + STL/null_twin_1to4.stl
```

Verify in the slicer: three open kidneys on Sabu; plain bowl + hub on null.  
Full steps: [STL/README.md](../STL/README.md).

Optional — track the binaries on GitHub:

```bash
git add STL/sabu_approx_1to4.stl STL/null_twin_1to4.stl
git commit -m "Add binary STLs: sabu_approx_1to4 + null_twin_1to4"
git push origin main
```

## Acoustic / null run

1. Print Sabu-form + null twin (`docs/REPLICA.md`). Log rows in `templates/print_log.csv`.
2. Fill `templates/pre_register.txt` **before** the session.
3. Positive check (no object, pure tone) — must pass.
4. Record coded files only (`OBJ-17_run1.wav`, not `sabu_peak.wav`).
5. Score with `python3 code/analyze_mic.py A.wav B.wav --compare`.
6. Open key last. Commit: pre-register sheet + print log + raw `mic_` files + metric table.
7. Never promote `sim_` plots into the results table.

Details: `docs/ACOUSTIC_TEST.md`, `docs/NULL_TEST.md`.
