def cifra_cesar(cad, llave):
    alfabeto = 'abcdefghijklmnopqrstuvwxyz'  # Definimos el alfabeto
    cifrado = ""  # Inicializamos la cadena cifrada

    for c in cad:  # Iteramos sobre cada carácter en la cadena original
        if c in alfabeto:  # Si el carácter está en el alfabeto
            indice = alfabeto.index(c)  # Encontramos su índice en el alfabeto
            nuevo_indice = (indice + llave) % len(alfabeto)  # Calculamos el nuevo índice aplicando la llave
            cifrado += alfabeto[nuevo_indice]  # Añadimos el carácter cifrado a la cadena resultado
        else:
            cifrado += c  # Si no está en el alfabeto, lo añadimos tal cual

    return cifrado  # Devolvemos la cadena cifrada

# Solicitamos al usuario que ingrese la cadena a cifrar y la llave
texto = input("Introduce el texto a cifrar: ").lower()  # Convertimos a minúsculas para uniformidad
llave = int(input("Introduce la llave (desplazamiento): "))

# Llamamos a la función y mostramos el resultado
resultado = cifra_cesar(texto, llave)
print("Texto cifrado:", resultado)
