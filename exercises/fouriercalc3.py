
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# import folium

# Path to the CSV file
path = '/home/arttu/Python files/FALL2024 | MATH AND PHYSICS/Soveltava-matematiikka-ja-fysiikka-ohjelmoinnissa/signal_sampling.csv'

# Read the data
df = pd.read_csv(path)

# Define time step and create time array
dt = 0.01
a = np.arange(0, 100, dt)

# Generate a synthetic signal (for demonstration)
f = np.sin(4*a) + np.sin(6*a-1) + np.random.randn(len(a))

# Perform Fourier Transform
N = len(f)
fourier = np.fft.fft(f, N)

# Calculate Power Spectral Density (PSD) and frequency array
psd = fourier * np.conj(fourier) / N
freq = np.fft.fftfreq(N, dt)

# Apply low-pass filter
cutoff = 50  # Cutoff frequency in Hz
fourier_filtered = fourier.copy()
fourier_filtered[np.abs(freq) > cutoff] = 0

# Perform Inverse Fourier Transform to get the filtered signal
suodatettu_signaali = np.fft.ifft(fourier_filtered)

# Ensure the filtered signal is real
suodatettu_signaali = np.real(suodatettu_signaali)

# Plot the original noisy signal and the filtered signal
plt.plot(a, f, label='Noisy Signal')
plt.plot(a, suodatettu_signaali, label='Filtered Signal')
plt.xlabel('Time (s)')
plt.ylabel('Signal')
plt.title('Noisy Signal vs Filtered Signal')
plt.legend()
plt.axis([0, 25, -12.5, 12.5])
plt.show()