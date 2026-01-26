"""Zadanie 8 – Reshape i flatten
Dana tablica:
arr = np.arange(1, 13)Wykonaj:
Zmień kształt na (3, 4)
Zmień kształt na (2, 6)
Zmień kształt na (4, 3)
Spłaszcz z powrotem do 1D (flatten lub ravel)
Wymagania:
Użyj metody .reshape()
Sprawdź różnicę między flatten() a ravel()"""

import numpy as np

arr = np.arange(1, 13)
print(arr)
print(arr.shape)

# Zmień kształt na (3, 4)
arr = arr.reshape(3, 4)
print(arr)
print(arr.shape)

# Zmień kształt na (2, 6)
arr = arr.reshape(2, 6)
print(arr)
print(arr.shape)

# Zmień kształt na (4, 3)
arr = arr.reshape(4, 3)
print(arr)
print(arr.shape)

# Spłaszcz z powrotem do 1D (flatten lub ravel)
arr = arr.ravel()
print(arr)
print(arr.shape)

