import tkinter as tk


def fondo():
    #segun el radioButton seleccionado cambiamos los fondos
    if var_radio.get() == "rojo":
        root.config(bg="red")
        radio1.config(bg="red")
        radio2.config(bg="red")
        radio3.config(bg="red")
    elif var_radio.get() == "verde":
        root.config(bg="green")
        radio1.config(bg="green")
        radio2.config(bg="green")
        radio3.config(bg="green")
    elif var_radio.get() == "azul":
        root.config(bg="blue")
        radio1.config(bg="blue")
        radio2.config(bg="blue")
        radio3.config(bg="blue")

#crear la ventana principal
root = tk.Tk()
root.title('Ejercicio 3')
root.geometry('300x200')


#crear la variable para el RadioButton
var_radio = tk.StringVar()
var_radio.set("blanco") #valor iniciar para evitar errores

#crear radioButtons
radio1 = tk.Radiobutton(root,text="Rojo", variable=var_radio, value ="rojo", command=fondo)
radio1.pack()

radio2 = tk.Radiobutton(root,text="Verde", variable=var_radio, value ="verde",  command=fondo)
radio2.pack()

radio3 = tk.Radiobutton(root,text="Azul", variable=var_radio, value ="azul",  command=fondo)
radio3.pack()


#ejecutar el bucle principal
root.mainloop()