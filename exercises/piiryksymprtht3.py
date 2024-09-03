import numpy as np
import matplotlib.pyplot as plt

# Piirrä yksikköympyrä ja esitä siinä seuraavat kulmat:
# a) 180°
plt.plot(np.cos(np.deg2rad(180)), np.sin(np.deg2rad(180)), 'ro', label='a) 180°')

# b) -270°
plt.plot(np.cos(np.deg2rad(-270)), np.sin(np.deg2rad(-270)), 'go', label='b) -270°')

# c) 765°
plt.plot(np.cos(np.deg2rad(765)), np.sin(np.deg2rad(765)), 'bo', label='c) 765°')

# d) 4/3π rad
plt.plot(np.cos(4/3*np.pi), np.sin(4/3*np.pi), 'yo', label='d) 4/3π rad')

# e) -5π rad
plt.plot(np.cos(-5*np.pi), np.sin(-5*np.pi), 'mo', label='e) -5π rad')

# f) π/2 rad
plt.plot(np.cos(np.pi/2), np.sin(np.pi/2), 'co', label='f) π/2 rad')

plt.axis('equal')
plt.legend()
plt.show()

# Piirrä ympyrä
theta = np.linspace(0, 2*np.pi, 100)
x = np.cos(theta)
y = np.sin(theta)
plt.plot(x, y, 'k-', label='Ympyrä')
