import numpy as np
import matplotlib.pyplot as plt

# Grid setup (2D projection)
x = np.linspace(-1, 1, 50)
y = np.linspace(-1, 1, 50)
X, Y = np.meshgrid(x, y)

# Polar coordinates
r = np.sqrt(X**2 + Y**2)
theta = np.arctan2(Y, X)

# Frequency pivot (377 Hz)
freq = 377
freq_factor = np.sin(2 * np.pi * freq * r)

# Spherical harmonic projection (simplified, 3-lobed toroidal overlay + radial stability)
u_theta = np.sin(3 * theta) * freq_factor
v_theta = np.cos(3 * theta) * freq_factor

# Add radial stabilizers (tetrahedral anchors)
u_radial = -0.3 * X / (r + 1e-6) * freq_factor
v_radial = -0.3 * Y / (r + 1e-6) * freq_factor

# Combine
u = u_theta + u_radial
v = v_theta + v_radial

# Mask center (avoid singularity)
mask = r < 0.1
u[mask] = 0
v[mask] = 0

# Quiver plot
plt.figure(figsize=(8, 8))
plt.quiver(X, Y, u, v, scale=40, color="black")
plt.title("Buga Sphere PIV Projection @ 377 Hz — Volumetric Harmonics")
plt.xlabel("X")
plt.ylabel("Y")
plt.grid()
plt.tight_layout()
plt.savefig("buga_piv_simulation.png")
