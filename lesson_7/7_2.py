"""Zadanie 2 – Suma liczb dodatnich
Masz listę temperatury: [-5, 3, -2, 8, 12, -1, 6, 0, 15, -3] . Oblicz sumę tylko
dodatnich wartości używając pętli for i instrukcji warunkowej.
Wymagania:
Użyj zmiennej suma = 0
W pętli sprawdzaj if temp > 0:
Dodaj tylko dodatnie wartości do sumy
Oczekiwany rezultat:
Wyświetlenie sumy dodatnich temperatur
Liczba dodatnich pomiarów"""

temp = [-5, 3, -2, 8, 12, -1, 6, 0, 15, -3]

suma = 0
pomiar = 0

for i in temp:
    if i > 0:
        suma += i
        pomiar += 1
print(f'''
suma dodatnich pomiarów: {suma}
liczba dodatnich pomiarów: {pomiar}
''')

temp_dodatnie = [i for i in temp if i > 0]
pomiar = len(temp_dodatnie)
suma = sum(temp_dodatnie)
print(f'''
suma dodatnich pomiarów LC: {suma}
liczba dodatnich pomiarów LC: {pomiar}
''')