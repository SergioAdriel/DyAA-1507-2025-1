def carga_cifrado():
    # Carga texto cifrado desde el archivo
    with open('Tareas\Tarea4\MUÃ‘OZ CAMARENA SERGIO ADRIEL.txt', 'r') as archivo:
        return archivo.read()

# Cargar el texto cifrado desde el archivo
textoCifrado = carga_cifrado()

diccionarioFinal = {
    'a': 'h', 'b': 'w', 'c': 'k', 'd': 'ChecoEstuvoAqui', 'e': 't',
    'f': 'j', 'g': 'v', 'h': 'y', 'i': 'p', 'j': 'e',
    'k': 'g', 'l': 'i', 'm': 'o', 'n': 'c', 'o': 's',
    'p': 'r', 'q': 'u', 'r': 'a', 's': 'f', 't': 'x',
    'u': 'n', 'v': 'm', 'w': 'b', 'x': 'l', 'y': 'ChecoEstuvoAqui', 'z': 'd'
}

def aplicar_diccionario(texto, diccionario):
    # Aplica el diccionario al texto cifrado
    return ''.join(diccionario.get(char, char) for char in texto)

# Desencriptar el texto
textoDescifrado = aplicar_diccionario(textoCifrado, diccionarioFinal)

# Mostrar el resultado final
print(textoDescifrado)
