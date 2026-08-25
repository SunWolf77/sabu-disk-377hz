#!/usr/bin/env python3
"""Teaching stub — Pancharatnam / Wilson holonomy extractor.

Not FEM. Not microphone data. Not a four-cell result.

Interface this file is waiting for:
  data/holonomy/cell_{Fp,Fm}_{Zp,Zm}/psi_k.npy   # occupied eigenfields, closed loop
Until those exist, this only:
  1) recovers Ω/2 on a spin-½ latitude (pipeline check)
  2) prints the pre-registered null: |γ| → 2π/3 in EVERY cell
     before any extra residual is discussed

Null (Paterson, Tobar, Goryachev, Bourhill, Phys. Rev. A 113, 04350 (2026);
arXiv:2506.07320): triangular Möbius TE1,0,n vs mirror twin → ±2π/3.
"""
from __future__ import annotations

import argparse
import math
from pathlib import Path

TWO_PI_OVER_3 = 2.0 * math.pi / 3.0
CELLS = ("F+Z+", "F+Z-", "F-Z+", "F-Z-")


def wrap_pi(g: float) -> float:
    x = g
    while x <= -math.pi:
        x += 2.0 * math.pi
    while x > math.pi:
        x -= 2.0 * math.pi
    return x


def spinor_plus(theta: float, phi: float):
    h = theta / 2.0
    s, c = math.sin(h), math.cos(h)
    return (c + 0j, s * complex(math.cos(phi), math.sin(phi)))


def overlap(u, v) -> complex:
    return u[0].conjugate() * v[0] + u[1].conjugate() * v[1]


def wilson_loop(states) -> float:
    w = 1 + 0j
    n = len(states)
    for k in range(n):
        o = overlap(states[k], states[(k + 1) % n])
        mag = abs(o)
        w *= o / mag if mag > 1e-14 else 1
    return math.atan2(w.imag, w.real)


def latitude_check(theta_deg: float = 70.0, n: int = 48) -> dict:
    th = math.radians(theta_deg)
    states = [spinor_plus(th, 2 * math.pi * k / n) for k in range(n)]
    gamma = wilson_loop(states)
    expected = math.pi * (1.0 - math.cos(th))
    return {
        "gamma": gamma,
        "expected": expected,
        "residual": wrap_pi(gamma - expected),
    }


def preregister_cells() -> list[dict]:
    """Baseline every 2×2 cell must recover before extra residual is claimed."""
    rows = []
    for cell in CELLS:
        rows.append(
            {
                "cell": cell,
                "null_rad": TWO_PI_OVER_3,
                "null_label": "±2π/3",
                "status": "NOT RUN — no eigenfield dump",
            }
        )
    return rows


def main() -> None:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--theta", type=float, default=70.0)
    p.add_argument("--n", type=int, default=48)
    p.add_argument("--dump-dir", type=Path, default=None)
    args = p.parse_args()

    chk = latitude_check(args.theta, args.n)
    print("pipeline check (spin-1/2 latitude, Pancharatnam)")
    print(f"  γ        {chk['gamma']:+.6f} rad")
    print(f"  π(1-cosθ) {chk['expected']:+.6f} rad")
    print(f"  residual {chk['residual']:+.6f} rad")
    print()
    print("pre-registered 2×2 null (Paterson et al. PRA 2026)")
    for row in preregister_cells():
        print(f"  {row['cell']:6}  expect {row['null_label']:8}  {row['status']}")
    if args.dump_dir:
        print(f"\nno FEM dumps at {args.dump_dir} — place psi_k.npy per cell to extract")


if __name__ == "__main__":
    main()
