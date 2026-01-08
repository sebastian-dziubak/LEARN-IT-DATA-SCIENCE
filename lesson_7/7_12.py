"""Zadanie 12 – Walidacja numeru PESEL (uproszczona)
Sprawdź poprawność sum kontrolnych dla listy numerów PESEL (symulacja):
["92041812345", "85010154321", "78121698765"] . Użyj pętli do iteracji po cyfrach.
Dataset:
Lista 3 numerów PESEL (string)
Wymagania:
Dla każdego PESEL iteruj po cyfrach
Sprawdź długość (11 cyfr)
Sprawdź czy wszystkie znaki to cyfry
Oznacz jako "poprawny format" lub "błędny format"
Oczekiwany rezultat:
Raport walidacji dla każdego numeru"""

dataset = ["92041812X345", "85010154321", "7812169Y8765"]

for pesel in dataset:
    format = 'poprawny'
    for number in pesel:
        if number.isdigit() != True:
            format = 'niepoprawny'
            break
    print(f'Numer pesel: {pesel} - format: {format}')