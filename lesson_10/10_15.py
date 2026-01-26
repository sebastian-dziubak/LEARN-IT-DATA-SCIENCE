"""Zadanie 15 – Convolution 1D (ręczna implementacja)
Dana tablica (sygnał) i kernel (filtr):
signal = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
kernel = np.array([0.2, 0.6, 0.2]) # Średnia ruchoma
Zaimplementuj ręcznie konwolucję 1D (bez np.convolve ):
Dla każdej pozycji w sygnale zastosuj kernel
Wynik: wygładzony sygnał
Wymagania:
Użyj pętli tylko po pozycjach, operacje na kernelu wektorowe
Wizualizuj: oryginalny sygnał vs wygładzony"""

import numpy as np
import matplotlib.pyplot as plt

signal = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
kernel = np.array([0.2, 0.6, 0.2])

n = len(signal)
k = len(kernel)
result_len = n - k + 1

smoothed_signal = np.zeros(result_len)

for i in range(result_len):
    fragment = signal[i : i+k]
    smoothed_signal[i] = np.sum(fragment * kernel)

print(f'''
Sygnał oryginalny: {signal}
Sygnał wygładzony: {smoothed_signal}
''')

plt.figure(figsize=(9, 4))

# oryginalny sygnał – rysujemy w punktach i linią
plt.plot(signal, 'o-', color='dodgerblue', label='oryginał', linewidth=1, markersize=8)

# wygładzony – przesunięty o 1 w prawo (bo straciliśmy 2 elementy)
x_smoothed = np.arange(1, 1 + len(smoothed_signal))   # 1,2,3,...,8
plt.plot(x_smoothed, smoothed_signal, 's-', color='tomato', label='wygładzony', linewidth=2)

plt.xticks(np.arange(0, 11))
plt.grid(True, alpha=0.3)
plt.legend()
plt.title("Konwolucja 1D – ręczna implementacja")
plt.xlabel("indeks")
plt.ylabel("wartość")
plt.show()
