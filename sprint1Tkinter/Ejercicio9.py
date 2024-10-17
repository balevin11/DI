import tkinter as tk
from tkinter import messagebox


def salir():
    root.quit()

def nueva_ventana():
    messagebox.showinfo("Nuevo", "Abrir una nueva ventana")

def mensaje_ayuda():
    messagebox.showinfo("Ayuda","Ejemplo de ayuda")

#crear la ventana principal
root = tk.Tk()
root.title('Ejercicio 9')
root.geometry('300x200')

#crear el menu principal
main_menu = tk.Menu(root)
root.config(menu=main_menu)

#crear submenú abrir
archive_menu = tk.Menu(main_menu, tearoff=0)
main_menu.add_cascade(label='Archivo', menu=archive_menu)
archive_menu.add_command(label='Abrir', command=nueva_ventana)
archive_menu.add_separator()
archive_menu.add_command(label='Salir', command=salir)

#crear submenú ayuda
help_menu = tk.Menu(main_menu, tearoff=0)
main_menu.add_cascade(label='Ayuda', menu=help_menu)
help_menu.add_command(label='Acerca de', command=mensaje_ayuda)

#ejecutar el bucle principal
root.mainloop()
