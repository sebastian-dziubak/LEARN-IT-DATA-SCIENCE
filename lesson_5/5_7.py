"""
Zadanie 7 – Zliczanie wystąpień
Masz listę predykcji: ['spam', 'ham', 'spam', 'spam', 'ham', 'ham', 'spam'] .
Policz ile jest 'spam' i ile 'ham' używając metody count() .

"""

my_list = ['spam', 'ham', 'spam', 'spam', 'ham', 'ham', 'spam']

uniqe_list = set(my_list)

for name in uniqe_list:
    print(f'ilość "{name}": {my_list.count(name)}')
