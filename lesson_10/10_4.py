"""Zadanie 4 – Tablice 2D
Utwórz tablicę 2D (5x4) wypełnioną losowymi liczbami całkowitymi od 1 do 50.
Wymagania:
Użyj np.random.randint()
Wypisz shape tablicy
Wypisz drugi wiersz
Wypisz trzecią kolumnę
Wypisz element z pozycji (2, 3)"""

import numpy as np

matrix = np.random.randint(1, 50, size=(5,5))
print(matrix)

print(f'''
shape tablicy: {matrix.shape}
drugi wiersz: {matrix[1]}
trzecia kolumna: {matrix[:, 3]}
element z pozycji (2, 3): {matrix[2, 3]} 
''')