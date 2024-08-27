# Clase del 27 de Agosto del 2024
import random

n = 10
lista = []

while len(lista) < n:
    ale = random.randint(1, n)
    if ale not in lista:
        lista.append(ale)

print(lista)
