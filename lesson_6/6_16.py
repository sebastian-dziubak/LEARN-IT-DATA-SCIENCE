"""
Zadanie 16 – Cache funkcji używając słownika (memoization)
Napisz funkcję fibonacci(n) która oblicza n-tą liczbę Fibonacciego. Użyj słownika jako
cache by przechowywać już obliczone wartości (memoization). Porównaj czas wykonania z
i bez cache dla n=35 .Wymagania:
Implementacja rekurencyjna z cache
Cache jako słownik globalny lub parametr z wartością domyślną
Pomiar czasu dla obu wersji
Wypisz liczbę wywołań funkcji
Oczekiwany wynik:
Fibonacci(35) obliczone
Porównanie czasu: z cache vs bez cache
Demonstracja przyspieszenia
"""

import time

calls_no_cache = 0
calls_cache = 0

def fibonacci_no_cache(n):
    global calls_no_cache
    calls_no_cache += 1
    if n <= 1:
        return n
    else:
        return fibonacci_no_cache(n - 1) + fibonacci_no_cache(n - 2)

def fibonacci_cache(n, memo={}):
    global calls_cache
    calls_cache += 1
    if n in memo:
        return memo[n]
    if n <= 1:
        memo[n] = n
    else:
        memo[n] = fibonacci_cache(n - 1, memo) + fibonacci_cache(n - 2, memo)
    return memo[n]

start = time.time()
fibo1 = fibonacci_no_cache(35)
stop = time.time()
fibo1_time = stop - start

start = time.time()
fibo2 = fibonacci_cache(35)
stop = time.time()
fibo2_time = stop - start

print(f'''
Numer liczby ciągu Fibonacciego: 35
*** Bez cache ***
czas wykonania funkcji: {fibo1_time:.6f} s
liczba wywołań funkcji: {calls_no_cache}

*** Z cache ***
czas wykonania funkcji: {fibo2_time:.6f} s
liczba wywołań funkcji: {calls_cache}
''')