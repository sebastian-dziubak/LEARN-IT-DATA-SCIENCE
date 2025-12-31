"""
Zadanie 5 – Parsing ścieżki pliku
Wyodrębnij informacje ze ścieżki do pliku.
Dane:
Ścieżka: "data/processed/train_fold_03_normalized.csv"
Wymagania:
Wyodrębnij: folder, typ zbioru (train/test), numer fold, format pliku
Użyj metod split() i indeksowania
Wyświetl każdą informację osobno

"""

path = "data/processed/train_fold_03_normalized.csv"

splitted_path = path.split('/')

folder_list = [splitted_path[0], splitted_path[1]]
folder = '/'.join(folder_list)

type_list = splitted_path[2]
working_list = type_list.split('_')
typ = working_list[0]
fold_number = working_list[2]
reszta, format_pliku = working_list[-1].split(".")

print(f'Ścieżka pliku: {path}\n')
print(f'Folder: {folder}')
print(f'Typ zbioru: {typ}')
print(f'Numer fold: {fold_number}')
print(f'Format pliku: {format_pliku}')

