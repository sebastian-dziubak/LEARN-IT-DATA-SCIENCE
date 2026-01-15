"""Zadanie 1 – Tworzenie klasy Produkt
Stwórz klasę Produkt z atrybutami: nazwa , cena , ilosc_w_magazynie .
Dodaj metody:
pokaz_info() – wyświetla informacje o produkcie
sprzedaj(ilosc) – zmniejsza ilosc_w_magazynie o podaną wartość
dostawa(ilosc) – zwiększa ilosc_w_magazynie
Stwórz 3 obiekty i przetestuj metody."""


class Produkt():
    def __init__(self, nazwa, cena, ilosc_w_magazynie):
        self.nazwa = nazwa
        self.cena = cena
        self.ilosc = ilosc_w_magazynie

    def pokaz_info(self):
        print(f'Nazwa: {self.nazwa}'
              f'Cena: {self.cena}'
              f'Ilość w magazynie: {self.ilosc}')

    def sprzedaj(self, ilosc):
        self.ilosc -= ilosc

    def dostawa(self, ilosc):
        self.ilosc += ilosc

obiekt1 = Produkt('książka', 55, 150)
obiekt2 = Produkt('piłka', 12, 33)
obiekt3 = Produkt('kubek', 5, 88)

print(obiekt1.ilosc)
obiekt1.sprzedaj(55)
print(obiekt1.ilosc)
obiekt1.dostawa(200)
print(obiekt1.ilosc)