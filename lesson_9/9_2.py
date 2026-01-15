"""Stwórz klasę Kalkulator z metodami: dodaj(a, b) , odejmij(a, b) , pomnoz(a, b) ,
podziel(a, b) .
Stwórz obiekt i wykonaj przykładowe obliczenia."""

class Kalkulator:

    @staticmethod
    def dodaj(a, b):
        return a + b

    @staticmethod
    def odejmij(a, b):
        return a - b

    @staticmethod
    def pomnoz(a, b):
        return a * b

    @staticmethod
    def podziel(a, b):
        return round((a / b), 2)

obliczenia = Kalkulator
a = 10
b = 3

print(f'''
a = {a}
b = {b}

dodawanie: {obliczenia.dodaj(a, b)}
odejmowanie: {obliczenia.odejmij(a, b)}
mnożenie: {obliczenia.pomnoz(a, b)}
dzielenie: {obliczenia.podziel(a, b)}
''')