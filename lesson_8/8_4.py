"""Zadanie 4 – Kwadraty liczb nieparzystych
Używając list comprehension, stwórz listę kwadratów liczb nieparzystych z zakresu 1-20.
Dataset:
Zakres: 1-20
Wymagania:List comprehension z warunkiem x % 2 != 0
Oblicz kwadraty tych liczb
Oczekiwany rezultat:
Lista: [1, 9, 25, 49, ...]"""

squares_not_even = [x ** 2 for x in range(1, 21) if x % 2 != 0]
print(squares_not_even)