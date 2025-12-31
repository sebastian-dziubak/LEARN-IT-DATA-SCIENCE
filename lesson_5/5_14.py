"""
Zadanie 14 – Ranking modeli
Masz listę wyników modeli:
models = [
('LogisticRegression', 0.78, 1.2),
('RandomForest', 0.92, 45.6),
('SVM', 0.85, 12.3),
('XGBoost', 0.95, 67.8)
]
# Format: (nazwa, accuracy, czas_treningu_s)
Stwórz ranking modeli według "efficiency score" = accuracy / log10(czas). Posortuj
malejąco i wyświetl top 3.

"""
from cgi import print_environ_usage

# Format: (nazwa, accuracy, czas_treningu_s)
models = [
    ('LogisticRegression', 0.78, 1.2),
    ('RandomForest', 0.92, 45.6),
    ('SVM', 0.85, 12.3),
    ('XGBoost', 0.95, 67.8)
]
score = []
for i in models:
    import math
    eff_score = round(i[1] / (math.log10(i[2])), 2)
    score.append((i[0], eff_score))

sorted_score = sorted(score, key=lambda score: score[1], reverse=True)
sorted_score.pop()

print('Trzy najlepsze modele - efficiency score')
for i in sorted_score:
    print(f'{i[0]}: {i[1]}')


