"""Zadanie 16 – Rekurencja - obliczanie silni i Fibonacciego
Napisz dwie funkcje rekurencyjne: silnia(n) i fibonacci(n) .
Dataset:n = 10 dla silni
n = 15 dla Fibonacciego
Wymagania:
Silnia: n! = n * (n-1)! , przypadek bazowy: 0! = 1
Fibonacci: fib(n) = fib(n-1) + fib(n-2) , bazowe: fib(0)=0, fib(1)=1
Oblicz silnię dla 10
Oblicz pierwsze 15 liczb Fibonacciego
Oczekiwany rezultat:
Silnia(10) = 3628800
Fibonacci(15): [0, 1, 1, 2, 3, 5, 8, 13, 21, ...]"""

def silnia(n):
    if n != 0:
        return n * silnia(n - 1)
    else:
        return 1

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

n = 10
print(f'Silnia({n}) = {silnia(n)}')
n = 15
print(f'Fibonacci({n}):', [fibonacci(i) for i in range(n)])