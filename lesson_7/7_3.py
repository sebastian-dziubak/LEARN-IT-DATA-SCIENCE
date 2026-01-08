"""Zadanie 3 – Odliczanie z krokiemNapisz program, który wyświetli odliczanie od 20 do 0 z krokiem -2 (20, 18, 16, ..., 2, 0).
Użyj pętli for i funkcji range() .
Wymagania:
for i in range(20, -1, -2):
Wyświetl każdą liczbę
Oczekiwany rezultat:
Lista liczb: 20, 18, 16, 14, 12, 10, 8, 6, 4, 2, 0"""

for i in range(20, -1, -2):
    if i == 0:
        print(f'{i}')
    else:
        print(f'{i}', end=', ')
