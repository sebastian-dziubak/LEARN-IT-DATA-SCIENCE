"""
Zadanie 1 – Tworzenie i indeksowanie listy
Stwórz listę zawierającą pomiary temperatury z 7 dni: [22.5, 23.0, 21.5, 24.0, 23.5,
22.0, 23.0] . Wyświetl:
Temperaturę z pierwszego dnia
Temperaturę z ostatniego dnia
Temperatury z trzech środkowych dni (slicing)

"""

temperature = [22.5, 23.0, 21.5, 24.0, 23.5, 22.0, 23.0]

print(f'Temperatura w pierwszym dniu: {temperature[0]}')
print(f'Temperatura w ostatnim dniu: {temperature[-1]}')

middle_index = len(temperature) // 2

print(f'Temperatura z trzech środkowych dni: '
      f'{temperature[middle_index - 1]}, '
      f'{temperature[middle_index]}, '
      f'{temperature[middle_index +1]}')