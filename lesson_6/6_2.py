"""
Zadanie 2 – Dodawanie i usuwanie elementów ze słownika
Masz słownik z produktami i cenami: {'jabłko': 3.50, 'banan': 2.20, 'pomarańcza':
4.00} . Dodaj nowy produkt 'gruszka': 3.80 , usuń 'banan' , zmień cenę jabłka na
3.20 i wypisz zaktualizowany słownik.
Wymagania:
Użyj odpowiednich operacji na słowniku
Wypisz słownik przed i po zmianach

"""

dict = {'jabłko': 3.50, 'banan': 2.20, 'pomarańcza': 4.00}

print(f'Słownik przed zmianami:\n{dict}')

dict['gruszka'] = 3.80
del dict['banan']
dict['jabłko'] = 3.20

print(f'Słownik po zmianach:\n{dict}')