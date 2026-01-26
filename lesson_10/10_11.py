"""Zadanie 11 – Analiza datasetu sprzedaży
Dataset: Sprzedaż 6 produktów w 30 dni
sales = np.random.randint(50, 200, size=(6, 30))
Oblicz:
Trend sprzedaży per produkt (różnica między ostatnimi 7 dniami a pierwszymi 7 dniami)
Najlepszy tydzień (dni 0-6, 7-13, 14-20, 21-27) dla całej sprzedaży
Wykres: sprzedaż per produkt w czasie (linie)
Wymagania:
Użyj slicingu do wycinania tygodni
Wizualizacja matplotlib"""
from operator import index

import numpy as np

np.random.seed(47)
sales = np.random.randint(50, 200, size=(6, 30))

print(sales)

firt_week = sales[:,:7]
last_week = sales[:,-7:]

trend_product = np.mean(last_week, axis=1) - np.mean(firt_week, axis=1)

print('Trend sprzedaży per produkt:')
for product, trend in enumerate(trend_product, 1):
    print(f'produkt: {product}: trend: {trend:.2f}')

weeks = {
    '0-6': sales[:, :7],
    '7-13': sales[:, 7:14],
    '14-20': sales[:, 14:20],
    '21-27': sales[:, 20:28],
}

week_total = []

for days, sales in weeks.items():
    week_total.append(np.sum(sales))

print('\nSuma sprzedaży tygodniowej:')
for week, total_sales in enumerate(week_total, 1):
    print(f'tydzień {week}, sprzedaż: {total_sales}')

print(f'''\nNajlepszy tydzień sprzedażowo: 
tydzień {week_total.index(max(week_total)) + 1} (sprzedaż: {np.max(week_total)})''')
