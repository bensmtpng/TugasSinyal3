# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 23:43:57 2023

@author: 62813
"""

import numpy as np
import cmath
import matplotlib.pyplot as plt

# Mendefinisikan parameter
A = 3  # Setengah panjang periode
T = 4 * A  # Panjang total sinyal
N = 1024  # Jumlah sampel
t = np.linspace(-T / 2, T / 2, N, endpoint=False)  # Sampel waktu

# Fungsi periodik
def f(t):
    if abs(t) <= A:
        return 1.0
    else:
        return 0.0

# Inisialisasi array FFT secara manual
F_manual = [0] * N

# Hitung FFT secara manual
for k in range(N):
    Fk = 0
    for j in range(N):
        Fk += f(t[j]) * cmath.exp(-2j * cmath.pi * k * j / N)
    F_manual[k] = Fk

# Hitung FFT menggunakan NumPy
F_numpy = np.fft.fft([f(tj) for tj in t])

# Validasi hasil
validation_result = np.allclose(F_manual, F_numpy, rtol=1e-10, atol=1e-10)
if validation_result:
    print("Hasil validasi: Hasil FFT manual dan NumPy mendekati atau sama.")
else:
    print("Hasil validasi: Hasil FFT manual dan NumPy tidak mendekati atau sama.")

# Hitung spektrum frekuensi
freqs = [k / T for k in range(N)]

# Plot sinyal asli
plt.figure(figsize=(10, 6))
plt.subplot(311)
plt.plot(t, [f(tj) for tj in t])
plt.title('Sinyal Asli')
plt.grid()

# Plot hasil manual
plt.subplot(312)
plt.plot(freqs, [abs(Fk) for Fk in F_manual])
plt.title('Spektrum Frekuensi (FFT Manual)')
plt.grid()

# Plot hasil NumPy
plt.subplot(313)
plt.plot(freqs, np.abs(F_numpy))
plt.title('Spektrum Frekuensi (FFT NumPy)')
plt.grid()

plt.tight_layout()
plt.show()
