"""
Zadanie 4 – Formatowanie nazw kolumn
Ustandaryzuj nazwę kolumny z datasetu.
Dane:
Nazwa raw: " PATIENT_age_YEARS "
Wymagania:
Usuń białe znaki
Zamień na małe literyZastąp _ przez " "
Użyj title case

"""

print('*** STANDARYZACJA NAZW KOLUMN ***\n')
raw_name = input('Podaj nazwę kolumny do ustandaryzowania: ')

new_name = raw_name.strip().title().replace("_", " ")

print(f'Stara nazwa kolumny: "{raw_name}"')
print(f'Ustandaryzowana nazwa kolumny: "{new_name}"')