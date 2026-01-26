"""Zadanie 5 – Statystyki per wiersz i kolumna
Dana tablica reprezentująca sprzedaż 4 produktów w 7 dni:
sales = np.random.randint(10, 100, size=(4, 7))Oblicz i wypisz:
Średnią sprzedaż per produkt (axis=1)
Średnią sprzedaż per dzień (axis=0)
Dzień z najwyższą sprzedażą (np.argmax)
Produkt z najniższą średnią sprzedażą"""

import numpy as np

sales = np.random.randint(10, 100, size=(4, 7))

mean_sales_day = np.mean(sales, axis=0)
mean_sales_product = np.mean(sales, axis=1)

print('Sprzedaż 4 produktów (wiersze) w 7 dniach (kolumny')
print(sales)

print('Średnia sprzedaż każdego produktu:')
for produkt, srednia in enumerate(mean_sales_product):
    print(f'produkt {produkt + 1}: {srednia:.2f}')

print('Średia sprzedaż każdego dnia:')
for dzien, srednia in enumerate(mean_sales_day):
    print(f'dzień {dzien + 1}: {srednia:.2f}')

print(f'Dzień z najwyższą średnią sprzedażą: {np.argmax(mean_sales_day) + 1}')
print(f'Produkt z najniższą średnią sprzedażą: {np.argmax(mean_sales_product) + 1}')
