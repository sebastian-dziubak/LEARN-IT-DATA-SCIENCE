"""Zadanie 10 – Klasa Zamowienie z kompozycją
Stwórz klasę Produkt (nazwa, cena) oraz klasę Zamowienie , która zawiera listę
produktów.
Metody Zamowienie :
dodaj_produkt(produkt, ilosc)
laczna_wartosc() – suma wartości zamówienia
pokaz_zamowienie() – wyświetla wszystkie produkty i łączną wartość
Stwórz zamówienie z 5 produktami."""
from xml.sax.handler import feature_namespace_prefixes


class Produkt:
    def __init__(self, nazwa, cena):
        self.nazwa = nazwa
        self.cena = cena

class Zamowienie:
    def __init__(self):
        self.order = []

    def dodaj_produkt(self, produkt, ilosc):
        self.order.append((produkt, ilosc))

    def laczna_wartosc(self):
        suma = 0
        for produkt, ilosc in self.order:
            suma += (produkt.cena * ilosc)
        return suma

    def pokaz_zamowienie(self):
        print('Zamówienie:')
        for produkt, ilosc in self.order:
            print(f'Nazwa: {produkt.nazwa}, cena: {produkt.cena}, ilość: {ilosc}')
        print(f'Całkowita wartość produktów: {my_order.laczna_wartosc():.2f} PLN')



p1 = Produkt('ksiazka', 30)
p2 = Produkt('piłka', 55)
p3 = Produkt('komputer', 3500)
p4 = Produkt('konsola', 3100)
p5 = Produkt('laptop', 4200)

my_order = Zamowienie()
my_order.dodaj_produkt(p1, 5)
my_order.dodaj_produkt(p2, 4)
my_order.dodaj_produkt(p3, 2)
my_order.dodaj_produkt(p4, 3)
my_order.dodaj_produkt(p5, 1)

my_order.pokaz_zamowienie()