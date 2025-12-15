"""
Zadanie 3 – Podział zbioru danych
Oblicz rozmiary zbiorów treningowego, walidacyjnego i testowego.
Dane:
Całkowita liczba próbek: 1000
Proporcje: 70% trening, 15% walidacja, 15% test
Wymagania:
Użyj mnożenia i dzielenia całkowitego
Upewnij się, że suma = 1000 (obsłuż resztę z dzielenia)
Wyświetl rozmiary wszystkich zbiorów

"""

calkowita_liczba_probek = 1000
zbior_treningowy = calkowita_liczba_probek * 70 // 100
zbior_walidacyjny = calkowita_liczba_probek * 15 // 100
zbior_testowy = calkowita_liczba_probek * 15 // 100


print(f'Całkowita liczba próbek: {calkowita_liczba_probek}')
print(f'Zbiór testowy: {zbior_testowy}')
print(f'Zbiór treningowy: {zbior_treningowy}')
print(f'Zbiór walidacyjny: {zbior_walidacyjny}')
print(f'Czy suma zbiorów = {calkowita_liczba_probek}: {calkowita_liczba_probek == zbior_testowy + zbior_treningowy + zbior_walidacyjny}')
