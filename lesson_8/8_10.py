"""Zadanie 10 – Dictionary comprehension - agregacja
Masz listę transakcji: [{"produkt": "X", "wartosc": 100}, ...] . Używając dict
comprehension i grupowania, oblicz łączną wartość dla każdego produktu.
Dataset:
transakcje = [
{"produkt": "laptop", "wartosc": 2999},
{"produkt": "mysz", "wartosc": 89},
{"produkt": "laptop", "wartosc": 2999},
{"produkt": "klawiatura", "wartosc": 249},
{"produkt": "mysz", "wartosc": 89},
{"produkt": "mysz", "wartosc": 89}
]
Wymagania:
Pogrupuj po produkcie
Zsumuj wartości dla każdego produktuWynik jako słownik: {"laptop": 5998, ...}
Oczekiwany rezultat:
Słownik z sumą wartości per produkt"""


transakcje = [
    {"produkt": "laptop", "wartosc": 2999},
    {"produkt": "mysz", "wartosc": 89},
    {"produkt": "laptop", "wartosc": 2999},
    {"produkt": "klawiatura", "wartosc": 249},
    {"produkt": "mysz", "wartosc": 89},
    {"produkt": "mysz", "wartosc": 89}
]

# unikalne produkty - set compr: {t['produkt'] for t in transakcje}
# suma dla każdej tranzakcji : sum(t['wartosc'] for t in transakcje if t['produkt] == p (unikalne produkty se compr)
# dict comprehension: {key: value for key in ... }

result = {
    p: sum(t['wartosc'] for t in transakcje if t['produkt'] == p) for p in {t['produkt'] for t in transakcje}
}

print(result)