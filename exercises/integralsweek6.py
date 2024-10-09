import numpy as np
import matplotlib.pyplot as plt
import sympy as sp
from sympy.abc import x

"""
Ratkaise homogeeniset yhtälöt
a) y' + 7y = 0
b) y' + cos(x)y = 0
c) xy' + 3x^2 y = 0 alkuehdolla y(0) = 2
vektori = a2 * v2 + a1 * v1asd
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
    print(f"    jossa, Alkuehto y(0) = 2")

    """
    25. Ratkaise seuraavat ei-homogeeniset yhtälöt
    a) y' - 5y = 2
    b) y' + 2y = 5e^(-x) alkuehdolla y(0) = 1
    """
    def task_2():
        x = sp.symbols('x')
        y = sp.Function('y')
        
        # a) y' - 5y = 2
        sol1 = sp.dsolve(sp.Derivative(y(x), x) - 5 * y(x) - 2, y(x))  # no initial conditions
        print(f"lineaarinen rationaalinen differentiaaliyhtälö: y' - 5y = 2")
        print(f"a) Ratkaisu y' - 5y = 2 on: {sol1}")
    
        # b) y' + 2y = 5e^(-x) alkuehdolla y(0) = 1
        sol2 = sp.dsolve(sp.Derivative(y(x), x) + 2 * y(x) - 5 * sp.exp(-x), y(x), ics={y(0): 1})  # with initial conditions
        print(f"lineaarinen rationaalinen differentiaaliyhtälö: y' + 2y = 5e^(-x) alkuehdolla y(0) = 1")
        print(f"b) Ratkaisu y' + 2y = 5e^(-x) alkuehdolla y(0) = 1 on: {sol2}")
    
        return sol1, sol2
    
    def plot_solution(sol1, sol2):
        x_vals = np.linspace(-10, 10, 400)
        y1 = sp.lambdify(x, sol1.rhs, 'numpy')
        y2 = sp.lambdify(x, sol2.rhs, 'numpy')
    
        plt.plot(x_vals, y1(x_vals), label="y' - 5y = 2")
        plt.plot(x_vals, y2(x_vals), label="y' + 2y = 5e^(-x)")
    
        plt.grid()
        plt.title("Ratkaisut")
        plt.xlabel('x')
        plt.ylabel('y')
        plt.legend()
        plt.show()


if __name__ == "__main__":
        print(f"Integraalit ja differentiaaliyhtälöt")
        print(f"task 1")
        task_1()
        print(f"task 2")
        sol1, sol2 = task_2()
        plot_solution(sol1, sol2)