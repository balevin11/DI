import tkinter as tk

def crear():
    #pasamos los entry a variables
    xa = float(positionxa.get())
    ya = float(positionya.get())
    xb = float(positionxb.get())
    yb = float(positionyb.get())

    #controlamos fuera de rango
    if (xa > 300 or ya > 300 or xb > 300 or yb > 300 or xa < 0 or
            ya < 0 or xb < 0 or yb < 0):
        label_error.config(text="Error, algún valor fuera de rango "
                                + "(Rango de 0 a 300)")
    else:
        #dibujamos rectangulo y círculo
        canvas.create_rectangle(xa, ya, xb, yb, width=1,
                                outline='black')
        canvas.create_oval(xa, ya, xb, yb, width=1, outline='black')
        label_error.config(text="")


#crear la ventana principal
root = tk.Tk()
root.title('Ejercicio 7')
root.geometry('700x700')

#crear el canvas
canvas = tk.Canvas(root, width=300, height=300, bg='white')
canvas.pack()

#solicitar puntos x e y con sus respectivas etiquetas
labela = tk.Label(root, text='Punto A')
labela.pack()

labelxa = tk.Label(root, text='Valor x:')
labelxa.pack()

positionxa = tk.Entry(root)
positionxa.pack()

labelya = tk.Label(root, text='Valor y:')
labelya.pack()

positionya = tk.Entry(root)
positionya.pack()

labelb = tk.Label(root, text='Punto B')
labelb.pack()

labelxb = tk.Label(root, text='Valor x:')
labelxb.pack()

positionxb = tk.Entry(root)
positionxb.pack()

labelyb = tk.Label(root, text='Valor y:')
labelyb.pack()

positionyb = tk.Entry(root)
positionyb.pack()

#creamos una etiqueta para el error
label_error = tk.Label(root, text='')
label_error.pack()

#crear boton para crear rectangulo
button = tk.Button(root, text='Crear rectángulo', command=crear)
button.pack()

#ejecutar el bucle principal
root.mainloop()
