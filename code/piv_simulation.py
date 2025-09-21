import numpy as np
import matplotlib.pyplot as plt

# Grid
x = np.linspace(-1, 1, 30)
y = np.linspace(-1, 1, 30)
X, Y = np.meshgrid(x, y)

# Polar
theta = np.arctan2(Y, X)
r = np.sqrt(X**2 + Y**2)

# Hybrid velocity: 120° toroidal + 90° tetrahedral @ 377 Hz
freq_factor = np.sin(2 * np.pi * 377 * r)
u_tri = np.sin(3 * theta) * freq_factor
v_tri = np.cos(3 * theta) * freq_factor
u_tet = -0.4 * (X**2 - Y**2) / (r**2 + 1e-6) * freq_factor
v_tet = -0.4 * X * Y / (r**2 + 1e-6) * freq_factor

# Combine
u = u_tri + u_tet - 0.4 * X / (r + 1e-6)
v = v_tri + v_tet - 0.4 * Y / (r + 1e-6)

# Mask hub
mask = r < 0.15
u[mask] = 0
v[mask] = 0

# Quiver plot
plt.figure(figsize=(8, 8))
plt.quiver(X, Y, u, v, scale=25)
plt.title('Hybrid PIV Velocity Field: 120° + 90° at 377 Hz')
plt.xlabel('X')
plt.ylabel('Y')
plt.grid()
plt.show()