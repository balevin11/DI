import tkinter as tk

#función para cerrar la ventana
def cerrar_ventana():
    root.destroy()

#función para mostrar texto
def mostrar_mensaje():
   label.config(text="Bienvenido")

#crear la ventana principal
root = tk.Tk()
root.title("Ejercicio 2")
root.geometry("300x200")

#crear texto
label = tk.Label(root, text="")
label.pack()

#crear el boton que muestre el texo
button = tk.Button(root,text="Mostrar texto", command = mostrar_mensaje)
button.pack()

#crear el boton que cierre la ventana
button = tk.Button(root,text="Cerrar ventana", command = cerrar_ventana)
button.pack()

#ejecutar el bucle principal
root.mainloop()
