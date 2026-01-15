'''Zadanie 6 – Funkcja z wartościami domyślnymi
Napisz funkcję powitanie(imie, jezyk="polski") , która wyświetla powitanie w
wybranym języku (polski, angielski, niemiecki).
Dataset:
Brak (funkcja operuje na stringach)
Wymagania:
Domyślny język to polski
Obsługa 3 językówWywołaj funkcję 3 razy z różnymi parametrami
Oczekiwany rezultat:
powitanie("Anna") → "Cześć, Anna!"
powitanie("Anna", "angielski") → "Hello, Anna!"'''

def powitanie(imie, jezyk="polski"):
    starting = 'Cześć'
    if jezyk == 'angielski':
        starting = 'Hello'
    elif jezyk == 'hiszpański':
        starting = 'Holla'
    print(f'{starting}, {imie.title()}')

powitanie('anna', 'hiszpański')