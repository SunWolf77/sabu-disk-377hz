#!/usr/bin/env python3
"""
buga_piv_simulation.py — SIMULATION / teaching only

Synthetic 3-fold quiver field with a 377 Hz radial modulation.
NOT laboratory PIV of any physical sphere.

Extension study only — not part of the Sabu Mode A null-test path.
"""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "data" / "buga_sphere"
OUT.mkdir(parents=True, exist_ok=True)

x = np.linspace(-1.0, 1.0, 30)
y = np.linspace(-1.0, 1.0, 30)
X, Y = np.meshgrid(x, y)
theta = np.arctan2(Y, X)
r = np.sqrt(X**2 + Y**2) + 1e-9

# Decorative radial factor (not a measured mode)
freq_factor = np.sin(2 * np.pi * 0.15 * r * 377 / 377.0)
u = np.sin(3 * theta) * freq_factor - 0.25 * X / r
v = np.cos(3 * theta) * freq_factor - 0.25 * Y / r

fig, ax = plt.subplots(figsize=(7, 7))
ax.quiver(X, Y, u, v, scale=28, color="steelblue", alpha=0.85)
ax.set_aspect("equal")
ax.set_title("SIM — Buga extension: synthetic 3-fold flow sketch (not lab PIV)")
ax.set_xlabel("X (arb.)")
ax.set_ylabel("Y (arb.)")
ax.grid(True, alpha=0.25)
fig.tight_layout()
png_path = OUT / "sim_buga_piv_simulation.png"
fig.savefig(png_path, dpi=120)
plt.close(fig)

print(f"SIM PNG → {png_path.relative_to(ROOT)}")
print("Teaching sketch only.")
