"""
Zadanie 9 – Normalizacja Min-Max
Znormalizuj wartość do zakresu [0, 1].
Dane:
Wartość: 75Minimum w kolumnie: 50
Maximum w kolumnie: 100
Wymagania:
Wzór: normalized = (value - min) / (max - min)
Oblicz dla wartości 75, 50, 100, 62.5
Sprawdź, czy wynik mieści się w [0, 1]
Wyświetl tabelkę: wartość oryginalna | wartość znormalizowana

"""

values = [75, 50, 100, 62.5]
value_normalized = []
value_in = []
min = 50
max = 100

for value in values:
    normalized = (value - min) / (max - min)
    value_normalized.append(normalized)
    if 0 <= normalized <= 1:
        value_in.append("TAK")
    else:
        value_in.append("NIE")

print(f'{"Wartość oryginalna":<10}  | {"Wartość znormalizowana":<10} | {"Czy mieści się w [0, 1]":<10}')
for i in range(len(values)):
    print('-' * 70)
    print(f'{values[i]:^20}|  {value_normalized[i]:^20}  | {value_in[i]:^20}')
print('-' * 70)
