import tkinter as tk

#crear funcion para la etiqueta
def aficiones():
    #controlar que checkButtons estan activos y guardarlos en variables
    if leer_var.get():
        leer = " leer"
    else:
        leer = ""
    if musica_var.get():
        musica = " musica"
    else:
        musica = ""
    if deporte_var.get():
        deporte = " deporte"
    else:
        deporte =""

    #modificar la etiqueta con los checkbutton elegidos
    label.config(text="Aficiones:"+leer+musica+deporte)




#crear la ventana principal
root = tk.Tk()
root.title('Ejercicio 3')
root.geometry('300x200')


#crear las variables CheckButton
leer_var = tk.BooleanVar()
musica_var = tk.BooleanVar()
deporte_var = tk.BooleanVar()

#las inicializamos
check = tk.Checkbutton(root,text="Leer", variable=leer_var, command=aficiones)
check.pack()
check2 = tk.Checkbutton(root,text="Música", variable=musica_var, command=aficiones)
check2.pack()
check3 = tk.Checkbutton(root,text="Deporte", variable=deporte_var, command=aficiones)
check3.pack()

#crear la etiqueta
label = tk.Label(root, text="Aficiones:")
label.pack()

#ejecutar el bucle principal
root.mainloop()