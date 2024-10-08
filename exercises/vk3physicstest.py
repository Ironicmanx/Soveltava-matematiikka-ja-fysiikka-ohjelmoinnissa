
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.signal import butter, filtfilt

"""
a) Tuo havaintodata Pythoniin ja piirrä sen kuvaaja.
b) Tutki, miten askelet näkyvät havainnoissa jaksollisena liikkeenä.
c) Määrittele, mikä kiihtyvyyden komponentti näyttää jaksollisuuden parhaiten ja valitse se seuraaviin kohtiin.
d)Määritä suodatus, jonka avulla voit poistaa valitusta kiihtyvyyden komponentista selvästi askeltaajuutta pienemmät
ja suuremmat taajuudet.
e) Laske askelten määrä suodatetusta datasta, voit esimerkiksi tutkia nollakohtien ylityksien, tai minimien ja maksimien määrää.
"""

def butter_lowpass_filter(data, cutoff, nyq, order): 
    normal_cutoff = cutoff / nyq
    # Get the filter coefficients
    b, a = butter(order, normal_cutoff, btype='low', analog=False)
    y = filtfilt(b, a, data)
    return y

# Read the data
data = pd.read_csv('exercises/vk1test/data/material/Acceleration without g 2024-09-15 17-38-32/Raw Data.csv')

# Filttereiden parametrit:
T = data['Time (s)'][len(data['Time (s)'])-1] - data['Time (s)'][0] # Koko datan pituus
n = len(data['Time (s)']) # Datapisteiden lukumäärä
fs = n/T # Näytteenottotaajuus (olettaen jotakuinkin vakioksi)
nyq = fs/2 # Nyqvistin taajuus
order = 3 # Kertaluku
cutoff = 1/(0.2) # Cutt-off taajuus

#filtteröidään data
filtered_signal = butter_lowpass_filter(data['Linear Acceleration y (m/s^2)'], cutoff, nyq, order)


# Lasketaan jaksojen määrä signaalissa (ja sitä kautta askelten määrä) laskemalla signaalin nollakohtien ylitysten määrä. 
# Nolla ylitetään kaksi kertaa jokaisen jakson aikana

jaksot = 0
for i in range(len(filtered_signal)-1):
    if filtered_signal[i] * filtered_signal[i+1] < 0:
        jaksot += 1

print('Askelmäärä on ', np.floor(jaksot/2))

# plotataan signaalit
plt.figure(figsize=(14,4))
plt.plot(data['Time (s)'], data['Linear Acceleration y (m/s^2)'], label='Original Signal')
plt.plot(data['Time (s)'], filtered_signal, label='Filtered Signal')
plt.xlabel('Predicted steps approximately: ' + str(np.floor(jaksot/2)))
plt.grid()
plt.axis([0,70,-3,3]) # kuvaajan skaalaus 70 sekunnin ajalle koska dataa yli 60 sekuntia
plt.legend()
plt.show()

