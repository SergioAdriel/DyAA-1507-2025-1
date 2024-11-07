import tkinter as tk

def Saludar(): # Este metodo es para agregar una accion al boton
    print("Hola, nenas")
# Estos metodos se llaman Widgets
ventana = tk.Tk()
ventana.title("Ventana")  # Se modifican los atrbutos como si fuese una clase
ventana.geometry("400x300")
etiqueta1=tk.Label(ventana, text="Hola") # Donde la vamos a poner y que texto va a tener
etiqueta1.pack() # lo agregamos a la ventana
boton1=tk.Button(ventana, text="Click Aquí", command=Saludar) # Mandar a llamar las funciones pero sin parentesis 
boton1.pack() # lo agregamos a la ventana
entrada1=tk.Entry(ventana) # Caja para texto
entrada1.pack()

ventana.mainloop()