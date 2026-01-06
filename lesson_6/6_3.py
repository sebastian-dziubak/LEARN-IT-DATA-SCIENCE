"""
Zadanie 3 – Liczenie wystąpień słów
Masz listę słów: ['python', 'java', 'python', 'javascript', 'python', 'java',
'c++', 'python'] . Policz ile razy każde słowo występuje używając słownika.
Wymagania:
Użyj pętli i metody .get()
Wypisz wyniki
Oczekiwany wynik:
Słownik z częstościami: {'python': 4, 'java': 2, ...}

"""

lst = ['python', 'java', 'python', 'javascript', 'python', 'java', 'c++', 'python']
dict = {}

for i in lst:
    dict[i] = dict.get(i, 0) + 1

print(dict)