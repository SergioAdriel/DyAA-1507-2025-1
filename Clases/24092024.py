def cifra_sustituye(cad, llave):
    alfabeto = "abcdefghijklmnopqrstuvwxyz"
    cifrada = ""
    for c in cad:
        if c in alfabeto:
            pos = alfabeto.index(c)
            cifrada += llave[pos]
        else:
            cifrada += c
    return cifrada

llave = 'oveflztrsmaiwgexqjpbuynhkd'
texto = "hola"
print(cifra_sustituye(texto, llave))
