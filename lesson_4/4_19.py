"""
Zadanie 19 – Kalkulator accuracy z threshold-em
Oblicz accuracy dla różnych progów klasyfikacji.
Dane (prawdopodobieństwa i prawdziwe etykiety):
Prawdopodobieństwa: 0.23, 0.67, 0.89, 0.34, 0.91, 0.12, 0.78, 0.45
Prawdziwe klasy: 0, 1, 1, 0, 1, 0, 1, 0
Wymagania:
Dla threshold = 0.5: jeśli prob >= 0.5 → klasa 1, inaczej klasa 0
Porównaj predykcje z prawdziwymi klasami
Oblicz accuracy = (liczba poprawnych) / (liczba wszystkich)
Powtórz dla threshold = 0.3, 0.5, 0.7
Wyświetl accuracy dla każdego threshold i wskaż optymalny

"""

probability = [0.23, 0.67, 0.89, 0.34, 0.91, 0.12, 0.78, 0.45]
real_class = [0, 1, 1, 0, 1, 0, 1, 0]
threshold = [0.3, 0.5, 0.7]
predictions = {}
threshold_accuracy = {}
final_accuracy = []
suma = 0

for i in threshold:
    predictions[i] = []
    threshold_accuracy[i] = []

for t in threshold:
    for i in probability:
        if i >= t:
            predictions[t].append(1)
        else:
            predictions[t].append(0)


for key, value in predictions.items():
    for i in range(len(real_class)):
        if real_class[i] == predictions[key][i]:
            threshold_accuracy[key].append(1)

for value in threshold_accuracy.values():
    final_accuracy.append((len(value) / len(real_class)))

print('*** RAPORT ***')
for i in range(len(threshold)):
    print(f'Threshold: {threshold[i]}, accuracy: {final_accuracy[i]:.3f}')
