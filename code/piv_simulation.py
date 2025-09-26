import numpy as np
import matplotlib.pyplot as plt

# Grid setup
x = np.linspace(-1, 1, 30)
y = np.linspace(-1, 1, 30)
X, Y = np.meshgrid(x, y)
theta = np.arctan2(Y, X)
r = np.sqrt(X**2 + Y**2)

# Hybrid velocity at 377 Hz
freq_factor = np.sin(2 * np.pi * 377 * r)
u_tri = np.sin(3 * theta) * freq_factor
v_tri = np.cos(3 * theta) * freq_factor
u_tet = -0.5 * (X**2 - Y**2) / r**2 * freq_factor
v_tet = -X * Y / r**2 * freq_factor
u = u_tri + u_tet - 0.3 * X / r
v = v_tri + v_tet - 0.3 * Y / r

# Mask hub
mask = r < 0.15
u[mask] = 0
v[mask] = 0

# Quiver plot
plt.figure(figsize=(8, 8))
plt.quiver(X, Y, u, v, scale=25)
plt.title('Hybrid PIV Velocity Field: 120° Toroidal + 90° Tetrahedral at 377 Hz')
plt.xlabel('X')
plt.ylabel('Y')
plt.grid()
plt.savefig('../data/sabu_disk/piv_simulation.png')
plt.close()
print("PIV plot saved to ../data/sabu_disk/piv_simulation.png")
