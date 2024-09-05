def cifra_cesar(cad, llave):
    # Definimos el alfabeto como una cadena de caracteres de la 'a' a la 'z'
    alfabeto = 'abcdefghijklmnopqrstuvwxyz'
    
    # Inicializamos la cadena cifrada como una cadena vacía
    cifrado = ""
    
    # Iteramos sobre cada carácter en la cadena original proporcionada por el usuario
    for c in cad:
        # Verificamos si el carácter está en el alfabeto
        if c in alfabeto:
            # Encontramos la posición del carácter actual en el alfabeto
            pos = alfabeto.index(c)
            
            # Calculamos la nueva posición aplicando la llave (desplazamiento)
            # Usamos el operador % para asegurarnos de que la posición esté dentro del rango de 0 a 25
            cifrado = cifrado + alfabeto[(pos + llave) % 26]
        else:
            # Si el carácter no está en el alfabeto (como espacios, números, o puntuación), lo añadimos tal cual
            cifrado += c

    # Devolvemos la cadena cifrada
    return cifrado

# Solicitamos al usuario que ingrese el texto a cifrar y lo convertimos a minúsculas para uniformidad
texto = input("Introduce el texto a cifrar: ").lower()

# Solicitamos al usuario que ingrese la llave (número de desplazamiento) y lo convertimos a entero
llave = int(input("Introduce la llave (desplazamiento): "))

# Llamamos a la función de cifrado César con los datos ingresados por el usuario y almacenamos el resultado
resultado = cifra_cesar(texto, llave)

# Mostramos el texto cifrado al usuario
print("Texto cifrado:", resultado)
