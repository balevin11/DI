import tkinter as tk


def mostrar():
    label3.config(text=text.get())

def no_mostrar():
    label3.config(text="")

#crear la ventana principal
root = tk.Tk()
root.title('Ejercicio 3')
root.geometry('300x200')

#crear los frames
frame1 = tk.Frame(root,  bg='lightgray')
frame1.pack(fill="both", expand=True)

frame2 = tk.Frame(root, bg='lightblue')
frame2.pack(fill="both", expand=True)

#crear etiquetas y entrada del frame 1
label1 = tk.Label(frame1, text='Etiqueta1', bg='lightgray')
label1.pack()

label2 = tk.Label(frame1, text='Etiqueta2', bg='lightgray')
label2.pack()

text = tk.Entry(frame1, bg='lightgray')
text.pack()

#crear etiqueta y botones del frame 2
label3 = tk.Label(frame2, text='', bg='lightblue')
label3.pack()

button = tk.Button(frame2, text='Mostrar etiqueta', command=mostrar,
                   bg='lightblue')
button.pack()

button = tk.Button(frame2, text='Ocultar etiqueta', command=no_mostrar,
                   bg='lightblue')
button.pack()

#ejecutar el bucle principal
root.mainloop()
