"""Zadanie 10 – Znajdź wszystkie liczby pierwsze do 100
Napisz program, który znajdzie wszystkie liczby pierwsze od 2 do 100 używając
zagnieżdżonych pętli.
Wymagania:
Pętla zewnętrzna: for n in range(2, 101):
Pętla wewnętrzna: sprawdź dzielniki od 2 do √n
Zmienna czy_pierwsza = True
Jeśli znajdziesz dzielnik, ustaw czy_pierwsza = False i użyj break
Jeśli czy_pierwsza == True , dodaj do listy
Oczekiwany rezultat:
Lista liczb pierwszych: [2, 3, 5, 7, 11, 13, ..., 97]
Liczba znalezionych: 25"""

pierwsze = []

for n in range(2, 101):
    czy_pierwsza = True
    for m in range(2, int(n ** 0.5)+1):
        if n % m == 0:
            czy_pierwsza = False
            break
    if czy_pierwsza == True:
       pierwsze.append(n)

print(f'''
Lista liczb pierwszych: {pierwsze}
Liczba znalezionych: {len(pierwsze)}
''')