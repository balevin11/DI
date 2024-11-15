
import tkinter as tk
from controlador import GameController
from modelo import GameModel

if __name__ == '__main__':
    root = tk.Tk()
    root.geometry ("200x100")
    controller = GameController(root)
    root.mainloop()
#preguntas que hacer:
#start_timer realiza un registro de las veces que se reinicia?
