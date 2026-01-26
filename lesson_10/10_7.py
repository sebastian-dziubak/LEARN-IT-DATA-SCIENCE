"""Zadanie 7 – Tworzenie macierzy specjalnych
Utwórz następujące macierze:
Macierz 3x3 wypełnioną zerami
Macierz 4x4 wypełnioną jedynkami
Macierz identyczności 5x5
Macierz 3x4 wypełnioną liczbą 7
Wektor 10 równoodległych wartości od 0 do 1
Wymagania:
Użyj np.zeros , np.ones , np.eye , np.full , np.linspace"""

import numpy as np

# Macierz 3x3 wypełnioną zerami
print(np.zeros([3,3]))

# Macierz 4x4 wypełnioną jedynkami
print(np.ones([4, 4]))

# Macierz identyczności 5x5
print(np.eye(5))

# Macierz 3x4 wypełnioną liczbą 7
print(np.full((3, 4), 7))

# Wektor 10 równoodległych wartości od 0 do 1
print(np.linspace(0, 1, 10))