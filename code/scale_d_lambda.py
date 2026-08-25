#!/usr/bin/env python3
"""Match electrical size d/λ — never raw hertz across media.

377 Hz acoustic is not 377 MHz microwave. If you parallel the Möbius
cavity (Paterson et al.) with an acoustic object, hold d/λ fixed.

Teaching sizes from that paper (aluminium D3 ring):
  vertex v ≈ 19.92 mm, mean radius R ≈ 23.67 mm
"""
from __future__ import annotations

import argparse
import math

C0 = 299_792_458.0
V_AIR = 343.0
V_PAPER_MM = 19.92e-3
R_PAPER_MM = 23.67e-3


def wavelength(f_hz: float, speed: float) -> float:
    return speed / f_hz


def d_over_lambda(d: float, f_hz: float, speed: float) -> float:
    return d / wavelength(f_hz, speed)


def freq_for_ratio(d: float, ratio: float, speed: float) -> float:
    return ratio * speed / d


def main() -> None:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--f-mw", type=float, default=3.77e9, help="microwave Hz")
    p.add_argument("--d-mw", type=float, default=R_PAPER_MM, help="microwave length (m)")
    p.add_argument("--d-ac", type=float, default=0.61, help="acoustic length (m), default museum Ø")
    p.add_argument("--c-ac", type=float, default=V_AIR)
    args = p.parse_args()

    ratio = d_over_lambda(args.d_mw, args.f_mw, C0)
    f_ac = freq_for_ratio(args.d_ac, ratio, args.c_ac)
    print(f"microwave  d={args.d_mw:.4e} m  f={args.f_mw:.4e} Hz  d/λ={ratio:.6f}")
    print(f"acoustic   d={args.d_ac:.4e} m  f={f_ac:.4e} Hz  (same d/λ, c={args.c_ac} m/s)")
    print("do not drive a 61 cm print at 377 Hz and call it the Möbius microwave point")


if __name__ == "__main__":
    main()
