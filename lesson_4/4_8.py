"""
Zadanie 8 – Obliczanie learning rate
Oblicz learning rate dla schedulera.
Dane:
Początkowy learning rate: 0.1
Współczynnik decay: 0.95
Numer epoki: 10
Wymagania:
Użyj wzoru: lr_new = lr_initial × (decay ^ epoch)
Operator potęgowania **
Wyświetl wynik w notacji naukowej ( .2e )

"""

poczatkowy_learning_rate = 0.1
decay = 0.95
numer_epoki = 10

lr_new = poczatkowy_learning_rate * (decay ** numer_epoki)

print(f'Learning rate po {numer_epoki} epokach: {lr_new:.2e}')