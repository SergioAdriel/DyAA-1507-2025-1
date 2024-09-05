# Ejercicio de Potencias
print("\n\n\nEjercicio de Potencias\n")
a = 2**16
b = 57**83
c = 93*125
print("Potencia de 2 a la 16 = " + str(a))
print("Potencia de 57 a la 83 = " + str(b))
print("Producto de 93 y 125 = " + str(c))

# Ejercicio de Booleanos
print("\n\n\nEjercicio de Booleanos\n")
a = 3 > 2
print("3 > 2 =", a)

a = (3 > 2) or (5 < 1)
print("(3 > 2) or (5 < 1) =", a)
a = (3 > 2) and (5 < 1)
print("(3 > 2) and (5 < 1) =", a)

print("not a =", not a)

# Ejercicio de Números Complejos
print("\n\n\nEjercicio de Números Complejos\n")
a = 3 + 8j
b = 5 + 3j

print("Suma= ", a + b)
print("Resta= ", a - b)
print("Producto= ", a * b)
print("Resta= ", a - b)

# Ejercicio con For
print("\n\n\nEjercicio For\n")
print("\tImprimir del 0 al 9")
for i in range(10):
    print(i)

print("\n") #Separador

print("\tImprimir del 4 al 9")
for i in range(4,10):
    print(i)

print("\n") #Separador

print("\tImprimir del 2 al 8 en paso de 2")
for i in range(2,10,2):
    print(i)

print("\n") #Separador

print("\tImprimir del 10 al 2")
for i in range(10,1,-1):
    print(i)

# Ejercicio de Suma de todos los numeros del 1 al 100
print("\n\n\nSuma del 1 al 100\n")
n=100
suma=0

for i in range (n+1):
    suma=suma+i
    print(suma)

# Ejercicio Condicion If
print("\n\n\nEjercicio If\n")
print("5 es mas grande que 3")
a=3
b=5
if(a>b):
    print("\ta es mayor")   # Aqui NO se imprime
print("\tFalso")

print("3 es mas grande que 5")
a=5
b=3
if(a>b):
    print("\ta es mayor")   # Aqui SI se imprime

# Ejercicio Condicion If-Else
print("\n\n\nEjercicio If-Else")
a=3
b=5

if(a>b):
    print("\n\ta es mayor")
else:
    print("\n\ta NO es mayor")

# Ejercicio de Raiz Cuadrada Exacta de 7, mostrando todos los pasos
print("\n\n\nRaiz Cuadra de 7\n")
n = 7
r = 0
error = 1
delta = 1

while error > 0.001:
    error = abs(r * r - n)
    if r * r > n:           
        r = r - delta
        delta = delta / 10
    else:
        r = r + delta

    print(r)


