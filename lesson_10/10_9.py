"""Zadanie 9 – Normalizacja danych
Dataset: Oceny z 3 przedmiotów dla 20 studentów
scores = np.random.randint(40, 100, size=(20, 3))
Wymagania:
Zastosuj normalizację Min-Max per przedmiot (kolumna) → [0, 1]
Sprawdź, że min=0 i max=1 dla każdego przedmiotu
Wizualizuj rozkład przed i po normalizacji (histogramy)
Oczekiwany rezultat:
Tablica znormalizowana
2 histogramy (przed/po)"""

import numpy as np

import matplotlib.pyplot as plt

scores = np.random.randint(40, 100, size=(20, 3))
print(scores)

min_subject = np.min(scores, axis=0)
max_subject = np.max(scores, axis=0)

scores_normalized = (scores - min_subject) / (max_subject - min_subject)

print(f'minimum znormalizowane: {np.min(scores_normalized)}')
print(f'maksimum znormalizowane: {np.max(scores_normalized)}')

# Histogram scores (spłaszczamy macierz do 1D)
plt.figure()
plt.hist(scores.flatten(), bins=10)
plt.title("Histogram scores")
plt.xlabel("Wynik")
plt.ylabel("Częstość")
plt.show()

# Histogram scores_normalized (spłaszczamy macierz do 1D)
plt.figure()
plt.hist(scores_normalized.flatten(), bins=10)
plt.title("Histogram scores_normalized")
plt.xlabel("Wartość znormalizowana")
plt.ylabel("Częstość")
plt.show()