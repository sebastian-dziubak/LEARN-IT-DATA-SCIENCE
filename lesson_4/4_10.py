"""
Zadanie 10 – Budowanie raportu modelu
Stwórz sformatowany raport wyników.
Dane:
Nazwa modelu: "XGBoost Classifier"
Dataset: "Credit Card Fraud"
Liczba próbek: 284807
Accuracy: 0.9991
Precision: 0.8876
Recall: 0.7561
F1-Score: oblicz ze wzoru 2×(precision×recall)/(precision+recall)
Wymagania:
Użyj f-strings do budowy raportu
Zastosuj wyrównanie kolumn
Liczba próbek z separatorem tysięcy
Metryki w procentach z odpowiednią precyzją
Raport w ramce z linii =

"""

name = "XGBoost Classifier"
dataset = "Credit Card Fraud"
samples = 284807
accuracy = 0.9991
precision = 0.8876
recall = 0.7561

f1_score = 2 * (precision * recall) / (precision + recall)

print(f'=' * 44)
print(f'{"Nazwa":^20} | {"Wartość":^20}|')
print(f'=' * 44)
print(f'{"Nazwa modelu":^20} | {name:^20}|')
print(f'=' * 44)
print(f'{"Dataset":^20} | {dataset:^20}|')
print(f'=' * 44)
print(f'{"Liczba próbek":^20} | {samples:^20}|')
print(f'=' * 44)
print(f'{"Accuracy":^20} | {accuracy:^20.2%}|')
print(f'=' * 44)
print(f'{"Precyzja":^20} | {precision:^20.2%}|')
print(f'=' * 44)
print(f'{"Recall":^20} | {recall:^20.2%}|')
print(f'=' * 44)
print(f'{"F1 SCORE":^20} | {f1_score:^20.2%}|')
print(f'=' * 44)