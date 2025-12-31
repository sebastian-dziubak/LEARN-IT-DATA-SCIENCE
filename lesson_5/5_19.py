"""
Zadanie 19 – Generowanie raportu markdown
Masz dane eksperymentów:
experiments = [
{'name': 'Exp_01', 'accuracy': 0.85, 'precision': 0.83, 'recall':
0.87},
{'name': 'Exp_02', 'accuracy': 0.89, 'precision': 0.88, 'recall':
0.90},
{'name': 'Exp_03', 'accuracy': 0.87, 'precision': 0.85, 'recall':
0.89}
]
Wygeneruj raport w formacie markdown z tabelą:
| Experiment | Accuracy | Precision | Recall |
|------------|----------|-----------|--------|
| Exp_01     | 85.00%   | 83.00%    | 87.00% |
...
Użyj list comprehension i join.

"""

experiments = [
{'name': 'Exp_01', 'accuracy': 0.85, 'precision': 0.83, 'recall': 0.87},
{'name': 'Exp_02', 'accuracy': 0.89, 'precision': 0.88, 'recall': 0.90},
{'name': 'Exp_03', 'accuracy': 0.87, 'precision': 0.85, 'recall': 0.89}
]

header = f'''
| Experiment | Accuracy | Recision | Recall |
|------------|----------|----------|--------|'''

rows = "".join([f'''
| {e['name']:^10} | {e['accuracy']:^8.2%} | {e['precision']:^8.2%} | {e['recall']:.2%} | '''
for e in experiments])

report = f'{header}{rows}'
print(report)