"""Zadanie 13 – Symulacja algorytmu K-Nearest Neighbors (1D)Masz dane treningowe: dane_treningowe = [(1.5, "A"), (2.3, "A"), (3.8, "B"),
(4.2, "B"), (5.1, "B")] (wartość, klasa). Dla nowego punktu x_nowy = 3.5 znajdź 3
najbliższych sąsiadów i przewiduj klasę (najczęstsza klasa wśród sąsiadów).
Dataset:
Lista krotek (wartość, etykieta)
Nowy punkt: 3.5
Wymagania:
Oblicz odległości: abs(x_nowy - punkt)
Posortuj według odległości (ręcznie lub używając sorted() )
Wybierz k=3 najbliższych
Policz wystąpienia klas
Przewiduj najczęstszą klasę
Oczekiwany rezultat:
3 najbliższe punkty z odległościami
Przewidywana klasa dla x=3.5"""

dane_treningowe = [(1.5, "A"), (2.3, "A"), (3.8, "B"), (4.2, "B"), (5.1, "B")]
result = []
klasy = {}
x_nowy = 3.5

for punkt in dane_treningowe:
    wartosc, klasa = punkt
    indeks = dane_treningowe.index(punkt)
    odleglosc = round(abs(x_nowy - wartosc), 1)
    result.append((odleglosc, klasa, indeks))

result.sort(key=lambda x: x[0])

for i in range(3):
    klasa = result[i][1]
    if klasa not in klasy:
        klasy[klasa] = 1
    else:
        klasy[klasa] += 1

klasy_sorted = sorted(klasy.items(), key=lambda x: x[1], reverse=True)

print(f'Punkt = {x_nowy}\nTrzy najbliższe punkty:')
for i in range(3):
    print(f'{dane_treningowe[result[i][2]]}, odległość od szukanego punktu: {result[i][0]}')
print(f'przwidywana klasa: {klasy_sorted[0][0]}')