"""Dana tablica ocen (5 studentów x 4 egzaminy):
exams = np.array([
[78, 85, 92, 88],
[65, 72, 68, 70],
[90, 88, 95, 92],[55, 60, 58, 62],
[82, 79, 85, 80]
])
Dodaj bonus do każdego egzaminu: [5, 10, 5, 10]
Następnie pomnóż wyniki każdego studenta przez mnożnik: [1.0, 1.1, 0.95, 1.15, 1.0]
Wymagania:
Użyj broadcastingu (bez pętli)
Wypisz wyniki przed i po"""

import numpy as np

exams = np.array([
    [78, 85, 92, 88],
    [65, 72, 68, 70],
    [90, 88, 95, 92],
    [55, 60, 58, 62],
    [82, 79, 85, 80]
])

bonus = np.array([5, 10, 5, 10])
mnoznik = np.array([1.0, 1.1, 0.95, 1.15, 1.0])

exams_bonus = exams + (bonus.reshape([1,4]))
exams_result = np.round(exams_bonus * mnoznik.reshape([5,1]), 2)

print(f'Wyniki przed:\n{exams}')
print(f'Wyniki po:\n{exams_result}')