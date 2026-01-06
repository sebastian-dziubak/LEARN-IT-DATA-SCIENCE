"""
Zadanie 8 – Porównanie kolekcji
Stwórz te same dane (liczby od 1 do 10) jako listę, krotkę i zbiór. Sprawdź czy 5 należy do
każdej z nich i zmierz czas używając time.time() .
Wymagania:Stwórz 3 kolekcje z tymi samymi danymi
Sprawdź 5 in kolekcja dla każdej
Porównaj (niekoniecznie precyzyjnie) szybkość

"""
import time


my_list = [i for i in range(11)]
my_tuple = tuple(my_list)
my_set = set(my_list)

my_time = []
list_of_elements = [my_list, my_tuple, my_set]
name_of_elements = ['lista', 'krotka', 'zbiór']

for i in list_of_elements:
    start = time.time()
    5 in i
    stop = time.time()
    my_time.append(stop - start)

result = list(zip(name_of_elements, my_time))


print('Czasy szukania liczby 5 w listach, krotkach i zbiorach:')
for i in range(len(result)):
    print(f'\tRodzaj: {(result[i][0]).title()}, czas: {result[i][1]:.2e} sekund')

