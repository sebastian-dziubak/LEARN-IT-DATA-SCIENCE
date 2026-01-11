"""Zadanie 16 – Symulacja Monte Carlo - Aproksymacja π
Użyj symulacji Monte Carlo do aproksymacji wartości π. Generuj losowe punkty w
kwadracie [0,1]×[0,1] i sprawdzaj, ile z nich pada w ćwierci koła o promieniu 1.
Wymagania:
Użyj modułu random
Wygeneruj 10000 losowych punktów (x, y)
Sprawdź warunek: x² + y² <= 1 (punkt w kole)
π ≈ 4 × (punkty_w_kole / wszystkie_punkty)
Użyj pętli for do generowania i sprawdzania
Oczekiwany rezultat:
Aproksymacja π (oczekiwana: ~3.14)
Błąd względny w procentach"""

import random
import math

random.seed(47)
data = [(random.random(), random.random()) for _ in range(10000)]
wszystkie_punkty = len(data)
punkty_w_kole = 0
for i in data:
    x, y = i
    if x ** 2 + y ** 2 <= 1:
        punkty_w_kole += 1

pi = 4 * (punkty_w_kole / wszystkie_punkty)
blad = (abs(pi - (math.pi)))/ math.pi
print(f'''
Wartość PI obliczona: {pi:.10f}
Wartość PI: {math.pi:.10f}
błąd względny: {blad:.2%}
''')
