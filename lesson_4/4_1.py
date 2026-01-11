"""
Zadanie 1 – Kalkulator BMI
Napisz program, który obliczy wskaźnik BMI (Body Mass Index).
Dane:
Waga: 70 kg
Wzrost: 1.75 m
Wymagania:
Stwórz zmienne waga i wzrost
Oblicz BMI według wzoru: BMI = waga / (wzrost²)
Wyświetl wynik z 2 miejscami po przecinku
Dodaj interpretację: BMI < 18.5 (niedowaga), 18.5-24.9 (norma), ≥25 (nadwaga)

"""

waga = float(input('Podaj swoją wagę w [kg]: '))
wzrost = float(input('Podaj swój wzrost w [m]: '))

bmi = waga / (wzrost **2)

if 18.5 <= bmi <= 24.9:
    interpretacja = 'norma'
elif bmi < 18.5:
    interpretacja = 'niedowaga'
else:
    interpretacja = 'nadwaga'

print(f'BMI: {bmi:.2f}')
print(f'Interpretacja: {interpretacja.title()}')

