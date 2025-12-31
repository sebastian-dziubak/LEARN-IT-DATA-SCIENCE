"""
Zadanie 2 – Dodawanie elementów do listy
Zacznij od pustej listy results = [] . Dodaj do niej 5 wartości accuracy: 0.75, 0.82, 0.79,
0.85, 0.88. Następnie:
Wyświetl długość listy
Wyświetl średnią wartość
Wyświetl maksymalną wartość

"""

results = []

accuracy = [0.75, 0.82, 0.79, 0.85, 0.88]
results.extend(accuracy)

length = len(results)
print(f'Długość listy: {length}')

mean = sum(results) / length
print(f'Średnia wartość: {mean:.2%}')

print(f'Maksymalna wartość: {max(results):.2%}')