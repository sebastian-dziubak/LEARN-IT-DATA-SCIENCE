"""Zadanie 17 – Parsing log-a treningowego
Wyodrębnij informacje z loga treningu modelu.
Dane:
Log: "Epoch 23/100 - loss: 0.3421 - accuracy: 0.8934 - val_loss: 0.4102 -
val_accuracy: 0.8712"
Wymagania:
Użyj metod split(), strip(), indeksowaniaWyodrębnij: numer epoki, total epok, loss, accuracy, val_loss, val_accuracy
Skonwertuj wartości string na odpowiednie typy (int/float)
Oblicz różnicę między train accuracy a val accuracy (oznaka overfittingu)
Wyświetl sformatowany raport"""

log ="Epoch 23/100 - loss: 0.3421 - accuracy: 0.8934 - val_loss: 0.4102 - val_accuracy: 0.8712"

print(log)

log_stripped = log.strip()
log_splitted = log_stripped.split()

epoch_index = log_splitted.index("Epoch")

epoch = int((log_splitted[epoch_index + 1][:2]))
total_epoch = int((log_splitted[epoch_index + 1][3:]))

loss_index = log_splitted.index("loss:")
loss = float((log_splitted[loss_index + 1]))

accuracy_index =log_splitted.index("accuracy:")
accuracy = float((log_splitted[accuracy_index + 1]))

val_loss_index = log_splitted.index("val_loss:")
val_loss = float((log_splitted[val_loss_index + 1]))

val_accuracy_index =log_splitted.index("val_accuracy:")
val_accuracy = float((log_splitted[val_accuracy_index + 1]))

print(f'''
numer epoki: {epoch}
wszystkich epok: {total_epoch}
loss: {loss}
accuracy: {accuracy}
val_loss: {val_loss}
val_accuracy: {val_accuracy}
overfitting: {accuracy - val_accuracy:.4f}
''')
