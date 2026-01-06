"""
Zadanie 7 – Zwracanie wielu wartości z funkcji
Napisz funkcję analiza_liczb(lista) która zwraca krotkę z: sumą, średnią, minimum i
maksimum z listy. Przetestuj na liście [10, 20, 30, 40, 50] .
Wymagania:
Funkcja zwraca krotkę z 4 wartościami
Użyj tuple unpacking przy wywołaniu
Wypisz wyniki

"""

def analiza_liczb(lista):
    suma = sum(lista)
    srednia = suma / len(lista)
    minimum = min(lista)
    maksimum = max(lista)
    return suma, srednia, minimum, maksimum


my_list = [10, 20, 30, 40, 50]

s, sr, min, max = analiza_liczb(my_list)

print(f'''
Lista liczb: {my_list}
Suma: {s}
Średnia: {sr}
Minimum: {min}
Maksimum: {max}
''')