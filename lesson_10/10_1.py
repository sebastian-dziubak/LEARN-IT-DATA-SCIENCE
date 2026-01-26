"""Zadanie 1 – Tworzenie i analiza tablic
Utwórz tablicę NumPy zawierającą liczby od 1 do 100. Oblicz i wypisz:
Sumę wszystkich elementów
Średnią arytmetyczną
Medianę
Wartość maksymalną i minimalną
Wymagania:
Użyj np.arange() do stworzenia tablicy
Użyj funkcji agregujących NumPy ( np.sum , np.mean , etc.)"""

import numpy as np

numbers = np.arange(1, 101)

suma = np.sum(numbers)
srednia = np.mean(numbers)
mediana = np.mean(numbers)
w_max = np.max(numbers)
w_min = np.min(numbers)

print(f'''
Lista:\n{numbers}
\nSuma elementów: {suma}
Średnia: {srednia:.2f}
Mediana: {mediana:.2f}
Wartość max: {w_max}
Wartość min: {w_min}
''')