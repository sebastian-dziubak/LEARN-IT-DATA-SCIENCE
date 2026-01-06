"""
Zadanie 1 – Tworzenie słownika z informacjami o osobie
Stwórz słownik osoba zawierający klucze: imie , nazwisko , wiek , miasto , email .
Wypełnij go przykładowymi danymi i wypisz wszystkie informacje w czytelny sposób.
Wymagania:
Użyj f-stringów do formatowaniaWypisz każdą informację w osobnej linii
Oczekiwany wynik:
Wydruk typu: "Imię: Jan, Nazwisko: Kowalski, ..."

"""

osoba = {'imie': 'Sebastian',
         'nazwisko': 'Dziubak',
         'wiek': 38,
         'miasto': 'warszawa',
         'email': 'sebastian.dziubak@yahoo.com'}

for k, v in osoba.items():
    if k == 'wiek':
        print(f'{k.title()}: {v}')
    elif k == 'email':
        print(f'{k.title()}: {v}')
    else:
        print(f'{k.title()}: {v.title()}')