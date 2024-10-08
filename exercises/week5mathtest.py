
import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

def task_1():
    # Tehtävä 1: Differentiaaliyhtälön y' = 2x^3 yleinen ratkaisu
    x, C = sp.symbols('x C')
    y = (1/2) * x**4 + C
    print(f"Yleinen ratkaisu y' = 2x^3 on: y = {y}")

    # Piirrä kuvaaja
    plot_solution(y)

def task_2():
    # Tehtävä 2: Separoituvat yhtälöt
    equations = [
        "y' = -3yx",
        "2y' = 3x - y + 4",
        "y' = 2x + 6xy",
        "y' = -x^2/(3y)"
    ]
    
    separable = [
        equations[0],  # y' = -3yx
        equations[3]   # y' = -x^2/(3y)
    ]
    
    print("Separoituvat yhtälöt:")
    for eq in separable:
        print(f" - {eq}")

def task_3():
    # Tehtävä 3: Differentiaaliyhtälön y'' + 3y^4 - 2x + 16 = 0 kertaluku
    print("Tehtävä 3: Differentiaaliyhtälön kertaluku on 2.")

def task_4():
    # Tehtävä 4: Yksittäisratkaisu y = x^4 + C, C = 2, x = 2
    C = 2
    x_value = 2
    y_value = x_value**4 + C
    print(f"Yksittäisratkaisun y arvo, kun x = {x_value} on: {y_value}")

    # Piirrä kuvaaja
    plot_individual_solution(C)

def task_5():
    # Tehtävä 5: Määrittele C, joka toteuttaa yksittäisratkaisun (0,3)
    x_value = 0
    y_value = 3
    C = y_value - x_value**4  # C = y - x^4
    print(f"C:n arvo, joka toteuttaa yksittäisratkaisun, joka kulkee pisteen (0, 3) kautta, on: {C}")

def plot_solution(y):
    # Piirrä y = 0.5 * x^4 + C
    x_vals = np.linspace(-2, 2, 400)
    
    # Arvioi y-lauseke numeerisesti useilla C-arvoilla
    C_values = [0, 1, 2, 3]  # Esimerkki C-arvoista
    for C in C_values:
        y_func = sp.lambdify('x', y.subs('C', C), modules=['numpy'])
        y_vals = y_func(x_vals)
        plt.plot(x_vals, y_vals, label=f'y = 0.5 * x^4 + {C}')

    plt.title('Yleinen ratkaisu: y\' = 2x^3')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.axhline(0, color='black', lw=0.5, ls='--')
    plt.axvline(0, color='black', lw=0.5, ls='--')
    plt.grid()
    plt.legend()
    plt.show()

def plot_individual_solution(C):
    # Piirrä yksittäisratkaisu y = x^4 + C
    x_vals = np.linspace(-2, 2, 400)
    y_vals = x_vals**4 + C
    plt.plot(x_vals, y_vals, label=f'y = x^4 + {C}', color='red')
    plt.title('Yksittäisratkaisu: y = x^4 + C')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.axhline(0, color='black', lw=0.5, ls='--')
    plt.axvline(0, color='black', lw=0.5, ls='--')
    plt.grid()
    plt.legend()
    plt.show()

if __name__ == "__main__":
    task_1()
    task_2()
    task_3()
    task_4()
    task_5()
