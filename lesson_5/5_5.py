"""
Zadanie 5 – Parsowanie CSV
Masz string CSV: "Alice,28,Data Scientist,75000" . Użyj split(',') aby wyciągnąć:
Imię
Wiek (jako int)
Zawód
Pensję (jako int)
Wyświetl te informacj

"""

my_string = "Alice,28,Data Scientist,75000"

name, age, profession, salary = my_string.split(',')

print(f'{name} ma {age} lat, pracuje jako {profession} i zarabia ${salary}')