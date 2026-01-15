"""Zadanie 5 – Klasa Student
Stwórz klasę Student z atrybutami: imie , numer_indeksu , oceny (lista ocen).
Metody:
dodaj_ocene(ocena) – dodaje ocenę do listy
srednia() – zwraca średnią ocen
__str__() – reprezentacja tekstowa
Stwórz 3 studentów, dodaj im oceny i wyświetl średnie."""


class Student():
    def __init__(self, imie, numer_indeksu, oceny):
        self.i = imie
        self.n = numer_indeksu
        self.o = oceny

    def dodaj_ocene(self, ocena):
        self.o.append(ocena)

    def srednia(self):
        return round(sum(self.o) / len(self.o), 2)


    def __str__(self):
        return (f'Imię: {self.i} (numer indeksu: {self.n})\n'
                f'oceny: {self.o}\n'
                f'średnia ocen: {self.srednia()}')

s1 = Student('sebastian', 77896, [3, 3, 4, 5])
print(s1)
s1.dodaj_ocene(6)
print(s1)
print(s1.srednia())