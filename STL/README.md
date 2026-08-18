# STL folder

| File | Use |
| --- | --- |
| `sabu_approx_1to4.stl` | Desk-scale (~152.5 mm Ø) — **generate** with the exporter |
| `null_twin_1to4.stl` | Matching null twin for Mode A |
| `*_placeholder*.stl` | **Removed / do not use** — old gear-like geometry |

## Generate printable meshes

```bash
# from repo root (stdlib only)
python code/export_stl_approx.py --scale 0.25 --out STL
# → STL/sabu_approx_1to4.stl
# → STL/null_twin_1to4.stl

python code/export_stl_approx.py --scale 0.5 --out STL
# → STL/sabu_approx_scale0p5.stl (+ null)
```

Finer lobe curvature (OpenSCAD):

```text
open code/openscad/sabu_disk_approx.scad
F6 → Export as STL  (sabu_approx)
swap to null_twin(); F6 → Export
```

**Approximate only** — not a JE 71295 laser scan.  
Check: three open kidney voids, continuous rim, central bore.  
Print notes: `docs/REPLICA.md`.
