"""
Zadanie 17 – Czyszczenie danych CSV
Masz surowe linie CSV z błędami:
csv_lines = [
"id,name,age,city",
"1,Alice,28, New York
"2, Bob ,, Boston",
"3,Charlie,35,",
"4,Diana,29,Chicago"
]
",
Wyczyść dane:
Usuń białe znaki z wartości
Zamień puste wartości na "Unknown"
Zbuduj listę słowników (każda linia = słownik)

"""
from contourpy.types import point_dtype

csv_lines = [
    "id,name,age,city",
    "1,Alice,28, New York ",
    "2, Bob ,, Boston",
    "3,Charlie,35,",
    "4,Diana,29,Chicago"
]

names = csv_lines[0].split(',')
result = []
data = []

my_lines = csv_lines[::]
my_lines.remove(my_lines[0])
for i in my_lines:
    for j in i.split(','):
        if len(j) == 0:
            j = "Unknown"
        result.append(j.strip())

for i in range(0, len(result), len(names)):
    data.append((dict(zip(names, result[i:i + len(names)]))))

for i in data:
    print(i)