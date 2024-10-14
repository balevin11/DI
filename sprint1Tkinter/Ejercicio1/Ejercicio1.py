import tkinter as tk


#Creamos la función para cambiar el texto
def cambio_texto():
    label3.config(text="Texto 2")

#crear la ventana principal
root = tk.Tk()
root.title("Ejercicio 1")
root.geometry("300x200")

#crear los textos
label1 = tk.Label(root, text="Bienvenido")
label1.pack()
label2 = tk.Label(root, text="Kevin Cancelo")
label2.pack()
label3 = tk.Label(root, text="Texto 1")
label3.pack()

#crear el boton que invoque la funcion cambio_texto
button = tk.Button(root,text="      ", command = cambio_texto)
button.pack()

#ejecutar el bucle principal
root.mainloop()

