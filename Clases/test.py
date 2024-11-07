import tkinter as tk
import random
import math

# Función para calcular la distancia entre dos puntos
def distancia(punto1, punto2):
    x1, y1 = punto1
    x2, y2 = punto2
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Función para encontrar la ruta utilizando el punto más cercano
def encontrar_ruta_cercana(puntos):
    ruta = []            # Arreglo para la ruta final (orden de los puntos visitados)
    no_visitados = puntos[:]  # Lista de puntos no visitados

    # Comenzamos desde el primer punto de la lista y lo agregamos a la ruta
    ruta.append(no_visitados.pop(0))

    # Recorremos hasta que todos los puntos hayan sido visitados
    while no_visitados:
        # Encuentra el punto no visitado más cercano al último punto en la ruta
        ultimo_punto = ruta[-1]
        punto_cercano = min(no_visitados, key=lambda punto: distancia(ultimo_punto, punto))
        
        # Agrega el punto más cercano a la ruta y lo elimina de los no visitados
        ruta.append(punto_cercano)
        no_visitados.remove(punto_cercano)

    return ruta

# Función para dibujar los puntos y la ruta más cercana en el canvas
def Dibujar():
    canvas.delete('all')
    puntos = []

    # Genera 10 puntos aleatorios en el canvas
    for i in range(10):
        x = random.randint(20, 380)
        y = random.randint(20, 380)
        puntos.append((x, y))
        
        # Dibuja un círculo en la posición del punto para representarlo
        canvas.create_oval(x-5, y-5, x+5, y+5, fill="blue")

    # Encuentra la ruta usando el algoritmo de punto más cercano
    ruta = encontrar_ruta_cercana(puntos)

    # Dibuja la ruta en el canvas
    for i in range(len(ruta) - 1):
        x1, y1 = ruta[i]
        x2, y2 = ruta[i + 1]
        canvas.create_line(x1, y1, x2, y2, fill="red", width=2)

# Configuración de la ventana principal
ventana = tk.Tk()
ventana.title("Problema del Viajero: Ruta Más Cercana")

# Configuración del canvas donde se dibujarán los puntos y la ruta
canvas = tk.Canvas(ventana, width=400, height=400, bg="white")
canvas.pack()

# Botón que activa la función Dibujar
boton = tk.Button(ventana, text="Dibujar Ruta Más Cercana", command=Dibujar)
boton.pack()
  
# Inicia el bucle principal de la ventana
ventana.mainloop()
