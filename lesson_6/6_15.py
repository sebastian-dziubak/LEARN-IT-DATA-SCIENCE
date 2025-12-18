"""
Zadanie 15 – Znajdowanie przecięć i różnic w zbiorach danych
Masz 3 zbiory użytkowników którzy odwiedzili stronę w różnych dniach. Znajdź:
użytkowników którzy byli wszystkie 3 dni, tylko jeden dzień, dokładnie 2 dni.
Dataset:
dzien1 = {'user001', 'user002', 'user003', 'user004', 'user005',
'user010'}
dzien2 = {'user002', 'user003', 'user006', 'user007', 'user008',
'user010'}
dzien3 = {'user003', 'user004', 'user009', 'user010', 'user011'}
Wymagania:
Użyj operacji zbiorowych
Znajdź użytkowników aktywnych wszystkie 3 dni
Znajdź użytkowników tylko w 1 dniu (w każdym dniu osobno)
Znajdź użytkowników w dokładnie 2 dniach
Oczekiwany wynik:
Zestawienie użytkowników według liczby dni aktywności
Szczegółowy raport

"""

dzien1 = {'user001', 'user002', 'user003', 'user004', 'user005', 'user010'}
dzien2 = {'user002', 'user003', 'user006', 'user007', 'user008', 'user010'}
dzien3 = {'user003', 'user004', 'user009', 'user010', 'user011'}

three_days = dzien1 & dzien2 & dzien3

one_day1 = dzien1 - (dzien2 | dzien3)
one_day2 = dzien2 - (dzien1 | dzien3)
one_day3 = dzien3 - (dzien1 | dzien2)
one_day = one_day1 | one_day2 | one_day3

two_day1 = ((dzien1 & dzien2) - dzien3)
two_day2 = ((dzien1 & dzien3) - dzien2)
two_day3 = ((dzien2 & dzien3) - dzien1)
two_days = two_day1 | two_day2 | two_day3

print(f'''
Użytkownicy co byli 3 dni: {three_days}
Użytkownicy co byli 2 dni: {two_days}
Użytkownicy co byli 1 dzień: {one_day}
''')
