"""Zadanie 13 – Analiza sentymentu komentarzy
Masz listę komentarzy (stringi) i słownik słów pozytywnych/negatywnych. Przeanalizuj
każdy komentarz i określ czy jest pozytywny (więcej słów pozytywnych), negatywny czy
neutralny.Dataset:
komentarze = [
"Ten produkt jest świetny i fantastyczny",
"Okropny towar, kiepska jakość",
"Całkiem dobry, ale mogłoby być lepiej",
"Rewelacja, super jakość, polecam",
"Słaby produkt, nie polecam"
]
slowa_pozytywne = {'świetny', 'fantastyczny', 'dobry', 'super',
'rewelacja', 'polecam'}
slowa_negatywne = {'okropny', 'kiepski', 'słaby', 'nie polecam', 'zły'}
Wymagania:
Rozdziel komentarze na słowa (użyj .lower().split() )
Policz słowa pozytywne i negatywne w każdym komentarzu
Określ sentyment (pozytywny/negatywny/neutralny)
Zwróć listę krotek: (komentarz, sentyment, liczba_poz, liczba_neg)
Oczekiwany wynik:
Lista z analizą sentymentu dla każdego komentarza
Statystyka: ile komentarzy pozytywnych/negatywnych/neutralnych"""

komentarze = [
"Ten produkt jest świetny i fantastyczny",
"Okropny towar, kiepska jakość",
"Całkiem dobry, ale mogłoby być lepiej",
"Rewelacja, super jakość, polecam",
"Słaby produkt, nie polecam"
]

slowa_pozytywne = {'świetny', 'fantastyczny', 'dobry', 'super', 'rewelacja', 'polecam'}
slowa_negatywne = {'okropny', 'kiepski', 'słaby', 'nie polecam', 'zły'}

comment_split = []
comment_set = []
for komentarz in komentarze:

    comment_split.append(komentarz.replace(',', '').lower().split(' '))

comment_split[4].pop()
comment_split[4].pop()
comment_split[4].append('nie polecam')

for i in comment_split:
    comment_set.append(set(i))

for i in range(len(komentarze)):
    positive = len(comment_set[i] & slowa_pozytywne)
    negative = len(comment_set[i] & slowa_negatywne)
    if positive > negative:
        sentyment = 'pozytywny'
    elif positive < negative:
        sentyment = 'negatywny'
    else:
        sentyment = 'neutralny'
    print((komentarze[i], sentyment, positive, negative))
