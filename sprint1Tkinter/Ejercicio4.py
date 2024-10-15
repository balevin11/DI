import tkinter as tk

#crear funcion para la etiqueta
def aficiones():
    #controlar que checkButtons estan activos y guardarlos en variables
    if read_var.get():
        read = " leer"
    else:
        read = ""
    if music_var.get():
        music = " música"
    else:
        music = ""
    if sport_var.get():
        sport = " deporte"
    else:
        sport = ""

    #modificar la etiqueta con los checkbutton elegidos
    label.config(text="Aficiones:" + read + music + sport)




#crear la ventana principal
root = tk.Tk()
root.title('Ejercicio 3')
root.geometry('300x200')


#crear las variables CheckButton
read_var = tk.BooleanVar()
music_var = tk.BooleanVar()
sport_var = tk.BooleanVar()

#crear checkButtons
check = tk.Checkbutton(root,text="Leer", variable=read_var, command=aficiones)
check.pack()

check2 = tk.Checkbutton(root,text="Música", variable=music_var, command=aficiones)
check2.pack()

check3 = tk.Checkbutton(root,text="Deporte", variable=sport_var, command=aficiones)
check3.pack()

#crear la etiqueta
label = tk.Label(root, text="Aficiones:")
label.pack()

#ejecutar el bucle principal
root.mainloop()