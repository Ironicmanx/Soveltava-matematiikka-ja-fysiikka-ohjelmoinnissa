import numpy as np
import matplotlib.pyplot as plt

# Funktio
def func(t):
    return 3 * np.cos(7 * t + 2)

# Aikaväli
t = np.linspace(0, 2 * np.pi, 1000)

# Funktioarvot
y = func(t)

# Amplitudi
amplitudi = 3

# Jaksonaika
kulmataajuus = 7
jaksoaika = 2 * np.pi / kulmataajuus

# Tulokset
print(f"Kysymys 1: Amplitudi = {amplitudi}")
print(f"Kysymys 3: Jaksoaika = {jaksoaika:.2f}")
print(f"Kysymys 4: Kulmataajuus = {kulmataajuus}")

# Kuvaajat
# Kysymys 1: Funktio ja amplitudi
plt.figure(figsize=(12, 6))

plt.subplot(1, 3, 1)
plt.plot(t, y, label='y = 3cos(7t + 2)')
plt.axhline(y=amplitudi, color='r', linestyle='--', label=f'Amplitudi = {amplitudi}')
plt.axhline(y=-amplitudi, color='r', linestyle='--')
plt.title('Kysymys 1: Amplitudi')
plt.xlabel('t')
plt.ylabel('y')
plt.legend()

# Kysymys 3: Jaksoaika
plt.subplot(1, 3, 2)
plt.plot(t, y, label='y = 3cos(7t + 2)')
plt.title('Kysymys 3: Jaksoaika')
plt.xlabel('t')
plt.ylabel('y')
plt.axvline(x=0, color='r', linestyle='--')
plt.axvline(x=jaksoaika, color='r', linestyle='--', label=f'Jaksoaika ≈ {jaksoaika:.2f}')
plt.legend()

# Kysymys 4: Kulmataajuus
plt.subplot(1, 3, 3)
plt.plot(t, y, label='y = 3cos(7t + 2)')
plt.title('Kysymys 4: Kulmataajuus')
plt.xlabel('t')
plt.ylabel('y')
plt.axvline(x=0, color='r', linestyle='--', label=f'Kulmataajuus = {kulmataajuus}')

plt.tight_layout()
plt.show()
