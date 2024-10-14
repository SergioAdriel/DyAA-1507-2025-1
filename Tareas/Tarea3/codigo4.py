import random

print("Programa piedra-papel-tijeras-lagarto-spock")
print("papel = 0")
print("piedra = 1")
print("tijeras = 2")
print("lagarto = 3")
print("spock = 4")

nombres = ["papel", "piedra", "tijeras", "lagarto", "spock"]
usuario = input("Escriba su elección (0, 1, 2, 3 ó 4): ")
compu = random.choice(['0', '1', '2', '3', '4'])

print("La computadora eligió", nombres[int(compu)])

if usuario == compu:
    print("Empate")
elif (int(usuario) - int(compu)) % 5 in [1,2]:
    print('Gana la computadora')
else:
    print('Usted gana')

<<<<<<< HEAD
    0
=======
#Checo Estuvo Aqui
>>>>>>> f8bf5cc79f75aa907e19e318b2ba2b355c87738d
