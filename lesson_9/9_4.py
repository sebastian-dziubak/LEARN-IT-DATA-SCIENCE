"""Zadanie 4 – Klasa Ksiazka
Stwórz klasę Ksiazka z atrybutami: tytul , autor , rok_wydania , liczba_stron .
Dodaj metodę __str__() , która zwraca czytelną reprezentację książki.
Stwórz listę 5 książek i wyświetl je używając print() ."""

class Ksiazka():
    def __init__(self, tytul, autor, rok_wydania, liczba_stron):
        self.tytul = tytul
        self.autor = autor
        self.rok_wydania = rok_wydania
        self.liczba_stron = liczba_stron

    def __str__(self):
        return f'Tytuł: "{self.tytul}", autorstwa: {self.autor} ({self.rok_wydania}) - liczba stron: {self.liczba_stron}'


k1 = Ksiazka('Pan Tadeusz', 'Adam Mickiewicz', 1870, 355)

print(k1)