"""Zadanie 11 – System ocen uczniów
Stwórz klasy:
Uczen (imie, oceny=[])
Klasa (nazwa, uczniowie=[])
Metody Klasa :
dodaj_ucznia(uczen)
srednia_klasy() – średnia ocen wszystkich uczniów
najlepszy_uczen() – zwraca ucznia z najwyższą średniąStwórz klasę z 5 uczniami i oblicz statystyki."""

class Uczen:
    def __init__(self, imie, oceny=[]):
        self.imie = imie.title()
        self.oceny = oceny

class Klasa:
    def __init__(self, nazwa, uczniowie=[]):
        self.nazwa = nazwa
        self.uczniowie = uczniowie

    def dodaj_ucznia(self, uczen):
        self.uczniowie.append(uczen)

    def srednia_klasy(self):
        liczba_uczniow = len(self.uczniowie)
        suma = 0
        for uczen in self.uczniowie:
            suma += float(self.srednia_uczen(uczen.imie))
        print(f'Średnia klasy {self.nazwa} - {suma / liczba_uczniow}')

    def najlepszy_uczen(self):
        best = self.uczniowie[0]
        for uczen in self.uczniowie:
            if self.srednia_uczen(uczen.imie) > self.srednia_uczen(best.imie):
                best = uczen
        print(f'Najlepszy uczeń w klasie {self.nazwa} - '
              f'{best.imie} (średnia: {self.srednia_uczen(best.imie)})')

    def wypisz(self):
        for uczen in self.uczniowie:
            print(uczen.imie, uczen.oceny)

    def srednia_uczen(self, imie):
        for uczen in self.uczniowie:
            if uczen.imie == imie.title():
                srednia = sum(uczen.oceny) / len(uczen.oceny)
        return f'{srednia:.2f}'




u1 = Uczen('sebastian', [5, 6, 4, 2, 1, 1, 1])
u2 = Uczen('agata', [2, 3, 4])
u3 = Uczen('tadeusz', [4,5,4, 1, 2 ,3])

klasa1 = Klasa('6F', [u1, u2, u3])

klasa1.srednia_klasy()
klasa1.najlepszy_uczen()

u4 = Uczen('andrzej', [6, 5, 4, 6 ,6])
klasa1.dodaj_ucznia(u4)

klasa1.srednia_klasy()
klasa1.najlepszy_uczen()