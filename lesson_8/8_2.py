"""Zadanie 2 – Konwerter jednostek
Napisz trzy funkcje: celsius_to_fahrenheit(c) , fahrenheit_to_celsius(f) ,
celsius_to_kelvin(c) .
Dataset:
Temperatury w Celsius: [0, 10, 20, 30, 37, 100]
Wymagania:
Każda funkcja zwraca skonwertowaną wartość
Zastosuj funkcje do konwersji wszystkich temperatur
Oczekiwany rezultat:
Tabela z trzema kolumnami: °C, °F, K"""


def celsius_to_fahrenheit(c):
    result = round((c * (9/5) + 32), 2)
    return result

def fahrenheit_to_celsius(f):
    result = round((f - 32) * (5/9), 2)
    return result

def celsius_to_kelvin(c):
    result = round((c + 273.15), 2)
    return result


temp_c = [0, 10, 20, 30, 37, 100]

print(f'°C\t\t °F\t\t\t K')
for i in temp_c:
    print(f'{i}\t\t {celsius_to_fahrenheit(i)}\t\t {celsius_to_kelvin(i)}')

print(f'\n\n ** DRUGIE ROZWIĄZANIE **\n')

temp_c = [0, 10, 20, 30, 37, 100]
temp_f = list(map(lambda f: f * 9/5 + 32, temp_c))
temp_k = list(map(lambda k: k + 273.15, temp_c))
opisy = ['°C', '°F', 'K']

print(f'°C\t\t °F\t\t\t K')
for c, f, k in zip(temp_c, temp_f, temp_k):
    print(f'{c}\t\t  {f}\t\t {k}')

