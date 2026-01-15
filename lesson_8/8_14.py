"""Zadanie 14 – Funkcja do detekcji outliers
Napisz funkcję wykryj_outliery(dane, metoda="IQR") , która wykrywa wartości
odstające używając metody IQR (Interquartile Range).
Dataset:czasy_odpowiedzi = [120, 135, 142, 128, 5000, 138, 145, 119, 10000, 133,
141]
Wymagania:
Oblicz Q1 (25 percentyl) i Q3 (75 percentyl)
IQR = Q3 - Q1
Outliers: wartości < Q1 - 1.5IQR lub > Q3 + 1.5IQR
Funkcja zwraca (czyste_dane, outliery)
Oczekiwany rezultat:
Lista outlierów: [5000, 10000]
Lista czystych danych bez outlierów"""


def wykryj_outliery(dane, metoda='IQR'):
    outliers = []
    dane_sorted = sorted(dane)
    q1_index = int((len(dane_sorted) + 1) * (1/4) - 1)
    q3_index = int((len(dane_sorted) + 1) * (3/4) - 1)
    Q1 = dane_sorted[q1_index]
    Q3 = dane_sorted[q3_index]
    IQR = Q3 - Q1
    for i in dane_sorted:
        if i < Q1 - (1.5 * IQR) or i > Q3 + (1.5 * IQR):
            outliers.append(i)
    for i in outliers:
        dane.remove(i)
    print(f'Lista outlierów: {outliers}\nLista czystych danych bez outlierów: {dane}')


czasy_odpowiedzi = [120, 135, 142, 128, 5000, 138, 145, 119, 10000, 133, 141]
wykryj_outliery(czasy_odpowiedzi)
