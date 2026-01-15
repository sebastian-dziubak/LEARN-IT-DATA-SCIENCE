"""Zadanie 6 – Dziedziczenie – Pojazd i Samochod
Stwórz klasę bazową Pojazd z atrybutami: marka , model , rok .
Stwórz klasę potomną Samochod z dodatkowym atrybutem liczba_drzwi .
Dodaj metodę pokaz_info() w obu klasach.
Stwórz obiekt Samochod i wywołaj metodę."""

class Pojazd:
    def __init__(self, marka, model, rok):
        self.marka = marka
        self.model = model
        self.rok = rok

    def pokaz_info(self):
        print(f'Klasa Pojazd\n'
              f'marka: {self.marka}\n'
              f'model: {self.model}\n'
              f'rocznik: {self.rok}\n')


class Samochod(Pojazd):
    def __init__(self, marka, model, rok, liczba_drzwi):
        super().__init__(marka, model, rok)
        self.liczba_drzwi = liczba_drzwi

    def pokaz_info(self):
        print(f'Klasa Samochód\n'
              f'marka: {self.marka}\n'
              f'model: {self.model}\n'
              f'rocznik: {self.rok}\n'
              f'liczba drzwi: {self.liczba_drzwi}')


pojazd = Pojazd('Ford', 'Focus', 2026)
samochod = Samochod('Skoda', 'Superb', 2005, 5)

pojazd.pokaz_info()
samochod.pokaz_info()
