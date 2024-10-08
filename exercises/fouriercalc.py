
import numpy as np
import matplotlib.pyplot as plt
# import fourier 

# signal body and noise
d_t = 0.01
t = np.arange(0, 1, d_t)
f = 1  # Frequency in Hz
A = 1  # Amplitude
noisy_signal = A * np.sin(2 * np.pi * f * t) + np.random.normal(0, 0.5, len(t))

# Plot the noisy signal


# Create a time vector from 0 to 1 with a step size of 0.01
f = noisy_signal - np.mean(noisy_signal)
N = len(f)
fourier = np.fft.fft(f, N)
psd = fourier * np.conj(fourier) / N
freq = np.fft.fftfreq(N, d_t)
L = np.arange(1, np.floor(N / 2), dtype=int)

plt.figure(figsize=(10, 5))
plt.plot(freq[L], psd[L])
plt.plot(noisy_signal - np.mean(noisy_signal))
plt.xlabel('Frequency (Hz)')
plt.ylabel('Power Spectral Density')
plt.title('Power Spectral Density of Noisy Signal')
plt.title('Noisy Signal')
plt.legend(['Power Spectral Density', 'Noisy Signal'])
plt.show()


fourier_dom = fourier.copy()
fourier_dom[psd.real < 100] = 0
signal_filtered = np.fft.ifft(fourier_dom)