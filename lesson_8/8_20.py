'''Zadanie 20 – Własna implementacja map() i filter()
Napisz własne wersje funkcji my_map(func, iterable) i my_filter(predicate,
iterable) bez używania wbudowanych.
Dataset:
liczby = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Wymagania:
my_map() aplikuje funkcję do każdego elementu
my_filter() zwraca tylko elementy spełniające warunek
Użyj pętli for i append
Przetestuj: podwój liczby, następnie zostaw tylko parzyste
Oczekiwany rezultat:
my_map(lambda x: x*2, liczby) → [2, 4, 6, ..., 20]
my_filter(lambda x: x%2==0, ...) → [2, 4, 6, 8, 10]
(challenge)'''

def my_map(function, iterable):
    result = []
    for i in iterable:
        result.append(function(i))
    return result

def my_filter(predicate, iterable):
    result = []
    for i in iterable:
        if predicate(i):
            result.append(i)
    return result


liczby = [x for x in range(1, 11)]

m = my_map(lambda x: x*2, liczby)
f = my_filter(lambda x: x%2==0, liczby)

print(f'''
dataset: {liczby}
funkcja my_map: {m}
funkcja my_filter: {f}
''')