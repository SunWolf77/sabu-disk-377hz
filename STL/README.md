# STL folder

Meshes are **approximate** (Emery 1949 dims), not a JE 71295 laser scan.  
`*.stl` is marked binary in `.gitattributes`.

| File | Use |
| --- | --- |
| `sabu_approx_1to4.stl` | Desk-scale (~152.5 mm Ø) — generate with the exporter |
| `null_twin_1to4.stl` | Matching null twin for Mode A |

These files are **not required in git**. Generate them locally before print.

---

## Generate (default 1:4)

From the repo root. No pip packages needed for this step.

```bash
git clone https://github.com/SunWolf77/sabu-disk-377hz.git
cd sabu-disk-377hz

# one command (recommended)
bash code/generate_stls.sh

# or call the exporter directly
python3 code/export_stl_approx.py --scale 0.25 --out STL
```

Expected output:

```
Wrote STL/sabu_approx_1to4.stl …  D=152.5 mm
Wrote STL/null_twin_1to4.stl …
```

### Other scales

```bash
bash code/generate_stls.sh 0.5 STL    # 1:2  → ~305 mm Ø
bash code/generate_stls.sh 1.0 STL    # 1:1  → 610 mm Ø (large bed / segments)
bash code/generate_stls.sh 0.1 STL    # 1:10 geometry check
```

Names at non-0.25 scales: `sabu_approx_scale0p5.stl` and `null_twin_scale0p5.stl` (dots become `p`).

ASCII instead of binary:

```bash
python3 code/export_stl_approx.py --scale 0.25 --out STL --ascii
```

---

## Verify before you slice

1. Both files exist and are non-empty (`ls -la STL/*.stl`).
2. Open **Sabu** in the slicer: three kidney voids pass light; central bore is open; rim is continuous. Not a gear.
3. Open **null twin**: same outer envelope and hub, **no** kidneys / no raised lobes.
4. Orientation: **bowl up** (floor on bed).
5. Supports: tree/organic under lobe undersides only; paint-exclude kidneys and hub bore. Null is usually support-free.

If the Sabu preview looks like a sprocket or the kidneys are filled solid, stop — wrong mesh or wrong support settings. See [docs/REPLICA.md](../docs/REPLICA.md).

---

## OpenSCAD path (finer lobes)

Use this if you want to tune `OPEN_HALF` / `SPOKE_RISE`.

1. Open `code/openscad/sabu_disk_approx.scad`.
2. Set `scale_factor` (default `0.25`).
3. Render (F6) → Export as `STL/sabu_approx_1to4.stl`.
4. Comment out `sabu_approx();`, uncomment `null_twin();`.
5. Render → Export as `STL/null_twin_1to4.stl`.

---

## After generation

1. Slice + print both parts — [docs/REPLICA.md](../docs/REPLICA.md).
2. Log mass / Ø / height — [templates/print_log.csv](../templates/print_log.csv).
3. Fill [templates/pre_register.txt](../templates/pre_register.txt) **before** any tone.
4. Blind Mode A — [docs/NULL_TEST.md](../docs/NULL_TEST.md).

---

## Optional: commit binaries

Only if you want GitHub visitors to download meshes without running Python.

```bash
git pull origin main
bash code/generate_stls.sh
ls -la STL/sabu_approx_1to4.stl STL/null_twin_1to4.stl
git add STL/sabu_approx_1to4.stl STL/null_twin_1to4.stl
git commit -m "Add binary STLs: sabu_approx_1to4 + null_twin_1to4"
git push origin main
```

---

## Do not commit

| Avoid | Why |
| --- | --- |
| Gear-like / “hubcap” fantasy meshes | Wrong geometry |
| Sabu without null twin | Mode A needs both |
| Claims of museum-exact scan | Still an approximation |
