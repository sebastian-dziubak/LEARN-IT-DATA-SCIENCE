'''Zadanie 15 – Funkcje wyższego rzędu - decorator pattern
Napisz funkcję timer(func) , która mierzy czas wykonania innej funkcji. Użyj jej do
porównania wydajności pętli vs comprehension.
Dataset:
Zakres: 1-100000
Wymagania:
Funkcja timer() przyjmuje funkcję jako argument
Wewnątrz timer() mierz czas wykonania func()
Porównaj czas dla:
Funkcji z pętlą for tworzącą listę kwadratów
List comprehension tworzącej listę kwadratów
Oczekiwany rezultat:
Wydruk: "Pętla: 0.123s, Comprehension: 0.089s"'''

def timer(func):
    import time
    start = time.time()
    func
    stop = time.time()
    return f'{(stop - start):.2e} s'

def petla():
    lst = []
    for i in range(1, 100001):
        lst.append(i ** 2)


def comprehension():
    lst = [x ** 2 for x in range(1, 100001)]


print(f'''
Czas wykonania funkcji "pętla": {timer(petla())}
Czas wykonania funkcji "comprehension": {timer(comprehension())}
''')
