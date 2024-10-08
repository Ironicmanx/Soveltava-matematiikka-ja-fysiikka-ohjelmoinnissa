import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

"""
Ratkaise homogeeniset yhtälöt
a) y' + 7y = 0
b) y' + cos(x)y = 0
c) xy' + 3x^2 y = 0 alkuehdolla y(0) = 2
"""


def task_1():
    x = sp.symbols('x')
    y = sp.Function('y')
    y = sp.dsolve(sp.Derivative(y(x), x) + 7 * y(x), y(x))
    print(f"a) Ratkaisu y' + 7y = 0 on: {y}")

    y = sp.Function('y')
    y = sp.dsolve(sp.Derivative(y(x), x) + sp.cos(x) * y(x), y(x))
    print(f"b) Ratkaisu y' + cos(x)y = 0 on: {y}")

    y = sp.Function('y')
    y = sp.dsolve(x * sp.Derivative(y(x), x) + 3 * x**2 * y(x), y(x))
    print(f"c) Ratkaisu xy' + 3x^2 y = 0 on: {y}")
    print(f"jossa, Alkuehto y(0) = 2")


if __name__ == "__main__":
    task_1()
   