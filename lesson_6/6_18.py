"""
Zadanie 18 – Analiza podobieństwa zestawów produktów - Jaccard similarityMasz 3 koszyki zakupów (zbiory produktów). Oblicz podobieństwo Jaccarda między każdą
parą koszyków. Jaccard = |A ∩ B| / |A ∪ B|
Dataset:
koszyk1 = {'mleko', 'chleb', 'masło', 'jajka', 'ser'}
koszyk2 = {'mleko', 'chleb', 'dżem', 'jogurt', 'ser'}
koszyk3 = {'woda', 'sok', 'chipsy', 'czekolada'}
Wymagania:
Napisz funkcję jaccard_similarity(set1, set2) zwracającą podobieństwo (0-1)
Oblicz dla wszystkich par: (1,2), (1,3), (2,3)
Interpretuj wyniki (0 = brak wspólnych, 1 = identyczne)
Oczekiwany wynik:
Podobieństwa między koszykami
Interpretacja: które koszyki są najbardziej podobne?
"""


koszyk1 = {'mleko', 'chleb', 'masło', 'jajka', 'ser'}
koszyk2 = {'mleko', 'chleb', 'dżem', 'jogurt', 'ser'}
koszyk3 = {'woda', 'sok', 'chipsy', 'czekolada'}

def jaccard_similarity(set1, set2):
    return len(set1 & set2) / len(set1 | set2)

k12 = jaccard_similarity(koszyk1, koszyk2)
k13 = jaccard_similarity(koszyk1, koszyk3)
k23 = jaccard_similarity(koszyk2, koszyk3)

koszyki = [k12, k13, k23]

print(f'''
Prawdopodobieństwo koszyków:
Koszyk 1 i 2: {k12:.2f}
Koszyk 1 i 3: {k13:.2f}
Koszyk 2 i 3: {k23:.2f}

Koszyki 1 i 2 są najbardziej podobne
''')
