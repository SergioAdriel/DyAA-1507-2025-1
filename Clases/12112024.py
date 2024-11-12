from itertools import permutations

# Definir la lista de colores
colores = ["rojo", "verde", "amarillo"]

# Obtener todas las permutaciones de los colores
combinaciones = list(permutations(colores))

# Imprimir cada combinación
print("Todas las combinaciones posibles de los colores:")
for combinacion in combinaciones:
    print(combinacion)