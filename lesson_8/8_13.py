"""Zadanie 13 – Pipeline przetwarzania danych sprzedażowych
Stwórz kompletny pipeline do analizy danych sprzedażowych. Dane zawierają: dzień,
kategoria, liczba transakcji, wartość.
Dataset:
sprzedaz = [
(1, "elektronika", 45, 12500),
(1, "odziez", 78, 4200),
(2, "elektronika", 52, 15200),
# ... więcej danych dla 7 dni
]
Wymagania:
Funkcja tuple_to_dict() - konwersja tuple na dict
Funkcja dodaj_srednia_transakcje() - feature engineering
Funkcja agreguj_po_kategorii() - suma wartości per kategoria
Użyj comprehensions do przetwarzania
Sortowanie kategorii według wartości (malejąco)
Oczekiwany rezultat:
Ranking kategorii z sumą wartości sprzedaży"""

sprzedaz = [
    (1, "elektronika", 45, 12500),
    (1, "odziez", 78, 4200),
    (1, "ksiazki", 34, 890),
    (2, "elektronika", 52, 15200),
    (2, "odziez", 65, 3800),
    (2, "ksiazki", 29, 760),
    (3, "elektronika", 38, 9800),
    (3, "odziez", 82, 5100),
    (3, "ksiazki", 41, 1020),
    (4, "elektronika", 61, 18900),
    (4, "odziez", 71, 4500),
    (4, "ksiazki", 38, 950),
    (5, "elektronika", 44, 11200),
    (5, "odziez", 88, 5600),
    (5, "ksiazki", 45, 1150)
]


# preprocessing - transformacja tuple do słownika
def tuple_to_dict(data):
    return {
        'dzień': data[0],
        'kategoria': data[1],
        'liczba_transakcji': data[2],
        'wartość': data[3]
    }

sprzedaz_dict = [tuple_to_dict(x) for x in sprzedaz]


# feature engineering - nowe cechy
def dodaj_srednia_transakcje(data):
    return {
        **data, 'średnia wartość transakcji': round(data['wartość'] / data['liczba_transakcji'], 2)
    }

sprzedaz_engineered = [dodaj_srednia_transakcje(x) for x in sprzedaz_dict]


# agregacja po kategoriach
def agreguj_po_kategorii(data, kategoria):
    dane_kat = [r for r in data if r['kategoria'] == kategoria]
    suma_transakcji = sum(r['liczba_transakcji'] for r in dane_kat)
    suma_wartosci = sum(r['wartość'] for r in dane_kat)

    return {
        'kategoria': kategoria,
        'suma transakcji': suma_transakcji,
        'suma wartości': suma_wartosci
    }

# unikalne kategorie
kategorie = {r['kategoria'] for r in sprzedaz_engineered}

#agregacja dla każdej kategorii
statystyki = [agreguj_po_kategorii(sprzedaz_engineered, kat) for kat in kategorie]

statystyki_sorted = sorted(statystyki, key=lambda x: x['suma wartości'], reverse=True)

for i in statystyki_sorted:
    print(i)