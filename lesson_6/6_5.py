"""
Zadanie 5 – Usuwanie duplikatów z listy
Masz listę z duplikatami: [1, 2, 3, 2, 4, 1, 5, 3, 6, 4, 7] . Usuń duplikaty używając
zbioru i przekonwertuj z powrotem na listę. Wypisz obie listy i porównaj długości.
Wymagania:
Użyj set() do usunięcia duplikatów
Wypisz przed i po

"""

lst = [1, 2, 3, 2, 4, 1, 5, 3, 6, 4, 7]

lst_uniqe = list(set(lst))

print(f'''
Lista oryginalna: {lst}
długość: {len(lst)}

Lista bez duplikatów: {lst_uniqe}
długość: {len(lst_uniqe)}
''')