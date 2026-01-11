'''Zadanie 19 – Pipeline z funkcjami: czyszczenie → transformacja → agregacja
Stwórz kompletny pipeline analizy danych klientów: czyszczenie outlierów → normalizacja
→ segmentacja.
Dataset:
klienci = [
{"id": 1, "wiek": 25, "dochod": 4500, "wydatki": 3200},
{"id": 2, "wiek": 200, "dochod": 7800, "wydatki": 5100},
wiek
{"id": 3, "wiek": 45, "dochod": 9200, "wydatki": -500},
wydatki
# ... więcej danych
]
# outlier
# outlier
Wymagania:
Funkcja usun_outliery() - usuwa rekordy z błędnymi wartościami
Funkcja normalizuj_kolumny() - normalizacja min-max dla wieku/dochodu
Funkcja segmentuj() - przypisuje klientów do segmentów (niski/średni/wysoki) według
dochodu
Użyj comprehensions i lambda w pipeline
Oczekiwany rezultat:
Czyste dane z segmentami i znormalizowanymi wartościami'''
from os import close

klienci = [
    {"id": 1, "wiek": 25, "dochod": 4500, "wydatki": 3200},
    {"id": 2, "wiek": 200, "dochod": 7800, "wydatki": 5100},
    {"id": 3, "wiek": 45, "dochod": 9200, "wydatki": -500},
    {"id": 4, "wiek": 32, "dochod": 8100, "wydatki": 5600},
    {"id": 5, "wiek": 28, "dochod": 4900, "wydatki": 3000},
    {"id": 6, "wiek": 300, "dochod": 800, "wydatki": 100},
    {"id": 7, "wiek": 55, "dochod": 200, "wydatki": 2700},
    {"id": 8, "wiek": 41, "dochod": 92000, "wydatki": 3600},
    {"id": 9, "wiek": 89, "dochod": 4800, "wydatki": 3300},
    {"id": 10, "wiek": 18, "dochod": 6800, "wydatki": 9100},
    {"id": 11, "wiek": 12, "dochod": 5200, "wydatki": 500},
    {"id": 12, "wiek": 10, "dochod": 1200, "wydatki": 700},
]


def delete_outliers(dane):
    """
    założenia:
    wiek 0 - 100
    dochód > 0
    wydatki >= 0
    """
    return [
        k for k in dane if 0 < k['wiek'] <= 100 and k['dochod'] > 0 and k['wydatki'] >= 0
    ]

def segmentuj(dane):
    return[
        {
            **k, 'segment':('niski' if k['dochod'] < 4000 else 'średni' if k['dochod'] <= 8000 else 'wysoki')
        }
        for k in dane
    ]

def normalizuj(dane, kolumny):
    for kolumna in kolumny:
        wartosci = [k[kolumna] for k in dane]
        min_v, max_v = min(wartosci), max(wartosci)

        for k in dane:
            value = (
            (k[kolumna] - min_v) / (max_v - min_v)
            if max_v != min_v else 0
            )
            value = round(value, 2)
            k[kolumna + "_norm"] = value
    return dane


klienci_outliers = delete_outliers(klienci)
klienci_segment = segmentuj(klienci_outliers)
klienci_norm = normalizuj(klienci_segment, ['wiek', 'dochod'])

for i in klienci_norm:
    print(i)


