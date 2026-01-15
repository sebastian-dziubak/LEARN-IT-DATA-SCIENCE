"""Stwórz klasę BankAccount z atrybutami: wlasciciel , saldo .
Metody:
wplac(kwota) – zwiększa saldo
wyplac(kwota) – zmniejsza saldo (tylko jeśli wystarczy środków)
pokaz_saldo() – wyświetla saldo
Stwórz kilka kont i przetestuj operacje."""


class BankAccount():
    def __init__(self, wlasciciel, saldo):
        self.wlasciciel = wlasciciel
        self.saldo = saldo

    def wplac(self, kwota):
        if kwota > 0:
            self.saldo += kwota
        else:
            print('Nie można dodać kwoty do salda')

    def wyplac(self, kwota):
        if kwota <= self.saldo:
            self.saldo -= kwota
        else:
            print('Niewystarczająca ilość środków')

    def pokaz_saldo(self):
        print(f'Klient: {self.wlasciciel} (saldo: {self.saldo} PLN)')


klient1 = BankAccount('Kowalski', 1500)
klient2 = BankAccount('Nowak', 3000)

klient1.pokaz_saldo()
klient1.wplac(2000)
klient1.pokaz_saldo()
klient1.wyplac(5000)
