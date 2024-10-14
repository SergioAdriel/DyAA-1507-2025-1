import random

print("Programa piedra-papel-tijeras")
print("papel = 0")
print("piedra = 1")
print("tijeras = 2")

nombres = ["papel", "piedra", "tijeras"]
usuario = input("Escriba su elección (0, 1 o 2): ")
compu = random.choice(['0', '1', '2'])

print("La computadora eligió", nombres[int(compu)])

if usuario == compu:
    print("Empate")
elif (int(usuario) - int(compu)) % 3 == 1:
    print('Gana la computadora')
else:
<<<<<<< HEAD
    print('Usted gana')
=======
    print('Usted gana')

#Checo Estuvo Aqui
>>>>>>> f8bf5cc79f75aa907e19e318b2ba2b355c87738d
