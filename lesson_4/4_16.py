"""
Stwórz tekstową reprezentację confusion matrix.
Dane (klasyfikacja binarna):
True Positives: 45
True Negatives: 38
False Positives: 7
False Negatives: 10
Wymagania:
Oblicz accuracy, precision, recall, F1-score
Narysuj confusion matrix używając stringów i formatowania
Użyj wyrównania do stworzenia czytelnej tabeli
Wyświetl metryki pod tabelą

"""

TP = 45
TN = 38
FP = 7
FN = 10

accuracy = (TP + TN) / (TP + TN + FP + FN)
precision = TP / (TP + FP)
recall = TP / (TP + FN)
f1 = (2 * precision * recall) / (precision + recall)

print(f'{"":^5}{"":^5}{"":^5}{"PREDICTED":^10}')
print(f'{"":^5}{"":^5}{"0":^5}{"1":^5}')
print(f'{"ACTUAL":^5}{"0":^5}{TN:^4}{FP:^5}')
print(f' {"":^5}{"1":^5}{FN:^5}{TP:^5}')

print(f'''
TP = {TP}
TN = {TN}
FP = {FP}
FN = {FN}

accuracy = {accuracy:.3f}
precission = {precision:.3f}
recall = {recall:.3f}
f1-score = {f1:.3f}
''')