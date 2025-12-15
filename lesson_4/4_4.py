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

raw_name = " PATIENT_age_YEARS "

new_name = raw_name.strip().title().replace("_", " ")

print(new_name)