import math
import numpy as np
import matplotlib.pyplot as plt


#Kirjoita sinifunktio, jonka amplitudio on 3, jaksoaika 4s ja vaihe pii
def sinifunktio(x):
    amplitude = 3
    period = 4
    phase = math.pi * x
    return amplitude * math.sin(2 * math.pi * x / period + phase)
    


def piirra_sinifunktio():
    x = np.linspace(0, 8, 1000)
    y = [sinifunktio(i) for i in x]
    plt.plot(x, y)
    plt.xlabel('aika (s)')
    plt.ylabel('g(t)')
    plt.title('siniaalto')
    plt.grid(True)
    plt.show()




def main():
    piirra_sinifunktio()
    for i in range(0, 9):
        print(f"sin({i}) = {sinifunktio(i)}")
    return