"""
Zadanie 8 – Ekstakcja informacji ze stringa
Masz nazwę pliku: "model_results_2024_Q3.csv" . Wyciągnij rok i kwartał używając
slicing lub split.

"""

file_name = "model_results_2024_Q3.csv"

year = file_name.split('_')[-2]
quarter = file_name.index('Q')

print(f'''
Rok: {year}
Kwartał: {file_name[quarter + 1]}
''')