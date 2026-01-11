"""Zadanie 5 – Suma liczb w zakresie
Oblicz sumę wszystkich liczb od 1 do 50 używając pętli while .
Wymagania:
Zmienne: suma = 0 , i = 1
while i <= 50:
Dodaj i do sumy i zwiększ i += 1
Sprawdź wynik wzorem: n*(n+1)/2 = 50*51/2 = 1275
Oczekiwany rezultat:
Suma: 1275"""

suma_while = 0
i = 1
n = 50
suma_n = n * (n + 1) / 2

while i <= n:
    suma_while += i
    i += 1

print(f'''
Suma While: {suma_while}   
Suma n: {suma_n}
Czy suma while = suma n? {suma_while == suma_n}
''')