"""Zadanie 14 – Symulacja Monte Carlo
Oszacuj wartość π metodą Monte Carlo:
Generuj 1,000,000 losowych punktów (x, y) w kwadracie [-1, 1] x [-1, 1]
Zlicz ile punktów znajduje się w kole (x² + y² <= 1)
π ≈ 4 * (liczba w kole / liczba total)Wymagania:
Użyj np.random.rand() i operacji wektorowych
Bez pętli (tylko NumPy)
Wizualizuj pierwsze 10,000 punktów (kolor: w kole/poza kołem)
Oczekiwany rezultat:
Oszacowanie"""

import numpy as np
import matplotlib.pyplot as plt

n = 1000000

x = np.random.uniform(-1,1, n)
y = np.random.uniform(-1,1, n)

warunek = (x**2 + y**2) <= 1
w_kole = np.sum(warunek)

pi_oszacowane = 4 * w_kole / n
print(f'PI obliczone: {pi_oszacowane:.8f}')
print(f'PI z numpy {np.pi:.8f}')

plt.figure(figsize=(6,6))
plt.scatter(x[:10000], y[:10000], c=warunek[:10000], s=1, cmap='coolwarm', alpha=0.6)
plt.gca().set_aspect('equal')
plt.title(f"Monte Carlo")
plt.show()