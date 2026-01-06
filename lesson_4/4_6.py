"""
Zadanie 6 – Dokładność w procentach
Sformatuj metryki modelu.
Dane:
Accuracy: 0.9234
Precision: 0.8891
Recall: 0.9456
Wymagania:
Wyświetl każdą metrykę w procentach z 2 miejscami po przecinku
Użyj f-strings z formatowaniem :.2%
Dodaj estetyczne wyrównanie kolumn

"""

accuracy = 0.9234
precision = 0.8891
recall = 0.9456

print(f'{"Nazwa metryki":<15}', "Wartość liczbowa")
print('-'*33)
print(f'{"Accuracy":<10} {accuracy:>15.2%}')
print(f'{"Precision":<10} {precision:>15.2%}')
print(f'{"Recall":<10} {recall:>15.2%}')