import numpy as np

"""
• Kertaustehtävä 2
Funktio f(x) = x**3 + x**2 + 2*x - 4
a) Piirrä funktion kuvaaja välillä [-2,2]
b) Määrittele funktion derivaatta ja piirrä sen kuvaaja
c) Vertaa funktiota ja derivaattaa, miten ne käyttäytyvät toisiinsa nähden?
d) Määrittele funktion integraali
e) Laske määrätty integraali välillä [-2,2]
"""

import matplotlib.pyplot as plt

def f(x):
    return x**3 + x**2 + 2*x - 4

# a) Piirrä funktion kuvaaja välillä [-2,2]
x = np.linspace(-2, 2, 100)
y = f(x)

plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Function f(x)')
plt.grid(True)
plt.show()

# b) Määrittele funktion derivaatta ja piirrä sen kuvaaja
def f_derivative(x):
    return 3*x**2 + 2*x + 2

x = np.linspace(-2, 2, 100)
y_derivative = f_derivative(x)

plt.plot(x, y_derivative)
plt.xlabel('x')
plt.ylabel("f'(x)")
plt.title("Derivative of f(x)")
plt.grid(True)
plt.show()

# c) Vertaa funktiota ja derivaattaa, miten ne käyttäytyvät toisiinsa nähden?
x = np.linspace(-2, 2, 100)
y = f(x)
y_derivative = f_derivative(x)

plt.plot(x, y, label='f(x)')
plt.plot(x, y_derivative, label="f'(x)")
plt.xlabel('x')
plt.ylabel('y')
plt.title('Comparison of f(x) and f\'(x)')
plt.legend()
plt.grid(True)
plt.show()

# d) Määrittele funktion integraali
def f_integral(x):
    return (1/4)*x**4 + (1/3)*x**3 + x**2 - 4*x

# e) Laske määrätty integraali välillä [-2,2]
integral_result = f_integral(2) - f_integral(-2)
print("The definite integral of f(x) from -2 to 2 is:", integral_result)