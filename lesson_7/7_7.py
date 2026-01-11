"""Zadanie 7 – Tabliczka mnożenia
Wyświetl tabliczkę mnożenia dla liczby 7 (od 7×1 do 7×10) używając pętli for i range() .
Wymagania:
for i in range(1, 11):
Oblicz wynik = 7 * i
Wyświetl: "7 × 1 = 7"
Oczekiwany rezultat:
10 linii z wynikami mnożenia"""

number = 7

for i in range(1, 11):
    wynik = number * i
    print(f'{number} x {i} = {wynik}')