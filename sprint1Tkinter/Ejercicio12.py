import tkinter as tk
from tkinter import messagebox


def actualizar(n):
    label2.config(text="Edad " + n)

#insertar usuario en la lista
def nuevo_usuario():
    namme = name.get()
    years = age.get()
    genre = var_genre.get()
    users.insert(tk.END, namme + ", " + str(years) + ", " + genre)

#eliminar usuario de la lista
def eliminar_usuario():
    selection = users.curselection()
    if selection:
        for i in reversed(selection):
            users.delete(i)

def guardar():
    messagebox.showinfo("Nuevo", "Lista guardada")

def cargar():
    messagebox.showinfo("Nuevo", "Lista caragada")

#crear la ventana principal
root = tk.Tk()
root.title('Ejercicio 12')
root.geometry('700x500')

#pedir nombre
label1 = tk.Label(root, text='Nombre')
label1.grid(column=0, row=0)

name = tk.Entry(root)
name.place(x=100, y=0)

#pedir edad mediante un scale
age = tk.Scale(root, from_=0, to=100, orient="horizontal",
                 command=actualizar)
age.grid(column=0, row=1)

label2 = tk.Label(root, text='Edad: 0')
label2.grid(column=0, row=2)

#pedir genero mediante RadioButtons
var_genre = tk.StringVar()
var_genre.set("humano")

radio1 = tk.Radiobutton(root,text="Femenino", variable=var_genre,
                        value ="femenino")
radio1.grid(column=0, row=3)

radio2 = tk.Radiobutton(root,text="Masculino", variable=var_genre,
                        value ="masculino")
radio2.grid(column=0, row=4)

radio3 = tk.Radiobutton(root,text="Otro", variable=var_genre,
                        value ="otro")
radio3.grid(column=0, row=5)

#botón añadir usuario
button1 = tk.Button(root,text="Añadir usuario", command=nuevo_usuario)
button1.grid(column=0, row=6)

#lista de usuarios con su scrollbar
users = tk.Listbox(root, selectmode=tk.MULTIPLE)
users.grid(column=0, row=7, sticky="nsew")

scroll = tk.Scrollbar(root, orient="vertical", command=users.yview)
scroll.grid(column=1, row=7, sticky="ns")
users.config(yscrollcommand=scroll.set)

#botón eliminar usuario
button2 = tk.Button(root, text="Eliminar", command=eliminar_usuario)
button2.grid(column=0, row=8)

#boton cerrar programa
button3 = tk.Button(root, text="Salir", command=root.destroy)
button3.grid(column=0, row=9)

#crear menu de guardado y cargar
main_menu = tk.Menu(root)
root.config(menu=main_menu)

menu = tk.Menu(main_menu, tearoff=0)
main_menu.add_cascade(label='Menú', menu=menu)
menu.add_command(label='Guardar Lista', command=guardar)
menu.add_command(label='Cargar Lista', command=cargar)

#ejecutar el bucle principal
root.mainloop()
