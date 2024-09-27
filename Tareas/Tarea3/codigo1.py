import random

print("Programa piedra-papel-tijeras")
print("papel = 0")
import random

print("piedra = 1")
print("tijeras = 2")

nombres = ["papel", "piedra", "tijeras"]
usuario = input("Escriba su elección (0, 1 o 2): ")
compu = random.choice(['0', '1', '2'])

print("La computadora eligió", nombres[int(compu)])

if usuario == compu:
    print("Empate")
else:
    if usuario == '0' and compu == '1':
        print("Usted gana")
    elif usuario == '0' and compu == '2':
        print("Gana la computadora")
    elif usuario == '1' and compu == '0':
        print("Gana la computadora")
    elif usuario == '1' and compu == '2':
        print("Usted gana")
    elif usuario == '2' and compu == '0':
        print("Usted gana")
    elif usuario == '2' and compu == '1':
        print("Gana la computadora")

#Checo Estuvo Aqui