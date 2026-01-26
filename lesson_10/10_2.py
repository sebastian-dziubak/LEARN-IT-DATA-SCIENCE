"""Zadanie 2 – Operacje wektorowe
Masz dwie tablice reprezentujące ceny produktów przed i po rabacie:
before = np.array([100, 250, 75, 320, 180, 450, 90])
after = np.array([80, 200, 60, 280, 150, 400, 75])
Oblicz i wypisz:Różnicę między cenami (oszczędności)
Procent rabatu dla każdego produktu
Średnią oszczędność
Wymagania:
Użyj operacji wektorowych (bez pętli)
Wynik zaokrąglij do 2 miejsc po przecinku"""

import numpy as np

before = np.array([100, 250, 75, 320, 180, 450, 90])
after = np.array([80, 200, 60, 280, 150, 400, 75])

print('Ceny przed rabatem', before)
print('Ceny po rabacie', after)
print('Różnica między cenami', before - after)
print('Procent rabatu', np.round((before - after) / before * 100, 2))
print(f'Średnia oszczędność {np.mean(before - after):.2f}')