"""Zadanie 8 – Map i filter
Używając map() i filter() z lambda, przetwórz listę liczb: najpierw zostaw tylko
dodatnie, potem podwój każdą.
Dataset:
liczby = [-5, 3, -2, 8, 0, -1, 7, 4, -9, 6]
Wymagania:
filter() z lambda: x > 0
map() z lambda: x * 2
Konwertuj wynik na listę
Oczekiwany rezultat:
Lista: [6, 16, 14, 8, 12] (tylko dodatnie i podwojone)"""

liczby = [-5, 3, -2, 8, 0, -1, 7, 4, -9, 6]

filtred_liczby = list(filter(lambda x: x > 0, liczby))
doubled_liczby = list(map(lambda x: x * 2, filtred_liczby))

print(doubled_liczby)