"""Zadanie 11 – Analiza trendów wzrostowych/spadkowychMasz dane sprzedaży miesięcznej: [1200, 1350, 1290, 1480, 1520, 1510, 1680,
1720, 1700, 1890, 1950, 2100] . Zidentyfikuj miesiące, w których sprzedaż wzrosła w
porównaniu do poprzedniego miesiąca.
Dataset:
Lista 12 wartości (sprzedaż miesięczna w PLN)
Wymagania:
Pętla for i in range(1, len(sprzedaz)):
Porównaj sprzedaz[i] z sprzedaz[i-1]
Oblicz zmianę procentową
Wyświetl miesiące ze wzrostem
Oczekiwany rezultat:
Lista miesięcy ze wzrostem i procentowy przyrost"""

sales = [1200, 1350, 1290, 1480, 1520, 1510, 1680, 1720, 1700, 1890, 1950, 2100]
months = ['styczeń', 'luty', 'marzec', 'kwiecień', 'maj', 'czerwiec', 'lipiec', 'sierpień', 'wrzesień', 'październik', 'listopad', 'grudzień']
result = []

for i in range(1, len(sales)):
    if sales[i] > sales[i-1]:
        wzrost = round(((sales[i] - sales[i-1]) / sales[i-1]) * 100, 2)
        month = months[i]
        result.append((month, wzrost))

print(result)