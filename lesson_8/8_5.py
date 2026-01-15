"""Zadanie 5 – Lambda do sortowania
Masz listę tuple z produktami: (nazwa, cena, ocena) . Posortuj ją według ceny rosnąco,
używając sorted() i lambda.
Dataset:
produkty = [
("laptop", 2999, 4.5),
("mysz", 89, 4.2),
("klawiatura", 249, 4.8),
("monitor", 899, 4.3)
]
Wymagania:
Użyj sorted() z parametrem key=lambda ...
Posortuj według drugiego elementu tuple (cena)
Oczekiwany rezultat:
Lista posortowana od najtańszego do najdroższego"""

produkty = [
    ("laptop", 2999, 4.5),
    ("mysz", 89, 4.2),
    ("klawiatura", 249, 4.8),
    ("monitor", 899, 4.3)
]

print(sorted(produkty, key=lambda x: x[1]))