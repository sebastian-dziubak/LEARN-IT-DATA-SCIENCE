"""Zadanie 20 – Dataset deduplication z zachowaniem kolejności
Masz listę rekordów (krotek) z danymi użytkowników. Niektóre rekordy są duplikatami. Usuń
duplikaty używając zbioru, ale zachowaj kolejność pierwszego wystąpienia (zbiory nie
zachowują kolejności!).
Dataset:
uzytkownicy = [
('user001', 'Anna', 'Kowalska'),
('user002', 'Jan', 'Nowak'),
('user001', 'Anna', 'Kowalska'), # duplikat
('user003', 'Maria', 'Zielińska'),
('user002', 'Jan', 'Nowak'),
# duplikat
('user004', 'Piotr', 'Wiśniewski'),
('user003', 'Maria', 'Zielińska'), # duplikat
('user005', 'Ewa', 'Wójcik')
]
Wymagania:
Usuń duplikaty (po pierwszym polu - ID użytkownika)
Zachowaj kolejność pierwszego wystąpienia
Użyj zbioru do śledzenia już widzianych ID
Wypisz oryginalne rekordy i po deduplikacji
Policz ile duplikatów usunięto
Oczekiwany wynik:
Lista bez duplikatów w oryginalnej kolejności
Raport: ile rekordów usunięto, oszczędność pamięci"""

uzytkownicy = [
    ('user001', 'Anna', 'Kowalska'),
    ('user002', 'Jan', 'Nowak'),
    ('user001', 'Anna', 'Kowalska'), # duplikat
    ('user003', 'Maria', 'Zielińska'),
    ('user002', 'Jan', 'Nowak'), # duplikat
    ('user004', 'Piotr', 'Wiśniewski'),
    ('user003', 'Maria', 'Zielińska'), # duplikat
    ('user005', 'Ewa', 'Wójcik')
]

uzytkownicy_bez_duplikatow = []
users = set()
duplikaty = 0

for i in uzytkownicy:
    if i[0] not in users:
        users.add(i[0])
        uzytkownicy_bez_duplikatow.append(i)
    else:
        duplikaty += 1

print(f'''
Oryginalna lista: 
{uzytkownicy}
Lista bez duplikatów:
{uzytkownicy_bez_duplikatow}
Usunięto duplikatów: {duplikaty}
''')