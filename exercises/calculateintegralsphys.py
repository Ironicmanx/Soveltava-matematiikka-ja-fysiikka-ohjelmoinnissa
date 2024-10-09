import numpy as np


#kappaleen lämpötila alussa T(0) =Io
#tutkitaan kappaleen lämpötilaa ajan funktiona
#empirinen tulos: kappaleen lämpötilan muutosnopeus on verrannollinen lämpötiluettoon T-T

#dT/dt = -k(T-To)
# T pienenee ajan funktiona eksponentiaalisesti

#tutkitaan ratkaisua 
#kun t = 00 => T = Ty + (To - Ty)e^(-kt)

import matplotlib.pyplot as plt

def calculate_temperature(T0, Ty, k, time):
    """
    Calculate the temperature of an object over time based on the cooling law.
    
    Parameters:
    T0 (float): Initial temperature of the object in celsius.
    Ty (float): Ambient temperature in celsius.
    k (float): Cooling constant.
    time (numpy array): Array of time points.
    
    Returns:
    numpy array: Temperature of the object at each time point.
    """
    return Ty + (T0 - Ty) * np.exp(-k * time) #T = Ty + (To - Ty)e^(-kt)

# Constants
time = np.linspace(0, 100, 500)  # Time array

# Initial conditions for different objects
initial_conditions = [
    {'T0': 100, 'Ty': 20, 'k': 0.1, 'label': 'Object 1'},
    {'T0': 150, 'Ty': 25, 'k': 0.05, 'label': 'Object 2'},
    {'T0': 200, 'Ty': 30, 'k': 0.2, 'label': 'Object 3'}
]

# Plotting the results for each object
for conditions in initial_conditions:
    T = calculate_temperature(conditions['T0'], conditions['Ty'], conditions['k'], time)
    plt.plot(time, T, label=conditions['label'])

plt.xlabel('Time')
plt.ylabel('Temperature (Celsius)')
plt.title('Cooling of Objects Over Time')
plt.legend()
plt.grid(True)
plt.show()

#kuin huomataan, kappaleen lämpötila laskee ajan funktiona eksponentiaalisesti
# tarkalleen ottaen, kappaleen lämpötila on yhtä suuri kuin ympäristön lämpötila kun t -> oo