import tkinter as tk


def mostrar_selecciones():
    selection = listBox.curselection()#recogemos los elementos marcado
    elements = [listBox.get(i) for i in selection]#los guardamos
    label.config(text="Seleccionaste: " + ', '.join(elements))
# ', '.lista sirve para poner una coma entre los objetos de la lista

#crear la ventana principal
root = tk.Tk()
root.title('Ejercicio 6')
root.geometry('300x200')

#creamos nuestra lista de opciones
options = ["Manzana", "Banana", "Naranja"]

#crear ListBox
listBox = tk.Listbox(root,selectmode=tk.MULTIPLE)
for option in options:
    listBox.insert(tk.END, option)
listBox.pack()

#boton para mostrar elecciones
button = tk.Button(root, text="Mostrar selecciones",
                   command=mostrar_selecciones)
button.pack()

#crear la etiqueta
label = tk.Label(root, text="")
label.pack()

#ejecutar el bucle principal
root.mainloop()
