"""Zadanie 12 – Zagnieżdżone comprehensions - macierz
Stwórz macierz 10x10 zawierającą wartości i * j (iloczyn indeksów) używając
zagnieżdżonych list comprehensions.
Dataset:
Rozmiar macierzy: 10x10
Wymagania:
Zewnętrzna comprehension: wiersze (i od 1 do 10)Wewnętrzna comprehension: kolumny (j od 1 do 10)
Wartość: i * j
Oczekiwany rezultat:
Macierz 10x10 wydrukowana czytelnie"""

i = 10
j = 10

matrix = [[x * y for y in range(1, j+1)] for x in range(1, i+1)]

for x in matrix:
    for y in x:
        print(y, end='\t')
    print()