import tkinter as tk

#funcion que personaliza el saludo (es necesario el get para distinguir
#entre widget entry y variable)"
def saludo():
    namee = name.get()
    label.config(text="Hola " + namee +". ¿Que tal estás?")

#crear la ventana principal
root = tk.Tk()
root.title('Ejercicio 3')
root.geometry('300x200')

#crear texto
label = tk.Label(root, text="")
label.pack()

#Introducir nombre
name = tk.Entry(root)
name.pack()

#crear el boton que muestre el saludo
button = tk.Button(root, text="Mostrar texto", command=saludo)
button.pack()

#ejecutar el bucle principal
root.mainloop()