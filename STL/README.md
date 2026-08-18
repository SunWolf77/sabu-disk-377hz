# STL folder

| File | Use |
| --- | --- |
| `sabu_approx_1to4.stl` | Desk-scale (~152.5 mm Ø) — generate + commit |
| `null_twin_1to4.stl` | Matching null twin for Mode A |
| `*_placeholder*.stl` | **Do not use** — old gear-like geometry (delete if still present) |

Meshes are **approximate** (Emery 1949 dims), not a JE 71295 laser scan.

---

## Generate printable meshes

```bash
# from repo root (Python stdlib only — no OpenSCAD required)
python code/export_stl_approx.py --scale 0.25 --out STL
# → STL/sabu_approx_1to4.stl
# → STL/null_twin_1to4.stl

python code/export_stl_approx.py --scale 0.5 --out STL
# → STL/sabu_approx_scale0p5.stl + null_twin_scale0p5.stl
```

Finer lobe curvature (OpenSCAD):

```text
open code/openscad/sabu_disk_approx.scad
F6 → Export as STL   (sabu_approx)
swap to null_twin(); F6 → Export
```

**Check before print:** three open kidney voids, continuous rim, central bore.  
Print notes: `docs/REPLICA.md`.

---

## Commit binary STLs (local git)

Binary meshes are generated on your machine, then committed. Do this from a clean working tree after `git pull`.

### 1. Generate

```bash
cd /path/to/sabu-disk-377hz
git pull origin main
python code/export_stl_approx.py --scale 0.25 --out STL
```

Optional OpenSCAD exports — same filenames if you want finer lobes:

- `STL/sabu_approx_1to4.stl`
- `STL/null_twin_1to4.stl`

### 2. Verify

```bash
ls -la STL/sabu_approx_1to4.stl STL/null_twin_1to4.stl
# both should be non-empty binary STLs (typically 100 KB–1 MB)

# quick sanity: file starts with 80-byte header (binary) or "solid " (ASCII)
xxd STL/sabu_approx_1to4.stl | head -2
```

In your slicer: open both → **light through three kidneys** on Sabu-form; null is plain bowl + hub.  
Delete any leftover `*_placeholder*.stl` so they are not committed.

```bash
rm -f STL/*placeholder*.stl STL/buga_sphere_placeholder.stl
```

### 3. Commit

```bash
git add STL/sabu_approx_1to4.stl STL/null_twin_1to4.stl STL/README.md
git status   # confirm only the intended meshes (+ no placeholders)

git commit -m "Add binary STLs: sabu_approx_1to4 + null_twin_1to4 (export_stl_approx 0.25)"
git push origin main
```

Other scales — same pattern, different names:

```bash
python code/export_stl_approx.py --scale 0.5 --out STL
git add STL/sabu_approx_scale0p5.stl STL/null_twin_scale0p5.stl
git commit -m "Add binary STLs at scale 0.5"
git push origin main
```

### 4. Optional .gitattributes (line endings)

Binary STLs should not be text-normalized:

```bash
echo "*.stl binary" >> .gitattributes
git add .gitattributes
git commit -m "Mark STL files as binary"
git push origin main
```

---

## What not to commit

| Avoid | Why |
| --- | --- |
| `*_placeholder*.stl` | Wrong (gear-like) geometry |
| Unlabelled “final_peak.stl” | Breaks hygiene / naming |
| Only Sabu without null twin | Mode A needs both |
| Claiming museum-exact mesh | Still an approximation |
