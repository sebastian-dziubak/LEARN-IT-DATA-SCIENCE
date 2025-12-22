"""
Zadanie 15 – Detekcja outliers metodą IQR
Dataset wyników egzaminów: [78, 82, 85, 88, 90, 92, 95, 97, 99, 45, 101, 103,
105, 180] . Wykryj outliers (wartości odstające) używając metody IQR (Interquartile
Range).
Dataset:
Lista wyników (zawiera outliers: 45 i 180)
Wymagania:
Posortuj dane
Oblicz Q1 (25 percentyl) i Q3 (75 percentyl) ręcznie
IQR = Q3 - Q1
Outliers: wartości < Q1 - 1.5×IQR lub > Q3 + 1.5×IQR
Zidentyfikuj i wyświetl outliers
Oczekiwany rezultat:
Q1, Q3, IQR
Lista outliers: [45, 180]

"""

numbers = [78, 82, 85, 88, 90, 92, 95, 97, 99, 45, 101, 103, 105, 180]
sorted_numbers = sorted(numbers)
outliers = []

for i in range(len(sorted_numbers)):
    percentyl = len(sorted_numbers[:i]) / len(sorted_numbers)
    if percentyl >= 0.25:
        q1 = sorted_numbers[i]
        break

for i in range(len(sorted_numbers)):
    percentyl= len(sorted_numbers[:i]) / len(sorted_numbers)
    if percentyl >= 0.75:
        q3 = sorted_numbers[i]
        break

iqr = q3 - q1

for i in sorted_numbers:
    if i < q1 - 1.5 * iqr or i > q3 + 1.5 * iqr:
        outliers.append(i)

print(outliers)