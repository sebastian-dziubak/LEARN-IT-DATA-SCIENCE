"""
Zadanie 20 – Generowanie SQL query z Python
Wygeneruj zapytanie SQL używając zmiennych Python.
Dane:
Tabela: "patients"
Kolumny do wybrania: ["patient_id", "age", "diagnosis"]
Warunek 1: age > 40
Warunek 2: diagnosis w ['diabetes', 'hypertension']
Sortowanie: według age malejąco
Limit: 100 wierszy
Wymagania:
Użyj f-strings do budowy zapytania SELECT
Poprawne formatowanie SQL (wielkie litery dla słów kluczowych)
Lista diagnoz jako string: "('diabetes', 'hypertension')"
Użyj join() do łączenia kolumn
Wyświetl gotowe zapytanie, które można skopiować do SQL

"""

print(f'''
SELECT p.patient_id, p.age, d.name AS diagnosis
FROM patients p
JOIN diagnosis d 
ON p.diagnosis_id = d.diagnosis_id
WHERE p.age > 40
AND d. name IN ('diabetes', 'hypertension')
ORDER BY p.age DESC
LIMIT 100
''')