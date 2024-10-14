def carga_cifrado():  # Carga texto cifrado desde el archivo
    with open('Tareas\Tarea4\MUÃ‘OZ CAMARENA SERGIO ADRIEL.txt', 'r') as archivo:
        return archivo.read()  # Lee todo el contenido del archivo

# Cargar el texto cifrado desde el archivo y lo almaceno en la variable de textoCifrado
textoCifrado = carga_cifrado()

# Diccionario con los caracteres que llegue a encontrar en mi texto
diccionarioFinal = {
    'a': 'h',
    'b': 'w',
    'c': 'k',
    'd': 'ChecoEstuvoAqui',
    'e': 't',
    'f': 'j',
    'g': 'v',
    'h': 'y',
    'i': 'p',
    'j': 'e',
    'k': 'g',
    'l': 'i',
    'm': 'o',
    'n': 'c',
    'o': 's',
    'p': 'r',
    'q': 'u',
    'r': 'a',
    's': 'f',
    't': 'x',
    'u': 'n',
    'v': 'm',
    'w': 'b',
    'x': 'l',
    'y': 'ChecoEstuvoAqui',
    'z': 'd',
}

# Función para aplicar Diccionario al texto cifrado
def aplicarDicionario(textoCifrado, diccionarioFinal):
    textoDescifrado = "" # Inicalizamos la cadena vacia para el texto ya descifrado
    for char in textoCifrado: # Itera sobre cada caracter en el texto cifrado 
        if char in diccionarioFinal: # Verifica que el caracter este en el diccionario
            textoDescifrado += diccionarioFinal[char] # Si esta lo agrega
        else:
            textoDescifrado += char  # En caso contrario pasa sin cambios
    return textoDescifrado

# Aplicar el diccionario al texto cifrado
textoDescifrado = aplicarDicionario(textoCifrado, diccionarioFinal) #Guardamos el texto del texto descifrado

# Mostrar el resultado final
print(textoDescifrado)