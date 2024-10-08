
# 14. Lataa Moodlesta tiedosto signal_to_be_cleaned.csv
# a) Määrittele Fourier-analyysin avulla kolme tehokkainta taajuutta ja suodata muut taajuudet pois.
# b) Mitkä ovat kolme tehokkainta taajuutta?
# c) Piirrä alkuperäisen signaalin ja suodatetun signaalin kuvaajat

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# Load the signal data from the CSV file
df = pd.read_csv('/home/arttu/Python files/FALL2024 | MATH AND PHYSICS/Soveltava-matematiikka-ja-fysiikka-ohjelmoinnissa/signal_sampling.csv')

# Assume the signal is sampled at 0.1 s intervals
dt = 0.1

# Extract the signal from the DataFrame

f = df['Signal'].values

N = len(f)
fourier = np.fft.fft(f, N)
psd = np.abs(fourier) ** 2 / N
freq = np.fft.fftfreq(N, dt)
L = np.arange(1, np.floor(N / 2), dtype=int)

# Find the indices of the three highest peaks in the power spectral density
indices = np.argsort(psd)[-3:]

# Get the corresponding frequencies
top_frequencies = freq[indices]

print("Three most powerful frequencies are:", top_frequencies)

# Filter out all frequencies except the three most powerful ones
filtered_fourier = np.zeros_like(fourier)
filtered_fourier[indices] = fourier[indices]
filtered_fourier[-indices] = fourier[-indices]  # Retain the negative frequency components

# Perform the inverse FFT to get the filtered signal
filtered_signal = np.fft.ifft(filtered_fourier)

# Plot the original and filtered signals
plt.figure(figsize=(12, 6))

plt.subplot(2, 1, 1)
plt.plot(f)
plt.title('Original Signal')

plt.plot(filtered_signal.real)  # Plot the real part of the filtered signal
plt.plot(filtered_signal)
plt.title('Filtered Signal')

plt.tight_layout()
plt.show()
