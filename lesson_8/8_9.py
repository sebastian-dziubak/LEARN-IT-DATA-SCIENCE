"""Zadanie 9 – Funkcja normalizacji min-max
Napisz funkcję normalize_minmax(dane) , która normalizuje listę liczb do zakresu [0, 1]
używając metody min-max.
Dataset:
wynagrodzenia = [3500, 4200, 5800, 7200, 9500, 4800, 6100]
Wymagania:
Wzór: (x - min) / (max - min)
Funkcja zwraca nową listę znormalizowanych wartości
Zaokrąglij do 3 miejsc po przecinku
Oczekiwany rezultat:
Lista wartości w zakresie [0.0, 1.0]"""


def normalize_minmax(dane):
    result = []
    maksimum = max(dane)
    minimum = min(dane)
    for i in dane:
        result.append(round((i - minimum) / (maksimum - minimum), 3))
    print(result)


wynagrodzenia = [3500, 4200, 5800, 7200, 9500, 4800, 6100]

normalize_minmax(wynagrodzenia)