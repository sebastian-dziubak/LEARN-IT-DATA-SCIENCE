"""Zadanie 1 – Klasyfikacja liczb parzystych i nieparzystych
Napisz program, który dla listy liczb [12, 7, 23, 45, 8, 19, 34, 56, 91, 2] wyświetli,
które liczby są parzyste, a które nieparzyste. Użyj instrukcji if/else i operatora modulo
%.
Wymagania:
Iteruj po liście używając pętli for
Dla każdej liczby sprawdź: if liczba % 2 == 0
Wyświetl wynik w formacie: "12 - parzysta", "7 - nieparzysta"
Oczekiwany rezultat:
Lista 10 linii z klasyfikacją każdej liczby"""

numbers = [12, 7, 23, 45, 8, 19, 34, 56, 91, 2]

for i in numbers:
    if i % 2 == 0:
        print(f'{i} - parzysta')
    else:
        print(f'{i} - nieparzysta')

# rozwiązanie z LC
print('\nRozwiązanie z LC')
numbers2 = [f'{i} - parzysta' if i % 2 == 0 else f'{i} - nieparzysta' for i in numbers]
for n in numbers2:
    print(n)