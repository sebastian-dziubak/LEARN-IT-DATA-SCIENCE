"""Zadanie 7 – Długości słów
Masz listę słów. Używając list comprehension, stwórz nową listę zawierającą długości tych
słów.
Dataset:
slowa = ["python", "data", "science", "machine", "learning", "AI"]
Wymagania:
Użyj list comprehension: [len(slowo) for slowo in slowa]
Oczekiwany rezultat:
Lista długości: [6, 4, 7, 7, 8, 2]"""

slowa = ["python", "data", "science", "machine", "learning", "AI"]

dlugosc = [len(slowo) for slowo in slowa]

print(dlugosc)