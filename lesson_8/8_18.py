'''Zadanie 18 – Funkcja kroswalidacji (podstawowa wersja)
Napisz funkcję k_fold_split(dane, k) , która dzieli dane na k części (foldów) do
walidacji krzyżowej.
Dataset:dane = list(range(1, 101))
# 100 obserwacji
Wymagania:
k = 5 (5-fold cross-validation)
Podziel dane na 5 równych części
Funkcja zwraca listę foldów (każdy fold to lista)
Użyj slicing i comprehensions
Oczekiwany rezultat:
5 foldów po 20 elementów każdy
Fold 1: [1-20], Fold 2: [21-40], ...'''

def k_fold_split(dane, s):
    result = []
    if len(dane) % s == 0:
        split_indeks = (len(dane) // s)
        for i in dane:
            r = dane[:split_indeks]
            result.append(r)
            for x in r:
                dane.remove(x)
        for i, r in enumerate(result, start=1):
            print(f'Fold {i}: {r}')
    else:
        print(f'Nie da się podzielić danych na {s} równych części')


dataset = [x for x in range(1, 101)]
k = 5

k_fold_split(dataset, k)