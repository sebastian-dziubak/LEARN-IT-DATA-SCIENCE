"""
Zadanie 16 – Confusion Matrix z list
Masz listę prawdziwych etykiet i predykcji:
y_true = [1, 0, 1, 1, 0, 1, 0, 0, 1, 0]
y_pred = [1, 0, 1, 0, 0, 1, 0, 1, 1, 0]
Oblicz TP, TN, FP, FN używając pętli i warunków. Następnie oblicz accuracy, precision,
recall.

"""

y_true = [1, 0, 1, 1, 0, 1, 0, 0, 1, 0]
y_pred = [1, 0, 1, 0, 0, 1, 0, 1, 1, 0]

names = ['TP', 'TN', 'FP', 'FN']
matrix = {}

for i in names:
    matrix[i] = 0

for i in range(len(y_true)):
    if y_true[i] == 1 and y_pred[i] == 1:
        matrix['TP'] += 1
    elif y_true[i] == 0 and y_pred[i] == 0:
        matrix['TN'] += 1
    elif y_true[i] == 1 and y_pred[i] == 0:
        matrix['FP'] += 1
    else:
        matrix['FN'] += 1

accuracy = (matrix['TP'] + matrix['TN']) / (matrix['TP'] + matrix['FN'] + matrix['FP'] + matrix['TN'])
precision = matrix['TP'] / (matrix['TP'] + matrix['FP'])
recall = matrix['TP'] / (matrix['TP'] + matrix['FN'])

for k, v in matrix.items():
    print(f'{k} = {v}')

print(f'''
Accuracy: {accuracy:.2%}
Precision: {precision:.2%}
Recall: {recall:.2%}
''')