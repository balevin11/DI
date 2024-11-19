import tkinter as tk
from controlador import GameController


if __name__ == '__main__':
    #crear ventana principal
    root = tk.Tk()
    root.geometry ("200x100")

    #crear controlador
    controller = GameController(root)

    #ejecutar el bucle principal
    root.mainloop()
