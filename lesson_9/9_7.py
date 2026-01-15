"""Zadanie 7 – Klasa Pracownik
Stwórz klasę Pracownik z atrybutami: imie , stanowisko , pensja .
Metody:
podwyzka(procent) – zwiększa pensję o procent%
__str__() – reprezentacja tekstowa
Stwórz 3 pracowników i daj im podwyżki."""


class Pracownik:
    def __init__(self, imie, stanowisko, pensja):
        self.imie = imie.title()
        self.stanowisko = stanowisko.title()
        self.pensja = pensja

    def podwyzka(self, procent):
        self.pensja *= (procent / 100) + 1

    def __str__(self):
        return (f'Imię pracownika: {self.imie}\n'
                f'Stanowisko: {self.stanowisko}\n'
                f'Zarobki: {self.pensja:.2f} PLN')

pracownicy = []
dane = [('sebastian', 'manager', 15000),
        ('agata', 'nauczycielka', 7000),
        ('tadeusz', 'nauczyciel akademicki', 12000)]

rises = [10, 25, 15]

for d in dane:
    i, s, p = d
    pracownicy.append(Pracownik(imie=i, stanowisko=s, pensja=p))

print('Pracownicy przed podwyżką: ')
for i in pracownicy:
    print(i, end='\n\n')

for pracownik, podwyzka in zip(pracownicy, rises):
    pracownik.podwyzka(podwyzka)

print('Pracownicy po podwyżce:')
for i in pracownicy:
    print(i, end='\n\n')