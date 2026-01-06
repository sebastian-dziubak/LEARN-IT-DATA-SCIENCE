"""
Zadanie 15 – Standaryzacja Z-score
Standaryzuj wartości używając wzoru z-score.
Dane (wagi pacjentów w kg):
65.5, 78.2, 54.8, 92.1, 70.0
Wymagania:
Oblicz średnią i odchylenie standardoweDla każdej wartości oblicz z-score: z = (x - mean) / std
Sprawdź, że średnia z-scores ≈ 0 i odchylenie ≈ 1
Wyświetl oryginalną wartość i jej z-score
Zinterpretuj: z > 2 (wartość bardzo wysoka), |z| < 1 (typowa), z < -2 (bardzo niska)

"""

weight = [65.5, 78.2, 54.8, 92.1, 70.0]

mean = sum(weight) / len(weight)
std_sum = 0
for x in weight:
    std_sum += (x - mean) ** 2
std = (std_sum / len(weight)) ** (1/2)

zscore_list = []
for x in weight:
    zscore_list.append((x - mean) / std)

zscore_mean = sum(zscore_list) / len(zscore_list)
zscore_sum = 0
for z in zscore_list:
    zscore_sum += (z - zscore_mean) ** 2
zscore_std = (zscore_sum / len(zscore_list)) ** (1/2)

print(f'Czy średnia z-score jest bliskie 0?')
print(round(zscore_mean) == 0)
print(f'Czy odchylenie z-score jest bliskie 1?')
print(round(zscore_std) == 1)

interpretacja_list = []
for i in zscore_list:
    if i > 2:
        interpretacja_list.append('bardzo wysoka')
    elif i < -2:
        interpretacja_list.append('bardzo niska')
    elif abs(i) < 1:
        interpretacja_list.append('typowa')
    else:
        interpretacja_list.append('wysoka / niska')

print(f'{"Wartość oryginalna":^20} | {"z-score":^20} | {"Wartość":^20}')
print("=" * 68)
for score in range(len(weight)):
    print(f'{weight[score]:^20} | {zscore_list[score]:^20.2f} | {interpretacja_list[score]:^20}')
