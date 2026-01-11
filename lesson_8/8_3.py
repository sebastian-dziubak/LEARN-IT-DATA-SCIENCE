"""Zadanie 3 – Filtr liczb parzystych
Używając list comprehension, stwórz listę zawierającą tylko liczby parzyste z zakresu 1-
100.
Dataset:
Zakres: 1-100
Wymagania:
Użyj list comprehension z warunkiem
Wypisz pierwsze 10 liczb parzystych
Oczekiwany rezultat:
Lista: [2, 4, 6, 8, 10, ...]"""

even = [x for x in range(1, 101) if x % 2 == 0]
print(even[:10])