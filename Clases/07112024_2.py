# Importamos la librería tkinter para la interfaz gráfica y random para generar valores aleatorios.
import tkinter as tk
import random 

# Función para dibujar puntos y líneas en el canvas
def Dibujar():
    # Borra todo lo dibujado anteriormente en el canvas.
    canvas.delete('all')
    
    # Lista que almacenará las coordenadas de los puntos generados.
    puntos = []

    # Genera 10 puntos aleatorios en el canvas.
    for i in range(10):
        x = random.randint(20, 380)  # Genera una coordenada x entre 20 y 380
        y = random.randint(20, 380)  # Genera una coordenada y entre 20 y 380
        puntos.append((x, y))  # Agrega el punto (x, y) a la lista de puntos
        
        # Dibuja un círculo en la posición del punto para representarlo.
        canvas.create_oval(x-5, y-5, x+5, y+5, fill="blue")

    # Dibuja líneas entre los puntos en el orden en que fueron generados.
    for i in range(len(puntos) - 1):
        x1, y1 = puntos[i]
        x2, y2 = puntos[i + 1]
        canvas.create_line(x1, y1, x2, y2, fill="red")

# Configuración de la ventana principal.
ventana = tk.Tk()
ventana.title("Dibujo de Puntos y Líneas")

# Configuración del canvas, donde se dibujarán los puntos y las líneas.
canvas = tk.Canvas(ventana, width=400, height=400, bg="white")
canvas.pack()

# Botón que activa la función Dibujar.
boton = tk.Button(ventana, text="Dibujar", command=Dibujar)
boton.pack()

# Inicia el bucle principal de la ventana.
ventana.mainloop()