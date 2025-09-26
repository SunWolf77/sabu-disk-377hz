import numpy as np
import matplotlib.pyplot as plt

# Grid for volumetric projection
x = np.linspace(-1, 1, 30)
y = np.linspace(-1, 1, 30)
X, Y = np.meshgrid(x, y)
theta = np.arctan2(Y, X)
r = np.sqrt(X**2 + Y**2)

# Volumetric harmonics at 377 Hz
freq_factor = np.sin(2 * np.pi * 377 * r)
u = np.sin(3 * theta) * freq_factor - 0.3 * X / r
v = np.cos(3 * theta) * freq_factor - 0.3 * Y / r

# Quiver plot
plt.figure(figsize=(8, 8))
plt.quiver(X, Y, u, v, scale=25)
plt.title('Buga Sphere PIV Projection @ 377 Hz - Volumetric Harmonics')
plt.xlabel('X')
plt.ylabel('Y')
plt.grid()
plt.savefig('../data/buga_sphere/buga_piv_simulation.png')
plt.close()
print("PIV plot saved to ../data/buga_sphere/buga_piv_simulation.png")
