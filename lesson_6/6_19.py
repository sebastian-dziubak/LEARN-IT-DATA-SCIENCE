"""
Zadanie 19 – Word frequency analysis - top N słów
Przeanalizuj długi tekst i znajdź 10 najczęściej występujących słów. Użyj słownika do
zliczania i zbioru do odfiltrowania stop words (częste słowa bez znaczenia).
Dataset:
tekst =
Python jest językiem programowania który jest bardzo popularny w data
science.
Python jest łatwy do nauki i ma ogromną społeczność. Wiele firm używa
Python
do analizy danych i machine learning. Python jest uniwersalny i można go
używać
do web development, automatyzacji i wielu innych zastosowań. Python jest
open source.
stop_words = {'jest', 'do', 'i', 'w', 'można', 'go', 'się', 'z', 'na',
'po'}
Wymagania:Konwertuj tekst na małe litery, podziel na słowa
Usuń stop words używając zbioru
Policz częstości słów (słownik)
Posortuj i wypisz top 10
Oczekiwany wynik:
Lista 10 najczęstszych słów z liczbą wystąpień
Wykres słupkowy (matplotlib) - opcjonalnie

"""

tekst = """
Python jest językiem programowania który jest bardzo popularny w data
science.
Python jest łatwy do nauki i ma ogromną społeczność. Wiele firm używa
Python
do analizy danych i machine learning. Python jest uniwersalny i można go
używać
do web development, automatyzacji i wielu innych zastosowań. Python jest
open source.
"""

stop_words = {'jest', 'do', 'i', 'w', 'można', 'go', 'się', 'z', 'na',
'po'}

tekst_split = tekst.lower().replace('\n',' ').replace('.', '').replace(',', '').strip().strip('\n').split(' ')
tekst_without_stop_words = {}

for i in tekst_split:
    word = set()
    word.add(i)
    result = word - stop_words
    if len(result) > 0:
        if i not in tekst_without_stop_words:
            tekst_without_stop_words[i] = 1
        else:
            tekst_without_stop_words[i] += 1

sorted_result = sorted(tekst_without_stop_words.items(), key=lambda item: item[1], reverse=True)

print('Top 10 najczęściej występujących słów:')
for i in range(10):
    print(f'"{sorted_result[i][0]}"')