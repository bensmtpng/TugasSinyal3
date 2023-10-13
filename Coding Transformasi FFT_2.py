# -*- coding: utf-8 -*-
"""
Created on Fri Oct 13 21:45:31 2023

@author: Benny Simatupang
"""

import cmath

def fft(x):
    N = len(x)
    if N <= 1:
        return x
    even = fft(x[0::2])
    odd = fft(x[1::2])
    T = [cmath.exp(-2j * cmath.pi * k / N) * odd[k] for k in range(N // 2)]
    return [even[k] + T[k] for k in range(N // 2)] + [even[k] - T[k] for k in range(N // 2)]

def fft2d(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    # FFT per baris
    for i in range(rows):
        matrix[i] = fft(matrix[i])

    # FFT per kolom
    for j in range(cols):
        col = [matrix[i][j] for i in range(rows)]
        col = fft(col)
        for i in range(rows):
            matrix[i][j] = col[i]

    return matrix

# Contoh penggunaan
input_matrix = [
    [0, 1, 2, 3],
    [4, 5, 6, 7],
    [8, 9, 10, 11],
    [12, 13, 14, 15]
]

result = fft2d(input_matrix)

# Validasi menggunakan NumPy
import numpy as np

np_result = np.fft.fft2(input_matrix)

# Perbandingan hasil
print("Hasil Implementasi Sendiri:")
print(np.round(result, decimals=2))
print("\nHasil NumPy:")
print(np.round(np_result, decimals=2))