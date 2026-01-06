"""
Zadanie 12 – Estymacja czasu treningu
Oblicz szacowany czas treningu modelu.
Dane:
Liczba próbek: 50000
Batch size: 128
Liczba epok: 50
Czas na jeden batch: 0.15 sekundy
Wymagania:
Oblicz liczbę batchy na epokę (użyj dzielenia całkowitego i modulo)
Oblicz całkowity czas w sekundach
Skonwertuj na minuty i godziny
Wyświetl: "Szacowany czas: X h Y min Z s"

"""
import math

samples = 50000
batch_size = 128
epochs = 50
batch_time = 0.15

#Obliczam ilość batchy na epokę przy pomocy dzielenia cełkowitego i modulo
batch_per_epoch = (samples // 128)
if samples % batch_size != 0:
    batch_per_epoch += 1

total_time_seconds = math.ceil(epochs * batch_per_epoch * batch_time)
time_hours = total_time_seconds // 3600
time_minutes = total_time_seconds // 60
time_seconds = total_time_seconds % 60

print(f'''
Liczba próbek: {samples:,}
batch size = {batch_size}
epoki = {epochs}
liczba batchy na epokę = {batch_per_epoch}
czas na jeden batch [s] = 0.15
Szacowany czas treningu modelu:
\t{time_hours} h {time_minutes} min {time_seconds} s
''')
