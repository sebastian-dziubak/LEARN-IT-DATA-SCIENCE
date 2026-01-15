"""Zadanie 1 – Kalkulator statystyk
Napisz funkcję statystyki(liczby) , która przyjmuje listę liczb i zwraca tuple zawierający:
(suma, średnia, minimum, maksimum).
Dataset:
Lista ocen: [3.5, 4.0, 5.0, 3.0, 4.5, 5.0, 4.0, 3.5]
Wymagania:
Funkcja powinna zwracać tuple z 4 wartościami
Średnia zaokrąglona do 2 miejsc po przecinku
Oczekiwany rezultat:
Wypisanie wszystkich statystyk na ekran"""


def statystyki(liczby):
    suma = sum(liczby)
    srednia = round(suma / len(liczby), 2)
    minimum = min(liczby)
    maksimum = max(liczby)
    return suma, srednia, minimum, maksimum


my_list = [3.5, 4.0, 5.0, 3.0, 4.5, 5.0, 4.0, 3.5]

print(statystyki(my_list))