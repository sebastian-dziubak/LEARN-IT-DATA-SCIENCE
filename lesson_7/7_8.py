"""Zadanie 8 – Konwersja listy używając list comprehension
Masz listę wzrostów w centymetrach: [165, 178, 182, 159, 171, 190] . Przekonwertuj
je na metry używając list comprehension.
Wymagania:
wzrosty_metry = [wzrost / 100 for wzrost in wzrosty_cm]
Wyświetl obie listy
Oczekiwany rezultat:
Lista wzrostów w metrach: [1.65, 1.78, 1.82, 1.59, 1.71, 1.90]"""

wzrosty_cm = [165, 178, 182, 159, 171, 190]

wzrosty_metry = [wzrost / 100 for wzrost in wzrosty_cm]

print(f'''
wzrosty w centymentrach: {wzrosty_cm}
wzrosty w metrach: {wzrosty_metry}
''')