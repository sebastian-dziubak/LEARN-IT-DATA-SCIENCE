"""
Zadanie 11 – Sprawdzanie poprawności hiperparametrów
Zwaliduj hiperparametry przed treningiem.
Dane:
learning_rate = 0.01
batch_size = 64
epochs = 100dropout = 0.5
Wymagania:
Sprawdź czy learning_rate w zakresie (0, 1]
Sprawdź czy batch_size jest potęgą 2 (użyj operacji bitowych lub logarytmów)
Sprawdź czy epochs > 0 i < 1000
Sprawdź czy dropout w zakresie [0, 1]
Wyświetl "OK" lub komunikat błędu dla każdego parametru

"""
from numpy.ma.core import count

learning_rate = 0.01
batch_size = 64
epoch = 100
dropout = 0.5

print(f'Czy learning rate w zakresie (0, 1]?')
print(f'\t * learning rate = {learning_rate} --> ', end="")
if 0 < learning_rate <= 1:
    print('OK')
else:
    print('ERROR')

print(f'Czy batch size jest potęgą "2" ?')
print(f'\t * batch size = {batch_size} --> ', end="")
# liczba jest potęgą liczby 2 tylko jeśli posiada tylko jedną 1 w zapisie binarnym
if bin(batch_size).count("1") == 1:
    print('OK')
else:
    print('ERROR')

print(f'Czy epochs > 0 i < 1000 ?')
print(f'\t * epochs = {epoch} --> ', end="")
if 0 < epoch < 1000:
    print('OK')
else:
    print('ERROR')

print(f'Czy dropout w zakresie [0, 1]?')
print(f'\t * dropout = {dropout} --> ', end="")
if 0 <= dropout <= 1:
    print('OK')
else:
    print('ERROR')

