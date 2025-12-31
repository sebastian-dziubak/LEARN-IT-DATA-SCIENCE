"""
Zadanie 6 – Formatowanie raportu
Masz dane: model_name = "XGBoost" , accuracy = 0.8934 , time = 45.67 . Użyj f-
string aby stworzyć raport:
Model: XGBoost
Accuracy: 89.34%
Training time: 45.67s

"""

model_name = "XGBoost"
accuracy = 0.8934
time = 45.67

print(f'''
Model: {model_name}
Accuracy: {accuracy:.2%}
Training time: {time}s
''')