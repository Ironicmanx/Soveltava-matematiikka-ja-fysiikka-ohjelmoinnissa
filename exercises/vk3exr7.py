


""" Kuvassa 1 on esitetty funktion kuvaaja. Määrittele kuvan perusteella kyseinen funktio. Piirrä määrittelemäsi funktion
kuvaaja Pythonilla käyttäen Matplotlib-kirjastoa. Vertaa piirtämääsi kuvaajaa ja kuvaa 1."""

#oletetaan, että funktio f(t) = A*sin(w*t + vaihe)
#kun t=0 niin f(t) = 0 => A*sin(vaihe) = 0 => vaihe = 0

#incomplete

import numpy as np
import matplotlib.pyplot as plt
import math



def funktio(t):
    A = 3
    w = 2
    vaihe = 0
    return A * math.sin(w*t + vaihe)

def laske():
    aika = 5 * t 
    t = aika/5 
    print(f"aika = {t}")

    


def main():
    funktio(0)
    laske()
    t = np.linspace(0, 2, 1000)
    f = [funktio(i) for i in t]
    plt.plot(t, f)
    plt.xlabel('aika (s)')
    plt.ylabel('f(t)')
    plt.title('siniaalto')
    plt.grid(True)
    plt.show()
    return

