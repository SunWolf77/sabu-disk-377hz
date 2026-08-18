"""
SIMULATED PIV-style quiver — NOT a laboratory particle-image recording.

Teaching visualisation of a 3-fold + radial field. Do not cite as measured
flow over a physical Sabu replica.
"""

import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / "data" / "sabu_disk"
OUT.mkdir(parents=True, exist_ok=True)

x = np.linspace(-1, 1, 30)
y = np.linspace(-1, 1, 30)
X, Y = np.meshgrid(x, y)
theta = np.arctan2(Y, X)
r = np.sqrt(X**2 + Y**2) + 1e-6

# Decorative 3-fold field (not physics of schist in air)
u = np.sin(3 * theta) * np.exp(-r)
v = np.cos(3 * theta) * np.exp(-r)
mask = r < 0.12
u[mask] = 0
v[mask] = 0

plt.figure(figsize=(7, 7))
plt.quiver(X, Y, u, v, scale=30)
plt.title("SIMULATION — synthetic 3-fold quiver (not lab PIV)")
plt.xlabel("X (arb.)")
plt.ylabel("Y (arb.)")
plt.axis("equal")
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig(OUT / "sim_piv_quiver.png", dpi=150)
plt.close()
print(f"Simulated PIV plot -> {OUT / 'sim_piv_quiver.png'}")
