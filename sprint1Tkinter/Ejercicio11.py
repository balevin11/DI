import tkinter as tk


def actualizar(n):
 label.config(text="Valor: " + n)

#crear la ventana principal
root = tk.Tk()
root.title('Ejercicio 11')
root.geometry('300x200')

#crear scale
scale = tk.Scale(root, from_=0, to=100, orient="horizontal",
                 command=actualizar)
scale.pack()

#crear etiqueta
label = tk.Label(root, text='Valor: 0')
label.pack()

#ejecutar el bucle principal
root.mainloop()
