"""
Zadanie 3 – Sortowanie listy
Masz listę wyników: [0.78, 0.92, 0.85, 0.88, 0.81] . Posortuj ją malejąco i wyświetl 3
najlepsze wyniki.

"""

lst = [0.78, 0.92, 0.85, 0.88, 0.81]
lst.sort()
print(f'Najlepsze wyniki: {lst[-1]:.2%}, {lst[-2]:.2%}, {lst[-3]:.2%}')