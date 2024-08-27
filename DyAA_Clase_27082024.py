# Clase del 27 de Agosto del 2024
import random

n = 10
lista = []

while len(lista) < n: #Mientras la lonigtud de elementos en mi lista
    ale = random.randint(1, n) #Creo de mi biblioteca de numeros alatorios
    if ale not in lista: #Si NO esta lo agrego, si esta NO lo agrega
        lista.append(ale) #Esto añade al final de la lista

#print(lista)

for i in range(n):
    for j in range(n-1): 
        if lista[j] > lista[j + 1]:
            temp = lista[j]
            lista[j] = lista[j + 1]
            lista[j + 1] = temp

#print(lista)

