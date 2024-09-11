
"""
Mikä on siniaallon 3/2sin(7t-1)
a) amplitudi
b) kulmataajuus
c) vaihe
d) jaksonaika
"""

import numpy as np
import matplotlib.pyplot as plt

#g(t) = A*np.sin(w*t - vaihe)
#g(t) = 3/2*np.sin(7*t - 1)
print("g(t) = 3/2*sin(7t-1)")

# a) amplitudi
A = 3/2
print(f"Amplitudi: {A}")
# b) kulmataajuus
w = 7
print(f"Kulmataajuus: {w}")
# c) vaihe
vaihe = -1
print(f"Vaihe: {vaihe}")
# d) jaksonaika
T = 2*np.pi/w
print(f"Jaksonaika: {T}")

#piirretään kuvaaja
t = np.linspace(0, 2, 1000)
g = 3/2*np.sin(7*t - 1)
plt.plot(t, g)
plt.xlabel('aika (s)')
plt.ylabel('g(t)')
plt.title('siniaalto')
plt.grid(True)
plt.show()


