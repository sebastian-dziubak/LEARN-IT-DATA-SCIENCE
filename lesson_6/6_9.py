"""
Zadanie 9 – Inwersja słownika
Masz słownik mapujący nazwy produktów na kategorie: {'laptop': 'elektronika',
'klawiatura': 'elektronika', 'krzesło': 'meble', 'biurko': 'meble'} . Stwórz
odwrotny słownik gdzie klucze to kategorie, a wartości to listy produktów.
Wymagania:
Iteruj po oryginalnym słowniku
Zgrupuj produkty według kategorii
Wynik: {'elektronika': ['laptop', 'klawiatura'], 'meble': [...]}
Oczekiwany wynik:
Słownik kategoria: lista_produktów

"""

dct = {'laptop': 'elektronika', 'klawiatura': 'elektronika', 'krzesło': 'meble', 'biurko': 'meble'}
new_dct = {}

for k, v in dct.items():
    if v not in new_dct:
        new_dct[v] = []
    new_dct[v].append(k)

print(new_dct)