"""Zadanie 14 – Generowanie macierzy korelacji (uproszczona)
Masz dwie zmienne: wzrost = [165, 170, 175, 180, 185] i waga = [60, 65, 70,
75, 80] . Oblicz korelację Pearsona ręcznie używając pętli.
Dataset:
Dwie listy równoległe
Wymagania:
Oblicz średnie obu zmiennych
Oblicz sumy: Σ((xi - x̄ )(yi - ȳ)), Σ(xi - x̄ )², Σ(yi - ȳ)²
Korelacja r = Σ((xi - x̄ )(yi - ȳ)) / √(Σ(xi - x̄ )² × Σ(yi - ȳ)²)
Użyj zagnieżdżonych obliczeń w pętli
Oczekiwany rezultat:
Współczynnik korelacji r (oczekiwany: bliski 1.0 - silna korelacja dodatnia)"""

wzrost = [165, 170, 175, 180, 185]
waga = [60, 65, 70, 75, 80]

srednia_wzrost = sum(wzrost) / len(wzrost)
srednia_waga = sum(waga) / len(waga)

kwadraty_wzrost = 0
kwadraty_wagi = 0
iloczyn_roznic = 0

for i in range(len(wzrost)):
    kwadraty_wzrost += (wzrost[i] - srednia_wzrost) ** 2
    kwadraty_wagi += (waga[i] - srednia_waga) ** 2
    iloczyn_roznic += ((wzrost[i] - srednia_wzrost) * (waga[i] - srednia_waga))

r = iloczyn_roznic / ((kwadraty_wzrost * kwadraty_wagi) ** 0.5)
print(f'{r:.4f}')