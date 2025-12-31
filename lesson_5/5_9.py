"""
Zadanie 9 – Filtrowanie outlierów
Masz listę pomiarów: [23, 24, 22, 150, 23, 25, -10, 24, 23] . Outlierem jest wartość
poza zakresem [20, 30]. Stwórz nową listę bez outlierów używając list comprehension.

"""

pomiary = [23, 24, 22, 150, 23, 25, -10, 24, 23]

new_list = [i for i in pomiary if 30 >= i >= 20]

print(f'''
Nowa lista bez outlinerów:
{new_list}
''')