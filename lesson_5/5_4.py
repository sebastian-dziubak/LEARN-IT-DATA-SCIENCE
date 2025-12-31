"""
Zadanie 4 – Czyszczenie nazw kolumn
Masz listę nazw kolumn: [" Customer ID ", "TOTAL AMOUNT", " date "] . Wyczyść je
zgodnie z konwencją:
Usuń białe znaki (strip)
Zamień na małe litery (lower)
Zamień spacje na podkreślniki (replace)

"""

columns_name = [" Customer ID ", "TOTAL AMOUNT", " date "]
new_colums = []

for column in columns_name:
    new_colums.append(column.strip().lower().replace(' ', '_'))

print(new_colums)