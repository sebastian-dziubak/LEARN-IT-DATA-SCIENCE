"""
Zadanie 10 – Agregacja danych po kategoriach
Masz listę transakcji (kategoria, kwota):
transactions = [
('food', 50),
('transport', 20),
('food', 30),
('entertainment', 40),
('transport', 15),
('food', 25)
]
Oblicz łączną kwotę dla każdej kategorii. Wynik zapisz w słowniku (użyj pętli i warunków).

"""

transactions = [
('food', 50),
('transport', 20),
('food', 30),
('entertainment', 40),
('transport', 15),
('food', 25)
]

uniqe_category = {}

for category, income in transactions:
    if category not in uniqe_category:
        uniqe_category[category] = income
    elif category in uniqe_category:
        uniqe_category[category] += income

print(uniqe_category)