"""
Zadanie 17 – Inwersja wielu-do-wielu - słownik z setami
Masz słownik gdzie jeden film może mieć wiele gatunków: {'Film1': ['Akcja', 'Sci-
Fi'], 'Film2': ['Komedia'], ...} . Stwórz odwrotny słownik: {gatunek:
zbiór_filmów} .
Dataset:
filmy_gatunki = {
'Matrix': ['Akcja', 'Sci-Fi'],
'Shrek': ['Komedia', 'Familijny', 'Animacja'],
'Inception': ['Akcja', 'Sci-Fi', 'Thriller'],
'Toy Story': ['Animacja', 'Familijny'],
'Die Hard': ['Akcja', 'Thriller'],
'The Hangover': ['Komedia']
}
Wymagania:
Klucze: gatunki, wartości: zbiory filmów (set!)
Iteruj po filmach i dodawaj do odpowiednich zbiorów
Wypisz każdy gatunek i filmy które do niego należą

"""

filmy_gatunki = {
'Matrix': ['Akcja', 'Sci-Fi'],
'Shrek': ['Komedia', 'Familijny', 'Animacja'],
'Inception': ['Akcja', 'Sci-Fi', 'Thriller'],
'Toy Story': ['Animacja', 'Familijny'],
'Die Hard': ['Akcja', 'Thriller'],
'The Hangover': ['Komedia']
}

filmy = {}

for k, v in filmy_gatunki.items():
    print(f'k {k}, v: {v}')
    for i in v:
        if i not in filmy:
            filmy[i] = set([k])
        else:
            filmy[i].add(k)

print(filmy)