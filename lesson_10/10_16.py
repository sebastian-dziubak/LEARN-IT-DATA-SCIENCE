"""Zadanie 16 – Matrix multiplication (dot product)
Masz 2 macierze reprezentujące dane:
A = np.random.rand(100, 50)
B = np.random.rand(50, 20)
# 100 próbek, 50 cech
# 50 cech → 20 cech (transformacja)
Wymagania:
Wykonaj mnożenie macierzy: C = A @ B
Zmierz czas operacji
Porównaj z ręczną implementacją (3 zagnieżdżone pętle)
Wypisz przyspieszenie NumPyOczekiwany rezultat:
Macierz C (100, 20)
Porównanie czasów"""

import numpy as np
import time

A = np.random.rand(100, 50)
B = np.random.rand(50, 20)

print(f'Shape macierzy A: {A.shape}')
print(f'Shape macierzy B: {B.shape}')

start = time.time()
C = A@B
numpy_time = time.time() - start

print(f'Czas numpy: {numpy_time:.10f} sekund')
print(f'Shape macierzy C: {C.shape}')

C_python = np.zeros((100,20))

start = time.time()
for i in range(100):
    for j in range(20):
        suma = 0
        for k in range(50):
            suma += A[i, k] * B[k, j]
        C_python[i, j] = suma
czas_python = time.time() - start

print(f'Czas python: {czas_python:.10f} sekund')
print(f'Shape macierzy C: {C_python.shape}')

print(f'Czas numpy jest {czas_python / numpy_time:.0f} razy szybszy niż python')