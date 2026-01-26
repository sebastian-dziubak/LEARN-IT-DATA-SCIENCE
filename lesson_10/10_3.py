"""Zadanie 3 – Indeksowanie i slicing
Dana tablica 1D:
temps = np.array([15, 18, 22, 25, 23, 20, 17, 14, 16, 19, 21, 24])
Wykonaj:
Wypisz temperatury z dni parzystych (0, 2, 4, ...)
Wypisz ostatnie 5 temperatur
Wypisz temperatury w odwrotnej kolejności
Znajdź temperatury większe niż 20"""

import numpy as np

temps = np.array([15, 18, 22, 25, 23, 20, 17, 14, 16, 19, 21, 24])

print(f'''
Temperatury dni parzystych: {temps[::2]}
Ostatnie 5 wartości: {temps[-5]}
Odwrotna kolejność: {temps[::-1]}
Temperatury większe niz 20: {temps[temps > 20]}
''')