"""Zadanie 4 – Znajdź maksimum ręcznie
Masz listę wyników testów: [78, 92, 65, 88, 95, 71, 85] . Znajdź maksymalny wynik
używając pętli for (bez funkcji max() ).
Wymagania:
Inicjuj maksimum = wyniki[0]
W pętli porównuj: if wynik > maksimum:
Aktualizuj maksimum gdy znajdziesz większą wartość
Oczekiwany rezultat:
Maksymalny wynik: 95"""

results = [78, 92, 65, 88, 95, 71, 85]

maksimum = results[0]

for i in results:
    if i > maksimum:
        maksimum = i

print(f'Maksymalny wynik:', maksimum)