import tkinter as tk


#funcion para crear muchas lineas
def texto_largo():
    for i in range(1,100):
        text.insert(tk.END, "Linea" + str(i) + "\n")

#crear la ventana principal
root = tk.Tk()
root.title('Ejercicio 10')
root.geometry('600x400')

#crear texto
text =tk.Text(root, height=20, width=50, wrap="none")
text.grid(row=0,column=0, sticky='nsew')#grid da mayor control del layout

#crear scrollbar
scroll = tk.Scrollbar(root, orient="vertical", command=text.yview)
scroll.grid(row=0, column=1, sticky='ns')
text.config(yscrollcommand=scroll.set)#asignarle la scrollbar al texto

#rellenamos el texto
texto_largo()

#ejecutar el bucle principal
root.mainloop()
