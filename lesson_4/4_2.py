"""
Zadanie 2 – Konwersja temperaturNapisz program konwertujący temperatury Celsius na Fahrenheit i Kelvin.
Dane:
Temperatura: 23.5°C
Wymagania:
Fahrenheit = Celsius × 9/5 + 32
Kelvin = Celsius + 273.15
Wyświetl wszystkie 3 wartości sformatowane z 1 miejscem po przecinku

"""

temp_c = 23.5
temp_f = temp_c * 9/5 + 32
temp_k = temp_c + 273.15

print(f'{temp_c:.1f}°C = {temp_f:.1f}°F = {temp_k:.1f} K')