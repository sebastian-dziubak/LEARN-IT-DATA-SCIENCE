"""
Masz dane: wartosci = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100] . Znormalizuj je
do zakresu [0, 1] używając Min-Max scaling: x_norm = (x - min) / (max - min) .
Dataset:
Lista wartości
Wymagania:
Znajdź minimum i maksimum używając pętli (bez min() / max() )
Dla każdej wartości oblicz x_norm
Zapisz znormalizowane wartości do nowej listy
Sprawdź: minimum powinno być 0.0, maksimum 1.0
Oczekiwany rezultat:
Lista znormalizowanych wartości [0.0, 0.111, 0.222, ..., 1.0]
Weryfikacja zakresu [0, 1]

"""

numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
maximum = numbers[0]
minimum = numbers[0]
numbers_norm = []

for i in numbers:
    if i > maximum:
        maximum = i
    if i < minimum:
        minimum = i
    if i == numbers[-1]:
        break

for i in numbers:
    i_norm = round((i - minimum) / (maximum - minimum), 2)
    numbers_norm.append(i_norm)


print(f'Lista znormalizowanych wartości:\n{numbers_norm}')
print(f'Weryfikacja zakresu [{min(numbers_norm)}, {max(numbers_norm)}]')