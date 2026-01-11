"""
Masz sekwencję stanów systemu: ["A", "B", "A", "A", "C", "B", "C", "A", "B",
"B"] . Oblicz macierz przejść: ile razy stan X przechodzi w stan Y.
Dataset:Lista stanów (sekwencja)
Wymagania:
Zidentyfikuj unikalne stany
Utwórz strukturę do przechowywania przejść (np. słownik słowników)
Pętla: dla i od 0 do len-2: zlicz przejście z stany[i] do stany[i+1]
Wyświetl macierz przejść w formacie tabelarycznym
Oczekiwany rezultat:
Macierz przejść (np. A→A: 1, A→B: 1, A→C: 1, B→A: 2, etc.)

"""

matrix = ["A", "B", "A", "A", "C", "B", "C", "A", "B", "B", "A", "A", "C", "C", "A", "B", "A", "A", "B", "A", "C"]
matrix_set = sorted(set(matrix))
result = {}

for m in matrix_set:
    for n in matrix_set:
        result[f'{m}{n}'] = 0

for i in range(0, len(matrix) - 1):
    result[f'{matrix[i]}{matrix[i+1]}'] += 1

for k, v in result.items():
    print(f'{k[0]} → {k[1]}: {v}')