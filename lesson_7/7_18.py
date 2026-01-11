"""Zadanie 18 – Histogram ręczny (binning)
Masz dane: [12, 15, 18, 22, 25, 28, 31, 35, 38, 42, 45, 48, 52, 55, 58] .
Utwórz histogram z przedziałami (bins): [10-20), [20-30), [30-40), [40-50), [50-60). Policz ile
wartości pada w każdy bin.
Dataset:
Lista 15 wartości
Wymagania:
Zdefiniuj granice binów: [10, 20, 30, 40, 50, 60]
Dla każdej wartości znajdź odpowiedni bin używając pętli
Zwiększ licznik dla tego binu
Wyświetl histogram tekstowy (np. gwiazdki: *** dla 3 wartości)
Oczekiwany rezultat:
Histogram pokazujący rozkład danych w przedziałach"""

data = [12, 13, 14, 18, 22, 23, 25, 26, 28, 30, 31, 49, 45, 44, 44, 44, 46, 48, 45, 15, 18, 22, 25, 28, 31, 35, 38, 42, 45, 48, 52, 55, 58]
bins = [x for x in range(10, 70, 10)]
result = {}

for b in bins:
    result[b / 10] = 0

for i in data:
    x = int(i // 10)
    result[x] += 1

print('Histogram pokazujący rozkład danych')
for i in range(len(bins) - 1):
    print(f'[{bins[i]} - {bins[i + 1]}) ', '* ' * result[i+1])
