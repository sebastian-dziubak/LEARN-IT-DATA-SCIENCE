"""
Zadanie 7 – Porównanie dwóch modeli
Określ, który model jest lepszy.Dane:
Model A: accuracy = 0.87, train time = 120s
Model B: accuracy = 0.89, train time = 450s
Wymagania:
Porównaj accuracy (różnica > 0.02 jest znacząca)
Porównaj czas treningu
Użyj operatorów logicznych do określenia "najlepszego kompromisu"
Wyświetl rekomendację

"""

acc_a = 0.87
acc_b = 0.89
train_time_a = 120
train_time_b = 450

diff = abs(acc_a - acc_b)

if round(diff, 2) <= 0.02:
    if train_time_a < train_time_b:
        recomendation = "Modele mają podobną zbieżność. Model A ma krótszy czas treningu. Wybrano model A"
    else:
        recomendation = "Modele mają podobną zbieżność. Model B ma krótszy czas treningu. Wybrano model B"
else:
    if acc_a > acc_b:
        recomendation = "Model A ma większą zbieżność. Wybieram model A"
    else:
        recomendation = "Model B ma większą zbieżność. Wybieram model B"

print(f'''
Model A:
* accuracy: {acc_a * 100} %
* train time: {train_time_a} s

Model B:
* accuracy: {acc_b * 100} %
* train time: {train_time_b} s
''')
print(f'Rekomendacja: {recomendation}')