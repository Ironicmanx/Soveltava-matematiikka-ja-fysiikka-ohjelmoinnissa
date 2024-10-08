

# tehtävä 17
#FUNKTIO y on diffrentiaaliyhtälön ratkaisu, jos se toteuttaa yhtälön
# eli yhtälö on tosi jos y sijoitetaan sinne
#eli oikea puoli on yhtä suuri kuin vasen puoli

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


#tehtävä a)
#yhtälö y'  = x^2 
# => y = x^3 * 1/3
# lasketaan tästä y' = d/dx(x^3 * 1/3)
#  = 1/3 * 3* x^3-1 
# = x^2
#sijoitetaan tämä yhtälöön
# y' - x^2 = 0
# = x^2 - x^2 = 0
# TOSI
#<=> y = x^3 / 3 yhtälön y' = x^2 ratkaisu

def y(x):
    return (1/3) * x**3

def y_prime(x):
    return x**2

# Check if the differential equation holds
x_values = np.linspace(-10, 10, 400)
lhs = y_prime(x_values)
rhs = x_values**2

# Verify if lhs equals rhs
is_solution = np.allclose(lhs, rhs)
print("The function y(x) is a solution to the differential equation y' = x^2:", is_solution)

# b)
# yhtälö y' = x-y
# => y' + y -x = 0
#mahdollinen ratkaisu y = 2e^-x + x - 1
#lasketaan
# y' = d/dx(2e^ -x + x - 1)
# = -2e^-x *(-1) + 1 = 0
# = 2e^-x + 1
#sijoitetaan yhtälöön
# y' + y - x = 0
# (-2e^-x + 1) + (2e^-x + x - 1) - x = 0
#     y'                 y
#  = 0
#  toteuttaa yhtälön
# => ratkaisu toimii koska jakojaannos on 0

def y_b(x):
    return 2 * np.exp(-x) + x - 1

def y_b_prime(x):
    return -2 * np.exp(-x) + 1

# Check if the differential equation holds for part b
lhs_b = y_b_prime(x_values) + y_b(x_values)
rhs_b = x_values

# Verify if lhs_b equals rhs_b
is_solution_b = np.allclose(lhs_b, rhs_b)
print("The function y_b(x) is a solution to the differential equation y' = x - y:", is_solution_b)
# c)
# yhtälö y' = 3y + e^x
# mahdollinen ratkaisu y = e^3x - (e^x)/2
# lasketaan derivaatta
# y' = d/dx(e^3x - (e^x)/2)
# = (3e^3x) * 3 - (e^x)/2
# sijoitetan yhtälöön y' = 3y + e^x
# (3e^3x - (e^x)/2) - (3e^3x - (e^x)/2) = 0
# voidaan selventää yhtälöä
# 3e^3x - (e^x)/2 - 3e^3x + (e^x)/2 = 0
# = (-3e^x)/2 + (3e^x)/2 = 0
# periaatteessa 1  -  1 = 0
# eli
# tämäkin yhtälö on tosi koska jakojaannos on 0

def y_c(x):
    return np.exp(3 * x) - (np.exp(x) / 2)

def y_c_prime(x):
    return 3 * np.exp(3 * x) - (np.exp(x) / 2)

# Check if the differential equation holds for part c
lhs_c = y_c_prime(x_values)
rhs_c = 3 * y_c(x_values) + np.exp(x_values)

# Verify if lhs_c equals rhs_c
is_solution_c = np.allclose(lhs_c, rhs_c)
print("The function y_c(x) is a solution to the differential equation y' = 3y + e^x:", is_solution_c)

# kaikki ratkaisut toimivat tehtävässä 17
print("All solutions are correct:", is_solution and is_solution_b and is_solution_c)


# tehtävä 18
# yhtälö y' = 4x^2
# yleinen ratkaisu  y = 4/3 * x^3 + C
# mikä ratkaisu kulkee pisteen (-3, 30) kautta?
# sijoitetaan ratkaisuun
# => -30 = 4/3 * (-3)^3 + C
# sievennetään
# => -30 = 4/3 * -27 + C
# => -30 = -36 + C   | +36
# => C = 6

#ratkaisu y = 4/3 * x^3 + 6
# sievennettynä y = (4/3)x^3 + 6
# eli ratkaisu kulkee pisteen (-3, 30) kautta
# koska y(-3) = (4/3) * (-3)^3 + 6 = 4/3 * -27 + 6 = -36 + 6 = -30
# Define the particular solution


#x:n arvot
x = np.arange(-4, 4, 0.01)

def y(x, C):
    return 4/3 * x**3 + C

plt.plot(x,y(x,0))
plt.plot(x,y(x,2))
plt.plot(x,y(x,4))
plt.plot(x,y(x,6))
plt.grid()
plt.legend(['C=0', 'C=2', 'C=4', 'C=6'])
plt.axis([-3.5, -2.5, -60, -20])
plt.xlabel('x')
plt.ylabel('y')
plt.show()

# tehtävä 19
# yhtälö y' = (2xy)^2
#ratkaisu y = 3/C+4x^3
#MIKÄ RATKAISU KULKEE PISTEEN (1, -0.5) KAUTTA?
#sijoitetaan ratkaisuun
# => -0.5 = 3/C + 4*1^3
# => -0.5 = 3/C + 4 
# C + 4 = 2 * 3
# C = 2


def y_19(x, C):
    return 3 / (C + 4 * x**3)

# Given point (1, -0.5), find C
x_point = 1
y_point = -0.5
C = 3 / (y_point - 4 * x_point**3)

# x values for plotting
x_values_19 = np.linspace(-2, 2, 400)

# Plot the solution
plt.plot(x_values_19, y_19(x_values_19, C))
plt.grid()
plt.title("Solution to y' = (2xy)^2 passing through (1, -0.5)")
plt.xlabel('x')
plt.ylabel('y')
plt.show()

# tehtävä 20
# a)
# y' = 3x + e^x  <==> y = integral(3x + e^x)dx
# dy/dx = 3x + e^x | * dx
# integral(dy) = integral(3x + e^x)dx
# y + C = 3*x^2  * 1/2 + e^x + C
# y = 3/2 * x^2 + e^x + C

# Define the general solution
def y_20(x, C):
    return (3/2) * x**2 + np.exp(x) + C

# Given point (0, 1), find C
x_point_20 = 0
y_point_20 = 1
C_20 = y_point_20 - y_20(x_point_20, 0)

# x values for plotting
x_values_20 = np.linspace(-2, 2, 400)

# Plot the solution
plt.plot(x_values_20, y_20(x_values_20, C_20))
plt.grid()
plt.title("Solution to y' = 3x + e^x passing through (0, 1)")
plt.xlabel('x')
plt.ylabel('y')
plt.show()

# c)
# y' = sin(x)*e^cos(x)
# => dy/dx = sin(x)*e^cos(x) | * dx
# => integral(dy) = integral(sin(x)*e^cos(x))dx
# => y + C = -e^cos(x) + C
# y = -e^cos(x) + C

def y_20c(x, C):
    return -np.exp(np.cos(x)) + C

# Given point (0, 1), find C
x_point_20c = 0
y_point_20c = 1
C_20c = y_point_20c - y_20c(x_point_20c, 0)

# x values for plotting
x_values_20c = np.linspace(-2 * np.pi, 2 * np.pi, 400)

# Plot the solution
plt.plot(x_values_20c, y_20c(x_values_20c, C_20c))
plt.grid()
plt.title("Solution to y' = sin(x) * e^cos(x) passing through (0, 1)")
plt.xlabel('x')
plt.ylabel('y')
plt.show()

# f)
# yhtälö y' = y   (kertaluku 1)
# dy/dx = y | * dx 
# integral(dy)/y = integral(dx)      (separoitu)
# integral(1/y)dy = integral(1)dx
# ln(y) = x + C
# e^ln(y) = e^(x + C)
# y = (e^x + C)
# y = e^x * e^C
# y = c2 * e^x
# derivoiminen ei muuta yhtälöä

def y_20f(x, C):
    return C * np.exp(x)

# Given point (0, 1), find C
x_point_20f = 0
y_point_20f = 1
C_20f = y_point_20f / np.exp(x_point_20f)

# x values for plotting
x_values_20f = np.linspace(-2, 2, 400)

# Plot the solution
plt.plot(x_values_20f, y_20f(x_values_20f, C_20f))
plt.grid()
plt.title("Solution to y' = y passing through (0, 1)")
plt.xlabel('x')
plt.ylabel('y')
plt.show()

# g)
# y' = y/x   (kertaluku 1)
# dy/dx = y/x | * dx
# integral(dy)/y = integral(dx/x)
# integral(1/y)dy = integral(1/x)dx
# ln(y) = ln(x) + C  | e^
# e^ln(y) = e^(ln(x) + C)
# y = e^(ln(x)) * e^C
# y = x * e^C
#         C2
# y = C2x

def y_20g(x, C):
    return C * x

# Given point (1, 2), find C
x_point_20g = 1
y_point_20g = 2
C_20g = y_point_20g / x_point_20g

# x values for plotting
x_values_20g = np.linspace(-2, 2, 400)

# Plot the solution
plt.plot(x_values_20g, y_20g(x_values_20g, C_20g))
plt.grid()
plt.title("Solution to y' = y/x passing through (1, 2)")
plt.xlabel('x')
plt.ylabel('y')
plt.show()