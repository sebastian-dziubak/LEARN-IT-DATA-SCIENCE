"""
Zadanie 12 – Tworzenie SQL query
Masz:
Books",Tabelę: "customers"
Kolumny do wybrania: ['id', 'name', 'email', 'city']
Warunek: "city = 'New York'"
Zbuduj string z query SQL używając join() :
SELECT id, name, email, city FROM customers WHERE city = 'New York'

"""

table = "customers"
collums = ['id', 'name', 'email', 'city']
condition ="city = 'New York'"

print(f'''
SELECT {(", ").join(collums)} 
FROM {table}
WHERE {condition}
''')
