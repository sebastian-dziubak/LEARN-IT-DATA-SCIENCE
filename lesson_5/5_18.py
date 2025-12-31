"""
Zadanie 18 – Agregacja z grupowaniem
Masz dane sprzedaży (produkt, kategoria, kwota):sales = [
('Laptop', 'Electronics', 1200),
('Book', 'Media', 15),
('Phone', 'Electronics', 800),
('DVD', 'Media', 10),
('Tablet', 'Electronics', 400),
('Magazine', 'Media', 5)
]
Oblicz:
Łączną sprzedaż dla każdej kategorii
Średnią cenę produktu w każdej kategorii
Liczbę produktów w każdej kategorii
Wynik jako słownik słowników.

"""

sales = [
    ('Laptop', 'Electronics', 1200),
    ('Book', 'Media', 15),
    ('Phone', 'Electronics', 800),
    ('DVD', 'Media', 10),
    ('Tablet', 'Electronics', 400),
    ('Magazine', 'Media', 5)
]

value_of_sales = {}
mean_value_category = {}
number_of_products = {}

for i in sales:
    if i[1] not in value_of_sales:
        value_of_sales[i[1]] = i[2]
        number_of_products[i[1]] = 1
    else:
        value_of_sales[i[1]] += i[2]
        number_of_products[i[1]] += 1

for k, v in value_of_sales.items():
    mean_value_category[k] = v / number_of_products[k]

result = {"Łączna sprzedaż dla każdej kategorii:": value_of_sales,
          "Średnia cena produktu w każdej kategorii:": mean_value_category,
          "Liczba produktów w każdej kategorii:": number_of_products}

for k, v in result.items():
    print(k, v)

