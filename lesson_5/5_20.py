"""
Zadanie 20 – Walidacja i transformacja pipeline
Stwórz funkcję clean_and_validate(data) , która dla listy stringów:raw_data = [
" 0.8567 ",
"invalid",
"0.9123",
"",
" 0.7890 ",
"0.95",
"not_a_number"
]
Wykonuje:
1. Strip białych znaków
2. Walidację czy string reprezentuje liczbę (użyj try/except)
3. Konwersję na float
4. Filtrowanie wartości poza zakresem [0, 1]
5. Zwraca listę poprawnych wartości float oraz listę błędów (indeks, wartość, powód)

"""
from operator import index


def clean_and_validate(data):
    clean_data = []
    errors = []
    for i in data:
        y = i.strip()
        try:
            if float(y):
                z = float(y)
                if 0 <= z <= 1:
                    clean_data.append(z)
                else:
                    errors.append((data.index(i), y, 'wartość poza zakresem [0, 1]'))
        except ValueError:
            errors.append((data.index(i), y, 'string nie jest liczbą'))
    return print(f'''
Lista poprawnych wartości: {clean_data}
Lista błędów: {errors}
''')


raw_data = [
    " 1.8567 ",
    "invalid",
    "0.9123",
    "",
    " 0.7890 ",
    "0.95",
    "not_a_number"
]

clean_and_validate(raw_data)