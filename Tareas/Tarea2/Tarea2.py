def carga_palabras():  # Carga palabras desde el archivo
        archivo = open('C:/Users/Adrie/OneDrive/Escritorio/GitHub/DyAA-1507-2025-1/Tareas/Tarea2/words.txt', 'r')
        renglon = archivo.readline()
        palabras = renglon.split()
        print(len(palabras), 'palabras leídas')  # Muestra la cantidad de palabras
        return palabras

def carga_cifrado():  # Carga texto cifrado desde el archivo
        archivo = open('C:/Users/Adrie/OneDrive/Escritorio/GitHub/DyAA-1507-2025-1/Tareas/Tarea2/textoCifrado.txt', 'r')
        renglon = archivo.readline()
        return renglon

def cifra_cesar(cadena, llave):  # Cifra texto usando el cifrado César
    if llave < 0:
        llave = 26 - llave
    nuevaCadena = ""
    alfabeto = 'abcdefghijklmnopqrstuvwxyz'
    for l in cadena:  # Recorre cada letra
        if l in alfabeto:  # Si la letra está en el alfabeto
            posicionLetra = alfabeto.find(l)
            nuevaCadena += alfabeto[((posicionLetra + llave) % 26)]  # Cifra
        else:
            nuevaCadena += l  # No cifra
    return nuevaCadena

def descifra_cesar(cadena, llave):  # Descifra usando el cifrado César
    return cifra_cesar(cadena, 26 -llave)

def get_aciertos(listaPalabras, diccionario):  # Obtiene número de aciertos
    return sum(1 for palabra in listaPalabras if palabra in diccionario)  # Cuenta aciertos

palabras = carga_palabras()  # Carga el diccionario de palabras
cadena = carga_cifrado()  # Carga el texto cifrado
maxAciertos = 0  # Inicializa maxAciertos en 0
posibleLlave = 0  # Inicializa posibleLLave en 0

for cont in range(26):  # Prueba todas las llaves
    cadenaCifrada = descifra_cesar(cadena, cont)  # Descifra con la llave
    listaCifrada = cadenaCifrada.split()  # Divide el texto en palabras
    numAciertos = get_aciertos(listaCifrada, palabras)  # Cuenta aciertos
    if numAciertos > maxAciertos:  # Si hay más aciertos
        maxAciertos = numAciertos
        posibleLlave = 26 - cont  # Guarda mejor llave

print("La mejor llave es:", posibleLlave)  # Muestra la mejor llave
print("\nEl texto descifrado es:")
print(cifra_cesar(cadena, posibleLlave))  # Muestra texto descifrado
print("\n\tCheco estuvo aquí")  # Easter Egg