"""Zadanie 12 – Odległość Euklidesowa
Masz 2 punkty w przestrzeni 5-wymiarowej:
point_a = np.array([1, 2, 3, 4, 5])
point_b = np.array([5, 4, 3, 2, 1])
Oblicz odległość Euklidesową: sqrt(sum((a - b)^2))
Następnie oblicz macierz odległości dla 4 punktów:points = np.random.rand(4, 5)
Wymagania:
Ręczna implementacja (bez gotowych funkcji)
Wynik: macierz 4x4 odległości między każdą parą punktów"""

import numpy as np

point_a = np.array([1, 2, 3, 4, 5])
point_b = np.array([5, 4, 3, 2, 1])

print(f'punkt a: {point_a}')
print(f'punkt b: {point_b}')

result = np.sqrt(np.sum((point_a - point_b) ** 2, axis=0))
print(f'Odległość Euklidesowa w przestrzeni 5-wymiarowej: {result:.2f}')


points = np.random.rand(4, 5)

n = points.shape[0]
result_e = np.zeros([n,n])

for x in range(n):
    for y in range(n):
        odleglosc = points[x] - points[y]
        result_e[x,y] = np.round(np.sqrt(np.sum(odleglosc ** 2)), 2)

print(f'Macierz odległosci:\n{result_e}')