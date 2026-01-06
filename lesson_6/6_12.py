"""Zadanie 12 – Analiza transakcji - słowniki zagnieżdżone
Masz listę transakcji (krotek): [('2024-01-15', 'Elektronika', 1200), ('2024-01-
16', 'Meble', 800), ('2024-01-15', 'Elektronika', 350), ...] . Stwórz słownik
gdzie kluczem jest data, a wartością słownik z sumą sprzedaży dla każdej kategorii tego
dnia.
Dataset:
transakcje = [
('2024-01-15', 'Elektronika', 1200),
('2024-01-15', 'Meble', 450),
('2024-01-16', 'Elektronika', 800),
('2024-01-16', 'Elektronika', 350),
('2024-01-15', 'Odzież', 200),
('2024-01-16', 'Meble', 600)
]
Wymagania:
Zagnieżdżone słowniki: {data: {kategoria: suma}}
Iteruj po transakcjach i akumuluj sumy
Oczekiwany wynik:
Słownik typu: {'2024-01-15': {'Elektronika': 1200, 'Meble': 450, ...}, ...}"""

transakcje = [
('2024-01-15', 'Elektronika', 1200),
('2024-01-15', 'Meble', 450),
('2024-01-16', 'Elektronika', 800),
('2024-01-16', 'Elektronika', 350),
('2024-01-15', 'Odzież', 200),
('2024-01-16', 'Meble', 600)
]

result = {}

for date, category, amount in transakcje:
    if date not in result:
        result[date] = {}
    if category not in result[date]:
        result[date][category] = 0
    result[date][category] += amount

print(result)


