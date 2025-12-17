"""Zadanie 13 – Detekcja anomalii prostą metodą
Wykryj wartości odstające używając reguły 3-sigma.
Dane (5 pomiarów ciśnienia krwi):
120, 125, 118, 190, 122 mmHg
Wymagania:
Oblicz średnią i odchylenie standardowe (ręcznie, bez bibliotek)Zidentyfikuj wartości, które odchylają się o więcej niż 3×std od średniej
Oznacz je jako anomalie
Wyświetl raport z wszystkimi wartościami i oznaczeniem anomalii"""

data = [120, 125, 118, 190, 122]
mean = sum(data) / len(data)
std_list = []
for x in data:
    std_list.append((x - mean) ** 2)

std = (sum(std_list) / len(std_list)) ** (1/2)
boundary_low = mean - (3 * std)
boundary_high = mean + (3 * std)

for x in data:
    print(f'Wartość: {x} - ', end="")
    if boundary_low < x < boundary_high:
        print('OK')
    else:
        print("ANOMALIA!")