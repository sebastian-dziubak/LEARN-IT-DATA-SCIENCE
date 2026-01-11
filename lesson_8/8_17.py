'''Zadanie 17 – Generator vs Lista - oszczędność pamięci
Porównaj zużycie pamięci: lista vs generator dla dużych danych.
Dataset:
n = 10 milionów elementów
Wymagania:
Stwórz list comprehension: [i**2 for i in range(n)]
Stwórz generator: (i**2 for i in range(n))
Użyj sys.getsizeof() do pomiaru rozmiaru w bajtach
Oblicz różnicę w MB
Oczekiwany rezultat:
Lista: ~80 MB
Generator: ~128 bajtów
Oszczędność pamięci: >99%'''

import sys

n = 10 ** 6
generator = (i**2 for i in range(n) )
list_comprehension = [i**2 for i in range(n)]

memory_generator = sys.getsizeof(generator)
memory_lc = sys.getsizeof(list_comprehension)

print(f'''
lista: {memory_lc / (100000):.2f} MB
generator: {memory_generator:.2f} bajtów
oszczędność pamięci: > {(memory_lc - memory_generator) / memory_lc:.3%}
''')