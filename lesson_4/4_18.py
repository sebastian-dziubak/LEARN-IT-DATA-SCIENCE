"""
Zadanie 18 – Walidacja formatu danych wejściowych
Sprawdź poprawność danych wejściowych przed analizą.
Dane:
" 45.7 " - wiek pacjenta
"male" - płeć
"120/80" - ciśnienie krwi
" 175.5cm " - wzrost
Wymagania:
Wyczyść białe znaki
Sprawdź czy wiek to liczba float w zakresie (0, 120]
Sprawdź czy płeć to "male" lub "female"
Rozdziel ciśnienie na skurczowe/rozkurczowe i zwaliduj zakresy
Wyodrębnij wartość liczbową ze wzrostu (usuń "cm")
Wyświetl raport walidacji dla każdego pola

"""
from os.path import split

age = " 45.7 "
gender = "male"
blood_pressure = "120/80"
height = " 175.5cm "

parameters = [age, gender, blood_pressure, height]
stripped_parameters = []

for parameter in parameters:
    stripped_parameters.append(parameter.strip())
del parameters

age = float(age)
if type(age) == float and 0 < age <= 120:
    is_float_and_number = True
else:
    is_float_and_number = False

if gender == "male" or gender == "female":
    is_gender = True
else:
    is_gender = False

blood_pressure_skurczowe, blood_pressure_rozkurczowe = blood_pressure.split("/")
height_number = height.replace("cm", "")

print(f'''
*** RAPORT ***
wiek = {age}
Czy wiek to float w zakresie (0, 120]? >> {is_float_and_number}\n
płeć = {gender}
Czy płeć to "male" lub "female"? >> {is_gender}\n
Ciśnienie = {blood_pressure}
Ciśnienie skurczowe: {blood_pressure_skurczowe}
Ciśnienie rozkurczowe: {blood_pressure_rozkurczowe}\n
wzrost = {height}
Wyodrębnienie wartości liczbowej: {height_number}
''')