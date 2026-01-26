"""Zadanie 6 – Boolean indexing
Masz tablicę z oceną studentów:
grades = np.array([78, 45, 92, 67, 34, 88, 56, 91, 23, 85, 73, 95])
Wykonaj:
Znajdź wszystkie oceny >= 80 (oceny wysokie)
Znajdź wszystkie oceny < 50 (oceny niedostateczne)
Policz ile jest ocen w przedziale [60, 80)
Zmień wszystkie oceny < 50 na 50 (podniesienie do minimum)"""

import numpy as np

grades = np.array([78, 45, 92, 67, 34, 88, 56, 91, 23, 85, 73, 95])

# Znajdź wszystkie oceny >= 80 (oceny wysokie)
print(grades[grades >= 80])

#Znajdź wszystkie oceny < 50 (oceny niedostateczne)
print(grades[grades < 50])

#Policz ile jest ocen w przedziale [60, 80)
print(len(grades[(grades >= 60) & (grades < 80)]))

#Zmień wszystkie oceny < 50 na 50 (podniesienie do minimum)
grades_copy = grades.copy()
grades_copy[grades_copy < 50] = 50

print(grades_copy)