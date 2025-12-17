"""
Zadanie 14 – Generowanie nazw plików dla cross-validation
Wygeneruj nazwy plików dla k-fold cross-validation.
Dane:
Dataset: "iris"
Liczba folds: 5
Typy: train, test
Wymagania:
Użyj pętli for (zakres od 1 do k)
Generuj nazwy w formacie: iris_fold_01_train.csv
Numeracja z zerem wiodącym (01, 02, ..., 05)
Wyświetl wszystkie nazwy (10 plików total)

"""

dataset = 'iris'
folds = 5
type_list = ['train', 'test']

for x in type_list:
    for y in range(folds):
        print(f'{dataset.lower()}_fold_{y+1:02d}_{x.lower()}.csv')
