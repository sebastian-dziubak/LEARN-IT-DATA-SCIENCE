"""Zadanie 17 – Algorytm Euklidesa (NWD) z licznikiem iteracjiZaimplementuj algorytm Euklidesa do znajdowania największego wspólnego dzielnika
(NWD) dwóch liczb: 252 i 105. Policz liczbę iteracji.
Wymagania:
Użyj pętli while
Algorytm: dopóki b ≠ 0: temp = b, b = a % b, a = temp
Zlicz iteracje
Wyświetl każdy krok
Oczekiwany rezultat:
NWD(252, 105) = 21
Liczba iteracji: 4"""

a = 252
b = 105
c = ''
liczba_iteracji = 0

print(f'NWD({a}, {b})\n')

while c != 0:
    nwd = b
    c = a % b
    print(f'{a} : {b} = {a // b}, reszta {c}')
    liczba_iteracji += 1
    a = b
    b = c

print(f'\nNWD = {nwd}\nLiczba iteracji: {liczba_iteracji}')

