"""Zadanie 6 – Filtrowanie listy z warunkiem
Masz listę temperatur ciała: [36.5, 37.8, 36.2, 38.5, 36.9, 39.2, 37.0] . Wyświetl
tylko te pomiary, które wskazują gorączkę (temperatura >= 38.0°C).
Wymagania:
Pętla for po liście
Instrukcja if temperatura >= 38.0:
Wyświetl temperaturę z ostrzeżeniem
Oczekiwany rezultat:
Lista temperatur >= 38.0 z komunikatem 'Gorączka'"""

temp = [36.5, 37.8, 36.2, 38.5, 36.9, 39.2, 37.0]

for i in temp:
    if i >= 38.0:
        print(f'Temperatura: {i} °C - Gorączka')

#LC
temp2 = [f'{x} °C - Gorączka' for x in temp if x >= 38.0]
for i in temp2:
    print('Temperatura:', i)