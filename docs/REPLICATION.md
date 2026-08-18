# How to add a run without breaking hygiene

1. Print Sabu-form + null twin (`docs/REPLICA.md`). Log rows in `templates/print_log.csv`.
2. Fill `templates/pre_register.txt` **before** the session.
3. Positive check (no object, pure tone) — must pass.
4. Record coded files only (`OBJ-17_run1.wav`, not `sabu_peak.wav`).
5. Score with `python code/analyze_mic.py A.wav B.wav --compare`.
6. Open key last. Commit: pre-register sheet + print log + raw `mic_` files + metric table.
7. Never promote `sim_` plots into the results table.

Details: `docs/ACOUSTIC_TEST.md`, `docs/NULL_TEST.md`.
