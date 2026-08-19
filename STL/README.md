# STL folder

| File | Use |
| --- | --- |
| `sabu_approx_1to4.stl` | Desk-scale (~152.5 mm Ø) — **generate** with the exporter |
| `null_twin_1to4.stl` | Matching null twin for Mode A |

Meshes are **approximate** (Emery 1949 dims), not a JE 71295 laser scan.  
`*.stl` is marked binary in `.gitattributes`.

---

## Generate

```bash
# from repo root (Python stdlib only)
python code/export_stl_approx.py --scale 0.25 --out STL
# → STL/sabu_approx_1to4.stl
# → STL/null_twin_1to4.stl

python code/export_stl_approx.py --scale 0.5 --out STL   # ~305 mm Ø
```

Finer lobes (OpenSCAD): open `code/openscad/sabu_disk_approx.scad` → F6 → Export; then `null_twin()` → Export.

**Before print:** three open kidney voids, continuous rim, central bore on Sabu; null is plain bowl + hub.  
Print notes: [docs/REPLICA.md](../docs/REPLICA.md).

---

## Commit binaries (optional)

Only needed if you want the meshes tracked on GitHub for others.

```bash
git pull origin main
python code/export_stl_approx.py --scale 0.25 --out STL

ls -la STL/sabu_approx_1to4.stl STL/null_twin_1to4.stl
# slicer check: light through three kidneys

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
