"""Zadanie 13 – Standaryzacja i outliers
Dataset: 100 wartości z rozkładu normalnego + 5 outliers
np.random.seed(42)
data = np.concatenate([np.random.randn(100) * 10 + 50,
np.array([150, -50, 200, -100, 180])])
np.random.shuffle(data)
Wymagania:
Zastosuj standaryzację (z-score)
Wykryj outliery (wartości z |z-score| > 3)
Usuń outliery i ponownie standaryzuj
Wizualizuj: przed/po (histogramy + box plot)
Oczekiwany rezultat:
Tablica bez outlierów
Wizualizacje pokazujące efekt"""

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

np.random.seed(42)
data = np.concatenate([np.random.randn(100) * 10 + 50, np.array([150, -50, 200, -100, 180])])
np.random.shuffle(data)

data_mean = np.mean(data)
data_std = np.std(data)
data_zscore = (data - data_mean) / data_std

print(f'''
wielkosc zbioru: {len(data)}
liczba outlierów: {len(data[np.abs(data_zscore) > 3])}
''')

data_clean = data[~(np.abs(data_zscore) > 3)]

data_clen_mean = np.mean(data_clean)
data_clean_std = np.std(data_clean)
z_score_data_clean = (data_clean - data_clen_mean) / data_clean_std

print(f'''
wielkosc zbioru po usunięciu outlierów: {len(data_clean)}
liczba outlierów: {len(data_clean[np.abs(z_score_data_clean) > 3])}
''')

plt.figure(figsize=(12, 8))

# ------------------ Histogramy ------------------
plt.subplot(2, 2, 1)
plt.hist(data, bins=35, color='salmon', edgecolor='black')
plt.title("Przed usunięciem\n(105 wartości + 5 dziwnych)")
plt.xlabel("Wartość")
plt.ylabel("Ile razy")

plt.subplot(2, 2, 2)
plt.hist(data_clean, bins=25, color='lightgreen', edgecolor='black')
plt.title("Po usunięciu outlierów\n(100 wartości)")
plt.xlabel("Wartość")
plt.ylabel("Ile razy")

# ------------------ Boxploty ------------------
plt.subplot(2, 2, 3)
plt.boxplot(data, vert=False, patch_artist=True, boxprops=dict(facecolor='salmon'))
plt.title("Boxplot – przed usunięciem")
plt.xlabel("Wartość")

plt.subplot(2, 2, 4)
plt.boxplot(data_clean, vert=False, patch_artist=True, boxprops=dict(facecolor='lightgreen'))
plt.title("Boxplot – po usunięciu")
plt.xlabel("Wartość")

plt.tight_layout()
plt.show()