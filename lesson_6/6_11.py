"""Zadanie 11 – Dictionary comprehension - kwadraty liczb
Stwórz słownik używając dictionary comprehension, gdzie klucze to liczby od 1 do 20, a
wartości to ich kwadraty. Następnie przefiltruj ten słownik (też comprehension!) by zawierał
tylko liczby parzyste.
Wymagania:Użyj dictionary comprehension 2 razy
Pierwszy słownik: wszystkie liczby 1-20
Drugi słownik: tylko parzyste klucze
Oczekiwany wynik:
Dwa słowniki wypisane"""

first_dct = {v: v ** 2 for v in range(1, 21)}
second_dict = {v: v ** 2 for v in range(1, 21) if v % 2 == 0}

print(f'Pierwszy słownik:\n{first_dct}')
print(f'Drugi słownik:\n{second_dict}')
