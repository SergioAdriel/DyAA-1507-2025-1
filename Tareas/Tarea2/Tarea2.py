def carga_palabras():  # Carga palabras desde el archivo
    with open('C:/Users/Adrie/OneDrive/Escritorio/GitHub/DyAA-1507-2025-1/Tareas/Tarea2/words.txt', 'r') as archivo:
        palabras = archivo.read().split()
        print(len(palabras), 'palabras leídas')  # Muestra la cantidad de palabras
    return palabras

def carga_cifrado():  # Carga texto cifrado desde el archivo
    with open('C:/Users/Adrie/OneDrive/Escritorio/GitHub/DyAA-1507-2025-1/Tareas/Tarea2/textoCifrado.txt', 'r') as archivo:
        return archivo.readline().strip()  # Elimina espacios en blanco

def cifra_cesar(cadena, llave):  # Cifra texto usando el cifrado César
    if llave < 0:  # Ajusta llave si es negativa
        llave = 26 - (abs(llave) % 26)  # Se asegura que sea positiva
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
    return cifra_cesar(cadena, 26 - llave)

def get_aciertos(listaPalabras, diccionario):  # Obtiene número de aciertos
    return sum(1 for palabra in listaPalabras if palabra in diccionario)  # Cuenta aciertos

dic1 = carga_palabras()  # Carga el diccionario de palabras
max_aciertos = 0  # Inicializa max_aciertos
mejor_llave = 0  # Inicializa mejor_llave
cadena = carga_cifrado()  # Carga el texto cifrado
for cont in range(26):  # Prueba todas las llaves
    cadenaCifrada = descifra_cesar(cadena, cont)  # Descifra con la llave
    listaCifrada = cadenaCifrada.split()  # Divide el texto en palabras
    numAciertos = get_aciertos(listaCifrada, dic1)  # Cuenta aciertos
    if numAciertos > max_aciertos:  # Si hay más aciertos
        max_aciertos = numAciertos
        mejor_llave = cont  # Guarda mejor llave

print("La mejor llave es:", 26 - mejor_llave)  # Muestra la mejor llave
print("\nEl texto descifrado es:")
print(descifra_cesar(cadena, mejor_llave))  # Muestra texto descifrado
print("\n\tCheco estuvo aquí")  # Easter Egg