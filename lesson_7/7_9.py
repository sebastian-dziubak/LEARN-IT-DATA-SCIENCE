"""Zadanie 9 – Kategorie BMI dla listy pacjentów
Masz dane pacjentów: wagi = [70, 85, 62, 95, 78] (kg) i wzrosty = [1.75, 1.80,
1.65, 1.78, 1.72] (m). Oblicz BMI dla każdego i sklasyfikuj (niedowaga < 18.5, norma
18.5-24.9, nadwaga >= 25).
Dataset:
Listy równoległe: wagi i wzrosty
Wymagania:
Użyj pętli for i in range(len(wagi)):
Oblicz bmi = wagi[i] / (wzrosty[i] ** 2)
Sklasyfikuj używając if/elif/else
Wyświetl wyniki dla każdego pacjenta
Oczekiwany rezultat:
5 linii z BMI i kategorią dla każdego pacjenta"""

wagi = [70, 85, 62, 95, 78]
wzrosty = [1.75, 1.80, 1.65, 1.78, 1.72]

for i in range(len(wagi)):
    bmi = wagi[i] / (wzrosty[i] ** 2)
    if bmi < 18.5:
        bmi_result = 'niedowaga'
        print(f'BMI: {bmi:.1f} - {bmi_result}')
    elif bmi >= 25:
        bmi_result = 'nadwaga'
        print(f'BMI: {bmi:.1f} - {bmi_result}')
    else:
        bmi_result = 'norma'
        print(f'BMI: {bmi:.1f} - {bmi_result}')