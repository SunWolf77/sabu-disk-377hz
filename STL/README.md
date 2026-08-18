# STL folder

| File | Use |
| --- | --- |
| `sabu_approx_1to4.stl` | Preferred desk-scale (~152.5 mm) — generate with `export_stl_approx.py` |
| `null_twin_1to4.stl` | Matching null twin |
| `sabu_disk_placeholder*.stl` | **Deprecated** — old gear-like geometry, do not print |
| `buga_sphere_placeholder.stl` | Placeholder only |

```bash
python code/export_stl_approx.py --scale 0.25 --out STL
# writes sabu_approx_scale0p25.stl and null_twin_scale0p25.stl
```

Finer lobes: `code/openscad/sabu_disk_approx.scad`. Approximate only — not JE 71295 scan.
