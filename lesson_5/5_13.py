"""
Zadanie 13 – Analiza Iris dataset
Użyj danych Iris z sekcji "Praca z Prawdziwymi Danymi". Dla każdego gatunku oblicz:
Średnią długość płatka (petal_length)
Maksymalną szerokość płatka (petal_width)
Stosunek długości płatka do szerokości
Wyświetl wyniki w czytelnym formacie tabelarycznym używając f-strings z wyrównaniem.

"""
from numpy.ma.core import maximum

iris_data_raw = """5.1,3.5,1.4,0.2,setosa
4.9,3.0,1.4,0.2,setosa
4.7,3.2,1.3,0.2,setosa
4.6,3.1,1.5,0.2,setosa
5.0,3.6,1.4,0.2,setosa
7.0,3.2,4.7,1.4,versicolor
6.4,3.2,4.5,1.5,versicolor
6.9,3.1,4.9,1.5,versicolor
5.5,2.3,4.0,1.3,versicolor
6.5,2.8,4.6,1.5,versicolor
6.3,3.3,6.0,2.5,virginica
5.8,2.7,5.1,1.9,virginica
7.1,3.0,5.9,2.1,virginica
6.3,2.9,5.6,1.8,virginica
6.5,3.0,5.8,2.2,virginica"""

column_names = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species']
unique_species = []
result_names = ['max szerokość płatka', 'śr. długość płatka', 'stosunek dł. do szer. płatka']
data = {}
result = {}

lines = iris_data_raw.strip().split('\n')

for line in lines:
    values = line.split(',')
    if values[4] not in data.keys():
        unique_species.append(values[4])
        data[values[4]] = {column_names[3]: [(float(values[3]))],
                           column_names[2]: [(float(values[2]))]}
    elif values[4] in data.keys():
        data[values[4]][column_names[3]].append(float(values[3]))
        data[values[4]][column_names[2]].append(float(values[2]))

for i in unique_species:
    result[i] = []

for key, value in data.items():
    for i in unique_species:
        if key == i:
            maximum = max(value['petal_width'])
            mean_len = sum(value['petal_length']) / len(value['petal_length'])
            mean_wid = sum(value['petal_width']) / len(value['petal_width'])
            len_wid = mean_len / mean_wid
            result[i].append(maximum)
            result[i].append(mean_len)
            result[i].append(len_wid)

print(result)

print(f'''
{'RAPORT':<20} {unique_species[0].title():>20} {unique_species[1].title():>20} {unique_species[2].title():>20}
{result_names[0].title():<25} {result[unique_species[0]][0]:>15} {result[unique_species[1]][0]:>20} {result[unique_species[2]][0]:>20}
{result_names[1].title():<25} {result[unique_species[0]][1]:>15} {result[unique_species[1]][1]:>20} {result[unique_species[2]][1]:>20}
{result_names[2].title():<25} {result[unique_species[0]][2]:>12.2f} {result[unique_species[1]][2]:>20.2f} {result[unique_species[2]][2]:>20.2f}
''')
