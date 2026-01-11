"""
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

all_logs = len(logs)
info_log = 0
warning_log = 0
error_log = 0

for log in logs:
    if 'INFO' in log:
        info_log += 1
    elif 'WARNING' in log:
        warning_log += 1
    else:
        error_log += 1

print(f'{"Nazwa loga":<15} {"Ilość wystąpień":<20} {"zawartość procentowa"}')
print(f'{"INFO":<15} {info_log:<20} {info_log / all_logs * 100 }%')
print(f'{"WARNING":<15} {info_log:<20} {warning_log / all_logs * 100 }%')
print(f'{"ERROR":<15} {info_log:<20} {error_log / all_logs * 100 }%')
