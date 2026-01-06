
studenci = [
('Anna', 'Kowalska', 5.0, 4.5, 5.0),
('Jan', 'Nowak', 3.0, 3.5, 3.0),
('Maria', 'Zielińska', 4.0, 4.5, 5.0),
('Piotr', 'Wiśniewski', 2.0, 3.0, 2.5),
('Ewa', 'Wójcik', 5.0, 5.0, 4.5),
('Tomasz', 'Kamiński', 4.0, 3.5, 4.0)
]

students = {}
srednia =[]
kategorie = []
tuples = []

for student in range(len(studenci)):
    srednia.append(round(((studenci[student][2] + studenci[student][3] + studenci[student][4]) / 3), 2))
    if srednia[student] >= 4.5:
        kategorie.append("wyróżniający")
    elif srednia[student] >= 3.5:
        kategorie.append("dobry")
    elif srednia[student] < 3.5:
        kategorie.append("średni")

for x in range(len(studenci)):
    tuples.append((studenci[x][0], studenci[x][1], srednia[x]))
    if kategorie[x] not in students:
        students[kategorie[x]] = []
        students[kategorie[x]].append(tuples[x])
    else:
        students[kategorie[x]].append(tuples[x])

print(students)