"""
Zadanie 10 – Walidacja danych ze zbiorem dozwolonych wartości
Masz listę kategorii od użytkowników: ['sport', 'muzyka', 'SPORT', 'film', 'xyz',
'nauka', 'gaming'] . Dozwolone kategorie to {'sport', 'muzyka', 'film', 'nauka',
'gry'} . Znajdź nieprawidłowe kategorie (uwzględnij wielkość liter - konwertuj na małe).
Wymagania:
Konwertuj wszystkie kategorie na małe litery
Użyj operacji zbiorowych by znaleźć nieprawidłowe
Wypisz prawidłowe i nieprawidłowe osobno

"""

categories = ['sport', 'muzyka', 'SPORT', 'film', 'xyz', 'nauka', 'gaming']
apr_categories = {'sport', 'muzyka', 'film', 'nauka', 'gry'}

for i in range(len(categories)):
    categories[i] = categories[i].lower()

set_categories = set(categories)

print('Dozwolone kategorie: ', end='')
for i in apr_categories:
    print(f'{i}', end=', ')

print('\n\nNiedozwolone kategorie: ', end='')
for i in (set_categories - apr_categories):
    print(f'{i}', end=', ')
