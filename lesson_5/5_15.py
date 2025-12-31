"""
Zadanie 15 – Parsowanie logów
Masz listę logów:logs = [
"2024-01-15 10:23:45 INFO Model training started",
"2024-01-15 10:45:12 WARNING Low memory",
"2024-01-15 11:02:33 ERROR Training failed",
"2024-01-15 11:05:01 INFO Retrying with smaller batch"
]
Wyciągnij i zlicz poziomy logów (INFO, WARNING, ERROR). Oblicz % każdego poziomu.

"""

logs = [
"2024-01-15 10:23:45 INFO Model training started",
"2024-01-15 10:45:12 WARNING Low memory",
"2024-01-15 11:02:33 ERROR Training failed",
"2024-01-15 11:05:01 INFO Retrying with smaller batch"
]

number_of_logs = {}
number_of_all_logs = 0

for i in logs:
    log_name = i.split(' ')[2:3]
    if log_name[0] not in number_of_logs:
        number_of_logs[log_name[0]] = 1
    else:
        number_of_logs[log_name[0]] += 1
    number_of_all_logs += 1

print(f'Procentowa zawarość logów:')
for k, v in number_of_logs.items():
    print(f'{k}: {(v / number_of_all_logs):.1%}')
