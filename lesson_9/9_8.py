"""Zadanie 8 – Klasa Zadanie (TO DO list)
Stwórz klasę Zadanie z atrybutami: opis , status (domyślnie "do zrobienia").
Metody:
oznacz_jako_zrobione() – zmienia status na "zrobione"
__str__() – wyświetla opis i statusStwórz listę 5 zadań i oznacz część jako zrobione."""
from operator import index


class Zadanie:
    def __init__(self, opis, status='do zrobienia'):
        self.opis = opis
        self.status = status

    def oznacz_jako_zrobione(self):
        self.status = 'zrobione'

    def __str__(self):
        return f'{self.opis} - {self.status}'

opisy = ['kupić mleko', 'pościelić łóżko', 'pograć w grę', 'poczytać książkę', 'pograć w piłkę']
lista_zadan = []

for opis in opisy:
    lista_zadan.append(Zadanie(opis=opis))

for zadanie in lista_zadan:
    if lista_zadan.index(zadanie) %2 == 0:
        zadanie.oznacz_jako_zrobione()
    print(zadanie)