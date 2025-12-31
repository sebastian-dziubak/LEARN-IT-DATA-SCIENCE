"""
Zadanie 11 – Normalizacja tekstów
Masz listę kategorii produktów z różnymi formatami:
categories = [" Electronics
"books ", "BOOKS"]
", "ELECTRONICS", "electronics", "
Znormalizuj je (strip + lower) i znajdź unikalne kategorie.

"""

categories = ["  Electronics ", "ELECTRONICS", "electronics", "  Books", "books ", "BOOKS"]

uniqe_categories = []

for category in categories:
    norm_category = category.strip().lower()
    if norm_category not in uniqe_categories:
        uniqe_categories.append(norm_category)

print(f'Unikalne kategorie: {uniqe_categories}')

