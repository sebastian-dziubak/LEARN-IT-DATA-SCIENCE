"""Zadanie 11 – Feature engineering z comprehension
Masz dane klientów: wiek i dochód. Dodaj nowe cechy: kat_wiekowa (młody/
średni/starszy) i kat_dochodu (niski/średni/wysoki).
Dataset:
klienci = [
{"id": 1, "wiek": 25, "dochod": 4500},
{"id": 2, "wiek": 45, "dochod": 9200},
{"id": 3, "wiek": 32, "dochod": 6800},
{"id": 4, "wiek": 28, "dochod": 5200},
{"id": 5, "wiek": 55, "dochod": 12000}
]
Wymagania:
Kategoria wiekowa: <30 = młody, 30-50 = średni, >50 = starszy
Kategoria dochodu: <5000 = niski, 5000-10000 = średni, >10000 = wysoki
Użyj list comprehension do tworzenia nowej listy z dodatkowymi cechami
Oczekiwany rezultat:
Lista klientów z 2 nowymi cechami"""

def kategoria_wiekowa(age):
    if age < 30:
        return 'młody'
    elif 30 <= age <= 50:
        return 'średni'
    else:
        return 'starszy'

def kategoria_dochodu(income):
    if income < 5000:
        return 'niski'
    elif 5000 <= income <= 10000:
        return 'średni'
    else:
        return 'wysoki'

klienci = [
    {"id": 1, "wiek": 25, "dochod": 4500},
    {"id": 2, "wiek": 45, "dochod": 9200},
    {"id": 3, "wiek": 32, "dochod": 6800},
    {"id": 4, "wiek": 28, "dochod": 5200},
    {"id": 5, "wiek": 55, "dochod": 12000}
]

result = [
    {
        'id': k['id'],
        'wiek': k['wiek'],
        'dochod': k['dochod'],
        'kat_wiekowa': kategoria_wiekowa(k['wiek']),
        'kat_dochodu': kategoria_dochodu(k['dochod'])
    }
    for k in klienci
]

for i in result:
    print(i)
