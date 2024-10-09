
import numpy as np

import matplotlib.pyplot as plt


def pudotus_nopeus(m,k, t):

    g = 9.81
    v = m/k*g*(1-np.exp(-k*t/m))
    return v
    
# Formula for terminal velocity is v(terminal) = m/k * g where m is mass and k is drag coefficient (basically air d) and g is gravity constant (9.81 m/s^2)
# Calculate terminal velocities for the given parameters
terminal_velocity_1 = 5 / 1 * 9.81
terminal_velocity_2 = 5 / 1.2 * 9.81
terminal_velocity_3 = 10 / 1 * 9.81


#aika 
t = np.arange(0, 130, 0.01)

plt.plot(t, pudotus_nopeus(5, 1, t))
plt.plot(t, pudotus_nopeus(5, 1.2, t))
plt.plot(t, pudotus_nopeus(10, 1, t))
plt.xlabel('Time (s)')
plt.ylabel('Velocity (m/s)')
plt.title('Velocity vs Time')

# Plot horizontal lines for terminal velocities
plt.axhline(y=terminal_velocity_1, color='r', linestyle='--', label=f'Terminal Velocity 1: {terminal_velocity_1:.2f} m/s')
plt.axhline(y=terminal_velocity_2, color='g', linestyle='--', label=f'Terminal Velocity 2: {terminal_velocity_2:.2f} m/s')
plt.axhline(y=terminal_velocity_3, color='b', linestyle='--', label=f'Terminal Velocity 3: {terminal_velocity_3:.2f} m/s')

plt.title('Velocity vs Time with Different Terminal Velocities')
plt.legend()
plt.grid()
plt.show()