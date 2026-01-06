"""
Zadanie 4 – Operacje na zbiorach
Masz dwa zbiory: A = {1, 2, 3, 4, 5} i B = {4, 5, 6, 7, 8} . Oblicz i wypisz:
Sumę zbiorów
Przecięcie
Różnicę A - B
Różnicę symetryczną
Wymagania:Użyj operatorów zbiorowych ( | , & , - , ^ )
Wypisz każdy wynik z opisem

"""

A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

print(f'''
Zbiór A: {A}
Zbiór B: {B}

Suma zbiorów: {A | B}
Przecięcie (część wspólna): {A & B}
Różnica A - B: {A - B}
Różnica symetryczna: {A ^ B}
''')