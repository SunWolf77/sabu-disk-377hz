#!/usr/bin/env python3
"""
export_stl_approx.py — approximate Sabu disk + null twin STLs (no OpenSCAD required)

Dimensions from Emery 1949 / JE 71295 (scaled). NOT a laser scan.
Prefer code/openscad/sabu_disk_approx.scad for finer lobe curvature.

Usage:
  python code/export_stl_approx.py --scale 0.25 --out STL
  python code/export_stl_approx.py --scale 0.5 --out STL --ascii
"""
from __future__ import annotations

import argparse
import math
import struct
from pathlib import Path


def dims(scale: float):
    D = 610.0 * scale
    return {
        "D": D,
        "R": D / 2,
        "H": 106.0 * scale,
        "HOLE": 80.0 * scale,
        "HUB_OD": 110.0 * scale,
        "WALL": max(2.4, 8.0 * scale),
        "RIM_H": 18.0 * scale,
        "FLOOR": max(1.6, 6.0 * scale),
        "OPEN_R0": (D / 2) * 0.30,
        "OPEN_R1": (D / 2) * 0.78,
        "OPEN_HALF": 28.0,
    }


def vsub(a, b):
    return (a[0] - b[0], a[1] - b[1], a[2] - b[2])


def vcross(a, b):
    return (
        a[1] * b[2] - a[2] * b[1],
        a[2] * b[0] - a[0] * b[2],
        a[0] * b[1] - a[1] * b[0],
    )


def vnorm(a):
    L = math.sqrt(a[0] * a[0] + a[1] * a[1] + a[2] * a[2]) or 1.0
    return (a[0] / L, a[1] / L, a[2] / L)


def write_stl_binary(path: Path, tris):
    with open(path, "wb") as f:
        f.write(b"\0" * 80)
        f.write(struct.pack("<I", len(tris)))
        for v1, v2, v3 in tris:
            n = vnorm(vcross(vsub(v2, v1), vsub(v3, v1)))
            f.write(struct.pack("<3f", *n))
            f.write(struct.pack("<3f", *v1))
            f.write(struct.pack("<3f", *v2))
            f.write(struct.pack("<3f", *v3))
            f.write(struct.pack("<H", 0))


def write_stl_ascii(path: Path, tris, name="sabu_approx"):
    lines = [f"solid {name}"]
    for v1, v2, v3 in tris:
        n = vnorm(vcross(vsub(v2, v1), vsub(v3, v1)))
        lines.append(f"  facet normal {n[0]:.6e} {n[1]:.6e} {n[2]:.6e}")
        lines.append("    outer loop")
        for v in (v1, v2, v3):
            lines.append(f"      vertex {v[0]:.6e} {v[1]:.6e} {v[2]:.6e}")
        lines.append("    endloop")
        lines.append("  endfacet")
    lines.append(f"endsolid {name}")
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def in_kidney(r, ang_deg, d):
    a = ang_deg % 360.0
    R = d["R"]
    for center in (0.0, 120.0, 240.0):
        da = (a - center + 180.0) % 360.0 - 180.0
        if abs(da) > d["OPEN_HALF"] * 1.05:
            continue
        r_mid = 0.52 * (d["OPEN_R0"] + d["OPEN_R1"])
        half_w = d["OPEN_HALF"] * (
            0.55 + 0.45 * math.exp(-(((r - r_mid) / (0.22 * R)) ** 2))
        )
        if abs(da) <= half_w and d["OPEN_R0"] * 0.92 <= r <= d["OPEN_R1"] * 1.02:
            return True
    return False


def spoke_height(r, ang_deg, d):
    a = ang_deg % 360.0
    dmin = min(abs((a - c + 180.0) % 360.0 - 180.0) for c in (60.0, 180.0, 300.0))
    if dmin > 50.0:
        return d["RIM_H"] if r > d["R"] - d["WALL"] else d["FLOOR"]
    u = max(0.0, min(1.0, (r - d["HOLE"] * 0.6) / (d["R"] - d["HOLE"] * 0.6)))
    peak = d["FLOOR"] + (d["H"] * 0.55) * math.sin(math.pi * u)
    w = max(0.0, 1.0 - dmin / 50.0) ** 2
    h = d["FLOOR"] + (peak - d["FLOOR"]) * w
    if r > d["R"] - d["WALL"]:
        h = max(h, d["RIM_H"])
    return min(h, d["H"] * 0.95)


def hub_tris(d, Nh=48):
    tris = []
    hub_r = d["HUB_OD"] / 2
    hole_r = d["HOLE"] / 2
    hub_h = d["H"] * 0.92
    for j in range(Nh):
        a0 = 2 * math.pi * j / Nh
        a1 = 2 * math.pi * (j + 1) / Nh
        for rad, invert in ((hub_r, False), (hole_r, True)):
            x0, y0 = rad * math.cos(a0), rad * math.sin(a0)
            x1, y1 = rad * math.cos(a1), rad * math.sin(a1)
            if invert:
                tris.append(((x0, y0, 0.0), (x0, y0, hub_h), (x1, y1, hub_h)))
                tris.append(((x0, y0, 0.0), (x1, y1, hub_h), (x1, y1, 0.0)))
            else:
                tris.append(((x0, y0, 0.0), (x1, y1, 0.0), (x1, y1, hub_h)))
                tris.append(((x0, y0, 0.0), (x1, y1, hub_h), (x0, y0, hub_h)))
        x0o, y0o = hub_r * math.cos(a0), hub_r * math.sin(a0)
        x1o, y1o = hub_r * math.cos(a1), hub_r * math.sin(a1)
        x0i, y0i = hole_r * math.cos(a0), hole_r * math.sin(a0)
        x1i, y1i = hole_r * math.cos(a1), hole_r * math.sin(a1)
        tris.append(((x0o, y0o, hub_h), (x1o, y1o, hub_h), (x1i, y1i, hub_h)))
        tris.append(((x0o, y0o, hub_h), (x1i, y1i, hub_h), (x0i, y0i, hub_h)))
    return tris


def build_sabu(d, n_th=96, n_r=28):
    tris = []
    rs = [d["HOLE"] * 0.5 + (d["R"] - d["HOLE"] * 0.5) * i / (n_r - 1) for i in range(n_r)]
    ths = [360.0 * j / n_th for j in range(n_th)]
    top, bot = {}, {}
    for i, r in enumerate(rs):
        for j, th in enumerate(ths):
            if in_kidney(r, th, d):
                continue
            x = r * math.cos(math.radians(th))
            y = r * math.sin(math.radians(th))
            top[(i, j)] = (x, y, spoke_height(r, th, d))
            bot[(i, j)] = (x, y, 0.0)
    for i in range(n_r - 1):
        for j in range(n_th):
            j2 = (j + 1) % n_th
            keys = [(i, j), (i, j2), (i + 1, j2), (i + 1, j)]
            if all(k in top for k in keys):
                a, b, c, e = (top[k] for k in keys)
                tris.append((a, b, c))
                tris.append((a, c, e))
                a, b, c, e = (bot[k] for k in keys)
                tris.append((a, e, c))
                tris.append((a, c, b))
    for j in range(n_th):
        j2 = (j + 1) % n_th
        r = d["R"]
        th, th2 = ths[j], ths[j2]
        x = r * math.cos(math.radians(th))
        y = r * math.sin(math.radians(th))
        x2 = r * math.cos(math.radians(th2))
        y2 = r * math.sin(math.radians(th2))
        z = spoke_height(r, th, d)
        z2 = spoke_height(r, th2, d)
        tris.append(((x, y, 0.0), (x2, y2, 0.0), (x2, y2, z2)))
        tris.append(((x, y, 0.0), (x2, y2, z2), (x, y, z)))
    tris.extend(hub_tris(d))
    return tris


def build_null(d, n_th=64, n_r=20):
    tris = []
    rs = [d["HOLE"] * 0.5 + (d["R"] - d["HOLE"] * 0.5) * i / (n_r - 1) for i in range(n_r)]
    ths = [360.0 * j / n_th for j in range(n_th)]
    top, bot = {}, {}
    for i, r in enumerate(rs):
        for j, th in enumerate(ths):
            x = r * math.cos(math.radians(th))
            y = r * math.sin(math.radians(th))
            z = d["RIM_H"] if r > d["R"] - d["WALL"] else d["FLOOR"]
            top[(i, j)] = (x, y, z)
            bot[(i, j)] = (x, y, 0.0)
    for i in range(n_r - 1):
        for j in range(n_th):
            j2 = (j + 1) % n_th
            keys = [(i, j), (i, j2), (i + 1, j2), (i + 1, j)]
            a, b, c, e = (top[k] for k in keys)
            tris.append((a, b, c))
            tris.append((a, c, e))
            a, b, c, e = (bot[k] for k in keys)
            tris.append((a, e, c))
            tris.append((a, c, b))
    for j in range(n_th):
        j2 = (j + 1) % n_th
        r = d["R"]
        th, th2 = ths[j], ths[j2]
        x = r * math.cos(math.radians(th))
        y = r * math.sin(math.radians(th))
        x2 = r * math.cos(math.radians(th2))
        y2 = r * math.sin(math.radians(th2))
        tris.append(((x, y, 0.0), (x2, y2, 0.0), (x2, y2, d["RIM_H"])))
        tris.append(((x, y, 0.0), (x2, y2, d["RIM_H"]), (x, y, d["RIM_H"])))
    tris.extend(hub_tris(d))
    return tris


def main():
    ap = argparse.ArgumentParser(description="Export approximate Sabu + null twin STLs")
    ap.add_argument("--scale", type=float, default=0.25, help="1.0 = full 61 cm; 0.25 ≈ 152.5 mm")
    ap.add_argument("--out", type=str, default="STL", help="output directory")
    ap.add_argument("--ascii", action="store_true", help="write ASCII STL instead of binary")
    args = ap.parse_args()

    d = dims(args.scale)
    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)
    tag = f"scale{str(args.scale).replace('.', 'p')}"
    # friendly 1:4 name when scale is 0.25
    if abs(args.scale - 0.25) < 1e-9:
        sabu_name = "sabu_approx_1to4.stl"
        null_name = "null_twin_1to4.stl"
    else:
        sabu_name = f"sabu_approx_{tag}.stl"
        null_name = f"null_twin_{tag}.stl"

    sabu = build_sabu(d)
    null = build_null(d)
    p1 = out / sabu_name
    p2 = out / null_name
    if args.ascii:
        write_stl_ascii(p1, sabu, "sabu_approx")
        write_stl_ascii(p2, null, "null_twin")
    else:
        write_stl_binary(p1, sabu)
        write_stl_binary(p2, null)
    print(f"Wrote {p1} ({len(sabu)} tris)  D={d['D']:.1f} mm")
    print(f"Wrote {p2} ({len(null)} tris)")
    print("Approximate geometry only — not JE 71295 scan. See docs/REPLICA.md.")


if __name__ == "__main__":
    main()
