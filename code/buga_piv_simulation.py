import numpy as np
import matplotlib.pyplot as plt

# Grid setup
x = np.linspace(-1, 1, 30)
y = np.linspace(-1, 1, 30)
X, Y = np.meshgrid(x, y)
theta = np.arctan2(Y, X)
r = np.sqrt(X**2 + Y**2)

# Frequency factor (377 Hz resonance)
freq_factor = np.sin(2 * np.pi * 377 * r)

# Toroidal component (3 spirals)
u_tri = np.sin(3 * theta) * freq_factor
v_tri = np.cos(3 * theta) * freq_factor

# Tetrahedral stabilizers (4 anchors)
u_tet = -0.4 * (X**2 - Y**2) / (r**2 + 1e-6) * freq_factor
v_tet = -0.4 * X * Y / (r**2 + 1e-6) * freq_factor

# Combine components
u = u_tri + u_tet - 0.4 * X / (r + 1e-6)
v = v_tri + v_tet - 0.4 * Y / (r + 1e-6)

# Mask central hub
mask = r < 0.15
u[mask] = 0
v[mask] = 0

# Plot vector field
plt.figure(figsize=(8, 8))
plt.quiver(X, Y, u, v, scale=25)
plt.title("Buga Sphere PIV Simulation at 377 Hz (3 Spirals + 4 Anchors)")
plt.xlabel("X")
plt.ylabel("Y")
plt.grid()
plt.savefig("../data/buga_sphere/buga_piv_simulation.png")
